from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.irma.shelve					import LibraryShelf
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.bloom.twigs			import Germination
from pygwarts.hagrid.bloom.leafs			import Rejuvenation
from pygwarts.hagrid.planting.leafs			import LeafGrowth
from pygwarts.hagrid.planting.twigs			import TwigThrive
from pygwarts.hagrid.planting.peels			import GrowingPeel
from pygwarts.hagrid.planting.peeks			import BlindPeek
from pygwarts.hagrid.cultivation.sifting	import SiftingController








class Hagrid(Tree):

	""" hagrid scheme to copy all content from one folder to another """

	bough = "target folder path"
	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	@GrowingPeel						# The part that in charge for folders synchronization.
	class thrive(TwigThrive):	pass	# GrowingPeel copies the absolute path from source folder
	class folders(Germination):	pass	# and add it to target.

	@GrowingPeel						# The part that in charge for files synchronization.
	@BlindPeek("seeds", renew=False)	# GrowingPeel copies the absolute path from source folder
	class grow(LeafGrowth):		pass	# and add it to target. BlindPeek triggers only files that
	class files(Rejuvenation):	pass	# has mtime greater that one from last synchronization.
	class seeds(LibraryShelf):

		grabbing	= "last sync peeks path"	# File that contain mtimes from last synchronization.
		reclaiming	= True						# Flag to safe current synchronization to last (rewrite).

	@fssprout("source folder path")
	class sync(Flourish):

		class twigs(SiftingController):

			# Include in sync and/or exclude from sync some folders (optional).
			# IMPORTANT: by including some folders, all other neighbor folders that are not included
			# are automatically excluded!
			include	= "include such folder", "include such folder"
			exclude	= "exclude such folder", "exclude such folder"

		class leafs(SiftingController):

			# Include in sync and/or exclude from sync some files (optional).
			# IMPORTANT: by including some file patterns, all other different patterns
			# are automatically excluded!
			include	= "include such file", "include such file"
			exclude	= "exclude such file", "exclude such file"








if	__name__ == "__main__":

	hagrid = Hagrid()
	hagrid.sync()

	diff = hagrid.seeds.real_diff
	for tracker in diff : hagrid.seeds.loggy.info(f"Discarded tracker for \"{tracker}\"")

	# Setting "modified" flag to True if there is a difference between "real_shelf"
	# which taken from file and "magical_shelf" which taken during synchronization,
	# so if some files from last synchronization are absent now, the Shelf will be
	# rewritten. By default if no files modified in current synchronization, "modified"
	# flag will not be toggled, despite number of discarded trackers.
	hagrid.seeds.modified |= bool(diff)
	hagrid.seeds.produce(magical=True, rewrite=True)







