import	os
import	unittest
from	pathlib						import Path
from	shutil						import rmtree
from	pygwarts.tests.hagrid		import HagridTestCase
from	pygwarts.irma.contrib		import LibraryContrib
from	pygwarts.hagrid.thrivables	import Tree
from	pygwarts.hagrid.thrivables	import Copse
from	pygwarts.hagrid.planting	import Flourish
from	pygwarts.hagrid.bloom.twigs	import Germination
from	pygwarts.hagrid.bloom.leafs	import Rejuvenation








class DispatchingCases(HagridTestCase):

	"""
		Some cases for Flourish algorithm.
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.FLOURISH_HANDLER): os.remove(cls.FLOURISH_HANDLER)

		if	os.path.isdir(cls.INIT_SET_BOUGH_1): rmtree(cls.INIT_SET_BOUGH_1)
		if	os.path.isdir(cls.INIT_SET_BOUGH_2): rmtree(cls.INIT_SET_BOUGH_2)
		if	os.path.isdir(cls.INIT_SET_BOUGH_3): rmtree(cls.INIT_SET_BOUGH_3)

	@classmethod
	def setUpClass(cls):

		if	not os.path.isdir(cls.INIT_SET_BOUGH_1): os.makedirs(cls.INIT_SET_BOUGH_1)
		if	not os.path.isdir(cls.INIT_SET_BOUGH_2): os.makedirs(cls.INIT_SET_BOUGH_2)
		if	not os.path.isdir(cls.INIT_SET_BOUGH_3): os.makedirs(cls.INIT_SET_BOUGH_3)
		cls.make_loggy_file(cls, cls.FLOURISH_HANDLER)




	def test_failed_start(self):
		class sync(Flourish):
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "failed_start"
				init_level	= 10


		with self.assertLogs("failed_start", 10) as case_loggy:

			self.test_case = sync()
			self.test_case(
				(
					self.INIT_SET_SPROUT,
					(
						(
							Path(self.INIT_SET_SPROUT),
							[ Path(self.INIT_SET_SPROUT).joinpath("some folder") ],
							[ Path(self.INIT_SET_SPROUT).joinpath("some file") ],
						)	for _ in range(1)
					)
				)
			)

		self.assertIn(f"CRITICAL:failed_start:{self.test_case} failed to start flourish", case_loggy.output)








	def test_no_plants(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "no_plants"
				init_level	= 10

			class sync(Flourish):		pass


		self.test_case = Sakura()


		with self.assertLogs("no_plants", 10) as case_loggy:
			self.test_case.sync()

		self.assertIn("DEBUG:no_plants:No plants to flourish", case_loggy.output)








	def test_valid_generator_1(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "valid_generator_1"
				init_level	= 10

			class sync(Flourish):		pass


		with self.assertLogs("valid_generator_1", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync(

				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				[ Path(self.INIT_SET_SPROUT).joinpath("some folder") ],
				[ Path(self.INIT_SET_SPROUT).joinpath("some file") ],
			)


		self.assertIn(f"DEBUG:valid_generator_1:Flourishing {self.INIT_SET_SPROUT}", case_loggy.output)
		self.assertIn(f"DEBUG:valid_generator_1:Current branch \"{self.INIT_SET_SPROUT}\"", case_loggy.output)
		self.assertIn("DEBUG:valid_generator_1:Number of twigs: 1", case_loggy.output)
		self.assertIn("DEBUG:valid_generator_1:Number of leafs: 1", case_loggy.output)
		self.assertIn("DEBUG:valid_generator_1:Chest is empty", case_loggy.output)








	def test_valid_generator_2(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "valid_generator_2"
				init_level	= 10

			class sync(Flourish):		pass


		with self.assertLogs("valid_generator_2", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync.innervate(
				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				[ Path(self.INIT_SET_SPROUT).joinpath("some folder") ],
				[ Path(self.INIT_SET_SPROUT).joinpath("some file") ],
			)


		self.assertNotIn(f"DEBUG:valid_generator_2:Flourishing {self.INIT_SET_SPROUT}", case_loggy.output)
		self.assertIn(f"DEBUG:valid_generator_2:Current branch \"{self.INIT_SET_SPROUT}\"", case_loggy.output)
		self.assertIn("DEBUG:valid_generator_2:Number of twigs: 1", case_loggy.output)
		self.assertIn("DEBUG:valid_generator_2:Number of leafs: 1", case_loggy.output)
		self.assertIn("DEBUG:valid_generator_2:Chest is empty", case_loggy.output)








	def test_invalid_generator_1(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "invalid_generator_1"
				init_level	= 10

			class sync(Flourish):		pass


		self.test_case = Sakura()
		with self.assertLogs("invalid_generator_1", 10) as case_loggy:

			self.test_case.sync(1)

		self.assertIn(f"WARNING:invalid_generator_1:Invalid plant length 1", case_loggy.output)
		with self.assertLogs("invalid_generator_1", 10) as case_loggy:

			self.test_case.sync(1,2)

		self.assertIn(f"WARNING:invalid_generator_1:Invalid plant length 2", case_loggy.output)
		with self.assertLogs("invalid_generator_1", 10) as case_loggy:

			self.test_case.sync(1,2,3)

		self.assertIn(f"WARNING:invalid_generator_1:Invalid plant length 3", case_loggy.output)
		with self.assertLogs("invalid_generator_1", 10) as case_loggy:

			self.test_case.sync(1,2,3,4,5)

		self.assertIn(f"WARNING:invalid_generator_1:Invalid plant length 5", case_loggy.output)








	def test_invalid_generator_2(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "invalid_generator_2"
				init_level	= 10

			class sync(Flourish):		pass


		self.test_case = Sakura()
		for S in ( 1,.1,( "tree", ),[ "tree" ],{ "tree" },{ "tree": "tree" },self.test_case, None,True ):
			with self.subTest(sprout=S):
				with self.assertLogs("invalid_generator_2", 10) as case_loggy:

					self.test_case.sync(S,2,3,4)
				self.assertIn(f"WARNING:invalid_generator_2:Invalid plant sprout \"{S}\"", case_loggy.output)








	def test_invalid_generator_3(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "invalid_generator_3"
				init_level	= 10

			class sync(Flourish):		pass


		self.test_case = Sakura()
		for B in ( 1,.1,( "tree", ),[ "tree" ],{ "tree" },{ "tree": "tree" },self.test_case, None,True ):
			with self.subTest(branch=B):
				with self.assertLogs("invalid_generator_3", 10) as case_loggy:

					self.test_case.sync(self.INIT_SET_SPROUT,B,3,4)
				self.assertIn(f"WARNING:invalid_generator_3:Invalid plant branch \"{B}\"", case_loggy.output)








	def test_invalid_generator_4(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "invalid_generator_4"
				init_level	= 10

			class sync(Flourish):		pass


		self.test_case = Sakura()
		for T in ( 1,.1,( "tree", ),{ "tree" },{ "tree": "tree" },self.test_case, None,True ):
			with self.subTest(twigs=T):
				with self.assertLogs("invalid_generator_4", 10) as case_loggy:

					self.test_case.sync(self.INIT_SET_SPROUT,Path(self.INIT_SET_SPROUT),T,4)
				self.assertIn(f"WARNING:invalid_generator_4:Invalid plant twigs {type(T)}", case_loggy.output)








	def test_invalid_generator_5(self):
		class Sakura(Tree):

			bough	= self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "invalid_generator_5"
				init_level	= 10

			class sync(Flourish):		pass


		self.test_case = Sakura()
		for L in ( 1,.1,( "tree", ),{ "tree" },{ "tree": "tree" },self.test_case, None,True ):
			with self.subTest(twigs=L):
				with self.assertLogs("invalid_generator_5", 10) as case_loggy:

					self.test_case.sync(self.INIT_SET_SPROUT,Path(self.INIT_SET_SPROUT),[],L)
				self.assertIn(f"WARNING:invalid_generator_5:Invalid plant leafs {type(L)}", case_loggy.output)








	def test_valid_grove(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "valid_grove"
				init_level	= 10

			class Deeper(Copse):
				class DeeperFirst(Tree):		bough = self.INIT_SET_BOUGH_1
				class DeeperSecond(Tree):		bough = self.INIT_SET_BOUGH_2
				class DeeperThird(Tree):		bough = self.INIT_SET_BOUGH_3

				class Deepest(Copse):
					class DeepestFirst(Tree):	bough = self.INIT_SET_BOUGH_1
					class DeepestSecond(Tree):	bough = self.INIT_SET_BOUGH_2
					class DeepestThird(Tree):	bough = self.INIT_SET_BOUGH_3

			class First(Tree):					bough = self.INIT_SET_BOUGH_1
			class Second(Tree):					bough = self.INIT_SET_BOUGH_2
			class Third(Tree):					bough = self.INIT_SET_BOUGH_3
			class sync(Flourish):				pass


		self.test_case = Forest()
		with self.assertLogs("valid_grove", 10) as case_loggy:
			forest = list(self.test_case.sync.grove(self.test_case))

		self.assertEqual(len(forest), 9)
		self.assertAlmostEqual(

			forest,
			[
				self.test_case.Deeper.DeeperFirst,
				self.test_case.Deeper.DeeperSecond,
				self.test_case.Deeper.DeeperThird,
				self.test_case.Deeper.Deepest.DeepestFirst,
				self.test_case.Deeper.Deepest.DeepestSecond,
				self.test_case.Deeper.Deepest.DeepestThird,
				self.test_case.First,
				self.test_case.Second,
				self.test_case.Third,
			]
		)
		self.assertIn(

			f"DEBUG:valid_grove:Walking copse {self.test_case} inner {self.test_case.Deeper}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:valid_grove:Walking copse {self.test_case.Deeper} inner {self.test_case.Deeper.Deepest}",
			case_loggy.output
		)








	def test_invalid_grove(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "invalid_grove"
				init_level	= 10

			class Deeper(Copse):
				class DeeperFirst(Tree):		bough = self.INIT_SET_BOUGH_1
				class DeeperSecond(Tree):		bough = self.INIT_SET_BOUGH_2
				class DeeperThird(Tree):		bough = self.INIT_SET_BOUGH_3

				class Deepest(Copse):
					class DeepestFirst(Tree):	bough = self.INIT_SET_BOUGH_1
					class DeepestSecond(Tree):	bough = self.INIT_SET_BOUGH_2
					class DeepestThird(Tree):	bough = self.INIT_SET_BOUGH_3

			class First(Tree):					bough = self.INIT_SET_BOUGH_1
			class Second(Tree):					bough = self.INIT_SET_BOUGH_2
			class Third(Tree):					bough = self.INIT_SET_BOUGH_3
			class sync(Flourish):				pass
			class rejuve(Rejuvenation):			pass
			class germinate(Germination):		pass


		self.test_case = Forest()
		self.test_case(self.test_case.sync)
		self.test_case.Deeper(self.test_case.rejuve)
		self.test_case.Deeper.Deepest(self.test_case.germinate)

		with self.assertLogs("invalid_grove", 10) as case_loggy:
			forest = list(self.test_case.sync.grove(self.test_case))

		self.assertEqual(len(forest), 9)
		self.assertAlmostEqual(

			forest,
			[
				self.test_case.Deeper.DeeperFirst,
				self.test_case.Deeper.DeeperSecond,
				self.test_case.Deeper.DeeperThird,
				self.test_case.Deeper.Deepest.DeepestFirst,
				self.test_case.Deeper.Deepest.DeepestSecond,
				self.test_case.Deeper.Deepest.DeepestThird,
				self.test_case.First,
				self.test_case.Second,
				self.test_case.Third,
			]
		)
		self.assertIn(

			f"DEBUG:invalid_grove:Walking copse {self.test_case} inner {self.test_case.Deeper}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:invalid_grove:Walking copse {self.test_case.Deeper} inner {self.test_case.Deeper.Deepest}",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:invalid_grove:Invalid thrivable \"{self.test_case.sync}\" for flourish",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:invalid_grove:Invalid thrivable \"{self.test_case.rejuve}\" for flourish",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:invalid_grove:Invalid thrivable \"{self.test_case.germinate}\" for flourish",
			case_loggy.output
		)








	def test_empty_grove(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.FLOURISH_HANDLER
				init_name	= "empty_grove"
				init_level	= 10

			class sync(Flourish):	pass


		with self.assertLogs("empty_grove", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync(self.INIT_SET_SPROUT, Path(self.INIT_SET_SPROUT), [],[])

		self.assertIn(f"DEBUG:empty_grove:Chest is empty", case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







