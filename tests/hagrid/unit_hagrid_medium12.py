import	os
import	unittest
from	pygwarts.tests.hagrid					import MediumSet
from	pygwarts.irma.shelve					import LibraryShelf
from	pygwarts.hagrid.thrivables				import Copse
from	pygwarts.hagrid.sprouts					import fssprout
from	pygwarts.hagrid.planting				import Flourish
from	pygwarts.hagrid.cultivation.registering	import PlantRegister
from	pygwarts.hagrid.cultivation.registering	import PlantRegisterQuerier
from	pygwarts.hagrid.cultivation.registering	import WG
from	pygwarts.hagrid.cultivation.registering	import TG
from	pygwarts.hagrid.cultivation.registering	import LG
from	pygwarts.hagrid.cultivation.registering	import WL
from	pygwarts.hagrid.cultivation.registering	import TL
from	pygwarts.hagrid.cultivation.registering	import LL








class RegisterMultiCases(MediumSet):

	"""
		Triple sources registering and querying
	"""

	@classmethod
	def tearDownClass(cls): cls.clean(cls)
	@classmethod
	def setUpClass(cls):

		super().setUpClass()

		class Forest(Copse):

			@fssprout(cls.MEDIUM_SET_SPROUT_3)
			@fssprout(cls.MEDIUM_SET_SPROUT_2)
			@fssprout(cls.MEDIUM_SET_SPROUT_1)
			@PlantRegister("garden")
			class walk(Flourish):		pass
			class garden(LibraryShelf):	pass

		cls.test_case = Forest()
		cls.test_case.walk()
		cls.prq = PlantRegisterQuerier(cls.test_case.garden)


	def test_PRQ_inner(self):

		self.assertTrue(len(self.test_case.garden), 3)
		self.assertIn(self.MEDIUM_SET_SPROUT_1, self.test_case.garden)
		self.assertIn(self.MEDIUM_SET_SPROUT_2, self.test_case.garden)
		self.assertIn(self.MEDIUM_SET_SPROUT_3, self.test_case.garden)

		self.assertTrue(len(self.test_case.garden()), 3)
		self.assertIn(self.MEDIUM_SET_SPROUT_1, self.test_case.garden())
		self.assertIn(self.MEDIUM_SET_SPROUT_2, self.test_case.garden())
		self.assertIn(self.MEDIUM_SET_SPROUT_3, self.test_case.garden())


	def test_register_roots_query(self):

		root1_WG = self.prq.query(key=WG)
		root1_TG = self.prq.query(key=TG)
		root1_LG = self.prq.query(key=LG)
		root1_WL = self.prq.query(key=WL)
		root1_TL = self.prq.query(key=TL)
		root1_LL = self.prq.query(key=LL)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_TG, int)
		self.assertIsInstance(root1_LG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertIsInstance(root1_TL, int)
		self.assertIsInstance(root1_LL, int)

		root2_WG = self.prq.query(key=WG)
		root2_TG = self.prq.query(key=TG)
		root2_LG = self.prq.query(key=LG)
		root2_WL = self.prq.query(key=WL)
		root2_TL = self.prq.query(key=TL)
		root2_LL = self.prq.query(key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_TG, int)
		self.assertIsInstance(root2_LG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertIsInstance(root2_TL, int)
		self.assertIsInstance(root2_LL, int)

		root3_WG = self.prq.query(key=WG)
		root3_TG = self.prq.query(key=TG)
		root3_LG = self.prq.query(key=LG)
		root3_WL = self.prq.query(key=WL)
		root3_TL = self.prq.query(key=TL)
		root3_LL = self.prq.query(key=LL)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_TG, int)
		self.assertIsInstance(root3_LG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertIsInstance(root3_TL, int)
		self.assertIsInstance(root3_LL, int)

		# For multiple sprout the very first sprout walked
		# must be chosen by default, so every call
		# must produce the same result
		self.assertTrue(root1_WG == root2_WG == root3_WG)
		self.assertTrue(root1_TG == root2_TG == root3_TG)
		self.assertTrue(root1_LG == root2_LG == root3_LG)
		self.assertTrue(root1_WL == root2_WL == root3_WL)
		self.assertTrue(root1_TL == root2_TL == root3_TL)
		self.assertTrue(root1_LL == root2_LL == root3_LL)


	def test_branch_register_roots_query(self):

		root1_WG = self.prq.query(self.MEDIUM_SET_SPROUT_1, key=WG)
		root1_TG = self.prq.query(self.MEDIUM_SET_SPROUT_1, key=TG)
		root1_LG = self.prq.query(self.MEDIUM_SET_SPROUT_1, key=LG)
		root1_WL = self.prq.query(self.MEDIUM_SET_SPROUT_1, key=WL)
		root1_TL = self.prq.query(self.MEDIUM_SET_SPROUT_1, key=TL)
		root1_LL = self.prq.query(self.MEDIUM_SET_SPROUT_1, key=LL)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertEqual(root1_TG, 11)
		self.assertEqual(root1_LG, 6)
		self.assertEqual(root1_TL, 2)
		self.assertEqual(root1_LL, 0)

		root2_WG = self.prq.query(self.MEDIUM_SET_SPROUT_2, key=WG)
		root2_TG = self.prq.query(self.MEDIUM_SET_SPROUT_2, key=TG)
		root2_LG = self.prq.query(self.MEDIUM_SET_SPROUT_2, key=LG)
		root2_WL = self.prq.query(self.MEDIUM_SET_SPROUT_2, key=WL)
		root2_TL = self.prq.query(self.MEDIUM_SET_SPROUT_2, key=TL)
		root2_LL = self.prq.query(self.MEDIUM_SET_SPROUT_2, key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 1)
		self.assertEqual(root2_LG, 10)
		self.assertEqual(root2_TL, 1)
		self.assertEqual(root2_LL, 2)

		root3_WG = self.prq.query(self.MEDIUM_SET_SPROUT_3, key=WG)
		root3_TG = self.prq.query(self.MEDIUM_SET_SPROUT_3, key=TG)
		root3_LG = self.prq.query(self.MEDIUM_SET_SPROUT_3, key=LG)
		root3_WL = self.prq.query(self.MEDIUM_SET_SPROUT_3, key=WL)
		root3_TL = self.prq.query(self.MEDIUM_SET_SPROUT_3, key=TL)
		root3_LL = self.prq.query(self.MEDIUM_SET_SPROUT_3, key=LL)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertEqual(root3_TG, 5)
		self.assertEqual(root3_LG, 10)
		self.assertEqual(root3_TL, 1)
		self.assertEqual(root3_LL, 0)


	def test_branch_sprout_register_roots_query(self):

		root1_WG = self.prq.query(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, key=WG)
		root1_TG = self.prq.query(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, key=TG)
		root1_LG = self.prq.query(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, key=LG)
		root1_WL = self.prq.query(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, key=WL)
		root1_TL = self.prq.query(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, key=TL)
		root1_LL = self.prq.query(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, key=LL)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertEqual(root1_TG, 11)
		self.assertEqual(root1_LG, 6)
		self.assertEqual(root1_TL, 2)
		self.assertEqual(root1_LL, 0)

		root2_WG = self.prq.query(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, key=WG)
		root2_TG = self.prq.query(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, key=TG)
		root2_LG = self.prq.query(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, key=LG)
		root2_WL = self.prq.query(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, key=WL)
		root2_TL = self.prq.query(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, key=TL)
		root2_LL = self.prq.query(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 1)
		self.assertEqual(root2_LG, 10)
		self.assertEqual(root2_TL, 1)
		self.assertEqual(root2_LL, 2)

		root3_WG = self.prq.query(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, key=WG)
		root3_TG = self.prq.query(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, key=TG)
		root3_LG = self.prq.query(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, key=LG)
		root3_WL = self.prq.query(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, key=WL)
		root3_TL = self.prq.query(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, key=TL)
		root3_LL = self.prq.query(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, key=LL)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertEqual(root3_TG, 5)
		self.assertEqual(root3_LG, 10)
		self.assertEqual(root3_TL, 1)
		self.assertEqual(root3_LL, 0)


	def test_sprout_register_roots_query(self):

		root1_WG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_1, key=WG)
		root1_TG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_1, key=TG)
		root1_LG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_1, key=LG)
		root1_WL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_1, key=WL)
		root1_TL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_1, key=TL)
		root1_LL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_1, key=LL)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertEqual(root1_TG, 11)
		self.assertEqual(root1_LG, 6)
		self.assertEqual(root1_TL, 2)
		self.assertEqual(root1_LL, 0)

		root2_WG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_2, key=WG)
		root2_TG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_2, key=TG)
		root2_LG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_2, key=LG)
		root2_WL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_2, key=WL)
		root2_TL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_2, key=TL)
		root2_LL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_2, key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 1)
		self.assertEqual(root2_LG, 10)
		self.assertEqual(root2_TL, 1)
		self.assertEqual(root2_LL, 2)

		root3_WG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_3, key=WG)
		root3_TG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_3, key=TG)
		root3_LG = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_3, key=LG)
		root3_WL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_3, key=WL)
		root3_TL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_3, key=TL)
		root3_LL = self.prq.query(sprout=self.MEDIUM_SET_SPROUT_3, key=LL)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertEqual(root3_TG, 5)
		self.assertEqual(root3_LG, 10)
		self.assertEqual(root3_TL, 1)
		self.assertEqual(root3_LL, 0)








	def test_branch_register_children_query(self):

		child1_WG = self.prq.query(self.d_mss1_c, key=WG)
		child1_TG = self.prq.query(self.d_mss1_c, key=TG)
		child1_LG = self.prq.query(self.d_mss1_c, key=LG)
		child1_WL = self.prq.query(self.d_mss1_c, key=WL)
		child1_TL = self.prq.query(self.d_mss1_c, key=TL)
		child1_LL = self.prq.query(self.d_mss1_c, key=LL)

		self.assertIsInstance(child1_WG, int)
		self.assertIsInstance(child1_WL, int)
		self.assertEqual(child1_TG, 8)
		self.assertEqual(child1_LG, 0)
		self.assertEqual(child1_TL, 8)
		self.assertEqual(child1_LL, 0)

		child2_WG = self.prq.query(self.d_mss2_c, key=WG)
		child2_TG = self.prq.query(self.d_mss2_c, key=TG)
		child2_LG = self.prq.query(self.d_mss2_c, key=LG)
		child2_WL = self.prq.query(self.d_mss2_c, key=WL)
		child2_TL = self.prq.query(self.d_mss2_c, key=TL)
		child2_LL = self.prq.query(self.d_mss2_c, key=LL)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 0)
		self.assertEqual(child2_LG, 8)
		self.assertEqual(child2_TL, 0)
		self.assertEqual(child2_LL, 8)

		child3_WG = self.prq.query(self.d_mss3_k_t, key=WG)
		child3_TG = self.prq.query(self.d_mss3_k_t, key=TG)
		child3_LG = self.prq.query(self.d_mss3_k_t, key=LG)
		child3_WL = self.prq.query(self.d_mss3_k_t, key=WL)
		child3_TL = self.prq.query(self.d_mss3_k_t, key=TL)
		child3_LL = self.prq.query(self.d_mss3_k_t, key=LL)

		self.assertIsInstance(child3_WG, int)
		self.assertIsInstance(child3_WL, int)
		self.assertEqual(child3_TG, 1)
		self.assertEqual(child3_LG, 5)
		self.assertEqual(child3_TL, 1)
		self.assertEqual(child3_LL, 0)


	def test_branch_sprout_register_children_query(self):

		child1_WG = self.prq.query(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, key=WG)
		child1_TG = self.prq.query(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, key=TG)
		child1_LG = self.prq.query(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, key=LG)
		child1_WL = self.prq.query(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, key=WL)
		child1_TL = self.prq.query(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, key=TL)
		child1_LL = self.prq.query(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, key=LL)

		self.assertIsInstance(child1_WG, int)
		self.assertIsInstance(child1_WL, int)
		self.assertEqual(child1_TG, 8)
		self.assertEqual(child1_LG, 0)
		self.assertEqual(child1_TL, 8)
		self.assertEqual(child1_LL, 0)

		child2_WG = self.prq.query(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, key=WG)
		child2_TG = self.prq.query(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, key=TG)
		child2_LG = self.prq.query(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, key=LG)
		child2_WL = self.prq.query(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, key=WL)
		child2_TL = self.prq.query(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, key=TL)
		child2_LL = self.prq.query(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, key=LL)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 0)
		self.assertEqual(child2_LG, 8)
		self.assertEqual(child2_TL, 0)
		self.assertEqual(child2_LL, 8)

		child3_WG = self.prq.query(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, key=WG)
		child3_TG = self.prq.query(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, key=TG)
		child3_LG = self.prq.query(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, key=LG)
		child3_WL = self.prq.query(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, key=WL)
		child3_TL = self.prq.query(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, key=TL)
		child3_LL = self.prq.query(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, key=LL)

		self.assertIsInstance(child3_WG, int)
		self.assertIsInstance(child3_WL, int)
		self.assertEqual(child3_TG, 1)
		self.assertEqual(child3_LG, 5)
		self.assertEqual(child3_TL, 1)
		self.assertEqual(child3_LL, 0)








	def test_register_roots_stats(self):

		root1_WG = self.prq.WG()
		root1_TG = self.prq.TG()
		root1_LG = self.prq.LG()
		root1_WL = self.prq.WL()
		root1_TL = self.prq.TL()
		root1_LL = self.prq.LL()

		root1_WG_apparent = self.prq.WG(apparent=True)
		root1_WL_apparent = self.prq.WL(apparent=True)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_TG, int)
		self.assertIsInstance(root1_LG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertIsInstance(root1_TL, int)
		self.assertIsInstance(root1_LL, int)

		self.assertIsInstance(root1_WG_apparent, int)
		self.assertIsInstance(root1_WL_apparent, int)

		self.assertLess(root1_WG, root1_WG_apparent)
		self.assertLess(root1_WL, root1_WL_apparent)

		root2_WG = self.prq.WG()
		root2_TG = self.prq.TG()
		root2_LG = self.prq.LG()
		root2_WL = self.prq.WL()
		root2_TL = self.prq.TL()
		root2_LL = self.prq.LL()

		root2_WG_apparent = self.prq.WG(apparent=True)
		root2_WL_apparent = self.prq.WL(apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_TG, int)
		self.assertIsInstance(root2_LG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertIsInstance(root2_TL, int)
		self.assertIsInstance(root2_LL, int)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertLess(root2_WG, root2_WG_apparent)
		self.assertLess(root2_WL, root2_WL_apparent)

		root3_WG = self.prq.WG()
		root3_TG = self.prq.TG()
		root3_LG = self.prq.LG()
		root3_WL = self.prq.WL()
		root3_TL = self.prq.TL()
		root3_LL = self.prq.LL()

		root3_WG_apparent = self.prq.WG(apparent=True)
		root3_WL_apparent = self.prq.WL(apparent=True)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_TG, int)
		self.assertIsInstance(root3_LG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertIsInstance(root3_TL, int)
		self.assertIsInstance(root3_LL, int)

		self.assertIsInstance(root3_WG_apparent, int)
		self.assertIsInstance(root3_WL_apparent, int)

		self.assertLess(root3_WG, root3_WG_apparent)
		self.assertLess(root3_WL, root3_WL_apparent)

		# For multiple sprout the very first sprout walked
		# must be chosen by default, so every call
		# must produce the same result
		self.assertTrue(root1_WG == root2_WG == root3_WG)
		self.assertTrue(root1_TG == root2_TG == root3_TG)
		self.assertTrue(root1_LG == root2_LG == root3_LG)
		self.assertTrue(root1_WL == root2_WL == root3_WL)
		self.assertTrue(root1_TL == root2_TL == root3_TL)
		self.assertTrue(root1_LL == root2_LL == root3_LL)

		self.assertTrue(root1_WG_apparent == root2_WG_apparent == root3_WG_apparent)
		self.assertTrue(root1_WL_apparent == root2_WL_apparent == root3_WL_apparent)


	def test_branch_register_roots_stats(self):

		root1_WG = self.prq.WG(self.MEDIUM_SET_SPROUT_1)
		root1_TG = self.prq.TG(self.MEDIUM_SET_SPROUT_1)
		root1_LG = self.prq.LG(self.MEDIUM_SET_SPROUT_1)
		root1_WL = self.prq.WL(self.MEDIUM_SET_SPROUT_1)
		root1_TL = self.prq.TL(self.MEDIUM_SET_SPROUT_1)
		root1_LL = self.prq.LL(self.MEDIUM_SET_SPROUT_1)

		root1_WG_apparent = self.prq.WG(self.MEDIUM_SET_SPROUT_1, apparent=True)
		root1_WL_apparent = self.prq.WL(self.MEDIUM_SET_SPROUT_1, apparent=True)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertEqual(root1_TG, 11)
		self.assertEqual(root1_LG, 6)
		self.assertEqual(root1_TL, 2)
		self.assertEqual(root1_LL, 0)

		self.assertIsInstance(root1_WG_apparent, int)
		self.assertIsInstance(root1_WL_apparent, int)

		self.assertEqual(root1_WG_apparent - root1_WG, 11 *4096)
		self.assertEqual(root1_WL_apparent - root1_WL, 2 *4096)

		root2_WG = self.prq.WG(self.MEDIUM_SET_SPROUT_2)
		root2_TG = self.prq.TG(self.MEDIUM_SET_SPROUT_2)
		root2_LG = self.prq.LG(self.MEDIUM_SET_SPROUT_2)
		root2_WL = self.prq.WL(self.MEDIUM_SET_SPROUT_2)
		root2_TL = self.prq.TL(self.MEDIUM_SET_SPROUT_2)
		root2_LL = self.prq.LL(self.MEDIUM_SET_SPROUT_2)

		root2_WG_apparent = self.prq.WG(self.MEDIUM_SET_SPROUT_2, apparent=True)
		root2_WL_apparent = self.prq.WL(self.MEDIUM_SET_SPROUT_2, apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 1)
		self.assertEqual(root2_LG, 10)
		self.assertEqual(root2_TL, 1)
		self.assertEqual(root2_LL, 2)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 4096)

		root3_WG = self.prq.WG(self.MEDIUM_SET_SPROUT_3)
		root3_TG = self.prq.TG(self.MEDIUM_SET_SPROUT_3)
		root3_LG = self.prq.LG(self.MEDIUM_SET_SPROUT_3)
		root3_WL = self.prq.WL(self.MEDIUM_SET_SPROUT_3)
		root3_TL = self.prq.TL(self.MEDIUM_SET_SPROUT_3)
		root3_LL = self.prq.LL(self.MEDIUM_SET_SPROUT_3)

		root3_WG_apparent = self.prq.WG(self.MEDIUM_SET_SPROUT_3, apparent=True)
		root3_WL_apparent = self.prq.WL(self.MEDIUM_SET_SPROUT_3, apparent=True)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertEqual(root3_TG, 5)
		self.assertEqual(root3_LG, 10)
		self.assertEqual(root3_TL, 1)
		self.assertEqual(root3_LL, 0)

		self.assertIsInstance(root3_WG_apparent, int)
		self.assertIsInstance(root3_WL_apparent, int)

		self.assertEqual(root3_WG_apparent - root3_WG, 5 *4096)
		self.assertEqual(root3_WL_apparent - root3_WL, 4096)


	def test_branch_sprout_register_roots_stats(self):

		root1_WG = self.prq.WG(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1)
		root1_TG = self.prq.TG(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1)
		root1_LG = self.prq.LG(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1)
		root1_WL = self.prq.WL(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1)
		root1_TL = self.prq.TL(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1)
		root1_LL = self.prq.LL(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1)

		root1_WG_apparent = self.prq.WG(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, apparent=True)
		root1_WL_apparent = self.prq.WL(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, apparent=True)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertEqual(root1_TG, 11)
		self.assertEqual(root1_LG, 6)
		self.assertEqual(root1_TL, 2)
		self.assertEqual(root1_LL, 0)

		self.assertIsInstance(root1_WG_apparent, int)
		self.assertIsInstance(root1_WL_apparent, int)

		self.assertEqual(root1_WG_apparent - root1_WG, 11 *4096)
		self.assertEqual(root1_WL_apparent - root1_WL, 2 *4096)

		root2_WG = self.prq.WG(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2)
		root2_TG = self.prq.TG(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2)
		root2_LG = self.prq.LG(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2)
		root2_WL = self.prq.WL(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2)
		root2_TL = self.prq.TL(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2)
		root2_LL = self.prq.LL(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2)

		root2_WG_apparent = self.prq.WG(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, apparent=True)
		root2_WL_apparent = self.prq.WL(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 1)
		self.assertEqual(root2_LG, 10)
		self.assertEqual(root2_TL, 1)
		self.assertEqual(root2_LL, 2)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 4096)

		root3_WG = self.prq.WG(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3)
		root3_TG = self.prq.TG(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3)
		root3_LG = self.prq.LG(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3)
		root3_WL = self.prq.WL(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3)
		root3_TL = self.prq.TL(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3)
		root3_LL = self.prq.LL(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3)

		root3_WG_apparent = self.prq.WG(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, apparent=True)
		root3_WL_apparent = self.prq.WL(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, apparent=True)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertEqual(root3_TG, 5)
		self.assertEqual(root3_LG, 10)
		self.assertEqual(root3_TL, 1)
		self.assertEqual(root3_LL, 0)

		self.assertIsInstance(root3_WG_apparent, int)
		self.assertIsInstance(root3_WL_apparent, int)

		self.assertEqual(root3_WG_apparent - root3_WG, 5 *4096)
		self.assertEqual(root3_WL_apparent - root3_WL, 4096)


	def test_sprout_register_roots_stats(self):

		root1_WG = self.prq.WG(sprout=self.MEDIUM_SET_SPROUT_1)
		root1_TG = self.prq.TG(sprout=self.MEDIUM_SET_SPROUT_1)
		root1_LG = self.prq.LG(sprout=self.MEDIUM_SET_SPROUT_1)
		root1_WL = self.prq.WL(sprout=self.MEDIUM_SET_SPROUT_1)
		root1_TL = self.prq.TL(sprout=self.MEDIUM_SET_SPROUT_1)
		root1_LL = self.prq.LL(sprout=self.MEDIUM_SET_SPROUT_1)

		root1_WG_apparent = self.prq.WG(sprout=self.MEDIUM_SET_SPROUT_1, apparent=True)
		root1_WL_apparent = self.prq.WL(sprout=self.MEDIUM_SET_SPROUT_1, apparent=True)

		self.assertIsInstance(root1_WG, int)
		self.assertIsInstance(root1_WL, int)
		self.assertEqual(root1_TG, 11)
		self.assertEqual(root1_LG, 6)
		self.assertEqual(root1_TL, 2)
		self.assertEqual(root1_LL, 0)

		self.assertIsInstance(root1_WG_apparent, int)
		self.assertIsInstance(root1_WL_apparent, int)

		self.assertEqual(root1_WG_apparent - root1_WG, 11 *4096)
		self.assertEqual(root1_WL_apparent - root1_WL, 2 *4096)

		root2_WG = self.prq.WG(sprout=self.MEDIUM_SET_SPROUT_2)
		root2_TG = self.prq.TG(sprout=self.MEDIUM_SET_SPROUT_2)
		root2_LG = self.prq.LG(sprout=self.MEDIUM_SET_SPROUT_2)
		root2_WL = self.prq.WL(sprout=self.MEDIUM_SET_SPROUT_2)
		root2_TL = self.prq.TL(sprout=self.MEDIUM_SET_SPROUT_2)
		root2_LL = self.prq.LL(sprout=self.MEDIUM_SET_SPROUT_2)

		root2_WG_apparent = self.prq.WG(sprout=self.MEDIUM_SET_SPROUT_2, apparent=True)
		root2_WL_apparent = self.prq.WL(sprout=self.MEDIUM_SET_SPROUT_2, apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 1)
		self.assertEqual(root2_LG, 10)
		self.assertEqual(root2_TL, 1)
		self.assertEqual(root2_LL, 2)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 4096)

		root3_WG = self.prq.WG(sprout=self.MEDIUM_SET_SPROUT_3)
		root3_TG = self.prq.TG(sprout=self.MEDIUM_SET_SPROUT_3)
		root3_LG = self.prq.LG(sprout=self.MEDIUM_SET_SPROUT_3)
		root3_WL = self.prq.WL(sprout=self.MEDIUM_SET_SPROUT_3)
		root3_TL = self.prq.TL(sprout=self.MEDIUM_SET_SPROUT_3)
		root3_LL = self.prq.LL(sprout=self.MEDIUM_SET_SPROUT_3)

		root3_WG_apparent = self.prq.WG(sprout=self.MEDIUM_SET_SPROUT_3, apparent=True)
		root3_WL_apparent = self.prq.WL(sprout=self.MEDIUM_SET_SPROUT_3, apparent=True)

		self.assertIsInstance(root3_WG, int)
		self.assertIsInstance(root3_WL, int)
		self.assertEqual(root3_TG, 5)
		self.assertEqual(root3_LG, 10)
		self.assertEqual(root3_TL, 1)
		self.assertEqual(root3_LL, 0)

		self.assertIsInstance(root3_WG_apparent, int)
		self.assertIsInstance(root3_WL_apparent, int)

		self.assertEqual(root3_WG_apparent - root3_WG, 5 *4096)
		self.assertEqual(root3_WL_apparent - root3_WL, 4096)








	def test_branch_register_children_stats(self):

		child1_WG = self.prq.WG(self.d_mss1_c)
		child1_TG = self.prq.TG(self.d_mss1_c)
		child1_LG = self.prq.LG(self.d_mss1_c)
		child1_WL = self.prq.WL(self.d_mss1_c)
		child1_TL = self.prq.TL(self.d_mss1_c)
		child1_LL = self.prq.LL(self.d_mss1_c)

		child1_WG_apparent = self.prq.WG(self.d_mss1_c, apparent=True)
		child1_WL_apparent = self.prq.WL(self.d_mss1_c, apparent=True)

		self.assertIsInstance(child1_WG, int)
		self.assertIsInstance(child1_WL, int)
		self.assertEqual(child1_TG, 8)
		self.assertEqual(child1_LG, 0)
		self.assertEqual(child1_TL, 8)
		self.assertEqual(child1_LL, 0)

		self.assertIsInstance(child1_WG_apparent, int)
		self.assertIsInstance(child1_WL_apparent, int)

		self.assertEqual(child1_WG_apparent - child1_WG, 8 *4096)
		self.assertEqual(child1_WL_apparent - child1_WL, 8 *4096)

		child2_WG = self.prq.WG(self.d_mss2_c)
		child2_TG = self.prq.TG(self.d_mss2_c)
		child2_LG = self.prq.LG(self.d_mss2_c)
		child2_WL = self.prq.WL(self.d_mss2_c)
		child2_TL = self.prq.TL(self.d_mss2_c)
		child2_LL = self.prq.LL(self.d_mss2_c)

		child2_WG_apparent = self.prq.WG(self.d_mss2_c, apparent=True)
		child2_WL_apparent = self.prq.WL(self.d_mss2_c, apparent=True)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 0)
		self.assertEqual(child2_LG, 8)
		self.assertEqual(child2_TL, 0)
		self.assertEqual(child2_LL, 8)

		self.assertIsInstance(child2_WG_apparent, int)
		self.assertIsInstance(child2_WL_apparent, int)

		self.assertEqual(child2_WG_apparent, child2_WG)
		self.assertEqual(child2_WL_apparent, child2_WL)

		child3_WG = self.prq.WG(self.d_mss3_k_t)
		child3_TG = self.prq.TG(self.d_mss3_k_t)
		child3_LG = self.prq.LG(self.d_mss3_k_t)
		child3_WL = self.prq.WL(self.d_mss3_k_t)
		child3_TL = self.prq.TL(self.d_mss3_k_t)
		child3_LL = self.prq.LL(self.d_mss3_k_t)

		child3_WG_apparent = self.prq.WG(self.d_mss3_k_t, apparent=True)
		child3_WL_apparent = self.prq.WL(self.d_mss3_k_t, apparent=True)

		self.assertIsInstance(child3_WG, int)
		self.assertIsInstance(child3_WL, int)
		self.assertEqual(child3_TG, 1)
		self.assertEqual(child3_LG, 5)
		self.assertEqual(child3_TL, 1)
		self.assertEqual(child3_LL, 0)

		self.assertIsInstance(child3_WG_apparent, int)
		self.assertIsInstance(child3_WL_apparent, int)

		self.assertEqual(child3_WG_apparent - child3_WG, 4096)
		self.assertEqual(child3_WL_apparent - child3_WL, 4096)


	def test_branch_sprout_register_children_stats(self):

		child1_WG = self.prq.WG(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1)
		child1_TG = self.prq.TG(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1)
		child1_LG = self.prq.LG(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1)
		child1_WL = self.prq.WL(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1)
		child1_TL = self.prq.TL(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1)
		child1_LL = self.prq.LL(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1)

		child1_WG_apparent = self.prq.WG(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, apparent=True)
		child1_WL_apparent = self.prq.WL(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, apparent=True)

		self.assertIsInstance(child1_WG, int)
		self.assertIsInstance(child1_WL, int)
		self.assertEqual(child1_TG, 8)
		self.assertEqual(child1_LG, 0)
		self.assertEqual(child1_TL, 8)
		self.assertEqual(child1_LL, 0)

		self.assertIsInstance(child1_WG_apparent, int)
		self.assertIsInstance(child1_WL_apparent, int)

		self.assertEqual(child1_WG_apparent - child1_WG, 8 *4096)
		self.assertEqual(child1_WL_apparent - child1_WL, 8 *4096)

		child2_WG = self.prq.WG(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2)
		child2_TG = self.prq.TG(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2)
		child2_LG = self.prq.LG(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2)
		child2_WL = self.prq.WL(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2)
		child2_TL = self.prq.TL(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2)
		child2_LL = self.prq.LL(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2)

		child2_WG_apparent = self.prq.WG(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, apparent=True)
		child2_WL_apparent = self.prq.WL(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, apparent=True)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 0)
		self.assertEqual(child2_LG, 8)
		self.assertEqual(child2_TL, 0)
		self.assertEqual(child2_LL, 8)

		self.assertIsInstance(child2_WG_apparent, int)
		self.assertIsInstance(child2_WL_apparent, int)

		self.assertEqual(child2_WG_apparent, child2_WG)
		self.assertEqual(child2_WL_apparent, child2_WL)

		child3_WG = self.prq.WG(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3)
		child3_TG = self.prq.TG(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3)
		child3_LG = self.prq.LG(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3)
		child3_WL = self.prq.WL(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3)
		child3_TL = self.prq.TL(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3)
		child3_LL = self.prq.LL(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3)

		child3_WG_apparent = self.prq.WG(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, apparent=True)
		child3_WL_apparent = self.prq.WL(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, apparent=True)

		self.assertIsInstance(child3_WG, int)
		self.assertIsInstance(child3_WL, int)
		self.assertEqual(child3_TG, 1)
		self.assertEqual(child3_LG, 5)
		self.assertEqual(child3_TL, 1)
		self.assertEqual(child3_LL, 0)

		self.assertIsInstance(child3_WG_apparent, int)
		self.assertIsInstance(child3_WL_apparent, int)

		self.assertEqual(child3_WG_apparent - child3_WG, 4096)
		self.assertEqual(child3_WL_apparent - child3_WL, 4096)








	def test_branch_sprout_content_roots(self):

		for content in (

			self.prq.content(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1),
			self.prq.content(self.MEDIUM_SET_SPROUT_1, self.MEDIUM_SET_SPROUT_1, apparent=True),
		):
			self.assertEqual(len(content),2)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)

		for content in (

			self.prq.content(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2),
			self.prq.content(self.MEDIUM_SET_SPROUT_2, self.MEDIUM_SET_SPROUT_2, apparent=True),
		):
			self.assertEqual(len(content),2)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)

		for content in (

			self.prq.content(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3),
			self.prq.content(self.MEDIUM_SET_SPROUT_3, self.MEDIUM_SET_SPROUT_3, apparent=True),
		):
			self.assertEqual(len(content),1)
			self.assertIsInstance(content[0],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)








	def test_branch_sprout_content_children(self):

		for content in (

			self.prq.content(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1),
			self.prq.content(self.d_mss1_c, self.MEDIUM_SET_SPROUT_1, apparent=True),
		):
			self.assertEqual(len(content),8)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertIsInstance(content[2],tuple)
			self.assertIsInstance(content[3],tuple)
			self.assertIsInstance(content[4],tuple)
			self.assertIsInstance(content[5],tuple)
			self.assertIsInstance(content[6],tuple)
			self.assertIsInstance(content[7],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertEqual(len(content[2]),2)
			self.assertEqual(len(content[3]),2)
			self.assertEqual(len(content[4]),2)
			self.assertEqual(len(content[5]),2)
			self.assertEqual(len(content[6]),2)
			self.assertEqual(len(content[7]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)
			self.assertIsInstance(content[2][0],int)
			self.assertIsInstance(content[2][1],str)
			self.assertIsInstance(content[3][0],int)
			self.assertIsInstance(content[3][1],str)
			self.assertIsInstance(content[4][0],int)
			self.assertIsInstance(content[4][1],str)
			self.assertIsInstance(content[5][0],int)
			self.assertIsInstance(content[5][1],str)
			self.assertIsInstance(content[6][0],int)
			self.assertIsInstance(content[6][1],str)
			self.assertIsInstance(content[7][0],int)
			self.assertIsInstance(content[7][1],str)

		for content in (

			self.prq.content(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2),
			self.prq.content(self.d_mss2_c, self.MEDIUM_SET_SPROUT_2, apparent=True),
		):
			self.assertEqual(len(content),1)
			self.assertIsInstance(content[0],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)

		for content in (

			self.prq.content(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3),
			self.prq.content(self.d_mss3_k_t, self.MEDIUM_SET_SPROUT_3, apparent=True),
		):
			self.assertEqual(len(content),1)
			self.assertIsInstance(content[0],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)








if __name__ == "__main__" : unittest.main(verbosity=2)







