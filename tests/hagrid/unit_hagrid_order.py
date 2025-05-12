import	os
import	unittest
from	shutil						import rmtree
from	pygwarts.tests.hagrid		import HagridTestCase
from	pygwarts.hagrid.thrivables	import Tree
from	pygwarts.hagrid.thrivables	import Copse
from	pygwarts.hagrid.bloom.twigs	import Germination
from	pygwarts.hagrid.bloom.leafs	import Rejuvenation
from	pygwarts.hagrid.bloom.weeds	import Efflorescence








class BloomsOrderCase(HagridTestCase):

	"""
		Some initiation order tests
	"""

	@classmethod
	def tearDownClass(cls):

		if	os.path.isdir(cls.ORDER_SET_BOUGH_1): rmtree(cls.ORDER_SET_BOUGH_1)
		if	os.path.isdir(cls.ORDER_SET_BOUGH_2): rmtree(cls.ORDER_SET_BOUGH_2)
		if	os.path.isdir(cls.ORDER_SET_BOUGH_3): rmtree(cls.ORDER_SET_BOUGH_3)

	def test_direct_order(self):
		class TestForest(Copse):

			strict_thrive = False

			class First(Tree):	bough = self.ORDER_SET_BOUGH_1
			class Second(Tree):	bough = self.ORDER_SET_BOUGH_2
			class Third(Tree):	bough = self.ORDER_SET_BOUGH_3

			class folders(Germination):	pass
			class files(Rejuvenation):	pass
			class clean(Efflorescence):	pass


		self.test_case = TestForest()
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.First ],
			[ "TestForest.folders", "TestForest.files", "TestForest.clean" ]
		)
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.Second ],
			[ "TestForest.folders", "TestForest.files", "TestForest.clean" ]
		)
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.Third ],
			[ "TestForest.folders", "TestForest.files", "TestForest.clean" ]
		)




	def test_two_order(self):
		class TestForest(Copse):

			strict_thrive = False

			class First(Tree):	bough = self.ORDER_SET_BOUGH_1
			class Second(Tree):	bough = self.ORDER_SET_BOUGH_2
			class Third(Tree):

				bough = self.ORDER_SET_BOUGH_3
				class clean(Efflorescence):	pass

			class folders(Germination):	pass
			class files(Rejuvenation):	pass


		self.test_case = TestForest()
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.First ],
			[ "TestForest.folders", "TestForest.files" ]
		)
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.Second ],
			[ "TestForest.folders", "TestForest.files" ]
		)
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.Third ],
			[ "TestForest.Third.clean", "TestForest.folders", "TestForest.files" ]
		)




	def test_all_in_one_order(self):
		class TestForest(Copse):

			strict_thrive = False

			class First(Tree):	bough = self.ORDER_SET_BOUGH_1
			class Second(Tree):	bough = self.ORDER_SET_BOUGH_2
			class Third(Tree):

				bough = self.ORDER_SET_BOUGH_3
				class clean(Efflorescence):	pass
				class folders(Germination):	pass
				class files(Rejuvenation):	pass



		self.test_case = TestForest()
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.First ],
			[]
		)
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.Second ],
			[]
		)
		self.assertEqual(

			[ str(bloom) for bloom in self.test_case.Third ],
			[ "TestForest.Third.clean", "TestForest.Third.folders", "TestForest.Third.files" ]
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







