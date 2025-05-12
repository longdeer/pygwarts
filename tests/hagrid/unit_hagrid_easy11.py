import	os
import	unittest
from	pathlib								import Path
from	shutil								import rmtree
from	shutil								import copyfile
from	time								import sleep
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.leafs		import LeafClone
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation








class LeafCloneCases(EasySet):

	"""
		GrowingPeel, Rejuvenation, cloning grow
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_11): os.remove(cls.EASY_HANDLER_11)

	@staticmethod
	def crossfs_copy(*args, **kwargs):

		copyfile(*args, **kwargs)
		raise	PermissionError("[Errno 1] Operation not permitted")

	@staticmethod
	def dontlike_copy(*args, **kwargs):
		raise	ValueError(f"I don't like \"{args[0]}\"")

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_11)

	def setUp(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_11
				init_level	= 10

			@GrowingPeel
			class grow(LeafClone):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass

		self.test_case = Sakura




	def test_clone_a_first_flourish(self):

		self.test_case.loggy.init_name = "clone_first_flourish"


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


		with self.assertLogs("clone_first_flourish", 10) as case_loggy:

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

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_first_flourish:Cloned leaf \"{self.dst_redundant_2}\"",
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








	def test_clone_a_interval_flourish(self):

		self.test_case.loggy.init_name = "clone_interval_flourish"
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


		with self.assertLogs("clone_interval_flourish", 10) as case_loggy:

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

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:clone_interval_flourish:Cloned leaf \"{self.dst_redundant_2}\"",
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








	def test_clone_b_crossfs_raise(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_11
				init_name	= "crossfs_raise"
				init_level	= 10

			@GrowingPeel
			class grow(Transmutable):

				# Actual "LeafClone" imitation with different copy function.
				# The implementation to be checked against original hagrid.planting.leafs.LeafClone!
				def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

					target	= bough.joinpath(leaf.name)
					shoot	= target.parent
					state	= target.stat().st_mtime if target.is_file() else 0


					if	leaf.is_file():
						if	not shoot.is_dir() : shoot.mkdir(parents=True)

						try:

							LeafCloneCases.crossfs_copy(leaf, target, follow_symlinks=False)
							origin.loggy.info(f"Cloned leaf \"{target}\"")


						except:
							if	target.is_file():
								if	state <target.stat().st_mtime:

									origin.loggy.info(f"Leaf \"{target}\" cloning stuck, grown instead")
									return
							raise
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


		with self.assertLogs("crossfs_raise", 10) as case_loggy:

			self.test_case = Sakura()
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

			f"INFO:crossfs_raise:Leaf \"{self.dst_file1}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_pros_file1}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_pros_file2}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_pros_file3}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_cons_file1}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_cons_file2}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_redundant_1}\" cloning stuck, grown instead",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:crossfs_raise:Leaf \"{self.dst_redundant_2}\" cloning stuck, grown instead",
			case_loggy.output
		)








	def test_clone_b_only_raise(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= self.EASY_HANDLER_11
				init_name	= "only_raise"
				init_level	= 10

			@GrowingPeel
			class grow(Transmutable):

				# Actual "LeafClone" imitation with different copy function.
				# The implementation to be checked against original hagrid.planting.leafs.LeafClone!
				def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

					target	= bough.joinpath(leaf.name)
					shoot	= target.parent
					state	= target.stat().st_mtime if target.is_file() else 0


					if	leaf.is_file():
						if	not shoot.is_dir() : shoot.mkdir(parents=True)

						try:

							LeafCloneCases.dontlike_copy(leaf, target, follow_symlinks=False)
							origin.loggy.info(f"Cloned leaf \"{target}\"")


						except:
							if	target.is_file():
								if	state <target.stat().st_mtime:

									origin.loggy.info(f"Leaf \"{target}\" cloning stuck, grown instead")
									return
							raise
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


		with self.assertLogs("only_raise", 10) as case_loggy:

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

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.file1}\" "
			f"due to ValueError: I don't like \"{self.file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.pros_file1}\" "
			f"due to ValueError: I don't like \"{self.pros_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.pros_file2}\" "
			f"due to ValueError: I don't like \"{self.pros_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.pros_file3}\" "
			f"due to ValueError: I don't like \"{self.pros_file3}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.cons_file1}\" "
			f"due to ValueError: I don't like \"{self.cons_file1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.cons_file2}\" "
			f"due to ValueError: I don't like \"{self.cons_file2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.redundant_1}\" "
			f"due to ValueError: I don't like \"{self.redundant_1}\"",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:only_raise:Failed to rejuve leaf \"{self.redundant_2}\" "
			f"due to ValueError: I don't like \"{self.redundant_2}\"",
			case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







