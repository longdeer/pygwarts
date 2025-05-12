import	os
import	unittest
from	pathlib									import Path
from	typing									import Dict
from	pygwarts.tests.hagrid					import MediumSet
from	pygwarts.irma.contrib					import LibraryContrib
from	pygwarts.irma.shelve					import LibraryShelf
from	pygwarts.hagrid.thrivables				import Tree
from	pygwarts.hagrid.sprouts					import fssprout
from	pygwarts.hagrid.planting				import Flourish
from	pygwarts.hagrid.cultivation.registering	import PlantRegister
from	pygwarts.hagrid.cultivation.registering	import TG
from	pygwarts.hagrid.cultivation.registering	import LG
from	pygwarts.hagrid.cultivation.registering	import WG
from	pygwarts.hagrid.cultivation.registering	import TL
from	pygwarts.hagrid.cultivation.registering	import LL
from	pygwarts.hagrid.cultivation.registering	import WL








class RegisteringCases(MediumSet):

	"""
		Complex testing of cultivation.registering functionality
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_8): os.remove(cls.MEDIUM_HANDLER_8)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_8)

	def measures_fields_types_check(self, folder :Dict[str,int]):

		self.assertIsInstance(folder.get(TG), int)
		self.assertIsInstance(folder.get(LG), int)
		self.assertIsInstance(folder.get(WG), int)
		self.assertIsInstance(folder.get(TL), int)
		self.assertIsInstance(folder.get(LL), int)
		self.assertIsInstance(folder.get(WL), int)

	def all_sources_exists(self):

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

	def first_sprout_real(self):

		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_1), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_1)), 2)
		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_1).get(self.d_mss1_md), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_md]), 4)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_md].get(self.f_mss1_md_rock), int
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_md].get(self.f_mss1_md_paper), int
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_md].get(self.f_mss1_md_scissors), int
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_md].get(self.d_mss1_md_gc), dict
		)
		self.assertEqual(
			len(self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_md][self.d_mss1_md_gc]), 3
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_1
			)[	self.d_mss1_md
			][	self.d_mss1_md_gc].get(self.f_mss1_md_gc_sadmovies), int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_1
			)[	self.d_mss1_md
			][	self.d_mss1_md_gc].get(self.f_mss1_md_gc_dumbasses), int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_1
			)[	self.d_mss1_md
			][	self.d_mss1_md_gc].get(self.f_mss1_md_gc_onion), int
		)
		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_1).get(self.d_mss1_c), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c]), 8)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_good), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_good
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_notgood), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_notgood
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_bad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_bad
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_notbad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_notbad
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_notnot), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_notnot
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_badbad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_badbad
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_badgood), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_badgood
				]
			),		0
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_1)[self.d_mss1_c].get(self.d_mss1_c_goodbad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(

					self.MEDIUM_SET_SPROUT_1
				)[	self.d_mss1_c
				][	self.d_mss1_c_goodbad
				]
			),		0
		)

	def second_sprout_real(self):

		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_2), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_2)), 3)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_2).get(self.f_mss2_tasksschedule), int
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_2).get(self.f_mss2_explangraph), int
		)
		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_2).get(self.d_mss2_c), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c]), 8)
		self.assertIsInstance(

			self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c].get(self.f_mss2_c_hardcleaning),
			int
		)
		self.assertIsInstance(

			self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c].get(self.f_mss2_c_hardwashing),
			int
		)
		self.assertIsInstance(

			self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c].get(self.f_mss2_c_mediumcooking),
			int
		)
		self.assertIsInstance(

			self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c].get(self.f_mss2_c_mediumhomework),
			int
		)
		self.assertIsInstance(

			self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c].get(self.f_mss2_c_mediumphysicals),
			int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_2
			)[	self.d_mss2_c
			].get(
				self.f_mss2_c_easyprocrastinating
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(self.MEDIUM_SET_SPROUT_2)[self.d_mss2_c].get(self.f_mss2_c_easyreflections),
			int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_2
			)[	self.d_mss2_c
			].get(
				self.f_mss2_c_easyphilosophizing
			),	int
		)

	def third_sprout_real(self):

		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_3), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_3)), 1)
		self.assertIsInstance(self.test_case.garden(self.MEDIUM_SET_SPROUT_3).get(self.d_mss3_k), dict)
		self.assertEqual(len(self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k]), 3)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k].get(self.d_mss3_k_f), dict
		)
		self.assertEqual(
			len(self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k][self.d_mss3_k_f]), 3
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_f
			].get(
				self.f_mss3_k_f_milk
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_f
			].get(
				self.f_mss3_k_f_cheese
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_f
			].get(
				self.f_mss3_k_f_meat
			),	int
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k].get(self.d_mss3_k_o), dict
		)
		self.assertEqual(
			len(self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k][self.d_mss3_k_o]), 2
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_o
			].get(
				self.f_mss3_k_o_chicken
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_o
			].get(
				self.f_mss3_k_o_pie
			),	int
		)
		self.assertIsInstance(
			self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k].get(self.d_mss3_k_t), dict
		)
		self.assertEqual(
			len(self.test_case.garden(self.MEDIUM_SET_SPROUT_3)[self.d_mss3_k][self.d_mss3_k_t]), 1
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_t
			].get(
				self.d_mss3_k_t_bc
			),	dict
		)
		self.assertEqual(
			len(
				self.test_case.garden(
					self.MEDIUM_SET_SPROUT_3
				)[	self.d_mss3_k
				][	self.d_mss3_k_t
				][	self.d_mss3_k_t_bc
				]
			),	5
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_t
			][	self.d_mss3_k_t_bc
			].get(
				self.f_mss3_k_t_bc_bread
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_t
			][	self.d_mss3_k_t_bc
			].get(
				self.f_mss3_k_t_bc_crumb1
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_t
			][	self.d_mss3_k_t_bc
			].get(
				self.f_mss3_k_t_bc_crumb2
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_t
			][	self.d_mss3_k_t_bc
			].get(
				self.f_mss3_k_t_bc_crumb420
			),	int
		)
		self.assertIsInstance(

			self.test_case.garden(

				self.MEDIUM_SET_SPROUT_3
			)[	self.d_mss3_k
			][	self.d_mss3_k_t
			][	self.d_mss3_k_t_bc
			].get(
				self.f_mss3_k_t_bc_crumb69
			),	int
		)

	def first_sprout_magical(self):

		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_1], dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_1]), 8)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_1])
		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_1].get(self.d_mss1_md), dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_md]), 7)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_md])
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_md].get(self.d_mss1_md_gc), dict
		)
		self.assertEqual(
			len(self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_md][self.d_mss1_md_gc]), 6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_md][self.d_mss1_md_gc]
		)
		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_1].get(self.d_mss1_c), dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c]), 14)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c])
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_good), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_good]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_good]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_notgood), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_notgood]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_notgood]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_bad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_bad]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_bad]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_notbad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_notbad]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_notbad]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_notnot), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_notnot]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_notnot]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_badbad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_badbad]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_badbad]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_badgood), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_badgood]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_badgood]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c].get(self.d_mss1_c_goodbad), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_1][
				self.d_mss1_c][
				self.d_mss1_c_goodbad]
			),	6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_1][self.d_mss1_c][self.d_mss1_c_goodbad]
		)


	def second_sprout_magical(self):

		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_2], dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_2]), 7)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_2])
		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_2].get(self.d_mss2_c), dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_2][self.d_mss2_c]), 6)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_2][self.d_mss2_c])


	def third_sprout_magical(self):

		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_3], dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_3]), 7)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_3])
		self.assertIsInstance(self.test_case.garden[self.MEDIUM_SET_SPROUT_3].get(self.d_mss3_k), dict)
		self.assertEqual(len(self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k]), 9)
		self.measures_fields_types_check(self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k])
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k].get(self.d_mss3_k_f), dict
		)
		self.assertEqual(
			len(self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k][self.d_mss3_k_f]), 6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k][self.d_mss3_k_f]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k].get(self.d_mss3_k_o), dict
		)
		self.assertEqual(
			len(self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k][self.d_mss3_k_o]), 6
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k][self.d_mss3_k_o]
		)
		self.assertIsInstance(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k].get(self.d_mss3_k_t), dict
		)
		self.assertEqual(
			len(self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k][self.d_mss3_k_t]), 7
		)
		self.measures_fields_types_check(
			self.test_case.garden[self.MEDIUM_SET_SPROUT_3][self.d_mss3_k][self.d_mss3_k_t]
		)
		self.assertIsInstance(

			self.test_case.garden[
			self.MEDIUM_SET_SPROUT_3][
			self.d_mss3_k][
			self.d_mss3_k_t].get(self.d_mss3_k_t_bc), dict
		)
		self.assertEqual(
			len(
				self.test_case.garden[
				self.MEDIUM_SET_SPROUT_3][
				self.d_mss3_k][
				self.d_mss3_k_t][
				self.d_mss3_k_t_bc]
			),	6
		)
		self.measures_fields_types_check(

			self.test_case.garden[
			self.MEDIUM_SET_SPROUT_3][
			self.d_mss3_k][
			self.d_mss3_k_t][
			self.d_mss3_k_t_bc]
		)




	def test_bottom_register(self):
		class Sakura(Tree):

			class loggy(LibraryContrib):

				init_name	= "bottom_register"
				init_level	= 10
				handler		= self.MEDIUM_HANDLER_8

			@fssprout(self.MEDIUM_SET_SPROUT_1)
			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_3)
			@PlantRegister("garden")
			class sync(Flourish):		pass
			class garden(LibraryShelf):	pass


		self.test_case = Sakura()
		self.test_case.sync()


		self.all_sources_exists()
		self.assertEqual(len(self.test_case.garden), 3)
		self.assertEqual(len(self.test_case.garden()), 3)


		self.first_sprout_real()
		self.second_sprout_real()
		self.third_sprout_real()
		self.first_sprout_magical()
		self.second_sprout_magical()
		self.third_sprout_magical()




	def test_middle_register(self):
		class Sakura(Tree):

			class loggy(LibraryContrib):

				init_name	= "middle_register"
				init_level	= 10
				handler		= self.MEDIUM_HANDLER_8

			@fssprout(self.MEDIUM_SET_SPROUT_1)
			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@PlantRegister("garden")
			@fssprout(self.MEDIUM_SET_SPROUT_3)
			class sync(Flourish):		pass
			class garden(LibraryShelf):	pass


		self.test_case = Sakura()
		self.test_case.sync()


		self.all_sources_exists()
		self.assertEqual(len(self.test_case.garden), 2)
		self.assertEqual(len(self.test_case.garden()), 2)


		self.first_sprout_real()
		self.second_sprout_real()
		self.first_sprout_magical()
		self.second_sprout_magical()


		self.assertIsNone(self.test_case.garden[self.MEDIUM_SET_SPROUT_3])
		self.assertIsNone(self.test_case.garden()[self.MEDIUM_SET_SPROUT_3])




	def test_upper_register(self):
		class Sakura(Tree):

			class loggy(LibraryContrib):

				init_name	= "upper_register"
				init_level	= 10
				handler		= self.MEDIUM_HANDLER_8

			@PlantRegister("garden")
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_3)
			class sync(Flourish):		pass
			class garden(LibraryShelf):	pass


		self.test_case = Sakura()
		self.test_case.sync()


		self.all_sources_exists()
		self.assertEqual(len(self.test_case.garden), 0)
		self.assertEqual(len(self.test_case.garden()), 0)


		self.assertIsNone(self.test_case.garden[self.MEDIUM_SET_SPROUT_1])
		self.assertIsNone(self.test_case.garden[self.MEDIUM_SET_SPROUT_2])
		self.assertIsNone(self.test_case.garden[self.MEDIUM_SET_SPROUT_3])
		self.assertIsNone(self.test_case.garden()[self.MEDIUM_SET_SPROUT_1])
		self.assertIsNone(self.test_case.garden()[self.MEDIUM_SET_SPROUT_2])
		self.assertIsNone(self.test_case.garden()[self.MEDIUM_SET_SPROUT_3])




	def test_free_register(self):
		class Sakura(Tree):

			class loggy(LibraryContrib):

				init_name	= "free_register"
				init_level	= 10
				handler		= self.MEDIUM_HANDLER_8

			@PlantRegister("garden")
			class sync(Flourish):		pass
			class garden(LibraryShelf):	pass


		self.test_case = Sakura()
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_1,
			Path(self.MEDIUM_SET_SPROUT_1),
			[ Path(self.d_mss1_md), Path(self.d_mss1_c) ],
			[]
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_1,
			Path(self.d_mss1_md),
			[ Path(self.d_mss1_md_gc) ],
			[
				Path(self.f_mss1_md_rock),
				Path(self.f_mss1_md_paper),
				Path(self.f_mss1_md_scissors),
			]
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_1,
			Path(self.d_mss1_md_gc),
			[],
			[
				Path(self.f_mss1_md_gc_sadmovies),
				Path(self.f_mss1_md_gc_dumbasses),
				Path(self.f_mss1_md_gc_onion),
			]
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_1,
			Path(self.d_mss1_c),
			[
				Path(self.d_mss1_c_good),
				Path(self.d_mss1_c_notgood),
				Path(self.d_mss1_c_bad),
				Path(self.d_mss1_c_notbad),
				Path(self.d_mss1_c_notnot),
				Path(self.d_mss1_c_badbad),
				Path(self.d_mss1_c_badgood),
				Path(self.d_mss1_c_goodbad),
			],
			[]
		)
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_good), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_notgood), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_bad), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_notbad), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_notnot), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_badbad), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_badgood), [], [])
		self.test_case.sync(self.MEDIUM_SET_SPROUT_1, Path(self.d_mss1_c_goodbad), [], [])


		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_2,
			Path(self.MEDIUM_SET_SPROUT_2),
			[ Path(self.d_mss2_c) ],
			[ Path(self.f_mss2_tasksschedule), Path(self.f_mss2_explangraph) ]
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_2,
			Path(self.d_mss2_c),
			[],
			[
				Path(self.f_mss2_c_hardcleaning),
				Path(self.f_mss2_c_hardwashing),
				Path(self.f_mss2_c_mediumcooking),
				Path(self.f_mss2_c_mediumhomework),
				Path(self.f_mss2_c_mediumphysicals),
				Path(self.f_mss2_c_easyprocrastinating),
				Path(self.f_mss2_c_easyreflections),
				Path(self.f_mss2_c_easyphilosophizing)
			]
		)


		self.test_case.sync(
			self.MEDIUM_SET_SPROUT_3, Path(self.MEDIUM_SET_SPROUT_3), [ Path(self.d_mss3_k) ], []
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_3,
			Path(self.d_mss3_k),
			[ Path(self.d_mss3_k_f), Path(self.d_mss3_k_o), Path(self.d_mss3_k_t) ],
			[]
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_3,
			Path(self.d_mss3_k_f),
			[],
			[ Path(self.f_mss3_k_f_milk), Path(self.f_mss3_k_f_cheese), Path(self.f_mss3_k_f_meat) ]
		)
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_3,
			Path(self.d_mss3_k_o),
			[],
			[ Path(self.f_mss3_k_o_chicken), Path(self.f_mss3_k_o_pie) ]
		)
		self.test_case.sync(self.MEDIUM_SET_SPROUT_3, Path(self.d_mss3_k_t), [ Path(self.d_mss3_k_t_bc) ], [])
		self.test_case.sync(

			self.MEDIUM_SET_SPROUT_3,
			Path(self.d_mss3_k_t_bc),
			[],
			[
				Path(self.f_mss3_k_t_bc_bread),
				Path(self.f_mss3_k_t_bc_crumb1),
				Path(self.f_mss3_k_t_bc_crumb2),
				Path(self.f_mss3_k_t_bc_crumb420),
				Path(self.f_mss3_k_t_bc_crumb69)
			]
		)


		self.first_sprout_real()
		self.second_sprout_real()
		self.third_sprout_real()
		self.first_sprout_magical()
		self.second_sprout_magical()
		self.third_sprout_magical()








if __name__ == "__main__" : unittest.main(verbosity=2)







