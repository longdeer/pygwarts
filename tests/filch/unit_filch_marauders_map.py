import	os
import	unittest
from	random							import choice
from	pygwarts.tests.filch			import FilchTestCase
from	pygwarts.irma.contrib			import LibraryContrib
from	pygwarts.filch.marauders_map	import MaraudersMap








class MaraudersMapCases(FilchTestCase):

	"""
		Very simple tests
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.MARAUDERS_HANDLER): os.remove(cls.MARAUDERS_HANDLER)

		if	os.path.isfile(cls.CSV_MAP_1):	os.remove(cls.CSV_MAP_1)
		if	os.path.isfile(cls.CSV_MAP_2):	os.remove(cls.CSV_MAP_2)
		if	os.path.isfile(cls.CSV_MAP_3):	os.remove(cls.CSV_MAP_3)
		if	os.path.isfile(cls.CSV_MAP_4):	os.remove(cls.CSV_MAP_4)
		if	os.path.isfile(cls.CSV_MAP_5):	os.remove(cls.CSV_MAP_5)
		if	os.path.isfile(cls.CSV_MAP_6):	os.remove(cls.CSV_MAP_6)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.MARAUDERS_HANDLER)

		cls.CSV_MAP_1 = str(cls.FILCH_ROOT /"map1.csv")
		cls.CSV_MAP_2 = str(cls.FILCH_ROOT /"map2.csv")
		cls.CSV_MAP_3 = str(cls.FILCH_ROOT /"map3.csv")
		cls.CSV_MAP_4 = str(cls.FILCH_ROOT /"map4.csv")
		cls.CSV_MAP_5 = str(cls.FILCH_ROOT /"map5.csv")
		cls.CSV_MAP_6 = str(cls.FILCH_ROOT /"map6.csv")
		cls.ip0 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip1 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip2 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip3 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip4 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip5 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip6 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip7 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip8 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.ip9 = str(

			f"{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
			f".{choice(cls.valid_IP_chars)}.{choice(cls.valid_IP_chars)}"
		)
		cls.mac0 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac1 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac2 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac3 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac4 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac5 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac6 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac7 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac8 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.mac9 = str(

			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
			"-"
			f"{choice(cls.valid_MAC_chars)}"
			f"{choice(cls.valid_MAC_chars)}"
		)
		cls.lmac0 = cls.mac0.lower()
		cls.lmac1 = cls.mac1.lower()
		cls.lmac2 = cls.mac2.lower()
		cls.lmac3 = cls.mac3.lower()
		cls.lmac4 = cls.mac4.lower()
		cls.lmac5 = cls.mac5.lower()
		cls.lmac6 = cls.mac6.lower()
		cls.lmac7 = cls.mac7.lower()
		cls.lmac8 = cls.mac8.lower()
		cls.lmac9 = cls.mac9.lower()

		cls.name0 = "dev-lls-cata0"
		cls.name1 = "dev-lls-cata1"
		cls.name2 = "dev-lls-cata2"
		cls.name3 = "dev-lls-cata3"
		cls.name4 = "dev-lls-cata4"
		cls.name5 = "dev-lls-cata5"
		cls.name6 = "dev-lls-cata6"
		cls.name7 = "dev-lls-cata7"
		cls.name8 = "dev-lls-cata8"
		cls.name9 = "dev-lls-cata9"

		cls.desc0 = "room 0 switch"
		cls.desc1 = "room 1 switch"
		cls.desc2 = "room 2 switch"
		cls.desc3 = "room 3 switch"
		cls.desc4 = "room 4 switch"
		cls.desc5 = "room 5 switch"
		cls.desc6 = "room 6 switch"
		cls.desc7 = "room 7 switch"
		cls.desc8 = "room 8 switch"
		cls.desc9 = "room 9 switch"

		cls.fmake(

			cls,
			cls.CSV_MAP_1,
			f"{cls.ip0};{cls.mac0};{cls.name0};{cls.desc0}\n"
			f"{cls.ip1};{cls.mac1};{cls.name1};{cls.desc1}\n"
			f"{cls.ip2};{cls.mac2};{cls.name2};{cls.desc2}\n"
			f"{cls.ip3};{cls.mac3};{cls.name3};{cls.desc3}\n"
			f"{cls.ip4};{cls.mac4};{cls.name4};{cls.desc4}\n"
			f"{cls.ip5};{cls.mac5};{cls.name5};{cls.desc5}\n"
			f"{cls.ip6};{cls.mac6};{cls.name6};{cls.desc6}\n"
			f"{cls.ip7};{cls.mac7};{cls.name7};{cls.desc7}\n"
			f"{cls.ip8};{cls.mac8};{cls.name8};{cls.desc8}\n"
			f"{cls.ip9};{cls.mac9};{cls.name9};{cls.desc9}\n"
		)
		cls.fmake(

			cls,
			cls.CSV_MAP_2,
			"mac,name,ip,desc\n"
			f"{cls.mac0},{cls.name0},{cls.ip0},{cls.desc0}\n"
			f"{cls.mac1},{cls.name1},{cls.ip1},{cls.desc1}\n"
			f"{cls.mac2},{cls.name2},{cls.ip2},{cls.desc2}\n"
			f"{cls.mac3},{cls.name3},{cls.ip3},{cls.desc3}\n"
			f"{cls.mac4},{cls.name4},{cls.ip4},{cls.desc4}\n"
			f"{cls.mac5},{cls.name5},{cls.ip5},{cls.desc5}\n"
			f"{cls.mac6},{cls.name6},{cls.ip6},{cls.desc6}\n"
			f"{cls.mac7},{cls.name7},{cls.ip7},{cls.desc7}\n"
			f"{cls.mac8},{cls.name8},{cls.ip8},{cls.desc8}\n"
			f"{cls.mac9},{cls.name9},{cls.ip9},{cls.desc9}\n"
		)
		cls.fmake(

			cls,
			cls.CSV_MAP_3,
			f"{cls.mac0}\t{cls.ip0}\n"
			f"{cls.mac1}\t{cls.ip1}\n"
			f"{cls.mac2}\t{cls.ip2}\n"
			f"{cls.mac3}\t{cls.ip3}\n"
			f"{cls.mac4}\t{cls.ip4}\n"
			f"{cls.mac5}\t{cls.ip5}\n"
			f"{cls.mac6}\t{cls.ip6}\n"
			f"{cls.mac7}\t{cls.ip7}\n"
			f"{cls.mac8}\t{cls.ip8}\n"
			f"{cls.mac9}\t{cls.ip9}\n"
		)
		cls.fmake(

			cls,
			cls.CSV_MAP_4,
			f"{cls.ip0};{cls.mac0};{cls.name0};{cls.desc0}\n"
			f"{cls.ip1};{cls.mac1};{cls.name1};{cls.desc1}\n"
			f"{cls.ip2};{cls.mac2};{cls.name2};{cls.desc2}\n"
		)
		cls.fmake(

			cls,
			cls.CSV_MAP_5,
			"mac,name,ip,desc\n"
			f"{cls.mac3},{cls.name3},{cls.ip3},{cls.desc3}\n"
			f"{cls.mac4},{cls.name4},{cls.ip4},{cls.desc4}\n"
			f"{cls.mac5},{cls.name5},{cls.ip5},{cls.desc5}\n"
			f"{cls.mac6},{cls.name6},{cls.ip6},{cls.desc6}\n"
		)
		cls.fmake(

			cls,
			cls.CSV_MAP_6,
			f"{cls.mac7}\t{cls.ip7}\n"
			f"{cls.mac8}\t{cls.ip8}\n"
			f"{cls.mac9}\t{cls.ip9}\n"
		)


	def test_CSV_1_valid_load(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_1_valid_load",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_1_valid_load", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:CSV_1_valid_load:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_1_valid_load:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_1_valid_load:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_1_valid_load:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_1_valid_load:10 MAC mappings total", case_loggy.output)
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"MAC":	self.mac0.lower(),
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"MAC":	self.mac1.lower(),
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"MAC":	self.mac2.lower(),
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"MAC":	self.mac3.lower(),
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"MAC":	self.mac4.lower(),
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"MAC":	self.mac5.lower(),
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"MAC":	self.mac6.lower(),
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"MAC":	self.mac7.lower(),
				"NAME":	self.name7,
				"DESC":	self.desc7,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"MAC":	self.mac8.lower(),
				"NAME":	self.name8,
				"DESC":	self.desc8,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"MAC":	self.mac9.lower(),
				"NAME":	self.name9,
				"DESC":	self.desc9,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"IP4":	self.ip0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"IP4":	self.ip1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"IP4":	self.ip2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"IP4":	self.ip3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"IP4":	self.ip4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"IP4":	self.ip5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"IP4":	self.ip6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"IP4":	self.ip7,
				"NAME":	self.name7,
				"DESC":	self.desc7,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"IP4":	self.ip8,
				"NAME":	self.name8,
				"DESC":	self.desc8,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"IP4":	self.ip9,
				"NAME":	self.name9,
				"DESC":	self.desc9,
			}
		)




	def test_CSV_2_valid_load(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_2_valid_load",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_2_valid_load", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_2, IP4=2, MAC=0, NAME=1, DESC=3)

		self.assertIn("DEBUG:CSV_2_valid_load:11 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_2_valid_load:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_2_valid_load:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_2_valid_load:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_2_valid_load:10 MAC mappings total", case_loggy.output)
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"MAC":	self.lmac0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"MAC":	self.lmac1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"MAC":	self.lmac2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"MAC":	self.lmac3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"MAC":	self.lmac4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"MAC":	self.lmac5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"MAC":	self.lmac6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"MAC":	self.lmac7,
				"NAME":	self.name7,
				"DESC":	self.desc7,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"MAC":	self.lmac8,
				"NAME":	self.name8,
				"DESC":	self.desc8,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"MAC":	self.lmac9,
				"NAME":	self.name9,
				"DESC":	self.desc9,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"IP4":	self.ip0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"IP4":	self.ip1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"IP4":	self.ip2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"IP4":	self.ip3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"IP4":	self.ip4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"IP4":	self.ip5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"IP4":	self.ip6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"IP4":	self.ip7,
				"NAME":	self.name7,
				"DESC":	self.desc7,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"IP4":	self.ip8,
				"NAME":	self.name8,
				"DESC":	self.desc8,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"IP4":	self.ip9,
				"NAME":	self.name9,
				"DESC":	self.desc9,
			}
		)




	def test_CSV_3_valid_load(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_3_valid_load",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_3_valid_load", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_3, "\t", IP4=1, MAC=0)

		self.assertIn("DEBUG:CSV_3_valid_load:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_3_valid_load:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_3_valid_load:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_3_valid_load:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_3_valid_load:10 MAC mappings total", case_loggy.output)
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"MAC":	self.lmac0,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"MAC":	self.lmac1,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"MAC":	self.lmac2,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"MAC":	self.lmac3,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"MAC":	self.lmac4,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"MAC":	self.lmac5,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"MAC":	self.lmac6,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"MAC":	self.lmac7,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"MAC":	self.lmac8,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"MAC":	self.lmac9,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"IP4":	self.ip0,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"IP4":	self.ip1,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"IP4":	self.ip2,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"IP4":	self.ip3,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"IP4":	self.ip4,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"IP4":	self.ip5,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"IP4":	self.ip6,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"IP4":	self.ip7,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"IP4":	self.ip8,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"IP4":	self.ip9,
				"NAME":	None,
				"DESC":	None,
			}
		)




	def test_CSV_1_invalid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_1_invalid",
				init_level=10,
			)
		)

		with self.assertLogs("CSV_1_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:CSV_1_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_1_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=3, MAC=3, NAME=3, DESC=3)

		self.assertIn("DEBUG:CSV_1_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_1_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=30)

		self.assertIn("DEBUG:CSV_1_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_1_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";")

		self.assertIn("DEBUG:CSV_1_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)




	def test_CSV_2_invalid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_2_invalid",
				init_level=10,
			)
		)

		with self.assertLogs("CSV_2_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_2, "\t", IP4=2, MAC=0, NAME=1, DESC=3)

		self.assertIn("DEBUG:CSV_2_invalid:11 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_2_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_2, IP4=3, MAC=3, NAME=3, DESC=3)

		self.assertIn("DEBUG:CSV_2_invalid:11 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_2_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_2, IP4=30, MAC=30, NAME=30, DESC=30)

		self.assertIn("DEBUG:CSV_2_invalid:11 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_2_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_2)

		self.assertIn("DEBUG:CSV_2_invalid:11 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)




	def test_CSV_3_invalid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_3_invalid",
				init_level=10,
			)
		)

		with self.assertLogs("CSV_3_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_3, IP4=1, MAC=0)

		self.assertIn("DEBUG:CSV_3_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_3_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_3, "\t", IP4=0, MAC=1)

		self.assertIn("DEBUG:CSV_3_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_3_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_3, "\t", IP4=10, MAC=10)

		self.assertIn("DEBUG:CSV_3_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)

		with self.assertLogs("CSV_3_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_3, "\t")

		self.assertIn("DEBUG:CSV_3_invalid:10 records read", case_loggy.output)
		self.assertEqual(len(self.test_case), 0)




	def test_CSV_onload(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_onload",
				init_level=10,
			)
		)

		with self.assertLogs("CSV_onload", 10) as case_loggy:

			self.test_case.CSV(self.CSV_MAP_4, ";", IP4=0, MAC=1, NAME=2, DESC=3)
			self.test_case.CSV(self.CSV_MAP_5, IP4=2, MAC=0, NAME=1, DESC=3)
			self.test_case.CSV(self.CSV_MAP_6, "\t", IP4=1, MAC=0)

		self.assertIn("DEBUG:CSV_onload:3 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:5 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:3 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:3 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:4 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:4 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:3 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:3 MAC mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:7 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:7 MAC mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_onload:10 MAC mappings total", case_loggy.output)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_onload:3 records read"),2)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_onload:3 new IP4 mappings done"),2)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_onload:3 new MAC mappings done"),2)
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"MAC":	self.lmac0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"MAC":	self.lmac1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"MAC":	self.lmac2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"MAC":	self.lmac3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"MAC":	self.lmac4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"MAC":	self.lmac5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"MAC":	self.lmac6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"MAC":	self.lmac7,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"MAC":	self.lmac8,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"MAC":	self.lmac9,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"IP4":	self.ip0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"IP4":	self.ip1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"IP4":	self.ip2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"IP4":	self.ip3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"IP4":	self.ip4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"IP4":	self.ip5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"IP4":	self.ip6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"IP4":	self.ip7,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"IP4":	self.ip8,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"IP4":	self.ip9,
				"NAME":	None,
				"DESC":	None,
			}
		)








	def test_CSV_reload(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_reload",
				init_level=10,
			)
		)

		with self.assertLogs("CSV_reload", 10) as case_loggy:

			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)
			self.test_case.CSV(self.CSV_MAP_2, IP4=2, MAC=0, NAME=1, DESC=3)
			self.test_case.CSV(self.CSV_MAP_3, "\t", IP4=1, MAC=0)

		self.assertIn("DEBUG:CSV_reload:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:11 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:0 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:0 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:CSV_reload:10 MAC mappings total", case_loggy.output)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_reload:10 records read"),2)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_reload:0 new IP4 mappings done"),2)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_reload:0 new MAC mappings done"),2)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_reload:10 IP4 mappings total"),3)
		self.assertEqual(case_loggy.output.count("DEBUG:CSV_reload:10 MAC mappings total"),3)
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"MAC":	self.lmac0,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"MAC":	self.lmac1,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"MAC":	self.lmac2,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"MAC":	self.lmac3,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"MAC":	self.lmac4,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"MAC":	self.lmac5,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"MAC":	self.lmac6,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"MAC":	self.lmac7,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"MAC":	self.lmac8,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"MAC":	self.lmac9,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"IP4":	self.ip0,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"IP4":	self.ip1,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"IP4":	self.ip2,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"IP4":	self.ip3,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"IP4":	self.ip4,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"IP4":	self.ip5,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"IP4":	self.ip6,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"IP4":	self.ip7,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"IP4":	self.ip8,
				"NAME":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"IP4":	self.ip9,
				"NAME":	None,
				"DESC":	None,
			}
		)








	def test_CSV_partial_load_1(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_partial_load_1",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_partial_load_1", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, NAME=2)

		self.assertIn("DEBUG:CSV_partial_load_1:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_1:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_1:10 IP4 mappings total", case_loggy.output)
		self.assertIsNone(self.test_case["MAC"])
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"NAME":	self.name0,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"NAME":	self.name1,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"NAME":	self.name2,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"NAME":	self.name3,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"NAME":	self.name4,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"NAME":	self.name5,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"NAME":	self.name6,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"NAME":	self.name7,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"NAME":	self.name8,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"NAME":	self.name9,
				"MAC":	None,
				"DESC":	None,
			}
		)








	def test_CSV_partial_load_2(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_partial_load_2",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_partial_load_2", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", MAC=1, DESC=3)

		self.assertIn("DEBUG:CSV_partial_load_2:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_2:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_2:10 MAC mappings total", case_loggy.output)
		self.assertIsNone(self.test_case["IP4"])
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"DESC":	self.desc0,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"DESC":	self.desc1,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"DESC":	self.desc2,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"DESC":	self.desc3,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"DESC":	self.desc4,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"DESC":	self.desc5,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"DESC":	self.desc6,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"DESC":	self.desc7,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"DESC":	self.desc8,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"DESC":	self.desc9,
				"IP4":	None,
				"NAME":	None,
			}
		)








	def test_CSV_partial_load_3(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_partial_load_4",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_partial_load_4", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0)

		self.assertIn("DEBUG:CSV_partial_load_4:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_4:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_4:10 IP4 mappings total", case_loggy.output)
		self.assertIsNone(self.test_case["MAC"])
		self.assertEqual(

			self.test_case["IP4"][self.ip0],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip1],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip2],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip3],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip4],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip5],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip6],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip7],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip8],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)
		self.assertEqual(

			self.test_case["IP4"][self.ip9],
			{
				"NAME":	None,
				"MAC":	None,
				"DESC":	None,
			}
		)








	def test_CSV_partial_load_4(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_partial_load_4",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_partial_load_4", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", MAC=1)

		self.assertIn("DEBUG:CSV_partial_load_4:10 records read", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_4:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:CSV_partial_load_4:10 MAC mappings total", case_loggy.output)
		self.assertIsNone(self.test_case["IP4"])
		self.assertEqual(

			self.test_case["MAC"][self.lmac0],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac1],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac2],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac3],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac4],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac5],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac6],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac7],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac8],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)
		self.assertEqual(

			self.test_case["MAC"][self.lmac9],
			{
				"DESC":	None,
				"IP4":	None,
				"NAME":	None,
			}
		)








	def test_CSV_partial_load_5(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="CSV_partial_load_3",
				init_level=10,
			)
		)
		with self.assertLogs("CSV_partial_load_3", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", NAME=2, DESC=3)

		self.assertIn("DEBUG:CSV_partial_load_3:10 records read", case_loggy.output)
		self.assertIsNone(self.test_case["IP4"])
		self.assertIsNone(self.test_case["MAC"])








	def test_mapping_properties(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="ip4_mapping_valid",
				init_level=10,
			)
		)
		with self.assertLogs("ip4_mapping_valid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:ip4_mapping_valid:10 records read", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 MAC mappings total", case_loggy.output)

		self.assertEqual(len(self.test_case.ip4), 10)
		self.assertEqual(len(self.test_case.mac), 10)
		self.assertEqual(
			self.test_case.ip4,
			{
				self.ip0: {

					"MAC":	self.lmac0,
					"NAME":	self.name0,
					"DESC":	self.desc0,
				},
				self.ip1: {

					"MAC":	self.lmac1,
					"NAME":	self.name1,
					"DESC":	self.desc1,
				},
				self.ip2: {

					"MAC":	self.lmac2,
					"NAME":	self.name2,
					"DESC":	self.desc2,
				},
				self.ip3: {

					"MAC":	self.lmac3,
					"NAME":	self.name3,
					"DESC":	self.desc3,
				},
				self.ip4: {

					"MAC":	self.lmac4,
					"NAME":	self.name4,
					"DESC":	self.desc4,
				},
				self.ip5: {

					"MAC":	self.lmac5,
					"NAME":	self.name5,
					"DESC":	self.desc5,
				},
				self.ip6: {

					"MAC":	self.lmac6,
					"NAME":	self.name6,
					"DESC":	self.desc6,
				},
				self.ip7: {

					"MAC":	self.lmac7,
					"NAME":	self.name7,
					"DESC":	self.desc7,
				},
				self.ip8: {

					"MAC":	self.lmac8,
					"NAME":	self.name8,
					"DESC":	self.desc8,
				},
				self.ip9: {

					"MAC":	self.lmac9,
					"NAME":	self.name9,
					"DESC":	self.desc9,
				},
			}
		)
		self.assertEqual(
			list(self.test_case.ip4.keys()),
			[
				self.ip0,
				self.ip1,
				self.ip2,
				self.ip3,
				self.ip4,
				self.ip5,
				self.ip6,
				self.ip7,
				self.ip8,
				self.ip9
			]
		)
		self.assertEqual(
			list(self.test_case.ip4.values()),
			[
				{

					"MAC":	self.lmac0,
					"NAME":	self.name0,
					"DESC":	self.desc0,
				},
				{

					"MAC":	self.lmac1,
					"NAME":	self.name1,
					"DESC":	self.desc1,
				},
				{

					"MAC":	self.lmac2,
					"NAME":	self.name2,
					"DESC":	self.desc2,
				},
				{

					"MAC":	self.lmac3,
					"NAME":	self.name3,
					"DESC":	self.desc3,
				},
				{

					"MAC":	self.lmac4,
					"NAME":	self.name4,
					"DESC":	self.desc4,
				},
				{

					"MAC":	self.lmac5,
					"NAME":	self.name5,
					"DESC":	self.desc5,
				},
				{

					"MAC":	self.lmac6,
					"NAME":	self.name6,
					"DESC":	self.desc6,
				},
				{

					"MAC":	self.lmac7,
					"NAME":	self.name7,
					"DESC":	self.desc7,
				},
				{

					"MAC":	self.lmac8,
					"NAME":	self.name8,
					"DESC":	self.desc8,
				},
				{

					"MAC":	self.lmac9,
					"NAME":	self.name9,
					"DESC":	self.desc9,
				},
			]
		)
		self.assertEqual(
			self.test_case.mac,
			{
				self.lmac0: {

					"IP4":	self.ip0,
					"NAME":	self.name0,
					"DESC":	self.desc0,
				},
				self.lmac1: {

					"IP4":	self.ip1,
					"NAME":	self.name1,
					"DESC":	self.desc1,
				},
				self.lmac2: {

					"IP4":	self.ip2,
					"NAME":	self.name2,
					"DESC":	self.desc2,
				},
				self.lmac3: {

					"IP4":	self.ip3,
					"NAME":	self.name3,
					"DESC":	self.desc3,
				},
				self.lmac4: {

					"IP4":	self.ip4,
					"NAME":	self.name4,
					"DESC":	self.desc4,
				},
				self.lmac5: {

					"IP4":	self.ip5,
					"NAME":	self.name5,
					"DESC":	self.desc5,
				},
				self.lmac6: {

					"IP4":	self.ip6,
					"NAME":	self.name6,
					"DESC":	self.desc6,
				},
				self.lmac7: {

					"IP4":	self.ip7,
					"NAME":	self.name7,
					"DESC":	self.desc7,
				},
				self.lmac8: {

					"IP4":	self.ip8,
					"NAME":	self.name8,
					"DESC":	self.desc8,
				},
				self.lmac9: {

					"IP4":	self.ip9,
					"NAME":	self.name9,
					"DESC":	self.desc9,
				},
			}
		)
		self.assertEqual(
			list(self.test_case.mac.keys()),
			[
				self.lmac0,
				self.lmac1,
				self.lmac2,
				self.lmac3,
				self.lmac4,
				self.lmac5,
				self.lmac6,
				self.lmac7,
				self.lmac8,
				self.lmac9
			]
		)
		self.assertEqual(
			list(self.test_case.mac.values()),
			[
				{

					"IP4":	self.ip0,
					"NAME":	self.name0,
					"DESC":	self.desc0,
				},
				{

					"IP4":	self.ip1,
					"NAME":	self.name1,
					"DESC":	self.desc1,
				},
				{

					"IP4":	self.ip2,
					"NAME":	self.name2,
					"DESC":	self.desc2,
				},
				{

					"IP4":	self.ip3,
					"NAME":	self.name3,
					"DESC":	self.desc3,
				},
				{

					"IP4":	self.ip4,
					"NAME":	self.name4,
					"DESC":	self.desc4,
				},
				{

					"IP4":	self.ip5,
					"NAME":	self.name5,
					"DESC":	self.desc5,
				},
				{

					"IP4":	self.ip6,
					"NAME":	self.name6,
					"DESC":	self.desc6,
				},
				{

					"IP4":	self.ip7,
					"NAME":	self.name7,
					"DESC":	self.desc7,
				},
				{

					"IP4":	self.ip8,
					"NAME":	self.name8,
					"DESC":	self.desc8,
				},
				{

					"IP4":	self.ip9,
					"NAME":	self.name9,
					"DESC":	self.desc9,
				},
			]
		)








	def test_ip4_mapping_valid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="ip4_mapping_valid",
				init_level=10,
			)
		)
		with self.assertLogs("ip4_mapping_valid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:ip4_mapping_valid:10 records read", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_valid:10 MAC mappings total", case_loggy.output)

		self.assertEqual(self.test_case.ip4map_mac(self.ip0), self.lmac0)
		self.assertEqual(self.test_case.ip4map_mac(self.ip1), self.lmac1)
		self.assertEqual(self.test_case.ip4map_mac(self.ip2), self.lmac2)
		self.assertEqual(self.test_case.ip4map_mac(self.ip3), self.lmac3)
		self.assertEqual(self.test_case.ip4map_mac(self.ip4), self.lmac4)
		self.assertEqual(self.test_case.ip4map_mac(self.ip5), self.lmac5)
		self.assertEqual(self.test_case.ip4map_mac(self.ip6), self.lmac6)
		self.assertEqual(self.test_case.ip4map_mac(self.ip7), self.lmac7)
		self.assertEqual(self.test_case.ip4map_mac(self.ip8), self.lmac8)
		self.assertEqual(self.test_case.ip4map_mac(self.ip9), self.lmac9)

		self.assertEqual(self.test_case.ip4map_name(self.ip0), self.name0)
		self.assertEqual(self.test_case.ip4map_name(self.ip1), self.name1)
		self.assertEqual(self.test_case.ip4map_name(self.ip2), self.name2)
		self.assertEqual(self.test_case.ip4map_name(self.ip3), self.name3)
		self.assertEqual(self.test_case.ip4map_name(self.ip4), self.name4)
		self.assertEqual(self.test_case.ip4map_name(self.ip5), self.name5)
		self.assertEqual(self.test_case.ip4map_name(self.ip6), self.name6)
		self.assertEqual(self.test_case.ip4map_name(self.ip7), self.name7)
		self.assertEqual(self.test_case.ip4map_name(self.ip8), self.name8)
		self.assertEqual(self.test_case.ip4map_name(self.ip9), self.name9)

		self.assertEqual(self.test_case.ip4map_desc(self.ip0), self.desc0)
		self.assertEqual(self.test_case.ip4map_desc(self.ip1), self.desc1)
		self.assertEqual(self.test_case.ip4map_desc(self.ip2), self.desc2)
		self.assertEqual(self.test_case.ip4map_desc(self.ip3), self.desc3)
		self.assertEqual(self.test_case.ip4map_desc(self.ip4), self.desc4)
		self.assertEqual(self.test_case.ip4map_desc(self.ip5), self.desc5)
		self.assertEqual(self.test_case.ip4map_desc(self.ip6), self.desc6)
		self.assertEqual(self.test_case.ip4map_desc(self.ip7), self.desc7)
		self.assertEqual(self.test_case.ip4map_desc(self.ip8), self.desc8)
		self.assertEqual(self.test_case.ip4map_desc(self.ip9), self.desc9)
		self.assertEqual(

			self.test_case.ip4map(self.ip0),
			{
				"MAC":	self.lmac0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip1),
			{
				"MAC":	self.lmac1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip2),
			{
				"MAC":	self.lmac2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip3),
			{
				"MAC":	self.lmac3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip4),
			{
				"MAC":	self.lmac4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip5),
			{
				"MAC":	self.lmac5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip6),
			{
				"MAC":	self.lmac6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip7),
			{
				"MAC":	self.lmac7,
				"NAME":	self.name7,
				"DESC":	self.desc7,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip8),
			{
				"MAC":	self.lmac8,
				"NAME":	self.name8,
				"DESC":	self.desc8,
			}
		)
		self.assertEqual(

			self.test_case.ip4map(self.ip9),
			{
				"MAC":	self.lmac9,
				"NAME":	self.name9,
				"DESC":	self.desc9,
			}
		)








	def test_ip4_mapping_invalid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="ip4_mapping_invalid",
				init_level=10,
			)
		)
		with self.assertLogs("ip4_mapping_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:ip4_mapping_invalid:10 records read", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_invalid:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_invalid:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_invalid:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:ip4_mapping_invalid:10 MAC mappings total", case_loggy.output)

		for invalid in (

			"IP4", 420, 69., True, False, None, ..., print, LibraryContrib,
			[ self.ip2 ],( self.ip2, ),{ self.ip2 },{ "IP4": self.ip2 }
		):
			with self.subTest(addr=invalid):

				self.assertIsNone(self.test_case.ip4map(invalid))
				self.assertIsNone(self.test_case.ip4map_mac(invalid))
				self.assertIsNone(self.test_case.ip4map_name(invalid))
				self.assertIsNone(self.test_case.ip4map_desc(invalid))








	def test_mac_mapping_valid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="mac_mapping_valid",
				init_level=10,
			)
		)
		with self.assertLogs("mac_mapping_valid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:mac_mapping_valid:10 records read", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_valid:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_valid:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_valid:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_valid:10 MAC mappings total", case_loggy.output)

		self.assertEqual(self.test_case.macmap_ip4(self.lmac0), self.ip0)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac1), self.ip1)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac2), self.ip2)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac3), self.ip3)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac4), self.ip4)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac5), self.ip5)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac6), self.ip6)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac7), self.ip7)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac8), self.ip8)
		self.assertEqual(self.test_case.macmap_ip4(self.lmac9), self.ip9)

		self.assertEqual(self.test_case.macmap_name(self.lmac0), self.name0)
		self.assertEqual(self.test_case.macmap_name(self.lmac1), self.name1)
		self.assertEqual(self.test_case.macmap_name(self.lmac2), self.name2)
		self.assertEqual(self.test_case.macmap_name(self.lmac3), self.name3)
		self.assertEqual(self.test_case.macmap_name(self.lmac4), self.name4)
		self.assertEqual(self.test_case.macmap_name(self.lmac5), self.name5)
		self.assertEqual(self.test_case.macmap_name(self.lmac6), self.name6)
		self.assertEqual(self.test_case.macmap_name(self.lmac7), self.name7)
		self.assertEqual(self.test_case.macmap_name(self.lmac8), self.name8)
		self.assertEqual(self.test_case.macmap_name(self.lmac9), self.name9)

		self.assertEqual(self.test_case.macmap_desc(self.lmac0), self.desc0)
		self.assertEqual(self.test_case.macmap_desc(self.lmac1), self.desc1)
		self.assertEqual(self.test_case.macmap_desc(self.lmac2), self.desc2)
		self.assertEqual(self.test_case.macmap_desc(self.lmac3), self.desc3)
		self.assertEqual(self.test_case.macmap_desc(self.lmac4), self.desc4)
		self.assertEqual(self.test_case.macmap_desc(self.lmac5), self.desc5)
		self.assertEqual(self.test_case.macmap_desc(self.lmac6), self.desc6)
		self.assertEqual(self.test_case.macmap_desc(self.lmac7), self.desc7)
		self.assertEqual(self.test_case.macmap_desc(self.lmac8), self.desc8)
		self.assertEqual(self.test_case.macmap_desc(self.lmac9), self.desc9)
		self.assertEqual(

			self.test_case.macmap(self.lmac0),
			{
				"IP4":	self.ip0,
				"NAME":	self.name0,
				"DESC":	self.desc0,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac1),
			{
				"IP4":	self.ip1,
				"NAME":	self.name1,
				"DESC":	self.desc1,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac2),
			{
				"IP4":	self.ip2,
				"NAME":	self.name2,
				"DESC":	self.desc2,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac3),
			{
				"IP4":	self.ip3,
				"NAME":	self.name3,
				"DESC":	self.desc3,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac4),
			{
				"IP4":	self.ip4,
				"NAME":	self.name4,
				"DESC":	self.desc4,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac5),
			{
				"IP4":	self.ip5,
				"NAME":	self.name5,
				"DESC":	self.desc5,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac6),
			{
				"IP4":	self.ip6,
				"NAME":	self.name6,
				"DESC":	self.desc6,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac7),
			{
				"IP4":	self.ip7,
				"NAME":	self.name7,
				"DESC":	self.desc7,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac8),
			{
				"IP4":	self.ip8,
				"NAME":	self.name8,
				"DESC":	self.desc8,
			}
		)
		self.assertEqual(

			self.test_case.macmap(self.lmac9),
			{
				"IP4":	self.ip9,
				"NAME":	self.name9,
				"DESC":	self.desc9,
			}
		)








	def test_mac_mapping_invalid(self):

		self.test_case = MaraudersMap(
			LibraryContrib(

				handler=self.MARAUDERS_HANDLER,
				init_name="mac_mapping_invalid",
				init_level=10,
			)
		)
		with self.assertLogs("mac_mapping_invalid", 10) as case_loggy:
			self.test_case.CSV(self.CSV_MAP_1, ";", IP4=0, MAC=1, NAME=2, DESC=3)

		self.assertIn("DEBUG:mac_mapping_invalid:10 records read", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_invalid:10 new IP4 mappings done", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_invalid:10 IP4 mappings total", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_invalid:10 new MAC mappings done", case_loggy.output)
		self.assertIn("DEBUG:mac_mapping_invalid:10 MAC mappings total", case_loggy.output)

		for invalid in (

			"MAC", 420, 69., True, False, None, ..., print, LibraryContrib,
			[ self.lmac4 ],( self.lmac4, ),{ self.lmac4 },{ "MAC": self.lmac4 }
		):
			with self.subTest(addr=invalid):

				self.assertIsNone(self.test_case.macmap(invalid))
				self.assertIsNone(self.test_case.macmap_ip4(invalid))
				self.assertIsNone(self.test_case.macmap_name(invalid))
				self.assertIsNone(self.test_case.macmap_desc(invalid))








if __name__ == "__main__" : unittest.main(verbosity=2)







