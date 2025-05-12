import	os
import	unittest
from	shutil								import rmtree
from	time								import sleep
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import DraftPeek
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class MultisproutTree(MediumSet):

	"""
		GrowingPeel, DraftPeek, Germination -> Rejuvenation
		Triple sprout copse
		Single bough tree
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_4): os.remove(cls.MEDIUM_HANDLER_4)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_4)
		if	os.path.isdir(cls.MEDIUM_SET_BOUGH_2): rmtree(cls.MEDIUM_SET_BOUGH_2)
		if	os.path.isdir(cls.MEDIUM_SET_BOUGH_3): rmtree(cls.MEDIUM_SET_BOUGH_3)

	def setUp(self):
		class Sakura(Tree):

			bough = self.MEDIUM_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_4
				init_level	= 10


			@GrowingPeel
			class thrive(TwigThrive):		pass
			class folders(Germination):		pass

			@GrowingPeel
			@DraftPeek(renew=False, picky=True)
			class grow(LeafGrowth):			pass
			class files(Rejuvenation):		pass

			@fssprout(self.MEDIUM_SET_SPROUT_3)
			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class sync(Flourish):

				class twigs(SiftingController):

					# no bads, please (missing not bad)
					exclude	= ( rf".+/.*bad.*$", ) if os.name == "posix" else ( rf".+\\.*bad.*$", )

				class leafs(SiftingController):

					# hate crumbs?
					exclude	= ( rf".+/crumb.*", ) if os.name == "posix" else ( rf".+\\crumb.*", )
					# include BOUGH_1 files for trimming
					# include SPROUT_1 files for sync
					# include SPROUT_3 files for sync
					include	= (
						(
							rf"{self.MEDIUM_SET_BOUGH_1}{os.sep}.+",
							rf"{self.MEDIUM_SET_SPROUT_1}{os.sep}.+",
							rf"{self.MEDIUM_SET_SPROUT_3}{os.sep}.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_3.replace("\\", "\\\\") + r"\\.+",
						)
					)


		self.test_case = Sakura




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




		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss1_md_rock}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_rock)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss1_md_paper}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_paper)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss1_md_scissors}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_scissors)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss1_md_gc_sadmovies}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_sadmovies)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss1_md_gc_dumbasses}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_dumbasses)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss1_md_gc_onion}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_onion)}",
			case_loggy.output
		)




		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_tasksschedule}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_tasksschedule)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_explangraph}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_explangraph)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_hardcleaning}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_hardcleaning)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_hardwashing}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_hardwashing)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_mediumcooking}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumcooking)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_mediumhomework}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumhomework)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_mediumphysicals}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumphysicals)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_easyprocrastinating}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyprocrastinating)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_easyreflections}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyreflections)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss2_c_easyphilosophizing}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyphilosophizing)}",
			case_loggy.output
		)




		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_f_milk}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_milk)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_f_cheese}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_cheese)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_f_meat}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_meat)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_o_chicken}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_o_chicken)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_o_pie}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_o_pie)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_t_bc_bread}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_bread)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb1}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb1)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb2}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb2)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb420}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb420)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:first_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb69}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb69)}",
			case_loggy.output
		)




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
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
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
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
















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




		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss1_md_rock}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_rock)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss1_md_paper}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_paper)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss1_md_scissors}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_scissors)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss1_md_gc_sadmovies}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_sadmovies)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss1_md_gc_dumbasses}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_dumbasses)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss1_md_gc_onion}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_onion)}",
			case_loggy.output
		)




		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_tasksschedule}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_tasksschedule)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_explangraph}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_explangraph)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_hardcleaning}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_hardcleaning)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_hardwashing}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_hardwashing)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_mediumcooking}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumcooking)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_mediumhomework}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumhomework)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_mediumphysicals}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumphysicals)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_easyprocrastinating}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyprocrastinating)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_easyreflections}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyreflections)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss2_c_easyphilosophizing}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyphilosophizing)}",
			case_loggy.output
		)




		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_f_milk}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_milk)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_f_cheese}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_cheese)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_f_meat}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_meat)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_o_chicken}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_o_chicken)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_o_pie}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_o_pie)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_bread}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_bread)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb1}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb1)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb2}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb2)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb420}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb420)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:no_touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb69}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb69)}",
			case_loggy.output
		)




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
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
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
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))
















	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"
		self.fmake(self.f_mss1_md_gc_onion, "makes even devil cry")
		self.fmake(self.f_mss2_tasksschedule, "1. get up\n2. get sad")
		self.fmake(self.f_mss3_k_t_bc_bread, "pit")


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




		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss1_md_rock}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_rock)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss1_md_paper}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_paper)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss1_md_scissors}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_scissors)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss1_md_gc_sadmovies}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_sadmovies)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss1_md_gc_dumbasses}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_dumbasses)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss1_md_gc_onion}\" "
			f"new ring: {os.path.getmtime(self.f_mss1_md_gc_onion)}",
			case_loggy.output
		)




		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_tasksschedule}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_tasksschedule)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_explangraph}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_explangraph)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_hardcleaning}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_hardcleaning)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_hardwashing}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_hardwashing)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_mediumcooking}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumcooking)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_mediumhomework}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumhomework)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_mediumphysicals}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_mediumphysicals)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_easyprocrastinating}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyprocrastinating)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_easyreflections}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyreflections)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss2_c_easyphilosophizing}\" "
			f"new ring: {os.path.getmtime(self.f_mss2_c_easyphilosophizing)}",
			case_loggy.output
		)




		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_f_milk}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_milk)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_f_cheese}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_cheese)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_f_meat}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_f_meat)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_o_chicken}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_o_chicken)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_o_pie}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_o_pie)}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_bread}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_bread)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb1}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb1)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb2}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb2)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb420}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb420)}",
			case_loggy.output
		)
		self.assertNotIn(

			f"DEBUG:touch_flourish:New draft peek \"{self.f_mss3_k_t_bc_crumb69}\" "
			f"new ring: {os.path.getmtime(self.f_mss3_k_t_bc_crumb69)}",
			case_loggy.output
		)




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
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
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
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))








if __name__ == "__main__" : unittest.main(verbosity=2)







