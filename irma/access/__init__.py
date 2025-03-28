import	re
from	typing					import List
from	pygwarts.magical.chests	import KeyChest








class LibraryAccess(KeyChest):

	"""
		irma.access main object, that represents the container for any accessing objects. Original design
		implies next library access algorithm:
			1.	LibraryAccess object is the top level for access;
			2.	LibraryVolume objects are declared under the top LibraryAccess and represents the volumes,
				or file locations to be accessed;
			3.	VolumeBookmark objects are declared either under the top LibraryAccess or under
				corresponding LibraryVolume, to organize handling of volumes access (it will be common
				bookmarks that are declared under the top LibraryAccess, means will be available for every
				LibraryVolume);
			4.	AccessHandler objects are declared under the corresponding VolumeBookmark objects and are
				defined the way they should handle information they will be supplied by the triggered
				bookmarks they declared under (or common);
			5.	AccessInducer objects are declared under corresponding AccessHandler and are defined the
				way the data handled by AccessHandler they declared under might be induced (or viewed) - it
				must return a string that will represent the view;
			6.	VolumeAnnex objects are declared under corresponding LibraryVolume objects as "Annex"
				member and organizes the volume data induce (or view) by collecting all volume's
				AccessInducer's strings into one concatenated string to be returned;
			7.	LibraryAnnex object declared under the top LibraryAccess and organizes first every volume
				access by it's API, and then tries to invoke every accessed volume's "Annex" to produce
				the final concatenation of all volumes "Annex" concatenations to return it.
			8.	Any other objects might be declared under the top LibraryAccess to be integrated into
				mutable chain and to be reachable for every access member.
	"""

	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.loggy.debug(f"Library access point created")


	def compile_triggers(self, triggers :List[str]) -> re.Pattern | None :

		"""
			Utility method for LibraryVolume objects to compile their VolumeBookmark triggers into one big
			regex. Accepts list "triggers" with every item is a string that represents a "trigger" field
			for a VolumeBookmark object. The final regex will be formed from every non empty string from
			"triggers" as an individual group. Returns compiled regex if at least one group formed. Returns
			None if "triggers" not a list or no groups were formed.
		"""

		if	isinstance(triggers, list) and (pattern := "("):

			for trigger in triggers:
				if	isinstance(trigger, str) and len(trigger):


					pattern += f"{trigger})|("
					self.loggy.debug(f"Compiling trigger \"{trigger}\"")
				else:
					self.loggy.debug(f"Skipping invalid trigger \"{trigger}\"")


			if		1 <len(pattern): return re.compile(pattern.rstrip("|("))
			else:	self.loggy.debug("No triggers compiled")
		else:		self.loggy.debug(f"Invalid triggers {type(triggers)}")







