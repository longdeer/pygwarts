import	os
import	unittest
from	pygwarts.magical.philosophers_stone		import Transmutable
from	pygwarts.magical.time_turner.timers		import mostsec
from	pygwarts.tests.irma						import IrmaTestCase
from	pygwarts.irma.contrib					import LibraryContrib
from	pygwarts.irma.shelve					import LibraryShelf
from	pygwarts.irma.access					import LibraryAccess
from	pygwarts.irma.access.annex				import VolumeAnnex
from	pygwarts.irma.access.volume				import LibraryVolume
from	pygwarts.irma.access.bookmarks			import VolumeBookmark
from	pygwarts.irma.access.bookmarks.counters	import InfoCount
from	pygwarts.irma.access.bookmarks.counters	import WarningCount
from	pygwarts.irma.access.bookmarks.counters	import ErrorCount
from	pygwarts.irma.access.bookmarks.counters	import CriticalCount
from	pygwarts.irma.access.bookmarks.viewers	import ViewWrapper
from	pygwarts.irma.access.bookmarks.viewers	import ViewCase
from	pygwarts.irma.access.handlers			import AccessHandlerRegisterCounter
from	pygwarts.irma.access.handlers.counters	import AccessCounter
from	pygwarts.irma.access.handlers.parsers	import TargetNumberAccumulator
from	pygwarts.irma.access.handlers.parsers	import TargetStringAccumulator
from	pygwarts.irma.access.inducers			import AccessInducer
from	pygwarts.irma.access.inducers.counters	import RegisterCounterInducer
from	pygwarts.irma.access.inducers.recap		import RegisterRecapInducer
from	pygwarts.irma.access.inducers.filters	import plurnum
from	pygwarts.irma.access.inducers.filters	import posnum
from	pygwarts.irma.access.inducers.case		import InducerCase
from	pygwarts.irma.access.utils				import TextWrapper
from	pygwarts.irma.shelve.casing				import shelf_case
from	pygwarts.irma.shelve.casing				import ShelfCase
from	pygwarts.irma.shelve.casing				import is_num
from	pygwarts.irma.shelve.casing				import is_iterable
from	pygwarts.irma.shelve.casing				import num_diff
from	pygwarts.irma.shelve.casing				import seq_diff
from	pygwarts.irma.shelve.casing				import NumDiffCase








class AccessBookmarkCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	class CasedStringsAccumulatorInducer(AccessInducer):
		def __call__(self, volume :LibraryVolume) -> str :


			if	isinstance(recap := self.get_register_recap(volume), list):
				if	getattr(self, "unique", False):


					uniqs	= set()
					accum	= [ acc for acc in map(str,recap) if not (acc in uniqs or uniqs.add(acc)) ]
				else:
					accum	= list(map(str,recap))


				if	isinstance(m := getattr(self, getattr(self, "case_link", ""),None), LibraryShelf|dict):


					if	str(volume) not in m : m[str(volume)] = dict()
					if	(casing := shelf_case(

						accum,
						key=str(self),
						shelf=m[str(volume)],
						prep=is_iterable,
						post=seq_diff,
					)):
						return str(getattr(self, "joint", " ")).join(casing)
				return	str(getattr(self, "joint", " ")).join(accum)


	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_BOOKMARK): os.remove(cls.ACCESS_BOOKMARK)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.ACCESS_BOOKMARK)
	def test_no_trigger_init(self):
		class LonelyBookmark(VolumeBookmark):

			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "no_trigger_init"
				init_level	= 10

		with self.assertLogs("no_trigger_init", 10) as case_loggy : self.test_case = LonelyBookmark()
		self.assertIn("DEBUG:no_trigger_init:Incomplete bookmark", case_loggy.output)
		self.assertIn(
			f"INFO:no_trigger_init:Bookmark {self.test_case} not assigned to library", case_loggy.output
		)




	def test_no_upper_init(self):
		class LonelyBookmark(VolumeBookmark):

			trigger	= "placeholder"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "no_upper_init"
				init_level	= 10

		with self.assertLogs("no_upper_init", 10) as case_loggy : self.test_case = LonelyBookmark()
		self.assertIn("DEBUG:no_upper_init:Upper layer not found", case_loggy.output)
		self.assertIn(
			f"INFO:no_upper_init:Bookmark {self.test_case} not assigned to library", case_loggy.output
		)




	def test_no_library_init(self):

		class FakeLibrary(Transmutable):
			class LonelyBookmark(VolumeBookmark):

				trigger = "placeholder"
				class loggy(LibraryContrib):

					handler		= self.ACCESS_BOOKMARK
					init_name	= "no_library_init"
					init_level	= 10

		with self.assertLogs("no_library_init", 10) as case_loggy : self.test_case = FakeLibrary()
		self.assertIn("DEBUG:no_library_init:Invalid upper layer", case_loggy.output)
		self.assertIn(

			f"INFO:no_library_init:Bookmark {self.test_case.LonelyBookmark} not assigned to library",
			case_loggy.output
		)




	def test_LibraryAccess_init(self):

		class LonelyLibrary(LibraryAccess):
			class LonelyBookmark(VolumeBookmark):

				trigger = "placeholder"
				class loggy(LibraryContrib):

					handler		= self.ACCESS_BOOKMARK
					init_name	= "LibraryAccess_init"
					init_level	= 10

		with self.assertLogs("LibraryAccess_init", 10) as case_loggy : self.test_case = LonelyLibrary()
		self.assertIn(f"DEBUG:LibraryAccess_init:Assigned to library {self.test_case}", case_loggy.output)




	def test_LibraryVolume_init(self):

		class LonelyLibrary(LibraryVolume):
			class LonelyBookmark(VolumeBookmark):

				trigger = "placeholder"
				class loggy(LibraryContrib):

					handler		= self.ACCESS_BOOKMARK
					init_name	= "LibraryVolume_init"
					init_level	= 10

		with self.assertLogs("LibraryVolume_init", 10) as case_loggy : self.test_case = LonelyLibrary()
		self.assertIn(f"DEBUG:LibraryVolume_init:Assigned to volume {self.test_case}", case_loggy.output)








	def test_update_valids(self):
		class LonelyBookmark(VolumeBookmark):

			trigger = "placeholder"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "update_valids"
				init_level	= 10

		self.test_case = LonelyBookmark()
		self.test_case(lambda _,V : V.loggy.info("OOH"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("EEH"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("OOH"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("AH"),		"handler")
		self.test_case(lambda _,V : V.loggy.info("AH"),		"handler")
		self.test_case(lambda _,V : V.loggy.info("TING"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("TANG"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("WALLA"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("WALLA"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("BING"),	"handler")
		self.test_case(lambda _,V : V.loggy.info("BANG"),	"handler")

		with self.assertLogs("update_valids", 10) as case_loggy : self.test_case.update("!",self.test_case)
		self.assertIn("INFO:update_valids:OOH", case_loggy.output)
		self.assertIn("INFO:update_valids:EEH", case_loggy.output)
		self.assertIn("INFO:update_valids:OOH", case_loggy.output)
		self.assertIn("INFO:update_valids:AH", case_loggy.output)
		self.assertIn("INFO:update_valids:AH", case_loggy.output)
		self.assertIn("INFO:update_valids:TING", case_loggy.output)
		self.assertIn("INFO:update_valids:TANG", case_loggy.output)
		self.assertIn("INFO:update_valids:WALLA", case_loggy.output)
		self.assertIn("INFO:update_valids:WALLA", case_loggy.output)
		self.assertIn("INFO:update_valids:BING", case_loggy.output)
		self.assertIn("INFO:update_valids:BANG", case_loggy.output)




	def test_update_invalids(self):
		class LonelyBookmark(VolumeBookmark):

			trigger = "placeholder"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "update_invalids"
				init_level	= 10

		self.test_case = LonelyBookmark()
		self.test_case(42, "handler")
		self.test_case(.69, "handler")
		self.test_case(None, "handler")
		self.test_case(( "AH ", ), "handler")

		with self.assertLogs("update_invalids", 10) as case_loggy : self.test_case.update("!",LibraryVolume)
		self.assertIn(

			"DEBUG:update_invalids:42 failed due to TypeError: 'int' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:update_invalids:0.69 failed due to TypeError: 'float' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:update_invalids:None failed due to TypeError: 'NoneType' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:update_invalids:('AH ',) failed due to TypeError: 'tuple' object is not callable",
			case_loggy.output
		)








	def test_view_valids(self):
		class LonelyBookmark(VolumeBookmark):

			trigger = "placeholder"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "view_valids"
				init_level	= 10

		self.test_case = LonelyBookmark()
		self.test_case(lambda _ : "OOH ",	"inducer")
		self.test_case(lambda _ : "EEH ",	"inducer")
		self.test_case(lambda _ : "OOH ",	"inducer")
		self.test_case(lambda _ : "AH ",	"inducer")
		self.test_case(lambda _ : "AH ",	"inducer")
		self.test_case(lambda _ : "TING ",	"inducer")
		self.test_case(lambda _ : "TANG ",	"inducer")
		self.test_case(lambda _ : "WALLA ",	"inducer")
		self.test_case(lambda _ : "WALLA ",	"inducer")
		self.test_case(lambda _ : "BING ",	"inducer")
		self.test_case(lambda _ : "BANG",	"inducer")
		self.assertEqual(

			self.test_case.view(LibraryVolume),
			"OOH EEH OOH AH AH TING TANG WALLA WALLA BING BANG"
		)




	def test_view_invalids(self):
		class LonelyBookmark(VolumeBookmark):

			trigger = "placeholder"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "view_invalids"
				init_level	= 10

		self.test_case = LonelyBookmark()
		inducer1 = lambda _ : 42
		inducer2 = lambda _ : .69
		inducer3 = lambda _ : None
		inducer4 = lambda _ : [ "OOH " ]
		inducer5 = lambda _ : ( "AH ", )
		inducer6 = lambda _ : { "AH " }
		inducer7 = lambda _ : { "TING ": "TANG " }
		self.test_case(inducer1, "inducer")
		self.test_case(inducer2, "inducer")
		self.test_case(inducer3, "inducer")
		self.test_case(inducer4, "inducer")
		self.test_case(inducer5, "inducer")
		self.test_case(inducer6, "inducer")
		self.test_case(inducer7, "inducer")
		self.test_case(42, "inducer")
		self.test_case(.69, "inducer")
		self.test_case(None, "inducer")
		self.test_case(( "AH ", ), "inducer")

		with self.assertLogs("view_invalids", 10) as case_loggy : self.test_case.view(LibraryVolume)
		self.assertIn(f"DEBUG:view_invalids:No view volume {LibraryVolume}", case_loggy.output)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer1} failed due to TypeError: "
			"can only concatenate str (not \"int\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer2} failed due to TypeError: "
			"can only concatenate str (not \"float\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer3} failed due to TypeError: "
			"can only concatenate str (not \"NoneType\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer4} failed due to TypeError: "
			"can only concatenate str (not \"list\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer5} failed due to TypeError: "
			"can only concatenate str (not \"tuple\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer6} failed due to TypeError: "
			"can only concatenate str (not \"set\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:view_invalids:{inducer7} failed due to TypeError: "
			"can only concatenate str (not \"dict\") to str",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:view_invalids:42 failed due to TypeError: 'int' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:view_invalids:0.69 failed due to TypeError: 'float' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:view_invalids:None failed due to TypeError: 'NoneType' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:view_invalids:('AH ',) failed due to TypeError: 'tuple' object is not callable",
			case_loggy.output
		)








	def test_InfoCount(self):
		class LonelyVolume(LibraryVolume):

			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "InfoCount"
				init_level	= 10

		with self.assertLogs("InfoCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:InfoCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:InfoCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:InfoCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts INFO : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts INFO : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "69")




	def test_WarningCount(self):
		class LonelyVolume(LibraryVolume):

			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "WarningCount"
				init_level	= 10

		with self.assertLogs("WarningCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:WarningCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:WarningCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:WarningCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts WARNING : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts WARNING : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "69")




	def test_ErrorCount(self):
		class LonelyVolume(LibraryVolume):

			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "ErrorCount"
				init_level	= 10

		with self.assertLogs("ErrorCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:ErrorCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:ErrorCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:ErrorCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts ERROR : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts ERROR : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "69")




	def test_CriticalCount(self):
		class LonelyVolume(LibraryVolume):

			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "CriticalCount"
				init_level	= 10

		with self.assertLogs("CriticalCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:CriticalCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:CriticalCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:CriticalCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts CRITICAL : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "69")








	def test_wrapped_InfoCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("INFOS: ")
			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "wrapped_InfoCount"
				init_level	= 10

		with self.assertLogs("wrapped_InfoCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:wrapped_InfoCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:wrapped_InfoCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:wrapped_InfoCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts INFO : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts INFO : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "INFOS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "INFOS: 69")




	def test_wrapped_WarningCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("WARNINGS: ")
			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "wrapped_WarningCount"
				init_level	= 10

		with self.assertLogs("wrapped_WarningCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:wrapped_WarningCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:wrapped_WarningCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:wrapped_WarningCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts WARNING : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts WARNING : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "WARNINGS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "WARNINGS: 69")




	def test_wrapped_ErrorCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("ERRORS: ")
			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "wrapped_ErrorCount"
				init_level	= 10

		with self.assertLogs("wrapped_ErrorCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:wrapped_ErrorCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:wrapped_ErrorCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:wrapped_ErrorCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts ERROR : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts ERROR : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "ERRORS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "ERRORS: 69")




	def test_wrapped_CriticalCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("CRITICALS: ")
			class LonelyCounter(InfoCount):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "wrapped_CriticalCount"
				init_level	= 10

		with self.assertLogs("wrapped_CriticalCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:wrapped_CriticalCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:wrapped_CriticalCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:wrapped_CriticalCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts CRITICAL : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "CRITICALS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "CRITICALS: 69")








	def test_cased_InfoCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("INFOS: ")
			@ViewCase("LonelyShelf", prep=is_num, post=num_diff)
			class LonelyCounter(InfoCount):		pass
			class LonelyShelf(LibraryShelf):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "cased_InfoCount"
				init_level	= 10

		with self.assertLogs("cased_InfoCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:cased_InfoCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:cased_InfoCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:cased_InfoCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts INFO : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts INFO : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "INFOS: 2 (+2)")
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "INFOS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "INFOS: 69 (+67)")




	def test_cased_WarningCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("WARNINGS: ")
			@ViewCase("LonelyShelf", prep=is_num, post=num_diff)
			class LonelyCounter(InfoCount):		pass
			class LonelyShelf(LibraryShelf):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "cased_WarningCount"
				init_level	= 10

		with self.assertLogs("cased_WarningCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:cased_WarningCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:cased_WarningCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:cased_WarningCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts WARNING : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts WARNING : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "WARNINGS: 2 (+2)")
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "WARNINGS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "WARNINGS: 69 (+67)")




	def test_cased_ErrorCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("ERRORS: ")
			@ViewCase("LonelyShelf", prep=is_num, post=num_diff)
			class LonelyCounter(InfoCount):		pass
			class LonelyShelf(LibraryShelf):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "cased_ErrorCount"
				init_level	= 10

		with self.assertLogs("cased_ErrorCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:cased_ErrorCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:cased_ErrorCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:cased_ErrorCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts ERROR : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts ERROR : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "ERRORS: 2 (+2)")
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "ERRORS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "ERRORS: 69 (+67)")




	def test_cased_CriticalCount(self):
		class LonelyVolume(LibraryVolume):

			@ViewWrapper("CRITICALS: ")
			@ViewCase("LonelyShelf", prep=is_num, post=num_diff)
			class LonelyCounter(InfoCount):		pass
			class LonelyShelf(LibraryShelf):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "cased_CriticalCount"
				init_level	= 10

		with self.assertLogs("cased_CriticalCount", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:cased_CriticalCount:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:cased_CriticalCount:Assigned to {self.test_case.LonelyCounter} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:cased_CriticalCount:Assigned to {self.test_case.LonelyCounter} bookmark "
			f"as {self.test_case.LonelyCounter.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyCounter.update(
			"31/12/2024 2359 @pygwarts CRITICAL : New year is comming!", self.test_case
		)
		self.test_case.LonelyCounter.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Happy new year!", self.test_case
		)
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "CRITICALS: 2 (+2)")
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "CRITICALS: 2")

		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyCounter.view(self.test_case))
		self.test_case[self.test_case.LonelyCounter.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyCounter.view(self.test_case), "CRITICALS: 69 (+67)")








	def test_CallstampActivity(self):

		class LonelyVolume(LibraryVolume):
			class CallstampActivity(VolumeBookmark):

				trigger	= " finished in "
				rpattern= r"finished in (?P<target>\d+)( seconds)?$"

				class Activities(AccessCounter):
					class Inducer(RegisterCounterInducer):	filter = plurnum

				@AccessHandlerRegisterCounter
				class Duration(TargetNumberAccumulator):

					class Total(RegisterRecapInducer):		filter = posnum
					class Average(AccessInducer):
						def __call__(self, volume :LibraryVolume) -> str | None :

							if	isinstance(recap := self.get_register_recap(volume), int | float):
								if	(counter := self.get_register_counter(volume)):

									return	str(recap /counter)
								return		str(recap)

		self.test_case = LonelyVolume()
		self.test_case.CallstampActivity.update(
			"01/01/2023 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2024 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.assertEqual(
			self.test_case.CallstampActivity.view(self.test_case), "39460800031536000.0"
		)




	def test_wrapped_CallstampActivity(self):

		class LonelyVolume(LibraryVolume):
			class CallstampActivity(VolumeBookmark):

				trigger	= " finished in "
				rpattern= r"finished in (?P<target>\d+)( seconds)?$"

				class Activities(AccessCounter):
					@TextWrapper("activities: ","\n")
					class Inducer(RegisterCounterInducer):	filter = plurnum

				@AccessHandlerRegisterCounter
				class Duration(TargetNumberAccumulator):

					@TextWrapper("total time: ","\n")
					class Total(RegisterRecapInducer):		filter = posnum
					@TextWrapper("average time: ","\n")
					class Average(AccessInducer):
						def __call__(self, volume :LibraryVolume) -> str | None :

							if	isinstance(recap := self.get_register_recap(volume), int | float):
								if	(counter := self.get_register_counter(volume)):

									return	str(recap /counter)
								return		str(recap)

		self.test_case = LonelyVolume()
		self.test_case.CallstampActivity.update(
			"01/01/2023 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2024 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.assertEqual(

			self.test_case.CallstampActivity.view(self.test_case),
			"activities: 3\ntotal time: 94608000\naverage time: 31536000.0\n"
		)




	def test_wrapped_cased_CallstampActivity(self):
		class LonelyVolume(LibraryVolume):

			class LonelyShelf(LibraryShelf):	pass
			class CallstampActivity(VolumeBookmark):

				trigger	= " finished in "
				rpattern= r"finished in (?P<target>\d+)( seconds)?$"

				class Activities(AccessCounter):

					@TextWrapper("activities: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer):	filter = plurnum

				@AccessHandlerRegisterCounter
				class Duration(TargetNumberAccumulator):

					@TextWrapper("total time: ","\n")
					@NumDiffCase("LonelyShelf")
					class Total(RegisterRecapInducer):		filter = posnum

					@TextWrapper("average time: ","\n")
					@NumDiffCase("LonelyShelf")
					class Average(AccessInducer):
						def __call__(self, volume :LibraryVolume) -> str | None :

							if	isinstance(recap := self.get_register_recap(volume), int | float):
								if	(counter := self.get_register_counter(volume)):

									return	str(recap /counter)
								return		str(recap)

		self.test_case = LonelyVolume()

		self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Total)] = "94602000"
		self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Average)] = "31536001"

		self.test_case.CallstampActivity.update(
			"01/01/2023 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2024 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.assertEqual(

			self.test_case.CallstampActivity.view(self.test_case),
			"activities: 3 (+3)\ntotal time: 94608000 (+6000)\naverage time: 31536000.0 (-1.0)\n"
		)

		self.assertEqual(
			self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Activities.Inducer)], "3"
		)
		self.assertEqual(
			self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Total)], "94608000"
		)
		self.assertEqual(
			self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Average)], "31536000.0"
		)








	def test_mostsecdiff_CallstampActivity(self):
		def mostsec_num_diff(num1 :int|float|str, num2 :int|float|str) -> str :

			diff = eval(f"{num1}-{num2}")
			left = f"{' (-' if str(diff).startswith('-') else ' (+'}"

			return f"{mostsec(num1)}{left}{mostsec(diff)})"

		class LonelyVolume(LibraryVolume):

			class LonelyShelf(LibraryShelf):	pass
			class CallstampActivity(VolumeBookmark):

				trigger	= " finished in "
				rpattern= r"finished in (?P<target>\d+)( seconds)?$"

				class Activities(AccessCounter):

					@TextWrapper("activities: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer):	filter = plurnum

				@AccessHandlerRegisterCounter
				class Duration(TargetNumberAccumulator):

					@TextWrapper("total time: ","\n")
					@ShelfCase("LonelyShelf", prep=is_num, post=mostsec_num_diff)
					class Total(RegisterRecapInducer):		filter = posnum

					@TextWrapper("average time: ","\n")
					@ShelfCase("LonelyShelf", prep=is_num, post=mostsec_num_diff)
					class Average(AccessInducer):
						def __call__(self, volume :LibraryVolume) -> str | None :

							if	isinstance(recap := self.get_register_recap(volume), int | float):
								if	(counter := self.get_register_counter(volume)):

									return	str(recap /counter)
								return		str(recap)

		self.test_case = LonelyVolume()

		self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Total)] = "94602000"
		self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Average)] = "31536001"

		self.test_case.CallstampActivity.update(
			"01/01/2023 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2024 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.test_case.CallstampActivity.update(
			"01/01/2025 0000 @pygwarts CRITICAL : Past year finished in 31536000 seconds", self.test_case
		)
		self.assertEqual(

			self.test_case.CallstampActivity.view(self.test_case),
			"activities: 3 (+3)\ntotal time: 1095 d (+1 h 40 m)\naverage time: 365 d (-1 s)\n"
		)

		self.assertEqual(
			self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Activities.Inducer)], "3"
		)
		self.assertEqual(
			self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Total)], "94608000"
		)
		self.assertEqual(
			self.test_case.LonelyShelf[str(self.test_case.CallstampActivity.Duration.Average)], "31536000.0"
		)








	def test_ShelfTrackers(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "ShelfTrackers"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyTracker(VolumeBookmark):

				trigger	= "Discarded tracker for"

				class Counter(AccessCounter):

					@TextWrapper("trackers removed: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("ShelfTrackers", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:ShelfTrackers:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:ShelfTrackers:Assigned to {self.test_case.LonelyTracker} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:ShelfTrackers:Assigned to {self.test_case.LonelyTracker} bookmark "
			f"as {self.test_case.LonelyTracker.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyTracker.update(
			"31/12/2024 2359 @pygwarts INFO : Discarded tracker for \"file1\"", self.test_case
		)
		self.test_case.LonelyTracker.update(
			"Discarded tracker for file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyTracker.view(self.test_case), "trackers removed: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyTracker.view(self.test_case), "trackers removed: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyTracker.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyTracker.view(self.test_case), "trackers removed: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyTracker.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyTracker.view(self.test_case), "trackers removed: 2 (-98)\n")

		self.test_case[self.test_case.LonelyTracker.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyTracker.view(self.test_case))
		self.test_case[self.test_case.LonelyTracker.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyTracker.view(self.test_case))

		self.test_case[self.test_case.LonelyTracker.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyTracker.view(self.test_case), "trackers removed: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyTracker.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyTracker.view(self.test_case), "trackers removed: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyTracker.Counter.Inducer)],"69")




	def test_ShelfProduces(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "ShelfProduces"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyProducer(VolumeBookmark):

				trigger	= "Rewritten Shelf"

				class Counter(AccessCounter):

					@TextWrapper("shelve produced: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("ShelfProduces", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:ShelfProduces:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:ShelfProduces:Assigned to {self.test_case.LonelyProducer} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:ShelfProduces:Assigned to {self.test_case.LonelyProducer} bookmark "
			f"as {self.test_case.LonelyProducer.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyProducer.update(
			"31/12/2024 2359 @pygwarts INFO : Rewritten Shelf \"file1\"", self.test_case
		)
		self.test_case.LonelyProducer.update(
			"Rewritten Shelf file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyProducer.view(self.test_case), "shelve produced: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyProducer.view(self.test_case), "shelve produced: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyProducer.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyProducer.view(self.test_case), "shelve produced: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyProducer.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyProducer.view(self.test_case), "shelve produced: 2 (-98)\n")

		self.test_case[self.test_case.LonelyProducer.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyProducer.view(self.test_case))
		self.test_case[self.test_case.LonelyProducer.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyProducer.view(self.test_case))

		self.test_case[self.test_case.LonelyProducer.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyProducer.view(self.test_case), "shelve produced: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyProducer.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyProducer.view(self.test_case), "shelve produced: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyProducer.Counter.Inducer)],"69")








	def test_LeafsGrown(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsGrown"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Grown leaf"

				class Counter(AccessCounter):

					@TextWrapper("leafs grown: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("LeafsGrown", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsGrown:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsGrown:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsGrown:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Grown leaf \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Grown leaf file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs grown: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs grown: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs grown: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs grown: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs grown: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs grown: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")




	def test_LeafsMoved(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsMoved"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Moved leaf"

				class Counter(AccessCounter):

					@TextWrapper("leafs moved: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("LeafsMoved", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsMoved:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsMoved:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsMoved:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Moved leaf \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Moved leaf file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs moved: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs moved: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs moved: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs moved: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs moved: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs moved: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")




	def test_LeafsCloned(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsCloned"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Cloned leaf"

				class Counter(AccessCounter):

					@TextWrapper("leafs cloned: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("LeafsCloned", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsCloned:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsCloned:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsCloned:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Cloned leaf \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Cloned leaf file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs cloned: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs cloned: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs cloned: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs cloned: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs cloned: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs cloned: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")




	def test_LeafsPushed(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsPushed"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Pushed leaf"

				class Counter(AccessCounter):

					@TextWrapper("leafs pushed: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("LeafsPushed", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsPushed:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsPushed:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsPushed:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Pushed leaf \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Pushed leaf file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs pushed: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs pushed: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs pushed: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs pushed: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs pushed: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs pushed: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")








	def test_TwigsThrived(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "TwigsThrived"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Thrived twig"

				class Counter(AccessCounter):

					@TextWrapper("twigs thrived: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("TwigsThrived", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:TwigsThrived:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:TwigsThrived:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:TwigsThrived:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Thrived twig \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Thrived twig file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs thrived: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs thrived: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs thrived: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs thrived: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs thrived: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs thrived: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")








	def test_LeafsTrimmed(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsTrimmed"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Trimmed leaf"

				class Counter(AccessCounter):

					@TextWrapper("leafs trimmed: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("LeafsTrimmed", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsTrimmed:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsTrimmed:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsTrimmed:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Trimmed leaf \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Trimmed leaf file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs trimmed: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs trimmed: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs trimmed: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs trimmed: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs trimmed: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "leafs trimmed: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")




	def test_TwigsTrimmed(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "TwigsTrimmed"
				init_level	= 10

			class LonelyShelf(LibraryShelf): pass
			class LonelyBookmark(VolumeBookmark):

				trigger	= "Trimmed twig"

				class Counter(AccessCounter):

					@TextWrapper("twigs trimmed: ","\n")
					@NumDiffCase("LonelyShelf")
					class Inducer(RegisterCounterInducer): filter = posnum

		with self.assertLogs("TwigsTrimmed", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:TwigsTrimmed:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:TwigsTrimmed:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:TwigsTrimmed:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.Counter} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Trimmed twig \"file1\"", self.test_case
		)
		self.test_case.LonelyBookmark.update(
			"Trimmed twig file2", self.test_case
		)

		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs trimmed: 2 (+2)\n")
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs trimmed: 2\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 1
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs trimmed: 2 (+1)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs trimmed: 2 (-98)\n")

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": -1 }
		self.assertIsNone(self.test_case.LonelyBookmark.view(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.Counter] = { "counter": 69 }
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs trimmed: 69 (+67)\n")
		self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)] = 100
		self.assertEqual(self.test_case.LonelyBookmark.view(self.test_case), "twigs trimmed: 69 (-31)\n")
		self.assertEqual(self.test_case.LonelyShelf[str(self.test_case.LonelyBookmark.Counter.Inducer)],"69")








	def test_LeafsGrown_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsGrown_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class GrowBookmark(VolumeBookmark):

				trigger		= "Grown leaf"
				rpattern	=  r"Grown leaf \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("leafs grown (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("LeafsGrown_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsGrown_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsGrown_repr:Assigned to {self.test_case.GrowBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsGrown_repr:Assigned to {self.test_case.GrowBookmark} bookmark "
			f"as {self.test_case.GrowBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.GrowBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Grown leaf \"file1\"", self.test_case
		)
		self.test_case.GrowBookmark.update(
			"Grown leaf \"file2\"", self.test_case
		)
		self.test_case.GrowBookmark.update(
			"Grown leaf \"file1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (3 (+3)): file1 (+), file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (3): file1, file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.GrowBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.GrowBookmark.Accumulator.ReprInducer)
		] = [ "file1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (3 (+2)): file1, file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.GrowBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.GrowBookmark.Accumulator.ReprInducer)
		] = [ "file2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (3 (-97)): file1 (+), file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)

		self.test_case[self.test_case.GrowBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"file1, file2\n"
		)
		self.test_case[self.test_case.GrowBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"file1, file2\n"
		)

		self.test_case[self.test_case.GrowBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (42 (+39)): "
		)

		self.test_case[self.test_case.GrowBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.GrowBookmark ])
		)

		self.test_case[self.test_case.GrowBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "file1", "file2", "file3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (69 (+27)): file1, file2, file3 (+)\n"
		)
		self.test_case[self.test_case.GrowBookmark.Accumulator] = { "counter": 10, "recap": [ "file1" ] }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.GrowBookmark ]),
			"leafs grown (10 (-59)): file1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.GrowBookmark.Accumulator.ReprInducer)
			],[ "file1" ]
		)








	def test_LeafsMoved_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsMoved_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class MoveBookmark(VolumeBookmark):

				trigger		= "Moved leaf"
				rpattern	=  r"Moved leaf \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("leafs moved (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("LeafsMoved_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsMoved_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsMoved_repr:Assigned to {self.test_case.MoveBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsMoved_repr:Assigned to {self.test_case.MoveBookmark} bookmark "
			f"as {self.test_case.MoveBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.MoveBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Moved leaf \"file1\"", self.test_case
		)
		self.test_case.MoveBookmark.update(
			"Moved leaf \"file2\"", self.test_case
		)
		self.test_case.MoveBookmark.update(
			"Moved leaf \"file1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (3 (+3)): file1 (+), file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (3): file1, file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.MoveBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.MoveBookmark.Accumulator.ReprInducer)
		] = [ "file1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (3 (+2)): file1, file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.MoveBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.MoveBookmark.Accumulator.ReprInducer)
		] = [ "file2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (3 (-97)): file1 (+), file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)

		self.test_case[self.test_case.MoveBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"file1, file2\n"
		)
		self.test_case[self.test_case.MoveBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"file1, file2\n"
		)

		self.test_case[self.test_case.MoveBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (42 (+39)): "
		)

		self.test_case[self.test_case.MoveBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.MoveBookmark ])
		)

		self.test_case[self.test_case.MoveBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "file1", "file2", "file3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (69 (+27)): file1, file2, file3 (+)\n"
		)
		self.test_case[self.test_case.MoveBookmark.Accumulator] = { "counter": 10, "recap": [ "file1" ] }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.MoveBookmark ]),
			"leafs moved (10 (-59)): file1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.MoveBookmark.Accumulator.ReprInducer)
			],[ "file1" ]
		)








	def test_LeafsCloned_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsCloned_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class CloneBookmark(VolumeBookmark):

				trigger		= "Cloned leaf"
				rpattern	=  r"Cloned leaf \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("leafs cloned (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("LeafsCloned_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsCloned_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsCloned_repr:Assigned to {self.test_case.CloneBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsCloned_repr:Assigned to {self.test_case.CloneBookmark} bookmark "
			f"as {self.test_case.CloneBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.CloneBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Cloned leaf \"file1\"", self.test_case
		)
		self.test_case.CloneBookmark.update(
			"Cloned leaf \"file2\"", self.test_case
		)
		self.test_case.CloneBookmark.update(
			"Cloned leaf \"file1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (3 (+3)): file1 (+), file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (3): file1, file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.CloneBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.CloneBookmark.Accumulator.ReprInducer)
		] = [ "file1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (3 (+2)): file1, file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.CloneBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.CloneBookmark.Accumulator.ReprInducer)
		] = [ "file2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (3 (-97)): file1 (+), file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)

		self.test_case[self.test_case.CloneBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"file1, file2\n"
		)
		self.test_case[self.test_case.CloneBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"file1, file2\n"
		)

		self.test_case[self.test_case.CloneBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (42 (+39)): "
		)

		self.test_case[self.test_case.CloneBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.CloneBookmark ])
		)

		self.test_case[self.test_case.CloneBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "file1", "file2", "file3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (69 (+27)): file1, file2, file3 (+)\n"
		)
		self.test_case[self.test_case.CloneBookmark.Accumulator] = { "counter": 10, "recap": [ "file1" ] }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.CloneBookmark ]),
			"leafs cloned (10 (-59)): file1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.CloneBookmark.Accumulator.ReprInducer)
			],[ "file1" ]
		)








	def test_LeafsPushed_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsPushed_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class PushBookmark(VolumeBookmark):

				trigger		= "Pushed leaf"
				rpattern	=  r"Pushed leaf \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("leafs pushed (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("LeafsPushed_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsPushed_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsPushed_repr:Assigned to {self.test_case.PushBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsPushed_repr:Assigned to {self.test_case.PushBookmark} bookmark "
			f"as {self.test_case.PushBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.PushBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Pushed leaf \"file1\"", self.test_case
		)
		self.test_case.PushBookmark.update(
			"Pushed leaf \"file2\"", self.test_case
		)
		self.test_case.PushBookmark.update(
			"Pushed leaf \"file1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (3 (+3)): file1 (+), file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (3): file1, file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.PushBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.PushBookmark.Accumulator.ReprInducer)
		] = [ "file1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (3 (+2)): file1, file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.PushBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.PushBookmark.Accumulator.ReprInducer)
		] = [ "file2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (3 (-97)): file1 (+), file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)

		self.test_case[self.test_case.PushBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"file1, file2\n"
		)
		self.test_case[self.test_case.PushBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"file1, file2\n"
		)

		self.test_case[self.test_case.PushBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (42 (+39)): "
		)

		self.test_case[self.test_case.PushBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.PushBookmark ])
		)

		self.test_case[self.test_case.PushBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "file1", "file2", "file3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (69 (+27)): file1, file2, file3 (+)\n"
		)
		self.test_case[self.test_case.PushBookmark.Accumulator] = { "counter": 10, "recap": [ "file1" ] }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.PushBookmark ]),
			"leafs pushed (10 (-59)): file1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.PushBookmark.Accumulator.ReprInducer)
			],[ "file1" ]
		)








	def test_TwigsThrived_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "TwigsThrived_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class ThriveBookmark(VolumeBookmark):

				trigger		= "Thrived twig"
				rpattern	=  r"Thrived twig \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("twigs thrived (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("TwigsThrived_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:TwigsThrived_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:TwigsThrived_repr:Assigned to {self.test_case.ThriveBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:TwigsThrived_repr:Assigned to {self.test_case.ThriveBookmark} bookmark "
			f"as {self.test_case.ThriveBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.ThriveBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Thrived twig \"file1\"", self.test_case
		)
		self.test_case.ThriveBookmark.update(
			"Thrived twig \"file2\"", self.test_case
		)
		self.test_case.ThriveBookmark.update(
			"Thrived twig \"file1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (3 (+3)): file1 (+), file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (3): file1, file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.ThriveBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.ThriveBookmark.Accumulator.ReprInducer)
		] = [ "file1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (3 (+2)): file1, file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.ThriveBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.ThriveBookmark.Accumulator.ReprInducer)
		] = [ "file2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (3 (-97)): file1 (+), file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)

		self.test_case[self.test_case.ThriveBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"file1, file2\n"
		)
		self.test_case[self.test_case.ThriveBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"file1, file2\n"
		)

		self.test_case[self.test_case.ThriveBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (42 (+39)): "
		)

		self.test_case[self.test_case.ThriveBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.ThriveBookmark ])
		)

		self.test_case[self.test_case.ThriveBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "file1", "file2", "file3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (69 (+27)): file1, file2, file3 (+)\n"
		)
		self.test_case[self.test_case.ThriveBookmark.Accumulator] = { "counter": 10, "recap": [ "file1" ] }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.ThriveBookmark ]),
			"twigs thrived (10 (-59)): file1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.ThriveBookmark.Accumulator.ReprInducer)
			],[ "file1" ]
		)








	def test_LeafsTrimmed_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "LeafsTrimmed_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class LeafsTrimmedBookmark(VolumeBookmark):

				trigger		= "Trimmed leaf"
				rpattern	=  r"Trimmed leaf \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("leafs trimmed (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("LeafsTrimmed_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:LeafsTrimmed_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:LeafsTrimmed_repr:Assigned to {self.test_case.LeafsTrimmedBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:LeafsTrimmed_repr:Assigned to {self.test_case.LeafsTrimmedBookmark} bookmark "
			f"as {self.test_case.LeafsTrimmedBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.LeafsTrimmedBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Trimmed leaf \"file1\"", self.test_case
		)
		self.test_case.LeafsTrimmedBookmark.update(
			"Trimmed leaf \"file2\"", self.test_case
		)
		self.test_case.LeafsTrimmedBookmark.update(
			"Trimmed leaf \"file1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (3 (+3)): file1 (+), file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (3): file1, file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.ReprInducer)
		] = [ "file1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (3 (+2)): file1, file2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.ReprInducer)
		] = [ "file2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (3 (-97)): file1 (+), file2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "file1", "file2" ]
		)

		self.test_case[self.test_case.LeafsTrimmedBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"file1, file2\n"
		)
		self.test_case[self.test_case.LeafsTrimmedBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "file1", "file2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"file1, file2\n"
		)

		self.test_case[self.test_case.LeafsTrimmedBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (42 (+39)): "
		)

		self.test_case[self.test_case.LeafsTrimmedBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ])
		)

		self.test_case[self.test_case.LeafsTrimmedBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "file1", "file2", "file3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (69 (+27)): file1, file2, file3 (+)\n"
		)
		self.test_case[self.test_case.LeafsTrimmedBookmark.Accumulator] = {

			"counter":	10,
			"recap":	[ "file1" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.LeafsTrimmedBookmark ]),
			"leafs trimmed (10 (-59)): file1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.LeafsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "file1" ]
		)








	def test_TwigsTrimmed_repr(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_BOOKMARK
				init_name	= "TwigsTrimmed_repr"
				init_level	= 10

			class Annex(VolumeAnnex):			pass
			class LonelyShelf(LibraryShelf):	pass
			class TwigsTrimmedBookmark(VolumeBookmark):

				trigger		= "Trimmed twig"
				rpattern	=  r"Trimmed twig \"(?P<target>.+)\"$"

				@AccessHandlerRegisterCounter
				class Accumulator(TargetStringAccumulator):

					@TextWrapper("twigs trimmed (","): ")
					@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
					class CountInducer(RegisterCounterInducer): filter = posnum
					@TextWrapper(footer="\n")
					class ReprInducer(AccessBookmarkCase.CasedStringsAccumulatorInducer):

						case_link	= "LonelyShelf"
						unique		= True
						joint		= ", "

		with self.assertLogs("TwigsTrimmed_repr", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(f"DEBUG:TwigsTrimmed_repr:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:TwigsTrimmed_repr:Assigned to {self.test_case.TwigsTrimmedBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:TwigsTrimmed_repr:Assigned to {self.test_case.TwigsTrimmedBookmark} bookmark "
			f"as {self.test_case.TwigsTrimmedBookmark.Accumulator} inducer",
			case_loggy.output
		)

		self.test_case.TwigsTrimmedBookmark.update(
			"31/12/2024 2359 @pygwarts INFO : Trimmed twig \"dir1\"", self.test_case
		)
		self.test_case.TwigsTrimmedBookmark.update(
			"Trimmed twig \"dir2\"", self.test_case
		)
		self.test_case.TwigsTrimmedBookmark.update(
			"Trimmed twig \"dir1\"", self.test_case
		)

		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (3 (+3)): dir1 (+), dir2 (+)\n"
		)
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (3): dir1, dir2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "dir1", "dir2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.CountInducer)
		] =	"1"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.ReprInducer)
		] = [ "dir1" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (3 (+2)): dir1, dir2 (+)\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "dir1", "dir2" ]
		)
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.CountInducer)
		] =	"100"
		self.test_case.LonelyShelf[

			str(self.test_case)
		][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.ReprInducer)
		] = [ "dir2" ]
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (3 (-97)): dir1 (+), dir2\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.CountInducer)
			],	"3"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "dir1", "dir2" ]
		)

		self.test_case[self.test_case.TwigsTrimmedBookmark.Accumulator] = {

			"counter":	0,
			"recap":	[ "dir1", "dir2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"dir1, dir2\n"
		)
		self.test_case[self.test_case.TwigsTrimmedBookmark.Accumulator] = {

			"counter":	-1,
			"recap":	[ "dir1", "dir2" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"dir1, dir2\n"
		)

		self.test_case[self.test_case.TwigsTrimmedBookmark.Accumulator] = { "counter": 42, "recap": None }
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (42 (+39)): "
		)

		self.test_case[self.test_case.TwigsTrimmedBookmark.Accumulator] = { "counter": 0, "recap": None }
		self.assertIsNone(
			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ])
		)

		self.test_case[self.test_case.TwigsTrimmedBookmark.Accumulator] = {

			"counter":	69,
			"recap":	[ "dir1", "dir2", "dir3" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (69 (+27)): dir1, dir2, dir3 (+)\n"
		)
		self.test_case[self.test_case.TwigsTrimmedBookmark.Accumulator] = {

			"counter":	10,
			"recap":	[ "dir1" ]
		}
		self.assertEqual(

			self.test_case.Annex([ self.test_case.TwigsTrimmedBookmark ]),
			"twigs trimmed (10 (-59)): dir1\n"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.CountInducer)
			],	"10"
		)
		self.assertEqual(

			self.test_case.LonelyShelf[

				str(self.test_case)
			][	str(self.test_case.TwigsTrimmedBookmark.Accumulator.ReprInducer)
			],[ "dir1" ]
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







