import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.shelve				import LibraryShelf
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.twigs			import Germination
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.planting.leafs		import LeafGrowth
from	pygwarts.hagrid.planting.leafs		import LeafMove
from	pygwarts.hagrid.planting.twigs		import TwigThrive
from	pygwarts.hagrid.planting.peels		import GrowingPeel
from	pygwarts.hagrid.planting.peels		import ThrivingPeel
from	pygwarts.hagrid.planting.peeks		import BlindPeek
from	pygwarts.hagrid.planting.peeks		import DraftPeek
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class FirstCase(MediumSet):

	"""
		GrowingPeel or ThrivingPeel, DraftPeek or BlindPeek, some Germination -> Rejuvenation,
		regular or moving grows
		Triple sprout copse
		Triple bough copse
	"""


	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_1): os.remove(cls.MEDIUM_HANDLER_1)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_1)

	def setUp(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_1
				init_level	= 10

			class TwoMain(Copse):

				class First(Tree):	bough = self.MEDIUM_SET_BOUGH_1		# This one must take all files
				class Second(Tree):	bough = self.MEDIUM_SET_BOUGH_3		# This one must have nothing left

				@GrowingPeel
				class thrive(TwigThrive):	pass
				class folders(Germination):	pass
				class leafs(SiftingController):
					include	= (

						( f"{self.MEDIUM_SET_SPROUT_1}/.+", f"{self.MEDIUM_SET_SPROUT_3}/.+" )
						if os.name == "posix" else
						(
							self.MEDIUM_SET_SPROUT_1.replace("\\","\\\\") + r"\\.+",
							self.MEDIUM_SET_SPROUT_3.replace("\\","\\\\") + r"\\.+"
						)
					)

			class Third(Tree):

				bough	= self.MEDIUM_SET_BOUGH_2
				@ThrivingPeel("weeds", to_peak=False)
				@BlindPeek("seeds", renew=False)
				class grow(LeafGrowth):		pass
				class seeds(LibraryShelf):

					grabbing	= self.MEDIUM_SET_SEEDS
					reclaiming	= self.MEDIUM_SET_SEEDS

			@GrowingPeel
			@DraftPeek(renew=False)
			class grow(LeafMove):			pass
			class files(Rejuvenation):		pass

			@fssprout(self.MEDIUM_SET_SPROUT_3)	# Order does matter cause every sprout pack it'self
			@fssprout(self.MEDIUM_SET_SPROUT_2)	# before previous sprout, so the nearest to dispatcher
			@fssprout(self.MEDIUM_SET_SPROUT_1)	# sprout will be processed first.
			class sync(Flourish):
				class twigs(SiftingController):
					exclude	= ( rf".+/table$", ) if os.name == "posix" else ( rf".+\\table$", )


		self.test_case = Forest


	def fthriving(self, dst :str) -> str :

		"""
			Makes destination file path according to hardcoded thriving
		"""

		return	os.path.join(
			self.MEDIUM_SET_BOUGH_2, "weeds", os.path.relpath(dst, self.MEDIUM_SET_BOUGH_2)
		)




	def test_first_flourish(self):

		self.test_case.loggy.init_name = "first_flourish"
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_1))
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_2))
		self.assertTrue(os.path.isdir(self.MEDIUM_SET_BOUGH_3))


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

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))


		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("first_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)




		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))


		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))

		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_md)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_md_gc)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_good)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notgood)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_bad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notbad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notnot)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_badbad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_badgood)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_goodbad)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_rock)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_paper)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_scissors)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_sadmovies)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_dumbasses)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_onion)))

		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.fthriving(self.tg2_d_mss2_c)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_tasksschedule)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_explangraph)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_hardcleaning)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_hardwashing)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumcooking)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumhomework)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumphysicals)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyprocrastinating)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyreflections)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyphilosophizing)))

		# Third sprout second bough
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_f)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_o)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_t)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_t_bc)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_milk)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_cheese)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_meat)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_o_chicken)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_o_pie)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_bread)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb1)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb2)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb420)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb69)))


		# Seeds for second bough
		self.assertEqual(len(self.test_case.Third.seeds()), 10)
		FirstCase.s_f_mss2_tasksschedule = self.test_case.Third.seeds()[
			self.f_mss2_tasksschedule
		]
		FirstCase.s_f_mss2_explangraph = self.test_case.Third.seeds()[
			self.f_mss2_explangraph
		]
		FirstCase.s_f_mss2_c_hardcleaning = self.test_case.Third.seeds()[
			self.f_mss2_c_hardcleaning
		]
		FirstCase.s_f_mss2_c_hardwashing = self.test_case.Third.seeds()[
			self.f_mss2_c_hardwashing
		]
		FirstCase.s_f_mss2_c_mediumcooking = self.test_case.Third.seeds()[
			self.f_mss2_c_mediumcooking
		]
		FirstCase.s_f_mss2_c_mediumhomework = self.test_case.Third.seeds()[
			self.f_mss2_c_mediumhomework
		]
		FirstCase.s_f_mss2_c_mediumphysicals = self.test_case.Third.seeds()[
			self.f_mss2_c_mediumphysicals
		]
		FirstCase.s_f_mss2_c_easyprocrastinating = self.test_case.Third.seeds()[
			self.f_mss2_c_easyprocrastinating
		]
		FirstCase.s_f_mss2_c_easyreflections = self.test_case.Third.seeds()[
			self.f_mss2_c_easyreflections
		]
		FirstCase.s_f_mss2_c_easyphilosophizing = self.test_case.Third.seeds()[
			self.f_mss2_c_easyphilosophizing
		]
		self.assertIsInstance(FirstCase.s_f_mss2_tasksschedule, int)
		self.assertIsInstance(FirstCase.s_f_mss2_explangraph, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_hardcleaning, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_hardwashing, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_mediumcooking, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_mediumhomework, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_mediumphysicals, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_easyprocrastinating, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_easyreflections, int)
		self.assertIsInstance(FirstCase.s_f_mss2_c_easyphilosophizing, int)





		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))

		# Third sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
















	def test_no_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "no_touch_flourish"


		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))


		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("no_touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)




		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))


		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))

		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_md)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_md_gc)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_good)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notgood)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_bad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notbad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notnot)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_badbad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_badgood)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_goodbad)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_rock)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_paper)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_scissors)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_sadmovies)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_dumbasses)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_onion)))

		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.fthriving(self.tg2_d_mss2_c)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_tasksschedule)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_explangraph)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_hardcleaning)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_hardwashing)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumcooking)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumhomework)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumphysicals)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyprocrastinating)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyreflections)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyphilosophizing)))

		# Third sprout second bough
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_f)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_o)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_t)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_t_bc)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_milk)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_cheese)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_meat)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_o_chicken)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_o_pie)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_bread)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb1)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb2)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb420)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb69)))


		# Seeds for second bough
		self.assertEqual(len(self.test_case.Third.seeds()), 10)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_tasksschedule],
			FirstCase.s_f_mss2_tasksschedule
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_explangraph],
			FirstCase.s_f_mss2_explangraph
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_hardcleaning],
			FirstCase.s_f_mss2_c_hardcleaning
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_hardwashing],
			FirstCase.s_f_mss2_c_hardwashing
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_mediumcooking],
			FirstCase.s_f_mss2_c_mediumcooking
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_mediumhomework],
			FirstCase.s_f_mss2_c_mediumhomework
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_mediumphysicals],
			FirstCase.s_f_mss2_c_mediumphysicals
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_easyprocrastinating],
			FirstCase.s_f_mss2_c_easyprocrastinating
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_easyreflections],
			FirstCase.s_f_mss2_c_easyreflections
		)
		self.assertEqual(

			self.test_case.Third.seeds()[self.f_mss2_c_easyphilosophizing],
			FirstCase.s_f_mss2_c_easyphilosophizing
		)




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))

		# Third sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))
















	def test_touch_flourish(self):

		sleep(1.1)
		self.test_case.loggy.init_name = "touch_flourish"
		self.fmake(self.f_mss2_tasksschedule, "1. get up\n2. get sad")
		self.fmake(self.f_mss2_explangraph, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
		self.fmake(self.f_mss2_c_hardcleaning, "especially vacuum")
		self.fmake(self.f_mss2_c_hardwashing, "dishes so dishes")
		self.fmake(self.f_mss2_c_mediumcooking, "who do you think i am, a chemist?")
		self.fmake(self.f_mss2_c_mediumhomework, "my son homework, ofcourse")
		self.fmake(self.f_mss2_c_mediumphysicals, "what the flip is that?")
		self.fmake(self.f_mss2_c_easyprocrastinating, "the easiest thing ever")
		self.fmake(self.f_mss2_c_easyreflections, "litlle harder but still easy")
		self.fmake(self.f_mss2_c_easyphilosophizing, "not easy at all, but why not")


		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))


		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		with self.assertLogs("touch_flourish", 10) as case_loggy:

			self.test_case = self.test_case()
			self.test_case.sync()




		self.no_loggy_levels(case_loggy.output, 30,40,50)




		# First sprout
		self.assertFalse(os.path.isfile(self.f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_onion))
		self.assertTrue(os.path.isdir(self.d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.d_mss1_c_goodbad))

		# Second sprout
		self.assertTrue(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		# Third sprout
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.f_mss3_k_o_pie))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_bread))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb420))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_bc_crumb69))


		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))




		# First sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_gc_onion))

		# Second sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg1_f_mss2_c_easyphilosophizing))

		# Third sprout first bough
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_md)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_md_gc)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_good)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notgood)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_bad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notbad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_notnot)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_badbad)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_badgood)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss1_c_goodbad)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_rock)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_paper)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_scissors)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_sadmovies)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_dumbasses)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss1_md_gc_onion)))

		# Second sprout second bough
		self.assertTrue(os.path.isdir(self.fthriving(self.tg2_d_mss2_c)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_tasksschedule)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_explangraph)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_hardcleaning)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_hardwashing)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumcooking)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumhomework)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_mediumphysicals)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyprocrastinating)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyreflections)))
		self.assertTrue(os.path.isfile(self.fthriving(self.tg2_f_mss2_c_easyphilosophizing)))

		# Third sprout second bough
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_f)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_o)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_t)))
		self.assertFalse(os.path.isdir(self.fthriving(self.tg2_d_mss3_k_t_bc)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_milk)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_cheese)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_f_meat)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_o_chicken)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_o_pie)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_bread)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb1)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb2)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb420)))
		self.assertFalse(os.path.isfile(self.fthriving(self.tg2_f_mss3_k_t_bc_crumb69)))


		# Seeds for second bough
		self.assertEqual(len(self.test_case.Third.seeds()), 10)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_tasksschedule],
			FirstCase.s_f_mss2_tasksschedule
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_explangraph],
			FirstCase.s_f_mss2_explangraph
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_hardcleaning],
			FirstCase.s_f_mss2_c_hardcleaning
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_hardwashing],
			FirstCase.s_f_mss2_c_hardwashing
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_mediumcooking],
			FirstCase.s_f_mss2_c_mediumcooking
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_mediumhomework],
			FirstCase.s_f_mss2_c_mediumhomework
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_mediumphysicals],
			FirstCase.s_f_mss2_c_mediumphysicals
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_easyprocrastinating],
			FirstCase.s_f_mss2_c_easyprocrastinating
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_easyreflections],
			FirstCase.s_f_mss2_c_easyreflections
		)
		self.assertGreater(

			self.test_case.Third.seeds()[self.f_mss2_c_easyphilosophizing],
			FirstCase.s_f_mss2_c_easyphilosophizing
		)




		# First sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertTrue(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

		# Second sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))

		# Third sprout third bough
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertTrue(os.path.isdir(self.tg3_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg3_f_mss3_k_t_bc_crumb69))








if __name__ == "__main__" : unittest.main(verbosity=2)







