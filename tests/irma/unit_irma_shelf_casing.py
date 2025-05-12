import	os
import	unittest
from	typing								import Hashable
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.irma					import IrmaTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.shelve				import LibraryShelf
from	pygwarts.irma.shelve.casing			import shelf_case
from	pygwarts.irma.shelve.casing			import is_num
from	pygwarts.irma.shelve.casing			import num_diff
from	pygwarts.irma.shelve.casing			import seq_diff
from	pygwarts.irma.shelve.casing			import mostsec_diff
from	pygwarts.irma.shelve.casing			import byte_size_diff
from	pygwarts.irma.shelve.casing			import ShelfCase
from	pygwarts.irma.shelve.casing			import NumDiffCase
from	pygwarts.irma.shelve.casing			import SeqDiffCase








class ShelfCasingCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""


	MOSTSEC_PATTERN		= r"\d+ [humnsd]+( \d+ [humnsd]+)* \([\+\-]\d+ [humnsd]+( \d+ [humnsd]+)*\)"
	BYTESIZE_PATTERN	= r"\d+[BKMGT]( \d+[BKMGT])* \([\+\-]\d+[BKMGT]( \d+[BKMGT])*\)"


	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.CASING_HANDLER): os.remove(cls.CASING_HANDLER)


	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.CASING_HANDLER)
		cls.prep1 = lambda _,A	: A
		cls.prep2 = lambda _,A	: f"{A} bananas"
		cls.post1 = lambda _,A,B: str(A)
		cls.post2 = lambda _,A,B: f"It's {A} and so on"
		cls.current_shelf = LibraryShelf()




	def test_shelf_case_targets(self):
		for target in (

			42, 69., "ten", True, False, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
		):
			with self.subTest(target=target):

				self.assertEqual(
					shelf_case(

						target,
						key="test",
						shelf=self.current_shelf,
						prep=self.prep1,
						post=self.post1,
					),	str(target)
				)
				self.assertEqual(self.current_shelf["test"], target)

		self.assertIsNotNone(self.current_shelf["test"])
		self.assertIsNone(
			shelf_case(

				None,
				key="test",
				shelf=self.current_shelf,
				prep=self.prep1,
				post=self.post1,
			),	str(target)
		)
		self.assertIsNotNone(self.current_shelf["test"])




	def test_shelf_case_keys(self):

		for item in ( 42, 69., "ten", True, False, None, ..., int, Transmutable,( 1, )):
			with self.subTest(key=item):

				self.assertEqual(
					shelf_case(

						"target",
						key=item,
						shelf=self.current_shelf,
						prep=self.prep1,
						post=self.post1,
					),	"target"
				)
				self.assertEqual(self.current_shelf[item], "target")




	def test_invalid_key_shelf_case(self):

		for invalid in ([ 1 ],{ 1 },{ "value": 1 }):
			with self.subTest(key=invalid):

				self.assertNotIsInstance(invalid, Hashable)
				self.assertIsNone(
					shelf_case(

						"target",
						key=invalid,
						shelf=self.current_shelf,
						prep=self.prep1,
						post=self.post1,
					)
				)




	def test_shelf_case_invalid_shelf(self):
		for invalid in (

			42, 69., "ten", True, False, None, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 }
		):
			with self.subTest(shelf=invalid):

				self.assertNotIsInstance(invalid, LibraryShelf)
				self.assertIsNone(
					shelf_case(

						"target",
						key="test",
						shelf=invalid,
						prep=self.prep1,
						post=self.post1,
					)
				)




	def test_shelf_case_invalid_prep(self):
		for invalid in (

			42, 69., "ten", True, False, None, ..., super, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
		):
			with self.subTest(prep=invalid):
				self.assertIsNone(
					shelf_case(

						42,
						key="test",
						shelf=self.current_shelf,
						prep=invalid,
						post=self.post1,
					)
				)




	def test_shelf_case_invalid_post(self):
		for invalid in (

			42, 69., "ten", True, False, None, ..., super, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
		):
			with self.subTest(post=invalid):
				self.assertIsNone(
					shelf_case(

						42,
						key="test",
						shelf=self.current_shelf,
						prep=self.prep1,
						post=invalid,
					)
				)








	def test_is_num_int_prep(self):

		for i in range(-100,101,1):
			with self.subTest(candidate=i): self.assertEqual(is_num(i),i)


	def test_is_num_str_prep(self):

		for i in range(-100,101,1):
			j = str(i)
			with self.subTest(candidate=j): self.assertEqual(is_num(j),j)


	def test_is_num_float_prep(self):

		for i in range(101):
			j = float(f".{i}")
			k = -j

			with self.subTest(candidates=( j,k )):

				self.assertEqual(is_num(j),j)
				self.assertEqual(is_num(k),k)








	def test_valid_num_diff_post(self):

		for i in range(101):
			for j in range(i +1,102):

				r00 = str(j)
				r01 = float(j)
				r02 = float(i)
				r03 = float(j -i)
				r04 = float(i -j)
				r05 = f"{j} (+{j -i})"
				r06 = f"{j} (+{r03})"
				r07 = f"{r01} (+{r03})"
				r08 = f"{i} ({i -j})"
				r09 = f"{i} ({r04})"
				r10 = f"{r02} ({r04})"

				self.assertEqual(num_diff(j,i),					r05)
				self.assertEqual(num_diff(j,str(i)),			r05)
				self.assertEqual(num_diff(j,float(i)),			r06)
				self.assertEqual(num_diff(str(j),i),			r05)
				self.assertEqual(num_diff(str(j),str(i)),		r05)
				self.assertEqual(num_diff(str(j),float(i)),		r06)
				self.assertEqual(num_diff(float(j),i),			r07)
				self.assertEqual(num_diff(float(j),str(i)),		r07)
				self.assertEqual(num_diff(float(j),float(i)),	r07)

				self.assertEqual(num_diff(i,j),					r08)
				self.assertEqual(num_diff(i,str(j)),			r08)
				self.assertEqual(num_diff(i,float(j)),			r09)
				self.assertEqual(num_diff(str(i),j),			r08)
				self.assertEqual(num_diff(str(i),str(j)),		r08)
				self.assertEqual(num_diff(str(i),float(j)),		r09)
				self.assertEqual(num_diff(float(i),j),			r10)
				self.assertEqual(num_diff(float(i),str(j)),		r10)
				self.assertEqual(num_diff(float(i),float(j)),	r10)

				self.assertEqual(num_diff(j,j),					r00)
				self.assertEqual(num_diff(j,str(j)),			r00)
				self.assertEqual(num_diff(j,float(j)),			r00)
				self.assertEqual(num_diff(str(j),j),			r00)
				self.assertEqual(num_diff(str(j),str(j)),		r00)
				self.assertEqual(num_diff(str(j),float(j)),		r00)
				self.assertEqual(num_diff(float(j),j),			str(r01))
				self.assertEqual(num_diff(float(j),str(j)),		str(r01))
				self.assertEqual(num_diff(float(j),float(j)),	str(r01))


	def test_invalid_num_diff_post(self):

		for invalid in ( ..., [ 1 ],( 1, ),{ 1 },{ "num1": 1 }):
			with self.subTest(num=invalid):

				self.assertRaises(TypeError, num_diff, 42, invalid)
				self.assertRaises(TypeError, num_diff, invalid, 42)
				if	invalid != { 1 } : self.assertRaises(TypeError, num_diff, invalid, invalid)

		for invalid in ( print, Transmutable ):
			with self.subTest(num=invalid):

				self.assertRaises(SyntaxError, num_diff, 42, invalid)
				self.assertRaises(SyntaxError, num_diff, invalid, 42)
				self.assertRaises(SyntaxError, num_diff, invalid, invalid)

		for invalid in ( "one", ):
			with self.subTest(num=invalid):

				self.assertRaises(NameError, num_diff, 42, invalid)
				self.assertRaises(NameError, num_diff, invalid, 42)
				self.assertRaises(NameError, num_diff, invalid, invalid)








	def test_valid_same_seq_diff_post(self):
		for seq1 in (

			( 1,2,3,4,5,6 ),[ 1,2,3,4,5,6 ],{ 1,2,3,4,5,6 },
			{ 1: True, 2: True, 3: True, 4: True, 5: True, 6: True },
		):
			for seq2 in (

				( 1,2,3,4 ),[ 1,2,3,4 ],{ 1,2,3,4 },
				{ 1: True, 2: True, 3: True, 4: True },
			):
				with self.subTest(seq1=seq1, seq2=seq2):
					self.assertCountEqual(seq_diff(seq1, seq2),[ "1","2","3","4","5 (+)","6 (+)" ])

				with self.subTest(seq1=seq1, seq2=seq1):
					self.assertCountEqual(seq_diff(seq1, seq1),[ "1","2","3","4","5","6" ])

				with self.subTest(seq1=seq2, seq2=seq1):
					self.assertCountEqual(seq_diff(seq2, seq1),[ "1","2","3","4" ])

				with self.subTest(seq1=seq2, seq2=seq2):
					self.assertCountEqual(seq_diff(seq2, seq1),[ "1","2","3","4" ])




	def test_valid_different_seq_diff_post(self):
		for seq1 in (

			( 1,2.,"3",4,5.,"6" ),[ 1,2.,"3",4,5.,"6" ],{ 1,2.,"3",4,5.,"6" },
			{ 1: True, 2.: True, "3": True, 4: True, 5.: True, "6": True },
		):
			for seq2 in (

				( "1",2,3,4 ),[ "1",2,3,4 ],{ "1",2,3,4 },
				{ "1": True, 2: True, 3: True, 4: True },
			):
				with self.subTest(seq1=seq1, seq2=seq2):
					self.assertCountEqual(
						seq_diff(seq1, seq2),[ "1 (+)","2.0","3 (+)","4","5.0 (+)","6 (+)" ]
					)

				with self.subTest(seq1=seq1, seq2=seq1):
					self.assertCountEqual(seq_diff(seq1, seq1),[ "1","2.0","3","4","5.0","6" ])

				with self.subTest(seq1=seq2, seq2=seq1):
					self.assertCountEqual(seq_diff(seq2, seq1),[ "1 (+)","2","3 (+)","4" ])

				with self.subTest(seq1=seq2, seq2=seq2):
					self.assertCountEqual(seq_diff(seq2, seq2),[ "1","2","3","4" ])




	def test_invalid_seq_diff_post(self):

		valid_seq = ( 1,2,3,4,5 )
		for invalid in ( 42, 69., True, ..., int, Transmutable ):

			self.assertRaises(TypeError, seq_diff, invalid, valid_seq)
			self.assertRaises(TypeError, seq_diff, valid_seq, invalid)
			self.assertRaises(TypeError, seq_diff, invalid, invalid)








	def test_valid_mostsec_diff_int(self):

		for i in range(100):
			for j in range(100):

				fi = float(i)
				fj = float(j)
				si1	= str(i)
				sj1	= str(j)
				si2	= str(fi)
				sj2	= str(fj)

				self.assertRegex(mostsec_diff(i,j), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,i), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,fj), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,fi), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,sj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,si1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,sj2), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,si2), self.MOSTSEC_PATTERN)

				self.assertRegex(mostsec_diff(j,i), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,j), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,fi), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,fj), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,si1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,sj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,si2), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,sj2), self.MOSTSEC_PATTERN)


	def test_valid_mostsec_diff_big_int(self):

		for i in range(int(1E9), int(100E9), int(1E9)):
			for j in range(100):

				fi = float(i)
				fj = float(j)
				si1	= str(i)
				sj1	= str(j)
				si2	= str(fi)
				sj2	= str(fj)

				self.assertRegex(mostsec_diff(i,j), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,i), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,fj), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,fi), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,sj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,si1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,sj2), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,si2), self.MOSTSEC_PATTERN)

				self.assertRegex(mostsec_diff(j,i), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,j), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,fi), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,fj), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,si1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,sj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,si2), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,sj2), self.MOSTSEC_PATTERN)


	def test_valid_mostsec_diff_float(self):

		for i in range(100):
			for j in range(100):

				fi1	= f"{i}.{j}"
				fj1 = f"{j}.{i}"
				si1	= float(fi1)
				sj1 = float(fj1)

				self.assertRegex(mostsec_diff(i,fj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,fi1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,sj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,si1), self.MOSTSEC_PATTERN)

				self.assertRegex(mostsec_diff(j,fi1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,fj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,si1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,sj1), self.MOSTSEC_PATTERN)


	def test_valid_mostsec_diff_big_float(self):

		for i in range(int(1E9), int(100E9), int(1E9)):
			for j in range(100):

				fi1	= f"{i}.{j}"
				fj1 = f"{j}.{i}"
				si1	= float(fi1)
				sj1 = float(fj1)

				self.assertRegex(mostsec_diff(i,fj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,fi1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,sj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(i,si1), self.MOSTSEC_PATTERN)

				self.assertRegex(mostsec_diff(j,fi1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,fj1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,si1), self.MOSTSEC_PATTERN)
				self.assertRegex(mostsec_diff(j,sj1), self.MOSTSEC_PATTERN)


	def test_invalid_mostsec_diff(self):

		for invalid1 in (

			"integer", ..., print, unittest, Transmutable,
			[ 42 ],( 42, ),{ "value": 42 }
		):
			for invalid2 in (

				"integer", ..., print, unittest, Transmutable,
				[ 42 ],( 42, ),{ "value": 42 }
			):
				with self.subTest(invalid1=invalid1, invalid2=invalid2):
					self.assertRaises(

						(NameError, TypeError, SyntaxError),
						mostsec_diff,
						invalid1,
						invalid2
					)
					self.assertRaises(

						(NameError, TypeError, SyntaxError),
						mostsec_diff,
						invalid2,
						invalid1
					)








	def test_valid_byte_size_diff_int(self):

		for i in range(100):
			for j in range(100):

				fi = float(i)
				fj = float(j)
				si1	= str(i)
				sj1	= str(j)
				si2	= str(fi)
				sj2	= str(fj)

				self.assertRegex(byte_size_diff(i,j), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,i), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,fj), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,fi), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,sj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,si1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,sj2), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,si2), self.BYTESIZE_PATTERN)

				self.assertRegex(byte_size_diff(j,i), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,j), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,fi), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,fj), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,si1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,sj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,si2), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,sj2), self.BYTESIZE_PATTERN)


	def test_valid_byte_size_diff_big_int(self):

		for i in range(int(1E9), int(100E9), int(1E9)):
			for j in range(100):

				fi = float(i)
				fj = float(j)
				si1	= str(i)
				sj1	= str(j)
				si2	= str(fi)
				sj2	= str(fj)

				self.assertRegex(byte_size_diff(i,j), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,i), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,fj), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,fi), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,sj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,si1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,sj2), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,si2), self.BYTESIZE_PATTERN)

				self.assertRegex(byte_size_diff(j,i), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,j), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,fi), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,fj), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,si1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,sj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,si2), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,sj2), self.BYTESIZE_PATTERN)


	def test_valid_byte_size_diff_float(self):

		for i in range(100):
			for j in range(100):

				fi1	= f"{i}.{j}"
				fj1 = f"{j}.{i}"
				si1	= float(fi1)
				sj1 = float(fj1)

				self.assertRegex(byte_size_diff(i,fj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,fi1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,sj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,si1), self.BYTESIZE_PATTERN)

				self.assertRegex(byte_size_diff(j,fi1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,fj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,si1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,sj1), self.BYTESIZE_PATTERN)


	def test_valid_byte_size_diff_big_float(self):

		for i in range(int(1E9), int(100E9), int(1E9)):
			for j in range(100):

				fi1	= f"{i}.{j}"
				fj1 = f"{j}.{i}"
				si1	= float(fi1)
				sj1 = float(fj1)

				self.assertRegex(byte_size_diff(i,fj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,fi1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,sj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(i,si1), self.BYTESIZE_PATTERN)

				self.assertRegex(byte_size_diff(j,fi1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,fj1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,si1), self.BYTESIZE_PATTERN)
				self.assertRegex(byte_size_diff(j,sj1), self.BYTESIZE_PATTERN)


	def test_invalid_byte_size_diff(self):

		for invalid1 in (

			"integer", ..., print, unittest, Transmutable,
			[ 42 ],( 42, ),{ "value": 42 }
		):
			for invalid2 in (

				"integer", ..., print, unittest, Transmutable,
				[ 42 ],( 42, ),{ "value": 42 }
			):
				with self.subTest(invalid1=invalid1, invalid2=invalid2):
					self.assertRaises(

						(NameError, TypeError, SyntaxError),
						byte_size_diff,
						invalid1,
						invalid2
					)
					self.assertRaises(

						(NameError, TypeError, SyntaxError),
						byte_size_diff,
						invalid2,
						invalid1
					)








	def test_ShelfCase_targets(self):

		@ShelfCase("CurrentShelf")
		class Shelfinator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "ShelfCase_targets"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Shelfinator()

		with self.assertLogs("ShelfCase_targets", 10) as case_loggy:
			for target in (

				42, 69., "ten", True, False, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
			):
				with self.subTest(target=target):

					self.assertEqual(self.test_case(target), target)
					self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], target)

			self.assertIn(
				f"DEBUG:ShelfCase_targets:Obtained shelf casing value \"{target}\"", case_loggy.output
			)




	def test_invalid_links_ShelfCase(self):
		for i,invalid in enumerate((

			42, 69., "ten", True, False, None, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 }
		)):
			@ShelfCase(invalid)
			class Shelfinator(Transmutable):
				class loggy(LibraryContrib):

					handler		= self.CASING_HANDLER
					init_name	= f"invalid_links_ShelfCase-{i}"
					init_level	= 10

				class CurrentShelf(LibraryShelf):	pass
				def __call__(self): return "cased"

			self.test_case = Shelfinator()

			with self.assertLogs(f"invalid_links_ShelfCase-{i}", 10) as case_loggy:
				self.assertEqual(self.test_case(), "cased")

			self.assertIn(

				f"DEBUG:invalid_links_ShelfCase-{i}:Failed to obtain shelf casing value",
				case_loggy.output
			)
			self.test_case.loggy.close()




	def test_ShelfCase_prep_targets(self):

		@ShelfCase("CurrentShelf", prep=self.prep2)
		class Shelfinator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "ShelfCase_prep_targets"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Shelfinator()

		with self.assertLogs("ShelfCase_prep_targets", 10) as case_loggy:
			for target in (

				42, 69., "ten", True, False, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
			):
				with self.subTest(target=target):

					self.assertEqual(self.test_case(target), f"{target} bananas")
					self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], f"{target} bananas")

			self.assertIn(

				f"DEBUG:ShelfCase_prep_targets:Obtained shelf casing value \"{target} bananas\"",
				case_loggy.output
			)




	def test_ShelfCase_post_targets(self):

		@ShelfCase("CurrentShelf", post=self.post2)
		class Shelfinator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "ShelfCase_post_targets"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Shelfinator()

		with self.assertLogs("ShelfCase_post_targets", 10) as case_loggy:
			for target in (

				42, 69., "ten", True, False, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
			):
				with self.subTest(target=target):

					self.assertEqual(self.test_case(target), f"It's {target} and so on")
					self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], target)

			self.assertIn(

				f"DEBUG:ShelfCase_post_targets:Obtained shelf casing value \"It's {target} and so on\"",
				case_loggy.output
			)




	def test_ShelfCase_prep_post_targets(self):

		@ShelfCase("CurrentShelf", prep=self.prep2, post=self.post2)
		class Shelfinator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "ShelfCase_prep_post_targets"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Shelfinator()

		with self.assertLogs("ShelfCase_prep_post_targets", 10) as case_loggy:
			for target in (

				42, 69., "ten", True, False, ..., int, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
			):
				with self.subTest(target=target):

					self.assertEqual(self.test_case(target), f"It's {target} bananas and so on")
					self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], f"{target} bananas")

			self.assertIn(

				"DEBUG:ShelfCase_prep_post_targets:"
				f"Obtained shelf casing value \"It's {target} bananas and so on\"",
				case_loggy.output
			)




	def test_ShelfCase_valid_prep_invalid_post_targets(self):
		for i,invalid in enumerate((

			42, 69., "ten", True, False, None, ..., super, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
		)):
			with self.subTest(post=invalid):

				@ShelfCase("CurrentShelf", prep=self.prep2, post=invalid)
				class Shelfinator(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.CASING_HANDLER
						init_name	= f"ShelfCase_valid_prep_invalid_post-{i}"
						init_level	= 10

					class CurrentShelf(LibraryShelf):	pass
					def __call__(self): return "forty two"

				self.test_case = Shelfinator()

				with self.assertLogs(f"ShelfCase_valid_prep_invalid_post-{i}", 10) as case_loggy:

					self.assertEqual(self.test_case(), "forty two")
					self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "forty two bananas")

				self.assertIn(

					f"DEBUG:ShelfCase_valid_prep_invalid_post-{i}:Failed to obtain shelf casing value",
					case_loggy.output
				)
				self.test_case.loggy.close()




	def test_ShelfCase_invalid_prep_valid_post_targets(self):
		for i,invalid in enumerate((

			42, 69., "ten", True, False, None, ..., super, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
		)):
			with self.subTest(prep=invalid):

				@ShelfCase("CurrentShelf", prep=invalid, post=self.post2)
				class Shelfinator(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.CASING_HANDLER
						init_name	= f"ShelfCase_invalid_prep_valid_post-{i}"
						init_level	= 10

					class CurrentShelf(LibraryShelf):	pass
					def __call__(self): return "forty two"

				self.test_case = Shelfinator()

				with self.assertLogs(f"ShelfCase_invalid_prep_valid_post-{i}", 10) as case_loggy:

					self.assertEqual(self.test_case(), "forty two")
					self.assertIsNone(self.test_case.CurrentShelf[str(self.test_case)])

				self.assertIn(

					f"DEBUG:ShelfCase_invalid_prep_valid_post-{i}:Failed to obtain shelf casing value",
					case_loggy.output
				)
				self.test_case.loggy.close()




	def test_ShelfCase_invalid_prep_invalid_post_targets(self):
		for i,invalid in enumerate((

			42, 69., "ten", True, False, None, ..., super, Transmutable,[ 1 ],( 1, ),{ 1 },{ "value": 1 }
		)):
			with self.subTest(prep=invalid, post=invalid):

				@ShelfCase("CurrentShelf", prep=invalid, post=invalid)
				class Shelfinator(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.CASING_HANDLER
						init_name	= f"ShelfCase_invalid_prep_invalid_post-{i}"
						init_level	= 10

					class CurrentShelf(LibraryShelf):	pass
					def __call__(self): return "forty two"

				self.test_case = Shelfinator()

				with self.assertLogs(f"ShelfCase_invalid_prep_invalid_post-{i}", 10) as case_loggy:

					self.assertEqual(self.test_case(), "forty two")
					self.assertIsNone(self.test_case.CurrentShelf[str(self.test_case)])

				self.assertIn(

					f"DEBUG:ShelfCase_invalid_prep_invalid_post-{i}:Failed to obtain shelf casing value",
					case_loggy.output
				)
				self.test_case.loggy.close()








	def test_NumDiffCase_int(self):

		@NumDiffCase("CurrentShelf")
		class Numericator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "NumDiffCase_int"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self): return 42

		self.test_case = Numericator()
		self.test_case.CurrentShelf[str(self.test_case)] = 0
		self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 0)

		with self.assertLogs("NumDiffCase_int", 10) as case_loggy:

			self.assertEqual(self.test_case(), "42 (+42)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 42)
			self.assertEqual(self.test_case(), "42")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 42)
			self.test_case.CurrentShelf[str(self.test_case)] = 84
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 84)
			self.assertEqual(self.test_case(), "42 (-42)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 42)

		self.assertIn(
			"DEBUG:NumDiffCase_int:Obtained number difference string \"42 (+42)\"", case_loggy.output
		)
		self.assertIn(
			"DEBUG:NumDiffCase_int:Obtained number difference string \"42\"", case_loggy.output
		)
		self.assertIn(
			"DEBUG:NumDiffCase_int:Obtained number difference string \"42 (-42)\"", case_loggy.output
		)




	def test_NumDiffCase_float(self):

		@NumDiffCase("CurrentShelf")
		class Numericator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "NumDiffCase_float"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self): return 69.

		self.test_case = Numericator()
		self.test_case.CurrentShelf[str(self.test_case)] = 0
		self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 0)

		with self.assertLogs("NumDiffCase_float", 10) as case_loggy:

			self.assertEqual(self.test_case(), "69.0 (+69.0)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 69.0)
			self.assertEqual(self.test_case(), "69.0")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 69.0)
			self.test_case.CurrentShelf[str(self.test_case)] = 138
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 138)
			self.assertEqual(self.test_case(), "69.0 (-69.0)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 69.0)

		self.assertIn(
			"DEBUG:NumDiffCase_float:Obtained number difference string \"69.0 (+69.0)\"", case_loggy.output
		)
		self.assertIn(
			"DEBUG:NumDiffCase_float:Obtained number difference string \"69.0\"", case_loggy.output
		)
		self.assertIn(
			"DEBUG:NumDiffCase_float:Obtained number difference string \"69.0 (-69.0)\"", case_loggy.output
		)




	def test_NumDiffCase_int_str(self):

		@NumDiffCase("CurrentShelf")
		class Numericator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "NumDiffCase_int_str"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self): return "42"

		self.test_case = Numericator()
		self.test_case.CurrentShelf[str(self.test_case)] = 0
		self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 0)

		with self.assertLogs("NumDiffCase_int_str", 10) as case_loggy:

			self.assertEqual(self.test_case(), "42 (+42)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "42")
			self.assertEqual(self.test_case(), "42")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "42")
			self.test_case.CurrentShelf[str(self.test_case)] = 84
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 84)
			self.assertEqual(self.test_case(), "42 (-42)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "42")

		self.assertIn(
			"DEBUG:NumDiffCase_int_str:Obtained number difference string \"42 (+42)\"", case_loggy.output
		)
		self.assertIn(
			"DEBUG:NumDiffCase_int_str:Obtained number difference string \"42\"", case_loggy.output
		)
		self.assertIn(
			"DEBUG:NumDiffCase_int_str:Obtained number difference string \"42 (-42)\"", case_loggy.output
		)




	def test_NumDiffCase_float_str(self):

		@NumDiffCase("CurrentShelf")
		class Numericator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "NumDiffCase_float_str"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self): return "69."

		self.test_case = Numericator()
		self.test_case.CurrentShelf[str(self.test_case)] = 0
		self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 0)

		with self.assertLogs("NumDiffCase_float_str", 10) as case_loggy:

			self.assertEqual(self.test_case(), "69. (+69.0)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "69.")
			self.assertEqual(self.test_case(), "69.")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "69.")
			self.test_case.CurrentShelf[str(self.test_case)] = 138
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 138)
			self.assertEqual(self.test_case(), "69. (-69.0)")
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], "69.")

		self.assertIn(

			"DEBUG:NumDiffCase_float_str:Obtained number difference string \"69. (+69.0)\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:NumDiffCase_float_str:Obtained number difference string \"69.\"",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:NumDiffCase_float_str:Obtained number difference string \"69. (-69.0)\"",
			case_loggy.output
		)




	def test_not_num_NumDiffCase(self):

		@NumDiffCase("CurrentShelf")
		class Numericator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "not_num_NumDiffCase"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Numericator()
		self.test_case.CurrentShelf[str(self.test_case)] = 0
		self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 0)

		with self.assertLogs("not_num_NumDiffCase", 10) as case_loggy:
			for invalid in (

				"ten", True, False, None, ..., print, Transmutable,[ 1 ],( 1, ),{ 1 },{ "target": 1 }
			):
				with self.subTest(target=invalid): self.assertEqual(self.test_case(invalid), invalid)

		self.assertIn("DEBUG:not_num_NumDiffCase:Number difference not obtained", case_loggy.output)
		self.assertEqual(
			# must be exactly 10, cause "None" doesn't trigger loggy
			case_loggy.output.count("DEBUG:not_num_NumDiffCase:Number difference not obtained"), 10
		)




	def test_invalid_link_NumDiffCase(self):
		for i,invalid in enumerate((

			42, 69., "ten", True, False, None, ..., print, Transmutable,[ 1 ],( 1, ),{ 1 },{ "target": 1 }
		)):
			with self.subTest(link=invalid):

				@NumDiffCase(invalid)
				class Numericator(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.CASING_HANDLER
						init_name	= f"invalid_link_NumDiffCase-{i}"
						init_level	= 10

					class CurrentShelf(LibraryShelf):	pass
					def __call__(self): return 42

				self.test_case = Numericator()
				self.test_case.CurrentShelf[str(self.test_case)] = 0

				with self.assertLogs(f"invalid_link_NumDiffCase-{i}", 10) as case_loggy:
					self.assertEqual(self.test_case(), 42)

				self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], 0)
				self.assertIn(

					f"DEBUG:invalid_link_NumDiffCase-{i}:Number difference not obtained",
					case_loggy.output
				)
				self.test_case.loggy.close()








	def test_valid_SeqDiffCase(self):

		@SeqDiffCase("CurrentShelf")
		class Sequenator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "valid_SeqDiffCase"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Sequenator()
		seq1 = [ 1, 3, 2, 4 ]
		seq2 = ( 1, 1, 3, 2, 2, 3, 4, 5, 6, 6 )
		res1 = [ "1 (+)", "3 (+)", "2 (+)", "4 (+)" ]
		res2 = [ "1", "1", "3", "2", "2", "3", "4", "5 (+)", "6 (+)", "6 (+)" ]

		with self.assertLogs("valid_SeqDiffCase", 10) as case_loggy:

			self.assertEqual(self.test_case(seq1), res1)
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], seq1)
			self.assertEqual(self.test_case(seq2), res2)
			self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)], seq2)

		self.assertIn(f"DEBUG:valid_SeqDiffCase:Obtained sequence difference \"{res1}\"", case_loggy.output)
		self.assertIn(f"DEBUG:valid_SeqDiffCase:Obtained sequence difference \"{res2}\"", case_loggy.output)




	def test_invalid_SeqDiffCase(self):

		@SeqDiffCase("CurrentShelf")
		class Sequenator(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CASING_HANDLER
				init_name	= "invalid_SeqDiffCase"
				init_level	= 10

			class CurrentShelf(LibraryShelf):	pass
			def __call__(self, KEY): return KEY

		self.test_case = Sequenator()

		with self.assertLogs("invalid_SeqDiffCase", 10) as case_loggy:
			for invalid in ( 42, 69., True, False, None, ..., print, Transmutable ):
				with self.subTest(seq1=invalid):

					self.assertEqual(self.test_case(invalid), invalid)
					self.assertIsNone(self.test_case.CurrentShelf[str(self.test_case)])

		self.assertIn(f"DEBUG:invalid_SeqDiffCase:Sequence difference not obtained", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:invalid_SeqDiffCase:Sequence difference not obtained"), 7
		)




	def test_invalid_link_SeqDiffCase(self):
		for i,invalid in enumerate((

			42, 69., "ten", True, False, None, ..., print, Transmutable,[ 1 ],( 1, ),{ 1 },{ "target": 1 }
		)):
			with self.subTest(link=invalid):

				@SeqDiffCase(invalid)
				class Sequenator(Transmutable):
					class loggy(LibraryContrib):

						handler		= self.CASING_HANDLER
						init_name	= f"invalid_link_SeqDiffCase-{i}"
						init_level	= 10

					class CurrentShelf(LibraryShelf):	pass
					def __call__(self): return [ 42 ]

				self.test_case = Sequenator()
				self.test_case.CurrentShelf[str(self.test_case)] = [ 0 ]

				with self.assertLogs(f"invalid_link_SeqDiffCase-{i}", 10) as case_loggy:
					self.assertEqual(self.test_case(),[ 42 ])

				self.assertEqual(self.test_case.CurrentShelf[str(self.test_case)],[ 0 ])
				self.assertIn(

					f"DEBUG:invalid_link_SeqDiffCase-{i}:Sequence difference not obtained",
					case_loggy.output
				)
				self.test_case.loggy.close()








if __name__ == "__main__" : unittest.main(verbosity=2)







