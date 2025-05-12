import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.shelve				import LibraryShelf
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import BlindPeek
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class RegularCase(EasySet):

	"""
		GrowingPeel, BlindPeek, LeafGrowth, Germination -> Rejuvenation
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_1): os.remove(cls.EASY_HANDLER_1)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_1)

	def setUp(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_1
				init_level	= 10

			@GrowingPeel
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			@GrowingPeel
			@BlindPeek("seeds", renew=False)
			class grow(LeafGrowth):		pass	# Testing with "copyfile"
			class files(Rejuvenation):	pass

			class seeds(LibraryShelf):

				grabbing	= self.EASY_SET_SEEDS
				reclaiming	= self.EASY_SET_SEEDS

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):

				class twigs(SiftingController):

					include	= (

						( os.path.join(self.EASY_SET_SPROUT, "pros"), )
						if os.name == "posix" else
						( os.path.join(self.EASY_SET_SPROUT, "pros").replace("\\", "\\\\"), )
					)
					exclude	= (

						( os.path.join(self.EASY_SET_SPROUT, "pros", ".+"), )
						if os.name == "posix" else
						( os.path.join(self.EASY_SET_SPROUT, "pros", ".+").replace("\\", "\\\\"), )
					)

				class leafs(SiftingController):

					include	= r".+\.txt$",
					exclude	= (

						( rf".+/[^/]+good.*\.txt$", )
						if os.name == "posix" else
						( rf".+\\[^\\]+good.*\.txt$", )
					)

		self.test_case = Sakura




	def test_first_flourish(self):

		self.test_case.loggy.init_name = "first_flourish"
		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		# Included file "WitchDoctor.txt"
		self.assertTrue(os.path.isfile(self.dst_file1))
		# Included folder "pros"
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		# File excluded by ".+{os.sep}[^{os.sep}]+good.*\.txt$"
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		# Files included by ".+\.txt$"
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		# Folders and files sifted out by being not included
		self.assertFalse(os.path.isdir(self.dst_cons_folder))
		self.assertFalse(os.path.isfile(self.dst_cons_file1))
		self.assertFalse(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertIn(f"INFO:first_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertIn(f"INFO:first_flourish:Thrived twig \"{self.dst_pros_folder}\"", case_loggy.output)
		self.assertIn(f"INFO:first_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertIn(f"INFO:first_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"cons\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"not so good.txt\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"redundant_folder_1\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"redundant_folder_2\"", case_loggy.output)
		self.assertNotIn(f"INFO:first_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:first_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:first_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:first_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:first_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:first_flourish:Thrived twig \"{self.dst_cons_folder}\"", case_loggy.output)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.dst_redundant_1_folder}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.dst_redundant_2_folder}\"",
			case_loggy.output
		)

		self.assertEqual(len(self.test_case.seeds),0)
		self.assertEqual(len(self.test_case.seeds()),3)
		self.assertNotIn(self.file1, self.test_case.seeds)
		self.assertNotIn(self.pros_file2, self.test_case.seeds)
		self.assertNotIn(self.pros_file3, self.test_case.seeds)
		self.assertIn(self.file1, self.test_case.seeds())
		self.assertIn(self.pros_file2, self.test_case.seeds())
		self.assertIn(self.pros_file3, self.test_case.seeds())
		self.assertFalse(os.path.isfile(self.EASY_SET_SEEDS))
		self.test_case.seeds.produce(magical=True, rewrite=True)
		self.assertTrue(

			os.path.isfile(self.EASY_SET_SEEDS)
			or
			os.path.isfile(self.EASY_SET_SEEDS + ".db")
			or
			os.path.isfile(self.EASY_SET_SEEDS + ".dat")
		)








	def test_no_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "no_touch_flourish"
		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()
			self.test_case.seeds.produce(magical=True, rewrite=True)


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertIn("DEBUG:no_touch_flourish:Shelf was not modified", case_loggy.output)
		self.assertIn("DEBUG:no_touch_flourish:Flourish stopped by blind peek comparator", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Thrived twig \"{self.dst_pros_folder}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertIn(f"DEBUG:no_touch_flourish:Sifted sprig \"cons\"", case_loggy.output)
		self.assertIn(f"DEBUG:no_touch_flourish:Sifted sprig \"not so good.txt\"", case_loggy.output)
		self.assertIn(f"DEBUG:no_touch_flourish:Sifted sprig \"redundant_folder_1\"", case_loggy.output)
		self.assertIn(f"DEBUG:no_touch_flourish:Sifted sprig \"redundant_folder_2\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:no_touch_flourish:Thrived twig \"{self.dst_cons_folder}\"", case_loggy.output)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.dst_redundant_1_folder}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Thrived twig \"{self.dst_redundant_2_folder}\"",
			case_loggy.output
		)








	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"
		self.fmake(self.pros_file3, "definitely the best way")
		self.fmake(self.cons_file1, "might cause a headache")

		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		# Included file "WitchDoctor.txt"
		self.assertTrue(os.path.isfile(self.dst_file1))
		# Included folder "pros"
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		# File excluded by ".+{os.sep}[^{os.sep}]+good.*\.txt$"
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		# Files included by ".+\.txt$"
		self.assertTrue(os.path.isfile(self.dst_pros_file2))
		self.assertTrue(os.path.isfile(self.dst_pros_file3))
		# Folders and files sifted out by being not included
		self.assertFalse(os.path.isdir(self.dst_cons_folder))
		self.assertFalse(os.path.isfile(self.dst_cons_file1))
		self.assertFalse(os.path.isfile(self.dst_cons_file2))
		self.assertFalse(os.path.isdir(self.dst_redundant_1_folder))
		self.assertFalse(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))

		self.assertIn("DEBUG:touch_flourish:Flourish stopped by blind peek comparator", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Thrived twig \"{self.dst_pros_folder}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_pros_file2}\"", case_loggy.output)
		self.assertIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_pros_file3}\"", case_loggy.output)
		self.assertIn(f"DEBUG:touch_flourish:Sifted sprig \"cons\"", case_loggy.output)
		self.assertIn(f"DEBUG:touch_flourish:Sifted sprig \"not so good.txt\"", case_loggy.output)
		self.assertIn(f"DEBUG:touch_flourish:Sifted sprig \"redundant_folder_1\"", case_loggy.output)
		self.assertIn(f"DEBUG:touch_flourish:Sifted sprig \"redundant_folder_2\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_pros_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_cons_file1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_cons_file2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_redundant_1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Grown leaf \"{self.dst_redundant_2}\"", case_loggy.output)
		self.assertNotIn(f"INFO:touch_flourish:Thrived twig \"{self.dst_cons_folder}\"", case_loggy.output)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.dst_redundant_1_folder}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Thrived twig \"{self.dst_redundant_2_folder}\"",
			case_loggy.output
		)

		self.assertEqual(len(self.test_case.seeds),3)
		self.assertEqual(len(self.test_case.seeds()),3)
		self.assertIn(self.file1, self.test_case.seeds)
		self.assertIn(self.pros_file2, self.test_case.seeds)
		self.assertIn(self.pros_file3, self.test_case.seeds)
		self.assertIn(self.file1, self.test_case.seeds())
		self.assertIn(self.pros_file2, self.test_case.seeds())
		self.assertIn(self.pros_file3, self.test_case.seeds())
		self.test_case.seeds.produce(magical=True, rewrite=True)
		self.assertTrue(

			os.path.isfile(self.EASY_SET_SEEDS)
			or
			os.path.isfile(self.EASY_SET_SEEDS + ".db")
			or
			os.path.isfile(self.EASY_SET_SEEDS + ".dat")
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







