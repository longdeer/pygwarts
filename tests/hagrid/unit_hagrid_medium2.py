import	os
import	unittest
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.leafs			import Transfer
from	pygwarts.hagrid.planting.leafs		import LeafMove
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class MultiTransferingCase(MediumSet):

	"""
		GrowingPeel, Transfer, moving graft
		File moving handler with all boughs filtered to collect corresponding files
		Triple sprout copse
		Triple bough copse
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_2): os.remove(cls.MEDIUM_HANDLER_2)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_2)
	def setUp(self): super().setUpClass()
	def test_filtered_flourish(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_2
				init_name	= "filtered_flourish"
				init_level	= 10

			class First(Tree):

				bough	= self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):
					include	= ( r".+/.+\.task$", ) if os.name == "posix" else ( r".+\\.+\.task$", )

			class Second(Tree):

				bough	= self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController):
					include	= (

						( r".+/(onion|milk|cheese|meat|chicken|pie|bread|crumb.+)$", )
						if os.name == "posix" else
						( r".+\\(onion|milk|cheese|meat|chicken|pie|bread|crumb.+)$", )
					)

			class Third(Tree):

				bough	= self.MEDIUM_SET_BOUGH_3
				class leafs(SiftingController):

					include	= (

						( rf"{self.MEDIUM_SET_SPROUT_1}/men due/.+", )
						if os.name == "posix" else
						( self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\men due\\.+", )
					)
					exclude	= (

						( rf"{self.MEDIUM_SET_SPROUT_1}/men due/girls cries/.+", )
						if os.name == "posix" else
						( self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\men due\\girls cries\\.+", )
					)

			@GrowingPeel
			class graft(LeafMove):	pass
			class files(Transfer):	pass

			@fssprout(self.MEDIUM_SET_SPROUT_3)	# Order does matter cause every sprout pack it'self
			@fssprout(self.MEDIUM_SET_SPROUT_2)	# before previous sprout, so the nearest to dispatcher
			@fssprout(self.MEDIUM_SET_SPROUT_1)	# sprout will be processed first.
			class sync(Flourish):	pass




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




		with self.assertLogs("filtered_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)




		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
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
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))

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
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

		# Second sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))

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




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

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

		# Third sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
















	def test_unfiltered_flourish(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_2
				init_name	= "unfiltered_flourish"
				init_level	= 10

			class First(Tree):

				bough	= self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):
					include	= ( r".+/.+\.task$", ) if os.name == "posix" else ( r".+\\.+\.task$", )

			class Second(Tree):

				bough	= self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController):
					include	= (

						( r".+/(onion|milk|cheese|meat|chicken|pie|bread|crumb.+)$",)
						if os.name == "posix" else
						( r".+\\(onion|milk|cheese|meat|chicken|pie|bread|crumb.+)$",)
					)

			class Third(Tree):

				bough	= self.MEDIUM_SET_BOUGH_3
				class leafs(SiftingController):	pass

			@GrowingPeel
			class graft(LeafMove):				pass
			class files(Transfer):				pass

			@fssprout(self.MEDIUM_SET_SPROUT_3)	# Order does matter cause every sprout pack it'self
			@fssprout(self.MEDIUM_SET_SPROUT_2)	# before previous sprout, so the nearest to dispatcher
			@fssprout(self.MEDIUM_SET_SPROUT_1)	# sprout will be processed first.
			class sync(Flourish):				pass




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




		with self.assertLogs("unfiltered_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)




		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertFalse(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))

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
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

		# Second sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))

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




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

		# Second sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))

		# Third sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))








if __name__ == "__main__" : unittest.main(verbosity=2)







