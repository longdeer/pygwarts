from pygwarts.irma.access.volume	import LibraryVolume
from pygwarts.irma.access.handlers	import AccessHandler








class AccessCounter(AccessHandler):

	"""
		Implementation of handler, that upon invocation does only two things:
			1. AccessHandlerCounter job - increments "access_handler_counter" field;
			2. AccessHandlerRegisterCounter job - increments it's "counter" integer mapping in
			LibraryVolume object "volume".
		Always returns True.
	"""

	def __call__(self, line :str, volume :LibraryVolume) -> True :

		self.access_handler_counter = getattr(self, "access_handler_counter", 0) +1
		self.loggy.debug(f"Handler counter incremented to {self.access_handler_counter}")

		if	self.registered(volume):

			volume[self].setdefault("counter",0)
			volume[self]["counter"] += 1
			self.loggy.debug(f"{volume} counter incremented to {volume[self]['counter']}")


		return True







