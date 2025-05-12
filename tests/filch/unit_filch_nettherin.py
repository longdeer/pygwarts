import	os
import	unittest
from	random							import choice
from	ipaddress						import ip_network
from	pygwarts.tests.filch			import FilchTestCase
from	pygwarts.irma.contrib			import LibraryContrib
from	pygwarts.filch.nettherin		import P_VALID_IP4
from	pygwarts.filch.nettherin		import GP_VALID_IP4
from	pygwarts.filch.nettherin		import is_valid_ip4
from	pygwarts.filch.nettherin		import validate_ip4
from	pygwarts.filch.nettherin.icmp	import HostPing








class NettherinCase(FilchTestCase):

	"""
		Testing L3 instruments
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.NETTHERIN_HANDLER): os.remove(cls.NETTHERIN_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.NETTHERIN_HANDLER)
	def test_P_VALID_IP4_valid(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):
					for o4 in ( choice(self.valid_IP_chars) for _ in range(10) ):

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}.{str(o4).zfill(2)}"
						v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}.{str(o4).zfill(3)}"

						with self.subTest(ip=v1): self.assertTrue(P_VALID_IP4.fullmatch(v1))
						with self.subTest(ip=v2): self.assertTrue(P_VALID_IP4.fullmatch(v2))
						with self.subTest(ip=v3): self.assertTrue(P_VALID_IP4.fullmatch(v3))




	def test_P_VALID_IP4_invalid_1_octet(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):

			v1 = f"{o1}"
			v2 = f"{str(o1).zfill(2)}"
			v3 = f"{str(o1).zfill(3)}"

			with self.subTest(ip=v1): self.assertFalse(P_VALID_IP4.fullmatch(v1))
			with self.subTest(ip=v2): self.assertFalse(P_VALID_IP4.fullmatch(v2))
			with self.subTest(ip=v3): self.assertFalse(P_VALID_IP4.fullmatch(v3))




	def test_P_VALID_IP4_invalid_2_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):

				v1 = f"{o1}.{o2}"
				v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}"
				v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}"

				with self.subTest(ip=v1): self.assertFalse(P_VALID_IP4.fullmatch(v1))
				with self.subTest(ip=v2): self.assertFalse(P_VALID_IP4.fullmatch(v2))
				with self.subTest(ip=v3): self.assertFalse(P_VALID_IP4.fullmatch(v3))




	def test_P_VALID_IP4_invalid_3_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):

						v1 = f"{o1}.{o2}.{o3}"
						v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}"
						v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}"

						with self.subTest(ip=v1): self.assertFalse(P_VALID_IP4.fullmatch(v1))
						with self.subTest(ip=v2): self.assertFalse(P_VALID_IP4.fullmatch(v2))
						with self.subTest(ip=v3): self.assertFalse(P_VALID_IP4.fullmatch(v3))




	def test_P_VALID_IP4_invalid(self):

		for o1 in 1, 420, 128., "LOL", True, False, None, ..., print:
			for o2 in 1, 420, 128., "LOL", True, False, None, ..., print:
				for o3 in 1, 420, 128., "LOL", True, False, None, ..., print:
					for o4 in 420, 128., "LOL", True, False, None, ..., print:

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						with self.subTest(ip=v1): self.assertFalse(P_VALID_IP4.fullmatch(v1))








	def test_GP_VALID_IP4_valid(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):
					for o4 in ( choice(self.valid_IP_chars) for _ in range(10) ):

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}.{str(o4).zfill(2)}"
						v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}.{str(o4).zfill(3)}"

						with self.subTest(ip=v1):

							match = GP_VALID_IP4.fullmatch(v1)
							O1,O2,O3,O4 = match.group("octet1", "octet2", "octet3", "octet4")
							self.assertEqual(int(O1),o1)
							self.assertEqual(int(O2),o2)
							self.assertEqual(int(O3),o3)
							self.assertEqual(int(O4),o4)

						with self.subTest(ip=v2):

							match = GP_VALID_IP4.fullmatch(v2)
							O1,O2,O3,O4 = match.group("octet1", "octet2", "octet3", "octet4")
							self.assertEqual(int(O1),o1)
							self.assertEqual(int(O2),o2)
							self.assertEqual(int(O3),o3)
							self.assertEqual(int(O4),o4)

						with self.subTest(ip=v3):

							match = GP_VALID_IP4.fullmatch(v3)
							O1,O2,O3,O4 = match.group("octet1", "octet2", "octet3", "octet4")
							self.assertEqual(int(O1),o1)
							self.assertEqual(int(O2),o2)
							self.assertEqual(int(O3),o3)
							self.assertEqual(int(O4),o4)




	def test_GP_VALID_IP4_invalid_1_octet(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):

			v1 = f"{o1}"
			v2 = f"{str(o1).zfill(2)}"
			v3 = f"{str(o1).zfill(3)}"

			with self.subTest(ip=v1): self.assertFalse(GP_VALID_IP4.fullmatch(v1))
			with self.subTest(ip=v2): self.assertFalse(GP_VALID_IP4.fullmatch(v2))
			with self.subTest(ip=v3): self.assertFalse(GP_VALID_IP4.fullmatch(v3))




	def test_GP_VALID_IP4_invalid_2_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):

				v1 = f"{o1}.{o2}"
				v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}"
				v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}"

				with self.subTest(ip=v1): self.assertFalse(GP_VALID_IP4.fullmatch(v1))
				with self.subTest(ip=v2): self.assertFalse(GP_VALID_IP4.fullmatch(v2))
				with self.subTest(ip=v3): self.assertFalse(GP_VALID_IP4.fullmatch(v3))




	def test_GP_VALID_IP4_invalid_3_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):

					v1 = f"{o1}.{o2}.{o3}"
					v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}"
					v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}"

					with self.subTest(ip=v1): self.assertFalse(GP_VALID_IP4.fullmatch(v1))
					with self.subTest(ip=v2): self.assertFalse(GP_VALID_IP4.fullmatch(v2))
					with self.subTest(ip=v3): self.assertFalse(GP_VALID_IP4.fullmatch(v3))




	def test_GP_VALID_IP4_invalid(self):

		for o1 in 1, 420, 128., "LOL", True, False, None, ..., print:
			for o2 in 1, 420, 128., "LOL", True, False, None, ..., print:
				for o3 in 1, 420, 128., "LOL", True, False, None, ..., print:
					for o4 in 420, 128., "LOL", True, False, None, ..., print:

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						with self.subTest(ip=v1): self.assertFalse(GP_VALID_IP4.fullmatch(v1))








	def test_is_valid_ip4_valid(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):
					for o4 in ( choice(self.valid_IP_chars) for _ in range(10) ):

						with self.subTest(ip=(v1 := f"{o1}.{o2}.{o3}.{o4}")):
							self.assertTrue(is_valid_ip4(v1))




	def test_is_valid_ip4_invalid_1_octet(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):

			v1 = f"{o1}"
			v2 = f"{str(o1).zfill(2)}"
			v3 = f"{str(o1).zfill(3)}"

			with self.subTest(ip=v1): self.assertFalse(is_valid_ip4(v1))
			with self.subTest(ip=v2): self.assertFalse(is_valid_ip4(v2))
			with self.subTest(ip=v3): self.assertFalse(is_valid_ip4(v3))




	def test_is_valid_ip4_invalid_2_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):

				v1 = f"{o1}.{o2}"
				v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}"
				v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}"

				with self.subTest(ip=v1): self.assertFalse(is_valid_ip4(v1))
				with self.subTest(ip=v2): self.assertFalse(is_valid_ip4(v2))
				with self.subTest(ip=v3): self.assertFalse(is_valid_ip4(v3))




	def test_is_valid_ip4_invalid_3_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):

					v1 = f"{o1}.{o2}.{o3}"
					v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}"
					v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}"

					with self.subTest(ip=v1): self.assertFalse(is_valid_ip4(v1))
					with self.subTest(ip=v2): self.assertFalse(is_valid_ip4(v2))
					with self.subTest(ip=v3): self.assertFalse(is_valid_ip4(v3))




	def test_is_valid_ip4_invalid_4_octets(self):

		for o1 in range(10):
			for o2 in range(10):
				for o3 in range(10):
					for o4 in range(10):

						v1 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}.{str(o4).zfill(2)}"
						v2 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}.{str(o4).zfill(3)}"

						with self.subTest(ip=v1): self.assertFalse(is_valid_ip4(v1))
						with self.subTest(ip=v2): self.assertFalse(is_valid_ip4(v2))




	def test_is_valid_ip4_invalid(self):

		for o1 in 1, 420, 128., "LOL", True, False, None, ..., print:
			for o2 in 1, 420, 128., "LOL", True, False, None, ..., print:
				for o3 in 1, 420, 128., "LOL", True, False, None, ..., print:
					for o4 in 420, 128., "LOL", True, False, None, ..., print:

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						with self.subTest(ip=v1): self.assertFalse(is_valid_ip4(v1))








	def test_validate_ip4_valid(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):
					for o4 in ( choice(self.valid_IP_chars) for _ in range(10) ):

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}.{str(o4).zfill(2)}"
						v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}.{str(o4).zfill(3)}"

						with self.subTest(ip=v1): self.assertEqual(validate_ip4(v1),v1)
						with self.subTest(ip=v2): self.assertEqual(validate_ip4(v2),v1)
						with self.subTest(ip=v3): self.assertEqual(validate_ip4(v3),v1)




	def test_validate_ip4_invalid_1_octet(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):

			v1 = f"{o1}"
			v2 = f"{str(o1).zfill(2)}"
			v3 = f"{str(o1).zfill(3)}"

			with self.subTest(ip=v1): self.assertIsNone(validate_ip4(v1))
			with self.subTest(ip=v2): self.assertIsNone(validate_ip4(v2))
			with self.subTest(ip=v3): self.assertIsNone(validate_ip4(v3))




	def test_validate_ip4_invalid_2_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):

				v1 = f"{o1}.{o2}"
				v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}"
				v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}"

				with self.subTest(ip=v1): self.assertIsNone(validate_ip4(v1))
				with self.subTest(ip=v2): self.assertIsNone(validate_ip4(v2))
				with self.subTest(ip=v3): self.assertIsNone(validate_ip4(v3))




	def test_validate_ip4_invalid_3_octets(self):

		for o1 in ( choice(self.valid_IP_chars) for _ in range(10) ):
			for o2 in ( choice(self.valid_IP_chars) for _ in range(10) ):
				for o3 in ( choice(self.valid_IP_chars) for _ in range(10) ):

					v1 = f"{o1}.{o2}.{o3}"
					v2 = f"{str(o1).zfill(2)}.{str(o2).zfill(2)}.{str(o3).zfill(2)}"
					v3 = f"{str(o1).zfill(3)}.{str(o2).zfill(3)}.{str(o3).zfill(3)}"

					with self.subTest(ip=v1): self.assertIsNone(validate_ip4(v1))
					with self.subTest(ip=v2): self.assertIsNone(validate_ip4(v2))
					with self.subTest(ip=v3): self.assertIsNone(validate_ip4(v3))




	def test_validate_ip4_invalid(self):

		for o1 in 1, 420, 128., "LOL", True, False, None, ..., print:
			for o2 in 1, 420, 128., "LOL", True, False, None, ..., print:
				for o3 in 1, 420, 128., "LOL", True, False, None, ..., print:
					for o4 in 420, 128., "LOL", True, False, None, ..., print:

						v1 = f"{o1}.{o2}.{o3}.{o4}"
						with self.subTest(ip=v1): self.assertIsNone(validate_ip4(v1))








	def test_HostPing(self):

		# Host ping packet builder example. Will try to send an ICMP echo request from some ip4 and
		# some interface with target ip4 address specified, and receive an answer.
		# It is assumed scappy 2.5.0rc3 installed, as was originally desinged.

		class TestPing(HostPing):
			class loggy(LibraryContrib):

				handler		= self.NETTHERIN_HANDLER
				init_name	= "HostPing"
				init_level	= 10

		self.test_case = TestPing()

		try:

			from scapy.all	import sr
			from scapy.all	import IP
			from scapy.all	import ICMP

			target = ""	# to be filled with real ip4 address to be checked
			assert len(target)

			def pinger(addr, **kwargs):

				R = sr(IP(dst=target) /ICMP(), **kwargs)
				if len(R) and len(R[0]): return R[0][0]

		except	(ImportError, AssertionError) as E:

			target = "10.10.10.10"
			def pinger(*args, **kwargs): return 42

		self.assertIsNotNone(self.test_case(target, pinger, verbose=0, timeout=1))




	def test_HostPing_invalid_ip(self):

		class TestPing(HostPing):
			class loggy(LibraryContrib):

				handler		= self.NETTHERIN_HANDLER
				init_name	= "HostPing_invalid_ip"
				init_level	= 10

		self.test_case = TestPing()
		for invalid in (

			"10.10.10.300", "LOL", 42, 69., True, False, None, ..., print, HostPing,
			[ "10.10.10.10" ],( "10.10.10.10", ),{ "10.10.10.10" },{ "target": "10.10.10.10" }
		):
			with self.subTest(ip=invalid):
				with self.assertLogs("HostPing_invalid_ip", 10) as case_loggy:

					self.assertIsNone(self.test_case(invalid, lambda : None))
			self.assertIn(
				f"DEBUG:HostPing_invalid_ip:Invalid IP4 address \"{invalid}\"", case_loggy.output
			)




	def test_HostPing_invalid_pinger(self):

		class TestPing(HostPing):
			class loggy(LibraryContrib):

				handler		= self.NETTHERIN_HANDLER
				init_name	= "HostPing_invalid_pinger"
				init_level	= 10

		self.test_case = TestPing()
		for invalid in (

			"LOL", 42, 69., True, False, None, ..., unittest,
			[ print ],( print, ),{ print },{ "pinger": print }
		):
			with self.subTest(pinger=invalid):
				with self.assertLogs("HostPing_invalid_pinger", 10) as case_loggy:

					self.assertIsNone(self.test_case("10.10.10.10", invalid))
			self.assertIn(

				f"DEBUG:HostPing_invalid_pinger:Invalid pinger \"{invalid}\"",
				case_loggy.output
			)




	def test_HostPing_raise(self):

		class TestPing(HostPing):
			class loggy(LibraryContrib):

				handler		= self.NETTHERIN_HANDLER
				init_name	= "HostPing_raise"
				init_level	= 10

		def raiser(*args, **kwargs): raise ValueError("The value is not enough")
		self.test_case = TestPing()
		with self.assertLogs("HostPing_raise", 10) as case_loggy:
			self.assertIsNone(self.test_case("10.10.10.10", raiser))

		self.assertIn(

			f"DEBUG:HostPing_raise:Ping failed due to ValueError: The value is not enough",
			case_loggy.output
		)




	def test_PoolPing(self):

		class TestPing(HostPing):
			class loggy(LibraryContrib):

				handler		= self.NETTHERIN_HANDLER
				init_name	= "PoolPing"
				init_level	= 10

		def pinger(*args, **kwargs): return not None
		self.test_case = TestPing()

		for ip4 in list(ip_network("192.168.0.0/24"))[1:-1]:
			self.assertIsNotNone(self.test_case(str(ip4), pinger))








if __name__ == "__main__" : unittest.main(verbosity=2)







