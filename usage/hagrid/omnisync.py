from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.magical.time_turner.timers	import Callstamp
from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.irma.contrib.intercept		import STDOUTL
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.planting.peels			import GrowingPeel
from pygwarts.hagrid.planting.peeks			import DraftPeek
from pygwarts.hagrid.planting.leafs			import LeafGrowth
from pygwarts.hagrid.planting.twigs			import TwigThrive
from pygwarts.hagrid.planting.weeds			import SprigTrimmer
from pygwarts.hagrid.bloom.twigs			import Germination
from pygwarts.hagrid.bloom.leafs			import Rejuvenation
from pygwarts.hagrid.bloom.weeds			import Efflorescence
from pygwarts.hagrid.cultivation.sifting	import SiftingController








p = TimeTurner()








class Omni(Copse):

	"""
		Personal script that implies synchronization of some source folders on personal computer
		with another disk, network folders and external disk (if plugged in). All data categorized
		as documents, development and personal files, by the use of multiple SiftingControllers.
		This is a good example of "peeking" strategy, cause for the first time it was "BlindPeek".
		The idea was it is better to check one record in shelf than to peek all possible targets.
		It crumbled against the fact such huge shelf (even two) takes time to load up x4 than actual
		synchronization...
	"""

	@STDOUTL
	class loggy(LibraryContrib):

		handler		= f"~/omnisync/{p.Ym_aspath}/{p.dm_asjoin}sync.loggy"
		init_name	= "omnisync"




	class documents(Copse):

		class container(Tree):	bough	= "/mnt/container/omnisync/Documents"
		class ghub(Tree):		bough	= "/mnt/ghub/lngd/Documents"
		class hhub(Tree):		bough	= "/mnt/hhub/lngd/Documents"
		class lngddata(Tree):

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafGrowth):	pass
			bough	= "/media/lngd/lngddata/Documents"

		class leafs(SiftingController):

			exclude	= r"~/Documents/Archive/_work/.+",
			include	= (

				r"~/Documents/.*",
				r"/mnt/container/omnisync/Documents/.+",
				r"/mnt/ghub/lngd/Documents/.+",
				r"/mnt/hhub/lngd/Documents/.+",
				r"/media/lngd/lngddata/Documents/.+",
			)
		class twigs(SiftingController):

			exclude	= r"~/Documents/Archive/_work(/.+)?",
			include	= (

				r"~/Documents/.+",
				r"/mnt/container/omnisync/Documents/.+",
				r"/mnt/ghub/lngd/Documents/.+",
				r"/mnt/hhub/lngd/Documents/.+",
				r"/media/lngd/lngddata/Documents/.+",
			)




	class stuff(Copse):
		class container(Tree):		bough	= "/mnt/container/omnisync/rmp"
		class lngddata(Tree):

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafGrowth):	pass
			bough	= "/media/lngd/lngddata/rmp"

		class leafs(SiftingController):

			exclude	= (

				r"~/rmp/pcs/.+",
				r"~/rmp/OLHA/.+",
				r"~/rmp/xerox3315.+",
				r"~/rmp/TLG2/.+",
				r"~/rmp/CanonManual/.+",
			)
			include	= (

				r"~/rmp/.*",
				r"/mnt/container/omnisync/rmp/.+",
				r"/media/lngd/lngddata/rmp/.+",
			)
		class twigs(SiftingController):

			exclude	= (

				r"~/rmp/pcs(/.+)?",
				r"~/rmp/OLHA(/.+)?",
				r"~/rmp/xerox3315(/.+)?",
				r"~/rmp/TLG2(/.+)?",
				r"~/rmp/CanonManual(/.+)?",
			)
			include	= (

				r"~/rmp/.+",
				r"/mnt/container/omnisync/rmp/.+",
				r"/media/lngd/lngddata/rmp/.+",
			)




	class personal(Tree):

		bough	= "/media/lngd/lngddata/lngd"
		class leafs(SiftingController):	include	= r"~/lngd/.*", r"/media/lngd/lngddata/lngd/.+",
		class twigs(SiftingController):	include	= r"~/lngd/.*", r"/media/lngd/lngddata/lngd/.+",




	class development(Copse):
		class container(Tree):		bough	= "/mnt/container/Development"
		class lngddata(Tree):

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafGrowth):	pass
			bough	= "/media/lngd/lngddata/Development"

		class leafs(SiftingController):

			exclude	= (

				r"~/Development/omnisync/.+",
				r"/mnt/container/Development/pygwarts/development/.+",
				r"/media/lngd/lngddata/Development/pygwarts/development/.+",
			)
			include	= (

				r"~/Development/.*",
				r"/mnt/container/Development/.+",
				r"/media/lngd/lngddata/Development/.+",
			)
		class twigs(SiftingController):

			exclude	= (

				r"~/Development/omnisync(/.+)?",

				# All stuff about development just collecting, means no cleaning for boughs.
				r"/mnt/container/Development/pygwarts/development/.+",
				"/mnt/container/Development/pygwarts/global_testing",
				"/mnt/container/Development/pygwarts/olds",
				"/mnt/container/Development/pygwarts/readyops",
				"/mnt/container/Development/pygwarts/exp",

				r"/media/lngd/lngddata/Development/pygwarts/development/.+",
				"/media/lngd/lngddata/Development/pygwarts/olds",
				"/media/lngd/lngddata/Development/pygwarts/readyops",
				"/media/lngd/lngddata/Development/pygwarts/exp",
			)
			include	= (

				r"~/Development/.+",
				r"/mnt/container/Development/.+",
				r"/media/lngd/lngddata/Development/.+",
			)




	@GrowingPeel
	class thrive(TwigThrive):		pass
	class germinate(Germination):	pass

	@GrowingPeel
	@DraftPeek(renew=False)
	class grow(LeafGrowth):			pass
	class rejuve(Rejuvenation):		pass
	class trim(SprigTrimmer):		pass
	class effloresce(Efflorescence):

		branches	= {

			"/mnt/container/omnisync/rmp"		: ( "~/rmp", ),
			"/media/lngd/lngddata/rmp"			: ( "~/rmp", ),
			"/media/lngd/lngddata/lngd"			: ( "~/lngd", ),
			"/mnt/container/omnisync/Documents"	: ( "~/Documents", ),
			"/mnt/ghub/lngd/Documents"			: ( "~/Documents", ),
			"/mnt/hhub/lngd/Documents"			: ( "~/Documents", ),
			"/media/lngd/lngddata/Documents"	: ( "~/Documents", ),
			"/mnt/container/Development"		: ( "~/Development", ),
			"/media/lngd/lngddata/Development"	: ( "~/Development", ),
		}


	@Callstamp
	@fssprout("~/Development")
	@fssprout("~/lngd")
	@fssprout("~/rmp")
	@fssprout("~/Documents")
	class sync(Flourish):

		class twigs(SiftingController):

			exclude	= (

				"~/Documents/Trash",
				"~/Documents/Projects",
				"~/Documents/A1",
				r".+/__pycache__",
			)








if	__name__ == "__main__" : Omni().sync()







