import	os
import	unittest
from	pathlib								import Path
from	shutil								import rmtree
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import HagridTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peels		import ThrivingPeel








class PeelCases(HagridTestCase):

	"""
		Try out peels variants
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.PEEL_HANDLER): os.remove(cls.PEEL_HANDLER)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.PEEL_HANDLER)

		cls.peel_2_2 = os.path.join("not so deep", "almost deep")
		cls.peel_2_3 = os.path.join(cls.peel_2_2, "the deep", "very deep", "oh my deep")

		cls.d2peel_1 = os.path.join(cls.INIT_SET_SPROUT, "d2peel_1")
		cls.d2peel_2 = os.path.join(cls.INIT_SET_SPROUT, cls.peel_2_2, "d2peel_2")
		cls.d2peel_3 = os.path.join(cls.INIT_SET_SPROUT, cls.peel_2_3, "d2peel_3")
		cls.f2peel_1 = os.path.join(cls.INIT_SET_SPROUT, "f2peel_1")
		cls.f2peel_2 = os.path.join(cls.INIT_SET_SPROUT, cls.peel_2_2, "f2peel_2")
		cls.f2peel_3 = os.path.join(cls.INIT_SET_SPROUT, cls.peel_2_3, "f2peel_3")




	def test_growing_peel(self):
		class Sakura(Tree):

			bough = self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.PEEL_HANDLER
				init_name	= "growing_peel"
				init_level	= 10


			@GrowingPeel
			class grow(Transmutable):
				def __call__(*args) : pass


		with self.assertLogs("growing_peel", 10) as case_loggy:

			self.test_case = Sakura()
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_1)),
				Path(os.path.basename(self.d2peel_1)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:growing_peel:Peeled growing bough \"{self.INIT_SET_BOUGH_1}\"",
				case_loggy.output
			)

			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_2)),
				Path(os.path.basename(self.d2peel_2)),
				Path(self.INIT_SET_BOUGH_1)
			)
			d2T = os.path.join(self.INIT_SET_BOUGH_1, self.peel_2_2)
			self.assertIn(f"DEBUG:growing_peel:Peeled growing bough \"{d2T}\"", case_loggy.output)

			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_3)),
				Path(os.path.basename(self.d2peel_3)),
				Path(self.INIT_SET_BOUGH_1)
			)
			d3T = os.path.join(self.INIT_SET_BOUGH_1, self.peel_2_3)
			self.assertIn(f"DEBUG:growing_peel:Peeled growing bough \"{d3T}\"", case_loggy.output)

			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_3)),
				Path(os.path.basename(self.d2peel_3)),
				Path(os.path.dirname(self.d2peel_3))
			)
			self.assertIn(f"DEBUG:growing_peel:Peeled growing bough \"{d3T}\"", case_loggy.output)








	def test_thriving_peel(self):
		testing_thrivings = "to", "the", "top",

		class Sakura(Tree):

			bough = self.INIT_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.PEEL_HANDLER
				init_name	= "thriving_peel"
				init_level	= 10

			@ThrivingPeel(*testing_thrivings)
			class top_grow(Transmutable):
				def __call__(*args):	pass

			@ThrivingPeel(*testing_thrivings, to_peak=False)
			class bot_grow(Transmutable):
				def __call__(*args):	pass


		top_grown	= os.path.join(self.INIT_SET_BOUGH_1, *testing_thrivings)
		bot_grown	= os.path.join(self.INIT_SET_BOUGH_1, *testing_thrivings)
		top_d2T		= os.path.join(self.INIT_SET_BOUGH_1, self.peel_2_2, *testing_thrivings)
		top_d3T		= os.path.join(self.INIT_SET_BOUGH_1, self.peel_2_3, *testing_thrivings)
		bot_d2T		= os.path.join(self.INIT_SET_BOUGH_1, *testing_thrivings, self.peel_2_2)
		bot_d3T		= os.path.join(self.INIT_SET_BOUGH_1, *testing_thrivings, self.peel_2_3)
		self.test_case = Sakura()

		with self.assertLogs("thriving_peel", 10) as case_loggy:

			self.test_case.top_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_1)),
				Path(os.path.basename(self.d2peel_1)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{top_grown}\"", case_loggy.output)

			self.test_case.top_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_2)),
				Path(os.path.basename(self.d2peel_2)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{top_d2T}\"", case_loggy.output)

			self.test_case.top_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_3)),
				Path(os.path.basename(self.d2peel_3)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{top_d3T}\"", case_loggy.output)

			self.test_case.top_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_3)),
				Path(os.path.basename(self.d2peel_3)),
				Path(os.path.dirname(self.d2peel_3))
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{top_d3T}\"", case_loggy.output)




			self.test_case.bot_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_1)),
				Path(os.path.basename(self.d2peel_1)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{bot_grown}\"", case_loggy.output)

			self.test_case.bot_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_2)),
				Path(os.path.basename(self.d2peel_2)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{bot_d2T}\"", case_loggy.output)

			self.test_case.bot_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_3)),
				Path(os.path.basename(self.d2peel_3)),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{bot_d3T}\"", case_loggy.output)

			self.test_case.bot_grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(os.path.dirname(self.d2peel_3)),
				Path(os.path.basename(self.d2peel_3)),
				Path(os.path.dirname(self.d2peel_3))
			)
			self.assertIn(f"DEBUG:thriving_peel:Peeled thriving bough \"{bot_d3T}\"", case_loggy.output)


		try:

			class SakuraRaise(Tree):

				bough = self.INIT_SET_BOUGH_1
				@ThrivingPeel("raise", "cause", False)
				class raising_grow(Transmutable):
					def __call__(*args):	pass


		except	Exception as E:

			self.assertIsInstance(E, AssertionError)
			self.assertEqual(str(E), f"Thriving must be with strings, not \"{type(False)}\"")








if __name__ == "__main__" : unittest.main(verbosity=2)







