from typing									import Any
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.irma.access.bookmarks			import VolumeBookmark
from pygwarts.irma.access.handlers			import AccessHandler
from pygwarts.irma.access.volume			import LibraryVolume








class AccessInducer(Transmutable):

	"""
		irma.access core super class for inducing results of access to library. In other words, this object
		is to process all data, gathered during access to library, and produce some report as a string.
		Must be declared under corresponding AccessHandler object, which data will be Induced. In turn
		the AccessHandler object above must be declared under VolumeBookmark object, which will be the
		end point for both, so all data will be anyway stored right there. Basically AccessInducer object
		must do the following upon being called:
			1. access either AccessHandler or LibraryVolume object it assigned to;
			2. process required data the way it supposed to;
			3. induce the result as a string.
		Any inducer must implement it's __call__ which will accept the only argument LibraryVolume object
		as a source file representation, will do some desired processing on the data fetched and will
		return exactly string or None. It is the originally designed idea to return only string, cause
		the default processing of inducers in VolumeBookmark.view method relies on concatenation of
		inducers strings.
	"""

	__call__ :Callable[[LibraryVolume],str | None]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		if	isinstance(handler := getattr(self, "_UPPER_LAYER", None), AccessHandler):
			if	isinstance(booklink := getattr(handler, "_UPPER_LAYER", None), VolumeBookmark):


				booklink(self, "inducer")
				self.loggy.debug(f"Assigned to {booklink} bookmark as {handler} inducer")


			else:	self.loggy.info(f"AccessInducer {self} not assigned to any bookmark")
		else:		self.loggy.info(f"AccessInducer {self} not registered to any handler")




	def get_handler_counter(self) -> int | None :

		"""
			Helper method that accesses the AccessHandler object it is assigned to, so it must be it's
			"_UPPER_LAYER", and returns it's "access_handler_counter" attribute, which must be integer
			that represents the counter for AccessHandler invocations. Returns None if either current
			AccessInducer object assigned not to AccessHandler, or if AccessHandler has no or not integer
			"access_handler_counter".
		"""

		if	isinstance(handler := getattr(self, "_UPPER_LAYER", None), AccessHandler):
			if	isinstance(handler_counter := getattr(handler, "access_handler_counter", None), int):


				self.loggy.debug(f"Found {handler} access handler counter {handler_counter}")
				return handler_counter
		else:	self.loggy.debug(f"Not registered to any handler")




	def get_register_counter(self, volume :LibraryVolume) -> int | None :

		"""
			Helper method that accesses provided "volume" argument LibraryVolume object with AccessHandler
			object it is assigned to, so it must be it's "_UPPER_LAYER", and returns corresponding mapped
			"counter" value, which must be integer that represents the counter of AccessHandler invocations
			for exactly "volume" object. Returns None if either current AccessInducer object assigned not
			to AccessHandler or "volume" is not LibraryVolume object, or if AccessHandler has no or not
			integer "counter" mapping in "volume".
		"""

		if	isinstance(handler := getattr(self, "_UPPER_LAYER", None), AccessHandler):
			if	isinstance(volume, LibraryVolume) and isinstance(vollink := volume[handler], dict):
				if	isinstance(register_counter := vollink.get("counter"), int):


					self.loggy.debug(f"Found {handler} register counter {register_counter}")
					return register_counter
			else:	self.loggy.debug(f"Handler {handler} not registered to volume {volume}")
		else:		self.loggy.debug(f"Not registered to any handler")




	def get_register_recap(self, volume :LibraryVolume) -> Any | None :

		"""
			Helper method that accesses provided "volume" argument LibraryVolume object with AccessHandler
			object it is assigned to, so it must be it's "_UPPER_LAYER", and returns corresponding mapped
			"recap" value, which might be any type and represents the object AccessHandler maintains for
			"volume". Returns None if either current AccessInducer object assigned not to AccessHandler
			or "volume" is not LibraryVolume object, or if AccessHandler has no or None "recap" mapping
			in "volume".
		"""

		if	isinstance(handler := getattr(self, "_UPPER_LAYER", None), AccessHandler):
			if	isinstance(volume, LibraryVolume) and isinstance(vollink := volume[handler], dict):
				if	(handler_recap := vollink.get("recap")) is not None:


					self.loggy.debug(f"Found {handler} recap of {type(handler_recap)}")
					return handler_recap
			else:	self.loggy.debug(f"Handler {handler} not registered to volume {volume}")
		else:		self.loggy.debug(f"Not registered to any handler")







