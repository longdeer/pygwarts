from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.bloom.leafs			import Rejuvenation
from pygwarts.hagrid.planting.leafs			import LeafMove
from pygwarts.hagrid.cultivation.sifting	import SiftingController








class Hagrid(Copse):

	"""
		hagrid scheme to sort files from different source folders to certain end folders.
		Any file that is sifted by corresponding "bough" will be moved right to the "bough".
	"""

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	class Docs(Tree):

		bough = "folder path to store documents"
		class leafs(SiftingController): include = r".+\.(docx?|txt|pdf)$",

	class Videos(Tree):

		bough = "folder path to store video files"
		class leafs(SiftingController): include = r".+\.(avi|mkv|mp4)$",

	class Pictures(Tree):

		bough = "folder path to store image files"
		class leafs(SiftingController): include = r".+\.(jpe?g|png|gif)$",

	class grow(LeafMove):		pass
	class files(Rejuvenation):	pass

	@fssprout("FIRST SOURCE folder path")	# Order does matter cause every sprout packs itself
	@fssprout("SECOND SOURCE folder path")	# before previous sprout, so the nearest to dispatcher
	@fssprout("THIRD SOURCE folder path")	# sprout will be processed first
	class sort(Flourish):		pass








if	__name__ == "__main__" : Hagrid().sort()







