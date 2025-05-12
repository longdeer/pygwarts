import	os
import	unittest
from	pathlib							import Path
from	shutil							import rmtree
from	pygwarts.tests.hagrid			import HagridTestCase
from	pygwarts.irma.contrib			import LibraryContrib
from	pygwarts.hagrid.thrivables		import Tree
from	pygwarts.hagrid.thrivables		import Copse
from	pygwarts.hagrid.sprouts			import fssprout
from	pygwarts.hagrid.planting		import Flourish
from	pygwarts.hagrid.bloom.twigs		import Germination
from	pygwarts.hagrid.bloom.leafs		import Rejuvenation
from	pygwarts.hagrid.planting.leafs	import LeafGrowth
from	pygwarts.hagrid.planting.twigs	import TwigThrive








class InitCase(HagridTestCase):

	"""
		Some initiation cases.
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.INIT_HANDLER): os.remove(cls.INIT_HANDLER)

		if	os.path.isdir(cls.INIT_SET_BOUGH_1):	rmtree(cls.INIT_SET_BOUGH_1)
		if	os.path.isdir(cls.INIT_SET_BOUGH_2):	rmtree(cls.INIT_SET_BOUGH_2)
		if	os.path.isdir(cls.INIT_SET_BOUGH_3):	rmtree(cls.INIT_SET_BOUGH_3)
		if	os.path.isdir(cls.INIT_SET_SPROUT):		rmtree(cls.INIT_SET_SPROUT)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.INIT_HANDLER)
		if	os.path.isdir(cls.INIT_SET_BOUGH_1):		rmtree(cls.INIT_SET_BOUGH_1)
		if	os.path.isdir(cls.INIT_SET_BOUGH_2):		rmtree(cls.INIT_SET_BOUGH_2)
		if	not os.path.isdir(cls.INIT_SET_SPROUT):		os.makedirs(cls.INIT_SET_SPROUT)
		if	not os.path.isdir(cls.INIT_SET_BOUGH_3):	os.makedirs(cls.INIT_SET_BOUGH_3)




	def test_no_bough_tree(self):
		class Sakura(Tree):

			class loggy(LibraryContrib):

				handler		= self.INIT_HANDLER
				init_name	= "no_bough_tree"
				init_level	= 10

			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.INIT_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("no_bough_tree", 10) as case_loggy:

			self.test_case = Sakura()
			self.assertIn("DEBUG:no_bough_tree:Sakura tree affected", case_loggy.output)
			self.assertIn(

				"DEBUG:no_bough_tree:Spreading complete, number of affected trees: 1",
				case_loggy.output
			)
			self.assertIn(

				"ERROR:no_bough_tree:Tree Sakura can't thrive due to "
				"AttributeError: Attribute 'bough' has no escalation to Sakura",
				case_loggy.output
			)
			self.assertIn("DEBUG:no_bough_tree:Discarded", case_loggy.output)
			self.assertEqual(len(self.test_case),0)








	def test_invalid_bough_tree(self):
		class Sakura(Tree):

			bough	= 42
			class loggy(LibraryContrib):

				handler		= self.INIT_HANDLER
				init_name	= "invalid_bough_tree"
				init_level	= 10

			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.INIT_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("invalid_bough_tree", 10) as case_loggy:

			self.test_case = Sakura()
			self.assertIn("DEBUG:invalid_bough_tree:Sakura tree affected", case_loggy.output)
			self.assertIn(

				"DEBUG:invalid_bough_tree:Spreading complete, number of affected trees: 1",
				case_loggy.output
			)
			self.assertIn(f"INFO:invalid_bough_tree:Bough \"42\" is invalid", case_loggy.output)
			self.assertIn("DEBUG:invalid_bough_tree:Discarded", case_loggy.output)
			self.assertEqual(len(self.test_case),0)








	def test_uncreatable_bough_tree(self):

		# It was hard and unsuccessfull work to find unwritable by default folder in windows10
		if os.name == "posix":

			class Sakura(Tree):

				# The path which hagrid won't be able to create, likely cause of permissions.
				bough	= "/mnt/notcreation"
				class loggy(LibraryContrib):

					handler		= self.INIT_HANDLER
					init_name	= "uncreatable_bough_tree"
					init_level	= 10
				strict_thrive	= False

				class thrive(TwigThrive):	pass
				class folders(Germination):	pass

				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

				@fssprout(self.INIT_SET_SPROUT)
				class sync(Flourish):		pass


			with self.assertLogs("uncreatable_bough_tree", 10) as case_loggy:

				self.test_case = Sakura()
				self.assertIn("DEBUG:uncreatable_bough_tree:Sakura tree affected", case_loggy.output)
				self.assertIn(

					"DEBUG:uncreatable_bough_tree:Spreading complete, number of affected trees: 1",
					case_loggy.output
				)
				# Perhaps on different systems PermissionError raise may differ...
				self.assertIn(

					"ERROR:uncreatable_bough_tree:"
					f"Tree {self.test_case} can't thrive due to "
					f"PermissionError: [Errno 13] Permission denied: '{self.test_case.bough}'",
					case_loggy.output
				)
				self.assertIn("DEBUG:uncreatable_bough_tree:Discarded", case_loggy.output)
				self.assertEqual(len(self.test_case),0)








	def test_unwritable_bough_tree(self):

		# It was hard and unsuccessfull work to find unwritable by default folder in windows10
		if os.name == "posix":

			class Sakura(Tree):

				# Existent directory in which we cannot create folders/files
				bough	= "/mnt"
				class loggy(LibraryContrib):

					handler		= self.INIT_HANDLER
					init_name	= "unwritable_bough_tree"
					init_level	= 10

				class thrive(TwigThrive):	pass
				class folders(Germination):	pass

				class grow(LeafGrowth):		pass
				class files(Rejuvenation):	pass

				@fssprout(self.INIT_SET_SPROUT)
				class sync(Flourish):		pass


			with self.assertLogs("unwritable_bough_tree", 10) as case_loggy:

				self.test_case = Sakura()
				self.assertIn("DEBUG:unwritable_bough_tree:Sakura tree affected", case_loggy.output)
				self.assertIn(

					"DEBUG:unwritable_bough_tree:Spreading complete, number of affected trees: 1",
					case_loggy.output
				)
				self.assertIn(

					"ERROR:unwritable_bough_tree:"
					f"Tree {self.test_case} can't thrive due to "
					f"AssertionError: Bough \"{self.test_case.bough}\" thrive restricted",
					case_loggy.output
				)
				self.assertIn("DEBUG:unwritable_bough_tree:Discarded", case_loggy.output)
				self.assertEqual(len(self.test_case),0)








	def test_strict_thirve_tree(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.INIT_HANDLER
				init_name	= "strict_thirve_tree"
				init_level	= 10

			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.INIT_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("strict_thirve_tree", 10) as case_loggy:

			self.test_case = Sakura()
			self.assertIn(

				"DEBUG:strict_thirve_tree:Sakura tree affected",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:strict_thirve_tree:Spreading complete, number of affected trees: 1",
				case_loggy.output
			)
			self.assertIn(
				f"INFO:strict_thirve_tree:Bough \"{self.INIT_SET_BOUGH_1}\" is invalid", case_loggy.output
			)
			self.assertIn("DEBUG:strict_thirve_tree:Discarded", case_loggy.output)
			self.assertEqual(len(self.test_case),0)








	def test_no_strict_thirve_tree(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.INIT_HANDLER
				init_name	= "no_strict_thirve_tree"
				init_level	= 10
			strict_thrive	= False

			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.INIT_SET_SPROUT)
			class sync(Flourish):		pass


		if	os.path.isdir(self.INIT_SET_BOUGH_1):	rmtree(self.INIT_SET_BOUGH_1)
		self.assertFalse(os.path.isdir(self.INIT_SET_BOUGH_1))


		with self.assertLogs("no_strict_thirve_tree", 10) as case_loggy:

			self.test_case = Sakura()
			self.assertIn("DEBUG:no_strict_thirve_tree:Sakura tree affected", case_loggy.output)
			self.assertIn(

				"DEBUG:no_strict_thirve_tree:Spreading complete, number of affected trees: 1",
				case_loggy.output
			)
			self.assertIn(f"DEBUG:no_strict_thirve_tree:Thriving single tree", case_loggy.output)
			self.assertEqual(len(self.test_case),2)


		if	os.path.isdir(self.INIT_SET_BOUGH_1):	rmtree(self.INIT_SET_BOUGH_1)
		self.assertFalse(os.path.isdir(self.INIT_SET_BOUGH_1))








	def test_no_bough_copse(self):
		class Grove(Copse):

			class loggy(LibraryContrib):

				handler		= self.INIT_HANDLER
				init_name	= "no_bough_copse"
				init_level	= 10

			class Sakura(Tree):			pass
			class Depth(Copse):
				class Sequoyah(Tree):	bough = self.INIT_SET_BOUGH_2
				class Hibiscus(Tree):	bough = self.INIT_SET_BOUGH_3

			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.INIT_SET_SPROUT)
			class sync(Flourish):		pass


		if	not os.path.isdir(self.INIT_SET_BOUGH_3):	os.makedirs(self.INIT_SET_BOUGH_3)
		self.assertTrue(os.path.isdir(self.INIT_SET_BOUGH_3))

		with self.assertLogs("no_bough_copse", 10) as case_loggy:

			self.test_case = Grove()
			self.assertNotIn(

				"DEBUG:no_bough_copse:Grove.Sakura tree affected",
				case_loggy.output
			)
			self.assertNotIn(

				"DEBUG:no_bough_copse:Grove.Depth.Sequoyah tree affected",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:no_bough_copse:Grove.Depth.Hibiscus tree affected",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:no_bough_copse:Spreading complete, number of affected trees: 1",
				case_loggy.output
			)
			self.assertIn(
				f"INFO:no_bough_copse:Bough \"{self.INIT_SET_BOUGH_2}\" is invalid", case_loggy.output
			)
			self.assertIn(

				"ERROR:no_bough_copse:Tree Grove.Sakura can't thrive due to "
				f"AttributeError: Attribute 'bough' has no escalation to Grove",
				case_loggy.output
			)
			self.assertEqual(len(self.test_case.Sakura),0)
			self.assertEqual(len(self.test_case.Depth.Sequoyah),0)
			self.assertEqual(len(self.test_case.Depth.Hibiscus),2)








	def test_bad_sprouts(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_3
			class loggy(LibraryContrib):

				handler		= self.INIT_HANDLER
				init_name	= "bad_sprouts"
				init_level	= 10

			@fssprout(Path(self.INIT_SET_BOUGH_1))
			@fssprout(self.INIT_SET_BOUGH_2)
			@fssprout(self.INIT_SET_SPROUT)
			class sync(Flourish):	pass


		with self.assertLogs("bad_sprouts", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync()


		self.assertIn(
			f"CRITICAL:bad_sprouts:Sprout \"{self.INIT_SET_BOUGH_1}\" is invalid", case_loggy.output
		)
		self.assertIn(
			f"CRITICAL:bad_sprouts:Sprout \"{self.INIT_SET_BOUGH_2}\" is not thrived", case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







