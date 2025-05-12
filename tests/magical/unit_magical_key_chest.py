import	os
import	unittest
from	typing								import Callable
from	pygwarts.tests.magical				import MagicalTestCase
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.chests				import KeyChest
from	pygwarts.irma.contrib				import LibraryContrib








class KeyChestCase(MagicalTestCase):

	"""
		Test cases for magical.chests.KeyChest
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.KEY_SET_HANDLER): os.remove(cls.KEY_SET_HANDLER)

	@classmethod
	def setUpClass(cls):
		class Treasure(Transmutable):

			weight	:int
			__call__:Callable[[], str]

		class CurrentChest(KeyChest):
			class loggy(LibraryContrib):

				init_name	= "key_chest"
				init_level	= 10
				handler		= cls.KEY_SET_HANDLER

			class Diamond(Treasure):

				weight	= 150
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


		cls.make_loggy_file(cls, cls.KEY_SET_HANDLER)
		cls.test_case = CurrentChest()
		cls.test_case(cls.test_case.Diamond,	cls.test_case.Diamond.weight)
		cls.test_case(cls.test_case.Ruby,		cls.test_case.Ruby.weight)
		cls.test_case(cls.test_case.Jade,		cls.test_case.Jade.weight)
		cls.test_case(cls.test_case.Sapphire,	cls.test_case.Sapphire.weight)
		cls.test_case(cls.test_case.Gold,		cls.test_case.Gold.weight)
		cls.test_case(cls.test_case.Silver,		cls.test_case.Silver.weight)

		class SameChest(KeyChest):	pass
		class NotSameChest(KeyChest):
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
		cls.not_same_case(cls.not_same_case.Diamond,	cls.not_same_case.Diamond.weight)
		cls.not_same_case(cls.not_same_case.Ruby,		cls.not_same_case.Ruby.weight)
		cls.not_same_case(cls.not_same_case.Jade,		cls.not_same_case.Jade.weight)
		cls.not_same_case(cls.not_same_case.Sapphire,	cls.not_same_case.Sapphire.weight)
		cls.not_same_case(cls.not_same_case.Gold,		cls.not_same_case.Gold.weight)
		cls.not_same_case(cls.not_same_case.Silver,		cls.not_same_case.Silver.weight)

		cls.same_case = SameChest()
		cls.same_case(cls.test_case.Diamond,	cls.test_case.Diamond.weight)
		cls.same_case(cls.test_case.Ruby,		cls.test_case.Ruby.weight)
		cls.same_case(cls.test_case.Jade,		cls.test_case.Jade.weight)
		cls.same_case(cls.test_case.Sapphire,	cls.test_case.Sapphire.weight)
		cls.same_case(cls.test_case.Gold,		cls.test_case.Gold.weight)
		cls.same_case(cls.test_case.Silver,		cls.test_case.Silver.weight)

		cls.same_asdict = {

			cls.test_case.Diamond:	cls.test_case.Diamond.weight,
			cls.test_case.Ruby:		cls.test_case.Ruby.weight,
			cls.test_case.Jade:		cls.test_case.Jade.weight,
			cls.test_case.Sapphire:	cls.test_case.Sapphire.weight,
			cls.test_case.Gold:		cls.test_case.Gold.weight,
			cls.test_case.Silver:	cls.test_case.Silver.weight
		}
		cls.not_same_asdict = {

			cls.not_same_case.Diamond:	cls.not_same_case.Diamond.weight,
			cls.not_same_case.Ruby:		cls.not_same_case.Ruby.weight,
			cls.not_same_case.Jade:		cls.not_same_case.Jade.weight,
			cls.not_same_case.Sapphire:	cls.not_same_case.Sapphire.weight,
			cls.not_same_case.Gold:		cls.not_same_case.Gold.weight,
			cls.not_same_case.Silver:	cls.not_same_case.Silver.weight
		}




	def test_length(self): self.assertEqual(len(self.test_case), 6)
	def test_contains(self):

		self.assertIn(self.test_case.Diamond,	self.test_case)
		self.assertIn(self.test_case.Ruby,		self.test_case)
		self.assertIn(self.test_case.Jade,		self.test_case)
		self.assertIn(self.test_case.Sapphire,	self.test_case)
		self.assertIn(self.test_case.Gold,		self.test_case)
		self.assertIn(self.test_case.Silver,	self.test_case)
		self.assertNotIn(self.test_case.Boot,	self.test_case)




	def test_getitem(self):

		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)
		self.assertEqual(self.test_case[self.test_case.Boot],		None)




	def test_setitem_and_delitem(self):

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[self.test_case.Sapphire], self.test_case.Sapphire.weight)

		self.test_case[self.test_case.Sapphire] = 69
		self.test_case[self.test_case.Boot] = self.test_case.Boot.weight

		self.assertIn(self.test_case.Boot, self.test_case)
		self.assertEqual(self.test_case[self.test_case.Boot], self.test_case.Boot.weight)
		self.assertNotEqual(self.test_case[self.test_case.Sapphire], self.test_case.Sapphire.weight)

		with self.assertLogs("key_chest", 30) as case_loggy : self.test_case[[self.test_case.Sapphire]] = 42

		self.assertIn(

			f"WARNING:key_chest:Can't put \"{[self.test_case.Sapphire]}\", "
			f"\"{42}\" pair in {self.test_case} KeyChest",
			case_loggy.output
		)

		self.test_case[self.test_case.Sapphire] = self.test_case.Sapphire.weight
		del self.test_case[self.test_case.Boot]

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[self.test_case.Sapphire], self.test_case.Sapphire.weight)


		# Broken "_locker_" must make some raise resulting warning log message
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		with self.assertLogs("key_chest", 30) as case_loggy: del self.test_case[self.test_case.Gold]
		self.assertIn(
			f"WARNING:key_chest:Key \"{self.test_case.Gold}\" not found in locker", case_loggy.output
		)
		self.test_case._locker_ = locker[:]




	def test_loading_and_deleting(self):

		self.test_case(self.test_case.Boot, self.test_case.Boot.weight)
		self.assertEqual(len(self.test_case), 7)
		self.assertEqual(self.test_case[self.test_case.Diamond], 	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby], 		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade], 		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire], 	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold], 		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver], 	self.test_case.Silver.weight)
		self.assertEqual(self.test_case[self.test_case.Boot], 		self.test_case.Boot.weight)

		del self.test_case[self.test_case.Boot]
		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertEqual(len(self.test_case), 6)




	def test_nested_loading_and_deleting(self):

		self.test_case("deep", {})
		self.test_case("deeper", {}, "deep")
		self.test_case("deepest", {}, "deep", "deeper")
		self.assertIn("deep", self.test_case)
		self.assertIn("deeper", self.test_case["deep"])
		self.assertIn("deepest", self.test_case["deep"]["deeper"])


		self.test_case(self.test_case.Boot, self.test_case.Boot.weight, "deep")
		self.test_case(self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper")
		self.test_case(self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper", "deepest")
		self.assertEqual(len(self.test_case), 7)
		self.assertIn(self.test_case.Boot, self.test_case["deep"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"]["deepest"])
		self.assertEqual(
			self.test_case["deep"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"]["deepest"][self.test_case.Boot], self.test_case.Boot.weight
		)


		del self.test_case["deep"]
		self.assertEqual(len(self.test_case), 6)


		self.test_case(
			self.test_case.Boot, self.test_case.Boot.weight, "deep", mapped=False
		)
		self.test_case(
			self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper", mapped=False
		)
		self.test_case(
			self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper", "deepest", mapped=False
		)
		self.assertEqual(len(self.test_case), 7)
		self.assertIn(self.test_case.Boot, self.test_case["deep"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"]["deepest"])
		self.assertEqual(
			self.test_case["deep"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"]["deepest"][self.test_case.Boot], self.test_case.Boot.weight
		)


		del self.test_case["deep"]
		self.assertEqual(len(self.test_case), 6)




	def test_unload(self):

		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)

		self.test_case.unload()
		self.assertEqual(len(self.test_case), 0)
		self.assertNotIn(self.test_case.Diamond,	self.test_case)
		self.assertNotIn(self.test_case.Ruby,		self.test_case)
		self.assertNotIn(self.test_case.Jade,		self.test_case)
		self.assertNotIn(self.test_case.Sapphire,	self.test_case)
		self.assertNotIn(self.test_case.Gold,		self.test_case)
		self.assertNotIn(self.test_case.Silver,		self.test_case)
		self.assertNotIn(self.test_case.Boot,		self.test_case)
		self.assertEqual(self.test_case[self.test_case.Diamond],	None)
		self.assertEqual(self.test_case[self.test_case.Ruby],		None)
		self.assertEqual(self.test_case[self.test_case.Jade],		None)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	None)
		self.assertEqual(self.test_case[self.test_case.Gold],		None)
		self.assertEqual(self.test_case[self.test_case.Silver],		None)

		self.test_case(self.test_case.Diamond,	self.test_case.Diamond.weight)
		self.test_case(self.test_case.Ruby,		self.test_case.Ruby.weight)
		self.test_case(self.test_case.Jade,		self.test_case.Jade.weight)
		self.test_case(self.test_case.Sapphire,	self.test_case.Sapphire.weight)
		self.test_case(self.test_case.Gold,		self.test_case.Gold.weight)
		self.test_case(self.test_case.Silver,	self.test_case.Silver.weight)
		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)




	def test_keysof(self):

		self.assertEqual(

			self.test_case.keysof(self.test_case.Diamond.weight),
			[ self.test_case.Diamond, self.test_case.Ruby ]
		)
		self.assertEqual(

			self.test_case.keysof(self.test_case.Ruby.weight),
			[ self.test_case.Diamond, self.test_case.Ruby ]
		)
		self.assertEqual(self.test_case.keysof(self.test_case.Jade.weight),		[ self.test_case.Jade ])
		self.assertEqual(self.test_case.keysof(self.test_case.Sapphire.weight),	[ self.test_case.Sapphire ])
		self.assertEqual(self.test_case.keysof(self.test_case.Gold.weight),		[ self.test_case.Gold ])
		self.assertEqual(self.test_case.keysof(self.test_case.Silver.weight),	[ self.test_case.Silver ])
		self.assertEqual(self.test_case.keysof(self.test_case.Boot.weight),		[])


		# Broken "_locker_" case
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		self.assertEqual(self.test_case.keysof(self.test_case.Diamond.weight),	[])
		self.assertEqual(self.test_case.keysof(self.test_case.Ruby.weight),		[])
		self.assertEqual(self.test_case.keysof(self.test_case.Jade.weight),		[])
		self.assertEqual(self.test_case.keysof(self.test_case.Sapphire.weight),	[])
		self.assertEqual(self.test_case.keysof(self.test_case.Gold.weight),		[])
		self.assertEqual(self.test_case.keysof(self.test_case.Silver.weight),	[])
		self.assertEqual(self.test_case.keysof(self.test_case.Boot.weight),		[])
		self.test_case._locker_ = locker[:]




	def test_eq_Chest(self):

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertEqual(len(self.test_case), len(self.not_same_case))

		self.assertNotEqual(
			self.test_case[self.test_case.Diamond],		self.not_same_case[self.not_same_case.Diamond]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Ruby],		self.not_same_case[self.not_same_case.Ruby]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Jade],		self.not_same_case[self.not_same_case.Jade]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Sapphire],	self.not_same_case[self.not_same_case.Sapphire]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Gold],		self.not_same_case[self.not_same_case.Gold]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Silver],		self.not_same_case[self.not_same_case.Silver]
		)

		self.assertEqual(self.test_case, self.same_case)
		self.assertEqual(len(self.test_case), len(self.same_case))

		self.assertEqual(
			self.test_case[self.test_case.Diamond],		self.same_case[self.test_case.Diamond]
		)
		self.assertEqual(
			self.test_case[self.test_case.Ruby],		self.same_case[self.test_case.Ruby]
		)
		self.assertEqual(
			self.test_case[self.test_case.Jade],		self.same_case[self.test_case.Jade]
		)
		self.assertEqual(
			self.test_case[self.test_case.Sapphire],	self.same_case[self.test_case.Sapphire]
		)
		self.assertEqual(
			self.test_case[self.test_case.Gold],		self.same_case[self.test_case.Gold]
		)
		self.assertEqual(
			self.test_case[self.test_case.Silver],		self.same_case[self.test_case.Silver]
		)




	def test_gt_ge_lt_le_Chest(self):

		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)
		del self.not_same_case[self.not_same_case.Diamond]

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertNotEqual(len(self.test_case), len(self.not_same_case))
		self.assertGreater(self.test_case, self.not_same_case)
		self.assertGreaterEqual(self.test_case, self.not_same_case)
		self.assertLess(self.not_same_case, self.test_case)
		self.assertLessEqual(self.not_same_case, self.test_case)

		self.not_same_case.unload()
		self.not_same_case(self.not_same_case.Diamond,	self.not_same_case.Diamond.weight)
		self.not_same_case(self.not_same_case.Ruby,		self.not_same_case.Ruby.weight)
		self.not_same_case(self.not_same_case.Jade,		self.not_same_case.Jade.weight)
		self.not_same_case(self.not_same_case.Sapphire,	self.not_same_case.Sapphire.weight)
		self.not_same_case(self.not_same_case.Gold,		self.not_same_case.Gold.weight)
		self.not_same_case(self.not_same_case.Silver,	self.not_same_case.Silver.weight)

		self.assertEqual(self.not_same_case[self.not_same_case.Diamond],	self.not_same_case.Diamond.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Ruby],		self.not_same_case.Ruby.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Jade],		self.not_same_case.Jade.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Sapphire],	self.not_same_case.Sapphire.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Gold],		self.not_same_case.Gold.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Silver],		self.not_same_case.Silver.weight)




	def test_eq_dict(self):

		self.assertNotEqual(self.test_case, self.not_same_asdict)
		self.assertEqual(len(self.test_case), len(self.not_same_asdict))

		self.assertNotEqual(
			self.test_case[self.test_case.Diamond],		self.not_same_asdict[self.not_same_case.Diamond]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Ruby],		self.not_same_asdict[self.not_same_case.Ruby]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Jade],		self.not_same_asdict[self.not_same_case.Jade]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Sapphire],	self.not_same_asdict[self.not_same_case.Sapphire]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Gold],		self.not_same_asdict[self.not_same_case.Gold]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Silver],		self.not_same_asdict[self.not_same_case.Silver]
		)


		self.assertEqual(self.test_case, self.same_asdict)
		self.assertEqual(len(self.test_case), len(self.same_asdict))

		self.assertEqual(
			self.test_case[self.test_case.Diamond],		self.same_asdict[self.test_case.Diamond]
		)
		self.assertEqual(
			self.test_case[self.test_case.Ruby],		self.same_asdict[self.test_case.Ruby]
		)
		self.assertEqual(
			self.test_case[self.test_case.Jade],		self.same_asdict[self.test_case.Jade]
		)
		self.assertEqual(
			self.test_case[self.test_case.Sapphire],	self.same_asdict[self.test_case.Sapphire]
		)
		self.assertEqual(
			self.test_case[self.test_case.Gold],		self.same_asdict[self.test_case.Gold]
		)
		self.assertEqual(
			self.test_case[self.test_case.Silver],		self.same_asdict[self.test_case.Silver]
		)




	def test_gt_ge_lt_le_list(self):

		self.assertEqual(self.not_same_asdict[self.not_same_case.Diamond],	self.not_same_case.Diamond.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Ruby],		self.not_same_case.Ruby.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Jade],		self.not_same_case.Jade.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Sapphire],	self.not_same_case.Sapphire.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Gold],		self.not_same_case.Gold.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Silver],	self.not_same_case.Silver.weight)
		del self.not_same_asdict[self.not_same_case.Diamond]

		self.assertNotEqual(self.test_case, self.not_same_asdict)
		self.assertNotEqual(len(self.test_case), len(self.not_same_asdict))
		self.assertGreater(self.test_case, self.not_same_asdict)
		self.assertGreaterEqual(self.test_case, self.not_same_asdict)
		self.assertLess(self.not_same_asdict, self.test_case)
		self.assertLessEqual(self.not_same_asdict, self.test_case)

		del self.not_same_asdict[self.not_same_case.Ruby]
		del self.not_same_asdict[self.not_same_case.Jade]
		del self.not_same_asdict[self.not_same_case.Sapphire]
		del self.not_same_asdict[self.not_same_case.Gold]
		del self.not_same_asdict[self.not_same_case.Silver]
		self.assertFalse(self.not_same_asdict)
		self.not_same_asdict[self.not_same_case.Diamond]	=	self.not_same_case.Diamond.weight
		self.not_same_asdict[self.not_same_case.Ruby]		=	self.not_same_case.Ruby.weight
		self.not_same_asdict[self.not_same_case.Jade]		=	self.not_same_case.Jade.weight
		self.not_same_asdict[self.not_same_case.Sapphire]	=	self.not_same_case.Sapphire.weight
		self.not_same_asdict[self.not_same_case.Gold]		=	self.not_same_case.Gold.weight
		self.not_same_asdict[self.not_same_case.Silver]		=	self.not_same_case.Silver.weight

		self.assertEqual(self.not_same_asdict[self.not_same_case.Diamond],	self.not_same_case.Diamond.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Ruby],		self.not_same_case.Ruby.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Jade],		self.not_same_case.Jade.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Sapphire],	self.not_same_case.Sapphire.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Gold],		self.not_same_case.Gold.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Silver],	self.not_same_case.Silver.weight)




	def test_iter(self):

		count = 0
		for K,V in self.test_case:

			self.assertEqual(K.weight, V)
			self.assertIsInstance(K(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))
		count = 0
		_case = iter(self.test_case)
		for one,two in zip(_case, _case):

			Kone,Vone = one
			self.assertEqual(Kone.weight, Vone)
			self.assertIsInstance(Kone(), str)
			count += 1
			Ktwo,Vtwo = two
			self.assertEqual(Ktwo.weight, Vtwo)
			self.assertIsInstance(Ktwo(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))


		# Breaking iteration by messing with "_locker_":
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		count = 0
		for K,V in self.test_case:

			self.assertEqual(K.weight, V)
			self.assertIsInstance(K(), str)
			count += 1

		self.assertEqual(count, 0)
		self.assertEqual(len(self.test_case), 6)
		self.assertNotEqual(count, len(self.test_case))
		self.test_case._locker_ = locker[:]




	def test_next(self):

		count = 0
		for _ in range(3 *len(self.test_case)):

			try:

				K,V = next(self.test_case)
				self.assertEqual(K.weight, V)
				self.assertIsInstance(K(), str)
				count += 1

			except	StopIteration:

				self.assertEqual(count, len(self.test_case))
				count = 0


		# Breaking "_locker_" and __next__ always raises StopIteration
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		count = 0
		for _ in range(3):

			try:

				next(self.test_case)
				count += 1

			except	StopIteration : self.assertEqual(count,0)

		self.assertEqual(count,0)
		self.test_case._locker_ = locker[:]




	def test_reversed(self):

		# Direct
		self.assertEqual(
			[ V for K,V in self.test_case ],
			[
				self.test_case.Diamond.weight,
				self.test_case.Ruby.weight,
				self.test_case.Jade.weight,
				self.test_case.Sapphire.weight,
				self.test_case.Gold.weight,
				self.test_case.Silver.weight
			]
		)

		# Reversed
		self.assertEqual(
			[ V for K,V in reversed(self.test_case) ],
			[
				self.test_case.Silver.weight,
				self.test_case.Gold.weight,
				self.test_case.Sapphire.weight,
				self.test_case.Jade.weight,
				self.test_case.Ruby.weight,
				self.test_case.Diamond.weight
			]
		)

		# Broken "_locker_" that already reversed
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = list(reversed(self.test_case._locker_))
		self.assertEqual(
			[ V for K,V in reversed(self.test_case) ],
			[
				self.test_case.Diamond.weight,
				self.test_case.Ruby.weight,
				self.test_case.Jade.weight,
				self.test_case.Sapphire.weight,
				self.test_case.Gold.weight,
				self.test_case.Silver.weight
			]
		)

		# Broken "_locker_" that is empty
		self.test_case._locker_ = []
		self.assertEqual([ V for K,V in self.test_case ], [])
		self.test_case._locker_ = locker[:]




	def test_noload_call(self):

		test_case = self.test_case()
		self.assertIsInstance(test_case, dict)
		self.assertEqual(test_case, self.test_case())
		self.assertNotEqual(id(test_case), id(self.test_case))

		self.assertEqual(self.test_case[self.test_case.Diamond],	test_case[str(self.test_case.Diamond)])
		self.assertEqual(self.test_case[self.test_case.Ruby],		test_case[str(self.test_case.Ruby)])
		self.assertEqual(self.test_case[self.test_case.Jade],		test_case[str(self.test_case.Jade)])
		self.assertEqual(self.test_case[self.test_case.Sapphire],	test_case[str(self.test_case.Sapphire)])
		self.assertEqual(self.test_case[self.test_case.Gold],		test_case[str(self.test_case.Gold)])
		self.assertEqual(self.test_case[self.test_case.Silver],		test_case[str(self.test_case.Silver)])
















class KeySelfPackedCase(MagicalTestCase):

	"""
		Test cases for magical.chests.Chest
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.PACKED_KEY_SET_HANDLER): os.remove(cls.PACKED_KEY_SET_HANDLER)

	@classmethod
	def setUpClass(cls):
		class Treasure(Transmutable):

			weight	:int
			__call__:Callable[[], str]

			def __init__(self, *args, **kwargs):

				super().__init__(*args, **kwargs)
				if	isinstance(self._UPPER_LAYER, KeyChest): self._UPPER_LAYER(self, self.weight)

		class CurrentChest(KeyChest):
			class loggy(LibraryContrib):

				init_name	= "pkey_chest"
				init_level	= 10
				handler		= cls.PACKED_KEY_SET_HANDLER

			class Diamond(Treasure):

				weight	= 150
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


		cls.make_loggy_file(cls, cls.PACKED_KEY_SET_HANDLER)
		cls.test_case = CurrentChest()

		class SameChest(KeyChest):	pass
		class NotSameChest(KeyChest):
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
		cls.same_case(cls.test_case.Diamond,	cls.test_case.Diamond.weight)
		cls.same_case(cls.test_case.Ruby,		cls.test_case.Ruby.weight)
		cls.same_case(cls.test_case.Jade,		cls.test_case.Jade.weight)
		cls.same_case(cls.test_case.Sapphire,	cls.test_case.Sapphire.weight)
		cls.same_case(cls.test_case.Gold,		cls.test_case.Gold.weight)
		cls.same_case(cls.test_case.Silver,		cls.test_case.Silver.weight)

		cls.same_asdict = {

			cls.test_case.Diamond:	cls.test_case.Diamond.weight,
			cls.test_case.Ruby:		cls.test_case.Ruby.weight,
			cls.test_case.Jade:		cls.test_case.Jade.weight,
			cls.test_case.Sapphire:	cls.test_case.Sapphire.weight,
			cls.test_case.Gold:		cls.test_case.Gold.weight,
			cls.test_case.Silver:	cls.test_case.Silver.weight
		}
		cls.not_same_asdict = {

			cls.not_same_case.Diamond:	cls.not_same_case.Diamond.weight,
			cls.not_same_case.Ruby:		cls.not_same_case.Ruby.weight,
			cls.not_same_case.Jade:		cls.not_same_case.Jade.weight,
			cls.not_same_case.Sapphire:	cls.not_same_case.Sapphire.weight,
			cls.not_same_case.Gold:		cls.not_same_case.Gold.weight,
			cls.not_same_case.Silver:	cls.not_same_case.Silver.weight
		}




	def test_packed_length(self):	self.assertEqual(len(self.test_case), 6)
	def test_packed_keys(self):		self.assertEqual(self.test_case.keys(), self.test_case._locker_)
	def test_packed_contains(self):

		self.assertIn(self.test_case.Diamond,	self.test_case)
		self.assertIn(self.test_case.Ruby,		self.test_case)
		self.assertIn(self.test_case.Jade,		self.test_case)
		self.assertIn(self.test_case.Sapphire,	self.test_case)
		self.assertIn(self.test_case.Gold,		self.test_case)
		self.assertIn(self.test_case.Silver,	self.test_case)
		self.assertNotIn(self.test_case.Boot,	self.test_case)




	def test_packed_getitem(self):

		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)
		self.assertEqual(self.test_case[self.test_case.Boot],		None)




	def test_packed_setitem_and_delitem(self):

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[self.test_case.Sapphire], self.test_case.Sapphire.weight)

		self.test_case[self.test_case.Sapphire] = 69
		self.test_case[self.test_case.Boot] = self.test_case.Boot.weight

		self.assertIn(self.test_case.Boot, self.test_case)
		self.assertEqual(self.test_case[self.test_case.Boot], self.test_case.Boot.weight)
		self.assertNotEqual(self.test_case[self.test_case.Sapphire], self.test_case.Sapphire.weight)

		with self.assertLogs("pkey_chest", 30) as case_loggy : self.test_case[[self.test_case.Sapphire]] = 42

		self.assertIn(

			f"WARNING:pkey_chest:Can't put \"{[self.test_case.Sapphire]}\", "
			f"\"{42}\" pair in {self.test_case} KeyChest",
			case_loggy.output
		)

		self.test_case[self.test_case.Sapphire] = self.test_case.Sapphire.weight
		del self.test_case[self.test_case.Boot]

		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertIn(self.test_case.Sapphire, self.test_case)
		self.assertEqual(self.test_case[self.test_case.Sapphire], self.test_case.Sapphire.weight)


		# Broken "_locker_" must make some raise resulting warning log message
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		with self.assertLogs("pkey_chest", 30) as case_loggy: del self.test_case[self.test_case.Gold]
		self.assertIn(
			f"WARNING:pkey_chest:Key \"{self.test_case.Gold}\" not found in locker", case_loggy.output
		)
		self.test_case._locker_ = locker[:]




	def test_packed_loading_and_deleting(self):

		self.test_case(self.test_case.Boot, self.test_case.Boot.weight)
		self.assertEqual(len(self.test_case), 7)
		self.assertEqual(self.test_case[self.test_case.Diamond], 	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby], 		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade], 		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire], 	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold], 		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver], 	self.test_case.Silver.weight)
		self.assertEqual(self.test_case[self.test_case.Boot], 		self.test_case.Boot.weight)

		del self.test_case[self.test_case.Boot]
		self.assertNotIn(self.test_case.Boot, self.test_case)
		self.assertEqual(len(self.test_case), 6)




	def test_packed_nested_loading_and_deleting(self):

		self.test_case("deep", {})
		self.test_case("deeper", {}, "deep")
		self.test_case("deepest", {}, "deep", "deeper")
		self.assertIn("deep", self.test_case)
		self.assertIn("deeper", self.test_case["deep"])
		self.assertIn("deepest", self.test_case["deep"]["deeper"])


		self.test_case(self.test_case.Boot, self.test_case.Boot.weight, "deep")
		self.test_case(self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper")
		self.test_case(self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper", "deepest")
		self.assertEqual(len(self.test_case), 7)
		self.assertIn(self.test_case.Boot, self.test_case["deep"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"]["deepest"])
		self.assertEqual(
			self.test_case["deep"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"]["deepest"][self.test_case.Boot], self.test_case.Boot.weight
		)


		del self.test_case["deep"]
		self.assertEqual(len(self.test_case), 6)


		self.test_case(
			self.test_case.Boot, self.test_case.Boot.weight, "deep", mapped=False
		)
		self.test_case(
			self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper", mapped=False
		)
		self.test_case(
			self.test_case.Boot, self.test_case.Boot.weight, "deep", "deeper", "deepest", mapped=False
		)
		self.assertEqual(len(self.test_case), 7)
		self.assertIn(self.test_case.Boot, self.test_case["deep"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"])
		self.assertIn(self.test_case.Boot, self.test_case["deep"]["deeper"]["deepest"])
		self.assertEqual(
			self.test_case["deep"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"][self.test_case.Boot], self.test_case.Boot.weight
		)
		self.assertEqual(
			self.test_case["deep"]["deeper"]["deepest"][self.test_case.Boot], self.test_case.Boot.weight
		)


		del self.test_case["deep"]
		self.assertEqual(len(self.test_case), 6)




	def test_packed_unload(self):

		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)

		self.test_case.unload()
		self.assertEqual(len(self.test_case), 0)
		self.assertNotIn(self.test_case.Diamond,	self.test_case)
		self.assertNotIn(self.test_case.Ruby,		self.test_case)
		self.assertNotIn(self.test_case.Jade,		self.test_case)
		self.assertNotIn(self.test_case.Sapphire,	self.test_case)
		self.assertNotIn(self.test_case.Gold,		self.test_case)
		self.assertNotIn(self.test_case.Silver,		self.test_case)
		self.assertNotIn(self.test_case.Boot,		self.test_case)
		self.assertEqual(self.test_case[self.test_case.Diamond],	None)
		self.assertEqual(self.test_case[self.test_case.Ruby],		None)
		self.assertEqual(self.test_case[self.test_case.Jade],		None)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	None)
		self.assertEqual(self.test_case[self.test_case.Gold],		None)
		self.assertEqual(self.test_case[self.test_case.Silver],		None)

		self.test_case(self.test_case.Diamond,	self.test_case.Diamond.weight)
		self.test_case(self.test_case.Ruby,		self.test_case.Ruby.weight)
		self.test_case(self.test_case.Jade,		self.test_case.Jade.weight)
		self.test_case(self.test_case.Sapphire,	self.test_case.Sapphire.weight)
		self.test_case(self.test_case.Gold,		self.test_case.Gold.weight)
		self.test_case(self.test_case.Silver,	self.test_case.Silver.weight)
		self.assertEqual(len(self.test_case), 6)
		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)




	def test_packed_keysof(self):

		self.assertEqual(

			self.test_case.keysof(self.test_case.Diamond.weight),
			[ self.test_case.Diamond, self.test_case.Ruby ]
		)
		self.assertEqual(

			self.test_case.keysof(self.test_case.Ruby.weight),
			[ self.test_case.Diamond, self.test_case.Ruby ]
		)
		self.assertEqual(self.test_case.keysof(self.test_case.Jade.weight),		[ self.test_case.Jade ])
		self.assertEqual(self.test_case.keysof(self.test_case.Sapphire.weight),	[ self.test_case.Sapphire ])
		self.assertEqual(self.test_case.keysof(self.test_case.Gold.weight),		[ self.test_case.Gold ])
		self.assertEqual(self.test_case.keysof(self.test_case.Silver.weight),	[ self.test_case.Silver ])
		self.assertEqual(self.test_case.keysof(self.test_case.Boot.weight),		[])


		# Broken "_locker_" case
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		self.assertEqual(self.test_case.keysof(self.test_case.Diamond.weight),	[])
		self.assertEqual(self.test_case.keysof(self.test_case.Ruby.weight),		[])
		self.assertEqual(self.test_case.keysof(self.test_case.Jade.weight),		[])
		self.assertEqual(self.test_case.keysof(self.test_case.Sapphire.weight),	[])
		self.assertEqual(self.test_case.keysof(self.test_case.Gold.weight),		[])
		self.assertEqual(self.test_case.keysof(self.test_case.Silver.weight),	[])
		self.assertEqual(self.test_case.keysof(self.test_case.Boot.weight),		[])
		self.test_case._locker_ = locker[:]




	def test_packed_eq_Chest(self):

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertEqual(len(self.test_case), len(self.not_same_case))

		self.assertNotEqual(
			self.test_case[self.test_case.Diamond],		self.not_same_case[self.not_same_case.Diamond]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Ruby],		self.not_same_case[self.not_same_case.Ruby]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Jade],		self.not_same_case[self.not_same_case.Jade]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Sapphire],	self.not_same_case[self.not_same_case.Sapphire]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Gold],		self.not_same_case[self.not_same_case.Gold]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Silver],		self.not_same_case[self.not_same_case.Silver]
		)

		self.assertEqual(self.test_case, self.same_case)
		self.assertEqual(len(self.test_case), len(self.same_case))

		self.assertEqual(
			self.test_case[self.test_case.Diamond],		self.same_case[self.test_case.Diamond]
		)
		self.assertEqual(
			self.test_case[self.test_case.Ruby],		self.same_case[self.test_case.Ruby]
		)
		self.assertEqual(
			self.test_case[self.test_case.Jade],		self.same_case[self.test_case.Jade]
		)
		self.assertEqual(
			self.test_case[self.test_case.Sapphire],	self.same_case[self.test_case.Sapphire]
		)
		self.assertEqual(
			self.test_case[self.test_case.Gold],		self.same_case[self.test_case.Gold]
		)
		self.assertEqual(
			self.test_case[self.test_case.Silver],		self.same_case[self.test_case.Silver]
		)




	def test_packed_gt_ge_lt_le_Chest(self):

		self.assertEqual(self.test_case[self.test_case.Diamond],	self.test_case.Diamond.weight)
		self.assertEqual(self.test_case[self.test_case.Ruby],		self.test_case.Ruby.weight)
		self.assertEqual(self.test_case[self.test_case.Jade],		self.test_case.Jade.weight)
		self.assertEqual(self.test_case[self.test_case.Sapphire],	self.test_case.Sapphire.weight)
		self.assertEqual(self.test_case[self.test_case.Gold],		self.test_case.Gold.weight)
		self.assertEqual(self.test_case[self.test_case.Silver],		self.test_case.Silver.weight)
		del self.not_same_case[self.not_same_case.Diamond]

		self.assertNotEqual(self.test_case, self.not_same_case)
		self.assertNotEqual(len(self.test_case), len(self.not_same_case))
		self.assertGreater(self.test_case, self.not_same_case)
		self.assertGreaterEqual(self.test_case, self.not_same_case)
		self.assertLess(self.not_same_case, self.test_case)
		self.assertLessEqual(self.not_same_case, self.test_case)

		self.not_same_case.unload()
		self.not_same_case(self.not_same_case.Diamond,	self.not_same_case.Diamond.weight)
		self.not_same_case(self.not_same_case.Ruby,		self.not_same_case.Ruby.weight)
		self.not_same_case(self.not_same_case.Jade,		self.not_same_case.Jade.weight)
		self.not_same_case(self.not_same_case.Sapphire,	self.not_same_case.Sapphire.weight)
		self.not_same_case(self.not_same_case.Gold,		self.not_same_case.Gold.weight)
		self.not_same_case(self.not_same_case.Silver,	self.not_same_case.Silver.weight)

		self.assertEqual(self.not_same_case[self.not_same_case.Diamond],	self.not_same_case.Diamond.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Ruby],		self.not_same_case.Ruby.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Jade],		self.not_same_case.Jade.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Sapphire],	self.not_same_case.Sapphire.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Gold],		self.not_same_case.Gold.weight)
		self.assertEqual(self.not_same_case[self.not_same_case.Silver],		self.not_same_case.Silver.weight)




	def test_packed_eq_dict(self):

		self.assertNotEqual(self.test_case, self.not_same_asdict)
		self.assertEqual(len(self.test_case), len(self.not_same_asdict))

		self.assertNotEqual(
			self.test_case[self.test_case.Diamond],		self.not_same_asdict[self.not_same_case.Diamond]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Ruby],		self.not_same_asdict[self.not_same_case.Ruby]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Jade],		self.not_same_asdict[self.not_same_case.Jade]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Sapphire],	self.not_same_asdict[self.not_same_case.Sapphire]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Gold],		self.not_same_asdict[self.not_same_case.Gold]
		)
		self.assertNotEqual(
			self.test_case[self.test_case.Silver],		self.not_same_asdict[self.not_same_case.Silver]
		)


		self.assertEqual(self.test_case, self.same_asdict)
		self.assertEqual(len(self.test_case), len(self.same_asdict))

		self.assertEqual(
			self.test_case[self.test_case.Diamond],		self.same_asdict[self.test_case.Diamond]
		)
		self.assertEqual(
			self.test_case[self.test_case.Ruby],		self.same_asdict[self.test_case.Ruby]
		)
		self.assertEqual(
			self.test_case[self.test_case.Jade],		self.same_asdict[self.test_case.Jade]
		)
		self.assertEqual(
			self.test_case[self.test_case.Sapphire],	self.same_asdict[self.test_case.Sapphire]
		)
		self.assertEqual(
			self.test_case[self.test_case.Gold],		self.same_asdict[self.test_case.Gold]
		)
		self.assertEqual(
			self.test_case[self.test_case.Silver],		self.same_asdict[self.test_case.Silver]
		)




	def test_packed_gt_ge_lt_le_list(self):

		self.assertEqual(self.not_same_asdict[self.not_same_case.Diamond],	self.not_same_case.Diamond.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Ruby],		self.not_same_case.Ruby.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Jade],		self.not_same_case.Jade.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Sapphire],	self.not_same_case.Sapphire.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Gold],		self.not_same_case.Gold.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Silver],	self.not_same_case.Silver.weight)
		del self.not_same_asdict[self.not_same_case.Diamond]

		self.assertNotEqual(self.test_case, self.not_same_asdict)
		self.assertNotEqual(len(self.test_case), len(self.not_same_asdict))
		self.assertGreater(self.test_case, self.not_same_asdict)
		self.assertGreaterEqual(self.test_case, self.not_same_asdict)
		self.assertLess(self.not_same_asdict, self.test_case)
		self.assertLessEqual(self.not_same_asdict, self.test_case)

		del self.not_same_asdict[self.not_same_case.Ruby]
		del self.not_same_asdict[self.not_same_case.Jade]
		del self.not_same_asdict[self.not_same_case.Sapphire]
		del self.not_same_asdict[self.not_same_case.Gold]
		del self.not_same_asdict[self.not_same_case.Silver]
		self.assertFalse(self.not_same_asdict)
		self.not_same_asdict[self.not_same_case.Diamond]	=	self.not_same_case.Diamond.weight
		self.not_same_asdict[self.not_same_case.Ruby]		=	self.not_same_case.Ruby.weight
		self.not_same_asdict[self.not_same_case.Jade]		=	self.not_same_case.Jade.weight
		self.not_same_asdict[self.not_same_case.Sapphire]	=	self.not_same_case.Sapphire.weight
		self.not_same_asdict[self.not_same_case.Gold]		=	self.not_same_case.Gold.weight
		self.not_same_asdict[self.not_same_case.Silver]		=	self.not_same_case.Silver.weight

		self.assertEqual(self.not_same_asdict[self.not_same_case.Diamond],	self.not_same_case.Diamond.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Ruby],		self.not_same_case.Ruby.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Jade],		self.not_same_case.Jade.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Sapphire],	self.not_same_case.Sapphire.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Gold],		self.not_same_case.Gold.weight)
		self.assertEqual(self.not_same_asdict[self.not_same_case.Silver],	self.not_same_case.Silver.weight)




	def test_packed_iter(self):

		count = 0
		for K,V in self.test_case:

			self.assertEqual(K.weight, V)
			self.assertIsInstance(K(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))
		count = 0
		_case = iter(self.test_case)
		for one,two in zip(_case, _case):

			Kone,Vone = one
			self.assertEqual(Kone.weight, Vone)
			self.assertIsInstance(Kone(), str)
			count += 1
			Ktwo,Vtwo = two
			self.assertEqual(Ktwo.weight, Vtwo)
			self.assertIsInstance(Ktwo(), str)
			count += 1

		self.assertEqual(count, len(self.test_case))


		# Breaking iteration by messing with "_locker_":
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		count = 0
		for K,V in self.test_case:

			self.assertEqual(K.weight, V)
			self.assertIsInstance(K(), str)
			count += 1

		self.assertEqual(count, 0)
		self.assertEqual(len(self.test_case), 6)
		self.assertNotEqual(count, len(self.test_case))
		self.test_case._locker_ = locker[:]




	def test_packed_next(self):

		count = 0
		for _ in range(3 *len(self.test_case)):

			try:

				K,V = next(self.test_case)
				self.assertEqual(K.weight, V)
				self.assertIsInstance(K(), str)
				count += 1

			except	StopIteration:

				self.assertEqual(count, len(self.test_case))
				count = 0


		# Breaking "_locker_" and __next__ always raises StopIteration
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = []
		count = 0
		for _ in range(3):

			try:

				next(self.test_case)
				count += 1

			except	StopIteration : self.assertEqual(count,0)

		self.assertEqual(count,0)
		self.test_case._locker_ = locker[:]




	def test_packed_reversed(self):

		# Direct
		self.assertEqual(
			[ V for K,V in self.test_case ],
			[
				self.test_case.Diamond.weight,
				self.test_case.Ruby.weight,
				self.test_case.Jade.weight,
				self.test_case.Sapphire.weight,
				self.test_case.Gold.weight,
				self.test_case.Silver.weight
			]
		)

		# Reversed
		self.assertEqual(
			[ V for K,V in reversed(self.test_case) ],
			[
				self.test_case.Silver.weight,
				self.test_case.Gold.weight,
				self.test_case.Sapphire.weight,
				self.test_case.Jade.weight,
				self.test_case.Ruby.weight,
				self.test_case.Diamond.weight
			]
		)

		# Broken "_locker_" that already reversed
		locker = self.test_case._locker_[:]
		self.test_case._locker_ = list(reversed(self.test_case._locker_))
		self.assertEqual(
			[ V for K,V in reversed(self.test_case) ],
			[
				self.test_case.Diamond.weight,
				self.test_case.Ruby.weight,
				self.test_case.Jade.weight,
				self.test_case.Sapphire.weight,
				self.test_case.Gold.weight,
				self.test_case.Silver.weight
			]
		)

		# Broken "_locker_" that is empty
		self.test_case._locker_ = []
		self.assertEqual([ V for K,V in self.test_case ], [])
		self.test_case._locker_ = locker[:]




	def test_packed_noload_call(self):

		test_case = self.test_case()
		self.assertIsInstance(test_case, dict)
		self.assertEqual(test_case, self.test_case())
		self.assertNotEqual(id(test_case), id(self.test_case))

		self.assertEqual(self.test_case[self.test_case.Diamond],	test_case[str(self.test_case.Diamond)])
		self.assertEqual(self.test_case[self.test_case.Ruby],		test_case[str(self.test_case.Ruby)])
		self.assertEqual(self.test_case[self.test_case.Jade],		test_case[str(self.test_case.Jade)])
		self.assertEqual(self.test_case[self.test_case.Sapphire],	test_case[str(self.test_case.Sapphire)])
		self.assertEqual(self.test_case[self.test_case.Gold],		test_case[str(self.test_case.Gold)])
		self.assertEqual(self.test_case[self.test_case.Silver],		test_case[str(self.test_case.Silver)])
















class DeepChest(MagicalTestCase):

	"""
		Testing deep method.
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.DEEP_KEY_SET_HANDLER): os.remove(cls.DEEP_KEY_SET_HANDLER)

	@classmethod
	def setUpClass(cls):
		class Digituts(KeyChest):

			class loggy(LibraryContrib):

				init_name	= "deep"
				init_level	= 10
				handler		= cls.DEEP_KEY_SET_HANDLER


		cls.make_loggy_file(cls, cls.DEEP_KEY_SET_HANDLER)
		cls.test_case = Digituts()
		cls.test_case(10, "the ten", *range(10), mapped=False)


	def test_consistency(self):

		self.assertEqual(len(self.test_case),1)

		self.assertIn(0, self.test_case)
		self.assertIsInstance(self.test_case[0], dict)

		self.assertIn(1, self.test_case[0])
		self.assertIsInstance(self.test_case[0][1], dict)

		self.assertIn(2, self.test_case[0][1])
		self.assertIsInstance(self.test_case[0][1][2], dict)

		self.assertIn(3, self.test_case[0][1][2])
		self.assertIsInstance(self.test_case[0][1][2][3], dict)

		self.assertIn(4, self.test_case[0][1][2][3])
		self.assertIsInstance(self.test_case[0][1][2][3][4], dict)

		self.assertIn(5, self.test_case[0][1][2][3][4])
		self.assertIsInstance(self.test_case[0][1][2][3][4][5], dict)

		self.assertIn(6, self.test_case[0][1][2][3][4][5])
		self.assertIsInstance(self.test_case[0][1][2][3][4][5][6], dict)

		self.assertIn(7, self.test_case[0][1][2][3][4][5][6])
		self.assertIsInstance(self.test_case[0][1][2][3][4][5][6][7], dict)

		self.assertIn(8, self.test_case[0][1][2][3][4][5][6][7])
		self.assertIsInstance(self.test_case[0][1][2][3][4][5][6][7][8], dict)

		self.assertIn(9, self.test_case[0][1][2][3][4][5][6][7][8])
		self.assertIsInstance(self.test_case[0][1][2][3][4][5][6][7][8][9], dict)

		self.assertIn(10, self.test_case[0][1][2][3][4][5][6][7][8][9])
		self.assertIsInstance(self.test_case[0][1][2][3][4][5][6][7][8][9][10], str)
		self.assertEqual(self.test_case[0][1][2][3][4][5][6][7][8][9][10], "the ten")


	def test_deep_1(self):

		for i in range(2,10):	self.assertIsInstance(self.test_case.deep(*range(i)), dict)


	def test_deep_2(self):

		self.assertEqual(self.test_case.deep(*range(1)), self.test_case[0])
		self.assertEqual(self.test_case.deep(*range(2)), self.test_case[0][1])
		self.assertEqual(self.test_case.deep(*range(3)), self.test_case[0][1][2])
		self.assertEqual(self.test_case.deep(*range(4)), self.test_case[0][1][2][3])
		self.assertEqual(self.test_case.deep(*range(5)), self.test_case[0][1][2][3][4])
		self.assertEqual(self.test_case.deep(*range(6)), self.test_case[0][1][2][3][4][5])
		self.assertEqual(self.test_case.deep(*range(7)), self.test_case[0][1][2][3][4][5][6])
		self.assertEqual(self.test_case.deep(*range(8)), self.test_case[0][1][2][3][4][5][6][7])
		self.assertEqual(self.test_case.deep(*range(9)), self.test_case[0][1][2][3][4][5][6][7][8])
		self.assertEqual(self.test_case.deep(*range(10)), self.test_case[0][1][2][3][4][5][6][7][8][9])
		self.assertEqual(self.test_case.deep(*range(11)), "the ten")


	def test_deep_3(self):

		self.assertIsNone(self.test_case.deep(*range(1), 42))
		self.assertIsNone(self.test_case.deep(*range(2), 42))
		self.assertIsNone(self.test_case.deep(*range(3), 42))
		self.assertIsNone(self.test_case.deep(*range(4), 42))
		self.assertIsNone(self.test_case.deep(*range(5), 42))
		self.assertIsNone(self.test_case.deep(*range(6), 42))
		self.assertIsNone(self.test_case.deep(*range(7), 42))
		self.assertIsNone(self.test_case.deep(*range(8), 42))
		self.assertIsNone(self.test_case.deep(*range(9), 42))
		self.assertIsNone(self.test_case.deep(*range(10), 42))


	def test_deep_4(self):

		for j in range(10, 1, -1):
			with self.assertLogs("deep", 10) as case_loggy:

				self.assertIsNone(self.test_case.deep(j))
				self.assertIn(f"DEBUG:deep:Root-key \"{j}\" not found", case_loggy.output)
				self.assertIsNone(self.test_case.deep(*range(1,j)))
				self.assertIn(f"DEBUG:deep:Root-key \"1\" not found", case_loggy.output)


	def test_deep_5(self):

		with self.assertLogs("deep", 10) as case_loggy:

			self.assertIsNone(self.test_case.deep())
			self.assertIn(f"DEBUG:deep:No depth to go deep", case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







