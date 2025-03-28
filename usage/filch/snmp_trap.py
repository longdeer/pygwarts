from typing								import Any
from typing								import List
from typing								import Dict
from typing								import Tuple
from typing								import Callable
from sys								import exc_info
from time								import time
from asyncore							import loop
from traceback							import format_exception
from pygwarts.irma.contrib				import LibraryContrib
from pygwarts.filch.apppuf.snmp			import SNMPtrap
from pysnmp.entity						import config
from pysnmp.entity.engine				import SnmpEngine
from pysnmp.entity.rfc3413				import ntfrcv
from pysnmp.carrier.asyncore.dgram		import udp
from pysnmp.carrier.asyncore.dispatch	import AsyncoreDispatcher as ScapyDispatcher
from pysnmp.smi							import builder
from pysnmp.smi							import view
from pysnmp.smi.rfc1902					import ObjectType
from pysnmp.smi.rfc1902					import ObjectIdentity
from pysnmp.proto.rfc1902				import ObjectName
from pysnmp.proto.rfc1902				import OctetString
from pysnmp.error						import PySnmpError








class Filch(SNMPtrap):
	class loggy(LibraryContrib):

		handler		= "file handler path (optional)"
		init_name	= "filch (optional)"

	def __init__(self):
		super().__init__()

		class AsyncoreDispatcher(ScapyDispatcher):
			def runDispatcher(self, kill_timer :int):

				start = time()

				while self.jobsArePending() or self.transportsAreWorking():
					tick = time()

					if		kill_timer <tick - start : break
					try:	loop(self.getTimerResolution(), use_poll=True, map=self.__sockMap, count=1)
					except	KeyboardInterrupt : raise
					except:	raise PySnmpError("poll error: %s"%";".join(format_exception(*exc_info())))

					self.handleTimerTick(tick)

		self.dispatcher = AsyncoreDispatcher
		self.builder	= builder.MibBuilder()
		self.viewer		= view.MibViewController(self.builder)
		self.handlers	= list()

	def trap(self, listen_ip :str, listen_port :int, listen_time :int, community :str, community_i :str):

		ENGINE = SnmpEngine()
		ENGINE.registerTransportDispatcher(self.dispatcher())
		self.loggy.debug(f"Registered dispatcher {ENGINE.transportDispatcher}")

		config.addTransport(

			ENGINE,
			udp.domainName + ( 1, ),
			udp.UdpTransport().openServerMode(( listen_ip,listen_port ))
		)
		self.loggy.debug(f"UDP transport established for {listen_ip}:{listen_port}")

		config.addV1System(ENGINE, community_i, community)
		nr = ntfrcv.NotificationReceiver(ENGINE, self.callback)
		self.loggy.debug(f"Registered receiver {nr}")

		try:

			self.loggy.debug("Starting dispatcher")
			ENGINE.transportDispatcher.jobStarted(1)
			ENGINE.transportDispatcher.runDispatcher(listen_time)

		finally:

			self.loggy.debug("Closing dispatcher")
			ENGINE.transportDispatcher.closeDispatcher()


	def add_handler(self, handler :Callable[[Tuple[str,str,str,str,str,str,str]],None]):

		if	callable(handler):

			self.handlers.append(handler)
			self.loggy.debug(f"Appended handler {handler}")


	def get_modules(self, sources :List[str], modules :List[str]):

		self.builder.addMibSources(*( builder.DirMibSource(S) for S in sources ))
		self.builder.loadModules(*modules)

		module_name	= self.viewer.getFirstModuleName()

		while True:

			if		module_name : self.loggy.info(f"Loaded module {module_name}")
			try:	module_name = self.viewer.getNextModuleName(module_name)
			except:	break


	def callback(
					self,
					engine				:SnmpEngine,
					state_reference		:int,
					context_engine_id	:OctetString,
					context_name		:OctetString,
					bind_variables		:List[Tuple[ObjectName,Any]],
					cbCtx				:Any,
				)-> Dict[str,List[str]]	:

		context = engine.observer.getExecutionContext("rfc3412.receiveMessage:request")
		SRC = context["transportAddress"][0]
		self.loggy.debug(f"Callback on {SRC} trap")

		for name, value in bind_variables:

			rfcobj = ObjectType(ObjectIdentity(name), value).resolveWithMib(self.viewer)
			NMOD, NSYM, NIND = rfcobj[0].getMibSymbol()

			try:	NIND = NIND[0]
			except:	pass

			try:	VMOD, VSYM, VIND = rfcobj[1].getMibSymbol()
			except:	VMOD, VSYM, VIND = str(), str(rfcobj[1]), str()

			current = (

				str(SRC),
				str(NMOD), str(NSYM), str(NIND),
				str(VMOD), str(VSYM),
				str(VIND) if VIND else str()
			)

			self.loggy.debug(f"Trap summary: {current}")

			for handler in self.handlers:

				self.loggy.debug(f"Invoking handler {handler}")
				handler(current)








if	__name__ == "__main__":

	filch = Filch()
	filch.add_handler(Callable[[Tuple[str,str,str,str,str,str,str]],None])
	filch.add_handler(Callable[[Tuple[str,str,str,str,str,str,str]],None])
	filch.add_handler(Callable[[Tuple[str,str,str,str,str,str,str]],None])
	filch.get_modules(

		[ "path to precomputed MIB files" ],
		[ "MIB to include", "MIB to include", "MIB to include" ]
	)

	filch(
			"ip4 address to listen",		# Address where trap will be caught
			54321,							# Port number where trap will be caught
			filch.trap,						# Inner callback method
			listen_time=100,				# Time for trap to be active
			community="community name",		# v1 community name
			community_i="community idnex"	# v1 community name index
		)







