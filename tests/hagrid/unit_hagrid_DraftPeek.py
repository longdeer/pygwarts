import	os
import	unittest
from	pathlib								import Path
from	time								import sleep
from	shutil								import rmtree
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.time_turner		import TimeTurner
from	pygwarts.tests.hagrid				import HagridTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.planting.peeks		import DraftPeek








class DraftPeekCases(HagridTestCase):

	"""
		Ensures peeks algorithm works as intended
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.DRAFT_PEEK_HANDLER): os.remove(cls.DRAFT_PEEK_HANDLER)

		if	os.path.isdir(cls.INIT_SET_SPROUT):		rmtree(cls.INIT_SET_SPROUT)
		if	os.path.isdir(cls.INIT_SET_BOUGH_1):	rmtree(cls.INIT_SET_BOUGH_1)

	@classmethod
	def setUpClass(cls):

		cls.peekable1 = "peekable1"
		cls.make_loggy_file(cls, cls.DRAFT_PEEK_HANDLER)
		if not os.path.isdir(cls.INIT_SET_BOUGH_1): os.makedirs(cls.INIT_SET_BOUGH_1)

		cls.peekable_sprout1	= os.path.join(cls.INIT_SET_SPROUT, "peekable1")
		cls.peekable_bough1		= os.path.join(cls.INIT_SET_BOUGH_1, "peekable1")
		cls.peekable_bough2		= os.path.join(cls.INIT_SET_BOUGH_2, "peekable1")
		cls.peekable_bough3		= os.path.join(cls.INIT_SET_BOUGH_3, "peekable1")




	def test_cached_draft_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_renew_1"
				init_level	= 10

			@DraftPeek()
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:cached_renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:cached_renew_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:cached_renew_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)








	def test_cached_draft_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_renew_2"
				init_level	= 10

			@DraftPeek()
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = int(os.path.getmtime(self.peekable_bough1))
		self.fmake(self.peekable_bough2)
		bough2_peek = int(os.path.getmtime(self.peekable_bough2))
		self.fmake(self.peekable_bough3)
		bough3_peek = int(os.path.getmtime(self.peekable_bough3))

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


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

				f"DEBUG:cached_renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:cached_renew_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:cached_renew_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_renew_2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_cached_draft_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_1"
				init_level	= 10

			@DraftPeek(renew=False)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:cached_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_1:Draft peek for \"{self.peekable_bough1}\" old ring: 0",
				case_loggy.output
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

				f"DEBUG:cached_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_1:Draft peek for \"{self.peekable_bough2}\" old ring: 0",
				case_loggy.output
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

				f"DEBUG:cached_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_1:Draft peek for \"{self.peekable_bough3}\" old ring: 0",
				case_loggy.output
			)








	def test_cached_draft_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_2"
				init_level	= 10

			@DraftPeek(renew=False)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = int(os.path.getmtime(self.peekable_bough1))
		self.fmake(self.peekable_bough2)
		bough2_peek = int(os.path.getmtime(self.peekable_bough2))
		self.fmake(self.peekable_bough3)
		bough3_peek = int(os.path.getmtime(self.peekable_bough3))

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


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

				f"DEBUG:cached_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:cached_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:cached_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_cached_draft_picky_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_picky_1"
				init_level	= 10

			@DraftPeek(renew=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:cached_picky_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Draft peek for \"{self.peekable_bough1}\" old ring: 0.0",
				case_loggy.output
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

				f"DEBUG:cached_picky_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Draft peek for \"{self.peekable_bough2}\" old ring: 0.0",
				case_loggy.output
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

				f"DEBUG:cached_picky_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_1:Draft peek for \"{self.peekable_bough3}\" old ring: 0.0",
				case_loggy.output
			)








	def test_cached_draft_picky_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_picky_2"
				init_level	= 10

			@DraftPeek(renew=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = os.path.getmtime(self.peekable_bough1)
		self.fmake(self.peekable_bough2)
		bough2_peek = os.path.getmtime(self.peekable_bough2)
		self.fmake(self.peekable_bough3)
		bough3_peek = os.path.getmtime(self.peekable_bough3)

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


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

				f"DEBUG:cached_picky_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:cached_picky_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:cached_picky_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_cached_draft_picky_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_picky_renew_1"
				init_level	= 10

			@DraftPeek(picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:cached_picky_renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_picky_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:cached_picky_renew_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_picky_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:cached_picky_renew_1:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:cached_picky_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)








	def test_cached_draft_picky_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "cached_picky_renew_2"
				init_level	= 10

			@DraftPeek(picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = os.path.getmtime(self.peekable_bough1)
		self.fmake(self.peekable_bough2)
		bough2_peek = os.path.getmtime(self.peekable_bough2)
		self.fmake(self.peekable_bough3)
		bough3_peek = os.path.getmtime(self.peekable_bough3)

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


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

				f"DEBUG:cached_picky_renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Draft peek for \"{self.peekable_bough1}\" "
				f"old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:cached_picky_renew_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Draft peek for \"{self.peekable_bough2}\" "
				f"old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:cached_picky_renew_2:Cached draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:cached_picky_renew_2:Draft peek for \"{self.peekable_bough3}\" "
				f"old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_draft_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "renew_1"
				init_level	= 10

			@DraftPeek(cache=False)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)








	def test_draft_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "renew_2"
				init_level	= 10

			@DraftPeek(cache=False)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = int(os.path.getmtime(self.peekable_bough1))
		self.fmake(self.peekable_bough2)
		bough2_peek = int(os.path.getmtime(self.peekable_bough2))
		self.fmake(self.peekable_bough3)
		bough3_peek = int(os.path.getmtime(self.peekable_bough3))

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


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

				f"DEBUG:renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:renew_2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:renew_2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:renew_2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_draft_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "1"
				init_level	= 10

			@DraftPeek(renew=False, cache=False)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:1:Draft peek for \"{self.peekable_bough1}\" old ring: 0",
				case_loggy.output
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

				f"DEBUG:1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:1:Draft peek for \"{self.peekable_bough2}\" old ring: 0",
				case_loggy.output
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

				f"DEBUG:1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:1:Draft peek for \"{self.peekable_bough3}\" old ring: 0",
				case_loggy.output
			)








	def test_draft_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "2"
				init_level	= 10

			@DraftPeek(renew=False, cache=False)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = int(os.path.getmtime(self.peekable_bough1))
		self.fmake(self.peekable_bough2)
		bough2_peek = int(os.path.getmtime(self.peekable_bough2))
		self.fmake(self.peekable_bough3)
		bough3_peek = int(os.path.getmtime(self.peekable_bough3))

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = int(os.path.getmtime(self.peekable_sprout1))


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

				f"DEBUG:2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_draft_picky_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "picky_1"
				init_level	= 10

			@DraftPeek(renew=False, cache=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:picky_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_1:Draft peek for \"{self.peekable_bough1}\" old ring: 0.0",
				case_loggy.output
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

				f"DEBUG:picky_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_1:Draft peek for \"{self.peekable_bough2}\" old ring: 0.0",
				case_loggy.output
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

				f"DEBUG:picky_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_1:Draft peek for \"{self.peekable_bough3}\" old ring: 0.0",
				case_loggy.output
			)








	def test_draft_picky_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "picky_2"
				init_level	= 10

			@DraftPeek(renew=False, cache=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = os.path.getmtime(self.peekable_bough1)
		self.fmake(self.peekable_bough2)
		bough2_peek = os.path.getmtime(self.peekable_bough2)
		self.fmake(self.peekable_bough3)
		bough3_peek = os.path.getmtime(self.peekable_bough3)

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


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

				f"DEBUG:picky_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:picky_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:picky_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_draft_picky_renew_1(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "picky_renew_1"
				init_level	= 10

			@DraftPeek(cache=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)
		if	os.path.isfile(self.peekable_bough1): os.remove(self.peekable_bough1)
		if	os.path.isfile(self.peekable_bough2): os.remove(self.peekable_bough2)
		if	os.path.isfile(self.peekable_bough3): os.remove(self.peekable_bough3)


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

				f"DEBUG:picky_renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:picky_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:picky_renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:picky_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)


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

				f"DEBUG:picky_renew_1:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				"DEBUG:picky_renew_1:Flourish stopped cause draft peek only for sprigs renew",
				case_loggy.output
			)








	def test_draft_picky_renew_2(self):

		class Sakura(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.DRAFT_PEEK_HANDLER
				init_name	= "picky_renew_2"
				init_level	= 10

			@DraftPeek(cache=False, picky=True)
			class grow(Transmutable):
				def __call__(*args):	pass


		self.test_case = Sakura()
		self.fmake(self.peekable_bough1)
		bough1_peek = os.path.getmtime(self.peekable_bough1)
		self.fmake(self.peekable_bough2)
		bough2_peek = os.path.getmtime(self.peekable_bough2)
		self.fmake(self.peekable_bough3)
		bough3_peek = os.path.getmtime(self.peekable_bough3)

		sleep(1.1)
		self.fmake(self.peekable_sprout1)
		first_peek = os.path.getmtime(self.peekable_sprout1)


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

				f"DEBUG:picky_renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:Draft peek for \"{self.peekable_bough1}\" old ring: {bough1_peek}",
				case_loggy.output
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

				f"DEBUG:picky_renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{first_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:Draft peek for \"{self.peekable_bough2}\" old ring: {bough2_peek}",
				case_loggy.output
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

				f"DEBUG:picky_renew_2:New draft peek \"{self.peekable_sprout1}\" new ring: "
				f"{second_peek}",
				case_loggy.output
			)
			self.assertIn(

				f"DEBUG:picky_renew_2:Draft peek for \"{self.peekable_bough3}\" old ring: {bough3_peek}",
				case_loggy.output
			)








	def test_draft_comparators(self):

		self.fmake(self.peekable_bough1)
		bough_peek = int(os.path.getmtime(self.peekable_bough1))

		sleep(1.1)
		self.fmake(self.peekable_sprout1)

		comparisons = {

			"Flourish stopped by draft peek comparator":							lambda A,B : A <B,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : B <A,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : A <= B,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : B <= A,
			"Flourish stopped by draft peek comparator":							lambda A,B : A == B,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : A != B,
		}

		for i,( message,comparator ) in enumerate(comparisons.items()):
			with self.assertLogs(f"comparator-{i}", 10) as case_loggy:

				class Sakura(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.DRAFT_PEEK_HANDLER
						init_name	= f"comparator-{i}"
						init_level	= 10

					@DraftPeek(renew=False, comparator=comparator)
					class grow(Transmutable):
						def __call__(*args):	pass

				self.test_case = Sakura()
				self.test_case.grow(

					self.test_case,
					self.INIT_SET_SPROUT,
					Path(self.INIT_SET_SPROUT),
					Path(self.peekable_sprout1),
					Path(self.INIT_SET_BOUGH_1)
				)
				self.assertIn(f"DEBUG:comparator-{i}:{message}", case_loggy.output)
			self.test_case.loggy.close()








	def test_draft_picky_comparators(self):

		self.fmake(self.peekable_bough1)
		bough_peek = os.path.getmtime(self.peekable_bough1)

		sleep(1.1)
		self.fmake(self.peekable_sprout1)

		comparisons = {

			"Flourish stopped by draft peek comparator":							lambda A,B : A <B,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : B <A,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : A <= B,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : B <= A,
			"Flourish stopped by draft peek comparator":							lambda A,B : A == B,
			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	lambda A,B : A != B,
		}

		for i,( message,comparator ) in enumerate(comparisons.items()):
			with self.assertLogs(f"picky_comparator-{i}", 10) as case_loggy:

				class Sakura(Transmutable):
					bough = self.INIT_SET_BOUGH_1
					class loggy(LibraryContrib):

						handler		= self.DRAFT_PEEK_HANDLER
						init_name	= f"picky_comparator-{i}"
						init_level	= 10

					@DraftPeek(renew=False, picky=True, comparator=comparator)
					class grow(Transmutable):
						def __call__(*args):	pass

				self.test_case = Sakura()
				self.test_case.grow(

					self.test_case,
					self.INIT_SET_SPROUT,
					Path(self.INIT_SET_SPROUT),
					Path(self.peekable_sprout1),
					Path(self.INIT_SET_BOUGH_1)
				)
				self.assertIn(f"DEBUG:picky_comparator-{i}:{message}", case_loggy.output)
			self.test_case.loggy.close()








	def test_draft_time_comparators(self):

		self.fmake(self.peekable_sprout1)
		self.fmake(self.peekable_bough1)

		sprout_peek = int(os.path.getmtime(self.peekable_sprout1))
		bough_peek = int(os.path.getmtime(self.peekable_bough1))
		self.assertEqual(sprout_peek, bough_peek)

		comparisons = {

			f"Draft peek for \"{self.peekable_bough1}\" old ring: {bough_peek}":	(
				lambda A,B : TimeTurner(minutes=-1).epoch <A
			),
		}

		for i,( message,comparator ) in enumerate(comparisons.items()):
			with self.assertLogs(f"time_comparator-{i}", 10) as case_loggy:

				class Sakura(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.DRAFT_PEEK_HANDLER
						init_name	= f"time_comparator-{i}"
						init_level	= 10

					@DraftPeek(renew=False, comparator=comparator)
					class grow(Transmutable):
						def __call__(*args):	pass

				self.test_case = Sakura()
				self.test_case.grow(

					self.test_case,
					self.INIT_SET_SPROUT,
					Path(self.INIT_SET_SPROUT),
					Path(self.peekable_sprout1),
					Path(self.INIT_SET_BOUGH_1)
				)
				self.assertIn(f"DEBUG:time_comparator-{i}:{message}", case_loggy.output)
			self.test_case.loggy.close()








	def test_draft_raising_comparators(self):

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

					@DraftPeek(comparator=comparator)
					class raising_grow(Transmutable):
						def __call__(*args):	pass


			except	Exception as E:

				self.assertIsInstance(E, TypeError)
				self.assertEqual(
					str(E), "Draft peek comparator must be Callable[[ int|float, int|float ], bool]"
				)








if __name__ == "__main__" : unittest.main(verbosity=2)







