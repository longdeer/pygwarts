import	os
import	unittest
from	pygwarts.tests.filch					import FilchTestCase
from	pygwarts.irma.contrib					import LibraryContrib
from	pygwarts.filch.transportclaw			import is_valid_port
from	pygwarts.filch.transportclaw			import validate_port
from	pygwarts.filch.transportclaw.scanning	import PortScanner








class TransportclawCase(FilchTestCase):

	"""
		Testing L4 instruments
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.TRNSPRTCLAW_HANDLER): os.remove(cls.TRNSPRTCLAW_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.TRNSPRTCLAW_HANDLER)
	def test_is_valid_port_valid(self):

		for number in range(65536):
			with self.subTest(port=number): self.assertTrue(is_valid_port(number))


	def test_is_valid_port_invalid_1(self):

		for number in range(65536):
			for port in float(number), str(number), str(float(number)):
				with self.subTest(port=port): self.assertFalse(is_valid_port(port))


	def test_is_valid_port_invalid_2(self):

		for invalid in (

			-1, -1., "-1", "-1.", 65536, 65536., "65536", "65536.",
			True, False, None, ..., print, unittest,[ 42 ],( 42, ),{ 42 },{ "port": 42 }
		):
			with self.subTest(port=invalid): self.assertFalse(is_valid_port(invalid))




	def test_validate_port_valid(self):

		for number in range(65536):
			for port in number, float(number), str(number), str(float(number)):
				with self.subTest(port=port): self.assertEqual(validate_port(port), number)


	def test_validate_port_invalid(self):
		for invalid in (

			-1, -1., "-1", "-1.", 65536, 65536., "65536", "65536.",
			True, False, None, ..., print, unittest,[ 42 ],( 42, ),{ 42 },{ "port": 42 }
		):
			self.assertIsNone(validate_port(invalid))








	def test_PortScanner(self):

		class TestScanner(PortScanner):
			class loggy(LibraryContrib):

				handler		= self.TRNSPRTCLAW_HANDLER
				init_name	= "PortScanner"
				init_level	= 10

		self.test_case = TestScanner()

		with self.assertLogs("PortScanner", 10) as case_loggy:
			current = self.test_case("127.0.0.1", 80)

		self.assertIn("DEBUG:PortScanner:Scanning 127.0.0.1:80", case_loggy.output)
		try:

			self.assertTrue(current)
			self.assertIn("INFO:PortScanner:127.0.0.1:80 listening", case_loggy.output)
		except:
			self.assertFalse(current)
			self.assertIn(

				"DEBUG:PortScanner:Socket write error %s"%(111 if os.name == "posix" else 10061),
				case_loggy.output
			)




	def test_PortScanner_invalid_ip(self):

		class TestScanner(PortScanner):
			class loggy(LibraryContrib):

				handler		= self.TRNSPRTCLAW_HANDLER
				init_name	= "PortScanner_invalid_ip"
				init_level	= 10

		self.test_case = TestScanner()
		for invalid in (

			"10.10.10.300", "LOL", 42, 69., True, False, None, ..., print, PortScanner,
			[ "10.10.10.10" ],( "10.10.10.10", ),{ "10.10.10.10" },{ "target": "10.10.10.10" }
		):
			with self.subTest(target=invalid):
				with self.assertLogs("PortScanner_invalid_ip", 10) as case_loggy:

					self.assertIsNone(self.test_case(invalid, 80))
			self.assertIn(f"DEBUG:PortScanner_invalid_ip:Invalid target \"{invalid}\"", case_loggy.output)




	def test_PortScanner_invalid_port(self):

		class TestScanner(PortScanner):
			class loggy(LibraryContrib):

				handler		= self.TRNSPRTCLAW_HANDLER
				init_name	= "PortScanner_invalid_port"
				init_level	= 10

		self.test_case = TestScanner()
		for invalid in (

			"80", "LOL", 80., True, False, None, ..., print, PortScanner,
			[ 80 ],( 80, ),{ 80 },{ "port": 80 }
		):
			with self.subTest(port=invalid):
				with self.assertLogs("PortScanner_invalid_port", 10) as case_loggy:

					self.assertIsNone(self.test_case("127.0.0.1", invalid))
			self.assertIn(f"DEBUG:PortScanner_invalid_port:Invalid port \"{invalid}\"", case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







