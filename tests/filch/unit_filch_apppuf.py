import	os
import	unittest
from	pygwarts.tests.filch		import FilchTestCase
from	pygwarts.irma.contrib		import LibraryContrib
from	pygwarts.filch.apppuf.snmp	import SNMPtrap








class ApppufCase(FilchTestCase):

	"""
		Testing L5 instruments
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.APPPUF_HANDLER): os.remove(cls.APPPUF_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.APPPUF_HANDLER)
	def test_SNMPtrap(self):

		class TestListener(SNMPtrap):
			class loggy(LibraryContrib):

				handler		= self.APPPUF_HANDLER
				init_name	= "SNMPtrap"
				init_level	= 10

		self.test_case = TestListener()

		with self.assertLogs("SNMPtrap", 10) as case_loggy:
			self.test_case(

				"127.0.0.11", 54321,
				lambda *args, **kwargs : None,
				listen_timer=42,
			)

		self.assertIn("INFO:SNMPtrap:Establishing SNMP trap at 127.0.0.11:54321", case_loggy.output)
		self.assertIn("DEBUG:SNMPtrap:Using listen_timer: 42", case_loggy.output)
		self.assertIn("INFO:SNMPtrap:127.0.0.11:54321 SNMP trap discarded", case_loggy.output)




	def test_SNMPtrap_invalid_ip(self):

		class TestListener(SNMPtrap):
			class loggy(LibraryContrib):

				handler		= self.APPPUF_HANDLER
				init_name	= "SNMPtrap_invalid_ip"
				init_level	= 10

		self.test_case = TestListener()

		with self.assertLogs("SNMPtrap_invalid_ip", 10) as case_loggy:
			self.test_case("127.0.0.311", 54321, lambda *args : None)

		self.assertIn("DEBUG:SNMPtrap_invalid_ip:Listen ip verification failed", case_loggy.output)




	def test_SNMPtrap_invalid_port(self):

		class TestListener(SNMPtrap):
			class loggy(LibraryContrib):

				handler		= self.APPPUF_HANDLER
				init_name	= "SNMPtrap_invalid_port"
				init_level	= 10

		self.test_case = TestListener()

		with self.assertLogs("SNMPtrap_invalid_port", 10) as case_loggy:
			self.test_case("127.0.0.11", 543211, lambda *args : None)

		self.assertIn("DEBUG:SNMPtrap_invalid_port:Listen port verification failed", case_loggy.output)




	def test_SNMPtrap_raise(self):

		class TestListener(SNMPtrap):
			class loggy(LibraryContrib):

				handler		= self.APPPUF_HANDLER
				init_name	= "SNMPtrap_raise"
				init_level	= 10

		def fake_trap(*args): raise ValueError("Enough of this")
		self.test_case = TestListener()

		with self.assertLogs("SNMPtrap_raise", 10) as case_loggy:
			self.test_case("127.0.0.11", 54321, fake_trap)

		self.assertIn(
			f"ERROR:SNMPtrap_raise:{self.test_case} got ValueError: Enough of this", case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







