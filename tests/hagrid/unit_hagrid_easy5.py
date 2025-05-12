import	os
import	unittest
from	pathlib								import Path
from	shutil								import rmtree
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.weeds		import TrimProbe
from	pygwarts.hagrid.planting.weeds		import SprigTrimmer
from	pygwarts.hagrid.bloom.weeds			import Efflorescence
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class EfflorescenceCase(EasySet):

	"""
		Flourishing and direct Efflorescence
		Single sprout
		Single bough
		Testing different variants
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_5): os.remove(cls.EASY_HANDLER_5)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_5)

		cls.fading1 = os.path.join(cls.EASY_SET_BOUGH, "fading1")
		cls.fading2 = os.path.join(cls.EASY_SET_BOUGH, "fading2")

		cls.notdst1 = os.path.join(cls.EASY_SET_BOUGH, "not.exist")
		cls.notdst2 = os.path.join(cls.EASY_SET_BOUGH, "not.exist1")
		cls.notdst3 = os.path.join(cls.EASY_SET_BOUGH, "not.exist2")
		cls.notdst4 = os.path.join(cls.EASY_SET_BOUGH, "not.exist3")
		cls.notsrc1 = os.path.join(cls.EASY_SET_SPROUT, "not.exist")
		cls.notsrc2 = os.path.join(cls.EASY_SET_SPROUT, "not.exist1")
		cls.notsrc3 = os.path.join(cls.EASY_SET_SPROUT, "not.exist2")
		cls.notsrc4 = os.path.join(cls.EASY_SET_SPROUT, "not.exist3")
		cls.notsrc5 = os.path.join(cls.EASY_SET_SPROUT, "non-existant folder")
		cls.notsrc6 = os.path.join(cls.notsrc5, "not.exist1")
		cls.notsrc7 = os.path.join(cls.notsrc5, "not.exist2")
		cls.notsrc8 = os.path.join(cls.notsrc5, "not.exist3")

		class Sakura(Tree):

			bough = cls.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				handler		= cls.EASY_HANDLER_5
				init_level	= 10

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	pass

		cls.sakura = Sakura


	def setUp(self):

		if	not os.path.isfile(self.fading1) : self.fmake(self.fading1, "this file must fade away")
		os.makedirs(self.fading2, exist_ok=True)




	def test_nobranches(self):

		self.sakura.loggy.init_name = "effloresce_nobranches"
		with self.assertLogs("effloresce_nobranches", 10) as case_loggy:

			self.test_case = self.sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.clean.blooming),0)
		self.assertNotIn("self.test_case", self.test_case.clean.blooming)
		self.assertNotIn(str(self.test_case), self.test_case.clean.blooming)
		self.assertIn(

			"DEBUG:effloresce_nobranches:Branches not found or sprout is not a string",
			case_loggy.output
		)








	def test_nosprout(self):

		self.sakura.loggy.init_name = "effloresce_nosprout"
		with self.assertLogs("effloresce_nosprout", 10) as case_loggy:

			self.test_case = self.sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case[0](

				self.test_case,
				self,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.clean.blooming),0)
		self.assertNotIn("self.test_case", self.test_case.clean.blooming)
		self.assertNotIn(str(self), self.test_case.clean.blooming)
		self.assertIn(

			"DEBUG:effloresce_nosprout:Branches not found or sprout is not a string",
			case_loggy.output
		)








	def test_nobough_1(self):

		self.sakura.loggy.init_name = "effloresce_nobough_1"
		with self.assertLogs("effloresce_nobough_1", 10) as case_loggy:

			self.test_case = self.sakura()
			self.test_case.branches = dict()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.clean.blooming),1)
		self.assertIn("self.test_case", self.test_case.clean.blooming)
		self.assertNotIn("trim", self.test_case.clean.blooming["self.test_case"])
		self.assertFalse(self.test_case.clean.blooming["self.test_case"]["bough"])
		self.assertIn(

			"ERROR:effloresce_nobough_1:Invalid tree self.test_case or no bough to effloresce",
			case_loggy.output
		)








	def test_nobough_2(self):

		self.sakura.loggy.init_name = "effloresce_nobough_2"
		with self.assertLogs("effloresce_nobough_2", 10) as case_loggy:

			self.test_case = self.sakura()
			self.test_case.branches = dict()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)
			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)
			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

			self.assertFalse(self.test_case.clean.blooming["self.test_case"]["bough"])
			self.test_case.clean.blooming["self.test_case"]["bough"] = True
			self.assertTrue(self.test_case.clean.blooming["self.test_case"]["bough"])

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.clean.blooming),1)
		self.assertIn("self.test_case", self.test_case.clean.blooming)
		self.assertNotIn("trim", self.test_case.clean.blooming["self.test_case"])
		self.assertFalse(self.test_case.clean.blooming["self.test_case"]["bough"])
		self.assertIn(

			"ERROR:effloresce_nobough_2:Invalid tree self.test_case or no bough to effloresce",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:effloresce_nobough_2:Invalid tree self.test_case or no bough to effloresce",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				"ERROR:effloresce_nobough_2:Invalid tree self.test_case or no bough to effloresce"
			), 2
		)
		self.assertEqual(

			case_loggy.output.count(
				"DEBUG:effloresce_nobough_2:Invalid tree self.test_case or no bough to effloresce"
			), 2
		)








	def test_notrim_1(self):

		self.sakura.loggy.init_name = "effloresce_notrim_1"
		with self.assertLogs("effloresce_notrim_1", 10) as case_loggy:

			self.test_case = self.sakura()
			self.test_case.branches = dict()
			self.test_case.trim = 42

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.clean.blooming),1)
		self.assertIn(str(self.test_case), self.test_case.clean.blooming)
		self.assertNotIn("bough", self.test_case.clean.blooming[str(self.test_case)])
		self.assertFalse(self.test_case.clean.blooming[str(self.test_case)]["trim"])
		self.assertIn(

			f"ERROR:effloresce_notrim_1:{self.test_case} doesn't implement trim",
			case_loggy.output
		)








	def test_notrim_2(self):

		self.sakura.loggy.init_name = "effloresce_notrim_2"
		with self.assertLogs("effloresce_notrim_2", 10) as case_loggy:

			self.test_case = self.sakura()
			self.test_case.branches = dict()
			self.test_case.trim = 42

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)
			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)
			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

			self.assertFalse(self.test_case.clean.blooming[str(self.test_case)]["trim"])
			self.test_case.clean.blooming[str(self.test_case)]["trim"] = True
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["trim"])

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.clean.blooming),1)
		self.assertIn(str(self.test_case), self.test_case.clean.blooming)
		self.assertNotIn("bough", self.test_case.clean.blooming[str(self.test_case)])
		self.assertFalse(self.test_case.clean.blooming[str(self.test_case)]["trim"])
		self.assertIn(

			f"ERROR:effloresce_notrim_2:{self.test_case} doesn't implement trim",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:effloresce_notrim_2:{self.test_case} doesn't implement trim",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"ERROR:effloresce_notrim_2:{self.test_case} doesn't implement trim"
			),2
		)
		self.assertEqual(

			case_loggy.output.count(
				f"DEBUG:effloresce_notrim_2:{self.test_case} doesn't implement trim"
			),2
		)








	def test_nocontrollers_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "nocontrollers_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("nocontrollers_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:nocontrollers_flourish:Controller for twigs not found",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nocontrollers_flourish:Controller for leafs not found",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nocontrollers_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nocontrollers_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nocontrollers_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nocontrollers_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_branches_1_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "branches_1_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = dict()

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("branches_1_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:branches_1_flourish:Bough \"{self.EASY_SET_BOUGH}\" not included for Efflorescence",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_1_flourish:Sprout \"{self.EASY_SET_SPROUT}\" not included for Efflorescence",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_1_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_1_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_1_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_1_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_branches_2_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "branches_2_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: tuple() }

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("branches_2_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:branches_2_flourish:Sprout \"{self.EASY_SET_SPROUT}\" not included for Efflorescence",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_2_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_2_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_2_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_2_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_branches_3_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "branches_3_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: list() }

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("branches_3_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:branches_3_flourish:Invalid sprouts mapping for \"{self.EASY_SET_BOUGH}\"",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_3_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_3_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_3_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:branches_3_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_branches_4_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "branches_4_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_SPROUT }

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("branches_4_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.clean.includable(self.EASY_SET_BOUGH)

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:branches_4_flourish:No branches included for Efflorescence",
			case_loggy.output
		)








	def test_wrong_include_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "wrong_include_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			# Looks like controller do have include field, but it's wrong types
			class leafs(SiftingController):

				include = (

					( rf"{self.EASY_SET_BOUGH}/.+" )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+" )
				)
			class twigs(SiftingController):

				include = (

					( rf"{self.EASY_SET_BOUGH}/.+" )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+" )
				)
			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}



			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("wrong_include_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.assertIn(

			"WARNING:wrong_include_flourish:"
			f"{self.test_case.twigs} include field improper, must be not empty list or tuple",
			case_loggy.output
		)
		self.assertIn(

			"WARNING:wrong_include_flourish:"
			f"{self.test_case.leafs} include field improper, must be not empty list or tuple",
			case_loggy.output
		)
		self.assertIn(
			"DEBUG:wrong_include_flourish:Include field for twigs not found", case_loggy.output
		)
		self.assertIn(
			"DEBUG:wrong_include_flourish:Include field for leafs not found", case_loggy.output
		)
		self.assertIn(
			f"DEBUG:wrong_include_flourish:Bough \"{self.dst_pros_folder}\" not thrived", case_loggy.output
		)
		self.assertIn(
			f"DEBUG:wrong_include_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived", case_loggy.output
		)
		self.assertIn(
			f"DEBUG:wrong_include_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived", case_loggy.output
		)
		self.assertIn(
			f"DEBUG:wrong_include_flourish:Bough \"{self.dst_cons_folder}\" not thrived", case_loggy.output
		)








	def test_probe_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "probe_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			# This is the example of a rule exception. The sifting basically designed to decalre
			# "twigs" and "leafs" separately under dispatcher (Flourish) object (main sifting)
			# and for every tree/copse somewhere else as many as need. But this situation is classic
			# cause it is single Tree that need effloresce, so for this to be done, the Tree object
			# must have controllers by itself, it wont be able to reach controllers under the Flourish.
			# So they are declared under the Tree. If Floursih will happen to have itself controllers,
			# main sifting will proceed with it. But in this situation, when there is no need in
			# main sifting, it will happen anyway, cause Flourish has access to the Tree's controllers.
			# So actually, includables for Efflorescence will not affect main sifting, just will take
			# some time, but the idea is the ability to put main siftables to the Tree.
			class leafs(SiftingController):
				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)
			class twigs(SiftingController):
				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)
			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("probe_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),1)
			self.assertIn(str(self.test_case), self.test_case.clean.blooming)
			self.assertIn("trim", self.test_case.clean.blooming[str(self.test_case)])
			self.assertIn("bough", self.test_case.clean.blooming[str(self.test_case)])
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["trim"])
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["bough"])


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		self.assertTrue(os.path.isfile(self.fading1))
		self.assertTrue(os.path.isdir(self.fading2))


		self.assertIn(f"INFO:probe_flourish:Leaf \"{self.fading1}\" trim probe", case_loggy.output)
		self.assertIn(f"INFO:probe_flourish:Twig \"{self.fading2}\" trim probe", case_loggy.output)
		self.assertNotIn(
			f"DEBUG:probe_flourish:Bough \"{self.dst_pros_folder}\" not thrived", case_loggy.output
		)
		self.assertNotIn(
			f"DEBUG:probe_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived", case_loggy.output
		)
		self.assertNotIn(
			f"DEBUG:probe_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived", case_loggy.output
		)
		self.assertNotIn(
			f"DEBUG:probe_flourish:Bough \"{self.dst_cons_folder}\" not thrived", case_loggy.output
		)








	def test_probe_no_thrive_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "probe_not_thrive_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class leafs(SiftingController):
				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)
			class twigs(SiftingController):
				include = (

					( rf"({self.EASY_SET_BOUGH}|{self.EASY_SET_SPROUT})/.+", )
					if os.name == "posix" else
					(
						r"(%s|%s)\\.+"%(

							self.EASY_SET_BOUGH.replace("\\", "\\\\"),
							self.EASY_SET_SPROUT.replace("\\", "\\\\")
						),
					)
				)

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("probe_not_thrive_flourish", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),1)
			self.assertIn(str(self.test_case), self.test_case.clean.blooming)
			self.assertIn("trim", self.test_case.clean.blooming[str(self.test_case)])
			self.assertIn("bough", self.test_case.clean.blooming[str(self.test_case)])
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["trim"])
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["bough"])


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		self.assertTrue(os.path.isfile(self.fading1))
		self.assertTrue(os.path.isdir(self.fading2))


		self.assertIn(f"INFO:probe_not_thrive_flourish:Leaf \"{self.fading1}\" trim probe", case_loggy.output)
		self.assertIn(f"INFO:probe_not_thrive_flourish:Twig \"{self.fading2}\" trim probe", case_loggy.output)
		self.assertIn(

			f"DEBUG:probe_not_thrive_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:probe_not_thrive_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:probe_not_thrive_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:probe_not_thrive_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_bad_probe(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "bad_probe_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class leafs(SiftingController):

				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)
			class twigs(SiftingController):


				include = (

					( rf"({self.EASY_SET_BOUGH}|{self.EASY_SET_SPROUT})/.+", )
					if os.name == "posix" else
					(
						r"(%s|%s)\\.+"%(

							self.EASY_SET_BOUGH.replace("\\", "\\\\"),
							self.EASY_SET_SPROUT.replace("\\", "\\\\")
						),
					)
				)

			class trim(TrimProbe):		pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("bad_probe_flourish", 10) as case_loggy:

			self.test_case = Sakura()

			self.assertTrue(len(self.test_case) == 1)
			self.assertTrue(str(self.test_case[0]) == "Sakura.clean")
			self.assertTrue(isinstance(self.test_case[0], Efflorescence))
			self.assertTrue(hasattr(self.test_case.clean, "blooming"))
			self.assertTrue(isinstance(self.test_case.clean.blooming, dict))
			self.assertEqual(len(self.test_case.clean.blooming),0)

			self.test_case.trim(

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				Path(self.EASY_SET_SPROUT).joinpath("non-existiest file"),
				Path(self.EASY_SET_BOUGH)
			)


		self.assertEqual(len(self.test_case.clean.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.clean.blooming)
		self.assertIn(

			"WARNING:bad_probe_flourish:Bad sprig "
			f"\"{os.path.join(self.EASY_SET_SPROUT, 'non-existiest file')}\""
			" to probe",
			case_loggy.output
		)








	def test_trim_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "trim_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class leafs(SiftingController):

				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)

			class twigs(SiftingController):

				include = (

					( rf"({self.EASY_SET_BOUGH}|{self.EASY_SET_SPROUT})/.+", )
					if os.name == "posix" else
					(
						r"(%s|%s)\\.+"%(

							self.EASY_SET_BOUGH.replace("\\", "\\\\"),
							self.EASY_SET_SPROUT.replace("\\", "\\\\")
						),
					)
				)

			class trim(SprigTrimmer):	pass
			class clean(Efflorescence):	branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		self.assertTrue(os.path.isfile(self.fading1))
		self.assertTrue(os.path.isdir(self.fading2))


		with self.assertLogs("trim_flourish", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),1)
			self.assertIn(str(self.test_case), self.test_case.clean.blooming)
			self.assertIn("trim", self.test_case.clean.blooming[str(self.test_case)])
			self.assertIn("bough", self.test_case.clean.blooming[str(self.test_case)])
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["trim"])
			self.assertTrue(self.test_case.clean.blooming[str(self.test_case)]["bough"])


		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		self.assertFalse(os.path.isfile(self.fading1))
		self.assertFalse(os.path.isdir(self.fading2))


		self.assertIn(f"INFO:trim_flourish:Trimmed leaf \"{self.fading1}\"", case_loggy.output)
		self.assertIn(f"INFO:trim_flourish:Trimmed twig \"{self.fading2}\"", case_loggy.output)
		self.assertIn(

			f"DEBUG:trim_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:trim_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:trim_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:trim_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_raise_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "raise_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class leafs(SiftingController):

				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)
			class twigs(SiftingController):

				include = (

					( rf"({self.EASY_SET_BOUGH}|{self.EASY_SET_SPROUT})/.+", )
					if os.name == "posix" else
					(
						r"(%s|%s)\\.+"%(

							self.EASY_SET_BOUGH.replace("\\", "\\\\"),
							self.EASY_SET_SPROUT.replace("\\", "\\\\")
						),
					)
				)

			class trim(Transmutable):
				def __call__(self, origin :Tree, sprout :str, branch :Path, sprig :str, bough :Path):

					target_branch = bough.joinpath(sprig)
					raise	PermissionError(f"Failed with \"{target_branch}\"")

			class clean(Efflorescence): branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		with self.assertLogs("raise_flourish", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync()

			self.assertEqual(len(self.test_case.clean.blooming),0)


		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		self.assertTrue(os.path.isfile(self.fading1))
		self.assertTrue(os.path.isdir(self.fading2))


		self.assertNotIn(f"INFO:raise_flourish:Trimmed leaf \"{self.fading1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:raise_flourish:Trimmed twig \"{self.fading2}\"", case_loggy.output)
		self.assertIn(

			"WARNING:raise_flourish:Failed to effloresce "
			f"\"{self.fading1}\" due to PermissionError: "
			f"Failed with \"{self.fading1}\"",
			case_loggy.output
		)
		self.assertIn(

			"WARNING:raise_flourish:Failed to effloresce "
			f"\"{self.fading2}\" due to PermissionError: "
			f"Failed with \"{self.fading2}\"",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:raise_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:raise_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:raise_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:raise_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








	def test_nosprigs_flourish(self):
		class Sakura(Tree):

			bough = self.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "nosprigs_flourish"
				handler		= self.EASY_HANDLER_5
				init_level	= 10

			class leafs(SiftingController):

				include = (

					( rf"{self.EASY_SET_BOUGH}/.+", )
					if os.name == "posix" else
					( self.EASY_SET_BOUGH.replace("\\", "\\\\") + r"\\.+", )
				)

			class twigs(SiftingController):

				include = (

					( rf"({self.EASY_SET_BOUGH}|{self.EASY_SET_SPROUT})/.+", )
					if os.name == "posix" else
					(
						r"(%s|%s)\\.+"%(

							self.EASY_SET_BOUGH.replace("\\", "\\\\"),
							self.EASY_SET_SPROUT.replace("\\", "\\\\")
						),
					)
				)

			class trim(SprigTrimmer):	pass
			class clean(Efflorescence): branches = { self.EASY_SET_BOUGH: ( self.EASY_SET_SPROUT, )}

			@fssprout(self.EASY_SET_SPROUT)
			class sync(Flourish):		pass


		if	os.path.isfile(self.fading1): os.remove(self.fading1)
		if	os.path.isdir(self.fading2)	: rmtree(self.fading2)

		with self.assertLogs("nosprigs_flourish", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.sync()

		self.assertEqual(len(self.test_case.clean.blooming),0)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertTrue(os.path.isdir(self.EASY_SET_BOUGH))
		self.assertFalse(os.path.isfile(self.fading1))
		self.assertFalse(os.path.isdir(self.fading2))


		self.assertNotIn(f"INFO:nosprigs_flourish:Trimmed leaf \"{self.fading1}\"", case_loggy.output)
		self.assertNotIn(f"INFO:nosprigs_flourish:Trimmed twig \"{self.fading2}\"", case_loggy.output)
		self.assertIn(
			f"DEBUG:nosprigs_flourish:No sprigs to effloresce \"{self.EASY_SET_BOUGH}\"", case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nosprigs_flourish:Bough \"{self.dst_pros_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nosprigs_flourish:Bough \"{self.dst_redundant_1_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nosprigs_flourish:Bough \"{self.dst_redundant_2_folder}\" not thrived",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:nosprigs_flourish:Bough \"{self.dst_cons_folder}\" not thrived",
			case_loggy.output
		)








if __name__ == "__main__" : unittest.main(verbosity=2)







