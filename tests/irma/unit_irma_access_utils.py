import	os
import	unittest
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.irma					import IrmaTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access.utils			import byte_size_string
from	pygwarts.irma.access.utils			import WriteWrapper








class AccessUtilsCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_UTILS): os.remove(cls.ACCESS_UTILS)

		if	os.path.isfile(cls.wwpath): os.remove(cls.wwpath)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.ACCESS_UTILS)
		cls.wwpath = str(cls.IRMA_ROOT /"ww.txt")


	def test_number_byte_size_string(self):

		self.assertEqual(byte_size_string(0), "0B")
		self.assertEqual(byte_size_string(1), "1B")
		self.assertEqual(byte_size_string(9), "9B")
		self.assertEqual(byte_size_string(10), "10B")
		self.assertEqual(byte_size_string(99), "99B")
		self.assertEqual(byte_size_string(100), "100B")
		self.assertEqual(byte_size_string(999), "999B")
		self.assertEqual(byte_size_string(1000), "1K")
		self.assertEqual(byte_size_string(1001), "1K 1B")
		self.assertEqual(byte_size_string(1009), "1K 9B")
		self.assertEqual(byte_size_string(1099), "1K 99B")
		self.assertEqual(byte_size_string(1100), "1K 100B")
		self.assertEqual(byte_size_string(1999), "1K 999B")
		self.assertEqual(byte_size_string(99999), "99K 999B")
		self.assertEqual(byte_size_string(999999), "999K 999B")
		self.assertEqual(byte_size_string(9999999), "9M 999K 999B")
		self.assertEqual(byte_size_string(99999999), "99M 999K 999B")
		self.assertEqual(byte_size_string(999999999), "999M 999K 999B")
		self.assertEqual(byte_size_string(9999999999), "9G 999M 999K 999B")
		self.assertEqual(byte_size_string(99999999999), "99G 999M 999K 999B")
		self.assertEqual(byte_size_string(999999999999), "999G 999M 999K 999B")
		self.assertEqual(byte_size_string(9999999999999), "9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(99999999999999), "99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(999999999999999), "999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string(0.9), "0B")
		self.assertEqual(byte_size_string(1.9), "1B")
		self.assertEqual(byte_size_string(9.9), "9B")
		self.assertEqual(byte_size_string(10.9), "10B")
		self.assertEqual(byte_size_string(99.9), "99B")
		self.assertEqual(byte_size_string(100.9), "100B")
		self.assertEqual(byte_size_string(999.9), "999B")
		self.assertEqual(byte_size_string(1000.9), "1K")
		self.assertEqual(byte_size_string(1001.9), "1K 1B")
		self.assertEqual(byte_size_string(1009.9), "1K 9B")
		self.assertEqual(byte_size_string(1099.9), "1K 99B")
		self.assertEqual(byte_size_string(1100.9), "1K 100B")
		self.assertEqual(byte_size_string(1999.9), "1K 999B")
		self.assertEqual(byte_size_string(99999.9), "99K 999B")
		self.assertEqual(byte_size_string(999999.9), "999K 999B")
		self.assertEqual(byte_size_string(9999999.9), "9M 999K 999B")
		self.assertEqual(byte_size_string(99999999.9), "99M 999K 999B")
		self.assertEqual(byte_size_string(999999999.9), "999M 999K 999B")
		self.assertEqual(byte_size_string(9999999999.9), "9G 999M 999K 999B")
		self.assertEqual(byte_size_string(99999999999.9), "99G 999M 999K 999B")
		self.assertEqual(byte_size_string(999999999999.9), "999G 999M 999K 999B")
		self.assertEqual(byte_size_string(9999999999999.9), "9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(99999999999999.9), "99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(999999999999999.9), "999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string(.0), "0B")
		self.assertEqual(byte_size_string(.1), "0B")
		self.assertEqual(byte_size_string(.9), "0B")
		self.assertEqual(byte_size_string(.10), "0B")
		self.assertEqual(byte_size_string(.99), "0B")
		self.assertEqual(byte_size_string(.100), "0B")
		self.assertEqual(byte_size_string(.999), "0B")
		self.assertEqual(byte_size_string(.1000), "0B")
		self.assertEqual(byte_size_string(.1001), "0B")
		self.assertEqual(byte_size_string(.1009), "0B")
		self.assertEqual(byte_size_string(.1099), "0B")
		self.assertEqual(byte_size_string(.1100), "0B")
		self.assertEqual(byte_size_string(.1999), "0B")
		self.assertEqual(byte_size_string(.99999), "0B")
		self.assertEqual(byte_size_string(.999999), "0B")
		self.assertEqual(byte_size_string(.9999999), "0B")
		self.assertEqual(byte_size_string(.99999999), "0B")
		self.assertEqual(byte_size_string(.999999999), "0B")
		self.assertEqual(byte_size_string(.9999999999), "0B")
		self.assertEqual(byte_size_string(.99999999999), "0B")
		self.assertEqual(byte_size_string(.999999999999), "0B")
		self.assertEqual(byte_size_string(.9999999999999), "0B")
		self.assertEqual(byte_size_string(.99999999999999), "0B")
		self.assertEqual(byte_size_string(.999999999999999), "0B")

	def test_string_byte_size_string(self):

		self.assertEqual(byte_size_string("0"), "0B")
		self.assertEqual(byte_size_string("1"), "1B")
		self.assertEqual(byte_size_string("9"), "9B")
		self.assertEqual(byte_size_string("10"), "10B")
		self.assertEqual(byte_size_string("99"), "99B")
		self.assertEqual(byte_size_string("100"), "100B")
		self.assertEqual(byte_size_string("999"), "999B")
		self.assertEqual(byte_size_string("1000"), "1K")
		self.assertEqual(byte_size_string("1001"), "1K 1B")
		self.assertEqual(byte_size_string("1009"), "1K 9B")
		self.assertEqual(byte_size_string("1099"), "1K 99B")
		self.assertEqual(byte_size_string("1100"), "1K 100B")
		self.assertEqual(byte_size_string("1999"), "1K 999B")
		self.assertEqual(byte_size_string("99999"), "99K 999B")
		self.assertEqual(byte_size_string("999999"), "999K 999B")
		self.assertEqual(byte_size_string("9999999"), "9M 999K 999B")
		self.assertEqual(byte_size_string("99999999"), "99M 999K 999B")
		self.assertEqual(byte_size_string("999999999"), "999M 999K 999B")
		self.assertEqual(byte_size_string("9999999999"), "9G 999M 999K 999B")
		self.assertEqual(byte_size_string("99999999999"), "99G 999M 999K 999B")
		self.assertEqual(byte_size_string("999999999999"), "999G 999M 999K 999B")
		self.assertEqual(byte_size_string("9999999999999"), "9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("99999999999999"), "99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("0999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("000999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("0000999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("000000999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("0000000999999999999999"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000000999999999999999"), "999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string("0.9"), "0B")
		self.assertEqual(byte_size_string("1.9"), "1B")
		self.assertEqual(byte_size_string("9.9"), "9B")
		self.assertEqual(byte_size_string("10.9"), "10B")
		self.assertEqual(byte_size_string("99.9"), "99B")
		self.assertEqual(byte_size_string("100.9"), "100B")
		self.assertEqual(byte_size_string("999.9"), "999B")
		self.assertEqual(byte_size_string("1000.9"), "1K")
		self.assertEqual(byte_size_string("1001.9"), "1K 1B")
		self.assertEqual(byte_size_string("1009.9"), "1K 9B")
		self.assertEqual(byte_size_string("1099.9"), "1K 99B")
		self.assertEqual(byte_size_string("1100.9"), "1K 100B")
		self.assertEqual(byte_size_string("1999.9"), "1K 999B")
		self.assertEqual(byte_size_string("99999.9"), "99K 999B")
		self.assertEqual(byte_size_string("999999.9"), "999K 999B")
		self.assertEqual(byte_size_string("9999999.9"), "9M 999K 999B")
		self.assertEqual(byte_size_string("99999999.9"), "99M 999K 999B")
		self.assertEqual(byte_size_string("999999999.9"), "999M 999K 999B")
		self.assertEqual(byte_size_string("9999999999.9"), "9G 999M 999K 999B")
		self.assertEqual(byte_size_string("99999999999.9"), "99G 999M 999K 999B")
		self.assertEqual(byte_size_string("999999999999.9"), "999G 999M 999K 999B")
		self.assertEqual(byte_size_string("9999999999999.9"), "9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("99999999999999.9"), "99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("999999999999999.9"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("0999999999999999.9"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00999999999999999.9"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("000999999999999999.9"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("0000999999999999999.9"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999.9"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999.90"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999.900"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999.9000"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999.90000"), "999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("00000999999999999999.900000"), "999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string(".0"), "0B")
		self.assertEqual(byte_size_string(".1"), "0B")
		self.assertEqual(byte_size_string(".9"), "0B")
		self.assertEqual(byte_size_string(".10"), "0B")
		self.assertEqual(byte_size_string(".99"), "0B")
		self.assertEqual(byte_size_string(".100"), "0B")
		self.assertEqual(byte_size_string(".999"), "0B")
		self.assertEqual(byte_size_string(".1000"), "0B")
		self.assertEqual(byte_size_string(".1001"), "0B")
		self.assertEqual(byte_size_string(".1009"), "0B")
		self.assertEqual(byte_size_string(".1099"), "0B")
		self.assertEqual(byte_size_string(".1100"), "0B")
		self.assertEqual(byte_size_string(".1999"), "0B")
		self.assertEqual(byte_size_string(".99999"), "0B")
		self.assertEqual(byte_size_string(".999999"), "0B")
		self.assertEqual(byte_size_string(".9999999"), "0B")
		self.assertEqual(byte_size_string(".99999999"), "0B")
		self.assertEqual(byte_size_string(".999999999"), "0B")
		self.assertEqual(byte_size_string(".9999999999"), "0B")
		self.assertEqual(byte_size_string(".99999999999"), "0B")
		self.assertEqual(byte_size_string(".999999999999"), "0B")
		self.assertEqual(byte_size_string(".9999999999999"), "0B")
		self.assertEqual(byte_size_string(".99999999999999"), "0B")
		self.assertEqual(byte_size_string(".999999999999999"), "0B")
		self.assertEqual(byte_size_string("0.999999999999999"), "0B")
		self.assertEqual(byte_size_string("00.999999999999999"), "0B")
		self.assertEqual(byte_size_string("000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("0000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("00000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("000000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("0000000.999999999999999"), "0B")

	def test_negative_number_byte_size_string(self):

		self.assertEqual(byte_size_string(-0), "0B")
		self.assertEqual(byte_size_string(-1), "-1B")
		self.assertEqual(byte_size_string(-9), "-9B")
		self.assertEqual(byte_size_string(-10), "-10B")
		self.assertEqual(byte_size_string(-99), "-99B")
		self.assertEqual(byte_size_string(-100), "-100B")
		self.assertEqual(byte_size_string(-999), "-999B")
		self.assertEqual(byte_size_string(-1000), "-1K")
		self.assertEqual(byte_size_string(-1001), "-1K 1B")
		self.assertEqual(byte_size_string(-1009), "-1K 9B")
		self.assertEqual(byte_size_string(-1099), "-1K 99B")
		self.assertEqual(byte_size_string(-1100), "-1K 100B")
		self.assertEqual(byte_size_string(-1999), "-1K 999B")
		self.assertEqual(byte_size_string(-99999), "-99K 999B")
		self.assertEqual(byte_size_string(-999999), "-999K 999B")
		self.assertEqual(byte_size_string(-9999999), "-9M 999K 999B")
		self.assertEqual(byte_size_string(-99999999), "-99M 999K 999B")
		self.assertEqual(byte_size_string(-999999999), "-999M 999K 999B")
		self.assertEqual(byte_size_string(-9999999999), "-9G 999M 999K 999B")
		self.assertEqual(byte_size_string(-99999999999), "-99G 999M 999K 999B")
		self.assertEqual(byte_size_string(-999999999999), "-999G 999M 999K 999B")
		self.assertEqual(byte_size_string(-9999999999999), "-9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(-99999999999999), "-99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(-999999999999999), "-999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string(-0.9), "0B")
		self.assertEqual(byte_size_string(-1.9), "-1B")
		self.assertEqual(byte_size_string(-9.9), "-9B")
		self.assertEqual(byte_size_string(-10.9), "-10B")
		self.assertEqual(byte_size_string(-99.9), "-99B")
		self.assertEqual(byte_size_string(-100.9), "-100B")
		self.assertEqual(byte_size_string(-999.9), "-999B")
		self.assertEqual(byte_size_string(-1000.9), "-1K")
		self.assertEqual(byte_size_string(-1001.9), "-1K 1B")
		self.assertEqual(byte_size_string(-1009.9), "-1K 9B")
		self.assertEqual(byte_size_string(-1099.9), "-1K 99B")
		self.assertEqual(byte_size_string(-1100.9), "-1K 100B")
		self.assertEqual(byte_size_string(-1999.9), "-1K 999B")
		self.assertEqual(byte_size_string(-99999.9), "-99K 999B")
		self.assertEqual(byte_size_string(-999999.9), "-999K 999B")
		self.assertEqual(byte_size_string(-9999999.9), "-9M 999K 999B")
		self.assertEqual(byte_size_string(-99999999.9), "-99M 999K 999B")
		self.assertEqual(byte_size_string(-999999999.9), "-999M 999K 999B")
		self.assertEqual(byte_size_string(-9999999999.9), "-9G 999M 999K 999B")
		self.assertEqual(byte_size_string(-99999999999.9), "-99G 999M 999K 999B")
		self.assertEqual(byte_size_string(-999999999999.9), "-999G 999M 999K 999B")
		self.assertEqual(byte_size_string(-9999999999999.9), "-9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(-99999999999999.9), "-99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string(-999999999999999.9), "-999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string(-.0), "0B")
		self.assertEqual(byte_size_string(-.1), "0B")
		self.assertEqual(byte_size_string(-.9), "0B")
		self.assertEqual(byte_size_string(-.10), "0B")
		self.assertEqual(byte_size_string(-.99), "0B")
		self.assertEqual(byte_size_string(-.100), "0B")
		self.assertEqual(byte_size_string(-.999), "0B")
		self.assertEqual(byte_size_string(-.1000), "0B")
		self.assertEqual(byte_size_string(-.1001), "0B")
		self.assertEqual(byte_size_string(-.1009), "0B")
		self.assertEqual(byte_size_string(-.1099), "0B")
		self.assertEqual(byte_size_string(-.1100), "0B")
		self.assertEqual(byte_size_string(-.1999), "0B")
		self.assertEqual(byte_size_string(-.99999), "0B")
		self.assertEqual(byte_size_string(-.999999), "0B")
		self.assertEqual(byte_size_string(-.9999999), "0B")
		self.assertEqual(byte_size_string(-.99999999), "0B")
		self.assertEqual(byte_size_string(-.999999999), "0B")
		self.assertEqual(byte_size_string(-.9999999999), "0B")
		self.assertEqual(byte_size_string(-.99999999999), "0B")
		self.assertEqual(byte_size_string(-.999999999999), "0B")
		self.assertEqual(byte_size_string(-.9999999999999), "0B")
		self.assertEqual(byte_size_string(-.99999999999999), "0B")
		self.assertEqual(byte_size_string(-.999999999999999), "0B")

	def test_negative_string_byte_size_string(self):

		self.assertEqual(byte_size_string("-0"), "0B")
		self.assertEqual(byte_size_string("-1"), "-1B")
		self.assertEqual(byte_size_string("-9"), "-9B")
		self.assertEqual(byte_size_string("-10"), "-10B")
		self.assertEqual(byte_size_string("-99"), "-99B")
		self.assertEqual(byte_size_string("-100"), "-100B")
		self.assertEqual(byte_size_string("-999"), "-999B")
		self.assertEqual(byte_size_string("-1000"), "-1K")
		self.assertEqual(byte_size_string("-1001"), "-1K 1B")
		self.assertEqual(byte_size_string("-1009"), "-1K 9B")
		self.assertEqual(byte_size_string("-1099"), "-1K 99B")
		self.assertEqual(byte_size_string("-1100"), "-1K 100B")
		self.assertEqual(byte_size_string("-1999"), "-1K 999B")
		self.assertEqual(byte_size_string("-99999"), "-99K 999B")
		self.assertEqual(byte_size_string("-999999"), "-999K 999B")
		self.assertEqual(byte_size_string("-9999999"), "-9M 999K 999B")
		self.assertEqual(byte_size_string("-99999999"), "-99M 999K 999B")
		self.assertEqual(byte_size_string("-999999999"), "-999M 999K 999B")
		self.assertEqual(byte_size_string("-9999999999"), "-9G 999M 999K 999B")
		self.assertEqual(byte_size_string("-99999999999"), "-99G 999M 999K 999B")
		self.assertEqual(byte_size_string("-999999999999"), "-999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-9999999999999"), "-9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-99999999999999"), "-99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-0999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-000999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-0000999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-000000999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-0000000999999999999999"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000000999999999999999"), "-999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string("-0.9"), "0B")
		self.assertEqual(byte_size_string("-1.9"), "-1B")
		self.assertEqual(byte_size_string("-9.9"), "-9B")
		self.assertEqual(byte_size_string("-10.9"), "-10B")
		self.assertEqual(byte_size_string("-99.9"), "-99B")
		self.assertEqual(byte_size_string("-100.9"), "-100B")
		self.assertEqual(byte_size_string("-999.9"), "-999B")
		self.assertEqual(byte_size_string("-1000.9"), "-1K")
		self.assertEqual(byte_size_string("-1001.9"), "-1K 1B")
		self.assertEqual(byte_size_string("-1009.9"), "-1K 9B")
		self.assertEqual(byte_size_string("-1099.9"), "-1K 99B")
		self.assertEqual(byte_size_string("-1100.9"), "-1K 100B")
		self.assertEqual(byte_size_string("-1999.9"), "-1K 999B")
		self.assertEqual(byte_size_string("-99999.9"), "-99K 999B")
		self.assertEqual(byte_size_string("-999999.9"), "-999K 999B")
		self.assertEqual(byte_size_string("-9999999.9"), "-9M 999K 999B")
		self.assertEqual(byte_size_string("-99999999.9"), "-99M 999K 999B")
		self.assertEqual(byte_size_string("-999999999.9"), "-999M 999K 999B")
		self.assertEqual(byte_size_string("-9999999999.9"), "-9G 999M 999K 999B")
		self.assertEqual(byte_size_string("-99999999999.9"), "-99G 999M 999K 999B")
		self.assertEqual(byte_size_string("-999999999999.9"), "-999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-9999999999999.9"), "-9T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-99999999999999.9"), "-99T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-999999999999999.9"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-0999999999999999.9"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00999999999999999.9"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-000999999999999999.9"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-0000999999999999999.9"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999.9"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999.90"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999.900"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999.9000"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999.90000"), "-999T 999G 999M 999K 999B")
		self.assertEqual(byte_size_string("-00000999999999999999.900000"), "-999T 999G 999M 999K 999B")

		self.assertEqual(byte_size_string("-.0"), "0B")
		self.assertEqual(byte_size_string("-.1"), "0B")
		self.assertEqual(byte_size_string("-.9"), "0B")
		self.assertEqual(byte_size_string("-.10"), "0B")
		self.assertEqual(byte_size_string("-.99"), "0B")
		self.assertEqual(byte_size_string("-.100"), "0B")
		self.assertEqual(byte_size_string("-.999"), "0B")
		self.assertEqual(byte_size_string("-.1000"), "0B")
		self.assertEqual(byte_size_string("-.1001"), "0B")
		self.assertEqual(byte_size_string("-.1009"), "0B")
		self.assertEqual(byte_size_string("-.1099"), "0B")
		self.assertEqual(byte_size_string("-.1100"), "0B")
		self.assertEqual(byte_size_string("-.1999"), "0B")
		self.assertEqual(byte_size_string("-.99999"), "0B")
		self.assertEqual(byte_size_string("-.999999"), "0B")
		self.assertEqual(byte_size_string("-.9999999"), "0B")
		self.assertEqual(byte_size_string("-.99999999"), "0B")
		self.assertEqual(byte_size_string("-.999999999"), "0B")
		self.assertEqual(byte_size_string("-.9999999999"), "0B")
		self.assertEqual(byte_size_string("-.99999999999"), "0B")
		self.assertEqual(byte_size_string("-.999999999999"), "0B")
		self.assertEqual(byte_size_string("-.9999999999999"), "0B")
		self.assertEqual(byte_size_string("-.99999999999999"), "0B")
		self.assertEqual(byte_size_string("-.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-0.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-00.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-0000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-00000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-000000.999999999999999"), "0B")
		self.assertEqual(byte_size_string("-0000000.999999999999999"), "0B")

	def test_overflow_byte_size_string(self):

		self.assertIsNone(byte_size_string(9999999999999999))
		self.assertIsNone(byte_size_string(99999999999999999))
		self.assertIsNone(byte_size_string(999999999999999999))
		self.assertIsNone(byte_size_string(9999999999999999999))
		self.assertIsNone(byte_size_string(99999999999999999999))
		self.assertIsNone(byte_size_string(999999999999999999999))
		self.assertIsNone(byte_size_string(9999999999999999999999))

		self.assertIsNone(byte_size_string(9999999999999999.9))
		self.assertIsNone(byte_size_string(99999999999999999.9))
		self.assertIsNone(byte_size_string(999999999999999999.9))
		self.assertIsNone(byte_size_string(9999999999999999999.9))
		self.assertIsNone(byte_size_string(99999999999999999999.9))
		self.assertIsNone(byte_size_string(999999999999999999999.9))
		self.assertIsNone(byte_size_string(9999999999999999999999.9))

		self.assertIsNone(byte_size_string("9999999999999999"))
		self.assertIsNone(byte_size_string("99999999999999999"))
		self.assertIsNone(byte_size_string("999999999999999999"))
		self.assertIsNone(byte_size_string("9999999999999999999"))
		self.assertIsNone(byte_size_string("99999999999999999999"))
		self.assertIsNone(byte_size_string("999999999999999999999"))
		self.assertIsNone(byte_size_string("9999999999999999999999"))
		self.assertIsNone(byte_size_string("09999999999999999999999"))
		self.assertIsNone(byte_size_string("009999999999999999999999"))
		self.assertIsNone(byte_size_string("0009999999999999999999999"))
		self.assertIsNone(byte_size_string("00009999999999999999999999"))
		self.assertIsNone(byte_size_string("000009999999999999999999999"))
		self.assertIsNone(byte_size_string("0000009999999999999999999999"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999"))
		self.assertIsNone(byte_size_string("000000009999999999999999999999"))

		self.assertIsNone(byte_size_string("9999999999999999.9"))
		self.assertIsNone(byte_size_string("99999999999999999.9"))
		self.assertIsNone(byte_size_string("999999999999999999.9"))
		self.assertIsNone(byte_size_string("9999999999999999999.9"))
		self.assertIsNone(byte_size_string("99999999999999999999.9"))
		self.assertIsNone(byte_size_string("999999999999999999999.9"))
		self.assertIsNone(byte_size_string("9999999999999999999999.9"))
		self.assertIsNone(byte_size_string("09999999999999999999999.9"))
		self.assertIsNone(byte_size_string("009999999999999999999999.9"))
		self.assertIsNone(byte_size_string("0009999999999999999999999.9"))
		self.assertIsNone(byte_size_string("00009999999999999999999999.9"))
		self.assertIsNone(byte_size_string("000009999999999999999999999.9"))
		self.assertIsNone(byte_size_string("0000009999999999999999999999.9"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.9"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.90"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.900"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.9000"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.90000"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.900000"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.9000000"))
		self.assertIsNone(byte_size_string("00000009999999999999999999999.90000000"))

	def test_invalid_byte_size_string(self):

		for value in (

			"forty two",[ 42 ],( 42, ),{ 42 },{ "value": 42 }, True, False, None, ...,
			print, unittest, self, type, object, super(), Exception
		):
			self.assertIsNone(byte_size_string(value))








	def test_WriteWrapper(self):

		if	os.path.isfile(self.wwpath): os.remove(self.wwpath)

		@WriteWrapper(self.wwpath)
		class SomeText(Transmutable):

			def __call__(self): return "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_UTILS
				init_name	= "WriteWrapper"
				init_level	= 10

		self.test_case = SomeText()

		with self.assertLogs("WriteWrapper", 10) as case_loggy:
			self.assertEqual(self.test_case(), "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG")

		self.assertTrue(os.path.isfile(self.wwpath))
		with open(self.wwpath) as ww:
			self.assertEqual(ww.read(), "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG")

		self.assertIn("DEBUG:WriteWrapper:Writing 49 symbols", case_loggy.output)
		self.assertIn(f"INFO:WriteWrapper:Written to {self.wwpath}", case_loggy.output)




	def test_WriteWrapper_rewrite(self):

		self.fmake(self.wwpath, "I SAY\n")
		self.assertTrue(os.path.isfile(self.wwpath))
		with open(self.wwpath) as ww : self.assertEqual(ww.read(), "I SAY\n")

		@WriteWrapper(self.wwpath, rewrite=True)
		class SomeText(Transmutable):

			def __call__(self): return "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_UTILS
				init_name	= "WriteWrapper_rewrite"
				init_level	= 10

		self.test_case = SomeText()

		with self.assertLogs("WriteWrapper_rewrite", 10) as case_loggy:
			self.assertEqual(self.test_case(), "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG")

		self.assertTrue(os.path.isfile(self.wwpath))
		with open(self.wwpath) as ww:
			self.assertEqual(ww.read(), "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG")

		self.assertIn("DEBUG:WriteWrapper_rewrite:Writing 49 symbols", case_loggy.output)
		self.assertIn(f"INFO:WriteWrapper_rewrite:Written to {self.wwpath}", case_loggy.output)




	def test_WriteWrapper_text_mode(self):

		self.fmake(self.wwpath, "I SAY\n")
		self.assertTrue(os.path.isfile(self.wwpath))
		with open(self.wwpath) as ww : self.assertEqual(ww.read(), "I SAY\n")

		@WriteWrapper(self.wwpath, text_mode=False)
		class SomeText(Transmutable):

			def __call__(self): return "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_UTILS
				init_name	= "WriteWrapper_text_mode"
				init_level	= 10

		self.test_case = SomeText()

		with self.assertLogs("WriteWrapper_text_mode", 10) as case_loggy:
			self.assertEqual(self.test_case(), self.wwpath)

		self.assertTrue(os.path.isfile(self.wwpath))
		with open(self.wwpath) as ww:
			self.assertEqual(ww.read(), "I SAY\nOOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG")

		self.assertIn("DEBUG:WriteWrapper_text_mode:Writing 49 symbols", case_loggy.output)
		self.assertIn(f"INFO:WriteWrapper_text_mode:Written to {self.wwpath}", case_loggy.output)




	def test_WriteWrapper_bad_super(self):

		for i,bad in enumerate((

			42, .69, True, False, None, ..., print, Transmutable,
			[ "text" ],( "text", ),{ "text" },{ "text": "text" }
		)):
			with self.subTest(super=bad):

				@WriteWrapper(self.wwpath)
				class SomeText(Transmutable):

					def __call__(self): return bad
					class loggy(LibraryContrib):

						handler		= self.ACCESS_UTILS
						init_name	= f"WriteWrapper_bad_super_{i}"
						init_level	= 10

				self.test_case = SomeText()
				with self.assertLogs(f"WriteWrapper_bad_super_{i}", 10) as case_loggy:
					self.assertIsNone(self.test_case())
				self.assertIn(
					f"DEBUG:WriteWrapper_bad_super_{i}:Text to write not fetched", case_loggy.output
				)
				self.test_case.loggy.close()




	def test_WriteWrapper_bad_path(self):

		for i,bad in enumerate((

			42, .69, True, False, None, ..., print, Transmutable,
			[ "text" ],( "text", ),{ "text" },{ "text": "text" }
		)):
			with self.subTest(path=bad):

				@WriteWrapper(bad)
				class SomeText(Transmutable):

					def __call__(self): return "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG"
					class loggy(LibraryContrib):

						handler		= self.ACCESS_UTILS
						init_name	= f"WriteWrapper_bad_path_{i}"
						init_level	= 10

				self.test_case = SomeText()
				with self.assertLogs(f"WriteWrapper_bad_path_{i}", 10) as case_loggy:
					self.assertIsNone(self.test_case())
				self.assertIn(f"DEBUG:WriteWrapper_bad_path_{i}:Writing 49 symbols", case_loggy.output)
				self.assertIn(
					f"DEBUG:WriteWrapper_bad_path_{i}:Path to write is not a string", case_loggy.output
				)
				self.test_case.loggy.close()




	@unittest.skip("manual invokation only")
	def test_WriteWrapper_raise(self):

		# path argument must be a local file with unset write bits
		NO_W_PATH = ""

		@WriteWrapper(NO_W_PATH)
		class SomeText(Transmutable):

			def __call__(self): return "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_UTILS
				init_name	= "WriteWrapper_raise"
				init_level	= 10

		self.test_case = SomeText()

		with self.assertLogs("WriteWrapper_raise", 10) as case_loggy : self.assertIsNone(self.test_case())
		self.assertIn("DEBUG:WriteWrapper_raise:Writing 49 symbols", case_loggy.output)
		# Error message is a subject to adjust to, perhaps
		self.assertIn(

			"DEBUG:WriteWrapper_raise:Writing failed due to PermissionError: "
			f"[Errno 13] Permission denied: '{NO_W_PATH}'",
			case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







