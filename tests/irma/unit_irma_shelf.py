import	os
import	unittest
from	pygwarts.irma.shelve	import LibraryShelf
from	pygwarts.irma.contrib	import LibraryContrib
from	pygwarts.tests.irma		import IrmaTestCase








class ItemsTest(IrmaTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ITEMS_HANDLER): os.remove(cls.ITEMS_HANDLER)

	@classmethod
	def setUpClass(cls):
		class ItemsTestCase(LibraryShelf):
			class loggy(LibraryContrib):

				init_name	= "ItemsTest"
				init_level	= 10
				handler		= cls.ITEMS_HANDLER

		cls.make_loggy_file(cls, cls.ITEMS_HANDLER)
		cls.test_case = ItemsTestCase()

	def setUp(self) : self.test_case.unload(magical=True)
	def test_is_mapping_check(self):

		self.assertTrue(hasattr(self.test_case, "keys"))
		self.assertTrue(hasattr(self.test_case, "__getitem__"))




	def test_real_setitem(self):

		for N,item in enumerate(( "LOL", 1, .1, 0, ( "LOL", ), None ),1):
			with self.subTest(item=item, N=N):

				self.test_case[item] = "KEK"
				self.assertEqual(len(self.test_case.real_shelf), N)
				self.assertEqual(len(self.test_case.magical_shelf), N)
				self.assertEqual(len(self.test_case.real_shelf._locker_), N)
				self.assertEqual(len(self.test_case.magical_shelf._locker_), N)
				self.assertEqual(self.test_case.diff,0)
				self.assertTrue(self.test_case.modified)


		self.assertEqual(self.test_case.keys(), [ "LOL", 1, .1, 0, ( "LOL", ), None ])
		self.assertEqual(self.test_case.keysof("KEK"), [ "LOL", 1, .1, 0, ( "LOL", ), None ])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [])




	def test_real_invalid_setitem(self):

		for item in [ "LOL","KEK" ], { "LOL": "KEK" }, { "LOL","KEK" }:
			with self.subTest(item=item):

				self.test_case[item] = "CHEBUREK"
				self.assertEqual(len(self.test_case.real_shelf), 0)
				self.assertEqual(len(self.test_case.magical_shelf), 0)
				self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
				self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
				self.assertEqual(self.test_case.diff,0)
				self.assertFalse(self.test_case.modified)


		self.assertEqual(self.test_case.keys(), [])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [])




	def test_real_setitem_edge_case(self):

		self.test_case[None] = None
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ None ])
		self.assertEqual(self.test_case.keysof(None), [ None ])


		# Imitation of situation, when Shelf is grabbed and modified
		self.test_case.modified = False
		self.test_case[None] = None
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ None ])
		self.assertEqual(self.test_case.keysof(None), [ None ])


		self.test_case.modified = False
		self.test_case[None] = "LOL-KEK-CHEBUREK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ None ])
		self.assertEqual(self.test_case.keysof("LOL-KEK-CHEBUREK"), [ None ])




	def test_real_replace_item(self):

		self.test_case["LOL"] = "KEK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ "LOL" ])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [])
		self.assertEqual(self.test_case.keysof("KEK"), [ "LOL" ])


		# Imitation of situation, when Shelf is grabbed and modified
		self.test_case.modified = False
		self.assertFalse(self.test_case.modified)
		self.test_case["LOL"] = "CHEBUREK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ "LOL" ])
		self.assertEqual(self.test_case.keysof("KEK"), [])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [ "LOL" ])


		self.test_case.modified = False
		self.assertFalse(self.test_case.modified)
		self.test_case["LOL"] = "CHEBUREK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ "LOL" ])
		self.assertEqual(self.test_case.keysof("KEK"), [])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [ "LOL" ])




	def test_real_getitem(self):

		self.test_case["LOL"] = "KEK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)


		self.assertEqual(self.test_case["LOL"], "KEK")
		self.assertEqual(self.test_case["KEK"], None)
		self.assertNotEqual(self.test_case["LOL"], "CHEBUREK")
		self.assertNotEqual(self.test_case["KEK"], "LOL")


		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)




	def test_real_contains_item(self):

		self.test_case["LOL"] = "KEK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)


		self.assertTrue("LOL" in self.test_case)
		self.assertFalse("KEK" in self.test_case)
		self.assertFalse([ "KEK" ] in self.test_case)




	def test_real_delitem(self):

		self.test_case["LOL"] = "KEK"
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.keys(), [ "LOL" ])
		self.assertEqual(self.test_case.keysof("KEK"), [ "LOL" ])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [])


		with self.assertLogs("ItemsTest", 10) as case_loggy:

			del self.test_case["LOL"]
			self.assertEqual(len(self.test_case.real_shelf), 0)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,0)
			del self.test_case["KEK"]
			del self.test_case[["KEK"]]


		self.assertEqual(self.test_case.keys(), [])
		self.assertEqual(self.test_case.keysof("KEK"), [])
		self.assertEqual(self.test_case.keysof("CHEBUREK"), [])
		self.assertIn("DEBUG:ItemsTest:Removed \"LOL\", \"KEK\" pair", case_loggy.output)
		self.assertIn(

			f"DEBUG:ItemsTest:Key \"KEK\" not in {self.test_case.real_shelf} KeyChest",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:ItemsTest:Key \"KEK\" not in {self.test_case.magical_shelf} KeyChest",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:ItemsTest:Impossible key \"[\'KEK\']\" for {self.test_case.real_shelf} KeyChest",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:ItemsTest:Impossible key \"[\'KEK\']\" for {self.test_case.magical_shelf} KeyChest",
			case_loggy.output
		)








	def test_magical_setitem(self):

		for N,item in enumerate(( "LOL", 1, .1, 0, ( "LOL", ), None ),1):
			with self.subTest(item=item, N=N):

				self.test_case(item, "KEK")
				self.assertEqual(len(self.test_case.real_shelf), 0)
				self.assertEqual(len(self.test_case.magical_shelf), N)
				self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
				self.assertEqual(len(self.test_case.magical_shelf._locker_), N)
				self.assertEqual(self.test_case.diff,-N)
				self.assertTrue(self.test_case.modified)


		self.assertEqual(self.test_case().keys(), [ "LOL", 1, .1, 0, ( "LOL", ), None ])
		self.assertEqual(self.test_case().keysof("KEK"), [ "LOL", 1, .1, 0, ( "LOL", ), None ])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [])




	def test_magical_invalid_setitem(self):

		for item in [ "LOL","KEK" ], { "LOL": "KEK" }, { "LOL","KEK" }:
			with self.subTest(item=item):

				self.test_case(item, "CHEBUREK")
				self.assertEqual(len(self.test_case.real_shelf), 0)
				self.assertEqual(len(self.test_case.magical_shelf), 0)
				self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
				self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
				self.assertEqual(self.test_case.diff,0)
				self.assertFalse(self.test_case.modified)


		self.assertEqual(self.test_case().keys(), [])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [])




	def test_magical_setitem_edge_case(self):

		self.test_case(None,None)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ None ])
		self.assertEqual(self.test_case().keysof(None), [ None ])


		# Imitation of situation, when Shelf is grabbed and modified
		self.test_case.modified = False
		self.test_case(None,None)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ None ])
		self.assertEqual(self.test_case().keysof(None), [ None ])


		self.test_case.modified = False
		self.test_case(None,"LOL-KEK-CHEBUREK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ None ])
		self.assertEqual(self.test_case().keysof("LOL-KEK-CHEBUREK"), [ None ])




	def test_magical_replace_item(self):

		self.test_case("LOL","KEK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ "LOL" ])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [])
		self.assertEqual(self.test_case().keysof("KEK"), [ "LOL" ])


		# Imitation of situation, when Shelf is grabbed and modified
		self.test_case.modified = False
		self.assertFalse(self.test_case.modified)
		self.test_case("LOL","CHEBUREK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ "LOL" ])
		self.assertEqual(self.test_case().keysof("KEK"), [])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [ "LOL" ])


		self.test_case.modified = False
		self.assertFalse(self.test_case.modified)
		self.test_case("LOL", "CHEBUREK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ "LOL" ])
		self.assertEqual(self.test_case().keysof("KEK"), [])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [ "LOL" ])




	def test_magical_getitem(self):

		self.test_case("LOL","KEK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)

		with self.assertNoLogs("ItemsTest", 30) as tcloggy1:
			self.assertEqual(self.test_case("LOL"), "KEK")

		with self.assertNoLogs("ItemsTest", 30) as tcloggy2:
			self.assertEqual(self.test_case("KEK"), None)

		with self.assertNoLogs("ItemsTest", 30) as tcloggy3:
			self.assertNotEqual(self.test_case("LOL"), "CHEBUREK")

		with self.assertNoLogs("ItemsTest", 30) as tcloggy4:
			self.assertNotEqual(self.test_case("KEK"), "LOL")


		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)




	def test_magical_contains_item(self):

		self.test_case("LOL","KEK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)

		self.assertTrue("LOL" in self.test_case())
		self.assertFalse("KEK" in self.test_case())
		self.assertFalse([ "KEK" ] in self.test_case())




	def test_magical_delitem(self):

		self.test_case("LOL","KEK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case().keys(), [ "LOL" ])
		self.assertEqual(self.test_case().keysof("KEK"), [ "LOL" ])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [])

		with self.assertLogs("ItemsTest", 10) as case_loggy:

			del self.test_case()["LOL"]
			self.assertEqual(len(self.test_case.real_shelf), 0)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,0)
			del self.test_case()["KEK"]
			del self.test_case()[["KEK"]]


		self.assertEqual(self.test_case().keys(), [])
		self.assertEqual(self.test_case().keysof("KEK"), [])
		self.assertEqual(self.test_case().keysof("CHEBUREK"), [])
		self.assertIn("DEBUG:ItemsTest:Removed \"LOL\", \"KEK\" pair", case_loggy.output)
		self.assertIn(

			f"DEBUG:ItemsTest:Key \"KEK\" not in {self.test_case.magical_shelf} KeyChest",
			case_loggy.output
		)
		self.assertIn(

			f"WARNING:ItemsTest:Impossible key \"[\'KEK\']\" for {self.test_case.magical_shelf} KeyChest",
			case_loggy.output
		)








	def test_magical_setitem_silent(self):

		for N,item in enumerate(( "LOL", 1, .1, 0, ( "LOL", )),1):
			with self.subTest(item=item, N=N):

				self.test_case(item, "KEK", silent=True)
				self.assertEqual(len(self.test_case.real_shelf), 0)
				self.assertEqual(len(self.test_case.magical_shelf), N)
				self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
				self.assertEqual(len(self.test_case.magical_shelf._locker_), N)
				self.assertEqual(self.test_case.diff,-N)
				self.assertFalse(self.test_case.modified)




	def test_magical_invalid_setitem_silent(self):

		for item in [ "LOL","KEK" ], { "LOL": "KEK" }, { "LOL","KEK" }:
			with self.subTest(item=item):

				self.test_case(item, "CHEBUREK", silent=True)
				self.assertEqual(len(self.test_case.real_shelf), 0)
				self.assertEqual(len(self.test_case.magical_shelf), 0)
				self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
				self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
				self.assertEqual(self.test_case.diff,0)
				self.assertFalse(self.test_case.modified)




	def test_magical_setitem_edge_case_silent(self):

		self.test_case(None,None, silent=True)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)

		self.test_case(None,None, silent=True)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)

		self.test_case(None,"LOL-KEK-CHEBUREK", silent=True)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)




	def test_magical_replace_item_silent(self):

		self.test_case("LOL","KEK", silent=True)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)

		self.test_case("LOL","CHEBUREK", silent=True)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)

		self.test_case("LOL", "CHEBUREK", silent=True)
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertEqual(self.test_case.diff,-1)
		self.assertFalse(self.test_case.modified)








	def test_real_diff_larger(self):

		self.test_case["LOL"] = "KEK"
		self.test_case.real_shelf("CHE", "BUREK")
		self.assertEqual(len(self.test_case.real_shelf), 2)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.diff, 1)
		self.assertEqual(self.test_case.real_diff,{ "CHE" })
		self.assertEqual(self.test_case.magical_diff, set())




	def test_magical_diff_larger(self):

		self.test_case["LOL"] = "KEK"
		self.test_case.magical_shelf("CHE", "BUREK")
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 2)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 2)
		self.assertTrue(self.test_case.modified)
		self.assertEqual(self.test_case.diff, -1)
		self.assertEqual(self.test_case.magical_diff,{ "CHE" })
		self.assertEqual(self.test_case.real_diff, set())




	def test_empties_diff(self):

		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case.diff, 0)
		self.assertEqual(self.test_case.real_diff, set())
		self.assertEqual(self.test_case.magical_diff, set())




	def test_empty_real_diff(self):

		self.test_case.real_shelf("LOL", "KEK")
		self.assertEqual(len(self.test_case.real_shelf), 1)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 1)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case.diff, 1)
		self.assertEqual(self.test_case.real_diff, { "LOL" })
		self.assertEqual(self.test_case.magical_diff, set())




	def test_empty_magical_diff(self):

		self.test_case.magical_shelf("LOL", "KEK")
		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 1)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 1)
		self.assertFalse(self.test_case.modified)
		self.assertEqual(self.test_case.diff, -1)
		self.assertEqual(self.test_case.magical_diff, { "LOL" })
		self.assertEqual(self.test_case.real_diff, set())
















class GrabbingTest(IrmaTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:

			if	os.path.isfile(cls.GRABBING_IN_INIT):			os.remove(cls.GRABBING_IN_INIT)
			if	os.path.isfile(cls.GRABBING_HANDLER):			os.remove(cls.GRABBING_HANDLER)

			if	os.path.isfile(cls.GRABBING_LOCKER):			os.remove(cls.GRABBING_LOCKER)
			if	os.path.isfile(cls.GRABBING_NO_LOCKER):			os.remove(cls.GRABBING_NO_LOCKER)

			if	os.path.isfile(cls.GRABBING_LOCKER + ".db"):	os.remove(cls.GRABBING_LOCKER + ".db")
			if	os.path.isfile(cls.GRABBING_NO_LOCKER + ".db"):	os.remove(cls.GRABBING_NO_LOCKER + ".db")

			if	os.path.isfile(cls.GRABBING_LOCKER + ".dat"):	os.remove(cls.GRABBING_LOCKER + ".dat")
			if	os.path.isfile(cls.GRABBING_LOCKER + ".bak"):	os.remove(cls.GRABBING_LOCKER + ".bak")
			if	os.path.isfile(cls.GRABBING_LOCKER + ".dir"):	os.remove(cls.GRABBING_LOCKER + ".dir")

			if	os.path.isfile(cls.GRABBING_NO_LOCKER + ".dat"):
				os.remove(cls.GRABBING_NO_LOCKER + ".dat")

			if	os.path.isfile(cls.GRABBING_NO_LOCKER + ".bak"):
				os.remove(cls.GRABBING_NO_LOCKER + ".bak")

			if	os.path.isfile(cls.GRABBING_NO_LOCKER + ".dir"):
				os.remove(cls.GRABBING_NO_LOCKER + ".dir")


	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.GRABBING_HANDLER)

		class Preparation(LibraryShelf):	pass

		preparation = Preparation()
		preparation["OOH"] = "EEH"
		preparation["OOH"] = "AAH-AAH"
		preparation["DING"] = "DANG"
		preparation["WOLO-WOLO"] = "BANG-BANG"
		preparation.produce(cls.GRABBING_NO_LOCKER, rewrite=True)
		preparation.produce(cls.GRABBING_LOCKER, rewrite=True, locker_mode=True)


		class GrabbingTestCase(LibraryShelf):
			class loggy(LibraryContrib):

				init_name	= "GrabbingTest"
				init_level	= 10
				handler		= cls.GRABBING_HANDLER

		cls.test_case = GrabbingTestCase()

	def setUp(self):	self.test_case.unload(magical=True)
	def test_grabbing_no_argument(self):

		with self.assertLogs("GrabbingTest", 10) as case_loggy:	self.test_case.grab()
		self.assertIn("DEBUG:GrabbingTest:Shelf to grab not provided", case_loggy.output)


		self.assertTrue(

			os.path.isfile(self.GRABBING_LOCKER)
			or
			os.path.isfile(self.GRABBING_LOCKER + ".db")
			or
			os.path.isfile(self.GRABBING_LOCKER + ".dat")
		)
		with self.assertLogs("GrabbingTest", 10) as case_loggy:

			self.test_case.grabbing = self.GRABBING_LOCKER
			self.test_case.grab()

		self.assertIn(
			f"DEBUG:GrabbingTest:Shelf \"{self.GRABBING_LOCKER}\" successfully grabbed", case_loggy.output
		)
		self.assertFalse(self.test_case.modified)




	def test_grabbing_invalid_arguments(self):
		self.test_case.grabbing = None

		for grabbable in False,"",[],{},str(),list(),set(),dict(),0,.0 :
			with self.subTest(grabbable=grabbable):

				with self.assertLogs("GrabbingTest", 10) as case_loggy : self.test_case.grab(grabbable)
				self.assertIn(f"DEBUG:GrabbingTest:Shelf to grab not provided", case_loggy.output)




	def test_grabbing_invalid_argument(self):

		for grabbable in (

			True,
			100500,
			420.69,
			unittest,
			...,
			[ "/SomeTest.Shelf" ],
			( "/SomeTest.Shelf", ),
			{ "/SomeTest.Shelf" },
			{ "path": "/SomeTest.Shelf" },
		):
			with self.subTest(grabbable=grabbable):

				with self.assertLogs("GrabbingTest", 10) as case_loggy : self.test_case.grab(grabbable)
				self.assertIn(

					f"WARNING:GrabbingTest:Invalid grabbing path type \"{type(grabbable)}\"",
					case_loggy.output
				)




	def test_grabbing_in_init(self):
		class GrabbingInInnit(LibraryShelf):

			grabbing = self.GRABBING_LOCKER
			class loggy(LibraryContrib):

				init_name	= "GrabbingInInnit"
				init_level	= 10
				handler		= self.GRABBING_IN_INIT


		self.make_loggy_file(self.GRABBING_IN_INIT)
		with self.assertLogs("GrabbingInInnit", 10) as grabbing_loggy:	current_case = GrabbingInInnit()

		self.assertIn("DEBUG:GrabbingInInnit:Obtained locker of length 3", grabbing_loggy.output)
		self.assertIn(

			f"DEBUG:GrabbingInInnit:Shelf \"{self.GRABBING_LOCKER}\" successfully grabbed",
			grabbing_loggy.output
		)
		self.assertEqual(len(current_case.real_shelf), 3)
		self.assertEqual(len(current_case.magical_shelf), 0)
		self.assertEqual(len(current_case.real_shelf._locker_), 3)
		self.assertEqual(len(current_case.magical_shelf._locker_), 0)
		self.assertEqual(current_case.diff,3)
		self.assertFalse(current_case.modified)
		# No "_locker_" in "keys" as it supposed to be
		self.assertEqual(current_case.keys(), [ "OOH", "DING", "WOLO-WOLO" ])
		self.assertEqual(current_case.keysof("EEH"), [])
		self.assertEqual(current_case.keysof("AAH-AAH"), [ "OOH" ])
		self.assertEqual(current_case.keysof("DANG"), [ "DING" ])
		self.assertEqual(current_case.keysof("BANG-BANG"), [ "WOLO-WOLO" ])
		current_case.loggy.handler.close()




	def test_grabbing_with_locker(self):

		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertEqual(self.test_case.diff,0)

		with self.assertLogs("GrabbingTest", 10) as case_loggy:
			self.assertEqual(
				self.test_case.grab(

					self.GRABBING_LOCKER,
					from_locker=True
				),	self.GRABBING_LOCKER
			)

		self.assertIn("DEBUG:GrabbingTest:Obtained locker of length 3", case_loggy.output)
		self.assertIn(
			f"DEBUG:GrabbingTest:Shelf \"{self.GRABBING_LOCKER}\" successfully grabbed", case_loggy.output
		)
		self.assertEqual(self.test_case.real_shelf._locker_, [ "OOH", "DING", "WOLO-WOLO" ])
		self.assertEqual(len(self.test_case.real_shelf), 3)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 3)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertEqual(self.test_case.diff,3)
		# No "_locker_" in "keys" as it supposed to be
		self.assertEqual(self.test_case.keys(), [ "OOH", "DING", "WOLO-WOLO" ])
		self.assertEqual(self.test_case.keysof("EEH"), [])
		self.assertEqual(self.test_case.keysof("AAH-AAH"), [ "OOH" ])
		self.assertEqual(self.test_case.keysof("DANG"), [ "DING" ])
		self.assertEqual(self.test_case.keysof("BANG-BANG"), [ "WOLO-WOLO" ])




	def test_grabbing_with_skipped_locker(self):

		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertEqual(self.test_case.diff,0)

		with self.assertLogs("GrabbingTest", 10) as case_loggy:
			self.assertEqual(
				self.test_case.grab(

					self.GRABBING_LOCKER,
					from_locker=False
				),	self.GRABBING_LOCKER
			)

		self.assertIn("DEBUG:GrabbingTest:Locker skipped, order not granted", case_loggy.output)
		self.assertIn(
			f"DEBUG:GrabbingTest:Shelf \"{self.GRABBING_LOCKER}\" successfully grabbed", case_loggy.output
		)
		self.assertEqual(len(self.test_case.real_shelf), 3)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 3)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertEqual(self.test_case.diff,3)




	def test_grabbing_with_no_locker(self):

		self.assertEqual(len(self.test_case.real_shelf), 0)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertEqual(self.test_case.diff,0)

		with self.assertLogs("GrabbingTest", 10) as case_loggy:
			self.assertEqual(
				self.test_case.grab(

					self.GRABBING_NO_LOCKER,
					from_locker=True
				),	self.GRABBING_NO_LOCKER
			)

		self.assertIn("DEBUG:GrabbingTest:Locker not obtained, order not granted", case_loggy.output)
		self.assertIn(

			f"DEBUG:GrabbingTest:Shelf \"{self.GRABBING_NO_LOCKER}\" successfully grabbed",
			case_loggy.output
		)
		self.assertEqual(len(self.test_case.real_shelf), 3)
		self.assertEqual(len(self.test_case.magical_shelf), 0)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 3)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
		self.assertEqual(self.test_case.diff,3)
















class ProducingTest(IrmaTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:

			if	os.path.isfile(cls.PRODUCING_HANDLER):		os.remove(cls.PRODUCING_HANDLER)
			if	os.path.isfile(cls.PRODUCING_PRODUCABLE):	os.remove(cls.PRODUCING_PRODUCABLE)

			if	os.path.isfile(cls.PRODUCING_PRODUCABLE + ".db"):
				os.remove(cls.PRODUCING_PRODUCABLE + ".db")

			if	os.path.isfile(cls.PRODUCING_PRODUCABLE + ".dat"):
				os.remove(cls.PRODUCING_PRODUCABLE + ".dat")

			if	os.path.isfile(cls.PRODUCING_PRODUCABLE + ".bak"):
				os.remove(cls.PRODUCING_PRODUCABLE + ".bak")

			if	os.path.isfile(cls.PRODUCING_PRODUCABLE + ".dir"):
				os.remove(cls.PRODUCING_PRODUCABLE + ".dir")

	@classmethod
	def setUpClass(cls):

		class ProducingTestCase(LibraryShelf):
			class loggy(LibraryContrib):

				init_name	= "ProducingTest"
				init_level	= 10
				handler		= cls.PRODUCING_HANDLER


		cls.make_loggy_file(cls, cls.PRODUCING_HANDLER)
		cls.test_case	= ProducingTestCase()

	def setUp(self):

		if	os.path.isfile(self.PRODUCING_PRODUCABLE):	os.remove(self.PRODUCING_PRODUCABLE)
		self.test_case.unload(magical=True)
		self.test_case["LOL"] = "KEK"
		self.test_case["CHE"] = "BUREK"


	def test_producing_real(self):

		self.assertEqual(len(self.test_case.real_shelf), 2)
		self.assertEqual(len(self.test_case.magical_shelf), 2)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 2)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)

		with self.assertLogs("ProducingTest", 10) as case_loggy:

			self.test_case.produce(self.PRODUCING_PRODUCABLE, rewrite=True)
			self.test_case.unload(magical=True)

			self.assertEqual(len(self.test_case.real_shelf), 0)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,0)

			self.test_case.grab(self.PRODUCING_PRODUCABLE)
			self.assertEqual(len(self.test_case.real_shelf), 2)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,2)

			self.test_case.produce(self.PRODUCING_PRODUCABLE)

		self.assertIn(

			f"INFO:ProducingTest:Rewritten Shelf \"{self.PRODUCING_PRODUCABLE}\"",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"LOL\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"CHE\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Shelf size 2 keys", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Locker not obtained, order not granted", case_loggy.output)




	def test_producing_real_with_locker(self):

		self.assertEqual(len(self.test_case.real_shelf), 2)
		self.assertEqual(len(self.test_case.magical_shelf), 2)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 2)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)

		with self.assertLogs("ProducingTest", 10) as case_loggy:

			self.test_case.produce(self.PRODUCING_PRODUCABLE, locker_mode=True)
			self.test_case.unload(magical=True)

			self.assertEqual(len(self.test_case.real_shelf), 0)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,0)

			self.test_case.grab(self.PRODUCING_PRODUCABLE)
			self.assertEqual(len(self.test_case.real_shelf), 2)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,2)

			self.test_case.produce(self.PRODUCING_PRODUCABLE)

		self.assertIn(f"DEBUG:ProducingTest:Produced key \"LOL\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"CHE\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Locker of length 2 produced", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Shelf size 3 keys", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Obtained locker of length 2", case_loggy.output)




	def test_producing_magical(self):

		self.assertEqual(len(self.test_case.real_shelf), 2)
		self.assertEqual(len(self.test_case.magical_shelf), 2)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 2)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)

		with self.assertLogs("ProducingTest", 10) as case_loggy:

			self.test_case.produce(self.PRODUCING_PRODUCABLE, rewrite=True, magical=True)
			self.test_case.unload(magical=True)

			self.assertEqual(len(self.test_case.real_shelf), 0)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,0)

			self.test_case.grab(self.PRODUCING_PRODUCABLE)
			self.assertEqual(len(self.test_case.real_shelf), 2)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,2)

			self.test_case.produce(self.PRODUCING_PRODUCABLE)

		self.assertIn(f"DEBUG:ProducingTest:Source is magical Shelf with 2 keys", case_loggy.output)
		self.assertIn(

			f"INFO:ProducingTest:Rewritten Shelf \"{self.PRODUCING_PRODUCABLE}\"",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"LOL\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"CHE\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Shelf size 2 keys", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Locker not obtained, order not granted", case_loggy.output)




	def test_producing_magical_with_locker(self):

		self.assertEqual(len(self.test_case.real_shelf), 2)
		self.assertEqual(len(self.test_case.magical_shelf), 2)
		self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
		self.assertEqual(len(self.test_case.magical_shelf._locker_), 2)
		self.assertEqual(self.test_case.diff,0)
		self.assertTrue(self.test_case.modified)

		with self.assertLogs("ProducingTest", 10) as case_loggy:

			self.test_case.produce(self.PRODUCING_PRODUCABLE, magical=True, locker_mode=True)
			self.test_case.unload(magical=True)

			self.assertEqual(len(self.test_case.real_shelf), 0)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 0)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,0)

			self.test_case.grab(self.PRODUCING_PRODUCABLE)
			self.assertEqual(len(self.test_case.real_shelf), 2)
			self.assertEqual(len(self.test_case.magical_shelf), 0)
			self.assertEqual(len(self.test_case.real_shelf._locker_), 2)
			self.assertEqual(len(self.test_case.magical_shelf._locker_), 0)
			self.assertEqual(self.test_case.diff,2)

			self.test_case.produce(self.PRODUCING_PRODUCABLE)

		self.assertIn(f"DEBUG:ProducingTest:Source is magical Shelf with 2 keys", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"LOL\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Produced key \"CHE\"", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Locker of length 2 produced", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Shelf size 3 keys", case_loggy.output)
		self.assertIn(f"DEBUG:ProducingTest:Obtained locker of length 2", case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







