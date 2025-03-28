from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.bloom.leafs			import Transfer
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.planting.leafs			import LeafPush
from pygwarts.hagrid.planting.peels			import ThrivingPeel
from pygwarts.hagrid.cultivation.sifting	import SiftingController








p = TimeTurner()








class Hagrid(Tree):

	"""
		hagrid archivation script, that implies every day invocation to walk all source folders and move
		some files, according to SiftingController filters. The final destination for every file will be
		the same as for source, nested with year, month and day folders, depending on the day the script
		was called. Basically this is for archivation of files that was created at the day to the folder
		that will point to same date, like every evening after work. TimeTurner objects attributes for
		ThrivingPeel might be also chosen according to OS type as single value, like "Ymd_aspath" for UNIX
		or "Ymd_aswpath" for windows. Also it must be noted, that "LeafPush" is used for preserving moved
		file meta data, which might cause a lot of warnings when destination folder need special
		permissions for meta data manipulations.
	"""

	bough = "archive root folder"
	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	@ThrivingPeel(p.Y, p.m, p.d)
	class graft(LeafPush):	pass
	class files(Transfer):	pass

	@fssprout("source path 3")	# Order does matter cause every sprout packs itself
	@fssprout("source path 2")	# before previous sprout, so the nearest to dispatcher
	@fssprout("source path 1")	# sprout will be processed first
	class arch(Flourish):

		class twigs(SiftingController):

			# Include in arch and/or exclude from arch some folders (optional).
			# IMPORTANT: by including some folders, all other neighbor folders that are not included
			# are automatically excluded!
			include	= "include such folder", "include such folder"
			exclude	= "exclude such folder", "exclude such folder"

		class leafs(SiftingController):

			# Include in arch and/or exclude from arch some files (optional).
			# IMPORTANT: by including some file patterns, all other different patterns
			# are automatically excluded!
			include	= "include such file", "include such file"
			exclude	= "exclude such file", "exclude such file"








if	__name__ == "__main__" : Hagrid().arch()







