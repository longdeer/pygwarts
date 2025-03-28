from typing							import Optional
from typing							import Callable
from pygwarts.irma.access.inducers	import AccessInducer
from pygwarts.irma.access.volume	import LibraryVolume








class HandlerCounterInducer(AccessInducer):

	"""
		Implementation of inducer, that accesses the AccessHandler object it is assigned to and returns
		it's "access_handler_counter" attribute, which must be integer that represents the counter for
		AccessHandler invocations. Processes obtained value with special field "filter", which must be
		callable that accepts two arguments - current AccessInducer object and the value it processing.
		It is must be noted, that "filter" invocation implemented according to "filter" assigned during
		declaration of AccessInducer class, so it is instantiated. If "filter" will be assigned to already
		instantiated AccessInducer object, it must account for accepting the value argument only. It doesn't
		restricted for "filter" what value to return, cause it anyway will be converted to string. Returns
		either obtained, and perhaps processed, value if it is originally not None or "filter" returned
		not None. Otherwise returns None. There is no Exception handling for "filter" invocation.
	"""

	filter :Optional[Callable[[AccessInducer,int],int | None]]

	def __call__(self, volume :LibraryVolume) -> str | None :
		if	isinstance((counter := self.get_handler_counter()), int):

			if		callable(getattr(self, "filter", None)): counter = self.filter(counter)
			else:	self.loggy.debug("Filter not applied")
			if		counter is not None : return str(counter)








class RegisterCounterInducer(AccessInducer):

	"""
		Implementation of inducer, that accesses provided "volume" argument LibraryVolume object with
		AccessHandler object it is assigned to, so it must be it's "_UPPER_LAYER", and returns
		corresponding mapped "counter" value, which must be integer that represents the counter of
		AccessHandler invocations for exactly "volume" object. Processes obtained value with special
		field "filter", which must be callable that accepts two arguments - current AccessInducer object
		and the value it processing. It is must be noted, that "filter" invocation implemented according
		to "filter" assigned during declaration of AccessInducer class, so it is instantiated. If "filter"
		will be assigned to already instantiated AccessInducer object, it must account for accepting the
		value argument only. It doesn't restricted for "filter" what value to return, cause it anyway will
		be converted to string. Returns either obtained, and perhaps processed, value if it is originally
		not None or "filter" returned not None. Otherwise returns None. There is no Exception handling for
		"filter" invocation.
	"""

	filter :Optional[Callable[[AccessInducer,int],int | None]]

	def __call__(self, volume :LibraryVolume) -> str | None :
		if	isinstance((counter := self.get_register_counter(volume)), int):

			if		callable(getattr(self, "filter", None)): counter = self.filter(counter)
			else:	self.loggy.debug("Filter not applied")
			if		counter is not None : return str(counter)







