import	os
import	unittest
from	pathlib								import Path
from	shutil								import rmtree
from	time								import sleep
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.leafs		import LeafMove
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation








class LeafMoveCase(EasySet):

	"""
		GrowingPeel, Rejuvenation, moving grow
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_10): os.remove(cls.EASY_HANDLER_10)

	@staticmethod
	def empty_copy(*args, **kwargs): pass
	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_10)

	def setUp(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_10
				init_level	= 10

			@GrowingPeel
			class grow(LeafMove):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass

		self.fmake(self.file1, "OOH EEH OOH AH AH TING TANG WALA WALA BING BANG")
		self.fmake(self.pros_file1, "may be ain't best way")
		self.fmake(self.pros_file2, "probably the best way")
		self.fmake(self.pros_file3, "definitely the best way")
		self.fmake(self.cons_file1, "might cause a headache")
		self.fmake(self.cons_file2, "annihilation")
		self.fmake(self.redundant_1, "no use 1")
		self.fmake(self.redundant_2, "no use 2")
		self.test_case = Sakura




	def test_move_a_first_flourish(self):

		self.test_case.loggy.init_name = "move_first_flourish"


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


		with self.assertLogs("move_first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertFalse(os.path.isfile(self.file1))
		self.assertTrue(os.path.isdir(self.pros_folder))
		self.assertFalse(os.path.isfile(self.pros_file1))
		self.assertFalse(os.path.isfile(self.pros_file2))
		self.assertFalse(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isdir(self.cons_folder))
		self.assertFalse(os.path.isfile(self.cons_file1))
		self.assertFalse(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isdir(self.redundant_1_folder))
		self.assertTrue(os.path.isdir(self.redundant_2_folder))
		self.assertFalse(os.path.isfile(self.redundant_1))
		self.assertFalse(os.path.isfile(self.redundant_2))


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

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_first_flourish:Moved leaf \"{self.dst_redundant_2}\"",
			case_loggy.output
		)








	def test_move_b_interval_flourish(self):

		self.test_case.loggy.init_name = "move_interval_flourish"
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


		with self.assertLogs("move_interval_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()


		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertFalse(os.path.isfile(self.file1))
		self.assertTrue(os.path.isdir(self.pros_folder))
		self.assertFalse(os.path.isfile(self.pros_file1))
		self.assertFalse(os.path.isfile(self.pros_file2))
		self.assertFalse(os.path.isfile(self.pros_file3))
		self.assertTrue(os.path.isdir(self.cons_folder))
		self.assertFalse(os.path.isfile(self.cons_file1))
		self.assertFalse(os.path.isfile(self.cons_file2))
		self.assertTrue(os.path.isdir(self.redundant_1_folder))
		self.assertTrue(os.path.isdir(self.redundant_2_folder))
		self.assertFalse(os.path.isfile(self.redundant_1))
		self.assertFalse(os.path.isfile(self.redundant_2))


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

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_interval_flourish:Moved leaf \"{self.dst_redundant_2}\"",
			case_loggy.output
		)








	def test_move_c_empty(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_10
				init_name	= "move_c_empty"
				init_level	= 10

			@GrowingPeel
			class grow(Transmutable):

				# Actual "LeafMove" imitation with different copy function.
				# The implementation to be checked against original hagrid.planting.leafs.LeafMove!
				def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

					target	= bough.joinpath(leaf.name)
					shoot	= target.parent


					if	leaf.is_file():
						if	not shoot.is_dir() : shoot.mkdir(parents=True)

						LeafMoveCase.empty_copy(leaf, target, follow_symlinks=False)

						if	target.is_file():

							leaf.unlink()
							origin.loggy.info(f"Moved leaf \"{target}\"")
						else:
							origin.loggy.info(f"Leaf \"{target}\" move failed")
					else:	origin.loggy.debug(f"Branch \"{leaf}\" not located")

			class files(Rejuvenation):	pass

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		if	os.path.isdir(self.EASY_SET_BOUGH): rmtree(self.EASY_SET_BOUGH)
		os.makedirs(self.EASY_SET_BOUGH, exist_ok=True)


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


		with self.assertLogs("move_c_empty", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync()


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
		self.assertTrue(os.path.isdir(self.dst_pros_folder))
		self.assertFalse(os.path.isfile(self.dst_pros_file1))
		self.assertFalse(os.path.isfile(self.dst_pros_file2))
		self.assertFalse(os.path.isfile(self.dst_pros_file3))
		self.assertTrue(os.path.isdir(self.dst_cons_folder))
		self.assertFalse(os.path.isfile(self.dst_cons_file1))
		self.assertFalse(os.path.isfile(self.dst_cons_file2))
		self.assertTrue(os.path.isdir(self.dst_redundant_1_folder))
		self.assertTrue(os.path.isdir(self.dst_redundant_2_folder))
		self.assertFalse(os.path.isfile(self.dst_redundant_1))
		self.assertFalse(os.path.isfile(self.dst_redundant_2))


		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_file1}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_pros_file1}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_pros_file2}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_pros_file3}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_cons_file1}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_cons_file2}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_redundant_1}\" move failed",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:move_c_empty:Leaf \"{self.dst_redundant_2}\" move failed",
			case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







