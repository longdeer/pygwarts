import	os
import	unittest
from	time								import sleep
from	shutil								import rmtree
from	pygwarts.tests.hagrid				import MediumSet
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








class FullSyncCase(MediumSet):

	"""
		Distributed synchronization blind variant with shelf tracking
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_10): os.remove(cls.MEDIUM_HANDLER_10)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_10)

	def setUp(self):

		class Forest(Copse):
			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_10
				init_level	= 10

			class seeds(LibraryShelf):

				grabbing	= self.MEDIUM_SET_SEEDS
				reclaiming	= self.MEDIUM_SET_SEEDS

			class First(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class twigs(SiftingController):
					include	= (

						( rf"{self.MEDIUM_SET_BOUGH_1}/.+", rf"{self.MEDIUM_SET_SPROUT_1}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+"
						)
					)
				class leafs(SiftingController):
					include	= (

						( rf"{self.MEDIUM_SET_BOUGH_1}/.+", rf"{self.MEDIUM_SET_SPROUT_1}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+"
						)
					)

			class Second(Tree):

				bough = self.MEDIUM_SET_BOUGH_2
				class twigs(SiftingController):
					include	= (

						( rf"{self.MEDIUM_SET_BOUGH_2}/.+", rf"{self.MEDIUM_SET_SPROUT_2}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_2.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_2.replace("\\", "\\\\") + r"\\.+"
						)
					)
				class leafs(SiftingController):
					include	= (

						( rf"{self.MEDIUM_SET_BOUGH_2}/.+", rf"{self.MEDIUM_SET_SPROUT_2}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_2.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_2.replace("\\", "\\\\") + r"\\.+"
						)
					)

			class Third(Tree):

				bough = self.MEDIUM_SET_BOUGH_3
				class twigs(SiftingController):
					include	= (

						( rf"{self.MEDIUM_SET_BOUGH_3}/.+", rf"{self.MEDIUM_SET_SPROUT_3}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_3.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_3.replace("\\", "\\\\") + r"\\.+"
						)
					)
				class leafs(SiftingController):
					include	= (

						( rf"{self.MEDIUM_SET_BOUGH_3}/.+", rf"{self.MEDIUM_SET_SPROUT_3}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_3.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_3.replace("\\", "\\\\") + r"\\.+"
						)
					)

			@GrowingPeel
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			@GrowingPeel
			@BlindPeek("seeds", renew=False)
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.MEDIUM_SET_SPROUT_3)	# Order does matter cause every sprout pack it'self
			@fssprout(self.MEDIUM_SET_SPROUT_2)	# before previous sprout, so the nearest to dispatcher
			@fssprout(self.MEDIUM_SET_SPROUT_1)	# sprout will be processed first.
			class sync(Flourish):		pass
			class trim(SprigTrimmer):	pass
			class clean(Efflorescence):
				branches	= {

					self.MEDIUM_SET_BOUGH_1: ( self.MEDIUM_SET_SPROUT_1, ),
					self.MEDIUM_SET_BOUGH_2: ( self.MEDIUM_SET_SPROUT_2, ),
					self.MEDIUM_SET_BOUGH_3: ( self.MEDIUM_SET_SPROUT_3, ),
				}

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
		self.assertTrue(os.path.isdir(self.d_mss2_c))
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




		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
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




		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

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




		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))
		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
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




		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.assertEqual(len(self.test_case.seeds), 0)
			self.assertEqual(len(self.test_case.seeds()), 0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.seeds), 0)
			self.assertEqual(len(self.test_case.seeds()), 26)
			self.assertEqual(len(self.test_case.seeds.real_diff), 0)

			self.test_case.seeds.modified |= bool(self.test_case.seeds.real_diff)
			self.assertFalse(

				os.path.isfile(self.MEDIUM_SET_SEEDS)
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".db")
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat")
			)

			self.test_case.seeds.produce(magical=True, rewrite=True)
			self.assertTrue(

				os.path.isfile(self.MEDIUM_SET_SEEDS)
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".db")
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat")
			)




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(
			f"DEBUG:first_flourish:Producing Shelf \"{self.MEDIUM_SET_SEEDS}\"", case_loggy.output
		)
		self.assertIn("DEBUG:first_flourish:Source is magical Shelf with 26 keys", case_loggy.output)
		self.assertIn(

			f"INFO:first_flourish:Rewritten Shelf \"{self.MEDIUM_SET_SEEDS}\"",
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
		self.assertTrue(os.path.isdir(self.d_mss2_c))
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




		# First bough
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

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




		# Second bough
		self.assertFalse(os.path.isdir(self.d_msb2_w))
		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

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




		# Third bough
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
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




		self.assertIsInstance(self.test_case.seeds(self.f_mss1_md_rock), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss1_md_paper), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss1_md_scissors), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss1_md_gc_sadmovies), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss1_md_gc_dumbasses), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss1_md_gc_onion), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_tasksschedule), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_explangraph), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_hardcleaning), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_hardwashing), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_mediumcooking), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_mediumhomework), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_mediumphysicals), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_easyprocrastinating), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_easyreflections), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss2_c_easyphilosophizing), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_f_milk), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_f_cheese), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_f_meat), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_o_chicken), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_o_pie), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_t_bc_bread), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_t_bc_crumb1), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_t_bc_crumb2), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_t_bc_crumb420), int)
		self.assertIsInstance(self.test_case.seeds(self.f_mss3_k_t_bc_crumb69), int)
















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
		self.assertTrue(os.path.isdir(self.d_mss2_c))
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




		# First bough
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

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




		# Second bough
		self.assertFalse(os.path.isdir(self.d_msb2_w))
		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

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




		# Third bough
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
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




		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.assertEqual(len(self.test_case.seeds), 26)
			self.assertEqual(len(self.test_case.seeds()), 0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.seeds), 26)
			self.assertEqual(len(self.test_case.seeds()), 26)
			self.assertEqual(len(self.test_case.seeds.real_diff), 0)

			self.test_case.seeds.modified |= bool(self.test_case.seeds.real_diff)
			self.assertTrue(

				os.path.isfile(self.MEDIUM_SET_SEEDS)
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".db")
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat")
			)
			self.test_case.seeds.produce(magical=True, rewrite=True)
			self.assertTrue(

				os.path.isfile(self.MEDIUM_SET_SEEDS)
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".db")
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat")
			)




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn("DEBUG:no_touch_flourish:Shelf was not modified", case_loggy.output)




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
		self.assertTrue(os.path.isdir(self.d_mss2_c))
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




		# First bough
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

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




		# Second bough
		self.assertFalse(os.path.isdir(self.d_msb2_w))
		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

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




		# Third bough
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
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




		self.assertIsInstance(self.test_case.seeds[self.f_mss1_md_rock], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss1_md_paper], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss1_md_scissors], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss1_md_gc_sadmovies], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss1_md_gc_dumbasses], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss1_md_gc_onion], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_tasksschedule], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_explangraph], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_hardcleaning], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_hardwashing], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_mediumcooking], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_mediumhomework], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_mediumphysicals], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_easyprocrastinating], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_easyreflections], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss2_c_easyphilosophizing], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_f_milk], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_f_cheese], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_f_meat], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_o_chicken], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_o_pie], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_t_bc_bread], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_t_bc_crumb1], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_t_bc_crumb2], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_t_bc_crumb420], int)
		self.assertIsInstance(self.test_case.seeds[self.f_mss3_k_t_bc_crumb69], int)
















	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"

		if os.path.isdir(self.d_mss1_c_bad):			rmtree(self.d_mss1_c_bad)
		if os.path.isdir(self.d_mss1_c_badbad):			rmtree(self.d_mss1_c_badbad)
		if os.path.isdir(self.d_mss1_c_goodbad):		rmtree(self.d_mss1_c_goodbad)
		if os.path.isdir(self.d_mss2_c):				rmtree(self.d_mss2_c)
		if os.path.isfile(self.f_mss3_k_t_bc_crumb1):	os.remove(self.f_mss3_k_t_bc_crumb1)
		if os.path.isfile(self.f_mss3_k_t_bc_crumb2):	os.remove(self.f_mss3_k_t_bc_crumb2)




		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertFalse(os.path.isdir(self.d_mss2_c))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First bough
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

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




		# Second bough
		self.assertFalse(os.path.isdir(self.d_msb2_w))
		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

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




		# Third bough
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
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




		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.assertEqual(len(self.test_case.seeds), 26)
			self.assertEqual(len(self.test_case.seeds()), 0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.seeds), 26)
			self.assertEqual(len(self.test_case.seeds()), 16)
			self.assertEqual(len(self.test_case.seeds.real_diff), 10)

			for record in self.test_case.seeds.real_diff:
				self.test_case.seeds.loggy.info(f"Discarded \"{record}\" tracker")

			self.test_case.seeds.modified |= bool(self.test_case.seeds.real_diff)
			self.assertTrue(

				os.path.isfile(self.MEDIUM_SET_SEEDS)
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".db")
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat")
			)
			self.test_case.seeds.produce(magical=True, rewrite=True)
			self.assertTrue(

				os.path.isfile(self.MEDIUM_SET_SEEDS)
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".db")
				or
				os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat")
			)




		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_hardcleaning}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_hardwashing}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_mediumcooking}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_mediumhomework}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_mediumphysicals}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_easyprocrastinating}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_easyreflections}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss2_c_easyphilosophizing}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss3_k_t_bc_crumb1}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Discarded \"{self.f_mss3_k_t_bc_crumb2}\" tracker",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:touch_flourish:Producing Shelf \"{self.MEDIUM_SET_SEEDS}\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:touch_flourish:Source is magical Shelf with 16 keys",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Rewritten Shelf \"{self.MEDIUM_SET_SEEDS}\"",
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
		self.assertFalse(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertFalse(os.path.isdir(self.d_mss2_c))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))




		# First bough
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

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




		# Second bough
		self.assertFalse(os.path.isdir(self.d_msb2_w))
		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
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
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

		# Second sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))

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




		# Third bough
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
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
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))








if __name__ == "__main__" : unittest.main(verbosity=2)







