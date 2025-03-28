from typing									import Any
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import patronus
from pygwarts.filch.nettherin				import is_valid_ip4
from pygwarts.filch.transportclaw			import is_valid_port








class SNMPtrap(Transmutable):

	"""
		Application layer class for serving SNMP notifications.
		Must accept setup positional arguments:
			listen_ip	- ip4 address to listen for notifications, as string;
			listen_port	- port number to listen for notifications, as int;
			trap		- callable that must accept "listen_ip" and "listen_port", along with any
						additional flags as **kwargs, and establish the actual listener.
		Once "listen_ip" and "listen_port" validated, the "trap" invocation starts. It must be
		maintained by the "trap" all the logic for SNMP processing and also the working time.
		When "trap" will be called all keyword arguments from current object __call__ will be
		passed to it, so this is the way for regulating "trap" from outside. Any Exception during
		"trap" working time will be caught and logged, and this will cause "trap" to stop.
	"""

	def __call__(
					self,
					listen_ip	:str,
					listen_port	:int,
					trap		:Callable[[Any],None],
					**kwargs
				):

		if	is_valid_ip4(listen_ip):
			if	is_valid_port(listen_port):


				self.listen_ip = listen_ip
				self.listen_port = listen_port


				self.loggy.info(f"Establishing SNMP trap at {self.listen_ip}:{self.listen_port}")
				for k,v in kwargs.items() : self.loggy.debug(f"Using {k}: {v}")


				try:	trap(self.listen_ip, self.listen_port, **kwargs)
				except	Exception as E: self.loggy.error(f"{self} got {patronus(E)}")
				else:	self.loggy.info(f"{self.listen_ip}:{self.listen_port} SNMP trap discarded")


			else:	self.loggy.debug("Listen port verification failed")
		else:		self.loggy.debug("Listen ip verification failed")







