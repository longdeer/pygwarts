import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Transfer
from	pygwarts.hagrid.planting.leafs		import LeafMove
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.peels		import ThrivingPeel
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class TransferCase(EasySet):

	"""
		ThrivingPeel, Germination -> Transfer
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_4): os.remove(cls.EASY_HANDLER_4)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_4)


	def setUp(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_4
				init_level	= 10

			@ThrivingPeel("today", "records", to_peak=False)
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			@ThrivingPeel("today", "records", to_peak=False)
			class graft(LeafMove):		pass
			class files(Transfer):		pass

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
						( rf".+\\[^(\\)]+good.*\.txt$", )
					)

		self.test_case = Sakura


	def fdthriving(self, dst :str) -> str :

		"""
			Makes destination file/folder path according to hardcoded thriving
		"""

		return	os.path.join(
			self.EASY_SET_BOUGH, "today", "records", os.path.relpath(dst, self.EASY_SET_BOUGH)
		)




	def test_first_flourish(self):

		self.test_case.loggy.init_name = "first_flourish"
		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		# Included file "WitchDoctor.txt"
		self.assertTrue(os.path.isfile(self.fdthriving(self.dst_file1)))
		# Included folder "pros"
		self.assertTrue(os.path.isdir(self.fdthriving(self.dst_pros_folder)))
		# File excluded by ".+{os.sep}[^{os.sep}]+good.*\.txt$"
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_pros_file1)))
		# Files included by ".+\.txt$"
		self.assertTrue(os.path.isfile(self.fdthriving(self.dst_pros_file2)))
		self.assertTrue(os.path.isfile(self.fdthriving(self.dst_pros_file3)))
		# Folders and files sifted out by being not included
		self.assertFalse(os.path.isdir(self.fdthriving(self.dst_cons_folder)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_cons_file1)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_cons_file2)))
		self.assertFalse(os.path.isdir(self.fdthriving(self.dst_redundant_1_folder)))
		self.assertFalse(os.path.isdir(self.fdthriving(self.dst_redundant_2_folder)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_redundant_1)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_redundant_2)))

		self.assertFalse(os.path.isfile(self.file1))
		self.assertTrue(os.path.isfile(self.pros_file1))
		self.assertFalse(os.path.isfile(self.pros_file2))
		self.assertFalse(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isfile(self.cons_file1))
		self.assertTrue(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isfile(self.redundant_1))
		self.assertTrue(os.path.isfile(self.redundant_2))

		self.assertIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_file1)}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Thrived twig \"{self.fdthriving(self.dst_pros_folder)}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_pros_file2)}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_pros_file3)}\"",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"cons\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"not so good.txt\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"redundant_folder_1\"", case_loggy.output)
		self.assertIn(f"DEBUG:first_flourish:Sifted sprig \"redundant_folder_2\"", case_loggy.output)
		self.assertNotIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_pros_file1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_cons_file1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_cons_file2)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_redundant_1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Moved leaf \"{self.fdthriving(self.dst_redundant_2)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.fdthriving(self.dst_cons_folder)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.fdthriving(self.dst_redundant_1_folder)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:first_flourish:Thrived twig \"{self.fdthriving(self.dst_redundant_2_folder)}\"",
			case_loggy.output
		)








	def test_second_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "second_flourish"
		with self.assertLogs("second_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		# Included file "WitchDoctor.txt"
		self.assertTrue(os.path.isfile(self.fdthriving(self.dst_file1)))
		# Included folder "pros"
		self.assertTrue(os.path.isdir(self.fdthriving(self.dst_pros_folder)))
		# File excluded by ".+{os.sep}[^{os.sep}]+good.*\.txt$"
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_pros_file1)))
		# Files included by ".+\.txt$"
		self.assertTrue(os.path.isfile(self.fdthriving(self.dst_pros_file2)))
		self.assertTrue(os.path.isfile(self.fdthriving(self.dst_pros_file3)))
		# Folders and files sifted out by being not included
		self.assertFalse(os.path.isdir(self.fdthriving(self.dst_cons_folder)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_cons_file1)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_cons_file2)))
		self.assertFalse(os.path.isdir(self.fdthriving(self.dst_redundant_1_folder)))
		self.assertFalse(os.path.isdir(self.fdthriving(self.dst_redundant_2_folder)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_redundant_1)))
		self.assertFalse(os.path.isfile(self.fdthriving(self.dst_redundant_2)))

		self.assertFalse(os.path.isfile(self.file1))
		self.assertTrue(os.path.isfile(self.pros_file1))
		self.assertFalse(os.path.isfile(self.pros_file2))
		self.assertFalse(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isfile(self.cons_file1))
		self.assertTrue(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isfile(self.redundant_1))
		self.assertTrue(os.path.isfile(self.redundant_2))

		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_file1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Thrived twig \"{self.fdthriving(self.dst_pros_folder)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_pros_file2)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_pros_file3)}\"",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:second_flourish:Sifted sprig \"cons\"", case_loggy.output)
		self.assertIn(f"DEBUG:second_flourish:Sifted sprig \"not so good.txt\"", case_loggy.output)
		self.assertIn(f"DEBUG:second_flourish:Sifted sprig \"redundant_folder_1\"", case_loggy.output)
		self.assertIn(f"DEBUG:second_flourish:Sifted sprig \"redundant_folder_2\"", case_loggy.output)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_pros_file1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_cons_file1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_cons_file2)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_redundant_1)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Moved leaf \"{self.fdthriving(self.dst_redundant_2)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Thrived twig \"{self.fdthriving(self.dst_cons_folder)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Thrived twig \"{self.fdthriving(self.dst_redundant_1_folder)}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:second_flourish:Thrived twig \"{self.fdthriving(self.dst_redundant_2_folder)}\"",
			case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







