import	os
import	unittest
from	pathlib								import Path
from	time								import sleep
from	shutil								import rmtree
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.hagrid				import HagridTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.shelve				import LibraryShelf
from	pygwarts.hagrid.planting.peeks		import BlindPeek








class BlindPeekCases(HagridTestCase):

	"""
		Ensures peeks algorithm works as intended
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.BLIND_PEEK_HANDLER): os.remove(cls.BLIND_PEEK_HANDLER)

		if	os.path.isdir(cls.INIT_SET_SPROUT):		rmtree(cls.INIT_SET_SPROUT)
		if	os.path.isdir(cls.INIT_SET_BOUGH_1):	rmtree(cls.INIT_SET_BOUGH_1)

	@classmethod
	def setUpClass(cls):

		cls.peekable1 = "peekable1"
		cls.make_loggy_file(cls, cls.BLIND_PEEK_HANDLER)
		if not os.path.isdir(cls.INIT_SET_BOUGH_1): os.makedirs(cls.INIT_SET_BOUGH_1)

		cls.peekable_sprout1	= os.path.join(cls.INIT_SET_SPROUT, "peekable1")
		cls.peekable_bough1		= os.path.join(cls.INIT_SET_BOUGH_1, "peekable1")
		cls.peekable_bough2		= os.path.join(cls.INIT_SET_BOUGH_2, "peekable1")
		cls.peekable_bough3		= os.path.join(cls.INIT_SET_BOUGH_3, "peekable1")




	def test_cached_blind_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_renew_1"
				init_level	= 10

			@BlindPeek("seeds")
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


		with self.assertLogs("cached_renew_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		with self.assertLogs("cached_renew_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_renew_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_renew_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_renew_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())








	def test_cached_blind_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_renew_2"
				init_level	= 10

			@BlindPeek("seeds")
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("cached_renew_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		with self.assertLogs("cached_renew_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_renew_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertNotEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)








	def test_cached_blind_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_1"
				init_level	= 10

			@BlindPeek("seeds", renew=False)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


		with self.assertLogs("cached_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		with self.assertLogs("cached_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertNotEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)








	def test_cached_blind_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_2"
				init_level	= 10

			@BlindPeek("seeds", renew=False)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("cached_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		with self.assertLogs("cached_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertNotEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)








	def test_cached_blind_picky_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_picky_1"
				init_level	= 10

			@BlindPeek("seeds", renew=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


		with self.assertLogs("cached_picky_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0.0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		with self.assertLogs("cached_picky_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0.0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_picky_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0.0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertNotEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)








	def test_cached_blind_picky_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_picky_2"
				init_level	= 10

			@BlindPeek("seeds", renew=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("cached_picky_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		with self.assertLogs("cached_picky_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_picky_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertNotEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)








	def test_cached_blind_picky_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_picky_renew_1"
				init_level	= 10

			@BlindPeek("seeds", picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


		with self.assertLogs("cached_picky_renew_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_picky_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		with self.assertLogs("cached_picky_renew_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_picky_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_picky_renew_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_1:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_picky_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())








	def test_cached_blind_picky_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "cached_picky_renew_2"
				init_level	= 10

			@BlindPeek("seeds", picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("cached_picky_renew_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		with self.assertLogs("cached_picky_renew_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)


		with self.assertLogs("cached_picky_renew_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Cached blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertNotEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)








	def test_blind_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "renew_1"
				init_level	= 10

			@BlindPeek("seeds", cache=False)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


		with self.assertLogs("renew_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		with self.assertLogs("renew_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = int(os.path.getmtime(self.peekable_sprout1))
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("renew_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())








	def test_blind_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "renew_2"
				init_level	= 10

			@BlindPeek("seeds", cache=False)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("renew_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:renew_2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		with self.assertLogs("renew_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:renew_2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = int(os.path.getmtime(self.peekable_sprout1))
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("renew_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:renew_2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertNotEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), second_peek)








	def test_blind_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "1"
				init_level	= 10

			@BlindPeek("seeds", cache=False, renew=False)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


		with self.assertLogs("1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		with self.assertLogs("1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = int(os.path.getmtime(self.peekable_sprout1))
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), second_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)








	def test_blind_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "2"
				init_level	= 10

			@BlindPeek("seeds", cache=False, renew=False)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		with self.assertLogs("2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), int(os.path.getmtime(self.peekable_sprout1))
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = int(os.path.getmtime(self.peekable_sprout1))
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertNotEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), second_peek)








	def test_blind_picky_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "picky_1"
				init_level	= 10

			@BlindPeek("seeds", cache=False, renew=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


		with self.assertLogs("picky_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:picky_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0.0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		with self.assertLogs("picky_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:picky_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0.0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = os.path.getmtime(self.peekable_sprout1)
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("picky_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:picky_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_1:Blind peek for \"{self.peekable_sprout1}\" old ring: 0.0",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), second_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)








	def test_blind_picky_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "picky_2"
				init_level	= 10

			@BlindPeek("seeds", cache=False, renew=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("picky_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:picky_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		with self.assertLogs("picky_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:picky_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = os.path.getmtime(self.peekable_sprout1)
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("picky_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:picky_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_2:Blind peek for \"{self.peekable_sprout1}\" old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertNotEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), second_peek)








	def test_blind_picky_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "picky_renew_1"
				init_level	= 10

			@BlindPeek("seeds", cache=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


		with self.assertLogs("picky_renew_1", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:picky_renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:picky_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		with self.assertLogs("picky_renew_1", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:picky_renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:picky_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = os.path.getmtime(self.peekable_sprout1)
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("picky_renew_1", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:picky_renew_1:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:picky_renew_1:Flourish stopped cause blind peek only for sprigs renew",
				case_loggy.output
			)
			self.assertNotIn(self.peekable_sprout1, self.test_case.seeds())








	def test_blind_picky_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "picky_renew_2"
				init_level	= 10

			@BlindPeek("seeds", cache=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass

			class seeds(LibraryShelf):	pass


		self.test_case = Sakura()
		if	not os.path.isfile(self.peekable_sprout1):	self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)

		bough_peek_mimic = first_peek -1
		self.test_case.seeds[self.peekable_sprout1] = bough_peek_mimic


		with self.assertLogs("picky_renew_2", 10) as case_loggy:
			#################### grow to bough1
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		with self.assertLogs("picky_renew_2", 10) as case_loggy:
			#################### grow to bough2
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_2)
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(
				self.test_case.seeds(self.peekable_sprout1), os.path.getmtime(self.peekable_sprout1)
			)


		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		second_peek = os.path.getmtime(self.peekable_sprout1)
		self.assertNotEqual(first_peek, second_peek)


		with self.assertLogs("picky_renew_2", 10) as case_loggy:
			#################### grow to bough3 (imitating source mtime change during Flourish)
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_3)
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:New blind peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:Blind peek for \"{self.peekable_sprout1}\" "
				f"old ring: {bough_peek_mimic}",
				case_loggy.output
			)
			self.assertIn(self.peekable_sprout1, self.test_case.seeds())
			self.assertNotEqual(self.test_case.seeds(self.peekable_sprout1), first_peek)
			self.assertEqual(self.test_case.seeds(self.peekable_sprout1), second_peek)








	def test_blind_comparators(self):

		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))
		second_peek = first_peek -1

		comparisons = {

			"Flourish stopped by blind peek comparator":							lambda A,B : A <B,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : B <A,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : A <= B,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : B <= A,
			"Flourish stopped by blind peek comparator":							lambda A,B : A == B,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : A != B,
		}

		for i,( message,comparator ) in enumerate(comparisons.items()):
			class Sakura(Transmutable):
				class loggy(LibraryContrib):

					handler		= self.BLIND_PEEK_HANDLER
					init_name	= f"comparator-{i}"
					init_level	= 10

				@BlindPeek("seeds", renew=False, comparator=comparator)
				class grow(Transmutable):
					def __call__(*args):	pass

				class seeds(LibraryShelf):	pass

			self.test_case = Sakura()
			self.test_case.seeds[self.peekable_sprout1] = second_peek

			with self.assertLogs(f"comparator-{i}", 10) as case_loggy:

				self.test_case.grow(

					self.test_case,
					self.INIT_SET_SPROUT,
					Path(self.INIT_SET_SPROUT),
					Path(self.peekable_sprout1),
					Path(self.INIT_SET_BOUGH_1)
				)
				self.assertIn(f"DEBUG:comparator-{i}:{message}", case_loggy.output)
			self.test_case.loggy.close()








	def test_blind_picky_comparators(self):

		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)
		second_peek = first_peek -1

		comparisons = {

			"Flourish stopped by blind peek comparator":							lambda A,B : A <B,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : B <A,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : A <= B,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : B <= A,
			"Flourish stopped by blind peek comparator":							lambda A,B : A == B,
			f"Blind peek for \"{self.peekable_sprout1}\" old ring: {second_peek}":	lambda A,B : A != B,
		}

		for i,( message,comparator ) in enumerate(comparisons.items()):
			class Sakura(Transmutable):
				class loggy(LibraryContrib):

					handler		= self.BLIND_PEEK_HANDLER
					init_name	= f"picky_comparator-{i}"
					init_level	= 10

				@BlindPeek("seeds", renew=False, picky=True, comparator=comparator)
				class grow(Transmutable):
					def __call__(*args):	pass

				class seeds(LibraryShelf):	pass

			self.test_case = Sakura()
			self.test_case.seeds[self.peekable_sprout1] = second_peek

			with self.assertLogs(f"picky_comparator-{i}", 10) as case_loggy:

				self.test_case.grow(

					self.test_case,
					self.INIT_SET_SPROUT,
					Path(self.INIT_SET_SPROUT),
					Path(self.peekable_sprout1),
					Path(self.INIT_SET_BOUGH_1)
				)
				self.assertIn(f"DEBUG:picky_comparator-{i}:{message}", case_loggy.output)
			self.test_case.loggy.close()








	def test_blind_extra_comparators(self):
		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.BLIND_PEEK_HANDLER
				init_name	= "extra_comparator"
				init_level	= 10

			@BlindPeek("seeds", renew=False, comparator=lambda A,B : B <A or not os.path.isfile(B))
			class grow(Transmutable):
				def __call__(self, *args):	self.loggy.info("Proceed growing")

			class seeds(LibraryShelf):	pass

		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))

		self.test_case = Sakura()
		self.test_case.seeds[self.peekable_sprout1] = first_peek

		with self.assertLogs("extra_comparator", 10) as case_loggy:
			self.test_case.grow(

				self.test_case,
				self.INIT_SET_SPROUT,
				Path(self.INIT_SET_SPROUT),
				Path(self.peekable_sprout1),
				Path(self.INIT_SET_BOUGH_1)
			)
		self.assertIn(

			f"DEBUG:extra_comparator:New blind peek \"{self.peekable_sprout1}\" new ring: "
			f"{first_peek}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:extra_comparator:Blind peek for \"{self.peekable_sprout1}\" old ring: {first_peek}",
			case_loggy.output
		)
		self.assertIn("INFO:extra_comparator:Proceed growing", case_loggy.output)








	def test_blind_raising_comparators(self):

		comparators = (

			lambda		: True,
			lambda A	: bool(A),
			lambda A	: A **2,
			lambda A,B	: A +B,
			lambda A,B	: "B <A",
			lambda A,B,C: A +B +C,
			lambda A,B,C: bool(A +B +C),
		)

		for comparator in comparators:

			try:

				class Sakura(Transmutable):

					@BlindPeek("seeds", comparator=comparator)
					class raising_grow(Transmutable):
						def __call__(*args):	pass


			except	Exception as E:

				self.assertIsInstance(E, TypeError)
				self.assertEqual(
					str(E), "Blind peek comparator must be Callable[[ int|float, int|float ], bool]"
				)








if __name__ == "__main__" : unittest.main(verbosity=2)







