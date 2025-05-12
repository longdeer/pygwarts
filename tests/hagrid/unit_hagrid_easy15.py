import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import DraftPeek
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class RenewalCase(EasySet):

	"""
		Renew peeks and adding files
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_15): os.remove(cls.EASY_HANDLER_15)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_15)

		cls.fmake(cls, cls.dst_pros_file2)
		cls.fmake(cls, cls.dst_pros_file3)
		cls.fmake(cls, cls.dst_cons_file1)
		cls.fmake(cls, cls.dst_cons_file2)


	def test_1_first_flourish(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_15
				init_name	= "1_first_flourish"
				init_level	= 10

			class Renewal(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=True)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

			class Adding(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=False)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass
				class leafs(SiftingController):

					include	= "",

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):			pass

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		with self.assertLogs("1_first_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:1_first_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)








	def test_2_touch_flourish(self):
		sleep(1.1)

		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_15
				init_name	= "2_touch_flourish"
				init_level	= 10

			class Renewal(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=True)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

			class Adding(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=False)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass
				class leafs(SiftingController):

					include	= "",

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):			pass

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.fmake(self.pros_file2)
		self.fmake(self.cons_file1)

		with self.assertLogs("2_touch_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertNotIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)

		self.assertEqual(
			case_loggy.output.count(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_pros_file2}\""),1
		)
		self.assertEqual(
			case_loggy.output.count(f"INFO:2_touch_flourish:Grown leaf \"{self.dst_cons_file1}\""),1
		)








	def test_3_no_touch_flourish(self):
		sleep(1.1)

		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_15
				init_name	= "3_no_touch_flourish"
				init_level	= 10

			class Renewal(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=True)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

			class Adding(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=False)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass
				class leafs(SiftingController):

					include	= "",

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):			pass

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		with self.assertLogs("3_no_touch_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:3_no_touch_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)








	def test_4_add_flourish(self):
		sleep(1.1)

		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_15
				init_name	= "4_add_flourish"
				init_level	= 10

			class Renewal(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=True)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

			class Adding(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=False)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass
				class leafs(SiftingController):

					include	= self.file1.replace("\\", "\\\\"),

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):			pass

		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		with self.assertLogs("4_add_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)

		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:4_add_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)

		self.assertEqual(
			case_loggy.output.count(f"INFO:4_add_flourish:Grown leaf \"{self.dst_file1}\""),1
		)








	def test_5_remove_flourish(self):
		sleep(1.1)

		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_15
				init_name	= "5_remove_flourish"
				init_level	= 10

			class Renewal(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=True)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

			class Adding(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=False)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass
				class leafs(SiftingController):

					include	= self.file1.replace("\\", "\\\\"),

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):			pass

		os.remove(self.dst_pros_file2)
		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertFalse(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		with self.assertLogs("5_remove_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)

		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertFalse(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:5_remove_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)








	def test_6_touch_flourish(self):
		sleep(1.1)

		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_15
				init_name	= "6_touch_flourish"
				init_level	= 10

			class Adding(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=False)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass
				class leafs(SiftingController):

					include	= self.file1.replace("\\", "\\\\"),

			class Renewal(Tree):

				bough = self.EASY_SET_BOUGH
				@GrowingPeel
				@DraftPeek(renew=True)
				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):			pass

		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertFalse(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.fmake(self.file1)
		self.fmake(self.pros_file1)
		self.fmake(self.pros_file2)
		self.fmake(self.pros_file3)
		self.fmake(self.cons_file1)
		self.fmake(self.cons_file2)
		self.fmake(self.redundant_1)
		self.fmake(self.redundant_2)

		with self.assertLogs("6_touch_flourish", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)

		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertFalse(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)

		self.assertEqual(
			case_loggy.output.count(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_file1}\"",), 1
		)
		self.assertEqual(
			case_loggy.output.count(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_pros_file3}\"",), 1
		)
		self.assertEqual(
			case_loggy.output.count(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_cons_file1}\"",), 1
		)
		self.assertEqual(
			case_loggy.output.count(f"INFO:6_touch_flourish:Grown leaf \"{self.dst_cons_file2}\"",), 1
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







