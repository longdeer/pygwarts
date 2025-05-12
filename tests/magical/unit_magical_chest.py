import	os
import	unittest
from	typing								import Callable
from	random								import randint
from	pygwarts.tests.magical				import MagicalTestCase
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.chests				import Chest
from	pygwarts.irma.contrib				import LibraryContrib








class PackingCase(MagicalTestCase):

	"""
		Test cases for magical.chests.Chest
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.SET_HANDLER): os.remove(cls.SET_HANDLER)

	@classmethod
	def setUpClass(cls):
		class Treasure(Transmutable):

			weight	:int
			__call__:Callable[[], str]

		class CurrentChest(Chest):
			class loggy(LibraryContrib):

				init_name	= "chest"
				init_level	= 10
				handler		= cls.SET_HANDLER

			class Diamond(Treasure):

				weight	= 100
				def __call__(self): return "is forever?"

			class Ruby(Treasure):

				weight	= 150
				def __call__(self): return "shining red"

			class Jade(Treasure):

				weight	= 200
				def __call__(self): return "ZYO"

			class Sapphire(Treasure):

				weight	= 174
				def __call__(self): return "expense"

			class Gold(Treasure):

				weight	= 995
				def __call__(self): return "The Best"

			class Silver(Treasure):

				weight	= 100500
				def __call__(self): return "never too much"

			class Boot(Transmutable):

				weight	= 500
				def __call__(self): return "was caught in a river, so might be dear to heart"


		cls.make_loggy_file(cls, cls.SET_HANDLER)
		cls.test_case = CurrentChest()
		cls.test_case(cls.test_case.Diamond)
		cls.test_case(cls.test_case.Ruby)
		cls.test_case(cls.test_case.Jade)
		cls.test_case(cls.test_case.Sapphire)
		cls.test_case(cls.test_case.Gold)
		cls.test_case(cls.test_case.Silver)

		class SameChest(Chest):		pass
		class NotSameChest(Chest):
			class Diamond(Treasure):

				weight	= 1002
				def __call__(self): return "same is forever?"

			class Ruby(Treasure):

				weight	= 1502
				def __call__(self): return "same shining red"

			class Jade(Treasure):

				weight	= 2002
				def __call__(self): return "same ZYO"

			class Sapphire(Treasure):

				weight	= 1742
				def __call__(self): return "same expense"

			class Gold(Treasure):

				weight	= 9952
				def __call__(self): return "same The Best"

			class Silver(Treasure):

				weight	= 1005002
				def __call__(self): return "same never too much"

			class Boot(Transmutable):

				weight	= 5002
				def __call__(self): return "same was caught in a river, so might be dear to heart"

		cls.not_same_case = NotSameChest()
		cls.not_same_case(cls.not_same_case.Diamond)
		cls.not_same_case(cls.not_same_case.Ruby)
		cls.not_same_case(cls.not_same_case.Jade)
		cls.not_same_case(cls.not_same_case.Sapphire)
		cls.not_same_case(cls.not_same_case.Gold)
		cls.not_same_case(cls.not_same_case.Silver)

		cls.same_case = SameChest()
		cls.same_case(cls.test_case.Diamond)
		cls.same_case(cls.test_case.Ruby)
		cls.same_case(cls.test_case.Jade)
		cls.same_case(cls.test_case.Sapphire)
		cls.same_case(cls.test_case.Gold)
		cls.same_case(cls.test_case.Silver)

		cls.same_aslist = [

			cls.test_case.Diamond,
			cls.test_case.Ruby,
			cls.test_case.Jade,
			cls.test_case.Sapphire,
			cls.test_case.Gold,
			cls.test_case.Silver
		]
		cls.not_same_aslist = [

			cls.not_same_case.Diamond,
			cls.not_same_case.Ruby,
			cls.not_same_case.Jade,
			cls.not_same_case.Sapphire,
			cls.not_same_case.Gold,
			cls.not_same_case.Silver
		]
		cls.astuple = (

			cls.test_case.Diamond,
			cls.test_case.Ruby,
			cls.test_case.Jade,
			cls.test_case.Sapphire,
			cls.test_case.Gold,
			cls.test_case.Silver
		)




	def test_length(self): self.assertEqual(len(self.test_case), 6)
	def test_inners(self):

		self.assertTrue(hasattr(self.test_case, "_inside_"))
		self.assertIsInstance(self.test_case._inside_, list)
		self.assertTrue(hasattr(self.test_case, "_current"))
		self.assertIsInstance(self.test_case._current, int)




	def test_contains(self):

		self.assertIn(self.test_case.Diamond,	self.test_case)
		self.assertIn(self.test_case.Ruby,		self.test_case)
		self.assertIn(self.test_case.Jade,		self.test_case)
		self.assertIn(self.test_case.Sapphire,	self.test_case)
		self.assertIn(self.test_case.Gold,		self.test_case)
		self.assertIn(self.test_case.Silver,	self.test_case)
		self.assertNotIn(self.test_case.Boot,	self.test_case)




	def test_getitem(self):

		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)
		self.assertEqual(self.test_case[6], None)

		self.assertEqual(self.test_case[-1], self.test_case.Silver)
		self.assertEqual(self.test_case[-2], self.test_case.Gold)
		self.assertEqual(self.test_case[-3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[-4], self.test_case.Jade)
		self.assertEqual(self.test_case[-5], self.test_case.Ruby)
		self.assertEqual(self.test_case[-6], self.test_case.Diamond)
		self.assertEqual(self.test_case[-7], None)




	def test_setitem(self):

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)

		self.test_case[3] = self.test_case.Boot

		self.assertIn(self.test_case.Boot, self.test_case)
		self.assertNotIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Boot)

		with self.assertLogs("chest", 30) as case_loggy : self.test_case[3] = 42

		self.assertIn(f"WARNING:chest:Can't put \"{type(42)}\" in {self.test_case} Chest", case_loggy.output)
		self.assertIn(self.test_case.Boot, self.test_case)
		self.assertNotIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Boot)

		self.test_case[3] = self.test_case.Sapphire

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)




	def test_loading_and_deleting(self):

		self.test_case(self.test_case.Boot)
		self.assertEqual(len(self.test_case), 7)
		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)
		self.assertEqual(self.test_case[6], self.test_case.Boot)

		del self.test_case[6]
		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertEqual(len(self.test_case), 6)




	def test_unload_and_multiple_load(self):

		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)

		self.test_case.unload()
		self.assertEqual(len(self.test_case), 0)
		self.assertNotIn(self.test_case.Diamond,	self.test_case)
		self.assertNotIn(self.test_case.Ruby,		self.test_case)
		self.assertNotIn(self.test_case.Jade,		self.test_case)
		self.assertNotIn(self.test_case.Sapphire,	self.test_case)
		self.assertNotIn(self.test_case.Gold,		self.test_case)
		self.assertNotIn(self.test_case.Silver,		self.test_case)
		self.assertNotIn(self.test_case.Boot,		self.test_case)

		with self.assertLogs("chest", 10) as case_loggy :
			self.test_case(

				self.test_case.Diamond,
				self.test_case.Ruby,
				self.test_case.Jade,
				69,
				self.test_case.Sapphire,
				self.test_case.Gold,
				self.test_case.Silver
			)

		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)
		self.assertIn(f"DEBUG:chest:Discarding \"{69}\" load", case_loggy.output)

		with self.assertLogs("chest", 30) as case_loggy : self.test_case(42)
		self.assertIn(f"WARNING:chest:Can't put \"{42}\" in {self.test_case} Chest", case_loggy.output)




	def test_index(self):

		self.assertEqual(self.test_case.index(self.test_case.Diamond),	0)
		self.assertEqual(self.test_case.index(self.test_case.Ruby),		1)
		self.assertEqual(self.test_case.index(self.test_case.Jade),		2)
		self.assertEqual(self.test_case.index(self.test_case.Sapphire),	3)
		self.assertEqual(self.test_case.index(self.test_case.Gold),		4)
		self.assertEqual(self.test_case.index(self.test_case.Silver),	5)




	def test_eq_Chest(self):

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertEqual(len(self.test_case), len(self.not_same_case))

		self.assertNotEqual(self.test_case[0], self.not_same_case[0])
		self.assertNotEqual(self.test_case[1], self.not_same_case[1])
		self.assertNotEqual(self.test_case[2], self.not_same_case[2])
		self.assertNotEqual(self.test_case[3], self.not_same_case[3])
		self.assertNotEqual(self.test_case[4], self.not_same_case[4])
		self.assertNotEqual(self.test_case[5], self.not_same_case[5])

		self.assertNotEqual(self.test_case[0].weight, self.not_same_case[0].weight)
		self.assertNotEqual(self.test_case[1].weight, self.not_same_case[1].weight)
		self.assertNotEqual(self.test_case[2].weight, self.not_same_case[2].weight)
		self.assertNotEqual(self.test_case[3].weight, self.not_same_case[3].weight)
		self.assertNotEqual(self.test_case[4].weight, self.not_same_case[4].weight)
		self.assertNotEqual(self.test_case[5].weight, self.not_same_case[5].weight)

		self.assertNotEqual(self.test_case[0](), self.not_same_case[0]())
		self.assertNotEqual(self.test_case[1](), self.not_same_case[1]())
		self.assertNotEqual(self.test_case[2](), self.not_same_case[2]())
		self.assertNotEqual(self.test_case[3](), self.not_same_case[3]())
		self.assertNotEqual(self.test_case[4](), self.not_same_case[4]())
		self.assertNotEqual(self.test_case[5](), self.not_same_case[5]())


		self.assertEqual(self.test_case, self.same_case)
		self.assertEqual(len(self.test_case), len(self.same_case))

		self.assertEqual(self.test_case[0], self.same_case[0])
		self.assertEqual(self.test_case[1], self.same_case[1])
		self.assertEqual(self.test_case[2], self.same_case[2])
		self.assertEqual(self.test_case[3], self.same_case[3])
		self.assertEqual(self.test_case[4], self.same_case[4])
		self.assertEqual(self.test_case[5], self.same_case[5])

		self.assertEqual(self.test_case[0].weight, self.same_case[0].weight)
		self.assertEqual(self.test_case[1].weight, self.same_case[1].weight)
		self.assertEqual(self.test_case[2].weight, self.same_case[2].weight)
		self.assertEqual(self.test_case[3].weight, self.same_case[3].weight)
		self.assertEqual(self.test_case[4].weight, self.same_case[4].weight)
		self.assertEqual(self.test_case[5].weight, self.same_case[5].weight)

		self.assertEqual(self.test_case[0](), self.same_case[0]())
		self.assertEqual(self.test_case[1](), self.same_case[1]())
		self.assertEqual(self.test_case[2](), self.same_case[2]())
		self.assertEqual(self.test_case[3](), self.same_case[3]())
		self.assertEqual(self.test_case[4](), self.same_case[4]())
		self.assertEqual(self.test_case[5](), self.same_case[5]())




	def test_gt_ge_lt_le_Chest(self):

		self.assertEqual(self.not_same_case[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_case[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_case[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_case[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_case[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_case[5], self.not_same_case.Silver)
		del self.not_same_case[0]

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertNotEqual(len(self.test_case), len(self.not_same_case))
		self.assertGreater(self.test_case, self.not_same_case)
		self.assertGreaterEqual(self.test_case, self.not_same_case)
		self.assertLess(self.not_same_case, self.test_case)
		self.assertLessEqual(self.not_same_case, self.test_case)

		while len(self.not_same_case): del self.not_same_case[0]
		self.not_same_case(self.not_same_case.Diamond)
		self.not_same_case(self.not_same_case.Ruby)
		self.not_same_case(self.not_same_case.Jade)
		self.not_same_case(self.not_same_case.Sapphire)
		self.not_same_case(self.not_same_case.Gold)
		self.not_same_case(self.not_same_case.Silver)

		self.assertEqual(self.not_same_case[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_case[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_case[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_case[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_case[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_case[5], self.not_same_case.Silver)




	def test_eq_list(self):

		self.assertNotEqual(self.test_case, self.not_same_aslist)
		self.assertEqual(len(self.test_case), len(self.not_same_aslist))

		self.assertNotEqual(self.test_case[0], self.not_same_aslist[0])
		self.assertNotEqual(self.test_case[1], self.not_same_aslist[1])
		self.assertNotEqual(self.test_case[2], self.not_same_aslist[2])
		self.assertNotEqual(self.test_case[3], self.not_same_aslist[3])
		self.assertNotEqual(self.test_case[4], self.not_same_aslist[4])
		self.assertNotEqual(self.test_case[5], self.not_same_aslist[5])

		self.assertNotEqual(self.test_case[0].weight, self.not_same_aslist[0].weight)
		self.assertNotEqual(self.test_case[1].weight, self.not_same_aslist[1].weight)
		self.assertNotEqual(self.test_case[2].weight, self.not_same_aslist[2].weight)
		self.assertNotEqual(self.test_case[3].weight, self.not_same_aslist[3].weight)
		self.assertNotEqual(self.test_case[4].weight, self.not_same_aslist[4].weight)
		self.assertNotEqual(self.test_case[5].weight, self.not_same_aslist[5].weight)

		self.assertNotEqual(self.test_case[0](), self.not_same_aslist[0]())
		self.assertNotEqual(self.test_case[1](), self.not_same_aslist[1]())
		self.assertNotEqual(self.test_case[2](), self.not_same_aslist[2]())
		self.assertNotEqual(self.test_case[3](), self.not_same_aslist[3]())
		self.assertNotEqual(self.test_case[4](), self.not_same_aslist[4]())
		self.assertNotEqual(self.test_case[5](), self.not_same_aslist[5]())


		self.assertEqual(self.test_case, self.same_aslist)
		self.assertEqual(len(self.test_case), len(self.same_aslist))

		self.assertEqual(self.test_case[0], self.same_aslist[0])
		self.assertEqual(self.test_case[1], self.same_aslist[1])
		self.assertEqual(self.test_case[2], self.same_aslist[2])
		self.assertEqual(self.test_case[3], self.same_aslist[3])
		self.assertEqual(self.test_case[4], self.same_aslist[4])
		self.assertEqual(self.test_case[5], self.same_aslist[5])

		self.assertEqual(self.test_case[0].weight, self.same_aslist[0].weight)
		self.assertEqual(self.test_case[1].weight, self.same_aslist[1].weight)
		self.assertEqual(self.test_case[2].weight, self.same_aslist[2].weight)
		self.assertEqual(self.test_case[3].weight, self.same_aslist[3].weight)
		self.assertEqual(self.test_case[4].weight, self.same_aslist[4].weight)
		self.assertEqual(self.test_case[5].weight, self.same_aslist[5].weight)

		self.assertEqual(self.test_case[0](), self.same_aslist[0]())
		self.assertEqual(self.test_case[1](), self.same_aslist[1]())
		self.assertEqual(self.test_case[2](), self.same_aslist[2]())
		self.assertEqual(self.test_case[3](), self.same_aslist[3]())
		self.assertEqual(self.test_case[4](), self.same_aslist[4]())
		self.assertEqual(self.test_case[5](), self.same_aslist[5]())




	def test_gt_ge_lt_le_list(self):

		self.assertEqual(self.not_same_aslist[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_aslist[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_aslist[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_aslist[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_aslist[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_aslist[5], self.not_same_case.Silver)
		del self.not_same_aslist[0]

		self.assertNotEqual(self.test_case, self.not_same_aslist)
		self.assertNotEqual(len(self.test_case), len(self.not_same_aslist))
		self.assertGreater(self.test_case, self.not_same_aslist)
		self.assertGreaterEqual(self.test_case, self.not_same_aslist)
		self.assertLess(self.not_same_aslist, self.test_case)
		self.assertLessEqual(self.not_same_aslist, self.test_case)

		self.not_same_aslist.insert(0, self.not_same_case.Diamond)
		self.assertEqual(self.not_same_aslist[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_aslist[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_aslist[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_aslist[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_aslist[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_aslist[5], self.not_same_case.Silver)




	def test_iter(self):

		count = 0
		for item in self.test_case:

			self.assertIsInstance(item.weight, int)
			self.assertIsInstance(item(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))
		count = 0
		_case = iter(self.test_case)
		for one,two in zip(_case, _case):

			self.assertIsInstance(one.weight, int)
			self.assertIsInstance(one(), str)
			count += 1
			self.assertIsInstance(two.weight, int)
			self.assertIsInstance(two(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))




	def test_next(self):

		count = 0
		for _ in range(3 *len(self.test_case)):

			try:

				next(self.test_case)
				count += 1

			except	StopIteration:

				self.assertEqual(count, len(self.test_case))
				count = 0




	def test_noload_call(self):

		test_case = self.test_case()
		self.assertIsInstance(test_case, list)
		self.assertEqual(test_case, self.test_case)
		self.assertNotEqual(id(test_case), id(self.test_case))
		self.assertEqual(test_case[0], self.test_case[0])
		self.assertEqual(test_case[1], self.test_case[1])
		self.assertEqual(test_case[2], self.test_case[2])
		self.assertEqual(test_case[3], self.test_case[3])
		self.assertEqual(test_case[4], self.test_case[4])
		self.assertEqual(test_case[5], self.test_case[5])
















class SelfPackedCase(MagicalTestCase):

	"""
		Test cases for magical.chests.Chest
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.PACKED_SET_HANDLER): os.remove(cls.PACKED_SET_HANDLER)

	@classmethod
	def setUpClass(cls):
		class Treasure(Transmutable):

			weight	:int
			__call__:Callable[[], str]

			def __init__(self, *args, **kwargs):

				super().__init__(*args, **kwargs)
				if	isinstance(self._UPPER_LAYER, Chest): self._UPPER_LAYER(self)

		class CurrentChest(Chest):
			class loggy(LibraryContrib):

				init_name	= "pchest"
				init_level	= 10
				handler		= cls.PACKED_SET_HANDLER

			class Diamond(Treasure):

				weight	= 100
				def __call__(self): return "is forever?"

			class Ruby(Treasure):

				weight	= 150
				def __call__(self): return "shining red"

			class Jade(Treasure):

				weight	= 200
				def __call__(self): return "ZYO"

			class Sapphire(Treasure):

				weight	= 174
				def __call__(self): return "expense"

			class Gold(Treasure):

				weight	= 995
				def __call__(self): return "The Best"

			class Silver(Treasure):

				weight	= 100500
				def __call__(self): return "never too much"

			class Boot(Transmutable):

				weight	= 500
				def __call__(self): return "was caught in a river, so might be dear to heart"


		cls.make_loggy_file(cls, cls.PACKED_SET_HANDLER)
		cls.test_case = CurrentChest()

		class SameChest(Chest):		pass
		class NotSameChest(Chest):
			class Diamond(Treasure):

				weight	= 1002
				def __call__(self): return "same is forever?"

			class Ruby(Treasure):

				weight	= 1502
				def __call__(self): return "same shining red"

			class Jade(Treasure):

				weight	= 2002
				def __call__(self): return "same ZYO"

			class Sapphire(Treasure):

				weight	= 1742
				def __call__(self): return "same expense"

			class Gold(Treasure):

				weight	= 9952
				def __call__(self): return "same The Best"

			class Silver(Treasure):

				weight	= 1005002
				def __call__(self): return "same never too much"

			class Boot(Transmutable):

				weight	= 5002
				def __call__(self): return "same was caught in a river, so might be dear to heart"

		cls.not_same_case = NotSameChest()
		cls.same_case = SameChest()
		cls.same_case(cls.test_case.Diamond)
		cls.same_case(cls.test_case.Ruby)
		cls.same_case(cls.test_case.Jade)
		cls.same_case(cls.test_case.Sapphire)
		cls.same_case(cls.test_case.Gold)
		cls.same_case(cls.test_case.Silver)

		cls.same_aslist = [

			cls.test_case.Diamond,
			cls.test_case.Ruby,
			cls.test_case.Jade,
			cls.test_case.Sapphire,
			cls.test_case.Gold,
			cls.test_case.Silver
		]
		cls.not_same_aslist = [

			cls.not_same_case.Diamond,
			cls.not_same_case.Ruby,
			cls.not_same_case.Jade,
			cls.not_same_case.Sapphire,
			cls.not_same_case.Gold,
			cls.not_same_case.Silver
		]
		cls.astuple = (

			cls.test_case.Diamond,
			cls.test_case.Ruby,
			cls.test_case.Jade,
			cls.test_case.Sapphire,
			cls.test_case.Gold,
			cls.test_case.Silver
		)




	def test_packed_length(self): self.assertEqual(len(self.test_case), 6)
	def test_inners(self):

		self.assertTrue(hasattr(self.test_case, "_inside_"))
		self.assertIsInstance(self.test_case._inside_, list)
		self.assertTrue(hasattr(self.test_case, "_current"))
		self.assertIsInstance(self.test_case._current, int)




	def test_packed_contains(self):

		self.assertIn(self.test_case.Diamond,	self.test_case)
		self.assertIn(self.test_case.Ruby,		self.test_case)
		self.assertIn(self.test_case.Jade,		self.test_case)
		self.assertIn(self.test_case.Sapphire,	self.test_case)
		self.assertIn(self.test_case.Gold,		self.test_case)
		self.assertIn(self.test_case.Silver,	self.test_case)
		self.assertNotIn(self.test_case.Boot,	self.test_case)




	def test_packed_getitem(self):

		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)
		self.assertEqual(self.test_case[6], None)

		self.assertEqual(self.test_case[-1], self.test_case.Silver)
		self.assertEqual(self.test_case[-2], self.test_case.Gold)
		self.assertEqual(self.test_case[-3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[-4], self.test_case.Jade)
		self.assertEqual(self.test_case[-5], self.test_case.Ruby)
		self.assertEqual(self.test_case[-6], self.test_case.Diamond)
		self.assertEqual(self.test_case[-7], None)




	def test_packed_setitem(self):

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)

		self.test_case[3] = self.test_case.Boot

		self.assertIn(self.test_case.Boot, self.test_case)
		self.assertNotIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Boot)

		with self.assertLogs("pchest", 30) as case_loggy : self.test_case[3] = 42

		self.assertIn(f"WARNING:pchest:Can't put \"{type(42)}\" in {self.test_case} Chest", case_loggy.output)
		self.assertIn(self.test_case.Boot, self.test_case)
		self.assertNotIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Boot)

		self.test_case[3] = self.test_case.Sapphire

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)




	def test_packed_loading_and_deleting(self):

		self.test_case(self.test_case.Boot)
		self.assertEqual(len(self.test_case), 7)
		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)
		self.assertEqual(self.test_case[6], self.test_case.Boot)

		del self.test_case[6]
		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertEqual(len(self.test_case), 6)




	def test_packed_unload_and_multiple_load(self):

		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)

		self.test_case.unload()
		self.assertEqual(len(self.test_case), 0)
		self.assertNotIn(self.test_case.Diamond,	self.test_case)
		self.assertNotIn(self.test_case.Ruby,		self.test_case)
		self.assertNotIn(self.test_case.Jade,		self.test_case)
		self.assertNotIn(self.test_case.Sapphire,	self.test_case)
		self.assertNotIn(self.test_case.Gold,		self.test_case)
		self.assertNotIn(self.test_case.Silver,		self.test_case)
		self.assertNotIn(self.test_case.Boot,		self.test_case)

		with self.assertLogs("pchest", 10) as case_loggy :
			self.test_case(

				self.test_case.Diamond,
				self.test_case.Ruby,
				self.test_case.Jade,
				69,
				self.test_case.Sapphire,
				self.test_case.Gold,
				self.test_case.Silver
			)

		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[0], self.test_case.Diamond)
		self.assertEqual(self.test_case[1], self.test_case.Ruby)
		self.assertEqual(self.test_case[2], self.test_case.Jade)
		self.assertEqual(self.test_case[3], self.test_case.Sapphire)
		self.assertEqual(self.test_case[4], self.test_case.Gold)
		self.assertEqual(self.test_case[5], self.test_case.Silver)
		self.assertIn(f"DEBUG:pchest:Discarding \"{69}\" load", case_loggy.output)

		with self.assertLogs("pchest", 30) as case_loggy : self.test_case(42)
		self.assertIn(f"WARNING:pchest:Can't put \"{42}\" in {self.test_case} Chest", case_loggy.output)




	def test_packed_index(self):

		self.assertEqual(self.test_case.index(self.test_case.Diamond),	0)
		self.assertEqual(self.test_case.index(self.test_case.Ruby),		1)
		self.assertEqual(self.test_case.index(self.test_case.Jade),		2)
		self.assertEqual(self.test_case.index(self.test_case.Sapphire),	3)
		self.assertEqual(self.test_case.index(self.test_case.Gold),		4)
		self.assertEqual(self.test_case.index(self.test_case.Silver),	5)




	def test_packed_eq_Chest(self):

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertEqual(len(self.test_case), len(self.not_same_case))

		self.assertNotEqual(self.test_case[0], self.not_same_case[0])
		self.assertNotEqual(self.test_case[1], self.not_same_case[1])
		self.assertNotEqual(self.test_case[2], self.not_same_case[2])
		self.assertNotEqual(self.test_case[3], self.not_same_case[3])
		self.assertNotEqual(self.test_case[4], self.not_same_case[4])
		self.assertNotEqual(self.test_case[5], self.not_same_case[5])

		self.assertNotEqual(self.test_case[0].weight, self.not_same_case[0].weight)
		self.assertNotEqual(self.test_case[1].weight, self.not_same_case[1].weight)
		self.assertNotEqual(self.test_case[2].weight, self.not_same_case[2].weight)
		self.assertNotEqual(self.test_case[3].weight, self.not_same_case[3].weight)
		self.assertNotEqual(self.test_case[4].weight, self.not_same_case[4].weight)
		self.assertNotEqual(self.test_case[5].weight, self.not_same_case[5].weight)

		self.assertNotEqual(self.test_case[0](), self.not_same_case[0]())
		self.assertNotEqual(self.test_case[1](), self.not_same_case[1]())
		self.assertNotEqual(self.test_case[2](), self.not_same_case[2]())
		self.assertNotEqual(self.test_case[3](), self.not_same_case[3]())
		self.assertNotEqual(self.test_case[4](), self.not_same_case[4]())
		self.assertNotEqual(self.test_case[5](), self.not_same_case[5]())


		self.assertEqual(self.test_case, self.same_case)
		self.assertEqual(len(self.test_case), len(self.same_case))

		self.assertEqual(self.test_case[0], self.same_case[0])
		self.assertEqual(self.test_case[1], self.same_case[1])
		self.assertEqual(self.test_case[2], self.same_case[2])
		self.assertEqual(self.test_case[3], self.same_case[3])
		self.assertEqual(self.test_case[4], self.same_case[4])
		self.assertEqual(self.test_case[5], self.same_case[5])

		self.assertEqual(self.test_case[0].weight, self.same_case[0].weight)
		self.assertEqual(self.test_case[1].weight, self.same_case[1].weight)
		self.assertEqual(self.test_case[2].weight, self.same_case[2].weight)
		self.assertEqual(self.test_case[3].weight, self.same_case[3].weight)
		self.assertEqual(self.test_case[4].weight, self.same_case[4].weight)
		self.assertEqual(self.test_case[5].weight, self.same_case[5].weight)

		self.assertEqual(self.test_case[0](), self.same_case[0]())
		self.assertEqual(self.test_case[1](), self.same_case[1]())
		self.assertEqual(self.test_case[2](), self.same_case[2]())
		self.assertEqual(self.test_case[3](), self.same_case[3]())
		self.assertEqual(self.test_case[4](), self.same_case[4]())
		self.assertEqual(self.test_case[5](), self.same_case[5]())




	def test_packed_gt_ge_lt_le_Chest(self):

		self.assertEqual(self.not_same_case[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_case[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_case[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_case[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_case[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_case[5], self.not_same_case.Silver)
		del self.not_same_case[0]

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertNotEqual(len(self.test_case), len(self.not_same_case))
		self.assertGreater(self.test_case, self.not_same_case)
		self.assertGreaterEqual(self.test_case, self.not_same_case)
		self.assertLess(self.not_same_case, self.test_case)
		self.assertLessEqual(self.not_same_case, self.test_case)

		while len(self.not_same_case): del self.not_same_case[0]
		self.not_same_case(self.not_same_case.Diamond)
		self.not_same_case(self.not_same_case.Ruby)
		self.not_same_case(self.not_same_case.Jade)
		self.not_same_case(self.not_same_case.Sapphire)
		self.not_same_case(self.not_same_case.Gold)
		self.not_same_case(self.not_same_case.Silver)

		self.assertEqual(self.not_same_case[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_case[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_case[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_case[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_case[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_case[5], self.not_same_case.Silver)




	def test_packed_eq_list(self):

		self.assertNotEqual(self.test_case, self.not_same_aslist)
		self.assertEqual(len(self.test_case), len(self.not_same_aslist))

		self.assertNotEqual(self.test_case[0], self.not_same_aslist[0])
		self.assertNotEqual(self.test_case[1], self.not_same_aslist[1])
		self.assertNotEqual(self.test_case[2], self.not_same_aslist[2])
		self.assertNotEqual(self.test_case[3], self.not_same_aslist[3])
		self.assertNotEqual(self.test_case[4], self.not_same_aslist[4])
		self.assertNotEqual(self.test_case[5], self.not_same_aslist[5])

		self.assertNotEqual(self.test_case[0].weight, self.not_same_aslist[0].weight)
		self.assertNotEqual(self.test_case[1].weight, self.not_same_aslist[1].weight)
		self.assertNotEqual(self.test_case[2].weight, self.not_same_aslist[2].weight)
		self.assertNotEqual(self.test_case[3].weight, self.not_same_aslist[3].weight)
		self.assertNotEqual(self.test_case[4].weight, self.not_same_aslist[4].weight)
		self.assertNotEqual(self.test_case[5].weight, self.not_same_aslist[5].weight)

		self.assertNotEqual(self.test_case[0](), self.not_same_aslist[0]())
		self.assertNotEqual(self.test_case[1](), self.not_same_aslist[1]())
		self.assertNotEqual(self.test_case[2](), self.not_same_aslist[2]())
		self.assertNotEqual(self.test_case[3](), self.not_same_aslist[3]())
		self.assertNotEqual(self.test_case[4](), self.not_same_aslist[4]())
		self.assertNotEqual(self.test_case[5](), self.not_same_aslist[5]())


		self.assertEqual(self.test_case, self.same_aslist)
		self.assertEqual(len(self.test_case), len(self.same_aslist))

		self.assertEqual(self.test_case[0], self.same_aslist[0])
		self.assertEqual(self.test_case[1], self.same_aslist[1])
		self.assertEqual(self.test_case[2], self.same_aslist[2])
		self.assertEqual(self.test_case[3], self.same_aslist[3])
		self.assertEqual(self.test_case[4], self.same_aslist[4])
		self.assertEqual(self.test_case[5], self.same_aslist[5])

		self.assertEqual(self.test_case[0].weight, self.same_aslist[0].weight)
		self.assertEqual(self.test_case[1].weight, self.same_aslist[1].weight)
		self.assertEqual(self.test_case[2].weight, self.same_aslist[2].weight)
		self.assertEqual(self.test_case[3].weight, self.same_aslist[3].weight)
		self.assertEqual(self.test_case[4].weight, self.same_aslist[4].weight)
		self.assertEqual(self.test_case[5].weight, self.same_aslist[5].weight)

		self.assertEqual(self.test_case[0](), self.same_aslist[0]())
		self.assertEqual(self.test_case[1](), self.same_aslist[1]())
		self.assertEqual(self.test_case[2](), self.same_aslist[2]())
		self.assertEqual(self.test_case[3](), self.same_aslist[3]())
		self.assertEqual(self.test_case[4](), self.same_aslist[4]())
		self.assertEqual(self.test_case[5](), self.same_aslist[5]())




	def test_packed_gt_ge_lt_le_list(self):

		self.assertEqual(self.not_same_aslist[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_aslist[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_aslist[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_aslist[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_aslist[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_aslist[5], self.not_same_case.Silver)
		del self.not_same_aslist[0]

		self.assertNotEqual(self.test_case, self.not_same_aslist)
		self.assertNotEqual(len(self.test_case), len(self.not_same_aslist))
		self.assertGreater(self.test_case, self.not_same_aslist)
		self.assertGreaterEqual(self.test_case, self.not_same_aslist)
		self.assertLess(self.not_same_aslist, self.test_case)
		self.assertLessEqual(self.not_same_aslist, self.test_case)

		self.not_same_aslist.insert(0, self.not_same_case.Diamond)
		self.assertEqual(self.not_same_aslist[0], self.not_same_case.Diamond)
		self.assertEqual(self.not_same_aslist[1], self.not_same_case.Ruby)
		self.assertEqual(self.not_same_aslist[2], self.not_same_case.Jade)
		self.assertEqual(self.not_same_aslist[3], self.not_same_case.Sapphire)
		self.assertEqual(self.not_same_aslist[4], self.not_same_case.Gold)
		self.assertEqual(self.not_same_aslist[5], self.not_same_case.Silver)




	def test_iter(self):

		count = 0
		for item in self.test_case:

			self.assertIsInstance(item.weight, int)
			self.assertIsInstance(item(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))
		count = 0
		_case = iter(self.test_case)
		for one,two in zip(_case, _case):

			self.assertIsInstance(one.weight, int)
			self.assertIsInstance(one(), str)
			count += 1
			self.assertIsInstance(two.weight, int)
			self.assertIsInstance(two(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))




	def test_next(self):

		count = 0
		for _ in range(3 *len(self.test_case)):

			try:

				next(self.test_case)
				count += 1

			except	StopIteration:

				self.assertEqual(count, len(self.test_case))
				count = 0




	def test_packed_noload_call(self):

		test_case = self.test_case()
		self.assertIsInstance(test_case, list)
		self.assertEqual(test_case, self.test_case)
		self.assertNotEqual(id(test_case), id(self.test_case))
		self.assertEqual(test_case[0], self.test_case[0])
		self.assertEqual(test_case[1], self.test_case[1])
		self.assertEqual(test_case[2], self.test_case[2])
		self.assertEqual(test_case[3], self.test_case[3])
		self.assertEqual(test_case[4], self.test_case[4])
		self.assertEqual(test_case[5], self.test_case[5])








if __name__ == "__main__" : unittest.main(verbosity=2)







