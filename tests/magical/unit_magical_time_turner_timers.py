import	os
import	unittest
from	typing								import List
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.time_turner.timers	import Callstamp
from	pygwarts.magical.time_turner.timers	import mostsec
from	pygwarts.magical.time_turner.timers	import mostsecfmt
from	pygwarts.magical.time_turner.timers	import DIRTtimer
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.tests.magical				import MagicalTestCase








class TimeTurnerTimersCases(MagicalTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.TIMETURN_TIMERS_HANDLER): os.remove(cls.TIMETURN_TIMERS_HANDLER)

	@classmethod
	def setUpClass(cls):

		@mostsecfmt(positive=False)
		class Secfmter(Transmutable):
			def __call__(self, *args, **kwargs): return args[0]

		@mostsecfmt(positive=True)
		class PositiveSecfmter(Transmutable):
			def __call__(self, *args, **kwargs): return args[0]

		cls.secfmter = Secfmter()
		cls.posfmter = PositiveSecfmter()
		cls.make_loggy_file(cls, cls.TIMETURN_TIMERS_HANDLER)


		class Chrome(Transmutable):

			def __init__(self, *args, **kwargs):

				super().__init__(*args, **kwargs)
				self.RAM = 1000

			def __call__(self, operation :str, *, source :List[int]):

				self.loggy.info(f"Going to {operation}")
				self.consume_RAM(source)

			def consume_RAM(self, source :List[int]):

				source[0] *= 2
				self.loggy.info(f"Current RAM consumed {source[0]}")

		cls.browser = Chrome




	def test_Callstamp_loggy(self):

		callstamp = str(self.MAGICAL_ROOT /"callstamp.loggy")
		self.make_loggy_file(callstamp)


		@Callstamp
		class Stamper(Transmutable):

			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"

			class loggy(LibraryContrib):

				handler		= callstamp
				init_name	= "callstamp-1"


		loggy = []
		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")
		self.test_case.loggy.close()

		with open(callstamp) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),2)
		self.assertEqual(loggy[0], "@callstamp-1 INFO : Making a stamp now")
		self.assertTrue(loggy[1].startswith("@callstamp-1 INFO : Stamper finished in "))




		@Callstamp
		class Stamper(Transmutable):

			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"

			class loggy(LibraryContrib):

				handler		= callstamp
				init_name	= "callstamp-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(callstamp)
		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")
		self.test_case.loggy.close()

		with open(callstamp) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),4)
		self.assertTrue(loggy[0].startswith("@callstamp-2-Stamper DEBUG : Start point "))
		self.assertEqual(loggy[1], "@callstamp-2-Stamper INFO : Making a stamp now")
		self.assertTrue(loggy[2].startswith("@callstamp-2-Stamper DEBUG : End point "))
		self.assertTrue(loggy[3].startswith("@callstamp-2-Stamper INFO : Stamper finished in "))




		@Callstamp
		class Stamper(Transmutable):

			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"

			class loggy(LibraryContrib):

				handler			= callstamp
				init_name		= "callstamp-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(callstamp)
		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")
		self.test_case.loggy.close()

		with open(callstamp) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),2)
		self.assertEqual(loggy[0], "@callstamp-3-Stamper INFO : Making a stamp now")
		self.assertTrue(loggy[1].startswith("@callstamp-3-Stamper INFO : Stamper finished in "))
		if os.path.isfile(callstamp): os.remove(callstamp)








	def test_Callstamp_name_loggy(self):

		callstamp_n = str(self.MAGICAL_ROOT /"callstamp_n.loggy")
		self.make_loggy_file(callstamp_n)


		@Callstamp
		class Stamper(Transmutable):

			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"

			class shmoggy(LibraryContrib):

				handler		= callstamp_n
				init_name	= "callstamp_n-1"


		loggy = []
		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")
		self.test_case.loggy.close()

		with open(callstamp_n) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),2)
		self.assertEqual(loggy[0], "@callstamp_n-1 INFO : Making a stamp now")
		self.assertTrue(loggy[1].startswith("@callstamp_n-1 INFO : Stamper finished in "))




		@Callstamp
		class Stamper(Transmutable):

			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"

			class shmoggy(LibraryContrib):

				handler		= callstamp_n
				init_name	= "callstamp_n-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(callstamp_n)
		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")
		self.test_case.loggy.close()

		with open(callstamp_n) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),4)
		self.assertTrue(loggy[0].startswith("@callstamp_n-2-Stamper DEBUG : Start point "))
		self.assertEqual(loggy[1], "@callstamp_n-2-Stamper INFO : Making a stamp now")
		self.assertTrue(loggy[2].startswith("@callstamp_n-2-Stamper DEBUG : End point "))
		self.assertTrue(loggy[3].startswith("@callstamp_n-2-Stamper INFO : Stamper finished in "))




		@Callstamp
		class Stamper(Transmutable):

			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"

			class shmoggy(LibraryContrib):

				handler			= callstamp_n
				init_name		= "callstamp_n-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(callstamp_n)
		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")
		self.test_case.loggy.close()

		with open(callstamp_n) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),2)
		self.assertEqual(loggy[0], "@callstamp_n-3-Stamper INFO : Making a stamp now")
		self.assertTrue(loggy[1].startswith("@callstamp_n-3-Stamper INFO : Stamper finished in "))
		if os.path.isfile(callstamp_n): os.remove(callstamp_n)








	def test_Callstamp_no_loggy(self):

		@Callstamp
		class Stamper(Transmutable):
			def __call__(self):

				self.loggy.info("Making a stamp now")
				return	"Making a stamp now"


		self.test_case = Stamper()
		current = self.test_case()
		self.assertEqual(current, "Making a stamp now")








	def test_nocall_Callstamp(self):

		nocall = str(self.MAGICAL_ROOT /"nocall.loggy")
		self.make_loggy_file(nocall)


		@Callstamp
		class Stamper(Transmutable):

			def stamping(self): self.loggy.info("This is not the stamp it should be")
			class loggy(LibraryContrib):

				handler		= nocall
				init_name	= "nocall-1"


		loggy = []
		self.test_case = Stamper()
		self.test_case.stamping()
		self.test_case.loggy.close()

		with open(nocall) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(len(loggy),1)
		self.assertEqual(loggy[0], "@nocall-1 INFO : This is not the stamp it should be")


		self.assertRaisesRegex(

			TypeError,
			"Stamper object is not callable",
			self.test_case
		)




		@Callstamp
		class Stamper(Transmutable):
			def stamping(self): self.loggy.info("This is not the stamp it should be")


		self.test_case = Stamper()
		self.test_case.stamping()
		self.assertRaisesRegex(

			TypeError,
			"Stamper object is not callable",
			self.test_case
		)
		if	os.path.isfile(nocall): os.remove(nocall)
















	def test_mostsec_int_seconds(self):

		self.assertEqual(mostsec(0, positive=True), None)
		self.assertEqual(mostsec(0), "<1 ns")
		self.assertEqual(mostsec(1), "1 s")
		self.assertEqual(mostsec(59), "59 s")
		self.assertEqual(mostsec(60), "1 m")
		self.assertEqual(mostsec(61), "1 m 1 s")
		self.assertEqual(mostsec(119), "1 m 59 s")
		self.assertEqual(mostsec(120), "2 m")
		self.assertEqual(mostsec(120), "2 m")
		self.assertEqual(mostsec(3599), "59 m 59 s")
		self.assertEqual(mostsec(3600), "1 h")
		self.assertEqual(mostsec(3601), "1 h")
		self.assertEqual(mostsec(3659), "1 h")
		self.assertEqual(mostsec(3660), "1 h 1 m")
		self.assertEqual(mostsec(86399), "23 h 59 m")
		self.assertEqual(mostsec(86400), "1 d")
		self.assertEqual(mostsec(86401), "1 d")
		self.assertEqual(mostsec(86459), "1 d")
		self.assertEqual(mostsec(89999), "1 d")
		self.assertEqual(mostsec(90000), "1 d 1 h")
		self.assertEqual(mostsec(31535999), "364 d 23 h")
		self.assertEqual(mostsec(31536000), "365 d")
		self.assertEqual(mostsec(31539599), "365 d")
		self.assertEqual(mostsec(31539600), "365 d 1 h")

	def test_mostsec_int_seconds_negative(self):

		self.assertEqual(mostsec(-0, positive=True), None)
		self.assertEqual(mostsec(-0), "<1 ns")
		self.assertEqual(mostsec(-1), "1 s")
		self.assertEqual(mostsec(-59), "59 s")
		self.assertEqual(mostsec(-60), "1 m")
		self.assertEqual(mostsec(-61), "1 m 1 s")
		self.assertEqual(mostsec(-119), "1 m 59 s")
		self.assertEqual(mostsec(-120), "2 m")
		self.assertEqual(mostsec(-120), "2 m")
		self.assertEqual(mostsec(-3599), "59 m 59 s")
		self.assertEqual(mostsec(-3600), "1 h")
		self.assertEqual(mostsec(-3601), "1 h")
		self.assertEqual(mostsec(-3659), "1 h")
		self.assertEqual(mostsec(-3660), "1 h 1 m")
		self.assertEqual(mostsec(-86399), "23 h 59 m")
		self.assertEqual(mostsec(-86400), "1 d")
		self.assertEqual(mostsec(-86401), "1 d")
		self.assertEqual(mostsec(-86459), "1 d")
		self.assertEqual(mostsec(-89999), "1 d")
		self.assertEqual(mostsec(-90000), "1 d 1 h")
		self.assertEqual(mostsec(-31535999), "364 d 23 h")
		self.assertEqual(mostsec(-31536000), "365 d")
		self.assertEqual(mostsec(-31539599), "365 d")
		self.assertEqual(mostsec(-31539600), "365 d 1 h")

	def test_mostsec_str_int_seconds(self):

		self.assertEqual(mostsec("0", positive=True), None)
		self.assertEqual(mostsec("0"), "<1 ns")
		self.assertEqual(mostsec("1"), "1 s")
		self.assertEqual(mostsec("59"), "59 s")
		self.assertEqual(mostsec("60"), "1 m")
		self.assertEqual(mostsec("61"), "1 m 1 s")
		self.assertEqual(mostsec("119"), "1 m 59 s")
		self.assertEqual(mostsec("120"), "2 m")
		self.assertEqual(mostsec("120"), "2 m")
		self.assertEqual(mostsec("3599"), "59 m 59 s")
		self.assertEqual(mostsec("3600"), "1 h")
		self.assertEqual(mostsec("3601"), "1 h")
		self.assertEqual(mostsec("3659"), "1 h")
		self.assertEqual(mostsec("3660"), "1 h 1 m")
		self.assertEqual(mostsec("86399"), "23 h 59 m")
		self.assertEqual(mostsec("86400"), "1 d")
		self.assertEqual(mostsec("86401"), "1 d")
		self.assertEqual(mostsec("86459"), "1 d")
		self.assertEqual(mostsec("89999"), "1 d")
		self.assertEqual(mostsec("90000"), "1 d 1 h")
		self.assertEqual(mostsec("90000"), "1 d 1 h")
		self.assertEqual(mostsec("31535999"), "364 d 23 h")
		self.assertEqual(mostsec("31536000"), "365 d")
		self.assertEqual(mostsec("31539599"), "365 d")
		self.assertEqual(mostsec("31539600"), "365 d 1 h")

	def test_mostsec_str_int_seconds_negative(self):

		self.assertEqual(mostsec("-0", positive=True), None)
		self.assertEqual(mostsec("-0"), "<1 ns")
		self.assertEqual(mostsec("-1"), "1 s")
		self.assertEqual(mostsec("-59"), "59 s")
		self.assertEqual(mostsec("-60"), "1 m")
		self.assertEqual(mostsec("-61"), "1 m 1 s")
		self.assertEqual(mostsec("-119"), "1 m 59 s")
		self.assertEqual(mostsec("-120"), "2 m")
		self.assertEqual(mostsec("-120"), "2 m")
		self.assertEqual(mostsec("-3599"), "59 m 59 s")
		self.assertEqual(mostsec("-3600"), "1 h")
		self.assertEqual(mostsec("-3601"), "1 h")
		self.assertEqual(mostsec("-3659"), "1 h")
		self.assertEqual(mostsec("-3660"), "1 h 1 m")
		self.assertEqual(mostsec("-86399"), "23 h 59 m")
		self.assertEqual(mostsec("-86400"), "1 d")
		self.assertEqual(mostsec("-86401"), "1 d")
		self.assertEqual(mostsec("-86459"), "1 d")
		self.assertEqual(mostsec("-89999"), "1 d")
		self.assertEqual(mostsec("-90000"), "1 d 1 h")
		self.assertEqual(mostsec("-31535999"), "364 d 23 h")
		self.assertEqual(mostsec("-31536000"), "365 d")
		self.assertEqual(mostsec("-31539599"), "365 d")
		self.assertEqual(mostsec("-31539600"), "365 d 1 h")

	def test_mostsec_float_seconds(self):

		self.assertEqual(mostsec(0., positive=True), None)
		self.assertEqual(mostsec(0.), "<1 ns")
		self.assertEqual(mostsec(1.), "1 s")
		self.assertEqual(mostsec(59.), "59 s")
		self.assertEqual(mostsec(60.), "1 m")
		self.assertEqual(mostsec(61.), "1 m 1 s")
		self.assertEqual(mostsec(119.), "1 m 59 s")
		self.assertEqual(mostsec(120.), "2 m")
		self.assertEqual(mostsec(120.), "2 m")
		self.assertEqual(mostsec(3599.), "59 m 59 s")
		self.assertEqual(mostsec(3600.), "1 h")
		self.assertEqual(mostsec(3601.), "1 h")
		self.assertEqual(mostsec(3659.), "1 h")
		self.assertEqual(mostsec(3660.), "1 h 1 m")
		self.assertEqual(mostsec(86399.), "23 h 59 m")
		self.assertEqual(mostsec(86400.), "1 d")
		self.assertEqual(mostsec(86401.), "1 d")
		self.assertEqual(mostsec(86459.), "1 d")
		self.assertEqual(mostsec(89999.), "1 d")
		self.assertEqual(mostsec(90000.), "1 d 1 h")
		self.assertEqual(mostsec(31535999.), "364 d 23 h")
		self.assertEqual(mostsec(31536000.), "365 d")
		self.assertEqual(mostsec(31539599.), "365 d")
		self.assertEqual(mostsec(31539600.), "365 d 1 h")

	def test_mostsec_float_seconds_negative(self):

		self.assertEqual(mostsec(-0., positive=True), None)
		self.assertEqual(mostsec(-0.), "<1 ns")
		self.assertEqual(mostsec(-1.), "1 s")
		self.assertEqual(mostsec(-59.), "59 s")
		self.assertEqual(mostsec(-60.), "1 m")
		self.assertEqual(mostsec(-61.), "1 m 1 s")
		self.assertEqual(mostsec(-119.), "1 m 59 s")
		self.assertEqual(mostsec(-120.), "2 m")
		self.assertEqual(mostsec(-120.), "2 m")
		self.assertEqual(mostsec(-3599.), "59 m 59 s")
		self.assertEqual(mostsec(-3600.), "1 h")
		self.assertEqual(mostsec(-3601.), "1 h")
		self.assertEqual(mostsec(-3659.), "1 h")
		self.assertEqual(mostsec(-3660.), "1 h 1 m")
		self.assertEqual(mostsec(-86399.), "23 h 59 m")
		self.assertEqual(mostsec(-86400.), "1 d")
		self.assertEqual(mostsec(-86401.), "1 d")
		self.assertEqual(mostsec(-86459.), "1 d")
		self.assertEqual(mostsec(-89999.), "1 d")
		self.assertEqual(mostsec(-90000.), "1 d 1 h")
		self.assertEqual(mostsec(-31535999.), "364 d 23 h")
		self.assertEqual(mostsec(-31536000.), "365 d")
		self.assertEqual(mostsec(-31539599.), "365 d")
		self.assertEqual(mostsec(-31539600.), "365 d 1 h")

	def test_mostsec_str_float_seconds(self):

		self.assertEqual(mostsec("0.", positive=True), None)
		self.assertEqual(mostsec("0."), "<1 ns")
		self.assertEqual(mostsec("1."), "1 s")
		self.assertEqual(mostsec("59."), "59 s")
		self.assertEqual(mostsec("60."), "1 m")
		self.assertEqual(mostsec("61."), "1 m 1 s")
		self.assertEqual(mostsec("119."), "1 m 59 s")
		self.assertEqual(mostsec("120."), "2 m")
		self.assertEqual(mostsec("120."), "2 m")
		self.assertEqual(mostsec("3599."), "59 m 59 s")
		self.assertEqual(mostsec("3600."), "1 h")
		self.assertEqual(mostsec("3601."), "1 h")
		self.assertEqual(mostsec("3659."), "1 h")
		self.assertEqual(mostsec("3660."), "1 h 1 m")
		self.assertEqual(mostsec("86399."), "23 h 59 m")
		self.assertEqual(mostsec("86400."), "1 d")
		self.assertEqual(mostsec("86401."), "1 d")
		self.assertEqual(mostsec("86459."), "1 d")
		self.assertEqual(mostsec("89999."), "1 d")
		self.assertEqual(mostsec("90000."), "1 d 1 h")
		self.assertEqual(mostsec("90000."), "1 d 1 h")
		self.assertEqual(mostsec("31535999."), "364 d 23 h")
		self.assertEqual(mostsec("31536000."), "365 d")
		self.assertEqual(mostsec("31539599."), "365 d")
		self.assertEqual(mostsec("31539600."), "365 d 1 h")

	def test_mostsec_str_float_seconds_negative(self):

		self.assertEqual(mostsec("-0.", positive=True), None)
		self.assertEqual(mostsec("-0."), "<1 ns")
		self.assertEqual(mostsec("-1."), "1 s")
		self.assertEqual(mostsec("-59."), "59 s")
		self.assertEqual(mostsec("-60."), "1 m")
		self.assertEqual(mostsec("-61."), "1 m 1 s")
		self.assertEqual(mostsec("-119."), "1 m 59 s")
		self.assertEqual(mostsec("-120."), "2 m")
		self.assertEqual(mostsec("-120."), "2 m")
		self.assertEqual(mostsec("-3599."), "59 m 59 s")
		self.assertEqual(mostsec("-3600."), "1 h")
		self.assertEqual(mostsec("-3601."), "1 h")
		self.assertEqual(mostsec("-3659."), "1 h")
		self.assertEqual(mostsec("-3660."), "1 h 1 m")
		self.assertEqual(mostsec("-86399."), "23 h 59 m")
		self.assertEqual(mostsec("-86400."), "1 d")
		self.assertEqual(mostsec("-86401."), "1 d")
		self.assertEqual(mostsec("-86459."), "1 d")
		self.assertEqual(mostsec("-89999."), "1 d")
		self.assertEqual(mostsec("-90000."), "1 d 1 h")
		self.assertEqual(mostsec("-31535999."), "364 d 23 h")
		self.assertEqual(mostsec("-31536000."), "365 d")
		self.assertEqual(mostsec("-31539599."), "365 d")
		self.assertEqual(mostsec("-31539600."), "365 d 1 h")

	def test_mostsec_float_lt_second(self):

		self.assertEqual(mostsec(.0, positive=True), None)
		self.assertEqual(mostsec(.0), "<1 ns")
		self.assertEqual(mostsec(.99999999), "999 ms")
		self.assertEqual(mostsec(.9999999), "999 ms")
		self.assertEqual(mostsec(.999999), "999 ms")
		self.assertEqual(mostsec(.99999), "999 ms")
		self.assertEqual(mostsec(.9999), "999 ms")
		self.assertEqual(mostsec(.999), "999 ms")
		self.assertEqual(mostsec(.19999999), "199 ms")
		self.assertEqual(mostsec(.1999999), "199 ms")
		self.assertEqual(mostsec(.199999), "199 ms")
		self.assertEqual(mostsec(.19999), "199 ms")
		self.assertEqual(mostsec(.1999), "199 ms")
		self.assertEqual(mostsec(.199), "199 ms")
		self.assertEqual(mostsec(.19), "190 ms")
		self.assertEqual(mostsec(.1), "100 ms")
		self.assertEqual(mostsec(.10), "100 ms")
		self.assertEqual(mostsec(.100), "100 ms")
		self.assertEqual(mostsec(.1000), "100 ms")
		self.assertEqual(mostsec(.10000), "100 ms")
		self.assertEqual(mostsec(.100000), "100 ms")
		self.assertEqual(mostsec(.1000000), "100 ms")
		self.assertEqual(mostsec(.10000000), "100 ms")
		self.assertEqual(mostsec(.09999999), "99 ms")
		self.assertEqual(mostsec(.0999999), "99 ms")
		self.assertEqual(mostsec(.099999), "99 ms")
		self.assertEqual(mostsec(.09999), "99 ms")
		self.assertEqual(mostsec(.0999), "99 ms")
		self.assertEqual(mostsec(.099), "99 ms")
		self.assertEqual(mostsec(.009), "9 ms")
		self.assertEqual(mostsec(.001), "1 ms")
		self.assertEqual(mostsec(.0010), "1 ms")
		self.assertEqual(mostsec(.00100), "1 ms")
		self.assertEqual(mostsec(.001000), "1 ms")
		self.assertEqual(mostsec(.0010000), "1 ms")
		self.assertEqual(mostsec(.00100000), "1 ms")
		self.assertEqual(mostsec(.00099999), "999 us")
		self.assertEqual(mostsec(.0009999), "999 us")
		self.assertEqual(mostsec(.000999), "999 us")
		self.assertEqual(mostsec(.00099), "990 us")
		self.assertEqual(mostsec(.0009), "900 us")
		self.assertEqual(mostsec(.0001), "100 us")
		self.assertEqual(mostsec(.00010), "100 us")
		self.assertEqual(mostsec(.000100), "100 us")
		self.assertEqual(mostsec(.0001000), "100 us")
		self.assertEqual(mostsec(.00010000), "100 us")
		self.assertEqual(mostsec(.00009999), "99 us")
		self.assertEqual(mostsec(.0000999), "99 us")
		self.assertEqual(mostsec(.000099), "99 us")
		self.assertEqual(mostsec(.000009), "9 us")
		self.assertEqual(mostsec(.000001), "1 us")
		self.assertEqual(mostsec(.0000010), "1 us")
		self.assertEqual(mostsec(.00000100), "1 us")
		self.assertEqual(mostsec(.0000009999), "999 ns")
		self.assertEqual(mostsec(.000000999), "999 ns")
		self.assertEqual(mostsec(.00000099), "990 ns")
		self.assertEqual(mostsec(.0000009), "900 ns")
		self.assertEqual(mostsec(.0000001), "100 ns")
		self.assertEqual(mostsec(.00000010), "100 ns")
		self.assertEqual(mostsec(.000000100), "100 ns")
		self.assertEqual(mostsec(.0000001000), "100 ns")
		self.assertEqual(mostsec(.00000010000), "100 ns")
		self.assertEqual(mostsec(.000000100000), "100 ns")
		self.assertEqual(mostsec(.000000099999), "99 ns")
		self.assertEqual(mostsec(.00000009999), "99 ns")
		self.assertEqual(mostsec(.0000000999), "99 ns")
		self.assertEqual(mostsec(.000000099), "99 ns")
		self.assertEqual(mostsec(.000000009), "9 ns")
		self.assertEqual(mostsec(.000000001), "1 ns")
		self.assertEqual(mostsec(.0000000001), "<1 ns")

	def test_mostsec_float_lt_second_negative(self):

		self.assertEqual(mostsec(-.0, positive=True), None)
		self.assertEqual(mostsec(-.0), "<1 ns")
		self.assertEqual(mostsec(-.99999999), "999 ms")
		self.assertEqual(mostsec(-.9999999), "999 ms")
		self.assertEqual(mostsec(-.999999), "999 ms")
		self.assertEqual(mostsec(-.99999), "999 ms")
		self.assertEqual(mostsec(-.9999), "999 ms")
		self.assertEqual(mostsec(-.999), "999 ms")
		self.assertEqual(mostsec(-.19999999), "199 ms")
		self.assertEqual(mostsec(-.1999999), "199 ms")
		self.assertEqual(mostsec(-.199999), "199 ms")
		self.assertEqual(mostsec(-.19999), "199 ms")
		self.assertEqual(mostsec(-.1999), "199 ms")
		self.assertEqual(mostsec(-.199), "199 ms")
		self.assertEqual(mostsec(-.19), "190 ms")
		self.assertEqual(mostsec(-.1), "100 ms")
		self.assertEqual(mostsec(-.10), "100 ms")
		self.assertEqual(mostsec(-.100), "100 ms")
		self.assertEqual(mostsec(-.1000), "100 ms")
		self.assertEqual(mostsec(-.10000), "100 ms")
		self.assertEqual(mostsec(-.100000), "100 ms")
		self.assertEqual(mostsec(-.1000000), "100 ms")
		self.assertEqual(mostsec(-.10000000), "100 ms")
		self.assertEqual(mostsec(-.09999999), "99 ms")
		self.assertEqual(mostsec(-.0999999), "99 ms")
		self.assertEqual(mostsec(-.099999), "99 ms")
		self.assertEqual(mostsec(-.09999), "99 ms")
		self.assertEqual(mostsec(-.0999), "99 ms")
		self.assertEqual(mostsec(-.099), "99 ms")
		self.assertEqual(mostsec(-.009), "9 ms")
		self.assertEqual(mostsec(-.001), "1 ms")
		self.assertEqual(mostsec(-.0010), "1 ms")
		self.assertEqual(mostsec(-.00100), "1 ms")
		self.assertEqual(mostsec(-.001000), "1 ms")
		self.assertEqual(mostsec(-.0010000), "1 ms")
		self.assertEqual(mostsec(-.00100000), "1 ms")
		self.assertEqual(mostsec(-.00099999), "999 us")
		self.assertEqual(mostsec(-.0009999), "999 us")
		self.assertEqual(mostsec(-.000999), "999 us")
		self.assertEqual(mostsec(-.00099), "990 us")
		self.assertEqual(mostsec(-.0009), "900 us")
		self.assertEqual(mostsec(-.0001), "100 us")
		self.assertEqual(mostsec(-.00010), "100 us")
		self.assertEqual(mostsec(-.000100), "100 us")
		self.assertEqual(mostsec(-.0001000), "100 us")
		self.assertEqual(mostsec(-.00010000), "100 us")
		self.assertEqual(mostsec(-.00009999), "99 us")
		self.assertEqual(mostsec(-.0000999), "99 us")
		self.assertEqual(mostsec(-.000099), "99 us")
		self.assertEqual(mostsec(-.000009), "9 us")
		self.assertEqual(mostsec(-.000001), "1 us")
		self.assertEqual(mostsec(-.0000010), "1 us")
		self.assertEqual(mostsec(-.00000100), "1 us")
		self.assertEqual(mostsec(-.0000009999), "999 ns")
		self.assertEqual(mostsec(-.000000999), "999 ns")
		self.assertEqual(mostsec(-.00000099), "990 ns")
		self.assertEqual(mostsec(-.0000009), "900 ns")
		self.assertEqual(mostsec(-.0000001), "100 ns")
		self.assertEqual(mostsec(-.00000010), "100 ns")
		self.assertEqual(mostsec(-.000000100), "100 ns")
		self.assertEqual(mostsec(-.0000001000), "100 ns")
		self.assertEqual(mostsec(-.00000010000), "100 ns")
		self.assertEqual(mostsec(-.000000100000), "100 ns")
		self.assertEqual(mostsec(-.000000099999), "99 ns")
		self.assertEqual(mostsec(-.00000009999), "99 ns")
		self.assertEqual(mostsec(-.0000000999), "99 ns")
		self.assertEqual(mostsec(-.000000099), "99 ns")
		self.assertEqual(mostsec(-.000000009), "9 ns")
		self.assertEqual(mostsec(-.000000001), "1 ns")
		self.assertEqual(mostsec(-.0000000001), "<1 ns")

	def test_mostsec_str_float_lt_second(self):

		self.assertEqual(mostsec(".0", positive=True), None)
		self.assertEqual(mostsec(".0"), "<1 ns")
		self.assertEqual(mostsec(".99999999"), "999 ms")
		self.assertEqual(mostsec(".9999999"), "999 ms")
		self.assertEqual(mostsec(".999999"), "999 ms")
		self.assertEqual(mostsec(".99999"), "999 ms")
		self.assertEqual(mostsec(".9999"), "999 ms")
		self.assertEqual(mostsec(".999"), "999 ms")
		self.assertEqual(mostsec(".19999999"), "199 ms")
		self.assertEqual(mostsec(".1999999"), "199 ms")
		self.assertEqual(mostsec(".199999"), "199 ms")
		self.assertEqual(mostsec(".19999"), "199 ms")
		self.assertEqual(mostsec(".1999"), "199 ms")
		self.assertEqual(mostsec(".199"), "199 ms")
		self.assertEqual(mostsec(".19"), "190 ms")
		self.assertEqual(mostsec(".1"), "100 ms")
		self.assertEqual(mostsec(".10"), "100 ms")
		self.assertEqual(mostsec(".100"), "100 ms")
		self.assertEqual(mostsec(".1000"), "100 ms")
		self.assertEqual(mostsec(".10000"), "100 ms")
		self.assertEqual(mostsec(".100000"), "100 ms")
		self.assertEqual(mostsec(".1000000"), "100 ms")
		self.assertEqual(mostsec(".10000000"), "100 ms")
		self.assertEqual(mostsec(".09999999"), "99 ms")
		self.assertEqual(mostsec(".0999999"), "99 ms")
		self.assertEqual(mostsec(".099999"), "99 ms")
		self.assertEqual(mostsec(".09999"), "99 ms")
		self.assertEqual(mostsec(".0999"), "99 ms")
		self.assertEqual(mostsec(".099"), "99 ms")
		self.assertEqual(mostsec(".009"), "9 ms")
		self.assertEqual(mostsec(".001"), "1 ms")
		self.assertEqual(mostsec(".0010"), "1 ms")
		self.assertEqual(mostsec(".00100"), "1 ms")
		self.assertEqual(mostsec(".001000"), "1 ms")
		self.assertEqual(mostsec(".0010000"), "1 ms")
		self.assertEqual(mostsec(".00100000"), "1 ms")
		self.assertEqual(mostsec(".00099999"), "999 us")
		self.assertEqual(mostsec(".0009999"), "999 us")
		self.assertEqual(mostsec(".000999"), "999 us")
		self.assertEqual(mostsec(".00099"), "990 us")
		self.assertEqual(mostsec(".0009"), "900 us")
		self.assertEqual(mostsec(".0001"), "100 us")
		self.assertEqual(mostsec(".00010"), "100 us")
		self.assertEqual(mostsec(".000100"), "100 us")
		self.assertEqual(mostsec(".0001000"), "100 us")
		self.assertEqual(mostsec(".00010000"), "100 us")
		self.assertEqual(mostsec(".00009999"), "99 us")
		self.assertEqual(mostsec(".0000999"), "99 us")
		self.assertEqual(mostsec(".000099"), "99 us")
		self.assertEqual(mostsec(".000009"), "9 us")
		self.assertEqual(mostsec(".000001"), "1 us")
		self.assertEqual(mostsec(".0000010"), "1 us")
		self.assertEqual(mostsec(".00000100"), "1 us")
		self.assertEqual(mostsec(".0000009999"), "999 ns")
		self.assertEqual(mostsec(".000000999"), "999 ns")
		self.assertEqual(mostsec(".00000099"), "990 ns")
		self.assertEqual(mostsec(".0000009"), "900 ns")
		self.assertEqual(mostsec(".0000001"), "100 ns")
		self.assertEqual(mostsec(".00000010"), "100 ns")
		self.assertEqual(mostsec(".000000100"), "100 ns")
		self.assertEqual(mostsec(".0000001000"), "100 ns")
		self.assertEqual(mostsec(".00000010000"), "100 ns")
		self.assertEqual(mostsec(".000000100000"), "100 ns")
		self.assertEqual(mostsec(".000000099999"), "99 ns")
		self.assertEqual(mostsec(".00000009999"), "99 ns")
		self.assertEqual(mostsec(".0000000999"), "99 ns")
		self.assertEqual(mostsec(".000000099"), "99 ns")
		self.assertEqual(mostsec(".000000009"), "9 ns")
		self.assertEqual(mostsec(".000000001"), "1 ns")
		self.assertEqual(mostsec(".0000000001"), "<1 ns")

	def test_mostsec_str_float_lt_second_negative(self):

		self.assertEqual(mostsec("-.0", positive=True), None)
		self.assertEqual(mostsec("-.0"), "<1 ns")
		self.assertEqual(mostsec("-.99999999"), "999 ms")
		self.assertEqual(mostsec("-.9999999"), "999 ms")
		self.assertEqual(mostsec("-.999999"), "999 ms")
		self.assertEqual(mostsec("-.99999"), "999 ms")
		self.assertEqual(mostsec("-.9999"), "999 ms")
		self.assertEqual(mostsec("-.999"), "999 ms")
		self.assertEqual(mostsec("-.19999999"), "199 ms")
		self.assertEqual(mostsec("-.1999999"), "199 ms")
		self.assertEqual(mostsec("-.199999"), "199 ms")
		self.assertEqual(mostsec("-.19999"), "199 ms")
		self.assertEqual(mostsec("-.1999"), "199 ms")
		self.assertEqual(mostsec("-.199"), "199 ms")
		self.assertEqual(mostsec("-.19"), "190 ms")
		self.assertEqual(mostsec("-.1"), "100 ms")
		self.assertEqual(mostsec("-.10"), "100 ms")
		self.assertEqual(mostsec("-.100"), "100 ms")
		self.assertEqual(mostsec("-.1000"), "100 ms")
		self.assertEqual(mostsec("-.10000"), "100 ms")
		self.assertEqual(mostsec("-.100000"), "100 ms")
		self.assertEqual(mostsec("-.1000000"), "100 ms")
		self.assertEqual(mostsec("-.10000000"), "100 ms")
		self.assertEqual(mostsec("-.09999999"), "99 ms")
		self.assertEqual(mostsec("-.0999999"), "99 ms")
		self.assertEqual(mostsec("-.099999"), "99 ms")
		self.assertEqual(mostsec("-.09999"), "99 ms")
		self.assertEqual(mostsec("-.0999"), "99 ms")
		self.assertEqual(mostsec("-.099"), "99 ms")
		self.assertEqual(mostsec("-.009"), "9 ms")
		self.assertEqual(mostsec("-.001"), "1 ms")
		self.assertEqual(mostsec("-.0010"), "1 ms")
		self.assertEqual(mostsec("-.00100"), "1 ms")
		self.assertEqual(mostsec("-.001000"), "1 ms")
		self.assertEqual(mostsec("-.0010000"), "1 ms")
		self.assertEqual(mostsec("-.00100000"), "1 ms")
		self.assertEqual(mostsec("-.00099999"), "999 us")
		self.assertEqual(mostsec("-.0009999"), "999 us")
		self.assertEqual(mostsec("-.000999"), "999 us")
		self.assertEqual(mostsec("-.00099"), "990 us")
		self.assertEqual(mostsec("-.0009"), "900 us")
		self.assertEqual(mostsec("-.0001"), "100 us")
		self.assertEqual(mostsec("-.00010"), "100 us")
		self.assertEqual(mostsec("-.000100"), "100 us")
		self.assertEqual(mostsec("-.0001000"), "100 us")
		self.assertEqual(mostsec("-.00010000"), "100 us")
		self.assertEqual(mostsec("-.00009999"), "99 us")
		self.assertEqual(mostsec("-.0000999"), "99 us")
		self.assertEqual(mostsec("-.000099"), "99 us")
		self.assertEqual(mostsec("-.000009"), "9 us")
		self.assertEqual(mostsec("-.000001"), "1 us")
		self.assertEqual(mostsec("-.0000010"), "1 us")
		self.assertEqual(mostsec("-.00000100"), "1 us")
		self.assertEqual(mostsec("-.0000009999"), "999 ns")
		self.assertEqual(mostsec("-.000000999"), "999 ns")
		self.assertEqual(mostsec("-.00000099"), "990 ns")
		self.assertEqual(mostsec("-.0000009"), "900 ns")
		self.assertEqual(mostsec("-.0000001"), "100 ns")
		self.assertEqual(mostsec("-.00000010"), "100 ns")
		self.assertEqual(mostsec("-.000000100"), "100 ns")
		self.assertEqual(mostsec("-.0000001000"), "100 ns")
		self.assertEqual(mostsec("-.00000010000"), "100 ns")
		self.assertEqual(mostsec("-.000000100000"), "100 ns")
		self.assertEqual(mostsec("-.000000099999"), "99 ns")
		self.assertEqual(mostsec("-.00000009999"), "99 ns")
		self.assertEqual(mostsec("-.0000000999"), "99 ns")
		self.assertEqual(mostsec("-.000000099"), "99 ns")
		self.assertEqual(mostsec("-.000000009"), "9 ns")
		self.assertEqual(mostsec("-.000000001"), "1 ns")
		self.assertEqual(mostsec("-.0000000001"), "<1 ns")

	def test_mostsec_float_big_seconds(self):

		self.assertEqual(mostsec(1.999), "1 s")
		self.assertEqual(mostsec(59.999), "59 s")
		self.assertEqual(mostsec(60.999), "1 m")
		self.assertEqual(mostsec(61.999), "1 m 1 s")
		self.assertEqual(mostsec(119.999), "1 m 59 s")
		self.assertEqual(mostsec(120.999), "2 m")
		self.assertEqual(mostsec(120.999), "2 m")
		self.assertEqual(mostsec(3599.999), "59 m 59 s")
		self.assertEqual(mostsec(3600.999), "1 h")
		self.assertEqual(mostsec(3601.999), "1 h")
		self.assertEqual(mostsec(3659.999), "1 h")
		self.assertEqual(mostsec(3660.999), "1 h 1 m")
		self.assertEqual(mostsec(86399.999), "23 h 59 m")
		self.assertEqual(mostsec(86400.999), "1 d")
		self.assertEqual(mostsec(86401.999), "1 d")
		self.assertEqual(mostsec(86459.999), "1 d")
		self.assertEqual(mostsec(89999.999), "1 d")
		self.assertEqual(mostsec(90000.999), "1 d 1 h")
		self.assertEqual(mostsec(31535999.999), "364 d 23 h")
		self.assertEqual(mostsec(31536000.999), "365 d")
		self.assertEqual(mostsec(31539599.999), "365 d")
		self.assertEqual(mostsec(31539600.999), "365 d 1 h")

	def test_mostsec_float_big_seconds_negative(self):

		self.assertEqual(mostsec(-1.999), "1 s")
		self.assertEqual(mostsec(-59.999), "59 s")
		self.assertEqual(mostsec(-60.999), "1 m")
		self.assertEqual(mostsec(-61.999), "1 m 1 s")
		self.assertEqual(mostsec(-119.999), "1 m 59 s")
		self.assertEqual(mostsec(-120.999), "2 m")
		self.assertEqual(mostsec(-120.999), "2 m")
		self.assertEqual(mostsec(-3599.999), "59 m 59 s")
		self.assertEqual(mostsec(-3600.999), "1 h")
		self.assertEqual(mostsec(-3601.999), "1 h")
		self.assertEqual(mostsec(-3659.999), "1 h")
		self.assertEqual(mostsec(-3660.999), "1 h 1 m")
		self.assertEqual(mostsec(-86399.999), "23 h 59 m")
		self.assertEqual(mostsec(-86400.999), "1 d")
		self.assertEqual(mostsec(-86401.999), "1 d")
		self.assertEqual(mostsec(-86459.999), "1 d")
		self.assertEqual(mostsec(-89999.999), "1 d")
		self.assertEqual(mostsec(-90000.999), "1 d 1 h")
		self.assertEqual(mostsec(-31535999.999), "364 d 23 h")
		self.assertEqual(mostsec(-31536000.999), "365 d")
		self.assertEqual(mostsec(-31539599.999), "365 d")
		self.assertEqual(mostsec(-31539600.999), "365 d 1 h")

	def test_mostsec_str_float_big_seconds(self):

		self.assertEqual(mostsec("1.999"), "1 s")
		self.assertEqual(mostsec("59.999"), "59 s")
		self.assertEqual(mostsec("60.999"), "1 m")
		self.assertEqual(mostsec("61.999"), "1 m 1 s")
		self.assertEqual(mostsec("119.999"), "1 m 59 s")
		self.assertEqual(mostsec("120.999"), "2 m")
		self.assertEqual(mostsec("120.999"), "2 m")
		self.assertEqual(mostsec("3599.999"), "59 m 59 s")
		self.assertEqual(mostsec("3600.999"), "1 h")
		self.assertEqual(mostsec("3601.999"), "1 h")
		self.assertEqual(mostsec("3659.999"), "1 h")
		self.assertEqual(mostsec("3660.999"), "1 h 1 m")
		self.assertEqual(mostsec("86399.999"), "23 h 59 m")
		self.assertEqual(mostsec("86400.999"), "1 d")
		self.assertEqual(mostsec("86401.999"), "1 d")
		self.assertEqual(mostsec("86459.999"), "1 d")
		self.assertEqual(mostsec("89999.999"), "1 d")
		self.assertEqual(mostsec("90000.999"), "1 d 1 h")
		self.assertEqual(mostsec("31535999.999"), "364 d 23 h")
		self.assertEqual(mostsec("31536000.999"), "365 d")
		self.assertEqual(mostsec("31539599.999"), "365 d")
		self.assertEqual(mostsec("31539600.999"), "365 d 1 h")

	def test_mostsec_str_float_big_seconds_negative(self):

		self.assertEqual(mostsec("-1.999"), "1 s")
		self.assertEqual(mostsec("-59.999"), "59 s")
		self.assertEqual(mostsec("-60.999"), "1 m")
		self.assertEqual(mostsec("-61.999"), "1 m 1 s")
		self.assertEqual(mostsec("-119.999"), "1 m 59 s")
		self.assertEqual(mostsec("-120.999"), "2 m")
		self.assertEqual(mostsec("-120.999"), "2 m")
		self.assertEqual(mostsec("-3599.999"), "59 m 59 s")
		self.assertEqual(mostsec("-3600.999"), "1 h")
		self.assertEqual(mostsec("-3601.999"), "1 h")
		self.assertEqual(mostsec("-3659.999"), "1 h")
		self.assertEqual(mostsec("-3660.999"), "1 h 1 m")
		self.assertEqual(mostsec("-86399.999"), "23 h 59 m")
		self.assertEqual(mostsec("-86400.999"), "1 d")
		self.assertEqual(mostsec("-86401.999"), "1 d")
		self.assertEqual(mostsec("-86459.999"), "1 d")
		self.assertEqual(mostsec("-89999.999"), "1 d")
		self.assertEqual(mostsec("-90000.999"), "1 d 1 h")
		self.assertEqual(mostsec("-31535999.999"), "364 d 23 h")
		self.assertEqual(mostsec("-31536000.999"), "365 d")
		self.assertEqual(mostsec("-31539599.999"), "365 d")
		self.assertEqual(mostsec("-31539600.999"), "365 d 1 h")

	def test_mostsec_E_seconds(self):

		self.assertEqual(mostsec(1E5), "1 d 3 h")
		self.assertEqual(mostsec(-1E5), "1 d 3 h")
		self.assertEqual(mostsec("1E5"), "1 d 3 h")
		self.assertEqual(mostsec("-1E5"), "1 d 3 h")

	def test_mostsec_invalids(self):

		for invalid in (

			"integer", True, False, ..., None, print, unittest, Transmutable,
			[ 42 ],( 42, ),{ 42 },{ "value": 42 }
		):
			self.assertIsNone(mostsec(invalid))








	def test_mostsecfmt_int_seconds(self):

		self.assertEqual(self.posfmter(0), None)
		self.assertEqual(self.secfmter(0), "<1 ns")
		self.assertEqual(self.secfmter(1), "1 s")
		self.assertEqual(self.secfmter(59), "59 s")
		self.assertEqual(self.secfmter(60), "1 m")
		self.assertEqual(self.secfmter(61), "1 m 1 s")
		self.assertEqual(self.secfmter(119), "1 m 59 s")
		self.assertEqual(self.secfmter(120), "2 m")
		self.assertEqual(self.secfmter(120), "2 m")
		self.assertEqual(self.secfmter(3599), "59 m 59 s")
		self.assertEqual(self.secfmter(3600), "1 h")
		self.assertEqual(self.secfmter(3601), "1 h")
		self.assertEqual(self.secfmter(3659), "1 h")
		self.assertEqual(self.secfmter(3660), "1 h 1 m")
		self.assertEqual(self.secfmter(86399), "23 h 59 m")
		self.assertEqual(self.secfmter(86400), "1 d")
		self.assertEqual(self.secfmter(86401), "1 d")
		self.assertEqual(self.secfmter(86459), "1 d")
		self.assertEqual(self.secfmter(89999), "1 d")
		self.assertEqual(self.secfmter(90000), "1 d 1 h")
		self.assertEqual(self.secfmter(31535999), "364 d 23 h")
		self.assertEqual(self.secfmter(31536000), "365 d")
		self.assertEqual(self.secfmter(31539599), "365 d")
		self.assertEqual(self.secfmter(31539600), "365 d 1 h")

	def test_mostsecfmt_int_seconds_negative(self):

		self.assertEqual(self.posfmter(-0), None)
		self.assertEqual(self.secfmter(-0), "<1 ns")
		self.assertEqual(self.secfmter(-1), "1 s")
		self.assertEqual(self.secfmter(-59), "59 s")
		self.assertEqual(self.secfmter(-60), "1 m")
		self.assertEqual(self.secfmter(-61), "1 m 1 s")
		self.assertEqual(self.secfmter(-119), "1 m 59 s")
		self.assertEqual(self.secfmter(-120), "2 m")
		self.assertEqual(self.secfmter(-120), "2 m")
		self.assertEqual(self.secfmter(-3599), "59 m 59 s")
		self.assertEqual(self.secfmter(-3600), "1 h")
		self.assertEqual(self.secfmter(-3601), "1 h")
		self.assertEqual(self.secfmter(-3659), "1 h")
		self.assertEqual(self.secfmter(-3660), "1 h 1 m")
		self.assertEqual(self.secfmter(-86399), "23 h 59 m")
		self.assertEqual(self.secfmter(-86400), "1 d")
		self.assertEqual(self.secfmter(-86401), "1 d")
		self.assertEqual(self.secfmter(-86459), "1 d")
		self.assertEqual(self.secfmter(-89999), "1 d")
		self.assertEqual(self.secfmter(-90000), "1 d 1 h")
		self.assertEqual(self.secfmter(-31535999), "364 d 23 h")
		self.assertEqual(self.secfmter(-31536000), "365 d")
		self.assertEqual(self.secfmter(-31539599), "365 d")
		self.assertEqual(self.secfmter(-31539600), "365 d 1 h")

	def test_mostsecfmt_str_int_seconds(self):

		self.assertEqual(self.posfmter("0"), None)
		self.assertEqual(self.secfmter("0"), "<1 ns")
		self.assertEqual(self.secfmter("1"), "1 s")
		self.assertEqual(self.secfmter("59"), "59 s")
		self.assertEqual(self.secfmter("60"), "1 m")
		self.assertEqual(self.secfmter("61"), "1 m 1 s")
		self.assertEqual(self.secfmter("119"), "1 m 59 s")
		self.assertEqual(self.secfmter("120"), "2 m")
		self.assertEqual(self.secfmter("120"), "2 m")
		self.assertEqual(self.secfmter("3599"), "59 m 59 s")
		self.assertEqual(self.secfmter("3600"), "1 h")
		self.assertEqual(self.secfmter("3601"), "1 h")
		self.assertEqual(self.secfmter("3659"), "1 h")
		self.assertEqual(self.secfmter("3660"), "1 h 1 m")
		self.assertEqual(self.secfmter("86399"), "23 h 59 m")
		self.assertEqual(self.secfmter("86400"), "1 d")
		self.assertEqual(self.secfmter("86401"), "1 d")
		self.assertEqual(self.secfmter("86459"), "1 d")
		self.assertEqual(self.secfmter("89999"), "1 d")
		self.assertEqual(self.secfmter("90000"), "1 d 1 h")
		self.assertEqual(self.secfmter("31535999"), "364 d 23 h")
		self.assertEqual(self.secfmter("31536000"), "365 d")
		self.assertEqual(self.secfmter("31539599"), "365 d")
		self.assertEqual(self.secfmter("31539600"), "365 d 1 h")

	def test_mostsecfmt_str_int_seconds_negative(self):

		self.assertEqual(self.posfmter("-0"), None)
		self.assertEqual(self.secfmter("-0"), "<1 ns")
		self.assertEqual(self.secfmter("-1"), "1 s")
		self.assertEqual(self.secfmter("-59"), "59 s")
		self.assertEqual(self.secfmter("-60"), "1 m")
		self.assertEqual(self.secfmter("-61"), "1 m 1 s")
		self.assertEqual(self.secfmter("-119"), "1 m 59 s")
		self.assertEqual(self.secfmter("-120"), "2 m")
		self.assertEqual(self.secfmter("-120"), "2 m")
		self.assertEqual(self.secfmter("-3599"), "59 m 59 s")
		self.assertEqual(self.secfmter("-3600"), "1 h")
		self.assertEqual(self.secfmter("-3601"), "1 h")
		self.assertEqual(self.secfmter("-3659"), "1 h")
		self.assertEqual(self.secfmter("-3660"), "1 h 1 m")
		self.assertEqual(self.secfmter("-86399"), "23 h 59 m")
		self.assertEqual(self.secfmter("-86400"), "1 d")
		self.assertEqual(self.secfmter("-86401"), "1 d")
		self.assertEqual(self.secfmter("-86459"), "1 d")
		self.assertEqual(self.secfmter("-89999"), "1 d")
		self.assertEqual(self.secfmter("-90000"), "1 d 1 h")
		self.assertEqual(self.secfmter("-31535999"), "364 d 23 h")
		self.assertEqual(self.secfmter("-31536000"), "365 d")
		self.assertEqual(self.secfmter("-31539599"), "365 d")
		self.assertEqual(self.secfmter("-31539600"), "365 d 1 h")

	def test_mostsecfmt_float_seconds(self):

		self.assertEqual(self.posfmter(0.), None)
		self.assertEqual(self.secfmter(0.), "<1 ns")
		self.assertEqual(self.secfmter(1.), "1 s")
		self.assertEqual(self.secfmter(59.), "59 s")
		self.assertEqual(self.secfmter(60.), "1 m")
		self.assertEqual(self.secfmter(61.), "1 m 1 s")
		self.assertEqual(self.secfmter(119.), "1 m 59 s")
		self.assertEqual(self.secfmter(120.), "2 m")
		self.assertEqual(self.secfmter(120.), "2 m")
		self.assertEqual(self.secfmter(3599.), "59 m 59 s")
		self.assertEqual(self.secfmter(3600.), "1 h")
		self.assertEqual(self.secfmter(3601.), "1 h")
		self.assertEqual(self.secfmter(3659.), "1 h")
		self.assertEqual(self.secfmter(3660.), "1 h 1 m")
		self.assertEqual(self.secfmter(86399.), "23 h 59 m")
		self.assertEqual(self.secfmter(86400.), "1 d")
		self.assertEqual(self.secfmter(86401.), "1 d")
		self.assertEqual(self.secfmter(86459.), "1 d")
		self.assertEqual(self.secfmter(89999.), "1 d")
		self.assertEqual(self.secfmter(90000.), "1 d 1 h")
		self.assertEqual(self.secfmter(31535999.), "364 d 23 h")
		self.assertEqual(self.secfmter(31536000.), "365 d")
		self.assertEqual(self.secfmter(31539599.), "365 d")
		self.assertEqual(self.secfmter(31539600.), "365 d 1 h")

	def test_mostsecfmt_float_seconds_negative(self):

		self.assertEqual(self.posfmter(-0.), None)
		self.assertEqual(self.secfmter(-0.), "<1 ns")
		self.assertEqual(self.secfmter(-1.), "1 s")
		self.assertEqual(self.secfmter(-59.), "59 s")
		self.assertEqual(self.secfmter(-60.), "1 m")
		self.assertEqual(self.secfmter(-61.), "1 m 1 s")
		self.assertEqual(self.secfmter(-119.), "1 m 59 s")
		self.assertEqual(self.secfmter(-120.), "2 m")
		self.assertEqual(self.secfmter(-120.), "2 m")
		self.assertEqual(self.secfmter(-3599.), "59 m 59 s")
		self.assertEqual(self.secfmter(-3600.), "1 h")
		self.assertEqual(self.secfmter(-3601.), "1 h")
		self.assertEqual(self.secfmter(-3659.), "1 h")
		self.assertEqual(self.secfmter(-3660.), "1 h 1 m")
		self.assertEqual(self.secfmter(-86399.), "23 h 59 m")
		self.assertEqual(self.secfmter(-86400.), "1 d")
		self.assertEqual(self.secfmter(-86401.), "1 d")
		self.assertEqual(self.secfmter(-86459.), "1 d")
		self.assertEqual(self.secfmter(-89999.), "1 d")
		self.assertEqual(self.secfmter(-90000.), "1 d 1 h")
		self.assertEqual(self.secfmter(-31535999.), "364 d 23 h")
		self.assertEqual(self.secfmter(-31536000.), "365 d")
		self.assertEqual(self.secfmter(-31539599.), "365 d")
		self.assertEqual(self.secfmter(-31539600.), "365 d 1 h")

	def test_mostsecfmt_str_float_seconds(self):

		self.assertEqual(self.posfmter("0."), None)
		self.assertEqual(self.secfmter("0."), "<1 ns")
		self.assertEqual(self.secfmter("1."), "1 s")
		self.assertEqual(self.secfmter("59."), "59 s")
		self.assertEqual(self.secfmter("60."), "1 m")
		self.assertEqual(self.secfmter("61."), "1 m 1 s")
		self.assertEqual(self.secfmter("119."), "1 m 59 s")
		self.assertEqual(self.secfmter("120."), "2 m")
		self.assertEqual(self.secfmter("120."), "2 m")
		self.assertEqual(self.secfmter("3599."), "59 m 59 s")
		self.assertEqual(self.secfmter("3600."), "1 h")
		self.assertEqual(self.secfmter("3601."), "1 h")
		self.assertEqual(self.secfmter("3659."), "1 h")
		self.assertEqual(self.secfmter("3660."), "1 h 1 m")
		self.assertEqual(self.secfmter("86399."), "23 h 59 m")
		self.assertEqual(self.secfmter("86400."), "1 d")
		self.assertEqual(self.secfmter("86401."), "1 d")
		self.assertEqual(self.secfmter("86459."), "1 d")
		self.assertEqual(self.secfmter("89999."), "1 d")
		self.assertEqual(self.secfmter("90000."), "1 d 1 h")
		self.assertEqual(self.secfmter("90000."), "1 d 1 h")
		self.assertEqual(self.secfmter("31535999."), "364 d 23 h")
		self.assertEqual(self.secfmter("31536000."), "365 d")
		self.assertEqual(self.secfmter("31539599."), "365 d")
		self.assertEqual(self.secfmter("31539600."), "365 d 1 h")

	def test_mostsecfmt_str_float_seconds_negative(self):

		self.assertEqual(self.posfmter("-0."), None)
		self.assertEqual(self.secfmter("-0."), "<1 ns")
		self.assertEqual(self.secfmter("-1."), "1 s")
		self.assertEqual(self.secfmter("-59."), "59 s")
		self.assertEqual(self.secfmter("-60."), "1 m")
		self.assertEqual(self.secfmter("-61."), "1 m 1 s")
		self.assertEqual(self.secfmter("-119."), "1 m 59 s")
		self.assertEqual(self.secfmter("-120."), "2 m")
		self.assertEqual(self.secfmter("-120."), "2 m")
		self.assertEqual(self.secfmter("-3599."), "59 m 59 s")
		self.assertEqual(self.secfmter("-3600."), "1 h")
		self.assertEqual(self.secfmter("-3601."), "1 h")
		self.assertEqual(self.secfmter("-3659."), "1 h")
		self.assertEqual(self.secfmter("-3660."), "1 h 1 m")
		self.assertEqual(self.secfmter("-86399."), "23 h 59 m")
		self.assertEqual(self.secfmter("-86400."), "1 d")
		self.assertEqual(self.secfmter("-86401."), "1 d")
		self.assertEqual(self.secfmter("-86459."), "1 d")
		self.assertEqual(self.secfmter("-89999."), "1 d")
		self.assertEqual(self.secfmter("-90000."), "1 d 1 h")
		self.assertEqual(self.secfmter("-31535999."), "364 d 23 h")
		self.assertEqual(self.secfmter("-31536000."), "365 d")
		self.assertEqual(self.secfmter("-31539599."), "365 d")
		self.assertEqual(self.secfmter("-31539600."), "365 d 1 h")

	def test_mostsecfmt_float_lt_second(self):

		self.assertEqual(self.posfmter(.0), None)
		self.assertEqual(self.secfmter(.0), "<1 ns")
		self.assertEqual(self.secfmter(.99999999), "999 ms")
		self.assertEqual(self.secfmter(.9999999), "999 ms")
		self.assertEqual(self.secfmter(.999999), "999 ms")
		self.assertEqual(self.secfmter(.99999), "999 ms")
		self.assertEqual(self.secfmter(.9999), "999 ms")
		self.assertEqual(self.secfmter(.999), "999 ms")
		self.assertEqual(self.secfmter(.19999999), "199 ms")
		self.assertEqual(self.secfmter(.1999999), "199 ms")
		self.assertEqual(self.secfmter(.199999), "199 ms")
		self.assertEqual(self.secfmter(.19999), "199 ms")
		self.assertEqual(self.secfmter(.1999), "199 ms")
		self.assertEqual(self.secfmter(.199), "199 ms")
		self.assertEqual(self.secfmter(.19), "190 ms")
		self.assertEqual(self.secfmter(.1), "100 ms")
		self.assertEqual(self.secfmter(.10), "100 ms")
		self.assertEqual(self.secfmter(.100), "100 ms")
		self.assertEqual(self.secfmter(.1000), "100 ms")
		self.assertEqual(self.secfmter(.10000), "100 ms")
		self.assertEqual(self.secfmter(.100000), "100 ms")
		self.assertEqual(self.secfmter(.1000000), "100 ms")
		self.assertEqual(self.secfmter(.10000000), "100 ms")
		self.assertEqual(self.secfmter(.09999999), "99 ms")
		self.assertEqual(self.secfmter(.0999999), "99 ms")
		self.assertEqual(self.secfmter(.099999), "99 ms")
		self.assertEqual(self.secfmter(.09999), "99 ms")
		self.assertEqual(self.secfmter(.0999), "99 ms")
		self.assertEqual(self.secfmter(.099), "99 ms")
		self.assertEqual(self.secfmter(.009), "9 ms")
		self.assertEqual(self.secfmter(.001), "1 ms")
		self.assertEqual(self.secfmter(.0010), "1 ms")
		self.assertEqual(self.secfmter(.00100), "1 ms")
		self.assertEqual(self.secfmter(.001000), "1 ms")
		self.assertEqual(self.secfmter(.0010000), "1 ms")
		self.assertEqual(self.secfmter(.00100000), "1 ms")
		self.assertEqual(self.secfmter(.00099999), "999 us")
		self.assertEqual(self.secfmter(.0009999), "999 us")
		self.assertEqual(self.secfmter(.000999), "999 us")
		self.assertEqual(self.secfmter(.00099), "990 us")
		self.assertEqual(self.secfmter(.0009), "900 us")
		self.assertEqual(self.secfmter(.0001), "100 us")
		self.assertEqual(self.secfmter(.00010), "100 us")
		self.assertEqual(self.secfmter(.000100), "100 us")
		self.assertEqual(self.secfmter(.0001000), "100 us")
		self.assertEqual(self.secfmter(.00010000), "100 us")
		self.assertEqual(self.secfmter(.00009999), "99 us")
		self.assertEqual(self.secfmter(.0000999), "99 us")
		self.assertEqual(self.secfmter(.000099), "99 us")
		self.assertEqual(self.secfmter(.000009), "9 us")
		self.assertEqual(self.secfmter(.000001), "1 us")
		self.assertEqual(self.secfmter(.0000010), "1 us")
		self.assertEqual(self.secfmter(.00000100), "1 us")
		self.assertEqual(self.secfmter(.0000009999), "999 ns")
		self.assertEqual(self.secfmter(.000000999), "999 ns")
		self.assertEqual(self.secfmter(.00000099), "990 ns")
		self.assertEqual(self.secfmter(.0000009), "900 ns")
		self.assertEqual(self.secfmter(.0000001), "100 ns")
		self.assertEqual(self.secfmter(.00000010), "100 ns")
		self.assertEqual(self.secfmter(.000000100), "100 ns")
		self.assertEqual(self.secfmter(.0000001000), "100 ns")
		self.assertEqual(self.secfmter(.00000010000), "100 ns")
		self.assertEqual(self.secfmter(.000000100000), "100 ns")
		self.assertEqual(self.secfmter(.000000099999), "99 ns")
		self.assertEqual(self.secfmter(.00000009999), "99 ns")
		self.assertEqual(self.secfmter(.0000000999), "99 ns")
		self.assertEqual(self.secfmter(.000000099), "99 ns")
		self.assertEqual(self.secfmter(.000000009), "9 ns")
		self.assertEqual(self.secfmter(.000000001), "1 ns")
		self.assertEqual(self.secfmter(.0000000001), "<1 ns")

	def test_mostsecfmt_float_lt_second_negative(self):

		self.assertEqual(self.posfmter(-.0), None)
		self.assertEqual(self.secfmter(-.0), "<1 ns")
		self.assertEqual(self.secfmter(-.99999999), "999 ms")
		self.assertEqual(self.secfmter(-.9999999), "999 ms")
		self.assertEqual(self.secfmter(-.999999), "999 ms")
		self.assertEqual(self.secfmter(-.99999), "999 ms")
		self.assertEqual(self.secfmter(-.9999), "999 ms")
		self.assertEqual(self.secfmter(-.999), "999 ms")
		self.assertEqual(self.secfmter(-.19999999), "199 ms")
		self.assertEqual(self.secfmter(-.1999999), "199 ms")
		self.assertEqual(self.secfmter(-.199999), "199 ms")
		self.assertEqual(self.secfmter(-.19999), "199 ms")
		self.assertEqual(self.secfmter(-.1999), "199 ms")
		self.assertEqual(self.secfmter(-.199), "199 ms")
		self.assertEqual(self.secfmter(-.19), "190 ms")
		self.assertEqual(self.secfmter(-.1), "100 ms")
		self.assertEqual(self.secfmter(-.10), "100 ms")
		self.assertEqual(self.secfmter(-.100), "100 ms")
		self.assertEqual(self.secfmter(-.1000), "100 ms")
		self.assertEqual(self.secfmter(-.10000), "100 ms")
		self.assertEqual(self.secfmter(-.100000), "100 ms")
		self.assertEqual(self.secfmter(-.1000000), "100 ms")
		self.assertEqual(self.secfmter(-.10000000), "100 ms")
		self.assertEqual(self.secfmter(-.09999999), "99 ms")
		self.assertEqual(self.secfmter(-.0999999), "99 ms")
		self.assertEqual(self.secfmter(-.099999), "99 ms")
		self.assertEqual(self.secfmter(-.09999), "99 ms")
		self.assertEqual(self.secfmter(-.0999), "99 ms")
		self.assertEqual(self.secfmter(-.099), "99 ms")
		self.assertEqual(self.secfmter(-.009), "9 ms")
		self.assertEqual(self.secfmter(-.001), "1 ms")
		self.assertEqual(self.secfmter(-.0010), "1 ms")
		self.assertEqual(self.secfmter(-.00100), "1 ms")
		self.assertEqual(self.secfmter(-.001000), "1 ms")
		self.assertEqual(self.secfmter(-.0010000), "1 ms")
		self.assertEqual(self.secfmter(-.00100000), "1 ms")
		self.assertEqual(self.secfmter(-.00099999), "999 us")
		self.assertEqual(self.secfmter(-.0009999), "999 us")
		self.assertEqual(self.secfmter(-.000999), "999 us")
		self.assertEqual(self.secfmter(-.00099), "990 us")
		self.assertEqual(self.secfmter(-.0009), "900 us")
		self.assertEqual(self.secfmter(-.0001), "100 us")
		self.assertEqual(self.secfmter(-.00010), "100 us")
		self.assertEqual(self.secfmter(-.000100), "100 us")
		self.assertEqual(self.secfmter(-.0001000), "100 us")
		self.assertEqual(self.secfmter(-.00010000), "100 us")
		self.assertEqual(self.secfmter(-.00009999), "99 us")
		self.assertEqual(self.secfmter(-.0000999), "99 us")
		self.assertEqual(self.secfmter(-.000099), "99 us")
		self.assertEqual(self.secfmter(-.000009), "9 us")
		self.assertEqual(self.secfmter(-.000001), "1 us")
		self.assertEqual(self.secfmter(-.0000010), "1 us")
		self.assertEqual(self.secfmter(-.00000100), "1 us")
		self.assertEqual(self.secfmter(-.0000009999), "999 ns")
		self.assertEqual(self.secfmter(-.000000999), "999 ns")
		self.assertEqual(self.secfmter(-.00000099), "990 ns")
		self.assertEqual(self.secfmter(-.0000009), "900 ns")
		self.assertEqual(self.secfmter(-.0000001), "100 ns")
		self.assertEqual(self.secfmter(-.00000010), "100 ns")
		self.assertEqual(self.secfmter(-.000000100), "100 ns")
		self.assertEqual(self.secfmter(-.0000001000), "100 ns")
		self.assertEqual(self.secfmter(-.00000010000), "100 ns")
		self.assertEqual(self.secfmter(-.000000100000), "100 ns")
		self.assertEqual(self.secfmter(-.000000099999), "99 ns")
		self.assertEqual(self.secfmter(-.00000009999), "99 ns")
		self.assertEqual(self.secfmter(-.0000000999), "99 ns")
		self.assertEqual(self.secfmter(-.000000099), "99 ns")
		self.assertEqual(self.secfmter(-.000000009), "9 ns")
		self.assertEqual(self.secfmter(-.000000001), "1 ns")
		self.assertEqual(self.secfmter(-.0000000001), "<1 ns")

	def test_mostsecfmt_str_float_lt_second(self):

		self.assertEqual(self.posfmter(".0"), None)
		self.assertEqual(self.secfmter(".0"), "<1 ns")
		self.assertEqual(self.secfmter(".99999999"), "999 ms")
		self.assertEqual(self.secfmter(".9999999"), "999 ms")
		self.assertEqual(self.secfmter(".999999"), "999 ms")
		self.assertEqual(self.secfmter(".99999"), "999 ms")
		self.assertEqual(self.secfmter(".9999"), "999 ms")
		self.assertEqual(self.secfmter(".999"), "999 ms")
		self.assertEqual(self.secfmter(".19999999"), "199 ms")
		self.assertEqual(self.secfmter(".1999999"), "199 ms")
		self.assertEqual(self.secfmter(".199999"), "199 ms")
		self.assertEqual(self.secfmter(".19999"), "199 ms")
		self.assertEqual(self.secfmter(".1999"), "199 ms")
		self.assertEqual(self.secfmter(".199"), "199 ms")
		self.assertEqual(self.secfmter(".19"), "190 ms")
		self.assertEqual(self.secfmter(".1"), "100 ms")
		self.assertEqual(self.secfmter(".10"), "100 ms")
		self.assertEqual(self.secfmter(".100"), "100 ms")
		self.assertEqual(self.secfmter(".1000"), "100 ms")
		self.assertEqual(self.secfmter(".10000"), "100 ms")
		self.assertEqual(self.secfmter(".100000"), "100 ms")
		self.assertEqual(self.secfmter(".1000000"), "100 ms")
		self.assertEqual(self.secfmter(".10000000"), "100 ms")
		self.assertEqual(self.secfmter(".09999999"), "99 ms")
		self.assertEqual(self.secfmter(".0999999"), "99 ms")
		self.assertEqual(self.secfmter(".099999"), "99 ms")
		self.assertEqual(self.secfmter(".09999"), "99 ms")
		self.assertEqual(self.secfmter(".0999"), "99 ms")
		self.assertEqual(self.secfmter(".099"), "99 ms")
		self.assertEqual(self.secfmter(".009"), "9 ms")
		self.assertEqual(self.secfmter(".001"), "1 ms")
		self.assertEqual(self.secfmter(".0010"), "1 ms")
		self.assertEqual(self.secfmter(".00100"), "1 ms")
		self.assertEqual(self.secfmter(".001000"), "1 ms")
		self.assertEqual(self.secfmter(".0010000"), "1 ms")
		self.assertEqual(self.secfmter(".00100000"), "1 ms")
		self.assertEqual(self.secfmter(".00099999"), "999 us")
		self.assertEqual(self.secfmter(".0009999"), "999 us")
		self.assertEqual(self.secfmter(".000999"), "999 us")
		self.assertEqual(self.secfmter(".00099"), "990 us")
		self.assertEqual(self.secfmter(".0009"), "900 us")
		self.assertEqual(self.secfmter(".0001"), "100 us")
		self.assertEqual(self.secfmter(".00010"), "100 us")
		self.assertEqual(self.secfmter(".000100"), "100 us")
		self.assertEqual(self.secfmter(".0001000"), "100 us")
		self.assertEqual(self.secfmter(".00010000"), "100 us")
		self.assertEqual(self.secfmter(".00009999"), "99 us")
		self.assertEqual(self.secfmter(".0000999"), "99 us")
		self.assertEqual(self.secfmter(".000099"), "99 us")
		self.assertEqual(self.secfmter(".000009"), "9 us")
		self.assertEqual(self.secfmter(".000001"), "1 us")
		self.assertEqual(self.secfmter(".0000010"), "1 us")
		self.assertEqual(self.secfmter(".00000100"), "1 us")
		self.assertEqual(self.secfmter(".0000009999"), "999 ns")
		self.assertEqual(self.secfmter(".000000999"), "999 ns")
		self.assertEqual(self.secfmter(".00000099"), "990 ns")
		self.assertEqual(self.secfmter(".0000009"), "900 ns")
		self.assertEqual(self.secfmter(".0000001"), "100 ns")
		self.assertEqual(self.secfmter(".00000010"), "100 ns")
		self.assertEqual(self.secfmter(".000000100"), "100 ns")
		self.assertEqual(self.secfmter(".0000001000"), "100 ns")
		self.assertEqual(self.secfmter(".00000010000"), "100 ns")
		self.assertEqual(self.secfmter(".000000100000"), "100 ns")
		self.assertEqual(self.secfmter(".000000099999"), "99 ns")
		self.assertEqual(self.secfmter(".00000009999"), "99 ns")
		self.assertEqual(self.secfmter(".0000000999"), "99 ns")
		self.assertEqual(self.secfmter(".000000099"), "99 ns")
		self.assertEqual(self.secfmter(".000000009"), "9 ns")
		self.assertEqual(self.secfmter(".000000001"), "1 ns")
		self.assertEqual(self.secfmter(".0000000001"), "<1 ns")

	def test_mostsecfmt_str_float_lt_second_negative(self):

		self.assertEqual(self.posfmter("-.0"), None)
		self.assertEqual(self.secfmter("-.0"), "<1 ns")
		self.assertEqual(self.secfmter("-.99999999"), "999 ms")
		self.assertEqual(self.secfmter("-.9999999"), "999 ms")
		self.assertEqual(self.secfmter("-.999999"), "999 ms")
		self.assertEqual(self.secfmter("-.99999"), "999 ms")
		self.assertEqual(self.secfmter("-.9999"), "999 ms")
		self.assertEqual(self.secfmter("-.999"), "999 ms")
		self.assertEqual(self.secfmter("-.19999999"), "199 ms")
		self.assertEqual(self.secfmter("-.1999999"), "199 ms")
		self.assertEqual(self.secfmter("-.199999"), "199 ms")
		self.assertEqual(self.secfmter("-.19999"), "199 ms")
		self.assertEqual(self.secfmter("-.1999"), "199 ms")
		self.assertEqual(self.secfmter("-.199"), "199 ms")
		self.assertEqual(self.secfmter("-.19"), "190 ms")
		self.assertEqual(self.secfmter("-.1"), "100 ms")
		self.assertEqual(self.secfmter("-.10"), "100 ms")
		self.assertEqual(self.secfmter("-.100"), "100 ms")
		self.assertEqual(self.secfmter("-.1000"), "100 ms")
		self.assertEqual(self.secfmter("-.10000"), "100 ms")
		self.assertEqual(self.secfmter("-.100000"), "100 ms")
		self.assertEqual(self.secfmter("-.1000000"), "100 ms")
		self.assertEqual(self.secfmter("-.10000000"), "100 ms")
		self.assertEqual(self.secfmter("-.09999999"), "99 ms")
		self.assertEqual(self.secfmter("-.0999999"), "99 ms")
		self.assertEqual(self.secfmter("-.099999"), "99 ms")
		self.assertEqual(self.secfmter("-.09999"), "99 ms")
		self.assertEqual(self.secfmter("-.0999"), "99 ms")
		self.assertEqual(self.secfmter("-.099"), "99 ms")
		self.assertEqual(self.secfmter("-.009"), "9 ms")
		self.assertEqual(self.secfmter("-.001"), "1 ms")
		self.assertEqual(self.secfmter("-.0010"), "1 ms")
		self.assertEqual(self.secfmter("-.00100"), "1 ms")
		self.assertEqual(self.secfmter("-.001000"), "1 ms")
		self.assertEqual(self.secfmter("-.0010000"), "1 ms")
		self.assertEqual(self.secfmter("-.00100000"), "1 ms")
		self.assertEqual(self.secfmter("-.00099999"), "999 us")
		self.assertEqual(self.secfmter("-.0009999"), "999 us")
		self.assertEqual(self.secfmter("-.000999"), "999 us")
		self.assertEqual(self.secfmter("-.00099"), "990 us")
		self.assertEqual(self.secfmter("-.0009"), "900 us")
		self.assertEqual(self.secfmter("-.0001"), "100 us")
		self.assertEqual(self.secfmter("-.00010"), "100 us")
		self.assertEqual(self.secfmter("-.000100"), "100 us")
		self.assertEqual(self.secfmter("-.0001000"), "100 us")
		self.assertEqual(self.secfmter("-.00010000"), "100 us")
		self.assertEqual(self.secfmter("-.00009999"), "99 us")
		self.assertEqual(self.secfmter("-.0000999"), "99 us")
		self.assertEqual(self.secfmter("-.000099"), "99 us")
		self.assertEqual(self.secfmter("-.000009"), "9 us")
		self.assertEqual(self.secfmter("-.000001"), "1 us")
		self.assertEqual(self.secfmter("-.0000010"), "1 us")
		self.assertEqual(self.secfmter("-.00000100"), "1 us")
		self.assertEqual(self.secfmter("-.0000009999"), "999 ns")
		self.assertEqual(self.secfmter("-.000000999"), "999 ns")
		self.assertEqual(self.secfmter("-.00000099"), "990 ns")
		self.assertEqual(self.secfmter("-.0000009"), "900 ns")
		self.assertEqual(self.secfmter("-.0000001"), "100 ns")
		self.assertEqual(self.secfmter("-.00000010"), "100 ns")
		self.assertEqual(self.secfmter("-.000000100"), "100 ns")
		self.assertEqual(self.secfmter("-.0000001000"), "100 ns")
		self.assertEqual(self.secfmter("-.00000010000"), "100 ns")
		self.assertEqual(self.secfmter("-.000000100000"), "100 ns")
		self.assertEqual(self.secfmter("-.000000099999"), "99 ns")
		self.assertEqual(self.secfmter("-.00000009999"), "99 ns")
		self.assertEqual(self.secfmter("-.0000000999"), "99 ns")
		self.assertEqual(self.secfmter("-.000000099"), "99 ns")
		self.assertEqual(self.secfmter("-.000000009"), "9 ns")
		self.assertEqual(self.secfmter("-.000000001"), "1 ns")
		self.assertEqual(self.secfmter("-.0000000001"), "<1 ns")

	def test_mostsecfmt_float_big_seconds(self):

		self.assertEqual(self.secfmter(1.999), "1 s")
		self.assertEqual(self.secfmter(59.999), "59 s")
		self.assertEqual(self.secfmter(60.999), "1 m")
		self.assertEqual(self.secfmter(61.999), "1 m 1 s")
		self.assertEqual(self.secfmter(119.999), "1 m 59 s")
		self.assertEqual(self.secfmter(120.999), "2 m")
		self.assertEqual(self.secfmter(120.999), "2 m")
		self.assertEqual(self.secfmter(3599.999), "59 m 59 s")
		self.assertEqual(self.secfmter(3600.999), "1 h")
		self.assertEqual(self.secfmter(3601.999), "1 h")
		self.assertEqual(self.secfmter(3659.999), "1 h")
		self.assertEqual(self.secfmter(3660.999), "1 h 1 m")
		self.assertEqual(self.secfmter(86399.999), "23 h 59 m")
		self.assertEqual(self.secfmter(86400.999), "1 d")
		self.assertEqual(self.secfmter(86401.999), "1 d")
		self.assertEqual(self.secfmter(86459.999), "1 d")
		self.assertEqual(self.secfmter(89999.999), "1 d")
		self.assertEqual(self.secfmter(90000.999), "1 d 1 h")
		self.assertEqual(self.secfmter(31535999.999), "364 d 23 h")
		self.assertEqual(self.secfmter(31536000.999), "365 d")
		self.assertEqual(self.secfmter(31539599.999), "365 d")
		self.assertEqual(self.secfmter(31539600.999), "365 d 1 h")

	def test_mostsecfmt_float_big_seconds_negative(self):

		self.assertEqual(self.secfmter(-1.999), "1 s")
		self.assertEqual(self.secfmter(-59.999), "59 s")
		self.assertEqual(self.secfmter(-60.999), "1 m")
		self.assertEqual(self.secfmter(-61.999), "1 m 1 s")
		self.assertEqual(self.secfmter(-119.999), "1 m 59 s")
		self.assertEqual(self.secfmter(-120.999), "2 m")
		self.assertEqual(self.secfmter(-120.999), "2 m")
		self.assertEqual(self.secfmter(-3599.999), "59 m 59 s")
		self.assertEqual(self.secfmter(-3600.999), "1 h")
		self.assertEqual(self.secfmter(-3601.999), "1 h")
		self.assertEqual(self.secfmter(-3659.999), "1 h")
		self.assertEqual(self.secfmter(-3660.999), "1 h 1 m")
		self.assertEqual(self.secfmter(-86399.999), "23 h 59 m")
		self.assertEqual(self.secfmter(-86400.999), "1 d")
		self.assertEqual(self.secfmter(-86401.999), "1 d")
		self.assertEqual(self.secfmter(-86459.999), "1 d")
		self.assertEqual(self.secfmter(-89999.999), "1 d")
		self.assertEqual(self.secfmter(-90000.999), "1 d 1 h")
		self.assertEqual(self.secfmter(-31535999.999), "364 d 23 h")
		self.assertEqual(self.secfmter(-31536000.999), "365 d")
		self.assertEqual(self.secfmter(-31539599.999), "365 d")
		self.assertEqual(self.secfmter(-31539600.999), "365 d 1 h")

	def test_mostsecfmt_str_float_big_seconds(self):

		self.assertEqual(self.secfmter("1.999"), "1 s")
		self.assertEqual(self.secfmter("59.999"), "59 s")
		self.assertEqual(self.secfmter("60.999"), "1 m")
		self.assertEqual(self.secfmter("61.999"), "1 m 1 s")
		self.assertEqual(self.secfmter("119.999"), "1 m 59 s")
		self.assertEqual(self.secfmter("120.999"), "2 m")
		self.assertEqual(self.secfmter("120.999"), "2 m")
		self.assertEqual(self.secfmter("3599.999"), "59 m 59 s")
		self.assertEqual(self.secfmter("3600.999"), "1 h")
		self.assertEqual(self.secfmter("3601.999"), "1 h")
		self.assertEqual(self.secfmter("3659.999"), "1 h")
		self.assertEqual(self.secfmter("3660.999"), "1 h 1 m")
		self.assertEqual(self.secfmter("86399.999"), "23 h 59 m")
		self.assertEqual(self.secfmter("86400.999"), "1 d")
		self.assertEqual(self.secfmter("86401.999"), "1 d")
		self.assertEqual(self.secfmter("86459.999"), "1 d")
		self.assertEqual(self.secfmter("89999.999"), "1 d")
		self.assertEqual(self.secfmter("90000.999"), "1 d 1 h")
		self.assertEqual(self.secfmter("31535999.999"), "364 d 23 h")
		self.assertEqual(self.secfmter("31536000.999"), "365 d")
		self.assertEqual(self.secfmter("31539599.999"), "365 d")
		self.assertEqual(self.secfmter("31539600.999"), "365 d 1 h")

	def test_mostsecfmt_str_float_big_seconds_negative(self):

		self.assertEqual(self.secfmter("-1.999"), "1 s")
		self.assertEqual(self.secfmter("-59.999"), "59 s")
		self.assertEqual(self.secfmter("-60.999"), "1 m")
		self.assertEqual(self.secfmter("-61.999"), "1 m 1 s")
		self.assertEqual(self.secfmter("-119.999"), "1 m 59 s")
		self.assertEqual(self.secfmter("-120.999"), "2 m")
		self.assertEqual(self.secfmter("-120.999"), "2 m")
		self.assertEqual(self.secfmter("-3599.999"), "59 m 59 s")
		self.assertEqual(self.secfmter("-3600.999"), "1 h")
		self.assertEqual(self.secfmter("-3601.999"), "1 h")
		self.assertEqual(self.secfmter("-3659.999"), "1 h")
		self.assertEqual(self.secfmter("-3660.999"), "1 h 1 m")
		self.assertEqual(self.secfmter("-86399.999"), "23 h 59 m")
		self.assertEqual(self.secfmter("-86400.999"), "1 d")
		self.assertEqual(self.secfmter("-86401.999"), "1 d")
		self.assertEqual(self.secfmter("-86459.999"), "1 d")
		self.assertEqual(self.secfmter("-89999.999"), "1 d")
		self.assertEqual(self.secfmter("-90000.999"), "1 d 1 h")
		self.assertEqual(self.secfmter("-31535999.999"), "364 d 23 h")
		self.assertEqual(self.secfmter("-31536000.999"), "365 d")
		self.assertEqual(self.secfmter("-31539599.999"), "365 d")
		self.assertEqual(self.secfmter("-31539600.999"), "365 d 1 h")

	def test_mostsecfmt_E_seconds(self):

		for exponential in ( 1E5, -1E5, "1E5", "-1E5" ):
			for formatter in ( self.secfmter, self.posfmter ):
				with self.subTest(value=exponential, positive=(formatter == self.posfmter)):
					self.assertEqual(formatter(exponential), "1 d 3 h")

	def test_mostsecfmt_invalids(self):

		for curent in ( "int",None,[ 42 ],{ 42 },{ "value": 42 },( 42, ),Transmutable,print,... ):
			for formatter in ( self.secfmter, self.posfmter ):
				with self.subTest(value=curent, positive=(formatter == self.posfmter)):
					self.assertIsNone(formatter(curent))








	def test_DIRTtimer_invalids_init(self):

		for item in ( None,[ 10 ],( 10, ),{ "T": 10 },{ 10 },Transmutable,print,... ):
			with self.subTest(current=item):
				try:

					@DIRTtimer(T=item)
					class Unmanagable(Transmutable): pass

				except Exception as E:

					self.assertIsInstance(E, ValueError)
					self.assertEqual(str(E), f"Termination timer \"{item}\" is invalid")

				try:

					@DIRTtimer(D=item)
					class Unmanagable(Transmutable): pass

				except Exception as E:

					self.assertIsInstance(E, ValueError)
					self.assertEqual(str(E), f"Delay timer \"{item}\" is invalid")

				try:

					@DIRTtimer(R=item)
					class Unmanagable(Transmutable): pass

				except Exception as E:

					self.assertIsInstance(E, ValueError)
					self.assertEqual(str(E), f"Repetition counter \"{item}\" is invalid")

				try:

					@DIRTtimer(I=item)
					class Unmanagable(Transmutable): pass

				except Exception as E:

					self.assertIsInstance(E, ValueError)
					self.assertEqual(str(E), f"Interval timer \"{item}\" is invalid")

				try:

					@DIRTtimer(spawner=item)
					class Unmanagable(Transmutable): pass

				except Exception as E:

					self.assertIsInstance(E, ValueError)
					self.assertEqual(str(E), f"Process spawner \"{item}\" is invalid")




	def test_DIRTtimer_valid_inits(self):

		for item in (

			1, 900., .42,
			"500", "5.", ".00001",
			-7575483, -11., -.19999999999,
			"-0", "-00000001.", "-000000.1",
			1E5, -2E3, "14E88", "-25E17",
			True, False
		):
			with self.subTest(current=item):

				@DIRTtimer(T=item, D=item, R=item, I=item)
				class Managable(Transmutable): pass
				self.assertIsInstance(Managable, type)


		@DIRTtimer()
		class Managable(Transmutable): pass
		self.assertIsInstance(Managable, type)




	def test_DIRTtimer_dummy_spawn(self):
		class DummyProcess(Transmutable):

			def __call__(self, *args, **kwargs): return self
			class loggy(LibraryContrib):

				handler		= self.TIMETURN_TIMERS_HANDLER
				init_name	= "DIRTtimer_dummy_spawn"

			def start(self):		self.loggy.info("Dummy \"start\"")
			def terminate(self):	self.loggy.info("Dummy \"terminate\"")

		self.test_case = DummyProcess()

		@DIRTtimer(T=.42, spawner=self.test_case)
		class ScaryWoker(Transmutable):
			def __call__(self): pass

		with self.assertLogs("DIRTtimer_dummy_spawn", 20) as case_loggy : ScaryWoker()()
		self.assertIn("INFO:DIRTtimer_dummy_spawn:Dummy \"start\"", case_loggy.output)
		self.assertIn("INFO:DIRTtimer_dummy_spawn:Dummy \"terminate\"", case_loggy.output)




	@unittest.skipIf(os.name == "nt", "cannot test termination, cause windows cannot fork")
	def test_DIRTtimer_complex(self):

		DIRT_complex = str(self.MAGICAL_ROOT /"DIRT_complex.loggy")
		self.make_loggy_file(DIRT_complex)

		@DIRTtimer(T=.42, D=.69, R=2, I=.75)
		class Monday(self.browser):
			class loggy(LibraryContrib):

				handler		= DIRT_complex
				init_name	= "DIRTtimer"
				init_level	= 10

		loggy = []
		RAM = [ 1000 ]
		self.test_case = Monday()
		self.test_case("open tab", source=RAM)
		self.assertEqual(RAM,[ 1000 ])
		self.test_case.loggy.close()

		with open(DIRT_complex) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@DIRTtimer-Monday DEBUG : Delay start timer 0.69 seconds",
				"@DIRTtimer-Monday DEBUG : Interval delay 0.75 seconds",
				"@DIRTtimer-Monday DEBUG : Repetition counter 2 times",
				"@DIRTtimer-Monday DEBUG : Termination timer 0.42 seconds",
				"@DIRTtimer-Monday DEBUG : Caller arguments: ('open tab',)",
				"@DIRTtimer-Monday DEBUG : Caller keyword arguments: {'source': [1000]}",
				"@DIRTtimer-Monday DEBUG : DIRT iteration 1",
				f"@DIRTtimer-Monday DEBUG : Delay 0.69 seconds for {self.test_case} performed",
				f"@DIRTtimer-Monday INFO : Starting 0.42 seconds timer for {self.test_case}",
				"@DIRTtimer-Monday INFO : Going to open tab",
				"@DIRTtimer-Monday INFO : Current RAM consumed 2000",
				f"@DIRTtimer-Monday DEBUG : Process {self.test_case} terminated",
				f"@DIRTtimer-Monday DEBUG : Interval 0.75 seconds for {self.test_case} performed",
				"@DIRTtimer-Monday DEBUG : DIRT iteration 2",
				f"@DIRTtimer-Monday DEBUG : Delay 0.69 seconds for {self.test_case} performed",
				f"@DIRTtimer-Monday INFO : Starting 0.42 seconds timer for {self.test_case}",
				"@DIRTtimer-Monday INFO : Going to open tab",
				"@DIRTtimer-Monday INFO : Current RAM consumed 2000",
				f"@DIRTtimer-Monday DEBUG : Process {self.test_case} terminated",
				f"@DIRTtimer-Monday DEBUG : Interval 0.75 seconds for {self.test_case} performed",
			]
		)
		if	os.path.isfile(DIRT_complex): os.remove(DIRT_complex)








	def test_DIRTtimer_defaults(self):

		DIRT_defaults = str(self.MAGICAL_ROOT /"DIRT_defaults.loggy")
		self.make_loggy_file(DIRT_defaults)

		@DIRTtimer()
		class Tuesday(self.browser):
			class loggy(LibraryContrib):

				handler		= DIRT_defaults
				init_name	= "DIRTtimer-d"

		loggy = []
		RAM = [ 1000 ]
		self.test_case = Tuesday()
		self.test_case("open tab", source=RAM)
		self.assertEqual(RAM,[ 2000 ])
		self.test_case.loggy.close()

		with open(DIRT_defaults) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@DIRTtimer-d INFO : Going to open tab",
				"@DIRTtimer-d INFO : Current RAM consumed 2000",
			]
		)
		if	os.path.isfile(DIRT_defaults): os.remove(DIRT_defaults)








	def test_DIRTtimer_soloproc(self):

		DIRT_soloproc = str(self.MAGICAL_ROOT /"DIRT_soloproc.loggy")
		self.make_loggy_file(DIRT_soloproc)

		@DIRTtimer(R=10, I=.05)
		class Wednesday(self.browser):
			class loggy(LibraryContrib):

				handler			= DIRT_soloproc
				init_name		= "DIRTtimer-s"
				force_handover	= True

		loggy = []
		RAM = [ 1000 ]
		self.test_case = Wednesday()
		self.test_case("open tab", source=RAM)
		self.assertEqual(RAM,[ 1024000 ])
		self.test_case.loggy.close()

		with open(DIRT_soloproc) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 2000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 4000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 8000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 16000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 32000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 64000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 128000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 256000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 512000",
				"@DIRTtimer-s-Wednesday INFO : Going to open tab",
				"@DIRTtimer-s-Wednesday INFO : Current RAM consumed 1024000",
			]
		)
		if	os.path.isfile(DIRT_soloproc): os.remove(DIRT_soloproc)








	def test_DIRTtimer_nocall(self):

		@DIRTtimer(T=1000)
		class Unmanagable(Transmutable): pass
		self.assertRaisesRegex(

			TypeError,
			"Unmanagable object is not callable",
			Unmanagable()
		)

	def test_DIRTtimer_positional_arguments(self):

		try:

			@DIRTtimer(1000,I=2000,R=3000,T=4000)
			class Unmanagable(Transmutable): pass

		except Exception as E:

			self.assertIsInstance(E, TypeError)
			self.assertEqual(

				str(E),
				"DIRTtimer.__init__() takes 1 positional argument but 2 positional arguments "
				"(and 3 keyword-only arguments) were given"
			)

		try:

			@DIRTtimer(1000,2000,R=3000,T=4000)
			class Unmanagable(Transmutable): pass

		except Exception as E:

			self.assertIsInstance(E, TypeError)
			self.assertEqual(

				str(E),
				"DIRTtimer.__init__() takes 1 positional argument but 3 positional arguments "
				"(and 2 keyword-only arguments) were given"
			)

		try:

			@DIRTtimer(1000,2000,3000,T=4000)
			class Unmanagable(Transmutable): pass

		except Exception as E:

			self.assertIsInstance(E, TypeError)
			self.assertEqual(

				str(E),
				"DIRTtimer.__init__() takes 1 positional argument but 4 positional arguments "
				"(and 1 keyword-only argument) were given"
			)

		try:

			@DIRTtimer(1000,2000,3000,4000)
			class Unmanagable(Transmutable): pass

		except Exception as E:

			self.assertIsInstance(E, TypeError)
			self.assertEqual(

				str(E),
				"DIRTtimer.__init__() takes 1 positional argument but 5 were given"
			)








if __name__ == "__main__" : unittest.main(verbosity=2)







