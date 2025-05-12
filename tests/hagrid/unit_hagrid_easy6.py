import	os
import	unittest
from	pathlib								import Path
from	shutil								import copyfile
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import EasySet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.planting.leafs		import LeafProbe
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation








class RejuvenationCase(EasySet):

	"""
		Custom grow (situative, must raise FileNotFoundError) for Rejuvenation
		Single sprout
		Single bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.EASY_HANDLER_6): os.remove(cls.EASY_HANDLER_6)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.EASY_HANDLER_6)
		class Sakura(Tree):

			bough = cls.EASY_SET_BOUGH
			class loggy(LibraryContrib):

				init_name	= "rejuvenations"
				handler		= cls.EASY_HANDLER_6
				init_level	= 10

			class files(Rejuvenation):		pass
			class pseudogrow(LeafProbe):	pass
			class grow(Transmutable):

				def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):
					copyfile(leaf, bough.joinpath(leaf.name))

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




	def test_initiate_rejuve(self):


		self.assertTrue(len(self.test_case) == 1)
		self.assertTrue(str(self.test_case[0]) == "Sakura.files")
		self.assertTrue(isinstance(self.test_case[0], Rejuvenation))
		self.assertTrue(hasattr(self.test_case.files, "blooming"))
		self.assertTrue(isinstance(self.test_case.files.blooming, dict))
		self.assertEqual(len(self.test_case.files.blooming),0)




	def test_j_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.files.blooming)
		self.assertIn(
			str(

				"WARNING:rejuvenations:Failed to rejuve leaf "
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist')}\" due to FileNotFoundError: "
				f"[Errno 2] No such file or directory: \'{self.notsrc1}\'"
			)	if os.name == "posix" else "%s%s%s'%s'"%(
				"WARNING:rejuvenations:Failed to rejuve leaf ",
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist')}\" due to FileNotFoundError: ",
				f"[Errno 2] No such file or directory: ",
				self.notsrc1.replace("\\", "\\\\")
			),
			case_loggy.output
		)




	def test_k_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[
					Path(self.EASY_SET_SPROUT).joinpath("not.exist1"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist2"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist3")
				]
			)

		self.assertEqual(len(self.test_case.files.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.files.blooming)
		self.assertIn(
			str(
				"WARNING:rejuvenations:Failed to rejuve leaf "
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist1')}\" due to "
				f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc2}\'"
			)	if os.name == "posix" else "%s%s%s'%s'"%(
				"WARNING:rejuvenations:Failed to rejuve leaf ",
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist1')}\" due to ",
				f"FileNotFoundError: [Errno 2] No such file or directory: ",
				self.notsrc2.replace("\\", "\\\\")
			),
			case_loggy.output
		)
		self.assertIn(
			str(
				"WARNING:rejuvenations:Failed to rejuve leaf "
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist2')}\" due to "
				f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc3}\'"
			)	if os.name == "posix" else "%s%s%s'%s'"%(
				"WARNING:rejuvenations:Failed to rejuve leaf ",
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist2')}\" due to ",
				f"FileNotFoundError: [Errno 2] No such file or directory: ",
				self.notsrc3.replace("\\", "\\\\")
			),
			case_loggy.output
		)
		self.assertIn(
			str(
				"WARNING:rejuvenations:Failed to rejuve leaf "
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist3')}\" due to "
				f"FileNotFoundError: [Errno 2] No such file or directory: \'{self.notsrc4}\'"
			)	if os.name == "posix" else "%s%s%s'%s'"%(
				"WARNING:rejuvenations:Failed to rejuve leaf ",
				f"\"{Path(self.EASY_SET_SPROUT).joinpath('not.exist3')}\" due to ",
				f"FileNotFoundError: [Errno 2] No such file or directory: ",
				self.notsrc4.replace("\\", "\\\\")
			),
			case_loggy.output
		)




	def test_l_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[]
			)

		self.assertEqual(len(self.test_case.files.blooming),0)
		self.assertNotIn(str(self.test_case), self.test_case.files.blooming)
		self.assertIn(

			f"DEBUG:rejuvenations:Branch \"{self.EASY_SET_SPROUT}\" has no leafs to rejuve",
			case_loggy.output
		)




	def test_m_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),1)
		self.assertIn("self.test_case", self.test_case.files.blooming)
		self.assertNotIn("grow", self.test_case.files.blooming["self.test_case"])
		self.assertFalse(self.test_case.files.blooming["self.test_case"]["bough"])
		self.assertIn(

			f"ERROR:rejuvenations:Invalid tree self.test_case or no bough to rejuve",
			case_loggy.output
		)




	def test_n_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[
					Path(self.EASY_SET_SPROUT).joinpath("not.exist")
				]
			)

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist1") ]
			)


		self.assertEqual(len(self.test_case.files.blooming),1)
		self.assertIn("self.test_case", self.test_case.files.blooming)
		self.assertNotIn("grow", self.test_case.files.blooming["self.test_case"])
		self.assertFalse(self.test_case.files.blooming["self.test_case"]["bough"])
		self.assertIn(

			f"DEBUG:rejuvenations:Invalid tree self.test_case or no bough to rejuve",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"DEBUG:rejuvenations:Invalid tree self.test_case or no bough to rejuve"
			),2
		)




	def test_o_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist2") ]
			)

			self.assertFalse(self.test_case.files.blooming["self.test_case"]["bough"])
			self.test_case.files.blooming["self.test_case"]["bough"] = True
			self.assertTrue(self.test_case.files.blooming["self.test_case"]["bough"])

			self.test_case[0](

				"self.test_case",
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist3") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),1)
		self.assertIn("self.test_case", self.test_case.files.blooming)
		self.assertNotIn("grow", self.test_case.files.blooming["self.test_case"])
		self.assertFalse(self.test_case.files.blooming["self.test_case"]["bough"])
		self.assertIn(

			f"DEBUG:rejuvenations:Invalid tree self.test_case or no bough to rejuve",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"DEBUG:rejuvenations:Invalid tree self.test_case or no bough to rejuve"
			),1
		)
		self.assertIn(

			f"ERROR:rejuvenations:Invalid tree self.test_case or no bough to rejuve",
			case_loggy.output
		)
		self.assertEqual(

			case_loggy.output.count(
				f"ERROR:rejuvenations:Invalid tree self.test_case or no bough to rejuve"
			),1
		)




	def test_p_rejuve(self):

		self.test_case.grow = 42
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.files.blooming)
		self.assertFalse(self.test_case.files.blooming[str(self.test_case)]["grow"])
		self.assertNotIn("bough", self.test_case.files.blooming[str(self.test_case)])
		self.assertIn(f"ERROR:rejuvenations:{self.test_case} doesn't implement grow", case_loggy.output)




	def test_q_rejuve(self):

		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ]
			)
			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist1") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.files.blooming)
		self.assertFalse(self.test_case.files.blooming[str(self.test_case)]["grow"])
		self.assertNotIn("bough", self.test_case.files.blooming[str(self.test_case)])
		self.assertIn(f"DEBUG:rejuvenations:{self.test_case} doesn't implement grow", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:rejuvenations:{self.test_case} doesn't implement grow"),2
		)




	def test_r_rejuve(self):

		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist2") ]
			)

			self.assertFalse(self.test_case.files.blooming[str(self.test_case)]["grow"])
			self.test_case.files.blooming[str(self.test_case)]["grow"] = True
			self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["grow"])

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist3") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.files.blooming)
		self.assertFalse(self.test_case.files.blooming[str(self.test_case)]["grow"])
		self.assertNotIn("bough", self.test_case.files.blooming[str(self.test_case)])
		self.assertIn(f"DEBUG:rejuvenations:{self.test_case} doesn't implement grow", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:rejuvenations:{self.test_case} doesn't implement grow"),1
		)
		self.assertIn(f"ERROR:rejuvenations:{self.test_case} doesn't implement grow", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"ERROR:rejuvenations:{self.test_case} doesn't implement grow"),1
		)




	def test_s_rejuve(self):

		self.test_case.grow = self.test_case.pseudogrow
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[ Path(self.EASY_SET_SPROUT).joinpath("not.exist") ]
			)

		self.assertEqual(len(self.test_case.files.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.files.blooming)
		self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["grow"])
		self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["bough"])
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc1}\" not located", case_loggy.output)




	def test_t_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(self.EASY_SET_SPROUT),
				[],
				[
					Path(self.EASY_SET_SPROUT).joinpath("not.exist1"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist2"),
					Path(self.EASY_SET_SPROUT).joinpath("not.exist3")
				]
			)

		self.assertEqual(len(self.test_case.files.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.files.blooming)
		self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["grow"])
		self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["bough"])
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc2}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc3}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc4}\" not located", case_loggy.output)




	def test_u_rejuve(self):
		with self.assertLogs("rejuvenations", 10) as case_loggy:

			self.test_case[0](

				self.test_case,
				self.EASY_SET_SPROUT,
				Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")),
				[],
				[
					Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")).joinpath("not.exist1"),
					Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")).joinpath("not.exist2"),
					Path(os.path.join(self.EASY_SET_SPROUT, "non-existant folder")).joinpath("not.exist3")
				]
			)

		self.assertEqual(len(self.test_case.files.blooming),2)
		self.assertIn(str(self.test_case), self.test_case.files.blooming)
		self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["grow"])
		self.assertTrue(self.test_case.files.blooming[str(self.test_case)]["bough"])
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc6}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc7}\" not located", case_loggy.output)
		self.assertIn(f"DEBUG:rejuvenations:Branch \"{self.notsrc8}\" not located", case_loggy.output)








if __name__ == "__main__" : unittest.main(verbosity=2)







