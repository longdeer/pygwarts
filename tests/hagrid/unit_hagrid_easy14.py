import	os
import	unittest
from	pygwarts.tests.hagrid					import EasySet
from	pygwarts.irma.contrib					import LibraryContrib
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








class RegisterSingleCase(EasySet):

	"""
		Single source registering and querying
	"""

	@classmethod
	def tearDownClass(cls): cls.clean(cls)
	@classmethod
	def setUpClass(cls):

		super().setUpClass()

		class Forest(Copse):

			@fssprout(cls.EASY_SET_SPROUT)
			@PlantRegister("garden")
			class walk(Flourish):		pass
			class garden(LibraryShelf):	pass

		cls.test_case = Forest()
		cls.test_case.walk()
		cls.prq = PlantRegisterQuerier(cls.test_case.garden)
		cls.miss_branch = os.path.join(cls.EASY_SET_SPROUT, "miss branch")
		cls.test_case.garden.produce(cls.EASY_SET_SEEDS, ignore_mod=True)
		cls.extern_shelf = LibraryShelf()
		cls.extern_shelf.grab(cls.EASY_SET_SEEDS)
		cls.prq2 = PlantRegisterQuerier(cls.extern_shelf)


	def test_PRQ_bad_init(self):

		for garden in (

			1, 1., "LibraryShelf", LibraryShelf, True, False, None, ..., print,
			[ self.test_case.garden ],
			( self.test_case.garden, ),
			{ self.test_case.garden },
			{ "garden": self.test_case.garden },
		):
			self.assertIsNone(PlantRegisterQuerier(garden).garden)


	def test_PRQ_query_bad_branch(self):

		for branch in (

			1, 1., "folder", LibraryShelf, True, False, ..., print,
			[ self.EASY_SET_SPROUT ],
			( self.EASY_SET_SPROUT, ),
			{ self.EASY_SET_SPROUT },
			{ "branch": self.EASY_SET_SPROUT },
		):
			with self.subTest(branch=branch):

				self.assertIsNone(self.prq.query(branch, key=WG))
				self.assertIsNone(self.prq.query(branch, key=WL))
				self.assertIsNone(self.prq.query(branch, key=TG))
				self.assertIsNone(self.prq.query(branch, key=LG))
				self.assertIsNone(self.prq.query(branch, key=TL))
				self.assertIsNone(self.prq.query(branch, key=LL))


	def test_PRQ_query_bad_sprout(self):

		for sprout in (

			1, 1., "folder", LibraryShelf, True, False, ..., print,
			[ self.EASY_SET_SPROUT ],
			( self.EASY_SET_SPROUT, ),
			{ self.EASY_SET_SPROUT },
			{ "sprout": self.EASY_SET_SPROUT },
		):
			with self.subTest(sprout=sprout):

				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, sprout, WG))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, sprout, WL))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, sprout, TG))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, sprout, LG))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, sprout, TL))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, sprout, LL))


	def test_PRQ_query_bad_key(self):

		for key in (

			1, 1., "weight", LibraryShelf, True, False, ..., print,
			[ WG ],( WG, ),{ WG },{ "key": WG },
		):
			with self.subTest(key=key):

				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key))
				self.assertIsNone(self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key))


	def test_PRQ_bad_named_queries(self):

		for shoot in (

			1, 1., "folder", LibraryShelf, True, False, ..., print,
			[ self.EASY_SET_SPROUT ],
			( self.EASY_SET_SPROUT, ),
			{ self.EASY_SET_SPROUT },
			{ "shoot": self.EASY_SET_SPROUT },
		):
			with self.subTest(shoot=shoot):

				self.assertIsNone(self.prq.WG(shoot))
				self.assertIsNone(self.prq.WG(shoot, shoot))
				self.assertIsNone(self.prq.WG(sprout=shoot))

				self.assertIsNone(self.prq.TG(shoot))
				self.assertIsNone(self.prq.TG(shoot, shoot))
				self.assertIsNone(self.prq.TG(sprout=shoot))

				self.assertIsNone(self.prq.LG(shoot))
				self.assertIsNone(self.prq.LG(shoot, shoot))
				self.assertIsNone(self.prq.LG(sprout=shoot))

				self.assertIsNone(self.prq.WL(shoot))
				self.assertIsNone(self.prq.WL(shoot, shoot))
				self.assertIsNone(self.prq.WL(sprout=shoot))

				self.assertIsNone(self.prq.TL(shoot))
				self.assertIsNone(self.prq.TL(shoot, shoot))
				self.assertIsNone(self.prq.TL(sprout=shoot))

				self.assertIsNone(self.prq.LL(shoot))
				self.assertIsNone(self.prq.LL(shoot, shoot))
				self.assertIsNone(self.prq.LL(sprout=shoot))








	def test_PRQ_bad_garden(self):

		for garden in (

			1, 1., "LibraryShelf", LibraryShelf, True, False, None, ..., print,
			[ self.test_case.garden ],
			( self.test_case.garden, ),
			{ self.test_case.garden },
			{ "garden": self.test_case.garden },
		):
			prq = PlantRegisterQuerier(garden)

			self.assertIsNone(prq.query(key=WG))
			self.assertIsNone(prq.query(key=TG))
			self.assertIsNone(prq.query(key=LG))
			self.assertIsNone(prq.query(key=WL))
			self.assertIsNone(prq.query(key=TL))
			self.assertIsNone(prq.query(key=LL))

			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, key=WG))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, key=TG))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, key=LG))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, key=WL))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, key=TL))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, key=LL))

			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=WG))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=TG))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=LG))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=WL))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=TL))
			self.assertIsNone(prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=LL))

			self.assertIsNone(prq.query(sprout=self.EASY_SET_SPROUT, key=WG))
			self.assertIsNone(prq.query(sprout=self.EASY_SET_SPROUT, key=TG))
			self.assertIsNone(prq.query(sprout=self.EASY_SET_SPROUT, key=LG))
			self.assertIsNone(prq.query(sprout=self.EASY_SET_SPROUT, key=WL))
			self.assertIsNone(prq.query(sprout=self.EASY_SET_SPROUT, key=TL))
			self.assertIsNone(prq.query(sprout=self.EASY_SET_SPROUT, key=LL))

			self.assertIsNone(prq.WG())
			self.assertIsNone(prq.TG())
			self.assertIsNone(prq.LG())
			self.assertIsNone(prq.WL())
			self.assertIsNone(prq.TL())
			self.assertIsNone(prq.LL())
			self.assertIsNone(prq.WG(apparent=True))
			self.assertIsNone(prq.WL(apparent=True))

			self.assertIsNone(prq.WG(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.TG(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.LG(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.WL(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.TL(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.LL(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.WG(self.EASY_SET_SPROUT, apparent=True))
			self.assertIsNone(prq.WL(self.EASY_SET_SPROUT, apparent=True))

			self.assertIsNone(prq.WG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.TG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.LG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.WL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.TL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.LL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.WG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True))
			self.assertIsNone(prq.WL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True))

			self.assertIsNone(prq.WG(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.TG(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.LG(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.WL(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.TL(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.LL(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.WG(sprout=self.EASY_SET_SPROUT, apparent=True))
			self.assertIsNone(prq.WL(sprout=self.EASY_SET_SPROUT, apparent=True))

			self.assertIsNone(prq.content(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT))
			self.assertIsNone(prq.content(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True))
			self.assertIsNone(prq.content(self.EASY_SET_SPROUT))
			self.assertIsNone(prq.content(self.EASY_SET_SPROUT, apparent=True))
			self.assertIsNone(prq.content(sprout=self.EASY_SET_SPROUT))
			self.assertIsNone(prq.content(sprout=self.EASY_SET_SPROUT, apparent=True))
			self.assertIsNone(prq.content())
			self.assertIsNone(prq.content(apparent=True))








	def test_miss_branch(self):

		self.assertIsNone(self.prq.query(self.miss_branch, WG))
		self.assertIsNone(self.prq.query(self.miss_branch, TG))
		self.assertIsNone(self.prq.query(self.miss_branch, LG))
		self.assertIsNone(self.prq.query(self.miss_branch, WL))
		self.assertIsNone(self.prq.query(self.miss_branch, TL))
		self.assertIsNone(self.prq.query(self.miss_branch, LL))

		self.assertIsNone(self.prq.query(self.miss_branch, self.EASY_SET_SPROUT, WG))
		self.assertIsNone(self.prq.query(self.miss_branch, self.EASY_SET_SPROUT, TG))
		self.assertIsNone(self.prq.query(self.miss_branch, self.EASY_SET_SPROUT, LG))
		self.assertIsNone(self.prq.query(self.miss_branch, self.EASY_SET_SPROUT, WL))
		self.assertIsNone(self.prq.query(self.miss_branch, self.EASY_SET_SPROUT, TL))
		self.assertIsNone(self.prq.query(self.miss_branch, self.EASY_SET_SPROUT, LL))

		self.assertIsNone(self.prq.WG(self.miss_branch))
		self.assertIsNone(self.prq.TG(self.miss_branch))
		self.assertIsNone(self.prq.LG(self.miss_branch))
		self.assertIsNone(self.prq.WL(self.miss_branch))
		self.assertIsNone(self.prq.TL(self.miss_branch))
		self.assertIsNone(self.prq.LL(self.miss_branch))

		self.assertIsNone(self.prq.WG(self.miss_branch, self.EASY_SET_SPROUT))
		self.assertIsNone(self.prq.TG(self.miss_branch, self.EASY_SET_SPROUT))
		self.assertIsNone(self.prq.LG(self.miss_branch, self.EASY_SET_SPROUT))
		self.assertIsNone(self.prq.WL(self.miss_branch, self.EASY_SET_SPROUT))
		self.assertIsNone(self.prq.TL(self.miss_branch, self.EASY_SET_SPROUT))
		self.assertIsNone(self.prq.LL(self.miss_branch, self.EASY_SET_SPROUT))

		self.assertIsNone(self.prq.WG(self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.WL(self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.WG(self.miss_branch, self.EASY_SET_SPROUT, apparent=True))
		self.assertIsNone(self.prq.WL(self.miss_branch, self.EASY_SET_SPROUT, apparent=True))


	def test_miss_sprout(self):

		self.assertIsNone(self.prq.query(sprout=self.miss_branch, key=WG))
		self.assertIsNone(self.prq.query(sprout=self.miss_branch, key=TG))
		self.assertIsNone(self.prq.query(sprout=self.miss_branch, key=LG))
		self.assertIsNone(self.prq.query(sprout=self.miss_branch, key=WL))
		self.assertIsNone(self.prq.query(sprout=self.miss_branch, key=TL))
		self.assertIsNone(self.prq.query(sprout=self.miss_branch, key=LL))

		self.assertIsNone(self.prq.query(self.pros_folder, self.miss_branch, key=WG))
		self.assertIsNone(self.prq.query(self.pros_folder, self.miss_branch, key=TG))
		self.assertIsNone(self.prq.query(self.pros_folder, self.miss_branch, key=LG))
		self.assertIsNone(self.prq.query(self.pros_folder, self.miss_branch, key=WL))
		self.assertIsNone(self.prq.query(self.pros_folder, self.miss_branch, key=TL))
		self.assertIsNone(self.prq.query(self.pros_folder, self.miss_branch, key=LL))

		self.assertIsNone(self.prq.WG(sprout=self.miss_branch))
		self.assertIsNone(self.prq.TG(sprout=self.miss_branch))
		self.assertIsNone(self.prq.LG(sprout=self.miss_branch))
		self.assertIsNone(self.prq.WL(sprout=self.miss_branch))
		self.assertIsNone(self.prq.TL(sprout=self.miss_branch))
		self.assertIsNone(self.prq.LL(sprout=self.miss_branch))

		self.assertIsNone(self.prq.WG(self.pros_folder, self.miss_branch))
		self.assertIsNone(self.prq.TG(self.pros_folder, self.miss_branch))
		self.assertIsNone(self.prq.LG(self.pros_folder, self.miss_branch))
		self.assertIsNone(self.prq.WL(self.pros_folder, self.miss_branch))
		self.assertIsNone(self.prq.TL(self.pros_folder, self.miss_branch))
		self.assertIsNone(self.prq.LL(self.pros_folder, self.miss_branch))

		self.assertIsNone(self.prq.WG(sprout=self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.WL(sprout=self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.WG(self.pros_folder, self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.WL(self.pros_folder, self.miss_branch, apparent=True))








	def test_register_root_query(self):

		root_WG = self.prq.query(key=WG)
		root_TG = self.prq.query(key=TG)
		root_LG = self.prq.query(key=LG)
		root_WL = self.prq.query(key=WL)
		root_TL = self.prq.query(key=TL)
		root_LL = self.prq.query(key=LL)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		root2_WG = self.prq2.query(key=WG)
		root2_TG = self.prq2.query(key=TG)
		root2_LG = self.prq2.query(key=LG)
		root2_WL = self.prq2.query(key=WL)
		root2_TL = self.prq2.query(key=TL)
		root2_LL = self.prq2.query(key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)


	def test_branch_register_root_query(self):

		root_WG = self.prq.query(self.EASY_SET_SPROUT, key=WG)
		root_TG = self.prq.query(self.EASY_SET_SPROUT, key=TG)
		root_LG = self.prq.query(self.EASY_SET_SPROUT, key=LG)
		root_WL = self.prq.query(self.EASY_SET_SPROUT, key=WL)
		root_TL = self.prq.query(self.EASY_SET_SPROUT, key=TL)
		root_LL = self.prq.query(self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		root2_WG = self.prq2.query(self.EASY_SET_SPROUT, key=WG)
		root2_TG = self.prq2.query(self.EASY_SET_SPROUT, key=TG)
		root2_LG = self.prq2.query(self.EASY_SET_SPROUT, key=LG)
		root2_WL = self.prq2.query(self.EASY_SET_SPROUT, key=WL)
		root2_TL = self.prq2.query(self.EASY_SET_SPROUT, key=TL)
		root2_LL = self.prq2.query(self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)


	def test_branch_sprout_register_root_query(self):

		root_WG = self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=WG)
		root_TG = self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=TG)
		root_LG = self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=LG)
		root_WL = self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=WL)
		root_TL = self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=TL)
		root_LL = self.prq.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		root2_WG = self.prq2.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=WG)
		root2_TG = self.prq2.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=TG)
		root2_LG = self.prq2.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=LG)
		root2_WL = self.prq2.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=WL)
		root2_TL = self.prq2.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=TL)
		root2_LL = self.prq2.query(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)


	def test_sprout_register_root_query(self):

		root_WG = self.prq.query(sprout=self.EASY_SET_SPROUT, key=WG)
		root_TG = self.prq.query(sprout=self.EASY_SET_SPROUT, key=TG)
		root_LG = self.prq.query(sprout=self.EASY_SET_SPROUT, key=LG)
		root_WL = self.prq.query(sprout=self.EASY_SET_SPROUT, key=WL)
		root_TL = self.prq.query(sprout=self.EASY_SET_SPROUT, key=TL)
		root_LL = self.prq.query(sprout=self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		root2_WG = self.prq2.query(sprout=self.EASY_SET_SPROUT, key=WG)
		root2_TG = self.prq2.query(sprout=self.EASY_SET_SPROUT, key=TG)
		root2_LG = self.prq2.query(sprout=self.EASY_SET_SPROUT, key=LG)
		root2_WL = self.prq2.query(sprout=self.EASY_SET_SPROUT, key=WL)
		root2_TL = self.prq2.query(sprout=self.EASY_SET_SPROUT, key=TL)
		root2_LL = self.prq2.query(sprout=self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)








	def test_branch_register_child_query(self):

		child_WG = self.prq.query(self.pros_folder, key=WG)
		child_TG = self.prq.query(self.pros_folder, key=TG)
		child_LG = self.prq.query(self.pros_folder, key=LG)
		child_WL = self.prq.query(self.pros_folder, key=WL)
		child_TL = self.prq.query(self.pros_folder, key=TL)
		child_LL = self.prq.query(self.pros_folder, key=LL)

		self.assertIsInstance(child_WG, int)
		self.assertIsInstance(child_WL, int)
		self.assertEqual(child_TG, 1)
		self.assertEqual(child_LG, 4)
		self.assertEqual(child_TL, 1)
		self.assertEqual(child_LL, 3)

		child2_WG = self.prq2.query(self.pros_folder, key=WG)
		child2_TG = self.prq2.query(self.pros_folder, key=TG)
		child2_LG = self.prq2.query(self.pros_folder, key=LG)
		child2_WL = self.prq2.query(self.pros_folder, key=WL)
		child2_TL = self.prq2.query(self.pros_folder, key=TL)
		child2_LL = self.prq2.query(self.pros_folder, key=LL)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 1)
		self.assertEqual(child2_LG, 4)
		self.assertEqual(child2_TL, 1)
		self.assertEqual(child2_LL, 3)


	def test_branch_sprout_register_child_query(self):

		child_WG = self.prq.query(self.pros_folder, self.EASY_SET_SPROUT, key=WG)
		child_TG = self.prq.query(self.pros_folder, self.EASY_SET_SPROUT, key=TG)
		child_LG = self.prq.query(self.pros_folder, self.EASY_SET_SPROUT, key=LG)
		child_WL = self.prq.query(self.pros_folder, self.EASY_SET_SPROUT, key=WL)
		child_TL = self.prq.query(self.pros_folder, self.EASY_SET_SPROUT, key=TL)
		child_LL = self.prq.query(self.pros_folder, self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(child_WG, int)
		self.assertIsInstance(child_WL, int)
		self.assertEqual(child_TG, 1)
		self.assertEqual(child_LG, 4)
		self.assertEqual(child_TL, 1)
		self.assertEqual(child_LL, 3)

		child2_WG = self.prq2.query(self.pros_folder, self.EASY_SET_SPROUT, key=WG)
		child2_TG = self.prq2.query(self.pros_folder, self.EASY_SET_SPROUT, key=TG)
		child2_LG = self.prq2.query(self.pros_folder, self.EASY_SET_SPROUT, key=LG)
		child2_WL = self.prq2.query(self.pros_folder, self.EASY_SET_SPROUT, key=WL)
		child2_TL = self.prq2.query(self.pros_folder, self.EASY_SET_SPROUT, key=TL)
		child2_LL = self.prq2.query(self.pros_folder, self.EASY_SET_SPROUT, key=LL)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 1)
		self.assertEqual(child2_LG, 4)
		self.assertEqual(child2_TL, 1)
		self.assertEqual(child2_LL, 3)








	def test_register_root_stats(self):

		root_WG = self.prq.WG()
		root_TG = self.prq.TG()
		root_LG = self.prq.LG()
		root_WL = self.prq.WL()
		root_TL = self.prq.TL()
		root_LL = self.prq.LL()

		root_WG_apparent = self.prq.WG(apparent=True)
		root_WL_apparent = self.prq.WL(apparent=True)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		self.assertIsInstance(root_WG_apparent, int)
		self.assertIsInstance(root_WL_apparent, int)

		self.assertEqual(root_WG_apparent - root_WG, 4 *4096)
		self.assertEqual(root_WL_apparent - root_WL, 3 *4096)

		root2_WG = self.prq2.WG()
		root2_TG = self.prq2.TG()
		root2_LG = self.prq2.LG()
		root2_WL = self.prq2.WL()
		root2_TL = self.prq2.TL()
		root2_LL = self.prq2.LL()

		root2_WG_apparent = self.prq2.WG(apparent=True)
		root2_WL_apparent = self.prq2.WL(apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4 *4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 3 *4096)


	def test_branch_register_root_stats(self):

		root_WG = self.prq.WG(self.EASY_SET_SPROUT)
		root_TG = self.prq.TG(self.EASY_SET_SPROUT)
		root_LG = self.prq.LG(self.EASY_SET_SPROUT)
		root_WL = self.prq.WL(self.EASY_SET_SPROUT)
		root_TL = self.prq.TL(self.EASY_SET_SPROUT)
		root_LL = self.prq.LL(self.EASY_SET_SPROUT)

		root_WG_apparent = self.prq.WG(self.EASY_SET_SPROUT, apparent=True)
		root_WL_apparent = self.prq.WL(self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		self.assertIsInstance(root_WG_apparent, int)
		self.assertIsInstance(root_WL_apparent, int)

		self.assertEqual(root_WG_apparent - root_WG, 4 *4096)
		self.assertEqual(root_WL_apparent - root_WL, 3 *4096)

		root2_WG = self.prq2.WG(self.EASY_SET_SPROUT)
		root2_TG = self.prq2.TG(self.EASY_SET_SPROUT)
		root2_LG = self.prq2.LG(self.EASY_SET_SPROUT)
		root2_WL = self.prq2.WL(self.EASY_SET_SPROUT)
		root2_TL = self.prq2.TL(self.EASY_SET_SPROUT)
		root2_LL = self.prq2.LL(self.EASY_SET_SPROUT)

		root2_WG_apparent = self.prq2.WG(self.EASY_SET_SPROUT, apparent=True)
		root2_WL_apparent = self.prq2.WL(self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4 *4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 3 *4096)


	def test_branch_sprout_register_root_stats(self):

		root_WG = self.prq.WG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root_TG = self.prq.TG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root_LG = self.prq.LG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root_WL = self.prq.WL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root_TL = self.prq.TL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root_LL = self.prq.LL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)

		root_WG_apparent = self.prq.WG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True)
		root_WL_apparent = self.prq.WL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		self.assertIsInstance(root_WG_apparent, int)
		self.assertIsInstance(root_WL_apparent, int)

		self.assertEqual(root_WG_apparent - root_WG, 4 *4096)
		self.assertEqual(root_WL_apparent - root_WL, 3 *4096)

		root2_WG = self.prq2.WG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root2_TG = self.prq2.TG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root2_LG = self.prq2.LG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root2_WL = self.prq2.WL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root2_TL = self.prq2.TL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)
		root2_LL = self.prq2.LL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT)

		root2_WG_apparent = self.prq2.WG(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True)
		root2_WL_apparent = self.prq2.WL(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4 *4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 3 *4096)


	def test_sprout_register_root_stats(self):

		root_WG = self.prq.WG(sprout=self.EASY_SET_SPROUT)
		root_TG = self.prq.TG(sprout=self.EASY_SET_SPROUT)
		root_LG = self.prq.LG(sprout=self.EASY_SET_SPROUT)
		root_WL = self.prq.WL(sprout=self.EASY_SET_SPROUT)
		root_TL = self.prq.TL(sprout=self.EASY_SET_SPROUT)
		root_LL = self.prq.LL(sprout=self.EASY_SET_SPROUT)

		root_WG_apparent = self.prq.WG(sprout=self.EASY_SET_SPROUT, apparent=True)
		root_WL_apparent = self.prq.WL(sprout=self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(root_WG, int)
		self.assertIsInstance(root_WL, int)
		self.assertEqual(root_TG, 4)
		self.assertEqual(root_LG, 8)
		self.assertEqual(root_TL, 3)
		self.assertEqual(root_LL, 1)

		self.assertIsInstance(root_WG_apparent, int)
		self.assertIsInstance(root_WL_apparent, int)

		self.assertEqual(root_WG_apparent - root_WG, 4 *4096)
		self.assertEqual(root_WL_apparent - root_WL, 3 *4096)

		root2_WG = self.prq2.WG(sprout=self.EASY_SET_SPROUT)
		root2_TG = self.prq2.TG(sprout=self.EASY_SET_SPROUT)
		root2_LG = self.prq2.LG(sprout=self.EASY_SET_SPROUT)
		root2_WL = self.prq2.WL(sprout=self.EASY_SET_SPROUT)
		root2_TL = self.prq2.TL(sprout=self.EASY_SET_SPROUT)
		root2_LL = self.prq2.LL(sprout=self.EASY_SET_SPROUT)

		root2_WG_apparent = self.prq2.WG(sprout=self.EASY_SET_SPROUT, apparent=True)
		root2_WL_apparent = self.prq2.WL(sprout=self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(root2_WG, int)
		self.assertIsInstance(root2_WL, int)
		self.assertEqual(root2_TG, 4)
		self.assertEqual(root2_LG, 8)
		self.assertEqual(root2_TL, 3)
		self.assertEqual(root2_LL, 1)

		self.assertIsInstance(root2_WG_apparent, int)
		self.assertIsInstance(root2_WL_apparent, int)

		self.assertEqual(root2_WG_apparent - root2_WG, 4 *4096)
		self.assertEqual(root2_WL_apparent - root2_WL, 3 *4096)








	def test_branch_register_child_stats(self):

		child_WG = self.prq.WG(self.pros_folder)
		child_TG = self.prq.TG(self.pros_folder)
		child_LG = self.prq.LG(self.pros_folder)
		child_WL = self.prq.WL(self.pros_folder)
		child_TL = self.prq.TL(self.pros_folder)
		child_LL = self.prq.LL(self.pros_folder)

		child_WG_apparent = self.prq.WG(self.pros_folder, apparent=True)
		child_WL_apparent = self.prq.WL(self.pros_folder, apparent=True)

		self.assertIsInstance(child_WG, int)
		self.assertIsInstance(child_WL, int)
		self.assertEqual(child_TG, 1)
		self.assertEqual(child_LG, 4)
		self.assertEqual(child_TL, 1)
		self.assertEqual(child_LL, 3)

		self.assertIsInstance(child_WG_apparent, int)
		self.assertIsInstance(child_WL_apparent, int)

		self.assertEqual(child_WG_apparent - child_WG, 4096)
		self.assertEqual(child_WL_apparent - child_WL, 4096)

		child2_WG = self.prq2.WG(self.pros_folder)
		child2_TG = self.prq2.TG(self.pros_folder)
		child2_LG = self.prq2.LG(self.pros_folder)
		child2_WL = self.prq2.WL(self.pros_folder)
		child2_TL = self.prq2.TL(self.pros_folder)
		child2_LL = self.prq2.LL(self.pros_folder)

		child2_WG_apparent = self.prq2.WG(self.pros_folder, apparent=True)
		child2_WL_apparent = self.prq2.WL(self.pros_folder, apparent=True)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 1)
		self.assertEqual(child2_LG, 4)
		self.assertEqual(child2_TL, 1)
		self.assertEqual(child2_LL, 3)

		self.assertIsInstance(child2_WG_apparent, int)
		self.assertIsInstance(child2_WL_apparent, int)

		self.assertEqual(child2_WG_apparent - child2_WG, 4096)
		self.assertEqual(child2_WL_apparent - child2_WL, 4096)


	def test_branch_sprout_register_child_stats(self):

		child_WG = self.prq.WG(self.pros_folder, self.EASY_SET_SPROUT)
		child_TG = self.prq.TG(self.pros_folder, self.EASY_SET_SPROUT)
		child_LG = self.prq.LG(self.pros_folder, self.EASY_SET_SPROUT)
		child_WL = self.prq.WL(self.pros_folder, self.EASY_SET_SPROUT)
		child_TL = self.prq.TL(self.pros_folder, self.EASY_SET_SPROUT)
		child_LL = self.prq.LL(self.pros_folder, self.EASY_SET_SPROUT)

		child_WG_apparent = self.prq.WG(self.pros_folder, self.EASY_SET_SPROUT, apparent=True)
		child_WL_apparent = self.prq.WL(self.pros_folder, self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(child_WG, int)
		self.assertIsInstance(child_WL, int)
		self.assertEqual(child_TG, 1)
		self.assertEqual(child_LG, 4)
		self.assertEqual(child_TL, 1)
		self.assertEqual(child_LL, 3)

		self.assertIsInstance(child_WG_apparent, int)
		self.assertIsInstance(child_WL_apparent, int)

		self.assertEqual(child_WG_apparent - child_WG, 4096)
		self.assertEqual(child_WL_apparent - child_WL, 4096)

		child2_WG = self.prq2.WG(self.pros_folder, self.EASY_SET_SPROUT)
		child2_TG = self.prq2.TG(self.pros_folder, self.EASY_SET_SPROUT)
		child2_LG = self.prq2.LG(self.pros_folder, self.EASY_SET_SPROUT)
		child2_WL = self.prq2.WL(self.pros_folder, self.EASY_SET_SPROUT)
		child2_TL = self.prq2.TL(self.pros_folder, self.EASY_SET_SPROUT)
		child2_LL = self.prq2.LL(self.pros_folder, self.EASY_SET_SPROUT)

		child2_WG_apparent = self.prq2.WG(self.pros_folder, self.EASY_SET_SPROUT, apparent=True)
		child2_WL_apparent = self.prq2.WL(self.pros_folder, self.EASY_SET_SPROUT, apparent=True)

		self.assertIsInstance(child2_WG, int)
		self.assertIsInstance(child2_WL, int)
		self.assertEqual(child2_TG, 1)
		self.assertEqual(child2_LG, 4)
		self.assertEqual(child2_TL, 1)
		self.assertEqual(child2_LL, 3)

		self.assertIsInstance(child2_WG_apparent, int)
		self.assertIsInstance(child2_WL_apparent, int)

		self.assertEqual(child2_WG_apparent - child2_WG, 4096)
		self.assertEqual(child2_WL_apparent - child2_WL, 4096)








	def test_branch_sprout_content_root(self):

		for content in (

			self.prq.content(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT),
			self.prq.content(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True),
			self.prq2.content(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT),
			self.prq2.content(self.EASY_SET_SPROUT, self.EASY_SET_SPROUT, apparent=True),
		):
			self.assertEqual(len(content),4)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertIsInstance(content[2],tuple)
			self.assertIsInstance(content[3],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertEqual(len(content[2]),2)
			self.assertEqual(len(content[3]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)
			self.assertIsInstance(content[2][0],int)
			self.assertIsInstance(content[2][1],str)
			self.assertIsInstance(content[3][0],int)
			self.assertIsInstance(content[3][1],str)


	def test_branch_content_root(self):

		for content in (

			self.prq.content(self.EASY_SET_SPROUT),
			self.prq.content(self.EASY_SET_SPROUT, apparent=True),
			self.prq2.content(self.EASY_SET_SPROUT),
			self.prq2.content(self.EASY_SET_SPROUT, apparent=True),
		):
			self.assertEqual(len(content),4)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertIsInstance(content[2],tuple)
			self.assertIsInstance(content[3],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertEqual(len(content[2]),2)
			self.assertEqual(len(content[3]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)
			self.assertIsInstance(content[2][0],int)
			self.assertIsInstance(content[2][1],str)
			self.assertIsInstance(content[3][0],int)
			self.assertIsInstance(content[3][1],str)


	def test_sprout_content_root(self):

		for content in (

			self.prq.content(sprout=self.EASY_SET_SPROUT),
			self.prq.content(sprout=self.EASY_SET_SPROUT, apparent=True),
			self.prq2.content(sprout=self.EASY_SET_SPROUT),
			self.prq2.content(sprout=self.EASY_SET_SPROUT, apparent=True),
		):
			self.assertEqual(len(content),4)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertIsInstance(content[2],tuple)
			self.assertIsInstance(content[3],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertEqual(len(content[2]),2)
			self.assertEqual(len(content[3]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)
			self.assertIsInstance(content[2][0],int)
			self.assertIsInstance(content[2][1],str)
			self.assertIsInstance(content[3][0],int)
			self.assertIsInstance(content[3][1],str)


	def test_content_root(self):

		for content in (

			self.prq.content(),
			self.prq.content(apparent=True),
			self.prq2.content(),
			self.prq2.content(apparent=True),
		):
			self.assertEqual(len(content),4)
			self.assertIsInstance(content[0],tuple)
			self.assertIsInstance(content[1],tuple)
			self.assertIsInstance(content[2],tuple)
			self.assertIsInstance(content[3],tuple)
			self.assertEqual(len(content[0]),2)
			self.assertEqual(len(content[1]),2)
			self.assertEqual(len(content[2]),2)
			self.assertEqual(len(content[3]),2)
			self.assertIsInstance(content[0][0],int)
			self.assertIsInstance(content[0][1],str)
			self.assertIsInstance(content[1][0],int)
			self.assertIsInstance(content[1][1],str)
			self.assertIsInstance(content[2][0],int)
			self.assertIsInstance(content[2][1],str)
			self.assertIsInstance(content[3][0],int)
			self.assertIsInstance(content[3][1],str)


	def test_content_bad_shoots(self):

		for shoot in (

			1, 1., "folder", LibraryShelf, True, False, ..., print,
			[ self.EASY_SET_SPROUT ],
			( self.EASY_SET_SPROUT, ),
			{ self.EASY_SET_SPROUT },
			{ "shoot": self.EASY_SET_SPROUT },
		):
			with self.subTest(shoot=shoot):

				self.assertIsNone(self.prq.content(shoot))
				self.assertIsNone(self.prq.content(shoot, shoot))
				self.assertIsNone(self.prq.content(sprout=shoot))
				self.assertIsNone(self.prq.content(shoot, apparent=True))
				self.assertIsNone(self.prq.content(shoot, shoot, apparent=True))
				self.assertIsNone(self.prq.content(sprout=shoot, apparent=True))


	def test_content_miss_branch(self):

		self.assertIsNone(self.prq.content(self.miss_branch))
		self.assertIsNone(self.prq.content(self.miss_branch, self.EASY_SET_SPROUT))
		self.assertIsNone(self.prq.content(sprout=self.miss_branch))
		self.assertIsNone(self.prq.content(self.EASY_SET_SPROUT, self.miss_branch))

		self.assertIsNone(self.prq.content(self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.content(self.miss_branch, self.EASY_SET_SPROUT, apparent=True))
		self.assertIsNone(self.prq.content(sprout=self.miss_branch, apparent=True))
		self.assertIsNone(self.prq.content(self.EASY_SET_SPROUT, self.miss_branch, apparent=True))


	def test_content_child(self):

		for content in (

			self.prq.content(self.pros_folder),
			self.prq.content(self.pros_folder, self.EASY_SET_SPROUT),
			self.prq.content(self.pros_folder, apparent=True),
			self.prq.content(self.pros_folder, self.EASY_SET_SPROUT, apparent=True),
			self.prq2.content(self.pros_folder),
			self.prq2.content(self.pros_folder, self.EASY_SET_SPROUT),
			self.prq2.content(self.pros_folder, apparent=True),
			self.prq2.content(self.pros_folder, self.EASY_SET_SPROUT, apparent=True),
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








if __name__ == "__main__" : unittest.main(verbosity=2)







