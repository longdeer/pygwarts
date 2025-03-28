import	os
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import DraftPeek
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class Hagrid(Copse):

	""" hagrid scheme to copy all content from one folder to another and vice versa """

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	class First(Tree):

		bough = "FIRST folder path"
		class leafs(SiftingController):

			include = (

				# Explicitly include sync for opposite folder
				# for both nt and posix OS.
				( r"SECOND folder path/.+", )
				if os.name == "posix" else
				( "SECOND folder path".replace("\\", "\\\\") + r"\\.+", )
			)
		class twigs(SiftingController):

			include = (

				# Explicitly include sync for opposite folder
				# for both nt and posix OS.
				( r"SECOND folder path/.+", )
				if os.name == "posix" else
				( "SECOND folder path".replace("\\", "\\\\") + r"\\.+", )
			)

	class Second(Tree):

		bough = "SECOND folder path"
		class leafs(SiftingController):

			include = (

				# Explicitly include sync for opposite folder
				# for both nt and posix OS.
				( r"FIRST folder path/.+", )
				if os.name == "posix" else
				( "FIRST folder path".replace("\\", "\\\\") + r"\\.+", )
			)
		class twigs(SiftingController):

			include = (

				# Explicitly include sync for opposite folder
				# for both nt and posix OS.
				( r"FIRST folder path/.+", )
				if os.name == "posix" else
				( "FIRST folder path".replace("\\", "\\\\") + r"\\.+", )
			)

	@GrowingPeel
	class thrive(TwigThrive):		pass
	class folders(Germination):		pass

	# DraftPeek comparator mitigates the effect when rejuved folder
	# becomes a sprout and files seams to be newer then their last
	# sources, so one hour (for example) gap must ensure there'll
	# be no rewriting
	@GrowingPeel
	@DraftPeek(renew=False, comparator=(lambda F,S : 360 <(F -S)))
	class grow(LeafGrowth):			pass
	class files(Rejuvenation):		pass

	@fssprout("SECOND folder path")
	@fssprout("FIRST folder path")
	class intergrowth(Flourish):	pass








if	__name__ == "__main__" : Hagrid().intergrowth()







