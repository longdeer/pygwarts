import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import DraftPeek








class RegrowthCase(MediumSet):

	"""
		GrowingPeel, DraftPeek, Rejuvenation
		Triple sprout copse
		Triple bough copse
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_3): os.remove(cls.MEDIUM_HANDLER_3)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_3)


		# First bough takes first sprout's
		cls.fmake(cls, cls.tg1_f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.tg1_f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.tg1_f_mss1_md_scissors, "only in HD or better")


		# Second bough takes second sprout's
		cls.fmake(cls, cls.tg2_f_mss2_explangraph,				"ex.plan graph.png")
		cls.fmake(cls, cls.tg2_f_mss2_c_easyprocrastinating,	"easy-procrastinating.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_easyreflections,		"easy-reflections.task")
		cls.fmake(cls, cls.tg2_f_mss2_c_easyphilosophizing,		"easy-philosophizing.task")


		# Thrid bough takes third sprout's
		cls.fmake(cls, cls.tg3_f_mss3_k_f_milk,			"milk")
		cls.fmake(cls, cls.tg3_f_mss3_k_f_cheese,		"cheese")
		cls.fmake(cls, cls.tg3_f_mss3_k_f_meat,			"meat")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_bread,		"bread")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_crumb420,	"crumb420")
		cls.fmake(cls, cls.tg3_f_mss3_k_t_bc_crumb69,	"crumb69")


		sleep(1.1)
		# Once again in case of regrowing
		################################### First sprout files ###################################
		cls.fmake(cls, cls.f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.f_mss1_md_scissors, "only in HD or better")
		cls.fmake(cls, cls.f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		cls.fmake(cls, cls.f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		cls.fmake(cls, cls.f_mss1_md_gc_onion, "makes even devil cry")




		################################### Second sprout files ###################################
		cls.fmake(cls, cls.f_mss2_tasksschedule, "1. get up\n2. get sad")
		cls.fmake(cls, cls.f_mss2_explangraph, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
		cls.fmake(cls, cls.f_mss2_c_hardcleaning, "especially vacuum")
		cls.fmake(cls, cls.f_mss2_c_hardwashing, "dishes so dishes")
		cls.fmake(cls, cls.f_mss2_c_mediumcooking, "who do you think i am, a chemist?")
		cls.fmake(cls, cls.f_mss2_c_mediumhomework, "my son homework, ofcourse")
		cls.fmake(cls, cls.f_mss2_c_mediumphysicals, "what the flip is that?")
		cls.fmake(cls, cls.f_mss2_c_easyprocrastinating, "the easiest thing ever")
		cls.fmake(cls, cls.f_mss2_c_easyreflections, "litlle harder but still easy")
		cls.fmake(cls, cls.f_mss2_c_easyphilosophizing, "not easy at all, but why not")




		################################### Third sprout files ###################################
		cls.fmake(cls, cls.f_mss3_k_f_milk, "from cow")
		cls.fmake(cls, cls.f_mss3_k_f_cheese, "from... cow")
		cls.fmake(cls, cls.f_mss3_k_f_meat, "from...")
		cls.fmake(cls, cls.f_mss3_k_o_chicken, "cooked in ~60 minutes")
		cls.fmake(cls, cls.f_mss3_k_o_pie, "already baked")
		cls.fmake(cls, cls.f_mss3_k_t_bc_bread, "always crumbles")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb1, "i barely believe it is just the first crumb")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb2, "i don't believe it is really the second crumb")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb420, "this crumb get really high")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb69, "this crumb get really nice")




	def setUp(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_3
				init_level	= 10


			class First(Tree):	bough = self.MEDIUM_SET_BOUGH_1
			class Second(Tree):	bough = self.MEDIUM_SET_BOUGH_2
			class Third(Tree):	bough = self.MEDIUM_SET_BOUGH_3


			@GrowingPeel
			@DraftPeek(renew=True)
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass


			@fssprout(self.MEDIUM_SET_SPROUT_3)
			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class sync(Flourish):		pass


		self.test_case = Forest




	def test_first_flourish(self):

		self.test_case.loggy.init_name = "first_flourish"
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_1))
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_2))
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_3))


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
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
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




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
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




		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
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
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))




		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


		# First sprout first bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertIn(

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


		# Second sprout first bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)


		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg1_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
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








		# First sprout second bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)


		# Second sprout second bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertIn(

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
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)


		# Third sprout second bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_f_meat}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_chicken}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_o_pie}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_bread}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb1}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb2}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg2_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)


		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
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








		# First sprout third bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_scissors}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_sadmovies}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_dumbasses}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss1_md_gc_onion}\"",
			case_loggy.output
		)


		# Second sprout third bough files
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_explangraph}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardcleaning}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_hardwashing}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumcooking}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumhomework}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_mediumphysicals}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss2_c_easyphilosophizing}\"",
			case_loggy.output
		)


		# Third sprout third bough files
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertIn(

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
		self.assertIn(

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
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)


		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
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
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
















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
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
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




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
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




		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
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
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))




		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


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


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
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


		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
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


		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
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
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))















	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"
		# Once again in case of regrowing
		################################### First sprout files ###################################
		self.fmake(self.f_mss1_md_rock, "it's about time it's about power")
		self.fmake(self.f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		self.fmake(self.f_mss1_md_scissors, "only in HD or better")
		self.fmake(self.f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		self.fmake(self.f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		self.fmake(self.f_mss1_md_gc_onion, "makes even devil cry")




		################################### Second sprout files ###################################
		self.fmake(self.f_mss2_tasksschedule, "1. get up\n2. get sad")
		self.fmake(self.f_mss2_explangraph, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
		self.fmake(self.f_mss2_c_hardcleaning, "especially vacuum")
		self.fmake(self.f_mss2_c_hardwashing, "dishes so dishes")
		self.fmake(self.f_mss2_c_mediumcooking, "who do you think i am, a chemist?")
		self.fmake(self.f_mss2_c_mediumhomework, "my son homework, ofcourse")
		self.fmake(self.f_mss2_c_mediumphysicals, "what the flip is that?")
		self.fmake(self.f_mss2_c_easyprocrastinating, "the easiest thing ever")
		self.fmake(self.f_mss2_c_easyreflections, "litlle harder but still easy")
		self.fmake(self.f_mss2_c_easyphilosophizing, "not easy at all, but why not")




		################################### Third sprout files ###################################
		self.fmake(self.f_mss3_k_f_milk, "from cow")
		self.fmake(self.f_mss3_k_f_cheese, "from... cow")
		self.fmake(self.f_mss3_k_f_meat, "from...")
		self.fmake(self.f_mss3_k_o_chicken, "cooked in ~60 minutes")
		self.fmake(self.f_mss3_k_o_pie, "already baked")
		self.fmake(self.f_mss3_k_t_bc_bread, "always crumbles")
		self.fmake(self.f_mss3_k_t_bc_crumb1, "i barely believe it is just the first crumb")
		self.fmake(self.f_mss3_k_t_bc_crumb2, "i don't believe it is really the second crumb")
		self.fmake(self.f_mss3_k_t_bc_crumb420, "this crumb get really high")
		self.fmake(self.f_mss3_k_t_bc_crumb69, "this crumb get really nice")




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
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
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




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
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




		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
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
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))




		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


		# First sprout first bough files
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
			case_loggy.output
		)
		self.assertIn(

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


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
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


		# Second sprout second bough files
		self.assertNotIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_tasksschedule}\"",
			case_loggy.output
		)
		self.assertIn(

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
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyprocrastinating}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyreflections}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg2_f_mss2_c_easyphilosophizing}\"",
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


		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
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


		# Third sprout third bough files
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_milk}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_f_cheese}\"",
			case_loggy.output
		)
		self.assertIn(

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
		self.assertIn(

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
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb420}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Grown leaf \"{self.tg3_f_mss3_k_t_bc_crumb69}\"",
			case_loggy.output
		)


		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
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
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))








if __name__ == "__main__" : unittest.main(verbosity=2)







