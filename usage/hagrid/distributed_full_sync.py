import	os
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.shelve				import LibraryShelf
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.bloom.weeds			import Efflorescence
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import BlindPeek
from	pygwarts.hagrid.planting.weeds		import SprigTrimmer
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class Hagrid(Copse):

	""" hagrid scheme to fully synchronize three target folders to corresponding three source folders """

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	class seeds(LibraryShelf):

		grabbing	= "path to shelve file with mtimes"	# Path to file with mtimes
		reclaiming	= True								# Flag to rewrite source file with mtimes

	class First(Tree):

		bough = "FIRST TARGET folder path"
		class twigs(SiftingController):

			include	= (

				# Including both current target and corresponding source folder to copy folders
				# from source to target and to delete folders in target that aren't present in
				# source for both nt and posix OS types
				( rf"{"FIRST TARGET folder path"}/.+", rf"{"FIRST SOURCE folder path"}/.+" )
				if os.name == "posix" else
				(
					"FIRST TARGET folder path".replace("\\", "\\\\") + r"\\.+",
					"FIRST SOURCE folder path".replace("\\", "\\\\") + r"\\.+"
				)
			)
		class leafs(SiftingController):

			include	= (

				# Including both current target and corresponding source folder to copy files
				# from source to target and to delete files in target that aren't present in
				# source for both nt and posix OS types
				( rf"{"FIRST TARGET folder path"}/.+", rf"{"FIRST SOURCE folder path"}/.+" )
				if os.name == "posix" else
				(
					"FIRST TARGET folder path".replace("\\", "\\\\") + r"\\.+",
					"FIRST SOURCE folder path".replace("\\", "\\\\") + r"\\.+"
				)
			)

	class Second(Tree):

		bough = "SECOND TARGET folder path"
		class twigs(SiftingController):

			include	= (

				# Including both current target and corresponding source folder to copy folders
				# from source to target and to delete folders in target that aren't present in
				# source for both nt and posix OS types
				( rf"{"SECOND TARGET folder path"}/.+", rf"{"SECOND SOURCE folder path"}/.+" )
				if os.name == "posix" else
				(
					"SECOND TARGET folder path".replace("\\", "\\\\") + r"\\.+",
					"SECOND SOURCE folder path".replace("\\", "\\\\") + r"\\.+"
				)
			)
		class leafs(SiftingController):

			include	= (

				# Including both current target and corresponding source folder to copy files
				# from source to target and to delete files in target that aren't present in
				# source for both nt and posix OS types
				( rf"{"SECOND TARGET folder path"}/.+", rf"{"SECOND SOURCE folder path"}/.+" )
				if os.name == "posix" else
				(
					"SECOND TARGET folder path".replace("\\", "\\\\") + r"\\.+",
					"SECOND SOURCE folder path".replace("\\", "\\\\") + r"\\.+"
				)
			)

	class Third(Tree):

		bough = "THIRD TARGET folder path"
		class twigs(SiftingController):

			include	= (

				# Including both current target and corresponding source folder to copy folders
				# from source to target and to delete folders in target that aren't present in
				# source for both nt and posix OS types
				( rf"{"THIRD TARGET folder path"}/.+", rf"{"THIRD SOURCE folder path"}/.+" )
				if os.name == "posix" else
				(
					"THIRD TARGET folder path".replace("\\", "\\\\") + r"\\.+",
					"THIRD SOURCE folder path".replace("\\", "\\\\") + r"\\.+"
				)
			)
		class leafs(SiftingController):

			include	= (

				# Including both current target and corresponding source folder to copy files
				# from source to target and to delete files in target that aren't present in
				# source for both nt and posix OS types
				( rf"{"THIRD TARGET folder path"}/.+", rf"{"THIRD SOURCE folder path"}/.+" )
				if os.name == "posix" else
				(
					"THIRD TARGET folder path".replace("\\", "\\\\") + r"\\.+",
					"THIRD SOURCE folder path".replace("\\", "\\\\") + r"\\.+"
				)
			)

	@GrowingPeel
	class thrive(TwigThrive):	pass
	class folders(Germination):	pass

	@GrowingPeel
	@BlindPeek("seeds", renew=False)
	class grow(LeafGrowth):		pass
	class files(Rejuvenation):	pass

	@fssprout("FIRST SOURCE folder path")	# Order does matter cause every sprout packs itself
	@fssprout("SECOND SOURCE folder path")	# before previous sprout, so the nearest to dispatcher
	@fssprout("THIRD SOURCE folder path")	# sprout will be processed first
	class fullsync(Flourish):	pass
	class trim(SprigTrimmer):	pass
	class clean(Efflorescence):

		branches	= {

			"FIRST TARGET folder path":		( "FIRST SOURCE folder path", ),
			"SECOND TARGET folder path":	( "SECOND SOURCE folder path", ),
			"THIRD TARGET folder path":		( "THIRD SOURCE folder path", ),
		}








if	__name__ == "__main__":

	hagrid = Hagrid()
	hagrid.fullsync()

	diff = hagrid.seeds.real_diff
	for tracker in diff : hagrid.seeds.loggy.info(f"Discarded tracker for \"{tracker}\"")

	# Setting "modified" flag to True if there is a difference between "real_shelf"
	# which taken from file and "magical_shelf" which taken during synchronization,
	# so if some files from last synchronization are absent now, the Shelf will be
	# rewritten. By default if no files modified in current synchronization, "modified"
	# flag will not be toggled, despite number of discarded trackers.
	hagrid.seeds.modified |= bool(diff)
	hagrid.seeds.produce(magical=True, rewrite=True)







