from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.bloom.leafs			import Rejuvenation
from pygwarts.hagrid.planting.leafs			import LeafGrowth
from pygwarts.hagrid.planting.peels			import GrowingPeel
from pygwarts.hagrid.planting.peeks			import DraftPeek
from pygwarts.hagrid.cultivation.sifting	import SiftingController








class Hagrid(Copse):

	"""
		hagrid scheme for maintaining certain files. Consists of two Tree objects, one for actual renewal
		of files that are present in both target and source folders, one for adding new files for renewal.
		Whole process is regulated by renew flag in DraftPeek, so all considered files in Renewal will
		be checked for mtime. Adding is regulated by SiftingController, which might be populated with
		new files to be considered by Renewal. The order of Tree objects doesn't matter, cause when file
		is copied by one grow, the second one's DraftPeek must skip it (unless files copying will take
		a lot of time, so some more extensive comparator might be used for DraftPeek - this situation might
		be applied if script supposed to be invoked with very little pauses.
	"""

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	class Renewal(Tree):

		bough = "target folder path"
		@GrowingPeel
		@DraftPeek(renew=True)
		class grow(LeafGrowth):		pass
		class files(Rejuvenation):	pass

	class Adding(Tree):

		bough = "target folder path"
		@GrowingPeel
		@DraftPeek(renew=False)
		class grow(LeafGrowth):		pass
		class files(Rejuvenation):	pass
		class leafs(SiftingController):

			include	= (

				"new file to include for renewal",
				"new file to include for renewal",
				"new file to include for renewal",
			)

	@fssprout("source folder path")
	class renewal(Flourish):

		class twigs(SiftingController):

			# Include in renewal and/or exclude from renewal some folders (optional).
			# IMPORTANT: by including some folders, all other neighbor folders that are not included
			# are automatically excluded!
			include	= "include such folder", "include such folder"
			exclude	= "exclude such folder", "exclude such folder"

		class leafs(SiftingController):

			# Include in renewal and/or exclude from renewal some files (optional).
			# IMPORTANT: by including some file patterns, all other different patterns
			# are automatically excluded!
			include	= "include such file", "include such file"
			exclude	= "exclude such file", "exclude such file"








if	__name__ == "__main__" : Hagrid().renewal()







