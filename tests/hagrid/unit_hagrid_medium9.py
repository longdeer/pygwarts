import	os
import	unittest
from	time								import sleep
from	shutil								import rmtree
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peeks		import DraftPeek
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class IntergrowthCase(MediumSet):

	"""
		Intergrowth scheme when there are two flourish with vice versa sprout and bough
	"""

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_9): os.remove(cls.MEDIUM_HANDLER_9)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_9)
		cls.mss1_flower = os.path.join(cls.MEDIUM_SET_SPROUT_1, os.path.basename(cls.f_msb1_flower))


	def test_separated_walks(self):
		class Sakura(Tree):

			bough	= self.MEDIUM_SET_BOUGH_1
			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_9
				init_name	= "Intergrowth-1"

			@GrowingPeel
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class walk(Flourish):		pass

		class Sequoia(Tree):

			bough	= self.MEDIUM_SET_SPROUT_1
			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_9
				init_name	= "Intergrowth-2"

			@GrowingPeel
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.MEDIUM_SET_BOUGH_1)
			class walk(Flourish):		pass


		if	not os.path.isfile(self.f_mss1_md_rock):			self.fmake(self.f_mss1_md_rock)
		if	not os.path.isfile(self.f_mss1_md_paper):			self.fmake(self.f_mss1_md_paper)
		if	not os.path.isfile(self.f_mss1_md_scissors):		self.fmake(self.f_mss1_md_scissors)
		if	not os.path.isfile(self.f_mss1_md_gc_sadmovies):	self.fmake(self.f_mss1_md_gc_sadmovies)
		if	not os.path.isfile(self.f_mss1_md_gc_dumbasses):	self.fmake(self.f_mss1_md_gc_dumbasses)
		if	not os.path.isfile(self.f_mss1_md_gc_dumbasses):	self.fmake(self.f_mss1_md_gc_dumbasses)
		if	os.path.isdir(self.tg1_d_mss1_md_gc):				rmtree(self.tg1_d_mss1_md_gc)
		if	os.path.isdir(self.d_mss1_c_good):					rmtree(self.d_mss1_c_good)
		if	os.path.isdir(self.d_mss1_c_notgood):				rmtree(self.d_mss1_c_notgood)
		if	not os.path.isdir(self.d_mss1_c_bad):				os.makedirs(self.d_mss1_c_bad)
		if	not os.path.isdir(self.d_mss1_c_notbad):			os.makedirs(self.d_mss1_c_notbad)
		if	not os.path.isdir(self.d_mss1_c_notnot):			os.makedirs(self.d_mss1_c_notnot)
		if	not os.path.isdir(self.d_mss1_c_badbad):			os.makedirs(self.d_mss1_c_badbad)
		if	not os.path.isdir(self.d_mss1_c_badgood):			os.makedirs(self.d_mss1_c_badgood)
		if	not os.path.isdir(self.d_mss1_c_goodbad):			os.makedirs(self.d_mss1_c_goodbad)

		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		if	os.path.isfile(self.tg1_f_mss1_md_rock):			os.remove(self.tg1_f_mss1_md_rock)
		if	os.path.isfile(self.tg1_f_mss1_md_paper):			os.remove(self.tg1_f_mss1_md_paper)
		if	os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies):	os.remove(self.tg1_f_mss1_md_gc_sadmovies)
		if	os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses):	os.remove(self.tg1_f_mss1_md_gc_dumbasses)
		if	os.path.isfile(self.tg1_f_mss1_md_gc_onion):		os.remove(self.tg1_f_mss1_md_gc_onion)
		if	not os.path.isdir(self.tg1_d_mss1_c_good):			os.makedirs(self.tg1_d_mss1_c_good)
		if	not os.path.isdir(self.tg1_d_mss1_c_notgood):		os.makedirs(self.tg1_d_mss1_c_notgood)
		if	not os.path.isfile(self.tg1_f_mss1_md_scissors):	self.fmake(self.tg1_f_mss1_md_scissors)
		if	os.path.isdir(self.tg1_d_mss1_c_bad):				rmtree(self.tg1_d_mss1_c_bad)
		if	os.path.isdir(self.tg1_d_mss1_c_notbad):			rmtree(self.tg1_d_mss1_c_notbad)
		if	os.path.isdir(self.tg1_d_mss1_c_notnot):			rmtree(self.tg1_d_mss1_c_notnot)
		if	os.path.isdir(self.tg1_d_mss1_c_badbad):			rmtree(self.tg1_d_mss1_c_badbad)
		if	os.path.isdir(self.tg1_d_mss1_c_badgood):			rmtree(self.tg1_d_mss1_c_badgood)
		if	os.path.isdir(self.tg1_d_mss1_c_goodbad):			rmtree(self.tg1_d_mss1_c_goodbad)

		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.f_msb1_flower))


		with self.assertLogs("Intergrowth-1", 20) as case_loggy:

			self.test_case = Sakura()
			self.test_case.walk()

		self.assertCountEqual(
			case_loggy.output,
			[
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_md_gc}\"",
				f"INFO:Intergrowth-1:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
				f"INFO:Intergrowth-1:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_c_notnot}\"",
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_c_bad}\"",
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_c_notbad}\"",
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_c_badbad}\"",
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_c_badgood}\"",
				f"INFO:Intergrowth-1:Thrived twig \"{self.tg1_d_mss1_c_goodbad}\"",
				f"INFO:Intergrowth-1:Grown leaf \"{self.tg1_f_mss1_md_gc_dumbasses}\"",
				f"INFO:Intergrowth-1:Grown leaf \"{self.tg1_f_mss1_md_gc_sadmovies}\"",
				f"INFO:Intergrowth-1:Grown leaf \"{self.tg1_f_mss1_md_gc_onion}\"",
			]
		)


		with self.assertLogs("Intergrowth-2", 20) as case_loggy:

			self.test_case.loggy.close()
			self.test_case = Sequoia()
			self.test_case.walk()

		self.assertCountEqual(
			case_loggy.output,
			[
				f"INFO:Intergrowth-2:Grown leaf \"{self.mss1_flower}\"",
				f"INFO:Intergrowth-2:Thrived twig \"{self.d_mss1_c_good}\"",
				f"INFO:Intergrowth-2:Thrived twig \"{self.d_mss1_c_notgood}\"",
			]
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
		self.assertTrue(os.path.isfile(self.f_msb1_flower))








	def test_single_walk(self):

		class Forest(Copse):
			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_9
				init_name	= "Intergrowth"

			class Sakura(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController):

					include = (

						( rf"{self.MEDIUM_SET_SPROUT_1}/.+", )
						if os.name == "posix" else
						( self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+", )
					)
				class twigs(SiftingController):

					include = (

						( rf"{self.MEDIUM_SET_SPROUT_1}/.+", )
						if os.name == "posix" else
						( self.MEDIUM_SET_SPROUT_1.replace("\\", "\\\\") + r"\\.+", )
					)

			class Sequoia(Tree):

				bough = self.MEDIUM_SET_SPROUT_1
				class leafs(SiftingController):

					include = (

						( rf"{self.MEDIUM_SET_BOUGH_1}/.+", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+", )
					)
				class twigs(SiftingController):

					include = (

						( rf"{self.MEDIUM_SET_BOUGH_1}/.+", )
						if os.name == "posix" else
						( self.MEDIUM_SET_BOUGH_1.replace("\\", "\\\\") + r"\\.+", )
					)

			@GrowingPeel
			class thrive(TwigThrive):	pass
			class folders(Germination):	pass

			# DraftPeek comparator mitigates the effect when rejuved folder becomes a sprout and
			# files seams to be newer then thier last sources, so one hour (for example) gap
			# must ensure there'll be no rewriting
			@GrowingPeel
			@DraftPeek(renew=False, comparator=(lambda F,S : 360 <(F -S)))
			class grow(LeafGrowth):		pass
			class files(Rejuvenation):	pass

			# Basically it might be two separated Flourish objects in one Copse or for different Trees.
			# Basically.
			@fssprout(self.MEDIUM_SET_BOUGH_1)
			@fssprout(self.MEDIUM_SET_SPROUT_1)
			class walk(Flourish):		pass


		self.clean()


		if	not os.path.isfile(self.f_mss1_md_rock):			self.fmake(self.f_mss1_md_rock)
		if	not os.path.isfile(self.f_mss1_md_paper):			self.fmake(self.f_mss1_md_paper)
		if	not os.path.isfile(self.f_mss1_md_scissors):		self.fmake(self.f_mss1_md_scissors)
		if	not os.path.isfile(self.f_mss1_md_gc_sadmovies):	self.fmake(self.f_mss1_md_gc_sadmovies)
		if	not os.path.isfile(self.f_mss1_md_gc_dumbasses):	self.fmake(self.f_mss1_md_gc_dumbasses)
		if	not os.path.isfile(self.f_mss1_md_gc_onion):		self.fmake(self.f_mss1_md_gc_onion)
		if	os.path.isdir(self.tg1_d_mss1_md_gc):				rmtree(self.tg1_d_mss1_md_gc)
		if	os.path.isdir(self.d_mss1_c_good):					rmtree(self.d_mss1_c_good)
		if	os.path.isdir(self.d_mss1_c_notgood):				rmtree(self.d_mss1_c_notgood)
		if	not os.path.isdir(self.d_mss1_c_bad):				os.makedirs(self.d_mss1_c_bad)
		if	not os.path.isdir(self.d_mss1_c_notbad):			os.makedirs(self.d_mss1_c_notbad)
		if	not os.path.isdir(self.d_mss1_c_notnot):			os.makedirs(self.d_mss1_c_notnot)
		if	not os.path.isdir(self.d_mss1_c_badbad):			os.makedirs(self.d_mss1_c_badbad)
		if	not os.path.isdir(self.d_mss1_c_badgood):			os.makedirs(self.d_mss1_c_badgood)
		if	not os.path.isdir(self.d_mss1_c_goodbad):			os.makedirs(self.d_mss1_c_goodbad)

		# First sprout
		self.assertTrue(os.path.isfile(self.f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertFalse(os.path.isdir(self.d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))


		sleep(1.1)


		if	os.path.isfile(self.tg1_f_mss1_md_rock):			os.remove(self.tg1_f_mss1_md_rock)
		if	os.path.isfile(self.tg1_f_mss1_md_paper):			os.remove(self.tg1_f_mss1_md_paper)
		if	os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies):	os.remove(self.tg1_f_mss1_md_gc_sadmovies)
		if	os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses):	os.remove(self.tg1_f_mss1_md_gc_dumbasses)
		if	os.path.isfile(self.tg1_f_mss1_md_gc_onion):		os.remove(self.tg1_f_mss1_md_gc_onion)
		if	not os.path.isdir(self.tg1_d_mss1_c_good):			os.makedirs(self.tg1_d_mss1_c_good)
		if	not os.path.isdir(self.tg1_d_mss1_c_notgood):		os.makedirs(self.tg1_d_mss1_c_notgood)
		if	not os.path.isfile(self.tg1_f_mss1_md_scissors):	self.fmake(self.tg1_f_mss1_md_scissors)
		if	os.path.isdir(self.tg1_d_mss1_c_bad):				rmtree(self.tg1_d_mss1_c_bad)
		if	os.path.isdir(self.tg1_d_mss1_c_notbad):			rmtree(self.tg1_d_mss1_c_notbad)
		if	os.path.isdir(self.tg1_d_mss1_c_notnot):			rmtree(self.tg1_d_mss1_c_notnot)
		if	os.path.isdir(self.tg1_d_mss1_c_badbad):			rmtree(self.tg1_d_mss1_c_badbad)
		if	os.path.isdir(self.tg1_d_mss1_c_badgood):			rmtree(self.tg1_d_mss1_c_badgood)
		if	os.path.isdir(self.tg1_d_mss1_c_goodbad):			rmtree(self.tg1_d_mss1_c_goodbad)
		if	not os.path.isfile(self.f_msb1_flower):				self.fmake(self.f_msb1_flower)

		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.f_msb1_flower))


		with self.assertLogs("Intergrowth", 20) as case_loggy:

			self.test_case = Forest()
			self.test_case.walk()

		self.assertCountEqual(
			case_loggy.output,
			[
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_md_gc}\"",
				f"INFO:Intergrowth:Grown leaf \"{self.tg1_f_mss1_md_rock}\"",
				f"INFO:Intergrowth:Grown leaf \"{self.tg1_f_mss1_md_paper}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_c_notnot}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_c_bad}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_c_notbad}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_c_badbad}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_c_badgood}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.tg1_d_mss1_c_goodbad}\"",
				f"INFO:Intergrowth:Grown leaf \"{self.tg1_f_mss1_md_gc_dumbasses}\"",
				f"INFO:Intergrowth:Grown leaf \"{self.tg1_f_mss1_md_gc_sadmovies}\"",
				f"INFO:Intergrowth:Grown leaf \"{self.tg1_f_mss1_md_gc_onion}\"",
				f"INFO:Intergrowth:Grown leaf \"{self.mss1_flower}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.d_mss1_c_good}\"",
				f"INFO:Intergrowth:Thrived twig \"{self.d_mss1_c_notgood}\"",
			]
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
		self.assertTrue(os.path.isfile(self.f_msb1_flower))








if __name__ == "__main__" : unittest.main(verbosity=2)







