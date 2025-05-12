import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation








class LeafGrowthCase(EasySet):

	"""
		GrowingPeel, Rejuvenation, regular grow
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_9): os.remove(cls.EASY_HANDLER_9)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_9)


	def setUp(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_9
				init_level	= 10

			@GrowingPeel
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass

		self.test_case = Sakura




	def test_growth_first_flourish(self):

		self.test_case.loggy.init_name = "growth_first_flourish"


		self.assertTrue(os.path.isfile(self.file1))
		self.assertTrue(os.path.isdir(self.pros_folder))
		self.assertTrue(os.path.isfile(self.pros_file1))
		self.assertTrue(os.path.isfile(self.pros_file2))
		self.assertTrue(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isdir(self.cons_folder))
		self.assertTrue(os.path.isfile(self.cons_file1))
		self.assertTrue(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isdir(self.redundant_1_folder))
		self.assertTrue(os.path.isdir(self.redundant_2_folder))
		self.assertTrue(os.path.isfile(self.redundant_1))
		self.assertTrue(os.path.isfile(self.redundant_2))


		self.assertFalse(os.path.isfile(self.dst_file1))
		self.assertFalse(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertFalse(os.path.isfile(self.dst_pros_file2))
		self.assertFalse(os.path.isfile(self.dst_pros_file3))
		self.assertFalse(os.path.isdir(self.dst_cons_folder))
		self.assertFalse(os.path.isfile(self.dst_cons_file1))
		self.assertFalse(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))


		with self.assertLogs("growth_first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertTrue(os.path.isfile(self.file1))
		self.assertTrue(os.path.isdir(self.pros_folder))
		self.assertTrue(os.path.isfile(self.pros_file1))
		self.assertTrue(os.path.isfile(self.pros_file2))
		self.assertTrue(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isdir(self.cons_folder))
		self.assertTrue(os.path.isfile(self.cons_file1))
		self.assertTrue(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isdir(self.redundant_1_folder))
		self.assertTrue(os.path.isdir(self.redundant_2_folder))
		self.assertTrue(os.path.isfile(self.redundant_1))
		self.assertTrue(os.path.isfile(self.redundant_2))


		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertTrue(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertTrue(os.path.isdir(self.dst_redundant_1_folder))
		self.assertTrue(os.path.isdir(self.dst_redundant_2_folder))
		self.assertTrue(os.path.isfile(self.dst_redundant_1))
		self.assertTrue(os.path.isfile(self.dst_redundant_2))


		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_first_flourish:Grown leaf \"{self.dst_redundant_2}\"",
			case_loggy.output
		)


		self.assertEqual(

			int(os.path.getmtime(self.file1)),
			int(os.path.getmtime(self.dst_file1))
		)
		self.assertEqual(

			int(os.path.getmtime(self.pros_file1)),
			int(os.path.getmtime(self.dst_pros_file1))
		)
		self.assertEqual(

			int(os.path.getmtime(self.pros_file2)),
			int(os.path.getmtime(self.dst_pros_file2))
		)
		self.assertEqual(

			int(os.path.getmtime(self.pros_file3)),
			int(os.path.getmtime(self.dst_pros_file3))
		)
		self.assertEqual(

			int(os.path.getmtime(self.cons_file1)),
			int(os.path.getmtime(self.dst_cons_file1))
		)
		self.assertEqual(

			int(os.path.getmtime(self.cons_file2)),
			int(os.path.getmtime(self.dst_cons_file2))
		)
		self.assertEqual(

			int(os.path.getmtime(self.redundant_1)),
			int(os.path.getmtime(self.dst_redundant_1))
		)
		self.assertEqual(

			int(os.path.getmtime(self.redundant_2)),
			int(os.path.getmtime(self.dst_redundant_2))
		)








	def test_growth_interval_flourish(self):

		self.test_case.loggy.init_name = "growth_interval_flourish"
		sleep(1.5)


		self.assertTrue(os.path.isfile(self.file1))
		self.assertTrue(os.path.isdir(self.pros_folder))
		self.assertTrue(os.path.isfile(self.pros_file1))
		self.assertTrue(os.path.isfile(self.pros_file2))
		self.assertTrue(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isdir(self.cons_folder))
		self.assertTrue(os.path.isfile(self.cons_file1))
		self.assertTrue(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isdir(self.redundant_1_folder))
		self.assertTrue(os.path.isdir(self.redundant_2_folder))
		self.assertTrue(os.path.isfile(self.redundant_1))
		self.assertTrue(os.path.isfile(self.redundant_2))


		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertTrue(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertTrue(os.path.isdir(self.dst_redundant_1_folder))
		self.assertTrue(os.path.isdir(self.dst_redundant_2_folder))
		self.assertTrue(os.path.isfile(self.dst_redundant_1))
		self.assertTrue(os.path.isfile(self.dst_redundant_2))


		with self.assertLogs("growth_interval_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertTrue(os.path.isfile(self.file1))
		self.assertTrue(os.path.isdir(self.pros_folder))
		self.assertTrue(os.path.isfile(self.pros_file1))
		self.assertTrue(os.path.isfile(self.pros_file2))
		self.assertTrue(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isdir(self.cons_folder))
		self.assertTrue(os.path.isfile(self.cons_file1))
		self.assertTrue(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isdir(self.redundant_1_folder))
		self.assertTrue(os.path.isdir(self.redundant_2_folder))
		self.assertTrue(os.path.isfile(self.redundant_1))
		self.assertTrue(os.path.isfile(self.redundant_2))


		self.assertTrue(os.path.isfile(self.dst_file1))
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertTrue(os.path.isfile(self.dst_pros_file1))
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertTrue(os.path.isfile(self.dst_cons_file1))
		self.assertTrue(os.path.isfile(self.dst_cons_file2))
		self.assertTrue(os.path.isdir(self.dst_redundant_1_folder))
		self.assertTrue(os.path.isdir(self.dst_redundant_2_folder))
		self.assertTrue(os.path.isfile(self.dst_redundant_1))
		self.assertTrue(os.path.isfile(self.dst_redundant_2))


		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:growth_interval_flourish:Grown leaf \"{self.dst_redundant_2}\"",
			case_loggy.output
		)


		self.assertLess(

			int(os.path.getmtime(self.file1)),
			int(os.path.getmtime(self.dst_file1))
		)
		self.assertLess(

			int(os.path.getmtime(self.pros_file1)),
			int(os.path.getmtime(self.dst_pros_file1))
		)
		self.assertLess(

			int(os.path.getmtime(self.pros_file2)),
			int(os.path.getmtime(self.dst_pros_file2))
		)
		self.assertLess(

			int(os.path.getmtime(self.pros_file3)),
			int(os.path.getmtime(self.dst_pros_file3))
		)
		self.assertLess(

			int(os.path.getmtime(self.cons_file1)),
			int(os.path.getmtime(self.dst_cons_file1))
		)
		self.assertLess(

			int(os.path.getmtime(self.cons_file2)),
			int(os.path.getmtime(self.dst_cons_file2))
		)
		self.assertLess(

			int(os.path.getmtime(self.redundant_1)),
			int(os.path.getmtime(self.dst_redundant_1))
		)
		self.assertLess(

			int(os.path.getmtime(self.redundant_2)),
			int(os.path.getmtime(self.dst_redundant_2))
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







