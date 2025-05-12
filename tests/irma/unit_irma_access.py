import	os
import	re
import	unittest
from	pygwarts.magical.philosophers_stone		import Transmutable
from	pygwarts.tests.irma						import IrmaTestCase
from	pygwarts.irma.contrib					import LibraryContrib
from	pygwarts.irma.access					import LibraryAccess
from	pygwarts.irma.access.volume				import LibraryVolume
from	pygwarts.irma.access.bookmarks			import VolumeBookmark
from	pygwarts.irma.access.handlers.counters	import AccessCounter
from	pygwarts.irma.access.handlers.parsers	import TargetHandler
from	pygwarts.irma.access.handlers.parsers	import TargetStringAccumulator
from	pygwarts.irma.access.inducers.counters	import HandlerCounterInducer
from	pygwarts.irma.access.inducers.counters	import RegisterCounterInducer
from	pygwarts.irma.access.inducers.recap		import RegisterRecapInducer
from	pygwarts.irma.access.inducers.recap		import RegisterRecapAccumulatorInducer
from	pygwarts.irma.access.annex				import VolumeAnnex
from	pygwarts.irma.access.annex				import LibraryAnnex
from	pygwarts.irma.access.utils				import TextWrapper








class AccessCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_LIBRARY): os.remove(cls.ACCESS_LIBRARY)

		if	os.path.isfile(cls.majorV1): os.remove(cls.majorV1)
		if	os.path.isfile(cls.majorV2): os.remove(cls.majorV2)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.ACCESS_LIBRARY)
		cls.majorV1 = str(cls.IRMA_ROOT /"majorV1.txt")
		cls.majorV2 = str(cls.IRMA_ROOT /"majorV2.txt")
		cls.fmake(

			cls, cls.majorV1,
			"31/12/2024 2359 @MajorData WARNING : All unsaved data will be gone next year\n"
			"01/01/2025 0000 @MajorData INFO : The new year has come\n"
			"01/01/2025 0001 @MajorData INFO : The new year has come one mintue now\n"
			"01/01/2025 0100 @MajorData INFO : The new year has come one hour now\n"
			"01/01/2025 0200 @MajorData INFO : The new year has come two hours now\n"
			"01/01/2025 0200 @MajorData INFO : It is time to destroy past year data\n"
			"01/01/2025 0200 @MajorData INFO : Past year data is 2195390253890235472904\n"
			"01/01/2025 0200 @MajorData WARNING : Past year data can't be destroyed because it's bad\n"
		)
		cls.fmake(

			cls, cls.majorV2,
			"02/01/2025 0000 @MajorData INFO : The new day of the new year has come\n"
			"02/01/2025 0001 @MajorData INFO : The new day of the new year has come one mintue now\n"
			"02/01/2025 0100 @MajorData INFO : The new day of the new year has come one hour now\n"
			"02/01/2025 0200 @MajorData INFO : The new day of the new year has come two hours now\n"
			"02/01/2025 0200 @MajorData INFO : It is time to destroy past year data\n"
			"02/01/2025 0200 @MajorData INFO : Found past year user John\n"
			"02/01/2025 0200 @MajorData INFO : Found past year user David\n"
			"02/01/2025 0200 @MajorData INFO : Found past year user Mia\n"
			"02/01/2025 0200 @MajorData WARNING : Past year data can't be destroyed because it's still bad\n"
		)


	def test_no_library(self):

		class LonelyAccess(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "no_library"
				init_level	= 10

		with self.assertLogs("no_library", 10) as case_loggy : self.test_case = LonelyAccess()
		self.assertIn(f"DEBUG:no_library:Library access point created", case_loggy.output)




	def test_dummy_library(self):

		class DummyLibrary(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "dummy_library"
				init_level	= 10

			class CommonBookmark1(VolumeBookmark):		trigger = "trigger1"
			class CommonBookmark2(VolumeBookmark):		trigger = "trigger2"
			class TheVolumeOne(LibraryVolume):			pass
			class TheVolumeTwo(LibraryVolume):

				class VolumesBookmark1(VolumeBookmark):	trigger = "trigger3"
				class VolumesBookmark2(VolumeBookmark):	trigger = "trigger4"

		with self.assertLogs("dummy_library", 10) as case_loggy : self.test_case = DummyLibrary()
		self.assertIn(f"DEBUG:dummy_library:Assigned to library {self.test_case}", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:dummy_library:Assigned to library {self.test_case}"),2
		)
		self.assertIn(
			f"DEBUG:dummy_library:Assigned to volume {self.test_case.TheVolumeTwo}", case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(f"DEBUG:dummy_library:Assigned to volume {self.test_case.TheVolumeTwo}"),
			2
		)
		self.assertIn(f"DEBUG:dummy_library:Library access point created", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.CommonBookmark1], "bookmark")
		self.assertEqual(self.test_case[self.test_case.CommonBookmark2], "bookmark")
		self.assertEqual(

			self.test_case.keysof("bookmark"),
			[ self.test_case.CommonBookmark1,self.test_case.CommonBookmark2 ]
		)
		self.assertEqual(self.test_case[self.test_case.TheVolumeOne], "volume")
		self.assertEqual(self.test_case[self.test_case.TheVolumeTwo], "volume")
		self.assertEqual(
			self.test_case.keysof("volume"),[ self.test_case.TheVolumeOne,self.test_case.TheVolumeTwo ]
		)
		self.assertEqual(

			self.test_case.TheVolumeTwo.keysof("bookmark"),
			[ self.test_case.TheVolumeTwo.VolumesBookmark1,self.test_case.TheVolumeTwo.VolumesBookmark2 ]
		)
		self.assertEqual(len(self.test_case),4)




	def test_broke_dummy_library(self):

		class DummyLibrary(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "broke_dummy_library"
				init_level	= 10

			class CommonBookmark1(VolumeBookmark):		pass
			class CommonBookmark2(VolumeBookmark):		pass
			class TheVolumeOne(LibraryVolume):			pass
			class TheVolumeTwo(LibraryVolume):

				class VolumesBookmark1(VolumeBookmark):	pass
				class VolumesBookmark2(VolumeBookmark):	pass

		with self.assertLogs("broke_dummy_library", 10) as case_loggy : self.test_case = DummyLibrary()
		self.assertIn(f"DEBUG:broke_dummy_library:Assigned to {self.test_case}", case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:broke_dummy_library:Assigned to {self.test_case}"),2)
		self.assertIn(f"DEBUG:broke_dummy_library:Incomplete bookmark", case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:broke_dummy_library:Incomplete bookmark"),4)
		self.assertIn(f"DEBUG:broke_dummy_library:Library access point created", case_loggy.output)
		self.assertIsNone(self.test_case[str(self.test_case)])
		self.assertIsNone(self.test_case[str(self.test_case.TheVolumeTwo)])
		self.assertEqual(self.test_case[self.test_case.TheVolumeOne], "volume")
		self.assertEqual(self.test_case[self.test_case.TheVolumeTwo], "volume")
		self.assertEqual(len(self.test_case),2)
		self.assertEqual(
			self.test_case.keysof("volume"),[ self.test_case.TheVolumeOne,self.test_case.TheVolumeTwo ]
		)








	def test_compile_triggers(self):

		class DummyLibrary(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "compile_triggers"
				init_level	= 10

		self.test_case = DummyLibrary()
		triggers = [ "trigger #1", "trigger #2", "trigger #3" ]

		with self.assertLogs("compile_triggers", 10) as case_loggy:
			self.assertEqual(

				self.test_case.compile_triggers(triggers),
				re.compile("(trigger #1)|(trigger #2)|(trigger #3)")
			)
		self.assertIn("DEBUG:compile_triggers:Compiling trigger \"trigger #1\"", case_loggy.output)
		self.assertIn("DEBUG:compile_triggers:Compiling trigger \"trigger #2\"", case_loggy.output)
		self.assertIn("DEBUG:compile_triggers:Compiling trigger \"trigger #3\"", case_loggy.output)




	def test_compile_bad_triggers(self):

		class DummyLibrary(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "compile_bad_triggers"
				init_level	= 10

		self.test_case = DummyLibrary()
		for bad_triggers in (

			"triggers", 42, .69, True, False, None, ..., print, Transmutable,
			( "trigger #1", "trigger #2", "trigger #3" ),
			{ "trigger #1", "trigger #2", "trigger #3" },
			{ 1: "trigger #1", 2: "trigger #2", 3: "trigger #3" },
		):
			with self.subTest(triggers=bad_triggers):
				with self.assertLogs("compile_bad_triggers", 10) as case_loggy:

					self.assertIsNone(self.test_case.compile_triggers(bad_triggers))
				self.assertIn(
					f"DEBUG:compile_bad_triggers:Invalid triggers {type(bad_triggers)}", case_loggy.output
				)




	def test_compile_mixed_triggers(self):

		class DummyLibrary(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "compile_mixed_triggers"
				init_level	= 10

		self.test_case = DummyLibrary()
		triggers = [ "trigger #1",[ "trigger #2" ], 42 ]
		with self.assertLogs("compile_mixed_triggers", 10) as case_loggy:
			self.assertEqual(

				self.test_case.compile_triggers(triggers),
				re.compile("(trigger #1)")
			)
		self.assertIn("DEBUG:compile_mixed_triggers:Compiling trigger \"trigger #1\"", case_loggy.output)
		self.assertIn(

			"DEBUG:compile_mixed_triggers:Skipping invalid trigger \"['trigger #2']\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:compile_mixed_triggers:Skipping invalid trigger \"42\"",
			case_loggy.output
		)




	def test_compile_no_triggers(self):

		class DummyLibrary(LibraryAccess):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "compile_no_triggers"
				init_level	= 10

		self.test_case = DummyLibrary()
		triggers = [( "trigger #1", ),[ "trigger #2" ],{ "trigger #3" },42 ]
		with self.assertLogs("compile_no_triggers", 10) as case_loggy:
			self.assertIsNone(self.test_case.compile_triggers(triggers))

		self.assertIn(

			"DEBUG:compile_no_triggers:Skipping invalid trigger \"('trigger #1',)\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:compile_no_triggers:Skipping invalid trigger \"['trigger #2']\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:compile_no_triggers:Skipping invalid trigger \"{'trigger #3'}\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:compile_no_triggers:Skipping invalid trigger \"42\"",
			case_loggy.output
		)
		self.assertIn("DEBUG:compile_no_triggers:No triggers compiled", case_loggy.output)


		with self.assertLogs("compile_no_triggers", 10) as case_loggy:
			self.assertIsNone(self.test_case.compile_triggers([]))
		self.assertIn("DEBUG:compile_no_triggers:No triggers compiled", case_loggy.output)








	def test_major_library(self):
		class MajorLibrary(LibraryAccess):

			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "major_library"
				init_level	= 10

			@TextWrapper("Major Library:\n")
			class MajorAnnex(LibraryAnnex):						pass
			class INFOS(VolumeBookmark):

				trigger	= "INFO : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tINFOS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class WARNINGS(VolumeBookmark):

				trigger	= "WARNING : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tWARNINGS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class ERRORS(VolumeBookmark):

				trigger	= "ERROR : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tERRORS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class V1(LibraryVolume):

				location = self.majorV1
				inrange = "01/01"
				@TextWrapper("\tVolume 1:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					trigger = "Past year data is "
					class Target(TargetHandler):

						rpattern = r".+ (?P<target>\d+)$"
						@TextWrapper("\t\tdata found: ", "\n")
						class Inducer(RegisterRecapInducer):	pass

			class V2(LibraryVolume):

				location = self.majorV2
				inrange	= "02/01/2025"
				@TextWrapper("\tVolume 2:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					trigger = "Found past year user "
					class Users(TargetStringAccumulator):

						rpattern = r".+ (?P<target>\w+)"
						@TextWrapper("\t\tusers: ","\n")
						class Inducer(RegisterRecapAccumulatorInducer):	joint = ", "


		self.test_case = MajorLibrary()
		self.assertEqual(

			self.test_case.MajorAnnex(),
			"Major Library:\n"
			"\tVolume 1:\n"
			"\t\tINFOS: 6/14\n"
			"\t\tWARNINGS: 1/2\n"
			"\t\tdata found: 2195390253890235472904\n"
			"\tVolume 2:\n"
			"\t\tINFOS: 8/14\n"
			"\t\tWARNINGS: 1/2\n"
			"\t\tusers: John, David, Mia\n"
		)








	def test_major_library_no_ranges(self):
		class MajorLibrary(LibraryAccess):

			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "major_library_no_ranges"
				init_level	= 10

			@TextWrapper("Major Library:\n")
			class MajorAnnex(LibraryAnnex):						pass
			class INFOS(VolumeBookmark):

				trigger	= "INFO : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tINFOS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class WARNINGS(VolumeBookmark):

				trigger	= "WARNING : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tWARNINGS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class ERRORS(VolumeBookmark):

				trigger	= "ERROR : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tERRORS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class V1(LibraryVolume):

				location = self.majorV1
				@TextWrapper("\tVolume 1:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					trigger = "Past year data is "
					class Target(TargetHandler):

						rpattern = r".+ (?P<target>\d+)$"
						@TextWrapper("\t\tdata found: ", "\n")
						class Inducer(RegisterRecapInducer):	pass

			class V2(LibraryVolume):

				location = self.majorV2
				@TextWrapper("\tVolume 2:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					trigger = "Found past year user "
					class Users(TargetStringAccumulator):

						rpattern = r".+ (?P<target>\w+)"
						@TextWrapper("\t\tusers: ","\n")
						class Inducer(RegisterRecapAccumulatorInducer):	joint = ", "


		self.test_case = MajorLibrary()
		self.assertIsNone(self.test_case.MajorAnnex())








	def test_major_library_no_locations(self):
		class MajorLibrary(LibraryAccess):

			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "major_library_no_locations"
				init_level	= 10

			@TextWrapper("Major Library:\n")
			class MajorAnnex(LibraryAnnex):						pass
			class INFOS(VolumeBookmark):

				trigger	= "INFO : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tINFOS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class WARNINGS(VolumeBookmark):

				trigger	= "WARNING : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tWARNINGS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class ERRORS(VolumeBookmark):

				trigger	= "ERROR : "
				class Counter(AccessCounter):

					@TextWrapper("\t\tERRORS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class V1(LibraryVolume):

				inrange = "01/01"
				@TextWrapper("\tVolume 1:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					trigger = "Past year data is "
					class Target(TargetHandler):

						rpattern = r".+ (?P<target>\d+)$"
						@TextWrapper("\t\tdata found: ", "\n")
						class Inducer(RegisterRecapInducer):	pass

			class V2(LibraryVolume):

				inrange	= "02/01/2025"
				@TextWrapper("\tVolume 2:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					trigger = "Found past year user "
					class Users(TargetStringAccumulator):

						rpattern = r".+ (?P<target>\w+)"
						@TextWrapper("\t\tusers: ","\n")
						class Inducer(RegisterRecapAccumulatorInducer):	joint = ", "


		self.test_case = MajorLibrary()
		self.assertIsNone(self.test_case.MajorAnnex())








	def test_major_library_no_triggers(self):
		class MajorLibrary(LibraryAccess):

			class loggy(LibraryContrib):

				handler		= self.ACCESS_LIBRARY
				init_name	= "major_library_no_triggers"
				init_level	= 10

			@TextWrapper("Major Library:\n")
			class MajorAnnex(LibraryAnnex):						pass
			class INFOS(VolumeBookmark):

				class Counter(AccessCounter):

					@TextWrapper("\t\tINFOS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class WARNINGS(VolumeBookmark):

				class Counter(AccessCounter):

					@TextWrapper("\t\tWARNINGS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class ERRORS(VolumeBookmark):

				class Counter(AccessCounter):

					@TextWrapper("\t\tERRORS: ")
					class Current(RegisterCounterInducer):		pass
					@TextWrapper("/","\n")
					class Total(HandlerCounterInducer):			pass

			class V1(LibraryVolume):

				location = self.majorV1
				inrange = "01/01"
				@TextWrapper("\tVolume 1:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					class Target(TargetHandler):

						rpattern = r".+ (?P<target>\d+)$"
						@TextWrapper("\t\tdata found: ", "\n")
						class Inducer(RegisterRecapInducer):	pass

			class V2(LibraryVolume):

				location = self.majorV2
				inrange	= "02/01/2025"
				@TextWrapper("\tVolume 2:\n")
				class Annex(VolumeAnnex):						pass
				class B1(VolumeBookmark):

					class Users(TargetStringAccumulator):

						rpattern = r".+ (?P<target>\w+)"
						@TextWrapper("\t\tusers: ","\n")
						class Inducer(RegisterRecapAccumulatorInducer):	joint = ", "


		self.test_case = MajorLibrary()
		self.assertIsNone(self.test_case.MajorAnnex())








if __name__ == "__main__" : unittest.main(verbosity=2)







