import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
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
from	pygwarts.hagrid.planting.peeks		import DraftPeek
from	pygwarts.hagrid.planting.weeds		import SprigTrimmer
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class MultiSproutEffloresce(MediumSet):

	"""
		GrowingPeel, DraftPeek, Germination -> Rejuvenation -> rEfflorescence
		Triple sprout copse
		Triple bough copse
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_6): os.remove(cls.MEDIUM_HANDLER_6)

	@classmethod
	def setUpClass(cls):

		"""
			d- MEDIUM_SET_BOUGH_1
				d- men due
					f- rock
					f- paper
					f- scissors
					f- lizzard						- this one to be effloresced
					f- spock						- this one to be effloresced
					d- girls cries
						f- sad movies
						f- dumbasses (literaly)
						f- onion
						d- mirror reflections		- this one to be effloresced
				d- commons
					d- good
					d- not good
					d- bad
					d- not bad
					d- not not
					d- bad bad
					d- bad good
					d- good bad
					d- big bad wolf					- this one to be effloresced
		"""

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_6)


		# First bough first sprout
		cls.fmake(cls, cls.tg1_f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.tg1_f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.tg1_f_mss1_md_scissors, "only in HD or better")
		cls.fmake(cls, cls.tg1_f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		cls.fmake(cls, cls.tg1_f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		cls.fmake(cls, cls.tg1_f_mss1_md_gc_onion, "makes even devil cry")
		os.makedirs(cls.tg1_d_mss1_c_good)
		os.makedirs(cls.tg1_d_mss1_c_notgood)
		os.makedirs(cls.tg1_d_mss1_c_bad)
		os.makedirs(cls.tg1_d_mss1_c_notbad)
		os.makedirs(cls.tg1_d_mss1_c_notnot)
		os.makedirs(cls.tg1_d_mss1_c_badbad)
		os.makedirs(cls.tg1_d_mss1_c_badgood)
		os.makedirs(cls.tg1_d_mss1_c_goodbad)


		# First bough extra
		cls.tg1_f_mss1_md_lizzard	= os.path.join(cls.tg1_d_mss1_md, "lizzard")
		cls.tg1_f_mss1_md_spock		= os.path.join(cls.tg1_d_mss1_md, "spock")
		cls.tg1_d_mss1_md_d_mirror	= os.path.join(cls.tg1_d_mss1_md_gc, "mirror reflections")
		cls.tg1_d_mss1_c_bbw		= os.path.join(cls.tg1_d_mss1_c, "big bad wolf")
		cls.fmake(cls, cls.tg1_f_mss1_md_lizzard, "poisones spock")
		cls.fmake(cls, cls.tg1_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(cls.tg1_d_mss1_md_d_mirror)
		os.makedirs(cls.tg1_d_mss1_c_bbw)




		# Second bough second sprout
		cls.fmake(cls, cls.tg2_f_mss2_tasksschedule,			"tasks schedule.txt")
		cls.fmake(cls, cls.tg2_f_mss2_explangraph,				"ex.plan graph.png")
		cls.fmake(cls, cls.tg2_f_mss2_c_hardcleaning,			"hard-cleaning.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_hardwashing,			"hard-washing.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_mediumcooking,			"medium-cooking.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_mediumhomework,			"medium-homework.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_mediumphysicals,		"medium-physicals.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_easyprocrastinating,	"easy-procrastinating.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_easyreflections,		"easy-reflections.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_easyphilosophizing,		"easy-philosophizing.task")


		# Second bough extra
		cls.tg2_f_mss1_md_lizzard	= os.path.join(cls.tg2_d_mss1_md, "lizzard")
		cls.tg2_f_mss1_md_spock		= os.path.join(cls.tg2_d_mss1_md, "spock")
		cls.tg2_d_mss1_md_d_mirror	= os.path.join(cls.tg2_d_mss1_md_gc, "mirror reflections")
		cls.tg2_d_mss1_c_bbw		= os.path.join(cls.tg2_d_mss1_c, "big bad wolf")
		cls.fmake(cls, cls.tg2_f_mss1_md_lizzard, "poisones spock")
		cls.fmake(cls, cls.tg2_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(cls.tg2_d_mss1_md_d_mirror)
		os.makedirs(cls.tg2_d_mss1_c_bbw)




		# Third bough third sprout
		cls.fmake(cls, cls.tg3_f_mss3_k_f_milk,			"milk")
		cls.fmake(cls, cls.tg3_f_mss3_k_f_cheese,		"cheese")
		cls.fmake(cls, cls.tg3_f_mss3_k_f_meat,			"meat")
		cls.fmake(cls, cls.tg3_f_mss3_k_o_chicken,		"chicken")
		cls.fmake(cls, cls.tg3_f_mss3_k_o_pie,			"pie")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_bread,		"bread")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_crumb1,	"crumb1")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_crumb2,	"crumb2")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_crumb420,	"crumb420")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_crumb69,	"crumb69")


		# Third bough extra
		cls.tg3_f_mss1_md_lizzard	= os.path.join(cls.tg3_d_mss1_md, "lizzard")
		cls.tg3_f_mss1_md_spock		= os.path.join(cls.tg3_d_mss1_md, "spock")
		cls.tg3_d_mss1_md_d_mirror	= os.path.join(cls.tg3_d_mss1_md_gc, "mirror reflections")
		cls.tg3_d_mss1_c_bbw		= os.path.join(cls.tg3_d_mss1_c, "big bad wolf")
		cls.fmake(cls, cls.tg3_f_mss1_md_lizzard, "poisones spock")
		cls.fmake(cls, cls.tg3_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(cls.tg3_d_mss1_md_d_mirror)
		os.makedirs(cls.tg3_d_mss1_c_bbw)




	def setUp(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_6
				init_level	= 10

			class First(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):

					# include for growing/thriving and for trimming
					include = r".+",
					# no more bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_1}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\[^(\\)]+$", )
					)

				class twigs(SiftingController):

					# include for growing/thriving and for trimming
					include = r".+",
					# no more bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_1}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\[^(\\)]+$", )
					)

			class Second(Tree):

				bough = self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController):

					# include for growing/thriving and for trimming
					include = r".+",
					# no more bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_2}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_2.replace("\\", "\\\\") + r"\\[^(\\)]+$", )
					)

				class twigs(SiftingController):

					# include for growing/thriving and for trimming
					include = r".+",
					# no more bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_2}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_2.replace("\\", "\\\\") + r"\\[^(\\)]+$", )
					)

			class Third(Tree):

				bough = self.MEDIUM_SET_BOUGH_3
				class leafs(SiftingController):

					# include for growing/thriving and for trimming
					include = r".+",
					# no more bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_3}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_3.replace("\\", "\\\\") + r"\\[^(\\)]+$", )
					)

				class twigs(SiftingController):

					# include for growing/thriving and for trimming
					include = r".+",
					# no more bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_3}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_3.replace("\\", "\\\\") + r"\\[^(\\)]+$", )
					)

			@GrowingPeel
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass
			class trim(SprigTrimmer):	pass
			class clean(Efflorescence):
				branches	= {

					self.MEDIUM_SET_BOUGH_1: (
						self.MEDIUM_SET_SPROUT_1,
						self.MEDIUM_SET_SPROUT_2,
						self.MEDIUM_SET_SPROUT_3,
					),

					self.MEDIUM_SET_BOUGH_2: (
						self.MEDIUM_SET_SPROUT_1,
						self.MEDIUM_SET_SPROUT_2,
						self.MEDIUM_SET_SPROUT_3,
					),

					self.MEDIUM_SET_BOUGH_3: (
						self.MEDIUM_SET_SPROUT_1,
						self.MEDIUM_SET_SPROUT_2,
						self.MEDIUM_SET_SPROUT_3,
					),
				}


			@fssprout(self.MEDIUM_SET_SPROUT_3)
			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class sync(Flourish):		pass


		self.test_case = Forest




	def test_first_flourish(self):

		self.test_case.loggy.init_name = "first_flourish"
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_1))


		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))




		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))




		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# Second sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bbw))




		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))
		# Third sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))
		# Second bough extra
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Second sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		# First sprout first bough folders
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout first bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout first bough folders
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout first bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout first bough folders
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg1_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout first bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.f_msb1_flower}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg1_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg1_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))








		# First sprout second bough folders
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout second bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout second bough folders
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout second bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout second bough folders
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg2_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout second bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:first_flourish:Trimmed twig \"{self.d_msb2_w}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg2_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg2_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))
		# Third sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))








		# First sprout third bough folders
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout third bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout third bough folders
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout third bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout third bough folders
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.tg3_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout third bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:first_flourish:Trimmed twig \"{self.d_msb3_a}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Trimmed twig \"{self.d_msb3_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.f_msb3_almost}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg3_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg3_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))
		# Third sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))








		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))




		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))




		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))
















	def test_no_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "no_touch_flourish"


		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))




		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))




		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))




		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))
		# Third sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		# First sprout first bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout first bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout first bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout first bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout first bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout first bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.f_msb1_flower}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg1_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg1_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))








		# First sprout second bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout second bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout second bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout second bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout second bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout second bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.d_msb2_w}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg2_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg2_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))
		# Third sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))








		# First sprout third bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout third bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout third bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout third bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout third bough folders
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout third bough files
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.d_msb3_a}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.d_msb3_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.f_msb3_almost}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg3_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg3_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))
		# Third sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))








		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))




		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))




		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))
















	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"


		self.fmake(self.tg1_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(self.tg1_d_mss1_c_bbw)
		self.fmake(self.tg2_f_mss1_md_lizzard, "poisones spock")
		os.makedirs(self.tg2_d_mss1_md_d_mirror)
		self.fmake(self.tg3_f_mss1_md_lizzard, "poisones spock")
		self.fmake(self.tg3_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(self.tg3_d_mss1_md_d_mirror)
		os.makedirs(self.tg3_d_mss1_c_bbw)



		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))




		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))




		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bbw))




		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))
		# Third sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))
		# Second bough extra
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		# First sprout first bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout first bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout first bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout first bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout first bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg1_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout first bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.f_msb1_flower}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg1_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg1_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))
		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))








		# First sprout second bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout second bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout second bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout second bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout second bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg2_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout second bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.d_msb2_w}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg2_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg2_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))
		# Third sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))








		# First sprout third bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_md}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_md_gc}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_good}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_notgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_bad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_notbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_notnot}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_badbad}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_badgood}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss1_c_goodbad}\"",
			case_loggy.output
		)


		# First sprout third bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)




		# Second sprout third bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss2_c}\"",
			case_loggy.output
		)


		# Second sprout third bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)




		# Third sprout third bough folders
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss3_k}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_f}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_o}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.tg3_d_mss3_k_t_bc}\"",
			case_loggy.output
		)


		# Third sprout third bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.d_msb3_a}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.d_msb3_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.f_msb3_almost}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg3_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg3_d_mss1_c_bbw}\"",
			case_loggy.output
		)




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))
		# Third sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))








		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))




		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))




		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))








if __name__ == "__main__" : unittest.main(verbosity=2)







