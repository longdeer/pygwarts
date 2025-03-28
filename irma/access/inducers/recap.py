from typing							import Optional
from typing							import Callable
from pygwarts.magical.spells		import flagrate
from pygwarts.irma.access.inducers	import AccessInducer
from pygwarts.irma.access.volume	import LibraryVolume








class RegisterRecapInducer(AccessInducer):

	"""
		Implementation of inducer, that accesses provided "volume" argument LibraryVolume object with
		AccessHandler object it is assigned to, so it must be it's "_UPPER_LAYER", and returns corresponding
		mapped "recap" value, which might be any type and represents the object AccessHandler maintains for
		"volume". Processes obtained value with special field "filter", which must be callable that accepts
		two arguments - current AccessInducer object and the value it processing. It is must be noted, that
		"filter" invocation implemented according to "filter" assigned during declaration of AccessInducer
		class, so it is instantiated. If "filter" will be assigned to already instantiated AccessInducer
		object, it must account for accepting the value argument only. It doesn't restricted for "filter"
		what value to return, cause it anyway will be converted to string. Returns either obtained, and
		perhaps processed, value if it is originally not None or "filter" returned not None. Otherwise
		returns None. There is no Exception handling for "filter" invocation.
	"""

	filter :Optional[Callable[[AccessInducer,object],str | None]]

	def __call__(self, volume :LibraryVolume) -> str | None :
		if	(recap := self.get_register_recap(volume)) is not None:

			if		callable(getattr(self, "filter", None)): recap = self.filter(recap)
			else:	self.loggy.debug("Filter not applied")
			if		recap is not None : return str(recap)








class RegisterRecapAccumulatorInducer(AccessInducer):

	"""
		Implementation of inducer, that accesses provided "volume" argument LibraryVolume object with
		AccessHandler object it is assigned to, so it must be it's "_UPPER_LAYER", and returns corresponding
		mapped "recap" value, which might be a list that represents the data AccessHandler maintains for
		"volume". Processes current "recap" list to obtain another list of unique items, if "unique" boolean
		field is set to True. Converts all items in "recap" to strings and join them with "joint" field
		value, that converted to string too. Returns resulted joined string. Returns None if either "recap"
		is not a list or empty list.
	"""


	joint	:Optional[str]
	unique	:Optional[bool]


	def __call__(self, volume :LibraryVolume) -> str | None :


		if	isinstance(recap := self.get_register_recap(volume), list):
			if	getattr(self, "unique", False):


				uniqs	= set()
				accum	= [ acc for acc in map(str,recap) if not (acc in uniqs or uniqs.add(acc)) ]
			else:
				accum	= list(map(str,recap))


			induce	= str(getattr(self, "joint", " ")).join(accum)
			count	= len(induce)


			self.loggy.debug(f"Accumulated {count} symbol{flagrate(count)} string")
			return induce or None







