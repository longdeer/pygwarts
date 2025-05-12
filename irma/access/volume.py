import	re
from	os						import R_OK
from	os						import access	as osaccess
from	os						import path		as ospath
from	typing					import Optional
from	typing					import Callable
from	typing					import Generator
from	pygwarts.magical.chests	import KeyChest
from	pygwarts.magical.spells	import patronus
from	pygwarts.irma.access	import LibraryAccess








class LibraryVolume(KeyChest):

	"""
		irma.access core super class that represents both, the existent file to access and it's access
		dispatcher. For the first part of it's functionality, every LibraryVolume object must have field
		"location" set to a string that must point to existent file to be processed. Also optional field
		"inrange" must be a string that will be compiled to a regex that will match desired lines. It
		is optional because it is possible to manually set "inrange" by the argument for corresponding
		method "get_range" for a file processing. Originally designed idea implies "inrange" to be set
		as a datetime string, e.g. as LibraryContrib logging pattern, to be matched for desired lines,
		but it's not the only way and also the wildcard ".+" might be used. LibraryVolume object is the
		point for LibraryAccess object to access specified file, so this is the second part of it, that
		is maintained by main methods:
			is_located		- method that verifies LibraryVolume points to accessible file;
			get_range		- method that suggests which lines of file will be considered by matching
							provided compiled regex (might be passed as an argument);
			g_reading		- generator method that opens "location" file and yields every line;
			g_triggering	- generator method that identifies what handling to trigger for every line.
		In the volume accessing time, the LibraryVolume object will serve as a container for all data that
		will be handled for that volume. Optional callable "Annex" is reserved for a object that will
		organize full volume access and, probably, organize data inducing.
	"""


	location	:str
	inrange		:Optional[str]
	Annex		:Optional[Callable[..., str | None]]


	def __init__(self, *args, **kwargs)	:
		super().__init__(*args, **kwargs)


		if	isinstance(liblink := getattr(self, "_UPPER_LAYER", None), LibraryAccess):

			liblink(self, "volume")
			self.loggy.debug(f"Assigned to {liblink}")
		else:
			self.loggy.info(f"Volume {self} not assigned to any library")




	def is_located(self) -> str | None :

		"""
			Preparation method that verifies provided "location" filed points to an existent file to read
			from. Returns the "location" string if verification was successful, None otherwise.
		"""

		if	isinstance(getattr(self, "location", None), str):
			if	ospath.isfile(self.location):
				if	osaccess(self.location, R_OK):


					self.loggy.debug(f"Accessible \"{self.location}\" located")
					return self.location


				else:	self.loggy.debug(f"Location \"{self.location}\" is not accessible")
			else:		self.loggy.debug(f"Location \"{self.location}\" is invalid")
		else:			self.loggy.debug("Location was not provided")




	def get_range(self, inrange :str =None) -> re.Pattern | None :

		"""
			Preparation method that compiles special regex, which must define lines to be processed
			by match, from "inrange" string, which must be either specified as a field or as an
			argument (the last one takes priority). Returns compiled regex if "inrange" string has
			been found, or None otherwise. The wildcard ".+" might be specified for matching every
			line, but it is not done by default.
		"""

		match inrange:

			case str(): return re.compile(inrange)
			case None if isinstance(getattr(self, "inrange", None), str): return re.compile(self.inrange)

		self.loggy.info(f"Valid {self} range not provided")




	def g_reading(self) -> Generator[str,None,None] :

		"""
			Access method that relies on valid "location" field, which will be ensured by "is_located"
			method beforehand, opens it and generates every line read. Any exception during file
			accessing will be caught and logged. Doesn't supposed to return anything.
		"""

		if	self.is_located():
			try:

				with open(self.location) as volume:
					self.loggy.info(f"Location \"{self.location}\" access granted")

					for line in volume : yield line.rstrip("\n")
			except	Exception as E:

				self.loggy.error(f"Location \"{self.location}\" access failed due to {patronus(E)}")




	def g_triggering(self, line :str, triggers: re.Pattern) -> Generator[str,None,None] :

		"""
			Access method that accepts two arguments - "line" string that was triggered and all "triggers"
			regex. When the "line" is triggered it must mean there are VolumeBookmark objects which
			"trigger" fields were found as current "line" substrings, which in turn means this "line"
			must be handled by that VolumeBookmark objects. For this to happen, "triggers" regex must
			comprise the triggers for VolumeBookmark objects. The main idea of current method is to
			find all possible "trigger" fields that will correspond to VolumeBookmark objects and yield it
			as strings. Doesn't supposed to return anything.
		"""

		if	isinstance(line, str):
			if	isinstance(triggers, re.Pattern):


				for triggered_group in triggers.finditer(line):
					for response in triggered_group.groups():
						if	response:


							self.loggy.debug(f"Triggered by \"{response}\"")
							yield response


			else:	self.loggy.debug(f"Invalid triggers \"{triggers}\"")
		else:		self.loggy.debug(f"Invalid line \"{line}\"")







