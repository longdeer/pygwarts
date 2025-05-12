import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.weeds			import Efflorescence
from	pygwarts.hagrid.cultivation.sifting	import SiftingController
from	pygwarts.hagrid.planting.weeds		import SprigTrimmer








class MultiBoughEfflorescence(MediumSet):

	"""
		Efflorescence
		Single sprout copse
		Triple bough copse
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_5): os.remove(cls.MEDIUM_HANDLER_5)

	@classmethod
	def setUpClass(cls):

		"""
			d- MEDIUM_SET_BOUGH_1
				d- men due
					f- rock
					f- paper
					f- scissors
					f- lizzard						- this one to be effloresced
					f- spock						- this one to be effloresced
					d- girls cries
						f- sad movies
						f- dumbasses (literaly)
						f- onion
						d- mirror reflections		- this one to be effloresced
				d- commons
					d- good
					d- not good
					d- bad
					d- not bad
					d- not not
					d- bad bad
					d- bad good
					d- good bad
					d- big bad wolf					- this one to be effloresced
		"""

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_5)


		# First bough first sprout
		cls.fmake(cls, cls.tg1_f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.tg1_f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.tg1_f_mss1_md_scissors, "only in HD or better")
		cls.fmake(cls, cls.tg1_f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		cls.fmake(cls, cls.tg1_f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		cls.fmake(cls, cls.tg1_f_mss1_md_gc_onion, "makes even devil cry")
		os.makedirs(cls.tg1_d_mss1_c_good)
		os.makedirs(cls.tg1_d_mss1_c_notgood)
		os.makedirs(cls.tg1_d_mss1_c_bad)
		os.makedirs(cls.tg1_d_mss1_c_notbad)
		os.makedirs(cls.tg1_d_mss1_c_notnot)
		os.makedirs(cls.tg1_d_mss1_c_badbad)
		os.makedirs(cls.tg1_d_mss1_c_badgood)
		os.makedirs(cls.tg1_d_mss1_c_goodbad)


		# Second bough first sprout
		cls.fmake(cls, cls.tg2_f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.tg2_f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.tg2_f_mss1_md_scissors, "only in HD or better")
		cls.fmake(cls, cls.tg2_f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		cls.fmake(cls, cls.tg2_f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		cls.fmake(cls, cls.tg2_f_mss1_md_gc_onion, "makes even devil cry")
		os.makedirs(cls.tg2_d_mss1_c_good)
		os.makedirs(cls.tg2_d_mss1_c_notgood)
		os.makedirs(cls.tg2_d_mss1_c_bad)
		os.makedirs(cls.tg2_d_mss1_c_notbad)
		os.makedirs(cls.tg2_d_mss1_c_notnot)
		os.makedirs(cls.tg2_d_mss1_c_badbad)
		os.makedirs(cls.tg2_d_mss1_c_badgood)
		os.makedirs(cls.tg2_d_mss1_c_goodbad)


		# Third bough first sprout
		cls.fmake(cls, cls.tg3_f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.tg3_f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.tg3_f_mss1_md_scissors, "only in HD or better")
		cls.fmake(cls, cls.tg3_f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		cls.fmake(cls, cls.tg3_f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		cls.fmake(cls, cls.tg3_f_mss1_md_gc_onion, "makes even devil cry")
		os.makedirs(cls.tg3_d_mss1_c_good)
		os.makedirs(cls.tg3_d_mss1_c_notgood)
		os.makedirs(cls.tg3_d_mss1_c_bad)
		os.makedirs(cls.tg3_d_mss1_c_notbad)
		os.makedirs(cls.tg3_d_mss1_c_notnot)
		os.makedirs(cls.tg3_d_mss1_c_badbad)
		os.makedirs(cls.tg3_d_mss1_c_badgood)
		os.makedirs(cls.tg3_d_mss1_c_goodbad)


		# First bough extra
		cls.tg1_f_mss1_md_lizzard	= os.path.join(cls.tg1_d_mss1_md, "lizzard")
		cls.tg1_f_mss1_md_spock		= os.path.join(cls.tg1_d_mss1_md, "spock")
		cls.tg1_d_mss1_md_d_mirror	= os.path.join(cls.tg1_d_mss1_md_gc, "mirror reflections")
		cls.tg1_d_mss1_c_bbw		= os.path.join(cls.tg1_d_mss1_c, "big bad wolf")
		cls.fmake(cls, cls.tg1_f_mss1_md_lizzard, "poisones spock")
		cls.fmake(cls, cls.tg1_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(cls.tg1_d_mss1_md_d_mirror)
		os.makedirs(cls.tg1_d_mss1_c_bbw)


		# Second bough extra
		cls.tg2_f_mss1_md_lizzard	= os.path.join(cls.tg2_d_mss1_md, "lizzard")
		cls.tg2_f_mss1_md_spock		= os.path.join(cls.tg2_d_mss1_md, "spock")
		cls.tg2_d_mss1_md_d_mirror	= os.path.join(cls.tg2_d_mss1_md_gc, "mirror reflections")
		cls.tg2_d_mss1_c_bbw		= os.path.join(cls.tg2_d_mss1_c, "big bad wolf")
		cls.fmake(cls, cls.tg2_f_mss1_md_lizzard, "poisones spock")
		cls.fmake(cls, cls.tg2_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(cls.tg2_d_mss1_md_d_mirror)
		os.makedirs(cls.tg2_d_mss1_c_bbw)


		# Third bough extra
		cls.tg3_f_mss1_md_lizzard	= os.path.join(cls.tg3_d_mss1_md, "lizzard")
		cls.tg3_f_mss1_md_spock		= os.path.join(cls.tg3_d_mss1_md, "spock")
		cls.tg3_d_mss1_md_d_mirror	= os.path.join(cls.tg3_d_mss1_md_gc, "mirror reflections")
		cls.tg3_d_mss1_c_bbw		= os.path.join(cls.tg3_d_mss1_c, "big bad wolf")
		cls.fmake(cls, cls.tg3_f_mss1_md_lizzard, "poisones spock")
		cls.fmake(cls, cls.tg3_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(cls.tg3_d_mss1_md_d_mirror)
		os.makedirs(cls.tg3_d_mss1_c_bbw)


	def setUp(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_5
				init_level	= 10

			class First(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):

					exclude = ( r".+/lizzard", ) if os.name == "posix" else ( r".+\\lizzard", )
					include = (
						(
							rf"{self.MEDIUM_SET_BOUGH_1}/.+",
							rf"{self.MEDIUM_SET_SPROUT_1}/.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
						)
					)

				class twigs(SiftingController):

					exclude = ( r".+/mirror.+", ) if os.name == "posix" else ( r".+\\mirror.+", )
					include = (
						(
							rf"{self.MEDIUM_SET_BOUGH_1}/.+",
							rf"{self.MEDIUM_SET_SPROUT_1}/.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
						)
					)

			class Second(Tree):

				bough = self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController):

					exclude = ( r".+/spock", ) if os.name == "posix" else ( r".+\\spock", )
					include = (
						(
							rf"{self.MEDIUM_SET_BOUGH_2}/.+",
							rf"{self.MEDIUM_SET_SPROUT_1}/.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_2.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
						)
					)

				class twigs(SiftingController):

					exclude = ( r".+/big.+", ) if os.name == "posix" else ( r".+\\big.+", )
					include = (
						(
							rf"{self.MEDIUM_SET_BOUGH_2}/.+",
							rf"{self.MEDIUM_SET_SPROUT_1}/.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_2.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
						)
					)

			class Third(Tree):

				bough = self.MEDIUM_SET_BOUGH_3
				class leafs(SiftingController):

					include = (
						(
							rf"{self.MEDIUM_SET_BOUGH_3}/.+",
							rf"{self.MEDIUM_SET_SPROUT_1}/.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_3.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
						)
					)

				class twigs(SiftingController):

					include = (
						(
							rf"{self.MEDIUM_SET_BOUGH_3}/.+",
							rf"{self.MEDIUM_SET_SPROUT_1}/.+",
						)	if os.name == "posix" else
						(
							self.MEDIUM_SET_BOUGH_3.replace("\\", "\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+",
						)
					)

			class trim(SprigTrimmer):	pass
			class clean(Efflorescence):
				branches	= {

					self.MEDIUM_SET_BOUGH_1: ( self.MEDIUM_SET_SPROUT_1, ),
					self.MEDIUM_SET_BOUGH_2: ( self.MEDIUM_SET_SPROUT_1, ),
					self.MEDIUM_SET_BOUGH_3: ( self.MEDIUM_SET_SPROUT_1, ),
				}


			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class sync(Flourish):		pass


		self.test_case = Forest




	def test_first_flourish(self):

		self.test_case.loggy.init_name = "first_flourish"
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_1))


		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# First bough extra
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bbw))


		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second bough extra
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb2_w))


		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Third bough extra
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg1_d_mss1_c_bbw}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.f_msb1_flower}\"",
			case_loggy.output
		)





		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.d_msb2_w}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg2_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_lizzard}\"",
			case_loggy.output
		)




		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg3_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.tg3_d_mss1_c_bbw}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.d_msb3_a}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed twig \"{self.d_msb3_t}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.f_msb3_almost}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:first_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_spock}\"",
			case_loggy.output
		)




		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# First bough extra
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))


		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb2_w))


		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Third bough extra
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
















	def test_no_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "no_touch_flourish"


		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# First bough extra
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))


		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb2_w))


		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Third bough extra
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg1_d_mss1_c_bbw}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.f_msb1_flower}\"",
			case_loggy.output
		)





		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.d_msb2_w}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg2_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_lizzard}\"",
			case_loggy.output
		)




		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg3_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.tg3_d_mss1_c_bbw}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.d_msb3_a}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed twig \"{self.d_msb3_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.f_msb3_almost}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:no_touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_spock}\"",
			case_loggy.output
		)


		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# First bough extra
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))


		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb2_w))


		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Third bough extra
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))
















	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"


		self.fmake(self.tg1_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(self.tg1_d_mss1_c_bbw)
		self.fmake(self.tg2_f_mss1_md_lizzard, "poisones spock")
		os.makedirs(self.tg2_d_mss1_md_d_mirror)
		self.fmake(self.tg3_f_mss1_md_lizzard, "poisones spock")
		self.fmake(self.tg3_f_mss1_md_spock, "vaporizes rock")
		os.makedirs(self.tg3_d_mss1_md_d_mirror)
		os.makedirs(self.tg3_d_mss1_c_bbw)



		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# First bough extra
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bbw))


		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second bough extra
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb2_w))


		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Third bough extra
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)


		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg1_d_mss1_c_bbw}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg1_f_mss1_md_spock}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.f_msb1_flower}\"",
			case_loggy.output
		)





		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.d_msb2_w}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg2_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg2_f_mss1_md_lizzard}\"",
			case_loggy.output
		)




		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg3_d_mss1_md_d_mirror}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.tg3_d_mss1_c_bbw}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.d_msb3_a}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed twig \"{self.d_msb3_t}\"",
			case_loggy.output
		)
		self.assertNotIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.f_msb3_almost}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_lizzard}\"",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:touch_flourish:Trimmed leaf \"{self.tg3_f_mss1_md_spock}\"",
			case_loggy.output
		)


		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		# First bough extra
		self.assertFalse(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_spock))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bbw))


		# First sprout second bough
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		# Second bough extra
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_lizzard))
		self.assertTrue(os.path.isfile(self.tg2_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_d_mirror))
		self.assertTrue(os.path.isdir(self.tg2_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb2_w))


		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg3_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		# Third bough extra
		self.assertFalse(os.path.isfile(self.f_msb3_almost))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_lizzard))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_spock))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_d_mirror))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bbw))
		self.assertFalse(os.path.isdir(self.d_msb3_a))
		self.assertFalse(os.path.isdir(self.d_msb3_t))








if __name__ == "__main__" : unittest.main(verbosity=2)







