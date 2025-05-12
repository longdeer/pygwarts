import	os
import	unittest
from	pygwarts.magical.philosophers_stone		import Transmutable
from	pygwarts.tests.irma						import IrmaTestCase
from	pygwarts.irma.contrib					import LibraryContrib
from	pygwarts.irma.shelve					import LibraryShelf
from	pygwarts.irma.shelve.casing				import is_num
from	pygwarts.irma.shelve.casing				import num_diff
from	pygwarts.irma.access.volume				import LibraryVolume
from	pygwarts.irma.access.bookmarks			import VolumeBookmark
from	pygwarts.irma.access.handlers			import AccessHandler
from	pygwarts.irma.access.inducers			import AccessInducer
from	pygwarts.irma.access.inducers.counters	import HandlerCounterInducer
from	pygwarts.irma.access.inducers.counters	import RegisterCounterInducer
from	pygwarts.irma.access.inducers.recap		import RegisterRecapInducer
from	pygwarts.irma.access.inducers.recap		import RegisterRecapAccumulatorInducer
from	pygwarts.irma.access.inducers.filters	import posnum
from	pygwarts.irma.access.inducers.filters	import negnum
from	pygwarts.irma.access.inducers.filters	import nonnegnum
from	pygwarts.irma.access.inducers.filters	import nonposnum
from	pygwarts.irma.access.inducers.filters	import zeronum
from	pygwarts.irma.access.inducers.filters	import plurnum
from	pygwarts.irma.access.inducers.case		import InducerCase








class AccessInducerCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_INDUCER): os.remove(cls.ACCESS_INDUCER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.ACCESS_INDUCER)
	def test_no_upper_init(self):

		class LonelyInducer(AccessInducer):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "no_upper_init"
				init_level	= 10

		with self.assertLogs("no_upper_init", 10) as case_loggy : self.test_case = LonelyInducer()
		self.assertIn(

			f"INFO:no_upper_init:AccessInducer {self.test_case} not registered to any handler",
			case_loggy.output
		)


	def test_handler_init(self):
		class LonelyHandler(AccessHandler):

			class LonelyInducer(AccessInducer):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "handler_init"
				init_level	= 10

		with self.assertLogs("handler_init", 10) as case_loggy : self.test_case = LonelyHandler()
		self.assertIn(

			f"INFO:handler_init:AccessHandler {self.test_case} not assigned to any bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:handler_init:AccessInducer {self.test_case.LonelyInducer} not assigned to any bookmark",
			case_loggy.output
		)


	def test_bookmark_init(self):

		class LonelyBookmark(VolumeBookmark):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "bookmark_init"
				init_level	= 10

			class LonelyHandler(AccessHandler):
				class LonelyInducer(AccessInducer):	pass

		with self.assertLogs("bookmark_init", 10) as case_loggy : self.test_case = LonelyBookmark()
		self.assertIn(

			f"INFO:bookmark_init:Bookmark {self.test_case} not assigned to library",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:bookmark_init:Assigned to {self.test_case} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:bookmark_init:Assigned to {self.test_case} bookmark "
			f"as {self.test_case.LonelyHandler} inducer",
			case_loggy.output
		)


	def test_not_handler_init(self):

		class LonelyBookmark(VolumeBookmark):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "not_handler_init"
				init_level	= 10

			class NotHandler(Transmutable):
				class LonelyInducer(AccessInducer):	pass

		with self.assertLogs("not_handler_init", 10) as case_loggy : self.test_case = LonelyBookmark()
		self.assertIn(

			f"INFO:not_handler_init:Bookmark {self.test_case} not assigned to library",
			case_loggy.output
		)
		self.assertIn(

			"INFO:not_handler_init:AccessInducer "
			f"{self.test_case.NotHandler.LonelyInducer} not registered to any handler",
			case_loggy.output
		)


	def test_not_bookmark_init(self):

		class NotBookmark(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "not_bookmark_init"
				init_level	= 10

			class LonelyHandler(AccessHandler):
				class LonelyInducer(AccessInducer):	pass

		with self.assertLogs("not_bookmark_init", 10) as case_loggy : self.test_case = NotBookmark()
		self.assertIn(

			"INFO:not_bookmark_init:AccessInducer "
			f"{self.test_case.LonelyHandler.LonelyInducer} not assigned to any bookmark",
			case_loggy.output
		)




	def test_getters(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "getters"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(AccessInducer):	pass

		with self.assertLogs("getters", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:getters:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:getters:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:getters:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:getters:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.LonelyHandler.access_handler_counter = 9001
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = {

			"counter":	420,
			"recap":	69,
		}
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.get_handler_counter(),
			9001
		)
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.get_register_counter(self.test_case),
			420
		)
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.get_register_recap(self.test_case),
			69
		)




	def test_handler_counter(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "handler_counter"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(HandlerCounterInducer):	pass

		with self.assertLogs("handler_counter", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:handler_counter:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:handler_counter:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:handler_counter:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:handler_counter:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case.LonelyBookmark.LonelyHandler.access_handler_counter = 9001
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"9001"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E: E if 0 <E else None
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"9001"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E: E if 9000 <E else None
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"9001"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E: E if 0 == E else None
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in (

			1, 1., "filter", True, False, None, ...,
			[ lambda E : E if 0 <E else None ],
			( lambda E : E if 0 <E else None, ),
			{ lambda E : E if 0 <E else None },
			{ "filter": lambda E : E if 0 <E else None },
		):
			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = invalid
			with self.subTest(filter=invalid), self.assertLogs("handler_counter", 10) as case_loggy :
				self.assertEqual(

					self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
					"9001"
				)
			self.assertIn(f"DEBUG:handler_counter:Filter not applied", case_loggy.output)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = None
		for	invalid in (

			"9001", None, ..., print, unittest,
			[ 9001 ],( 9001, ),{ 9001 },{ "access_handler_counter": 9001 },
		):
			self.test_case.LonelyBookmark.LonelyHandler.access_handler_counter = invalid
			with self.subTest(access_handler_counter=invalid):
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_register_counter(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "register_counter"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterCounterInducer):	pass

		with self.assertLogs("register_counter", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:register_counter:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:register_counter:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:register_counter:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:register_counter:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "counter": 420 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"420"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E : E if 0 <E else None
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"420"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E : E if 1 <E else None
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"420"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E : E if 0 == E else None
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in (

			1, 1., "filter", True, False, None, ...,
			[ lambda E : E if 0 <E else None ],
			( lambda E : E if 0 <E else None, ),
			{ lambda E : E if 0 <E else None },
			{ "filter": lambda E : E if 0 <E else None },
		):
			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = invalid
			with self.subTest(filter=invalid), self.assertLogs("register_counter", 10) as case_loggy :
				self.assertEqual(

					self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
					"420"
				)
			self.assertIn(f"DEBUG:register_counter:Filter not applied", case_loggy.output)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = None
		for	invalid in (

			"420", None, ..., print, unittest,
			[ 420 ],( 420, ),{ 420 },{ "access_handler_counter": 420 },
		):
			self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "counter": invalid }
			with self.subTest(register_counter=invalid):
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_register_recap(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "register_recap"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	pass

		with self.assertLogs("register_recap", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:register_recap:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:register_recap:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:register_recap:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:register_recap:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E: E if 0 <E else None
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E: E if 1 <E else None
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = lambda E: E if 0 == E else None
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in (

			1, 1., "filter", True, False, None, ...,
			[ lambda E : E if 0 <E else None ],
			( lambda E : E if 0 <E else None, ),
			{ lambda E : E if 0 <E else None },
			{ "filter": lambda E : E if 0 <E else None },
		):
			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = invalid
			with self.subTest(filter=invalid), self.assertLogs("register_recap", 10) as case_loggy :
				self.assertEqual(

					self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
					"69"
				)
			self.assertIn(f"DEBUG:register_recap:Filter not applied", case_loggy.output)

		self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.filter = None
		for	variant in (

			69., "69", True, False, ...,
			[ 69 ],( 69, ),{ 69 },{ "recap": 69 },
		):
			with self.subTest(recap=variant):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": variant }
				self.assertEqual(

					self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
					str(variant)
				)








	def test_register_recap_accumulator(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "recap_accumulator"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapAccumulatorInducer):	pass

		with self.assertLogs("recap_accumulator", 10) as case_loggy:

			self.test_case = LonelyVolume()
			self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": [ 420,69,69 ] }
			self.assertEqual(

				self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
				"420 69 69"
			)

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.joint = "\n"
			self.assertEqual(

				self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
				"420\n69\n69"
			)

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer.unique = True
			self.assertEqual(

				self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
				"420\n69"
			)

		self.assertIn(

			f"INFO:recap_accumulator:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:recap_accumulator:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:recap_accumulator:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:recap_accumulator:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)
		self.assertIn("DEBUG:recap_accumulator:Accumulated 9 symbols string", case_loggy.output)
		self.assertEqual(case_loggy.output.count("DEBUG:recap_accumulator:Accumulated 9 symbols string"), 2)
		self.assertIn("DEBUG:recap_accumulator:Accumulated 6 symbols string", case_loggy.output)

		for	invalid in (

			1, 1., "filter", True, False, None, ...,
			( 420,69,69, ),{ 420,69,69 },{ "filter": [ 420,69,69 ] }
		):
			self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
			self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_filter_posnum(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "filter_posnum"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	filter = posnum

		with self.assertLogs("filter_posnum", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:filter_posnum:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:filter_posnum:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:filter_posnum:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:filter_posnum:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": .69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0.69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			".69"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "0" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".0" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in ( "filter", True, False, None, ...,[ 42 ],( 42, ),{ 42 },{ "value": 42 }):
			with self.subTest(value=invalid):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_filter_negnum(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "filter_negnum"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	filter = negnum

		with self.assertLogs("filter_negnum", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:filter_negnum:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:filter_negnum:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:filter_negnum:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:filter_negnum:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -.69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-0.69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-.69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-.69"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "0" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".0" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in ( "filter", True, False, None, ...,[ 42 ],( 42, ),{ 42 },{ "value": 42 }):
			with self.subTest(value=invalid):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_filter_nonnegnum(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "filter_nonnegnum"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	filter = nonnegnum

		with self.assertLogs("filter_nonnegnum", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:filter_nonnegnum:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:filter_nonnegnum:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:filter_nonnegnum:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:filter_nonnegnum:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0. }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0.0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "0" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".0" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			".0"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69. }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69.0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			".69"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-.69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in ( "filter", True, False, None, ...,[ 42 ],( 42, ),{ 42 },{ "value": 42 }):
			with self.subTest(value=invalid):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_filter_nonposnum(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "filter_nonposnum"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	filter = nonposnum

		with self.assertLogs("filter_nonposnum", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:filter_nonposnum:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:filter_nonposnum:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:filter_nonposnum:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:filter_nonposnum:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0. }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0.0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "0" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".0" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			".0"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69. }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-69.0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-.69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"-.69"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in ( "filter", True, False, None, ...,[ 42 ],( 42, ),{ 42 },{ "value": 42 }):
			with self.subTest(value=invalid):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_filter_zeronum(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "filter_zeronum"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	filter = zeronum

		with self.assertLogs("filter_zeronum", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:filter_zeronum:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:filter_zeronum:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:filter_zeronum:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:filter_zeronum:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0. }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0.0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "0" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".0" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			".0"
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": -69. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "-.69" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in ( "filter", True, False, None, ...,[ 42 ],( 42, ),{ 42 },{ "value": 42 }):
			with self.subTest(value=invalid):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_filter_plurnum(self):

		class LonelyVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "filter_plurnum"
				init_level	= 10

			class LonelyBookmark(VolumeBookmark):
				trigger = "trigger"

				class LonelyHandler(AccessHandler):
					class LonelyInducer(RegisterRecapInducer):	filter = plurnum

		with self.assertLogs("filter_plurnum", 10) as case_loggy : self.test_case = LonelyVolume()
		self.assertIn(

			f"INFO:filter_plurnum:Volume {self.test_case} not assigned to any library",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:filter_plurnum:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(

			f"DEBUG:filter_plurnum:Assigned to {self.test_case.LonelyBookmark} bookmark",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:filter_plurnum:Assigned to {self.test_case.LonelyBookmark} bookmark "
			f"as {self.test_case.LonelyBookmark.LonelyHandler} inducer",
			case_loggy.output
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69 }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 69. }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69.0"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "69" }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69"
		)
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "69." }
		self.assertEqual(

			self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case),
			"69."
		)

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 1 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 1. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "1" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "1." }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0 }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": 0. }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": "0" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))
		self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": ".0" }
		self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))

		for	invalid in ( "filter", True, False, None, ...,[ 42 ],( 42, ),{ 42 },{ "value": 42 }):
			with self.subTest(value=invalid):

				self.test_case[self.test_case.LonelyBookmark.LonelyHandler] = { "recap": invalid }
				self.assertIsNone(self.test_case.LonelyBookmark.LonelyHandler.LonelyInducer(self.test_case))








	def test_InducerCase(self):
		class FakeLibrary(Transmutable):

			class LonelyVolume(LibraryVolume):	pass
			class LonelyShelf(LibraryShelf):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_INDUCER
				init_name	= "InducerCase"
				init_level	= 10

			@InducerCase("LonelyShelf", prep=is_num, post=num_diff)
			class LonelyInducer(AccessInducer):
				def __call__(self, volume :LibraryVolume) -> str : return "69"

		self.test_case = FakeLibrary()
		self.assertIsNone(self.test_case.LonelyShelf[str(self.test_case.LonelyVolume)])
		self.assertEqual(self.test_case.LonelyInducer(self.test_case.LonelyVolume), "69 (+69)")
		self.assertEqual(self.test_case.LonelyInducer(self.test_case.LonelyVolume), "69")
		self.assertEqual(
			self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			],	"69"
		)
		self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			] =	"68"
		self.assertEqual(self.test_case.LonelyInducer(self.test_case.LonelyVolume), "69 (+1)")
		self.assertEqual(
			self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			],	"69"
		)
		self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			] =	"70"
		self.assertEqual(self.test_case.LonelyInducer(self.test_case.LonelyVolume), "69 (-1)")
		self.assertEqual(
			self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			],	"69"
		)
		self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			] =	"69"
		self.assertEqual(self.test_case.LonelyInducer(self.test_case.LonelyVolume), "69")
		self.assertEqual(
			self.test_case.LonelyShelf[
				str(self.test_case.LonelyVolume)
			][	str(self.test_case.LonelyInducer)
			],	"69"
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







