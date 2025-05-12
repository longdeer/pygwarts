import	os
import	re
import	unittest
from	pygwarts.magical.philosophers_stone		import Transmutable
from	pygwarts.tests.irma						import IrmaTestCase
from	pygwarts.irma.contrib					import LibraryContrib
from	pygwarts.irma.access.handlers			import AccessHandler
from	pygwarts.irma.access.handlers			import AccessHandlerCounter
from	pygwarts.irma.access.handlers			import AccessHandlerRegisterCounter
from	pygwarts.irma.access.handlers.counters	import AccessCounter
from	pygwarts.irma.access.handlers.parsers	import GroupParser
from	pygwarts.irma.access.handlers.parsers	import TargetHandler
from	pygwarts.irma.access.handlers.parsers	import TargetNumberAccumulator
from	pygwarts.irma.access.handlers.parsers	import TargetStringAccumulator
from	pygwarts.irma.access.bookmarks			import VolumeBookmark
from	pygwarts.irma.access.volume				import LibraryVolume








class AccessHandlerCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_HANDLER): os.remove(cls.ACCESS_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.ACCESS_HANDLER)
	def test_no_upper_init(self):

		class LonelyHandler(AccessHandler):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "no_upper_init"
				init_level	= 10

		with self.assertLogs("no_upper_init", 10) as case_loggy : self.test_case = LonelyHandler()
		self.assertIn(

			f"INFO:no_upper_init:AccessHandler {self.test_case} not assigned to any bookmark",
			case_loggy.output
		)


	def test_bookmark_init(self):
		class LonelyBookmark(VolumeBookmark):

			class LonelyHandler(AccessHandler):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "bookmark_init"
				init_level	= 10

		with self.assertLogs("bookmark_init", 10) as case_loggy : self.test_case = LonelyBookmark()
		self.assertIn(

			f"INFO:bookmark_init:Bookmark {self.test_case} not assigned to library",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:bookmark_init:Assigned to {self.test_case} bookmark",
			case_loggy.output
		)


	def test_no_bookmark_init(self):
		class NotBookmark(Transmutable):

			class NotBookmarkHandler(AccessHandler):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "no_bookmark_init"
				init_level	= 10

		with self.assertLogs("no_bookmark_init", 10) as case_loggy : self.test_case = NotBookmark()
		self.assertIn(

			f"INFO:no_bookmark_init:AccessHandler {self.test_case.NotBookmarkHandler} "
			"not assigned to any bookmark",
			case_loggy.output
		)








	def test_registered_valid(self):

		class TestVolume(LibraryVolume):
			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				class Handler(AccessHandler): pass

		self.test_case = TestVolume()
		handler = AccessHandler()
		volume = LibraryVolume()

		self.assertNotIn(self.test_case.TestBookmark.Handler, self.test_case)
		self.assertTrue(self.test_case.TestBookmark.Handler.registered(self.test_case))
		self.assertIn(self.test_case.TestBookmark.Handler, self.test_case)

		self.assertNotIn(handler, self.test_case)
		self.assertTrue(handler.registered(self.test_case))
		self.assertIn(handler, self.test_case)

		self.assertNotIn(self.test_case.TestBookmark.Handler, volume)
		self.assertTrue(self.test_case.TestBookmark.Handler.registered(volume))
		self.assertIn(self.test_case.TestBookmark.Handler, volume)

		self.assertNotIn(handler, volume)
		self.assertTrue(handler.registered(volume))
		self.assertIn(handler, volume)


	def test_registered_invalid(self):

		class TestVolume(LibraryVolume):
			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				class Handler(AccessHandler): pass

		self.test_case = TestVolume()
		handler = AccessHandler()

		for invalid in (

			420, 69., True, False, None, ..., print, unittest, LibraryVolume,
			[ LibraryVolume ],( LibraryVolume, ),{ LibraryVolume },{ "volume": LibraryVolume }
		):
			self.assertIsNone(self.test_case.TestBookmark.Handler.registered(invalid))
			self.assertIsNone(handler.registered(invalid))


	def test_registered_invalid_mapping(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "registered_invalid_mapping"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				class Handler(AccessHandler): pass

		self.test_case = TestVolume()
		handler = AccessHandler()
		volume = LibraryVolume()

		for invalid in (

			420, 69., True, False, ..., print, unittest, LibraryVolume,
			[ LibraryVolume ],( LibraryVolume, ),{ LibraryVolume }
		):
			with self.subTest(mapping=invalid):

				self.test_case[self.test_case.TestBookmark.Handler] = invalid
				self.assertEqual(self.test_case[self.test_case.TestBookmark.Handler], invalid)

				with self.assertLogs("registered_invalid_mapping", 10) as case_loggy:
					self.assertIsNone(self.test_case.TestBookmark.Handler.registered(self.test_case))

				self.assertEqual(self.test_case[self.test_case.TestBookmark.Handler], invalid)
				self.assertIn(

					f"DEBUG:registered_invalid_mapping:Invalid mapping in {self.test_case} volume",
					case_loggy.output
				)

				volume[self.test_case.TestBookmark.Handler] = invalid
				self.assertEqual(volume[self.test_case.TestBookmark.Handler], invalid)

				with self.assertLogs("registered_invalid_mapping", 10) as case_loggy:
					self.assertIsNone(self.test_case.TestBookmark.Handler.registered(volume))

				self.assertEqual(volume[self.test_case.TestBookmark.Handler], invalid)
				self.assertIn(

					f"DEBUG:registered_invalid_mapping:Invalid mapping in {volume} volume",
					case_loggy.output
				)

				self.test_case[handler] = invalid
				self.assertEqual(self.test_case[handler], invalid)
				self.assertIsNone(handler.registered(self.test_case))
				self.assertEqual(self.test_case[handler], invalid)

				volume[handler] = invalid
				self.assertEqual(volume[handler], invalid)
				self.assertIsNone(handler.registered(volume))
				self.assertEqual(volume[handler], invalid)








	def test_AccessHandlerRegisterCounter_no_link(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "AccessHandlerRegisterCounter_no_link"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerRegisterCounter
				class Handler(AccessHandler):

					# Imitating handler that makes no link
					def __call__(self, line :str, volume :LibraryVolume): return True

		with self.assertLogs("AccessHandlerRegisterCounter_no_link", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Handler("this is line", self.test_case)

		self.assertIsNone(self.test_case[self.test_case.TestBookmark.Handler])
		self.assertIn(

			"DEBUG:AccessHandlerRegisterCounter_no_link:"
			f"{self.test_case} counter link was not created",
			case_loggy.output
		)








	def test_AccessCounter(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "AccessCounter"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				class Counter(AccessCounter):	pass

		with self.assertLogs("AccessCounter", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("line", self.test_case)
			self.test_case.TestBookmark.Counter("line", self.test_case)
			self.test_case.TestBookmark.Counter("line", self.test_case)

		self.assertIn(
			f"INFO:AccessCounter:Volume {self.test_case} not assigned to any library", case_loggy.output
		)
		self.assertIn(f"DEBUG:AccessCounter:Assigned to volume {self.test_case}", case_loggy.output)
		self.assertIn(
			f"DEBUG:AccessCounter:Assigned to {self.test_case.TestBookmark} bookmark", case_loggy.output
		)

		self.assertIn("DEBUG:AccessCounter:Handler counter incremented to 1", case_loggy.output)
		self.assertIn("DEBUG:AccessCounter:Handler counter incremented to 2", case_loggy.output)
		self.assertIn("DEBUG:AccessCounter:Handler counter incremented to 3", case_loggy.output)
		self.assertTrue(hasattr(self.test_case.TestBookmark.Counter, "access_handler_counter"))
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)

		self.assertIn(f"DEBUG:AccessCounter:{self.test_case} counter incremented to 1", case_loggy.output)
		self.assertIn(f"DEBUG:AccessCounter:{self.test_case} counter incremented to 2", case_loggy.output)
		self.assertIn(f"DEBUG:AccessCounter:{self.test_case} counter incremented to 3", case_loggy.output)
		self.assertIn(self.test_case.TestBookmark.Counter, self.test_case)
		self.assertIn("counter", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 3)








	def test_GroupParser_no_rpattern(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "GroupParser_no_rpattern"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				class Counter(GroupParser):	pass

		with self.assertLogs("GroupParser_no_rpattern", 10) as case_loggy : self.test_case = TestVolume()
		self.assertIn(

			f"WARNING:GroupParser_no_rpattern:{self.test_case.TestBookmark.Counter} "
			"doesn't have pattern for parsing",
			case_loggy.output
		)




	def test_GroupParser_type_rpattern(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "GroupParser_type_rpattern"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				class Counter(GroupParser): rpattern = 42

		with self.assertLogs("GroupParser_type_rpattern", 10) as case_loggy : self.test_case = TestVolume()
		self.assertIn(

			f"WARNING:GroupParser_type_rpattern:{self.test_case.TestBookmark.Counter} "
			"has invalid pattern for parsing",
			case_loggy.output
		)








	def test_TargetHandler_str(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "TargetHandler_str"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerCounter
				@AccessHandlerRegisterCounter
				class Counter(TargetHandler): rpattern = r"(?P<target>42)"

		with self.assertLogs("TargetHandler_str", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("the answer is 42", self.test_case)

		self.assertIn(
			"DEBUG:TargetHandler_str:Accepted string \"(?P<target>42)\"", case_loggy.output
		)
		self.assertIn("DEBUG:TargetHandler_str:Recap set to \"42\"", case_loggy.output)
		self.assertIsInstance(self.test_case[self.test_case.TestBookmark.Counter], dict)
		self.assertIn("recap", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_str:Handler counter incremented to 1", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 1)
		self.assertIn(
			f"DEBUG:TargetHandler_str:{self.test_case} counter incremented to 1", case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 1)


		self.test_case[self.test_case.TestBookmark.Counter]["recap"] = "69"
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "69")


		with self.assertLogs("TargetHandler_str", 10) as case_loggy:
			self.test_case.TestBookmark.update("the answer is 42", self.test_case)

		self.assertIn("DEBUG:TargetHandler_str:Recap set to \"42\"", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_str:Handler counter incremented to 2", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 2)
		self.assertIn(
			f"DEBUG:TargetHandler_str:{self.test_case} counter incremented to 2", case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetHandler_str", 10) as case_loggy:
			self.test_case.TestBookmark.update("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetHandler_str:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_str:Handler counter incremented to 3", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetHandler_str", 10) as case_loggy:
			self.test_case.TestBookmark.Counter("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetHandler_str:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_str:Handler counter incremented to 4", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 4)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)




	def test_TargetHandler_Pattern(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "TargetHandler_Pattern"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerCounter
				@AccessHandlerRegisterCounter
				class Counter(TargetHandler): rpattern = re.compile(r"(?P<target>42)")

		with self.assertLogs("TargetHandler_Pattern", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("the answer is 42", self.test_case)

		self.assertIn(
			"DEBUG:TargetHandler_Pattern:Accepted pattern \"(?P<target>42)\"", case_loggy.output
		)
		self.assertIn("DEBUG:TargetHandler_Pattern:Recap set to \"42\"", case_loggy.output)
		self.assertIsInstance(self.test_case[self.test_case.TestBookmark.Counter], dict)
		self.assertIn("recap", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_Pattern:Handler counter incremented to 1", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 1)
		self.assertIn(
			f"DEBUG:TargetHandler_Pattern:{self.test_case} counter incremented to 1", case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 1)


		self.test_case[self.test_case.TestBookmark.Counter]["recap"] = "69"
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "69")


		with self.assertLogs("TargetHandler_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.update("the answer is 42", self.test_case)

		self.assertIn("DEBUG:TargetHandler_Pattern:Recap set to \"42\"", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_Pattern:Handler counter incremented to 2", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 2)
		self.assertIn(
			f"DEBUG:TargetHandler_Pattern:{self.test_case} counter incremented to 2", case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetHandler_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.update("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetHandler_Pattern:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_Pattern:Handler counter incremented to 3", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetHandler_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.Counter("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetHandler_Pattern:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), "42")
		self.assertIn("DEBUG:TargetHandler_Pattern:Handler counter incremented to 4", case_loggy.output)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 4)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)








	def test_TargetNumberAccumulator_str(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "TargetNumberAccumulator_str"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerCounter
				@AccessHandlerRegisterCounter
				class Counter(TargetNumberAccumulator): rpattern = r"(?P<target>42)"

		with self.assertLogs("TargetNumberAccumulator_str", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("the answer is 42", self.test_case)

		self.assertIn(
			"DEBUG:TargetNumberAccumulator_str:Accepted string \"(?P<target>42)\"", case_loggy.output
		)
		self.assertIn("DEBUG:TargetNumberAccumulator_str:Recap accumulation is \"42\"", case_loggy.output)
		self.assertIsInstance(self.test_case[self.test_case.TestBookmark.Counter], dict)
		self.assertIn("recap", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 42)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_str:Handler counter incremented to 1", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 1)
		self.assertIn(

			f"DEBUG:TargetNumberAccumulator_str:{self.test_case} counter incremented to 1",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 1)


		with self.assertLogs("TargetNumberAccumulator_str", 10) as case_loggy:
			self.test_case.TestBookmark.update("the answer is 42", self.test_case)

		self.assertIn("DEBUG:TargetNumberAccumulator_str:Recap accumulation is \"84\"", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 84)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_str:Handler counter incremented to 2", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 2)
		self.assertIn(

			f"DEBUG:TargetNumberAccumulator_str:{self.test_case} counter incremented to 2",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetNumberAccumulator_str", 10) as case_loggy:
			self.test_case.TestBookmark.update("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetNumberAccumulator_str:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 84)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_str:Handler counter incremented to 3", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetNumberAccumulator_str", 10) as case_loggy:
			self.test_case.TestBookmark.Counter("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetNumberAccumulator_str:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 84)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_str:Handler counter incremented to 4", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 4)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)




	def test_TargetNumberAccumulator_Pattern(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "TargetNumberAccumulator_Pattern"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerCounter
				@AccessHandlerRegisterCounter
				class Counter(TargetNumberAccumulator): rpattern = re.compile(r"(?P<target>42)")

		with self.assertLogs("TargetNumberAccumulator_Pattern", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("the answer is 42", self.test_case)

		self.assertIn(
			"DEBUG:TargetNumberAccumulator_Pattern:Accepted pattern \"(?P<target>42)\"", case_loggy.output
		)
		self.assertIn("DEBUG:TargetNumberAccumulator_Pattern:Recap accumulation is \"42\"", case_loggy.output)
		self.assertIsInstance(self.test_case[self.test_case.TestBookmark.Counter], dict)
		self.assertIn("recap", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 42)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_Pattern:Handler counter incremented to 1", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 1)
		self.assertIn(

			f"DEBUG:TargetNumberAccumulator_Pattern:{self.test_case} counter incremented to 1",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 1)


		with self.assertLogs("TargetNumberAccumulator_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.update("the answer is 42", self.test_case)

		self.assertIn("DEBUG:TargetNumberAccumulator_Pattern:Recap accumulation is \"84\"", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 84)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_Pattern:Handler counter incremented to 2", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 2)
		self.assertIn(

			f"DEBUG:TargetNumberAccumulator_Pattern:{self.test_case} counter incremented to 2",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetNumberAccumulator_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.update("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetNumberAccumulator_Pattern:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 84)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_Pattern:Handler counter incremented to 3", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetNumberAccumulator_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.Counter("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetNumberAccumulator_Pattern:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"), 84)
		self.assertIn(
			"DEBUG:TargetNumberAccumulator_Pattern:Handler counter incremented to 4", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 4)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)








	def test_TargetStringAccumulator_str(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "TargetStringAccumulator_str"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerCounter
				@AccessHandlerRegisterCounter
				class Counter(TargetStringAccumulator): rpattern = r"(?P<target>42)"

		with self.assertLogs("TargetStringAccumulator_str", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("the answer is 42", self.test_case)

		self.assertIn(
			"DEBUG:TargetStringAccumulator_str:Accepted string \"(?P<target>42)\"", case_loggy.output
		)
		self.assertIn("DEBUG:TargetStringAccumulator_str:Recap extended to 1 item", case_loggy.output)
		self.assertIsInstance(self.test_case[self.test_case.TestBookmark.Counter], dict)
		self.assertIn("recap", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_str:Handler counter incremented to 1", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 1)
		self.assertIn(

			f"DEBUG:TargetStringAccumulator_str:{self.test_case} counter incremented to 1",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 1)


		with self.assertLogs("TargetStringAccumulator_str", 10) as case_loggy:
			self.test_case.TestBookmark.update("the answer is 42", self.test_case)

		self.assertIn("DEBUG:TargetStringAccumulator_str:Recap extended to 2 items", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42","42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_str:Handler counter incremented to 2", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 2)
		self.assertIn(

			f"DEBUG:TargetStringAccumulator_str:{self.test_case} counter incremented to 2",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetStringAccumulator_str", 10) as case_loggy:
			self.test_case.TestBookmark.update("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetStringAccumulator_str:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42","42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_str:Handler counter incremented to 3", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetStringAccumulator_str", 10) as case_loggy:
			self.test_case.TestBookmark.Counter("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetStringAccumulator_str:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42","42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_str:Handler counter incremented to 4", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 4)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)




	def test_TargetStringAccumulator_Pattern(self):

		class TestVolume(LibraryVolume):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_HANDLER
				init_name	= "TargetStringAccumulator_Pattern"
				init_level	= 10

			class TestBookmark(VolumeBookmark):

				trigger = "place for trigger"
				@AccessHandlerCounter
				@AccessHandlerRegisterCounter
				class Counter(TargetStringAccumulator): rpattern = re.compile(r"(?P<target>42)")

		with self.assertLogs("TargetStringAccumulator_Pattern", 10) as case_loggy:

			self.test_case = TestVolume()
			self.test_case.TestBookmark.Counter("the answer is 42", self.test_case)

		self.assertIn(
			"DEBUG:TargetStringAccumulator_Pattern:Accepted pattern \"(?P<target>42)\"", case_loggy.output
		)
		self.assertIn("DEBUG:TargetStringAccumulator_Pattern:Recap extended to 1 item", case_loggy.output)
		self.assertIsInstance(self.test_case[self.test_case.TestBookmark.Counter], dict)
		self.assertIn("recap", self.test_case[self.test_case.TestBookmark.Counter])
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_Pattern:Handler counter incremented to 1", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 1)
		self.assertIn(

			f"DEBUG:TargetStringAccumulator_Pattern:{self.test_case} counter incremented to 1",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 1)


		with self.assertLogs("TargetStringAccumulator_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.update("the answer is 42", self.test_case)

		self.assertIn("DEBUG:TargetStringAccumulator_Pattern:Recap extended to 2 items", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42","42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_Pattern:Handler counter incremented to 2", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 2)
		self.assertIn(

			f"DEBUG:TargetStringAccumulator_Pattern:{self.test_case} counter incremented to 2",
			case_loggy.output
		)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetStringAccumulator_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.update("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetStringAccumulator_Pattern:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42","42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_Pattern:Handler counter incremented to 3", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 3)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)


		with self.assertLogs("TargetStringAccumulator_Pattern", 10) as case_loggy:
			self.test_case.TestBookmark.Counter("Better be 69", self.test_case)

		self.assertIn("DEBUG:TargetStringAccumulator_Pattern:No match for target", case_loggy.output)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter].get("recap"),[ "42","42" ])
		self.assertIn(
			"DEBUG:TargetStringAccumulator_Pattern:Handler counter incremented to 4", case_loggy.output
		)
		self.assertEqual(self.test_case.TestBookmark.Counter.access_handler_counter, 4)
		self.assertEqual(self.test_case[self.test_case.TestBookmark.Counter]["counter"], 2)








if __name__ == "__main__" : unittest.main(verbosity=2)







