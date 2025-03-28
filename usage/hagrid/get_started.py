from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse
from pygwarts.hagrid.bloom.twigs			import Germination
from pygwarts.hagrid.bloom.leafs			import Rejuvenation
from pygwarts.hagrid.bloom.leafs			import Transfer
from pygwarts.hagrid.bloom.weeds			import Efflorescence
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.planting.peels			import GrowingPeel
from pygwarts.hagrid.planting.peels			import ThrivingPeel
from pygwarts.hagrid.planting.peeks			import DraftPeek
from pygwarts.hagrid.planting.leafs			import LeafProbe
from pygwarts.hagrid.planting.twigs			import TwigProbe
from pygwarts.hagrid.planting.weeds			import TrimProbe
from pygwarts.hagrid.cultivation.sifting	import SiftingController








class Hagrid(Copse):

	"""
		hagrid probe script to get started with. It is recommended to use such scheme with dummy operations
		before apply real fs manipulation. Consists of two Tree objects, one for copying files and one for
		moving. Also includes all source folders replication and removing items from target folders, that
		are not presented in source. Might be regulated by global SiftingControllers and must include local
		ones for Efflorescence. The idea is to get a log about what operations will proceed, because
		LeafProbe, TwigProbe and TrimProbe will not do anything else, just inform. Also debug level set
		for operations dispatchers for clarity.
	"""

	class loggy(LibraryContrib):

		init_name	= "hagrid (optional)"
		force_debug	= "*.files", "*.folders", "*.clean"

	class Copies(Tree):

		bough = "target folder one"
		@GrowingPeel
		@DraftPeek(renew=False)
		class grow(LeafProbe):		pass
		class files(Rejuvenation):	pass
		class twigs(SiftingController):

			include	= "include source folder for copy", "include target folder for delete"
			exclude	= "exclude source folder from delete", "exclude target folder from delete"

		class leafs(SiftingController):

			include	= "include source file for copy", "include target file for delete"
			exclude	= "exclude source file from delete", "exclude target file from delete"

	class Transfers(Tree):

		bough = "target folder two"
		@ThrivingPeel("moved", "for", "example")
		@DraftPeek(renew=False)
		class graft(LeafProbe):		pass
		class files(Transfer):		pass
		class twigs(SiftingController):

			include	= "include source folder for copy", "include target folder for delete"
			exclude	= "exclude source folder from delete", "exclude target folder from delete"

		class leafs(SiftingController):

			include	= "include source file for copy", "include target file for delete"
			exclude	= "exclude source file from delete", "exclude target file from delete"

	@GrowingPeel
	class thrive(TwigProbe):		pass
	class folders(Germination):		pass
	class trim(TrimProbe):			pass
	class clean(Efflorescence):

		branches = {

			"target folder one":	( "source folder", ),
			"target folder two":	( "source folder", ),
		}

	@fssprout("source folder")
	class probe(Flourish):

		class twigs(SiftingController):

			# Include in probe and/or exclude from probe some folders (optional).
			# IMPORTANT: by including some folders, all other neighbor folders that are not included
			# are automatically excluded!
			include	= "include such folder", "include such folder"
			exclude	= "exclude such folder", "exclude such folder"

		class leafs(SiftingController):

			# Include in probe and/or exclude from probe some files (optional).
			# IMPORTANT: by including some file patterns, all other different patterns
			# are automatically excluded!
			include	= "include such file", "include such file"
			exclude	= "exclude such file", "exclude such file"








if	__name__ == "__main__" : Hagrid().probe()







