import	os
import	unittest
from	pathlib								import Path
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.planting.twigs		import TwigProbe
from	pygwarts.hagrid.bloom.twigs			import Germination








class GerminationCase(EasySet):

	"""
		Custom thrive (raises FileNotFoundError) for Germination
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_8): os.remove(cls.EASY_HANDLER_8)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_8)
		class Sakura(Tree):

			bough = cls.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "germinations"
				handler		= cls.EASY_HANDLER_8
				init_level	= 10

			class folders(Germination):		pass
			class pseudothrive(TwigProbe):	pass
			class thrive(Transmutable):

				def __call__(self, origin :Tree, sprout :str, branch :Path, twig :Path, bough :Path):
					raise FileNotFoundError(
						f"[Errno 2] No such file or directory: \'{os.path.join(branch, twig)}\'"
					)

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
		cls.test_case = Sakura()




	def test_initiate_germinate(self):


		self.assertTrue(len(self.test_case) == 1)
		self.assertTrue(str(self.test_case[0]) == "Sakura.folders")
		self.assertTrue(isinstance(self.test_case[0], Germination))
		self.assertTrue(hasattr(self.test_case.folders, "blooming"))
		self.assertTrue(isinstance(self.test_case.folders.blooming, dict))
		self.assertEqual(len(self.test_case.folders.blooming),0)




	def test_j_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertIn(

			"WARNING:germinations:Failed to germinate twig "
			f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist')}\" due to "
			f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc1}\'",
			case_loggy.output
		)




	def test_k_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[
					Path(self.EASY_SET_SPROUT).joinpath("not.exist1"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist2"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist3")
				],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertIn(

			"WARNING:germinations:Failed to germinate twig "
			f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist1')}\" due to "
			f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc2}\'",
			case_loggy.output
		)
		self.assertIn(

			"WARNING:germinations:Failed to germinate twig "
			f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist2')}\" due to "
			f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc3}\'",
			case_loggy.output
		)
		self.assertIn(

			"WARNING:germinations:Failed to germinate twig "
			f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist3')}\" due to "
			f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc4}\'",
			case_loggy.output
		)




	def test_l_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertIn(

			f"DEBUG:germinations:Branch \"{self.EASY_SET_SPROUT}\" has no twigs to germinate",
			case_loggy.output
		)




	def test_m_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),1)
		self.assertIn("self.test_case", self.test_case.folders.blooming)
		self.assertNotIn("thrive", self.test_case.folders.blooming["self.test_case"])
		self.assertFalse(self.test_case.folders.blooming["self.test_case"]["bough"])
		self.assertIn(

			f"ERROR:germinations:Invalid tree self.test_case or no bough to germinate",
			case_loggy.output
		)




	def test_n_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ],
				[]
			)

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist1") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),1)
		self.assertIn("self.test_case", self.test_case.folders.blooming)
		self.assertNotIn("thrive", self.test_case.folders.blooming["self.test_case"])
		self.assertFalse(self.test_case.folders.blooming["self.test_case"]["bough"])
		self.assertIn(

			f"DEBUG:germinations:Invalid tree self.test_case or no bough to germinate",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"DEBUG:germinations:Invalid tree self.test_case or no bough to germinate"
			),2
		)




	def test_o_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist2") ],
				[]
			)

			self.assertFalse(self.test_case.folders.blooming["self.test_case"]["bough"])
			self.test_case.folders.blooming["self.test_case"]["bough"] = True
			self.assertTrue(self.test_case.folders.blooming["self.test_case"]["bough"])

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist3") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),1)
		self.assertIn("self.test_case", self.test_case.folders.blooming)
		self.assertNotIn("thrive", self.test_case.folders.blooming["self.test_case"])
		self.assertFalse(self.test_case.folders.blooming["self.test_case"]["bough"])
		self.assertIn(

			f"DEBUG:germinations:Invalid tree self.test_case or no bough to germinate",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"DEBUG:germinations:Invalid tree self.test_case or no bough to germinate"
			),1
		)
		self.assertIn(

			f"ERROR:germinations:Invalid tree self.test_case or no bough to germinate",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"ERROR:germinations:Invalid tree self.test_case or no bough to germinate"
			),1
		)




	def test_p_germinate(self):

		self.test_case.thrive = 42
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertFalse(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
		self.assertNotIn("bough", self.test_case.folders.blooming[str(self.test_case)])
		self.assertIn(f"ERROR:germinations:{self.test_case} doesn't implement thrive", case_loggy.output)




	def test_q_germinate(self):

		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ],
				[]
			)
			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist1") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertFalse(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
		self.assertNotIn("bough", self.test_case.folders.blooming[str(self.test_case)])
		self.assertIn(f"DEBUG:germinations:{self.test_case} doesn't implement thrive", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:germinations:{self.test_case} doesn't implement thrive"),2
		)




	def test_r_germinate(self):

		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist2") ],
				[]
			)

			self.assertFalse(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
			self.test_case.folders.blooming[str(self.test_case)]["thrive"] = True
			self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["thrive"])

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist3") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertFalse(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
		self.assertNotIn("bough", self.test_case.folders.blooming[str(self.test_case)])
		self.assertIn(f"DEBUG:germinations:{self.test_case} doesn't implement thrive", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:germinations:{self.test_case} doesn't implement thrive"),1
		)
		self.assertIn(f"ERROR:germinations:{self.test_case} doesn't implement thrive", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"ERROR:germinations:{self.test_case} doesn't implement thrive"),1
		)




	def test_s_germinate(self):

		self.test_case.thrive = self.test_case.pseudothrive
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
		self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["bough"])
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc1}\" not located", case_loggy.output)




	def test_t_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[
					Path(self.EASY_SET_SPROUT).joinpath("not.exist1"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist2"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist3")
				],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
		self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["bough"])
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc2}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc3}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc4}\" not located", case_loggy.output)




	def test_u_germinate(self):
		with self.assertLogs("germinations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")),
				[
					Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")).joinpath("not.exist1"),
					Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")).joinpath("not.exist2"),
					Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")).joinpath("not.exist3")
				],
				[]
			)

		self.assertEqual(len(self.test_case.folders.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.folders.blooming)
		self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["thrive"])
		self.assertTrue(self.test_case.folders.blooming[str(self.test_case)]["bough"])
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc6}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc7}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:germinations:Branch \"{self.notsrc8}\" not located", case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







