from typing												import Literal
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import Transmutation
from pygwarts.magical.spells							import geminio
from pygwarts.irma.access.bookmarks						import VolumeBookmark
from pygwarts.irma.access.volume						import LibraryVolume








class AccessHandler(Transmutable):

	"""
		irma.access core super class for processing library volumes. In other words this object is to
		gather, or handle, all data during access to library. The handling of data means processing
		some strings in order to obtain information. Every AccessHandler must be declared under it's
		VolumeBookmark object, in order to be assigned to it, which in turn will be accessed by
		LibraryVolume objects. Every AccessHandler must define it's __call__ method, which must accept
		two arguments - the string to be handled, which is as line of some text, and corresponding
		LibraryVolume object as the text source. The result of lines processing must be stored in
		LibraryVolume object, so it might be further accessed by inducers.
	"""

	__call__ :Callable[[str,LibraryVolume], Literal[True] | None]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		if	isinstance(booklink := getattr(self, "_UPPER_LAYER", None), VolumeBookmark):

			booklink(self, "handler")
			self.loggy.debug(f"Assigned to {booklink} bookmark")
		else:
			self.loggy.info(f"AccessHandler {self} not assigned to any bookmark")




	def registered(self, volume :LibraryVolume) -> Literal[True] | None :

		"""
			Helper method that ensures "volume" is a LibraryVolume object which either already has
			dictionary mapping for current AccessHandler object or it might be created, so True will
			be returned in those two only cases. Returns None if "volume" is different type or if it
			is LibraryVolume object with other than dictionary mapping for current AccessHandler.
		"""

		if	isinstance(volume, LibraryVolume):
			match volume[self]:

				case dict()	: pass
				case None	: volume[self] = dict()
				case _:

					self.loggy.debug(f"Invalid mapping in {volume} volume")
					return
			return	True








class AccessHandlerCounter(Transmutation):

	"""
		AccessHandler utility decorator, that counts decorated AccessHandler invocations. In mutable
		chain acts as a mutation - takes decorated AccessHandler class and rewrites it's __call__
		the way with every invocation the special "access_handler_counter" field will be incremented.
		Doesn't influence decorated __call__ invocation, neither handles possible Exception.
	"""

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :
		class Handler(geminio(layer)):

			def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

				self.access_handler_counter = getattr(self, "access_handler_counter", 0) +1
				self.loggy.debug(f"Handler counter incremented to {self.access_handler_counter}")

				return super().__call__(line, volume)
		return	Handler








class AccessHandlerRegisterCounter(Transmutation):

	"""
		AccessHandler utility decorator, that counts decorated AccessHandler invocations for provided
		LibraryVolume object "volume". In mutable chain acts as a mutation - takes decorated AccessHandler
		class and rewrites it's __call__ the way with every successful invocation, which is defined by
		truly return of decorated __call__, the "counter" integer mapping for current AccessHandler in
		LibraryVolume object "volume" will be incremented. Doesn't influence decorated __call__ invocation,
		neither handles possible Exception.
	"""

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :
		class Handler(geminio(layer)):

			def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

				if	(handle := super().__call__(line, volume)):
					if	isinstance(vollink := volume[self], dict):


						# It is assumed decorated AccessHandler call already mapped itself in a volume,
						# so setting "counter" mapping in it may proceed. It also will serve as a guard
						# to not count if mapping not set.
						vollink.setdefault("counter",0)
						vollink["counter"] += 1
						self.loggy.debug(f"{volume} counter incremented to {vollink['counter']}")


					else:	self.loggy.debug(f"{volume} counter link was not created")
					return	handle
		return		Handler







