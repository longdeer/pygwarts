import	os
import	re
import	unittest
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.irma					import IrmaTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access				import LibraryAccess
from	pygwarts.irma.access.volume			import LibraryVolume








class AccessVolumeCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_VOLUME): os.remove(cls.ACCESS_VOLUME)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.ACCESS_VOLUME)
		cls.some_location = os.path.join(os.path.dirname(cls.ACCESS_VOLUME), "some_location")

	def setUp(self):

		if	os.path.isfile(self.some_location):	os.remove(self.some_location)
		if	os.path.isdir(self.some_location):	os.rmdir(self.some_location)


	def test_no_upper_init(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "no_upper_init"
				init_level	= 10

		with self.assertLogs("no_upper_init", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(
			f"INFO:no_upper_init:Volume {self.test_case} not assigned to any library", case_loggy.output
		)


	def test_LibraryAccess_init(self):
		class LonelyLibrary(LibraryAccess):

			class LonelyVolume(LibraryVolume):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "LibraryAccess_init"
				init_level	= 10

		with self.assertLogs("LibraryAccess_init", 10) as case_loggy : self.test_case = LonelyLibrary()
		self.assertIn(f"DEBUG:LibraryAccess_init:Assigned to {self.test_case}", case_loggy.output)








	def test_get_range_valids(self):
		class LonelyVolume(LibraryVolume):	pass

		self.test_case = LonelyVolume()
		self.assertEqual(self.test_case.get_range("0420"), re.compile("0420"))
		self.test_case.inrange = "01/01"
		self.assertEqual(self.test_case.get_range(), re.compile("01/01"))


	def test_get_range_invalids(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "get_range_invalids"
				init_level	= 10

		self.test_case = LonelyVolume()
		for invalid in (

			42, .69, None, Transmutable, print, True, False, ...,
			[ "0420" ],( "0420", ),{ "0420" },{ "inrange": "0420" }
		):
			with self.subTest(invalid=invalid):
				with self.assertLogs("get_range_invalids", 10) as case_loggy:

					self.assertIsNone(self.test_case.get_range(invalid))
					self.test_case.inrange = invalid
					self.assertIsNone(self.test_case.get_range())

				self.assertIn(

					f"INFO:get_range_invalids:Valid {self.test_case} range not provided",
					case_loggy.output
				)
				self.assertEqual(
					case_loggy.output.count(

						f"INFO:get_range_invalids:Valid {self.test_case} range not provided"
					),	2
				)








	def test_is_located(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "is_located"
				init_level	= 10

		self.test_case = LonelyVolume()
		with self.assertLogs("is_located", 10) as case_loggy:
			self.assertIsNone(self.test_case.is_located())

		self.assertIn("DEBUG:is_located:Location was not provided", case_loggy.output)

		self.test_case.location = self.some_location
		with self.assertLogs("is_located", 10) as case_loggy:
			self.assertIsNone(self.test_case.is_located())

		self.assertIn(f"DEBUG:is_located:Location \"{self.some_location}\" is invalid", case_loggy.output)

		os.mkdir(self.some_location)
		with self.assertLogs("is_located", 10) as case_loggy:
			self.assertIsNone(self.test_case.is_located())

		self.assertIn(f"DEBUG:is_located:Location \"{self.some_location}\" is invalid", case_loggy.output)

		os.rmdir(self.some_location)
		self.fmake(self.some_location)
		with self.assertLogs("is_located", 10) as case_loggy:
			self.assertEqual(self.test_case.is_located(), self.some_location)

		self.assertIn(f"DEBUG:is_located:Accessible \"{self.some_location}\" located", case_loggy.output)

		os.remove(self.some_location)
		self.assertFalse(os.path.isfile(self.some_location))
		self.assertFalse(os.path.isdir(self.some_location))

		#
		# Bonus for normal OS. location might be set to any existent but lack of r-bit file
		#
		#self.test_case.location = "/swapfile"
		#with self.assertLogs("is_located", 10) as case_loggy:
		#	self.assertIsNone(self.test_case.is_located())

		#self.assertIn(
		#	f"DEBUG:is_located:Location \"/swapfile\" is not accessible", case_loggy.output
		#)








	def test_read_generator(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "read_generator"
				init_level	= 10

		self.fmake(self.some_location, "OOH\nEEH\nOOH\nAH\nAH\nTING\nTANG\nWALLA\nWALLA\nBING\nBANG")
		self.test_case = LonelyVolume()

		with self.assertLogs("read_generator", 10) as case_loggy:
			self.assertEqual(

				list(self.test_case.g_reading()),
				[ "OOH", "EEH", "OOH", "AH", "AH", "TING", "TANG", "WALLA", "WALLA", "BING", "BANG" ]
			)
		self.assertIn(
			f"INFO:read_generator:Location \"{self.some_location}\" access granted", case_loggy.output
		)
		self.assertEqual(self.test_case.is_located(), self.some_location)

		with self.assertLogs("read_generator", 10) as case_loggy:

			lines = []
			for line in self.test_case.g_reading() : lines.append(line)
			self.assertEqual(

				lines,
				[ "OOH", "EEH", "OOH", "AH", "AH", "TING", "TANG", "WALLA", "WALLA", "BING", "BANG" ]
			)
		self.assertIn(
			f"INFO:read_generator:Location \"{self.some_location}\" access granted", case_loggy.output
		)
		self.assertEqual(self.test_case.is_located(), self.some_location)




	def test_read_generator_no_file(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "read_generator_no_file"
				init_level	= 10

		self.test_case = LonelyVolume()
		self.assertFalse(os.path.isfile(self.some_location))
		self.assertFalse(os.path.isdir(self.some_location))

		with self.assertLogs("read_generator_no_file", 10) as case_loggy:
			lines = []
			for line in self.test_case.g_reading() : lines.append(line)

		self.assertIn(
			f"DEBUG:read_generator_no_file:Location \"{self.some_location}\" is invalid", case_loggy.output
		)
		self.assertIsNone(self.test_case.is_located())




	def test_read_generator_break_outer(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "read_generator_break_outer"
				init_level	= 10

		self.fmake(self.some_location, "OOH\nEEH\nOOH\nAH\nAH\nTING\nTANG\nWALLA\nWALLA\nBING\nBANG")
		self.test_case = LonelyVolume()

		with self.assertLogs("read_generator_break_outer", 10) as case_loggy:

			lines = []
			for line in self.test_case.g_reading():

				if	line == "AH" : break
				lines.append(line)

			self.assertEqual(lines,[ "OOH", "EEH", "OOH" ])
		self.assertIn(

			f"INFO:read_generator_break_outer:Location \"{self.some_location}\" access granted",
			case_loggy.output
		)
		self.assertEqual(self.test_case.is_located(), self.some_location)








	def test_triggering_generator(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "triggering_generator"
				init_level	= 10

		line = "OOH EEH OOH AH AH TING TANG WALLA WALLA BING BANG"
		triggers = re.compile("(OOH EEH)|(ooh ah ah)|(WALLA WALLA)")
		self.test_case = LonelyVolume()

		with self.assertLogs("triggering_generator", 10) as case_loggy:
			self.assertEqual(

				list(self.test_case.g_triggering(line, triggers)),
				[ "OOH EEH","WALLA WALLA" ]
			)

		self.assertIn("DEBUG:triggering_generator:Triggered by \"OOH EEH\"", case_loggy.output)
		self.assertIn("DEBUG:triggering_generator:Triggered by \"WALLA WALLA\"", case_loggy.output)


		with self.assertLogs("triggering_generator", 10) as case_loggy:

			responses = []
			for response in self.test_case.g_triggering(line, triggers) : responses.append(response)
			self.assertEqual(responses,[ "OOH EEH","WALLA WALLA" ])

		self.assertIn("DEBUG:triggering_generator:Triggered by \"OOH EEH\"", case_loggy.output)
		self.assertIn("DEBUG:triggering_generator:Triggered by \"WALLA WALLA\"", case_loggy.output)




	def test_triggering_generator_bad_triggers(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "triggering_generator_bad_triggers"
				init_level	= 10

		self.test_case = LonelyVolume()
		for bad_triggers in (

			"triggers", 42, .69, True, False, None, ..., print, Transmutable,
			( "trigger #1", "trigger #2", "trigger #3" ),
			{ "trigger #1", "trigger #2", "trigger #3" },
			{ 1: "trigger #1", 2: "trigger #2", 3: "trigger #3" },
		):
			with self.subTest(triggers=bad_triggers):
				with self.assertLogs("triggering_generator_bad_triggers", 10) as case_loggy:
					self.assertEqual(
						list(self.test_case.g_triggering("no need line", bad_triggers)),[]
					)
				self.assertIn(

					f"DEBUG:triggering_generator_bad_triggers:Invalid triggers \"{bad_triggers}\"",
					case_loggy.output
				)




	def test_triggering_generator_bad_line(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "triggering_generator_bad_line"
				init_level	= 10

		self.test_case = LonelyVolume()
		triggers = re.compile("(no)|(need)|(line)")
		for bad_line in (

			42, .69, True, False, None, ..., print, Transmutable,
			[ "no need line" ],
			( "no need line", ),
			{ "no need line" },
			{ "line": "no need line" },
		):
			with self.subTest(line=bad_line):
				with self.assertLogs("triggering_generator_bad_line", 10) as case_loggy:
					self.assertEqual(
						list(self.test_case.g_triggering(bad_line, triggers)),[]
					)
				self.assertIn(

					f"DEBUG:triggering_generator_bad_line:Invalid line \"{bad_line}\"",
					case_loggy.output
				)




	def test_triggering_generator_no_response(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "triggering_generator_no_response"
				init_level	= 10

		line = "OOH EEH OOH AH AH TING TANG WALLA WALLA BING BANG"
		triggers = re.compile("(ooh EEH)|(ooh AH AH)|(walla WALLA)")

		self.test_case = LonelyVolume()
		self.assertEqual(list(self.test_case.g_triggering(line, triggers)),[])




	def test_triggering_generator_break(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "triggering_generator_break"
				init_level	= 10

		line = "OOH EEH OOH AH AH TING TANG WALLA WALLA BING BANG"
		triggers = re.compile("(OOH EEH)|(OOH AH AH)|(WALLA WALLA)")
		self.test_case = LonelyVolume()

		with self.assertLogs("triggering_generator_break", 10) as case_loggy:

			responses = []
			for response in self.test_case.g_triggering(line, triggers):

				responses.append(response)
				break

			self.assertEqual(responses,[ "OOH EEH" ])
		self.assertIn("DEBUG:triggering_generator_break:Triggered by \"OOH EEH\"", case_loggy.output)




	def test_triggering_generator_single_trigger(self):
		class LonelyVolume(LibraryVolume):

			location = self.some_location
			class loggy(LibraryContrib):

				handler		= self.ACCESS_VOLUME
				init_name	= "triggering_generator_single_trigger"
				init_level	= 10

		line = "OOH EEH OOH AH AH TING TANG WALLA WALLA BING BANG"
		triggers = re.compile("(OOH EEH)")
		self.test_case = LonelyVolume()

		with self.assertLogs("triggering_generator_single_trigger", 10) as case_loggy:
			self.assertEqual(list(self.test_case.g_triggering(line, triggers)),[ "OOH EEH" ])
		self.assertIn("DEBUG:triggering_generator_single_trigger:Triggered by \"OOH EEH\"",case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







