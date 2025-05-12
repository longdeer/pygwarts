import	os
import	unittest
from	random								import choice
from	ipaddress							import ip_network
from	pygwarts.magical.time_turner.timers	import DIRTtimer
from	pygwarts.tests.filch				import FilchTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.filch.nettherin			import is_valid_ip4
from	pygwarts.filch.linkindor			import P_VALID_MAC
from	pygwarts.filch.linkindor			import P_ARP_REQ
from	pygwarts.filch.linkindor			import GP_ARP_REQ
from	pygwarts.filch.linkindor			import GP_ARP_REQ_LOG
from	pygwarts.filch.linkindor			import GP_ARP_RES_LOG
from	pygwarts.filch.linkindor			import GP_O1_VALID_MAC
from	pygwarts.filch.linkindor			import GP_O2_VALID_MAC
from	pygwarts.filch.linkindor			import is_valid_MAC
from	pygwarts.filch.linkindor			import EUI48_format
from	pygwarts.filch.linkindor.arp		import ARPDiscovery
from	pygwarts.filch.linkindor.arp		import ARPSniffer
from	pygwarts.filch.linkindor.arp		import ARPRequestInspector
from	pygwarts.filch.linkindor.arp		import ARPResponseInspector
from	pygwarts.filch.marauders_map		import MaraudersMap








class LinkindorCase(FilchTestCase):

	"""
		Testing L2 instruments
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.LINKINDOR_HANDLER): os.remove(cls.LINKINDOR_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.LINKINDOR_HANDLER)
	def test_P_VALID_MAC_valid(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertTrue(P_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertTrue(P_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertTrue(P_VALID_MAC.fullmatch(mac3))




	def test_P_VALID_MAC_invalid_1(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac5 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac6 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac7 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac8 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac9 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac10 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac11 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac12 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):	self.assertFalse(P_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2):	self.assertFalse(P_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3):	self.assertFalse(P_VALID_MAC.fullmatch(mac3))
		with self.subTest(mac=mac4):	self.assertFalse(P_VALID_MAC.fullmatch(mac4))
		with self.subTest(mac=mac5):	self.assertFalse(P_VALID_MAC.fullmatch(mac5))
		with self.subTest(mac=mac6):	self.assertFalse(P_VALID_MAC.fullmatch(mac6))
		with self.subTest(mac=mac7):	self.assertFalse(P_VALID_MAC.fullmatch(mac7))
		with self.subTest(mac=mac8):	self.assertFalse(P_VALID_MAC.fullmatch(mac8))
		with self.subTest(mac=mac9):	self.assertFalse(P_VALID_MAC.fullmatch(mac9))
		with self.subTest(mac=mac10):	self.assertFalse(P_VALID_MAC.fullmatch(mac10))
		with self.subTest(mac=mac11):	self.assertFalse(P_VALID_MAC.fullmatch(mac11))
		with self.subTest(mac=mac12):	self.assertFalse(P_VALID_MAC.fullmatch(mac12))




	def test_P_VALID_MAC_invalid_2(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertFalse(P_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertFalse(P_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertFalse(P_VALID_MAC.fullmatch(mac3))




	def test_P_VALID_MAC_invalid_3(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertFalse(P_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertFalse(P_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertFalse(P_VALID_MAC.fullmatch(mac3))
		with self.subTest(mac=mac4): self.assertFalse(P_VALID_MAC.fullmatch(mac4))




	def test_P_VALID_MAC_invalid_4(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertFalse(P_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertFalse(P_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertFalse(P_VALID_MAC.fullmatch(mac3))




	def test_P_VALID_MAC_invalid_5(self):

		for o1 in 10, 42., "AM", True:
			for o2 in 10, 42., "AM", True:
				for o3 in 10, 42., "AM", True:
					for o4 in 10, 42., "AM", True:
						for o5 in 10, 42., "AM", True:
							for o6 in 42., "AM", True:

								mac1 = f"{o1}:{o2}:{o3}:{o4}:{o5}:{o6}"
								mac2 = f"{o1}-{o2}-{o3}-{o4}-{o5}-{o6}"
								mac3 = f"{o1}{o2}.{o3}{o4}.{o5}{o6}"

								with self.subTest(mac=mac1): self.assertFalse(P_VALID_MAC.fullmatch(mac1))
								with self.subTest(mac=mac2): self.assertFalse(P_VALID_MAC.fullmatch(mac2))
								with self.subTest(mac=mac3): self.assertFalse(P_VALID_MAC.fullmatch(mac3))








	def test_is_valid_MAC_valid(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertTrue(is_valid_MAC(mac1))
		with self.subTest(mac=mac2): self.assertTrue(is_valid_MAC(mac2))
		with self.subTest(mac=mac3): self.assertTrue(is_valid_MAC(mac3))




	def test_is_valid_MAC_invalid_1(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac5 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac6 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac7 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac8 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac9 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac10 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac11 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac12 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):	self.assertIsNone(is_valid_MAC(mac1))
		with self.subTest(mac=mac2):	self.assertIsNone(is_valid_MAC(mac2))
		with self.subTest(mac=mac3):	self.assertIsNone(is_valid_MAC(mac3))
		with self.subTest(mac=mac4):	self.assertIsNone(is_valid_MAC(mac4))
		with self.subTest(mac=mac5):	self.assertIsNone(is_valid_MAC(mac5))
		with self.subTest(mac=mac6):	self.assertIsNone(is_valid_MAC(mac6))
		with self.subTest(mac=mac7):	self.assertIsNone(is_valid_MAC(mac7))
		with self.subTest(mac=mac8):	self.assertIsNone(is_valid_MAC(mac8))
		with self.subTest(mac=mac9):	self.assertIsNone(is_valid_MAC(mac9))
		with self.subTest(mac=mac10):	self.assertIsNone(is_valid_MAC(mac10))
		with self.subTest(mac=mac11):	self.assertIsNone(is_valid_MAC(mac11))
		with self.subTest(mac=mac12):	self.assertIsNone(is_valid_MAC(mac12))




	def test_is_valid_MAC_invalid_2(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertIsNone(is_valid_MAC(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(is_valid_MAC(mac2))
		with self.subTest(mac=mac3): self.assertIsNone(is_valid_MAC(mac3))




	def test_is_valid_MAC_invalid_3(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertIsNone(is_valid_MAC(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(is_valid_MAC(mac2))
		with self.subTest(mac=mac3): self.assertIsNone(is_valid_MAC(mac3))
		with self.subTest(mac=mac4): self.assertIsNone(is_valid_MAC(mac4))




	def test_is_valid_MAC_invalid_4(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertFalse(is_valid_MAC(mac1))
		with self.subTest(mac=mac2): self.assertFalse(is_valid_MAC(mac2))
		with self.subTest(mac=mac3): self.assertFalse(is_valid_MAC(mac3))




	def test_is_valid_MAC_invalid_5(self):

		for o1 in 10, 42., "AM", True:
			for o2 in 10, 42., "AM", True:
				for o3 in 10, 42., "AM", True:
					for o4 in 10, 42., "AM", True:
						for o5 in 10, 42., "AM", True:
							for o6 in 42., "AM", True:

								mac1 = f"{o1}:{o2}:{o3}:{o4}:{o5}:{o6}"
								mac2 = f"{o1}-{o2}-{o3}-{o4}-{o5}-{o6}"
								mac3 = f"{o1}{o2}.{o3}{o4}.{o5}{o6}"

								with self.subTest(mac=mac1): self.assertIsNone(is_valid_MAC(mac1))
								with self.subTest(mac=mac2): self.assertIsNone(is_valid_MAC(mac2))
								with self.subTest(mac=mac3): self.assertIsNone(is_valid_MAC(mac3))








	def test_GP_O1_VALID_MAC_valid(self):

		O11		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O12		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O13		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O14		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O15		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O16		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O21		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O22		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O23		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O24		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O25		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O26		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O31		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O32		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O33		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O34		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O35		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O36		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"

		mac1	= f"{O11}:{O12}:{O13}:{O14}:{O15}:{O16}"
		mac2	= f"{O21}-{O22}-{O23}-{O24}-{O25}-{O26}"
		mac3	= f"{O31}-{O32}:{O33}-{O34}:{O35}-{O36}"

		with self.subTest(mac=mac1):

			match = GP_O1_VALID_MAC.fullmatch(mac1)
			O1,O2,O3,O4,O5,O6 = match.group("octet1","octet2","octet3","octet4","octet5","octet6")
			self.assertEqual(int(O1,16), int(O11,16))
			self.assertEqual(int(O2,16), int(O12,16))
			self.assertEqual(int(O3,16), int(O13,16))
			self.assertEqual(int(O4,16), int(O14,16))
			self.assertEqual(int(O5,16), int(O15,16))
			self.assertEqual(int(O6,16), int(O16,16))

		with self.subTest(mac=mac2):

			match = GP_O1_VALID_MAC.fullmatch(mac2)
			O1,O2,O3,O4,O5,O6 = match.group("octet1","octet2","octet3","octet4","octet5","octet6")
			self.assertEqual(int(O1,16), int(O21,16))
			self.assertEqual(int(O2,16), int(O22,16))
			self.assertEqual(int(O3,16), int(O23,16))
			self.assertEqual(int(O4,16), int(O24,16))
			self.assertEqual(int(O5,16), int(O25,16))
			self.assertEqual(int(O6,16), int(O26,16))

		with self.subTest(mac=mac3):

			match = GP_O1_VALID_MAC.fullmatch(mac3)
			O1,O2,O3,O4,O5,O6 = match.group("octet1","octet2","octet3","octet4","octet5","octet6")
			self.assertEqual(int(O1,16), int(O31,16))
			self.assertEqual(int(O2,16), int(O32,16))
			self.assertEqual(int(O3,16), int(O33,16))
			self.assertEqual(int(O4,16), int(O34,16))
			self.assertEqual(int(O5,16), int(O35,16))
			self.assertEqual(int(O6,16), int(O36,16))




	def test_GP_O1_VALID_MAC_invalid_1(self):
		OS1 = str(
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		OS2 = str(
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		OS3 = str(
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac = f"{OS1}.{OS2}.{OS3}"

		self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac))




	def test_GP_O1_VALID_MAC_invalid_2(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac5 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac6 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac7 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac8 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac9 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac10 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac11 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac12 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac3))
		with self.subTest(mac=mac4):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac4))
		with self.subTest(mac=mac5):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac5))
		with self.subTest(mac=mac6):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac6))
		with self.subTest(mac=mac7):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac7))
		with self.subTest(mac=mac8):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac8))
		with self.subTest(mac=mac9):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac9))
		with self.subTest(mac=mac10):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac10))
		with self.subTest(mac=mac11):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac11))
		with self.subTest(mac=mac12):	self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac12))




	def test_GP_O1_VALID_MAC_invalid_3(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac3))




	def test_GP_O1_VALID_MAC_invalid_4(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac3))




	def test_GP_O1_VALID_MAC_invalid_5(self):

		for o1 in 10, 42., "AM", True:
			for o2 in 10, 42., "AM", True:
				for o3 in 10, 42., "AM", True:
					for o4 in 10, 42., "AM", True:
						for o5 in 10, 42., "AM", True:
							for o6 in 42., "AM", True:

								mac1 = f"{o1}:{o2}:{o3}:{o4}:{o5}:{o6}"
								mac2 = f"{o1}-{o2}-{o3}-{o4}-{o5}-{o6}"
								mac3 = f"{o1}{o2}.{o3}{o4}.{o5}{o6}"

								with self.subTest(mac=mac1):
									self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac1))

								with self.subTest(mac=mac2):
									self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac2))

								with self.subTest(mac=mac3):
									self.assertIsNone(GP_O1_VALID_MAC.fullmatch(mac3))








	def test_GP_O2_VALID_MAC_valid(self):

		for i in range(20000):

			OS1 = str(
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
			)
			OS2 = str(
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
			)
			OS3 = str(
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
			)

			mac = f"{OS1}.{OS2}.{OS3}"
			match = GP_O2_VALID_MAC.fullmatch(mac)
			OO1,OO2,OO3 = match.group("octets1", "octets2", "octets3")
			self.assertEqual(int(OO1,16), int(OS1,16))
			self.assertEqual(int(OO2,16), int(OS2,16))
			self.assertEqual(int(OO3,16), int(OS3,16))




	def test_GP_O2_VALID_MAC_invalid_1(self):

		O11		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O12		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O13		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O14		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O15		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O16		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O21		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O22		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O23		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O24		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O25		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O26		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O31		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O32		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O33		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O34		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O35		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		O36		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
		mac1	= f"{O11}:{O12}:{O13}:{O14}:{O15}:{O16}"
		mac2	= f"{O21}-{O22}-{O23}-{O24}-{O25}-{O26}"
		mac3	= f"{O31}-{O32}:{O33}-{O34}:{O35}-{O36}"

		with self.subTest(mac=mac1): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac3))




	def test_GP_O2_VALID_MAC_invalid_2(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac5 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac6 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac7 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac8 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac9 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac10 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac11 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac12 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac3))
		with self.subTest(mac=mac4):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac4))
		with self.subTest(mac=mac5):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac5))
		with self.subTest(mac=mac6):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac6))
		with self.subTest(mac=mac7):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac7))
		with self.subTest(mac=mac8):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac8))
		with self.subTest(mac=mac9):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac9))
		with self.subTest(mac=mac10):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac10))
		with self.subTest(mac=mac11):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac11))
		with self.subTest(mac=mac12):	self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac12))




	def test_GP_O2_VALID_MAC_invalid_3(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac2))




	def test_GP_O2_VALID_MAC_invalid_4(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac1))
		with self.subTest(mac=mac2): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac2))
		with self.subTest(mac=mac3): self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac3))




	def test_GP_O2_VALID_MAC_invalid_5(self):

		for o1 in 10, 42., "AM", True:
			for o2 in 10, 42., "AM", True:
				for o3 in 10, 42., "AM", True:
					for o4 in 10, 42., "AM", True:
						for o5 in 10, 42., "AM", True:
							for o6 in 42., "AM", True:

								mac = f"{o1}{o2}.{o3}{o4}.{o5}{o6}"

								with self.subTest(mac=mac):
									self.assertIsNone(GP_O2_VALID_MAC.fullmatch(mac))








	def test_EUI48_format_valid(self):

		for i in range(10000):

			OS1		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
			OS2		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
			OS3		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
			OS4		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
			OS5		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"
			OS6		= f"{choice(self.valid_MAC_chars)}{choice(self.valid_MAC_chars)}"

			mac1	= f"{OS1}-{OS2}-{OS3}-{OS4}-{OS5}-{OS6}"
			mac2	= f"{OS1}:{OS2}:{OS3}:{OS4}:{OS5}:{OS6}"
			mac3	= f"{OS1}{OS2}.{OS3}{OS4}.{OS5}{OS6}"
			mac4	= f"{OS1}-{OS2}:{OS3}-{OS4}:{OS5}-{OS6}"

			mac1l	= mac1.lower()
			mac2l	= mac2.lower()
			mac3l	= mac3.lower()
			mac4l	= mac4.lower()

			with self.subTest(addr=mac1):

				self.assertEqual(EUI48_format(mac1),mac1l)
				self.assertEqual(EUI48_format(mac1,":"),mac2l)
				self.assertEqual(EUI48_format(mac1,"."),mac3l)

			with self.subTest(addr=mac2):

				self.assertEqual(EUI48_format(mac2),mac1l)
				self.assertEqual(EUI48_format(mac2,":"),mac2l)
				self.assertEqual(EUI48_format(mac2,"."),mac3l)

			with self.subTest(addr=mac3):

				self.assertEqual(EUI48_format(mac3),mac1l)
				self.assertEqual(EUI48_format(mac3,":"),mac2l)
				self.assertEqual(EUI48_format(mac3,"."),mac3l)

			with self.subTest(addr=mac3):

				self.assertEqual(EUI48_format(mac4),mac1l)
				self.assertEqual(EUI48_format(mac4,":"),mac2l)
				self.assertEqual(EUI48_format(mac4,"."),mac3l)




	def test_EUI48_format_invalid_1(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac4 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac5 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac6 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac7 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac8 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac9 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac10 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac11 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac12 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):

			self.assertIsNone(EUI48_format(mac1))
			self.assertIsNone(EUI48_format(mac1,":"))
			self.assertIsNone(EUI48_format(mac1,"."))

		with self.subTest(mac=mac2):

			self.assertIsNone(EUI48_format(mac2))
			self.assertIsNone(EUI48_format(mac2,":"))
			self.assertIsNone(EUI48_format(mac2,"."))

		with self.subTest(mac=mac3):

			self.assertIsNone(EUI48_format(mac3))
			self.assertIsNone(EUI48_format(mac3,":"))
			self.assertIsNone(EUI48_format(mac3,"."))

		with self.subTest(mac=mac4):

			self.assertIsNone(EUI48_format(mac4))
			self.assertIsNone(EUI48_format(mac4,":"))
			self.assertIsNone(EUI48_format(mac4,"."))

		with self.subTest(mac=mac5):

			self.assertIsNone(EUI48_format(mac5))
			self.assertIsNone(EUI48_format(mac5,":"))
			self.assertIsNone(EUI48_format(mac5,"."))

		with self.subTest(mac=mac6):

			self.assertIsNone(EUI48_format(mac6))
			self.assertIsNone(EUI48_format(mac6,":"))
			self.assertIsNone(EUI48_format(mac6,"."))

		with self.subTest(mac=mac7):

			self.assertIsNone(EUI48_format(mac7))
			self.assertIsNone(EUI48_format(mac7,":"))
			self.assertIsNone(EUI48_format(mac7,"."))

		with self.subTest(mac=mac8):

			self.assertIsNone(EUI48_format(mac8))
			self.assertIsNone(EUI48_format(mac8,":"))
			self.assertIsNone(EUI48_format(mac8,"."))

		with self.subTest(mac=mac9):

			self.assertIsNone(EUI48_format(mac9))
			self.assertIsNone(EUI48_format(mac9,":"))
			self.assertIsNone(EUI48_format(mac9,"."))

		with self.subTest(mac=mac10):

			self.assertIsNone(EUI48_format(mac10))
			self.assertIsNone(EUI48_format(mac10,":"))
			self.assertIsNone(EUI48_format(mac10,"."))

		with self.subTest(mac=mac11):

			self.assertIsNone(EUI48_format(mac11))
			self.assertIsNone(EUI48_format(mac11,":"))
			self.assertIsNone(EUI48_format(mac11,"."))

		with self.subTest(mac=mac12):

			self.assertIsNone(EUI48_format(mac12))
			self.assertIsNone(EUI48_format(mac12,":"))
			self.assertIsNone(EUI48_format(mac12,"."))




	def test_EUI48_format_invalid_2(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):

			self.assertFalse(EUI48_format(mac1))
			self.assertFalse(EUI48_format(mac1,":"))
			self.assertFalse(EUI48_format(mac1,"."))

		with self.subTest(mac=mac2):

			self.assertFalse(EUI48_format(mac2))
			self.assertFalse(EUI48_format(mac2,":"))
			self.assertFalse(EUI48_format(mac2,"."))

		with self.subTest(mac=mac3):

			self.assertFalse(EUI48_format(mac3))
			self.assertFalse(EUI48_format(mac3,":"))
			self.assertFalse(EUI48_format(mac3,"."))




	def test_EUI48_format_invalid_3(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):

			self.assertIsNone(EUI48_format(mac1))
			self.assertIsNone(EUI48_format(mac1,":"))
			self.assertIsNone(EUI48_format(mac1,"."))

		with self.subTest(mac=mac2):

			self.assertIsNone(EUI48_format(mac2))
			self.assertIsNone(EUI48_format(mac2,":"))
			self.assertIsNone(EUI48_format(mac2,"."))

		with self.subTest(mac=mac3):

			self.assertIsNone(EUI48_format(mac3))
			self.assertIsNone(EUI48_format(mac3,":"))
			self.assertIsNone(EUI48_format(mac3,"."))




	def test_EUI48_format_invalid_4(self):
		mac1 = str(

			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			":"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac2 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)
		mac3 = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"."
			f"{choice(self.valid_MAC_chars[1:])}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		with self.subTest(mac=mac1):

			self.assertIsNone(EUI48_format(mac1))
			self.assertIsNone(EUI48_format(mac1,":"))
			self.assertIsNone(EUI48_format(mac1,"."))

		with self.subTest(mac=mac2):

			self.assertIsNone(EUI48_format(mac2))
			self.assertIsNone(EUI48_format(mac2,":"))
			self.assertIsNone(EUI48_format(mac2,"."))

		with self.subTest(mac=mac3):

			self.assertIsNone(EUI48_format(mac3))
			self.assertIsNone(EUI48_format(mac3,":"))
			self.assertIsNone(EUI48_format(mac3,"."))




	def test_EUI48_format_invalid_5(self):

		for o1 in 10, 42., "AM", True:
			for o2 in 10, 42., "AM", True:
				for o3 in 10, 42., "AM", True:
					for o4 in 10, 42., "AM", True:
						for o5 in 10, 42., "AM", True:
							for o6 in 42., "AM", True:

								mac1 = f"{o1}:{o2}:{o3}:{o4}:{o5}:{o6}"
								mac2 = f"{o1}-{o2}-{o3}-{o4}-{o5}-{o6}"
								mac3 = f"{o1}{o2}.{o3}{o4}.{o5}{o6}"

								with self.subTest(mac=mac1):

									self.assertIsNone(EUI48_format(mac1))
									self.assertIsNone(EUI48_format(mac1,":"))
									self.assertIsNone(EUI48_format(mac1,"."))

								with self.subTest(mac=mac2):

									self.assertIsNone(EUI48_format(mac2))
									self.assertIsNone(EUI48_format(mac2,":"))
									self.assertIsNone(EUI48_format(mac2,"."))

								with self.subTest(mac=mac3):

									self.assertIsNone(EUI48_format(mac3))
									self.assertIsNone(EUI48_format(mac3,":"))
									self.assertIsNone(EUI48_format(mac3,"."))




	def test_EUI48_format_invalid_delimiter(self):

		mac = str(

			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
			"-"
			f"{choice(self.valid_MAC_chars)}"
			f"{choice(self.valid_MAC_chars)}"
		)

		for delimiter in ",", 1, .1, True, False, None, ..., print, [ "-" ],( "-", ),{ "-" },{ "d": "-" }:
			with self.subTest(addr=mac, d=delimiter):
				self.assertRaises(AssertionError, EUI48_format, mac, delimiter)








	def test_ARP_records(self):

		for o11,o12 in (
			( choice(self.valid_IP_chars),choice(self.valid_IP_chars) ) for _ in range(10)
		):
			for o21,o22 in (
				( choice(self.valid_IP_chars),choice(self.valid_IP_chars) ) for _ in range(10)
			):
				for o31,o32 in (
					( choice(self.valid_IP_chars),choice(self.valid_IP_chars) ) for _ in range(10)
				):
					for o41,o42 in (
						( choice(self.valid_IP_chars),choice(self.valid_IP_chars) ) for _ in range(10)
					):

						v11 = f"{o11}.{o21}.{o31}.{o41}"
						v12 = f"{o12}.{o22}.{o32}.{o42}"
						mac = str(

							f"{choice(self.valid_MAC_chars)}"
							f"{choice(self.valid_MAC_chars)}"
							"-"
							f"{choice(self.valid_MAC_chars)}"
							f"{choice(self.valid_MAC_chars)}"
							"-"
							f"{choice(self.valid_MAC_chars)}"
							f"{choice(self.valid_MAC_chars)}"
							"-"
							f"{choice(self.valid_MAC_chars)}"
							f"{choice(self.valid_MAC_chars)}"
							"-"
							f"{choice(self.valid_MAC_chars)}"
							f"{choice(self.valid_MAC_chars)}"
							"-"
							f"{choice(self.valid_MAC_chars)}"
							f"{choice(self.valid_MAC_chars)}"
						)
						REQ = f"who has {v11} says {v12} ({mac})"
						RES = f"{mac} answered"

						with self.subTest(dst=v11, src=v12, mac=mac):

							self.assertTrue(P_ARP_REQ.search(REQ))

							dst1,src1 = GP_ARP_REQ.search(REQ).group("dst", "src")
							self.assertEqual(dst1, v11)
							self.assertEqual(src1, v12)

							dst2,src2,smac1 = GP_ARP_REQ_LOG.search(REQ).group("dst", "src", "mac")
							self.assertEqual(dst2, v11)
							self.assertEqual(src2, v12)
							self.assertEqual(smac1, mac)

							smac2 = GP_ARP_RES_LOG.search(RES).group("mac")
							self.assertEqual(smac2, mac)








	def test_ARPDiscovery(self):

		# Host discovery packet builder example. Will try to send an ARP request from some ip4 and
		# some interface with target ip4 address specified, and receive an answer.
		# It is assumed scappy 2.5.0rc3 installed, as was originally desinged.

		class TestDiscovery(ARPDiscovery):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "ARPDiscovery"
				init_level	= 10

		self.test_case = TestDiscovery()

		try:

			from scapy.all	import srp
			from scapy.all	import Ether
			from scapy.all	import ARP
			from operator	import getitem

			target = ""	# to be filled with real ip4 address to be checked
			expect = ""	# to be filled with real physical address to be checked

			assert len(target)
			assert len(expect)

			def discoverer(addr, **kwargs) -> str :

				R = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /ARP(pdst=addr), **kwargs)
				if len(R) and len(R[0]): return getattr(getattr(getitem(getitem(R,0),0),"answer"),"src")

		except	(ImportError, AssertionError):

			target = "10.10.10.10"
			expect = str(

				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				"-"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				"-"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				"-"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				"-"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
				"-"
				f"{choice(self.valid_MAC_chars)}"
				f"{choice(self.valid_MAC_chars)}"
			)

			def discoverer(target, **kwargs): return expect

		self.assertEqual(self.test_case(target, discoverer, retry=1, timeout=1, verbose=0), expect.lower())




	def test_ARPDiscovery_invalid_ip(self):

		class TestDiscovery(ARPDiscovery):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "ARPDiscovery_invalid_ip"
				init_level	= 10

		self.test_case = TestDiscovery()
		for invalid in (

			"10.10.10.300", "LOL", 42, 69., True, False, None, ..., print, ARPDiscovery,
			[ "10.10.10.10" ],( "10.10.10.10", ),{ "10.10.10.10" },{ "target": "10.10.10.10" }
		):
			with self.subTest(ip=invalid):
				with self.assertLogs("ARPDiscovery_invalid_ip", 10) as case_loggy:

					self.assertIsNone(self.test_case(invalid, lambda : None))
			self.assertIn(
				f"DEBUG:ARPDiscovery_invalid_ip:Invalid IP4 address \"{invalid}\"", case_loggy.output
			)




	def test_ARPDiscovery_invalid_discoverer(self):

		class TestDiscovery(ARPDiscovery):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "ARPDiscovery_invalid_discoverer"
				init_level	= 10

		self.test_case = TestDiscovery()
		for invalid in (

			"LOL", 42, 69., True, False, None, ..., unittest,
			[ print ],( print, ),{ print },{ "discoverer": print }
		):
			with self.subTest(discoverer=invalid):
				with self.assertLogs("ARPDiscovery_invalid_discoverer", 10) as case_loggy:

					self.assertIsNone(self.test_case("10.10.10.10", invalid))
			self.assertIn(

				f"DEBUG:ARPDiscovery_invalid_discoverer:Invalid discoverer \"{invalid}\"",
				case_loggy.output
			)




	def test_ARPDiscovery_raise(self):

		class TestDiscovery(ARPDiscovery):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "ARPDiscovery_raise"
				init_level	= 10

		def raiser(*args, **kwargs): raise ValueError("The value is not enough")
		self.test_case = TestDiscovery()
		with self.assertLogs("ARPDiscovery_raise", 10) as case_loggy:
			self.assertIsNone(self.test_case("10.10.10.10", raiser))

		self.assertIn(

			f"DEBUG:ARPDiscovery_raise:Discovery failed due to ValueError: The value is not enough",
			case_loggy.output
		)




	def test_PoolDiscovery(self):

		class TestDiscovery(ARPDiscovery):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "PoolDiscovery"
				init_level	= 10

		self.test_case = TestDiscovery()
		expect = "11-22-33-44-55-66"

		def discoverer(target, **kwargs):
			if	is_valid_ip4(target): return expect

		for ip4 in list(ip_network("192.168.0.0/24"))[1:-1]:
			self.assertEqual(self.test_case(str(ip4), discoverer), expect)








	@unittest.skipIf(os.name == "nt", "cannot test termination, cause windows cannot fork")
	def test_ARPSniffing(self):

		# ARP sniffer example. Will try to listen broadcast traffic on some ip4 and some interface
		# (can be specified by "iface" kwarg in current implementation) and recognize ARP requests.
		# It is assumed scappy 2.5.0rc3 installed, as was originally desinged.

		try:

			from scapy.all	import sniff
			from scapy.all	import Ether
			from scapy.all	import ARP

			@DIRTtimer(T=5)
			class TestSniffing(ARPSniffer):
				class loggy(LibraryContrib):

					handler		= self.LINKINDOR_HANDLER
					init_name	= "ARPSniffer"
					init_level	= 10

				def trap(self, FRAME :Ether):

					if	(MAC := EUI48_format(FRAME.src)) is not None:
						match FRAME[ARP].op:

							case 1:	self.loggy.info(f"{P_ARP_REQ.search(FRAME.summary()).group()} ({MAC})")
							case 2:	self.loggy.debug(f"{MAC} answer")
							case _:	self.loggy.debug(FRAME.summary())

			self.test_case = TestSniffing()
			self.test_case(sniff, filter="arp", prn=self.test_case.trap)

		except:	return




	def test_ARPSniffing_invalid_sniffer(self):

		class TestSniffing(ARPSniffer):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "ARPSniffing_invalid_sniffer"
				init_level	= 10

		self.test_case = TestSniffing()
		for invalid in (

			"LOL", 42, 69., True, False, None, ..., unittest,
			[ print ],( print, ),{ print },{ "sniffer": print }
		):
			with self.subTest(sniffer=invalid):
				with self.assertLogs("ARPSniffing_invalid_sniffer", 10) as case_loggy:

					self.assertIsNone(self.test_case(invalid))
			self.assertIn(

				f"DEBUG:ARPSniffing_invalid_sniffer:Invalid sniffer \"{invalid}\"",
				case_loggy.output
			)




	def test_ARPSniffing_raise(self):

		class TestSniffing(ARPSniffer):
			class loggy(LibraryContrib):

				handler		= self.LINKINDOR_HANDLER
				init_name	= "ARPSniffing_raise"
				init_level	= 10

		def raiser(*args, **kwargs): raise ValueError("The value is not enough")
		self.test_case = TestSniffing()
		with self.assertLogs("ARPSniffing_raise", 10) as case_loggy:
			self.assertIsNone(self.test_case(raiser))

		self.assertIn(

			f"DEBUG:ARPSniffing_raise:ARP trap failed due to ValueError: The value is not enough",
			case_loggy.output
		)








	def test_ARPRequestInspector_states(self):

		class Inspector(ARPRequestInspector):
			class filchmap(MaraudersMap): pass

		inspector = Inspector()
		inspector.filchmap(

			"10.10.0.1",
			{
				"MAC":	"12:34:56:78:9a:bc",
				"NAME":	"host-one",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"10.10.0.2",
			{
				"MAC":	"23:45:67:89:ab:cd",
				"NAME":	"host-two",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"10.10.0.3",
			{
				"MAC":	"34:56:78:9a:bc:de",
				"NAME":	"host-three",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"10.10.0.4",
			{
				"MAC":	"34:56:78:9a:bc:de",
				"NAME":	"host-three-two",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"12:34:56:78:9a:bc",
			{
				"IP4":	"10.10.0.1",
				"NAME":	"host-one",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		inspector.filchmap(

			"23:45:67:89:ab:cd",
			{
				"IP4":	"10.10.0.2",
				"NAME":	"host-two",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		inspector.filchmap(

			"34:56:78:9a:bc:de",
			{
				"IP4":	"10.10.0.3",
				"NAME":	"host-three",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		inspector.filchmap(

			"34:56:78:9a:bc:de",
			{
				"IP4":	"10.10.0.4",
				"NAME":	"host-three-two",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.3 (34:56:78:9a:bc:de)"),
			{
				"state":				509,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.4",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.5 (23:45:67:89:ab:cd)"),
			{
				"state":				996,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.2",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.2",
				"source MAC to name":	"host-two",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.5 (34:56:78:9a:bc:de)"),
			{
				"state":				996,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.4",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.1 says 0.0.0.0 (12:34:56:78:9a:bc)"),
			{
				"state":				998,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.1",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"12:34:56:78:9a:bc",
				"target ip4 to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 0.0.0.0 (34:56:78:9a:bc:de)"),
			{
				"state":				998,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.4",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.1 (23:45:67:89:ab:cd)"),
			{
				"state":				1021,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.2",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.2",
				"source MAC to name":	"host-two",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.5 says 10.10.0.1 (12:34:56:78:9a:bc)"),
			{
				"state":				1145,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.5",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.5 says 10.10.0.3 (34:56:78:9a:bc:de)"),
			{
				"state":				1145,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.5",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.5 says 10.10.0.4 (34:56:78:9a:bc:de)"),
			{
				"state":				1145,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.5",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.1 (12:34:56:78:9a:bc)"),
			{
				"state":				1533,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.2",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.1 says 10.10.0.4 (34:56:78:9a:bc:de)"),
			{
				"state":				1533,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.1",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"12:34:56:78:9a:bc",
				"target ip4 to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.1 says 10.10.0.3 (34:56:78:9a:bc:de)"),
			{
				"state":				1533,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.1",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"12:34:56:78:9a:bc",
				"target ip4 to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.4 (34:56:78:9a:bc:de)"),
			{
				"state":				1533,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.3",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.1 (12:34:56:78:9a:bc)"),
			{
				"state":				1533,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.3",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.1 (12:34:56:78:9a:bc)"),
			{
				"state":				1533,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.4",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 10.10.0.5 (01:23:45:67:89:ab)"),
			{
				"state":				1536,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.6",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 0.0.0.0 (01:23:45:67:89:ab)"),
			{
				"state":				1538,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.6",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 10.10.0.2 (01:23:45:67:89:ab)"),
			{
				"state":				1561,
				"source ip4":			"10.10.0.2",
				"target ip4":			"10.10.0.6",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 10.10.0.5 (23:45:67:89:ab:cd)"),
			{
				"state":				1632,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.6",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.2",
				"source MAC to name":	"host-two",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 10.10.0.5 (34:56:78:9a:bc:de)"),
			{
				"state":				1632,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.6",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 0.0.0.0 (23:45:67:89:ab:cd)"),
			{
				"state":				1634,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.6",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.2",
				"source MAC to name":	"host-two",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 10.10.0.1 (23:45:67:89:ab:cd)"),
			{
				"state":				1657,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.6",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.2",
				"source MAC to name":	"host-two",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.5 (01:23:45:67:89:ab)"),
			{
				"state":				1924,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.2",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.5 (01:23:45:67:89:ab)"),
			{
				"state":				1924,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.3",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.5 (01:23:45:67:89:ab)"),
			{
				"state":				1924,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.4",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 0.0.0.0 (01:23:45:67:89:ab)"),
			{
				"state":				1926,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.2",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 0.0.0.0 (01:23:45:67:89:ab)"),
			{
				"state":				1926,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.3",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 0.0.0.0 (01:23:45:67:89:ab)"),
			{
				"state":				1926,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.4",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.1 (01:23:45:67:89:ab)"),
			{
				"state":				1949,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.2",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.3 (01:23:45:67:89:ab)"),
			{
				"state":				1949,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.4",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.4 (01:23:45:67:89:ab)"),
			{
				"state":				1949,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.3",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.5 (12:34:56:78:9a:bc)"),
			{
				"state":				2020,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.2",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.5 (12:34:56:78:9a:bc)"),
			{
				"state":				2020,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.3",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.5 (34:56:78:9a:bc:de)"),
			{
				"state":				2020,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.3",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 0.0.0.0 (12:34:56:78:9a:bc)"),
			{
				"state":				2022,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.2",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 0.0.0.0 (34:56:78:9a:bc:de)"),
			{
				"state":				2022,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.3",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 0.0.0.0 (12:34:56:78:9a:bc)"),
			{
				"state":				2022,
				"source ip4":			"0.0.0.0",
				"target ip4":			"10.10.0.3",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.3 (12:34:56:78:9a:bc)"),
			{
				"state":				2045,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.2",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.1 (34:56:78:9a:bc:de)"),
			{
				"state":				2045,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.2",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.2 (12:34:56:78:9a:bc)"),
			{
				"state":				2045,
				"source ip4":			"10.10.0.2",
				"target ip4":			"10.10.0.3",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.3 (23:45:67:89:ab:cd)"),
			{
				"state":				2045,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.4",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.2",
				"source MAC to name":	"host-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.2 (12:34:56:78:9a:bc)"),
			{
				"state":				2045,
				"source ip4":			"10.10.0.2",
				"target ip4":			"10.10.0.4",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.4 (12:34:56:78:9a:bc)"),
			{
				"state":				2045,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.3",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.1 says 10.10.0.1 (12:34:56:78:9a:bc)"),
			{
				"state":				2557,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.1",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"12:34:56:78:9a:bc",
				"target ip4 to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.4 (34:56:78:9a:bc:de)"),
			{
				"state":				2557,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.4",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.3 (34:56:78:9a:bc:de)"),
			{
				"state":				3581,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.3",
				"source MAC":			"34:56:78:9a:bc:de",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.4",
				"source MAC to name":	"host-three-two",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.5 says 10.10.0.5 (01:23:45:67:89:ab)"),
			{
				"state":				3584,
				"source ip4":			"10.10.0.5",
				"target ip4":			"10.10.0.5",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.6 says 10.10.0.6 (12:34:56:78:9a:bc)"),
			{
				"state":				3680,
				"source ip4":			"10.10.0.6",
				"target ip4":			"10.10.0.6",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	None,
				"target ip4 to name":	None,
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.1 says 10.10.0.1 (01:23:45:67:89:ab)"),
			{
				"state":				3997,
				"source ip4":			"10.10.0.1",
				"target ip4":			"10.10.0.1",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"12:34:56:78:9a:bc",
				"target ip4 to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.4 (01:23:45:67:89:ab)"),
			{
				"state":				3997,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.4",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.3 (01:23:45:67:89:ab)"),
			{
				"state":				3997,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.3",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.2 says 10.10.0.2 (12:34:56:78:9a:bc)"),
			{
				"state":				4093,
				"source ip4":			"10.10.0.2",
				"target ip4":			"10.10.0.2",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"23:45:67:89:ab:cd",
				"target ip4 to name":	"host-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.4 says 10.10.0.4 (12:34:56:78:9a:bc)"),
			{
				"state":				4093,
				"source ip4":			"10.10.0.4",
				"target ip4":			"10.10.0.4",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three-two",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three-two",
			}
		)
		self.assertEqual(

			inspector("who has 10.10.0.3 says 10.10.0.3 (12:34:56:78:9a:bc)"),
			{
				"state":				4093,
				"source ip4":			"10.10.0.3",
				"target ip4":			"10.10.0.3",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"34:56:78:9a:bc:de",
				"source ip4 to name":	"host-three",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
				"target ip4 to MAC":	"34:56:78:9a:bc:de",
				"target ip4 to name":	"host-three",
			}
		)








	def test_ARPResponseInspector_states(self):

		class Inspector(ARPResponseInspector):
			class filchmap(MaraudersMap): pass

		inspector = Inspector()
		inspector.filchmap(

			"10.10.0.1",
			{
				"MAC":	"12:34:56:78:9a:bc",
				"NAME":	"host-one",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"10.10.0.2",
			{
				"MAC":	"23:45:67:89:ab:cd",
				"NAME":	"host-two",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"10.10.0.3",
			{
				"MAC":	"23:45:67:89:ab:cd",
				"NAME":	"host-two-two",
				"DESC":	"not necessary"
			},
			"IP4",
			mapped=False
		)
		inspector.filchmap(

			"12:34:56:78:9a:bc",
			{
				"IP4":	"10.10.0.1",
				"NAME":	"host-one",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		inspector.filchmap(

			"23:45:67:89:ab:cd",
			{
				"IP4":	"10.10.0.2",
				"NAME":	"host-two",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		inspector.filchmap(

			"23:45:67:89:ab:cd",
			{
				"IP4":	"10.10.0.3",
				"NAME":	"host-two-two",
				"DESC":	"not necessary"
			},
			"MAC",
			mapped=False
		)
		self.assertEqual(

			inspector("10.10.0.1", "12:34:56:78:9a:bc"),
			{
				"state":				63,
				"source ip4":			"10.10.0.1",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("10.10.0.3", "23:45:67:89:ab:cd"),
			{
				"state":				63,
				"source ip4":			"10.10.0.3",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two-two",
				"source MAC to ip4":	"10.10.0.3",
				"source MAC to name":	"host-two-two",
			}
		)
		self.assertEqual(

			inspector("10.10.0.2", "23:45:67:89:ab:cd"),
			{
				"state":				159,
				"source ip4":			"10.10.0.2",
				"source MAC":			"23:45:67:89:ab:cd",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two",
				"source MAC to ip4":	"10.10.0.3",
				"source MAC to name":	"host-two-two",
			}
		)
		self.assertEqual(

			inspector("10.10.0.1", "01:23:45:67:89:ab"),
			{
				"state":				199,
				"source ip4":			"10.10.0.1",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	"12:34:56:78:9a:bc",
				"source ip4 to name":	"host-one",
				"source MAC to ip4":	None,
				"source MAC to name":	None,
			}
		)
		self.assertEqual(

			inspector("10.10.0.4", "12:34:56:78:9a:bc"),
			{
				"state":				216,
				"source ip4":			"10.10.0.4",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("10.10.0.2", "12:34:56:78:9a:bc"),
			{
				"state":				223,
				"source ip4":			"10.10.0.2",
				"source MAC":			"12:34:56:78:9a:bc",
				"source ip4 to MAC":	"23:45:67:89:ab:cd",
				"source ip4 to name":	"host-two",
				"source MAC to ip4":	"10.10.0.1",
				"source MAC to name":	"host-one",
			}
		)
		self.assertEqual(

			inspector("10.10.0.5", "01:23:45:67:89:ab"),
			{
				"state":				224,
				"source ip4":			"10.10.0.5",
				"source MAC":			"01:23:45:67:89:ab",
				"source ip4 to MAC":	None,
				"source ip4 to name":	None,
				"source MAC to ip4":	None,
				"source MAC to name":	None,
			}
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







