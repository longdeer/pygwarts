import	os
import	unittest
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.weeds		import SprigTrimmer
from	pygwarts.hagrid.bloom.weeds			import Efflorescence
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class EdgeMultiEffloresce(MediumSet):

	"""
		Efflorescence only, with branches, with and without bough included
		Double sprout copse
		Double bough copse
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_7): os.remove(cls.MEDIUM_HANDLER_7)

	@classmethod
	def setUpClass(cls):

		"""
			d- MEDIUM_SET_BOUGH_1
				f- lelik
				f- bolik
				d- bin
					f- untouchable
					f- mister
					d- in my bag
			d- MEDIUM_SET_BOUGH_2
				f- lelik
				f- bolik
				d- bin
					f- untouchable
					f- missis
					d- too bad

			d- MEDIUM_SET_SPROUT_1
				f- lelik
				d- bin
					f- untouchable
					f- mister
					d- in my bag
			d- MEDIUM_SET_SPROUT_2
				f- bolik
				d- bin
					f- untouchable
					f- missis
					d- too bad
		"""

		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_7)


		# First sprout
		cls.d_mss1_b				= os.path.join(cls.MEDIUM_SET_SPROUT_1, "bin")
		cls.f_mss1_lelik			= os.path.join(cls.MEDIUM_SET_SPROUT_1, "lelik")
		cls.f_mss1_b_untouchable	= os.path.join(cls.d_mss1_b, "untouchable")
		cls.f_mss1_b_mister			= os.path.join(cls.d_mss1_b, "mister")
		# Second sprout
		cls.d_mss2_b				= os.path.join(cls.MEDIUM_SET_SPROUT_2, "bin")
		cls.f_mss2_bolik			= os.path.join(cls.MEDIUM_SET_SPROUT_2, "bolik")
		cls.f_mss2_b_untouchable	= os.path.join(cls.d_mss2_b, "untouchable")
		cls.d_mss2_b_tb				= os.path.join(cls.d_mss2_b, "too bad")
		# First bough
		cls.tg1_f_lelik				= os.path.join(cls.MEDIUM_SET_BOUGH_1, "lelik")
		cls.tg1_f_bolik				= os.path.join(cls.MEDIUM_SET_BOUGH_1, "bolik")
		cls.tg1_d_b					= os.path.join(cls.MEDIUM_SET_BOUGH_1, "bin")
		cls.tg1_f_b_untouchable		= os.path.join(cls.tg1_d_b, "untouchable")
		cls.tg1_f_b_mister			= os.path.join(cls.tg1_d_b, "mister")
		cls.tg1_d_b_imb				= os.path.join(cls.tg1_d_b, "in my bag")
		# Sceond bough
		cls.tg2_f_lelik				= os.path.join(cls.MEDIUM_SET_BOUGH_2, "lelik")
		cls.tg2_f_bolik				= os.path.join(cls.MEDIUM_SET_BOUGH_2, "bolik")
		cls.tg2_d_b					= os.path.join(cls.MEDIUM_SET_BOUGH_2, "bin")
		cls.tg2_f_b_untouchable		= os.path.join(cls.tg2_d_b, "untouchable")
		cls.tg2_f_b_missis			= os.path.join(cls.tg2_d_b, "missis")
		cls.tg2_d_b_tb				= os.path.join(cls.tg2_d_b, "too bad")




	def setUp(self):
		self.clean()

		self.fmake(self.f_mss1_lelik, "bolik's brother")
		self.fmake(self.f_mss1_b_untouchable, "can't touch this")
		self.fmake(self.f_mss1_b_mister, "what is his name?")


		self.fmake(self.f_mss2_bolik, "lelik's brother")
		self.fmake(self.f_mss2_b_untouchable, "can't touch this")
		os.makedirs(self.d_mss2_b_tb, exist_ok=True)


		self.fmake(self.tg1_f_lelik, "bolik's brother")
		self.fmake(self.tg1_f_bolik, "lelik's brother")
		self.fmake(self.tg1_f_b_untouchable, "can't touch this")
		self.fmake(self.tg1_f_b_mister, "what is his name?")
		os.makedirs(self.tg1_d_b_imb, exist_ok=True)


		self.fmake(self.tg2_f_lelik, "bolik's brother")
		self.fmake(self.tg2_f_bolik, "lelik's brother")
		self.fmake(self.tg2_f_b_untouchable, "can't touch this")
		self.fmake(self.tg2_f_b_missis, "ain't real, actually, i guess")
		os.makedirs(self.tg2_d_b_tb, exist_ok=True)








	def test_distributed_effloresce(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_7
				init_name	= "distributed_effloresce"
				init_level	= 10

			class First(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):

					# include for growing/thriving and for trimming
					include = rf".+",
					# no bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_1}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_1.replace("\\","\\\\") + r"\\[^(\\)]+$", )
					)

				class twigs(SiftingController):

					# include for growing/thriving and for trimming
					include = rf".+",
					# no bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_1}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_1.replace("\\","\\\\") + r"\\[^(\\)]+$", )
					)

			class Second(Tree):

				bough = self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController):

					# include for growing/thriving and for trimming
					include = rf".+",
					# no bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_2}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_2.replace("\\","\\\\") + r"\\[^(\\)]+$", )
					)

				class twigs(SiftingController):

					# include for growing/thriving and for trimming
					include = rf".+",
					# no bough root mess
					exclude = (

						( rf"{self.MEDIUM_SET_BOUGH_2}/[^/]+$", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_2.replace("\\","\\\\") + r"\\[^(\\)]+$", )
					)



			class trim(SprigTrimmer):	pass
			class clean(Efflorescence):
				branches	= {

					self.MEDIUM_SET_BOUGH_1: ( self.MEDIUM_SET_SPROUT_1, ),
					self.MEDIUM_SET_BOUGH_2: ( self.MEDIUM_SET_SPROUT_2, ),
				}


			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class sync(Flourish):		pass




		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_lelik))
		self.assertTrue(os.path.isdir(self.d_mss1_b))
		self.assertTrue(os.path.isfile(self.f_mss1_b_untouchable))
		self.assertTrue(os.path.isfile(self.f_mss1_b_mister))


		# Sceond sprout
		self.assertTrue(os.path.isfile(self.f_mss2_bolik))
		self.assertTrue(os.path.isdir(self.d_mss2_b))
		self.assertTrue(os.path.isfile(self.f_mss2_b_untouchable))
		self.assertTrue(os.path.isdir(self.d_mss2_b_tb))


		# First bough
		self.assertTrue(os.path.isfile(self.tg1_f_lelik))
		self.assertTrue(os.path.isfile(self.tg1_f_bolik))
		self.assertTrue(os.path.isdir(self.tg1_d_b))
		self.assertTrue(os.path.isfile(self.tg1_f_b_untouchable))
		self.assertTrue(os.path.isfile(self.tg1_f_b_mister))
		self.assertTrue(os.path.isdir(self.tg1_d_b_imb))


		# Sceond bough
		self.assertTrue(os.path.isfile(self.tg2_f_lelik))
		self.assertTrue(os.path.isfile(self.tg2_f_bolik))
		self.assertTrue(os.path.isdir(self.tg2_d_b))
		self.assertTrue(os.path.isfile(self.tg2_f_b_untouchable))
		self.assertTrue(os.path.isfile(self.tg2_f_b_missis))
		self.assertTrue(os.path.isdir(self.tg2_d_b_tb))




		with self.assertLogs("distributed_effloresce", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()

		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg1_f_lelik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg1_f_bolik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed twig \"{self.tg1_d_b}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg1_f_b_untouchable}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg1_f_b_mister}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:distributed_effloresce:Trimmed twig \"{self.tg1_d_b_imb}\"",
			case_loggy.output
		)


		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg2_f_lelik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg2_f_bolik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed twig \"{self.tg2_d_b}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed twig \"{self.tg2_f_b_untouchable}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:distributed_effloresce:Trimmed leaf \"{self.tg2_f_b_missis}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:distributed_effloresce:Trimmed twig \"{self.tg2_d_b_tb}\"",
			case_loggy.output
		)




		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_lelik))
		self.assertTrue(os.path.isdir(self.d_mss1_b))
		self.assertTrue(os.path.isfile(self.f_mss1_b_untouchable))
		self.assertTrue(os.path.isfile(self.f_mss1_b_mister))


		# Sceond sprout
		self.assertTrue(os.path.isfile(self.f_mss2_bolik))
		self.assertTrue(os.path.isdir(self.d_mss2_b))
		self.assertTrue(os.path.isfile(self.f_mss2_b_untouchable))
		self.assertTrue(os.path.isdir(self.d_mss2_b_tb))


		# First bough
		self.assertTrue(os.path.isfile(self.tg1_f_lelik))
		self.assertTrue(os.path.isfile(self.tg1_f_bolik))
		self.assertTrue(os.path.isdir(self.tg1_d_b))
		self.assertTrue(os.path.isfile(self.tg1_f_b_untouchable))
		self.assertTrue(os.path.isfile(self.tg1_f_b_mister))
		self.assertFalse(os.path.isdir(self.tg1_d_b_imb))


		# Sceond bough
		self.assertTrue(os.path.isfile(self.tg2_f_lelik))
		self.assertTrue(os.path.isfile(self.tg2_f_bolik))
		self.assertTrue(os.path.isdir(self.tg2_d_b))
		self.assertTrue(os.path.isfile(self.tg2_f_b_untouchable))
		self.assertFalse(os.path.isfile(self.tg2_f_b_missis))
		self.assertTrue(os.path.isdir(self.tg2_d_b_tb))








	def test_bough_roots_effloresce(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_7
				init_name	= "bough_roots_effloresce"
				init_level	= 10

			class First(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):	include = rf".+",
				class twigs(SiftingController):	include = rf".+",

			class Second(Tree):

				bough = self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController):	include = rf".+",
				class twigs(SiftingController):	include = rf".+",


			class trim(SprigTrimmer):	pass
			class clean(Efflorescence):
				branches	= {

					self.MEDIUM_SET_BOUGH_1: ( self.MEDIUM_SET_SPROUT_1, ),
					self.MEDIUM_SET_BOUGH_2: ( self.MEDIUM_SET_SPROUT_2, ),
				}


			@fssprout(self.MEDIUM_SET_SPROUT_2)
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class sync(Flourish):		pass




		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_lelik))
		self.assertTrue(os.path.isdir(self.d_mss1_b))
		self.assertTrue(os.path.isfile(self.f_mss1_b_untouchable))
		self.assertTrue(os.path.isfile(self.f_mss1_b_mister))


		# Sceond sprout
		self.assertTrue(os.path.isfile(self.f_mss2_bolik))
		self.assertTrue(os.path.isdir(self.d_mss2_b))
		self.assertTrue(os.path.isfile(self.f_mss2_b_untouchable))
		self.assertTrue(os.path.isdir(self.d_mss2_b_tb))


		# First bough
		self.assertTrue(os.path.isfile(self.tg1_f_lelik))
		self.assertTrue(os.path.isfile(self.tg1_f_bolik))
		self.assertTrue(os.path.isdir(self.tg1_d_b))
		self.assertTrue(os.path.isfile(self.tg1_f_b_untouchable))
		self.assertTrue(os.path.isfile(self.tg1_f_b_mister))
		self.assertTrue(os.path.isdir(self.tg1_d_b_imb))


		# Sceond bough
		self.assertTrue(os.path.isfile(self.tg2_f_lelik))
		self.assertTrue(os.path.isfile(self.tg2_f_bolik))
		self.assertTrue(os.path.isdir(self.tg2_d_b))
		self.assertTrue(os.path.isfile(self.tg2_f_b_untouchable))
		self.assertTrue(os.path.isfile(self.tg2_f_b_missis))
		self.assertTrue(os.path.isdir(self.tg2_d_b_tb))




		with self.assertLogs("bough_roots_effloresce", 10) as case_loggy:

			self.test_case = Forest()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)




		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg1_f_lelik}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg1_f_bolik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed twig \"{self.tg1_d_b}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg1_f_b_untouchable}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg1_f_b_mister}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:bough_roots_effloresce:Trimmed twig \"{self.tg1_d_b_imb}\"",
			case_loggy.output
		)


		self.assertIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg2_f_lelik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg2_f_bolik}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed twig \"{self.tg2_d_b}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed twig \"{self.tg2_f_b_untouchable}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:bough_roots_effloresce:Trimmed leaf \"{self.tg2_f_b_missis}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:bough_roots_effloresce:Trimmed twig \"{self.tg2_d_b_tb}\"",
			case_loggy.output
		)




		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_lelik))
		self.assertTrue(os.path.isdir(self.d_mss1_b))
		self.assertTrue(os.path.isfile(self.f_mss1_b_untouchable))
		self.assertTrue(os.path.isfile(self.f_mss1_b_mister))


		# Sceond sprout
		self.assertTrue(os.path.isfile(self.f_mss2_bolik))
		self.assertTrue(os.path.isdir(self.d_mss2_b))
		self.assertTrue(os.path.isfile(self.f_mss2_b_untouchable))
		self.assertTrue(os.path.isdir(self.d_mss2_b_tb))


		# First bough
		self.assertTrue(os.path.isfile(self.tg1_f_lelik))
		self.assertFalse(os.path.isfile(self.tg1_f_bolik))
		self.assertTrue(os.path.isdir(self.tg1_d_b))
		self.assertTrue(os.path.isfile(self.tg1_f_b_untouchable))
		self.assertTrue(os.path.isfile(self.tg1_f_b_mister))
		self.assertFalse(os.path.isdir(self.tg1_d_b_imb))


		# Sceond bough
		self.assertFalse(os.path.isfile(self.tg2_f_lelik))
		self.assertTrue(os.path.isfile(self.tg2_f_bolik))
		self.assertTrue(os.path.isdir(self.tg2_d_b))
		self.assertTrue(os.path.isfile(self.tg2_f_b_untouchable))
		self.assertFalse(os.path.isfile(self.tg2_f_b_missis))
		self.assertTrue(os.path.isdir(self.tg2_d_b_tb))








if __name__ == "__main__" : unittest.main(verbosity=2)







