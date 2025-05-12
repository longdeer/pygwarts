from typing						import List
from time						import sleep
from threading					import Thread
from multiprocessing			import current_process
from pygwarts.magical.spells	import flagrate
from pygwarts.irma.contrib		import LibraryContrib








class ContribInterceptor:

	"""
		LibraryContrib decorators super class. Implements the mutable chain injection for a LibraryContrib
		type or object, with "CONTRIB_HOOK" field and it's corresponding processing in decoration time.
		As decorated layer in __init__ must be either LibraryContrib or it's another decorator,
		"CONTRIB_HOOK" will help recognize proper entities.
	"""

	CONTRIB_HOOK = True

	def __init__(self, layer :LibraryContrib) -> LibraryContrib :

		match layer:

			case	LibraryContrib(): self.layer = layer
			case	type() if getattr(layer, "CONTRIB_HOOK", None): self.layer = layer
			case	object() if getattr(layer, "CONTRIB_HOOK", None): self.layer = layer()
			case _:	raise TypeError(f"Intercepting invalid object \"{layer}\"")








class STDOUTL(ContribInterceptor):

	"""
		LibraryContrib decorator, that overwrites following LibraryContrib level methods:
			"info",
			"warning",
			"error",
			"critical",
		to intercept messages and put it to the standard output (print it) before return
		to the LibraryContrib corresponding level method. If "handover_name" is available, it will
		be precede the message in standard output.
	"""

	def __call__(self):
		class Interceptor(self.layer):

			def info(self, message :str):

				print(

					"%sINFO : %s"%(

						f"{self.handover_name} " if self.handover_name is not None else "",
						message
					)
				)
				return super().info(message)

			def warning(self, message :str):

				print(

					"%sWARNING : %s"%(

						f"{self.handover_name} " if self.handover_name is not None else "",
						message
					)
				)
				return super().warning(message)

			def error(self, message :str):

				print(

					"%sERROR : %s"%(

						f"{self.handover_name} " if self.handover_name is not None else "",
						message
					)
				)
				return super().error(message)

			def critical(self, message :str):

				print(

					"%sCRITICAL : %s"%(

						f"{self.handover_name} " if self.handover_name is not None else "",
						message
					)
				)
				return super().critical(message)


		return	Interceptor








class PoolHoist(ContribInterceptor):

	"""
		LibraryContrib main decorator, that implements the hoisting of any strings, which are considered
		to got through the decorated LibraryContrib object, to the pool of threads. Basically strings
		are the logging messages, hoisting is actual intercepting of them on order to put in special
		buffer and pool of threads is the schedule of such buffer termination methods calls. By default
		"PoolHoist" doesn't implement the actual hoist, only the buffer and pool communication, so
		it is possible to construct any level hoisting within other objects, either decorators or even
		in mutable chain. The process of pool interaction releis on following methods:
			buffer_insert	- the method to be invoked for actual intercepting; will accept the message
							string and will maintain the buffer and pool insertion; in total, this method
							must be called for every string that is intended to be hoisted;
			buffer_release	- the method that is a buffer terminator; it is always invoked in a thread
							to implement delayed buffer comparison; as this method returns terminated
							buffer, the best idea is to overwrite it in any descent decorator, or even
							in direct inheritance.
		For every message to be inserted in buffer a unique id number is created to escort it. For the
		very first message hoist, when the buffer is first time extended, the process of buffering is
		turned on and special field's "POOL_STATE" first bit set to 1 will indicate it. Along with it
		the thread with buffer terminator is started, which will delay the actual termination by
		"POOL_TIMER" seconds every time the buffer will be altered. This delay is limited by "POOL_LIMIT".
		All messages hoisting during "buffering" will be the buffer altering that will cause delay. After
		some time that not exceeds "POOL_LIMIT" seconds and buffer changing stopped, or after "POOL_LIMIT"
		exceed, the buffer will terminated.
	"""


	def __call__(self):
		class Interceptor(self.layer):


			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)


				self.POOL_TIMER	= getattr(super(), "pool_timer", 5)
				self.POOL_LIMIT	= getattr(super(), "pool_limit", 50)
				self.POOL_NAME	= current_process().name
				self.POOL_STATE	= int()
				self.POOL_SET	= set()
				self.BUFFER		= list()




			@property
			def BL(self): return len(self.BUFFER)
			def buffer_insert(self, message :str):

				"""
					Main method, that takes any string, that considered as some message, for example
					emitted at any log level higher than debug, and puts it in the pool with "pool_insert"
					method. For every "buffer_insert" call the unique number "POOL_ID" is created to serve
					as unique identifier for current "message". This "POOL_ID" will be first used to locate
					current pool with "pool_locate" method, which might wipe the whole buffer. After pool
					location the "BUFFER" list will be extended with current "message", along with insertion
					into the pool with "pool_insert" method. "POOL_SET" will be also maintained and all
					messages will be first check if it is already in it, so duplicates will be skipped.
				"""

				if	isinstance(message, str) and (mlen := len(message)) and message not in self.POOL_SET:
					P = self.pool_get_new_id()


					self.pool_locate(P)
					self.POOL_SET.add(message)
					self.BUFFER.append(message)


					self.pool_debug(f"(pool-id-{P}) {mlen} symbol{flagrate(mlen)} message inserted")
					self.pool_debug(f"(pool-id-{P}) buffer extended to {self.BL} item{flagrate(self.BL)}")
					self.pool_insert(P)




			def buffer_release(self, P :int) -> List[str] :

				"""
					Main method that acts as a buffer terminator. When invoked it is assumed that "BUFFER"
					was altered to have the first message, so the cycle of buffer comparison is started.
					This cycle checks the buffer size and buffer time, which both are set to "BUFFER" items
					count and "POOL_TIMER" seconds corresponding. On every iteration of cycle, after the
					"POOL_TIMER" timeout the buffer size again is set to "BUFFER" items count and buffer
					time incremented by "POOL_TIMER". The cycle goes on this way until either buffer size
					will have no changes between iterations, or the buffer time exceeds "POOL_LIMIT" seconds.
					When the cycle ends, "POOL_STATE" first bit will be set to 0 to inform that buffering
					is over. The "POOL_SET" and "BUFFER" will be wiped and it's content will be returned.
				"""

				buffer_size = 0
				buffer_time = 0


				while buffer_size <self.BL and buffer_time <self.POOL_LIMIT:


					buffer_size = self.BL
					buffer_time += self.POOL_TIMER


					sleep(self.POOL_TIMER)
					if self.POOL_TIMER <buffer_time : self.pool_debug(f"(pool-id-{P}) timer extended")


				self.pool_debug(f"(pool-id-{P}) was {buffer_time} second{flagrate(buffer_time)}")
				self.pool_debug(f"(pool-id-{P}) was {buffer_size} item{flagrate(buffer_size)}")


				self.POOL_STATE |= 1
				self.POOL_STATE ^= 1


				buffer_dump	= self.BUFFER


				self.POOL_SET = set()
				self.BUFFER	= list()


				return	buffer_dump








			def pool_debug(self, message :str):

				"""
					PoolHoist inner debug message emitter. Implements the Transmutable style of logging,
					when it is "handovered" the "loggy" object, which in this situation is itself, and
					then emits message. The handovered name in this case is not taken from any layer object
					as in mutable chain, but is strictly defined as "loggy.pool". As any overwriting of
					"debug" method functionality will affect current inner logging method, and as debug
					flow might be extremely vast, the best idea is to never intercept it.
				"""

				self.handover("loggy.pool", assign=False)
				self.debug(message)




			def pool_get_new_id(self) -> int :

				"""
					Helper method that maintains the generation of unique id numbers to be used for
					pool operations. Starts with 0 and increments every time called.
				"""

				current_id = getattr(self, "POOL_ID_GENERATOR", 0)
				self.POOL_ID_GENERATOR = current_id +1

				return current_id




			def pool_insert(self, P :int):

				"""
					The crucial method of pool, which serves as a thread dispatcher. Accepts the unique
					pool id number "P" and first of all checks if there is any already started thread by
					"POOL_STATE" 1 bit set. If 1 bit set it means the "buffering" state and all messages
					must be handled by already started thread. Otherwise the "P" id will be used with
					new thread start. The new thread starts the "buffer_release" method which will gather
					messages while "buffering" is on.
				"""

				if	self.POOL_STATE &1 == 0:
					self.POOL_STATE ^= 1

					self.pool_debug(f"(pool-id-{P}) starting new thread")
					Thread(target=self.buffer_release, kwargs={ "P": P }).start()




			def pool_locate(self, P :int):

				"""
					Core method that allows to detect pool migration between processes. If the process
					where PoolHoist was originally started will be forked, which will be detected by process
					name changes, when the parent process had thread started, it means the child process will
					inherit the "POOL_STATE" set to "buffering", which means there is already working thread.
					But when such thread, which is "buffer_release" method, will be stopped, it will happen
					only in parent process and the child "POOL_STATE" will stay the same. That will restrict
					thread starting in child process. This method solves this by locating current process
					and managing "POOL_STATE" when forked. Also the inherited buffer and set will be wiped.
					Accepts the unique pool id number "P" to be used for maintaining.
				"""

				if	(current_name := current_process().name) != self.POOL_NAME :

					self.pool_debug(f"(pool-id-{P}) switching from {self.POOL_NAME} to {current_name}")
					self.pool_debug(f"(pool-id-{P}) wiping {self.BL} item{flagrate(self.BL)} buffer")

					self.POOL_STATE |= 1
					self.POOL_STATE ^= 1

					self.POOL_NAME	= current_name
					self.BUFFER		= list()
					self.POOL_SET	= set()


		return	Interceptor







