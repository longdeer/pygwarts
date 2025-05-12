import	os
import	unittest
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.irma					import IrmaTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access				import LibraryAccess
from	pygwarts.irma.access.bookmarks		import VolumeBookmark
from	pygwarts.irma.access.volume			import LibraryVolume
from	pygwarts.irma.access.annex			import VolumeAnnex
from	pygwarts.irma.access.annex			import LibraryAnnex








class AccessAnnexCases(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.ACCESS_ANNEX): os.remove(cls.ACCESS_ANNEX)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.ACCESS_ANNEX)
	def test_volume_no_upper_init(self):

		class LonelyVolumeAnnex(VolumeAnnex):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "volume_no_upper_init"
				init_level	= 10

		with self.assertLogs("volume_no_upper_init", 10) as case_loggy:

			self.test_case = LonelyVolumeAnnex()
			self.test_case([])

		self.assertIn("DEBUG:volume_no_upper_init:Library not found", case_loggy.output)




	def test_volume_annex(self):
		class LonelyVolume(LibraryVolume):

			class B1(VolumeBookmark):	trigger = "trigger1"
			class B2(VolumeBookmark):	trigger = "trigger2"
			class B3(VolumeBookmark):	trigger = "trigger3"
			class B4(VolumeBookmark):	trigger = "trigger4"
			class B5(VolumeBookmark):	trigger = "trigger5"
			class Annex(VolumeAnnex):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "volume_annex"
				init_level	= 10

		self.test_case = LonelyVolume()
		self.test_case.B1(lambda _ : "OOH EEH\n", "inducer")
		self.test_case.B2(lambda _ : "OOH AH AH\n", "inducer")
		self.test_case.B3(lambda _ : "TING TANG\n", "inducer")
		self.test_case.B4(lambda _ : "WALLA WALLA BING BANG\n", "inducer")
		self.test_case.B5(lambda _ : "", "inducer")

		with self.assertLogs("volume_annex", 10) as case_loggy:
			self.assertEqual(

				self.test_case.Annex(self.test_case.keysof("bookmark")),
				"OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG\n"
			)

		self.assertIn(f"INFO:volume_annex:Fetching volume {self.test_case} annex", case_loggy.output)
		self.assertIn(f"DEBUG:volume_annex:{self.test_case.B1} bookmark view 8 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:volume_annex:{self.test_case.B2} bookmark view 10 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:volume_annex:{self.test_case.B3} bookmark view 10 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:volume_annex:{self.test_case.B4} bookmark view 22 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:volume_annex:Volume {self.test_case} annex 50 symbols", case_loggy.output)




	def test_volume_empty_annex(self):
		class LonelyVolume(LibraryVolume):

			class B1(VolumeBookmark):	trigger = "trigger1"
			class B2(VolumeBookmark):	trigger = "trigger2"
			class B3(VolumeBookmark):	trigger = "trigger3"
			class B4(VolumeBookmark):	trigger = "trigger4"
			class B5(VolumeBookmark):	trigger = "trigger5"
			class Annex(VolumeAnnex):	pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "volume_empty_annex"
				init_level	= 10

		inducer1 = lambda _ : 42
		inducer2 = lambda _ : ...
		self.test_case = LonelyVolume()
		self.test_case.B1("OOH EEH", "inducer")
		self.test_case.B2(True, "inducer")
		self.test_case.B3(inducer1, "inducer")
		self.test_case.B4(inducer2, "inducer")
		self.test_case.B5(lambda _ : "", "inducer")

		with self.assertLogs("volume_empty_annex", 10) as case_loggy:
			self.assertIsNone(self.test_case.Annex(self.test_case.keysof("bookmark")))

		self.assertIn(f"INFO:volume_empty_annex:Fetching volume {self.test_case} annex", case_loggy.output)
		self.assertIn(

			"DEBUG:volume_empty_annex:OOH EEH failed due to TypeError: 'str' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:volume_empty_annex:True failed due to TypeError: 'bool' object is not callable",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_empty_annex:{inducer1} failed due to TypeError: "
			"can only concatenate str (not \"int\") to str",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_empty_annex:{inducer2} failed due to TypeError: "
			"can only concatenate str (not \"ellipsis\") to str",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:volume_empty_annex:No view volume {self.test_case}", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:volume_empty_annex:No view volume {self.test_case}"),5
		)
		self.assertIn(f"DEBUG:volume_empty_annex:Volume {self.test_case} annex 0 symbols", case_loggy.output)




	def test_volume_not_viewable_annex(self):
		class LonelyVolume(LibraryVolume):

			class Annex(VolumeAnnex):	pass
			class B1(VolumeBookmark):	trigger = "trigger1"
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "volume_not_viewable_annex"
				init_level	= 10

		self.test_case = LonelyVolume()

		with self.assertLogs("volume_not_viewable_annex", 10) as case_loggy:
			for unviewable in (

				"view", 42, .69, True, False, None, ...,
				[ "view" ],( "view", ),{ "view" },{ "view": "view" }
			):
				with self.subTest(view=unviewable):

					setattr(self.test_case.B1, "view", unviewable)
					self.assertIsNone(self.test_case.Annex(self.test_case.keysof("bookmark")))

			del self.test_case[self.test_case.B1]
			self.test_case.loggy.warning("PART II")

			for nobookmark in "view", 42, .69, True, False, None, ...,( "view", ):
				self.test_case(nobookmark, "bookmark")
			self.assertIsNone(self.test_case.Annex(self.test_case.keysof("bookmark")))

		self.assertIn(
			f"INFO:volume_not_viewable_annex:Fetching volume {self.test_case} annex", case_loggy.output
		)
		self.assertIn(
			f"DEBUG:volume_not_viewable_annex:{self.test_case.B1} is not viewable", case_loggy.output
		)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark view", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark 42", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark 0.69", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark True", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark False", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark None", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark Ellipsis", case_loggy.output)
		self.assertIn(f"DEBUG:volume_not_viewable_annex:Invalid bookmark ('view',)", case_loggy.output)
		self.assertIn(
			f"DEBUG:volume_not_viewable_annex:Volume {self.test_case} annex 0 symbols", case_loggy.output
		)
		self.assertEqual(
			case_loggy.output.count(
				f"INFO:volume_not_viewable_annex:Fetching volume {self.test_case} annex"
			),	12
		)
		self.assertEqual(
			case_loggy.output.count(
				f"DEBUG:volume_not_viewable_annex:{self.test_case.B1} is not viewable"
			),	11
		)
		self.assertEqual(
			case_loggy.output.count(
				f"DEBUG:volume_not_viewable_annex:Volume {self.test_case} annex 0 symbols"
			),	12
		)




	def test_volume_not_string_views_annex(self):
		class LonelyVolume(LibraryVolume):

			class Annex(VolumeAnnex):	pass
			class B1(VolumeBookmark):

				trigger = "trigger1"
				def view(self, volume :LibraryVolume): return 42

			class B2(VolumeBookmark):

				trigger = "trigger2"
				def view(self, volume :LibraryVolume): return .69

			class B3(VolumeBookmark):

				trigger = "trigger3"
				def view(self, volume :LibraryVolume): return True

			class B4(VolumeBookmark):

				trigger = "trigger4"
				def view(self, volume :LibraryVolume): return False

			class B5(VolumeBookmark):

				trigger = "trigger5"
				def view(self, volume :LibraryVolume): return ...

			class B6(VolumeBookmark):

				trigger = "trigger6"
				def view(self, volume :LibraryVolume): return print

			class B7(VolumeBookmark):

				trigger = "trigger7"
				def view(self, volume :LibraryVolume): return Transmutable

			class B8(VolumeBookmark):

				trigger = "trigger8"
				def view(self, volume :LibraryVolume): return ( "view", )

			class B9(VolumeBookmark):

				trigger = "trigger9"
				def view(self, volume :LibraryVolume): return [ "view" ]

			class B10(VolumeBookmark):

				trigger = "trigger10"
				def view(self, volume :LibraryVolume): return { "view" }

			class B11(VolumeBookmark):

				trigger = "trigger11"
				def view(self, volume :LibraryVolume): return { "view": "view" }

			class B12(VolumeBookmark):

				trigger = "trigger12"
				def view(self, volume :LibraryVolume): return None

			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "volume_not_string_views_annex"
				init_level	= 10

		self.test_case = LonelyVolume()

		with self.assertLogs("volume_not_string_views_annex", 10) as case_loggy:
			self.assertIsNone(self.test_case.Annex(self.test_case.keysof("bookmark")))

		self.assertIn(

			f"INFO:volume_not_string_views_annex:Fetching volume {self.test_case} annex",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B1} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B2} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B3} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B4} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B5} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B6} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B7} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B8} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B9} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B10} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B11} view is not a string",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:{self.test_case.B12} view is None",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:volume_not_string_views_annex:Volume {self.test_case} annex 0 symbols",
			case_loggy.output
		)
















	def test_library_no_upper_init(self):

		class LonelyLibraryAnnex(LibraryAnnex):
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "library_no_upper_init"
				init_level	= 10

		with self.assertLogs("library_no_upper_init", 10) as case_loggy:

			self.test_case = LonelyLibraryAnnex()
			self.test_case()

		self.assertIn("DEBUG:library_no_upper_init:Library not found", case_loggy.output)




	def test_library_direct_annex(self):
		class LonelyLibrary(LibraryAccess):

			class LibAnnex(LibraryAnnex): pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "library_annex"
				init_level	= 10

			class V1(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger1"
				class B2(VolumeBookmark): trigger = "trigger2"
				class Annex(VolumeAnnex): pass
				inrange = r".+"

			class V2(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger3"
				class B2(VolumeBookmark): trigger = "trigger4"
				class Annex(VolumeAnnex): pass
				inrange = r".+"

			class V3(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger6"
				class B2(VolumeBookmark): trigger = "trigger7"
				class Annex(VolumeAnnex): pass
				inrange = r".+"

			class V4(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger8"
				class B2(VolumeBookmark): trigger = "trigger9"
				class Annex(VolumeAnnex): pass
				inrange = r".+"

			class V5(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger10"
				class B2(VolumeBookmark): trigger = "trigger11"
				class Annex(VolumeAnnex): pass
				inrange = r".+"


		self.test_case = LonelyLibrary()
		self.test_case.V1.B1(lambda _ : "OOH ", "inducer")
		self.test_case.V1.B2(lambda _ : "EEH\n", "inducer")
		self.test_case.V2.B1(lambda _ : "OOH ", "inducer")
		self.test_case.V2.B1(lambda _ : "AH ", "inducer")
		self.test_case.V2.B2(lambda _ : "AH\n", "inducer")
		self.test_case.V3.B1(lambda _ : "TING ", "inducer")
		self.test_case.V3.B2(lambda _ : "TANG\n", "inducer")
		self.test_case.V4.B1(lambda _ : "WALLA ", "inducer")
		self.test_case.V4.B2(lambda _ : "WALLA ", "inducer")
		self.test_case.V5.B1(lambda _ : "BING ", "inducer")
		self.test_case.V5.B2(lambda _ : "BANG", "inducer")

		# Imitating volume polution by handlers
		self.test_case.V1("some handler gets", 42)
		self.test_case.V2("some handler gets", 42)
		self.test_case.V3("some handler gets", 42)
		self.test_case.V4("some handler gets", 42)
		self.test_case.V5("some handler gets", 42)


		self.assertEqual(self.test_case.LibAnnex(), "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA BING BANG")








	def test_library_direct_annex_no_range(self):
		class LonelyLibrary(LibraryAccess):

			class LibAnnex(LibraryAnnex): pass
			class loggy(LibraryContrib):

				handler		= self.ACCESS_ANNEX
				init_name	= "library_annex_no_range"
				init_level	= 10

			class V1(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger1"
				class B2(VolumeBookmark): trigger = "trigger2"
				class Annex(VolumeAnnex): pass

			class V2(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger3"
				class B2(VolumeBookmark): trigger = "trigger4"
				class Annex(VolumeAnnex): pass

			class V3(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger6"
				class B2(VolumeBookmark): trigger = "trigger7"
				class Annex(VolumeAnnex): pass

			class V4(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger8"
				class B2(VolumeBookmark): trigger = "trigger9"
				class Annex(VolumeAnnex): pass

			class V5(LibraryVolume):

				class B1(VolumeBookmark): trigger = "trigger10"
				class B2(VolumeBookmark): trigger = "trigger11"
				class Annex(VolumeAnnex): pass


		self.test_case = LonelyLibrary()
		self.test_case.V1.B1(lambda _ : "OOH ", "inducer")
		self.test_case.V1.B2(lambda _ : "EEH\n", "inducer")
		self.test_case.V2.B1(lambda _ : "OOH ", "inducer")
		self.test_case.V2.B1(lambda _ : "AH ", "inducer")
		self.test_case.V2.B2(lambda _ : "AH\n", "inducer")
		self.test_case.V3.B1(lambda _ : "TING ", "inducer")
		self.test_case.V3.B2(lambda _ : "TANG\n", "inducer")
		self.test_case.V4.B1(lambda _ : "WALLA ", "inducer")
		self.test_case.V4.B2(lambda _ : "WALLA ", "inducer")
		self.test_case.V5.B1(lambda _ : "BING ", "inducer")
		self.test_case.V5.B2(lambda _ : "BANG", "inducer")


		with self.assertLogs("library_annex_no_range", 10) as case_loggy:
			self.assertIsNone(self.test_case.LibAnnex())

		self.assertIn(

			f"DEBUG:library_annex_no_range:Fetching library {self.test_case} annex",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:library_annex_no_range:Valid {self.test_case.V1} range not provided",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:library_annex_no_range:Valid {self.test_case.V2} range not provided",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:library_annex_no_range:Valid {self.test_case.V3} range not provided",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:library_annex_no_range:Valid {self.test_case.V4} range not provided",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:library_annex_no_range:Valid {self.test_case.V5} range not provided",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:library_annex_no_range:Library {self.test_case} annex 0 symbols",
			case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







