import	os
import	unittest
from	time								import sleep
from	pygwarts.tests.hagrid				import MediumSet
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.thrivables			import Copse
from	pygwarts.hagrid.sprouts				import fssprout
from	pygwarts.hagrid.planting			import Flourish
from	pygwarts.hagrid.bloom.leafs			import Rejuvenation
from	pygwarts.hagrid.planting.leafs		import LeafMove
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class SortingCase(MediumSet):

	""" Sorting of files. From source directly to the bough. """

	@classmethod
	def tearDownClass(cls):
		cls.clean(cls)

		if	cls.clean_up:
			if	os.path.isfile(cls.MEDIUM_HANDLER_11): os.remove(cls.MEDIUM_HANDLER_11)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.MEDIUM_HANDLER_11)

		cls.f_mss1_resume		= os.path.join(cls.MEDIUM_SET_SPROUT_1, "resume.docx")
		cls.f_mss1_md_grocery	= os.path.join(cls.d_mss1_md, "grocery.txt")
		cls.f_mss1_md_gc_ps		= os.path.join(cls.d_mss1_md_gc, "ps i love you.avi")
		cls.f_mss1_md_gc_h		= os.path.join(cls.d_mss1_md_gc, "something about hope.mkv")
		cls.f_mss1_c_f1			= os.path.join(cls.d_mss1_c, "foto.png")
		cls.f_mss1_c_f2			= os.path.join(cls.d_mss1_c, "foto.jpeg")

		cls.f_mss2_vinstr		= os.path.join(cls.MEDIUM_SET_SPROUT_2, "vacuum cleaner.pdf")
		cls.f_mss2_c_summer		= os.path.join(cls.d_mss2_c, "summer.jpg")
		cls.f_mss2_c_winter		= os.path.join(cls.d_mss2_c, "winter.jpg")
		cls.f_mss2_c_autumn		= os.path.join(cls.d_mss2_c, "autumn.jpg")
		cls.f_mss2_c_spring		= os.path.join(cls.d_mss2_c, "spring.jpg")

		cls.f_mss3_k_fdesc		= os.path.join(cls.d_mss3_k, "fridge.pdf")
		cls.f_mss3_k_odesc		= os.path.join(cls.d_mss3_k, "oven.pdf")
		cls.f_mss3_k_t_crumf1	= os.path.join(cls.d_mss3_k_t, "crumb.png")
		cls.f_mss3_k_t_crumf2	= os.path.join(cls.d_mss3_k_t, "crumb2.png")
		cls.f_mss3_k_t_crumv1	= os.path.join(cls.d_mss3_k_t, "holy crumb.mp4")
		cls.f_mss3_k_t_crumv2	= os.path.join(cls.d_mss3_k_t, "holy crumb2.mp4")

		cls.fmake(cls, cls.f_mss1_resume, "ready to work!")
		cls.fmake(cls, cls.f_mss1_md_grocery, "milk, meat, bread")
		cls.fmake(cls, cls.f_mss1_md_gc_ps, "she might not love it")
		cls.fmake(cls, cls.f_mss1_md_gc_h, "can't even recall name")
		cls.fmake(cls, cls.f_mss1_c_f1, "me")
		cls.fmake(cls, cls.f_mss1_c_f2, "not me")

		cls.fmake(cls, cls.f_mss2_vinstr, "how to use it")
		cls.fmake(cls, cls.f_mss2_c_summer, "summer")
		cls.fmake(cls, cls.f_mss2_c_winter, "winter")
		cls.fmake(cls, cls.f_mss2_c_autumn, "autumn")
		cls.fmake(cls, cls.f_mss2_c_spring, "spring")

		cls.fmake(cls, cls.f_mss3_k_fdesc, "the fridge")
		cls.fmake(cls, cls.f_mss3_k_odesc, "the oven")
		cls.fmake(cls, cls.f_mss3_k_t_crumf1, "crumb1 is lit")
		cls.fmake(cls, cls.f_mss3_k_t_crumf2, "crumb2 is litter")
		cls.fmake(cls, cls.f_mss3_k_t_crumv1, "why lit")
		cls.fmake(cls, cls.f_mss3_k_t_crumv2, "why litter")

		cls.tg1_f_mss1_resume		= os.path.join(cls.MEDIUM_SET_BOUGH_1, "resume.docx")
		cls.tg1_f_mss1_md_grocery	= os.path.join(cls.MEDIUM_SET_BOUGH_1, "grocery.txt")
		cls.tg1_f_mss2_vinstr		= os.path.join(cls.MEDIUM_SET_BOUGH_1, "vacuum cleaner.pdf")
		cls.tg1_f_mss3_k_fdesc		= os.path.join(cls.MEDIUM_SET_BOUGH_1, "fridge.pdf")
		cls.tg1_f_mss3_k_odesc		= os.path.join(cls.MEDIUM_SET_BOUGH_1, "oven.pdf")

		cls.tg2_f_mss1_md_gc_ps		= os.path.join(cls.MEDIUM_SET_BOUGH_3, "ps i love you.avi")
		cls.tg2_f_mss1_md_gc_h		= os.path.join(cls.MEDIUM_SET_BOUGH_3, "something about hope.mkv")
		cls.tg2_f_mss3_k_t_crumv1	= os.path.join(cls.MEDIUM_SET_BOUGH_3, "holy crumb.mp4")
		cls.tg2_f_mss3_k_t_crumv2	= os.path.join(cls.MEDIUM_SET_BOUGH_3, "holy crumb2.mp4")

		cls.tg3_f_mss2_c_summer		= os.path.join(cls.MEDIUM_SET_BOUGH_2, "summer.jpg")
		cls.tg3_f_mss2_c_winter		= os.path.join(cls.MEDIUM_SET_BOUGH_2, "winter.jpg")
		cls.tg3_f_mss2_c_autumn		= os.path.join(cls.MEDIUM_SET_BOUGH_2, "autumn.jpg")
		cls.tg3_f_mss2_c_spring		= os.path.join(cls.MEDIUM_SET_BOUGH_2, "spring.jpg")
		cls.tg3_f_mss1_c_f1			= os.path.join(cls.MEDIUM_SET_BOUGH_2, "foto.png")
		cls.tg3_f_mss1_c_f2			= os.path.join(cls.MEDIUM_SET_BOUGH_2, "foto.jpeg")
		cls.tg3_f_mss3_k_t_crumf1	= os.path.join(cls.MEDIUM_SET_BOUGH_2, "crumb.png")
		cls.tg3_f_mss3_k_t_crumf2	= os.path.join(cls.MEDIUM_SET_BOUGH_2, "crumb2.png")

	def setUp(self):
		class Forest(Copse):

			class loggy(LibraryContrib):

				handler		= self.MEDIUM_HANDLER_11
				init_level	= 10

			class First(Tree):

				bough = self.MEDIUM_SET_BOUGH_1
				class leafs(SiftingController): include = r".+\.(docx?|txt|pdf)$",

			class Second(Tree):

				bough = self.MEDIUM_SET_BOUGH_2
				class leafs(SiftingController): include = r".+\.(avi|mkv|mp4)$",

			class Third(Tree):

				bough = self.MEDIUM_SET_BOUGH_3
				class leafs(SiftingController): include = r".+\.(jpe?g|png|gif)$",

			class grow(LeafMove):		pass
			class files(Rejuvenation):	pass

			@fssprout(self.MEDIUM_SET_SPROUT_3)	# Order does matter cause every sprout pack it'self
			@fssprout(self.MEDIUM_SET_SPROUT_2)	# before previous sprout, so the nearest to dispatcher
			@fssprout(self.MEDIUM_SET_SPROUT_1)	# sprout will be processed first.
			class sync(Flourish):		pass


		self.test_case = Forest




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

		self.assertTrue(os.path.isfile(self.f_mss1_resume))
		self.assertTrue(os.path.isfile(self.f_mss1_md_grocery))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_ps))
		self.assertTrue(os.path.isfile(self.f_mss1_md_gc_h))
		self.assertTrue(os.path.isfile(self.f_mss1_c_f1))
		self.assertTrue(os.path.isfile(self.f_mss1_c_f2))

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

		self.assertTrue(os.path.isfile(self.f_mss2_vinstr))
		self.assertTrue(os.path.isfile(self.f_mss2_c_summer))
		self.assertTrue(os.path.isfile(self.f_mss2_c_winter))
		self.assertTrue(os.path.isfile(self.f_mss2_c_autumn))
		self.assertTrue(os.path.isfile(self.f_mss2_c_spring))

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

		self.assertTrue(os.path.isfile(self.f_mss3_k_fdesc))
		self.assertTrue(os.path.isfile(self.f_mss3_k_odesc))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_crumf1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_crumf2))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_crumv1))
		self.assertTrue(os.path.isfile(self.f_mss3_k_t_crumv2))

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

		self.assertFalse(os.path.isfile(self.f_mss1_resume))
		self.assertFalse(os.path.isfile(self.f_mss1_md_grocery))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_ps))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_h))
		self.assertFalse(os.path.isfile(self.f_mss1_c_f1))
		self.assertFalse(os.path.isfile(self.f_mss1_c_f2))

		# Second sprout
		self.assertFalse(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		self.assertFalse(os.path.isfile(self.f_mss2_vinstr))
		self.assertFalse(os.path.isfile(self.f_mss2_c_summer))
		self.assertFalse(os.path.isfile(self.f_mss2_c_winter))
		self.assertFalse(os.path.isfile(self.f_mss2_c_autumn))
		self.assertFalse(os.path.isfile(self.f_mss2_c_spring))

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

		self.assertFalse(os.path.isfile(self.f_mss3_k_fdesc))
		self.assertFalse(os.path.isfile(self.f_mss3_k_odesc))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumf1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumf2))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumv1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumv2))

		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_resume))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_grocery))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_vinstr))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_fdesc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_odesc))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		self.assertTrue(self.tg2_f_mss1_md_gc_ps)
		self.assertTrue(self.tg2_f_mss1_md_gc_h)
		self.assertTrue(self.tg2_f_mss3_k_t_crumv1)
		self.assertTrue(self.tg2_f_mss3_k_t_crumv2)
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))
		self.assertTrue(self.tg3_f_mss2_c_summer)
		self.assertTrue(self.tg3_f_mss2_c_winter)
		self.assertTrue(self.tg3_f_mss2_c_autumn)
		self.assertTrue(self.tg3_f_mss2_c_spring)
		self.assertTrue(self.tg3_f_mss1_c_f1)
		self.assertTrue(self.tg3_f_mss1_c_f2)
		self.assertTrue(self.tg3_f_mss3_k_t_crumf1)
		self.assertTrue(self.tg3_f_mss3_k_t_crumf2)




		# First sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))


		# Second sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
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
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

		# Second sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))

		# Third sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))




		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

		# Second sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))

		# Third sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
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

		self.assertFalse(os.path.isfile(self.f_mss1_resume))
		self.assertFalse(os.path.isfile(self.f_mss1_md_grocery))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_ps))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_h))
		self.assertFalse(os.path.isfile(self.f_mss1_c_f1))
		self.assertFalse(os.path.isfile(self.f_mss1_c_f2))

		# Second sprout
		self.assertFalse(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		self.assertFalse(os.path.isfile(self.f_mss2_vinstr))
		self.assertFalse(os.path.isfile(self.f_mss2_c_summer))
		self.assertFalse(os.path.isfile(self.f_mss2_c_winter))
		self.assertFalse(os.path.isfile(self.f_mss2_c_autumn))
		self.assertFalse(os.path.isfile(self.f_mss2_c_spring))

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

		self.assertFalse(os.path.isfile(self.f_mss3_k_fdesc))
		self.assertFalse(os.path.isfile(self.f_mss3_k_odesc))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumf1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumf2))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumv1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumv2))

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

		self.assertFalse(os.path.isfile(self.f_mss1_resume))
		self.assertFalse(os.path.isfile(self.f_mss1_md_grocery))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_ps))
		self.assertFalse(os.path.isfile(self.f_mss1_md_gc_h))
		self.assertFalse(os.path.isfile(self.f_mss1_c_f1))
		self.assertFalse(os.path.isfile(self.f_mss1_c_f2))

		# Second sprout
		self.assertFalse(os.path.isfile(self.f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.f_mss2_explangraph))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardcleaning))
		self.assertTrue(os.path.isfile(self.f_mss2_c_hardwashing))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumcooking))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumhomework))
		self.assertTrue(os.path.isfile(self.f_mss2_c_mediumphysicals))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyprocrastinating))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyreflections))
		self.assertTrue(os.path.isfile(self.f_mss2_c_easyphilosophizing))

		self.assertFalse(os.path.isfile(self.f_mss2_vinstr))
		self.assertFalse(os.path.isfile(self.f_mss2_c_summer))
		self.assertFalse(os.path.isfile(self.f_mss2_c_winter))
		self.assertFalse(os.path.isfile(self.f_mss2_c_autumn))
		self.assertFalse(os.path.isfile(self.f_mss2_c_spring))

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

		self.assertFalse(os.path.isfile(self.f_mss3_k_fdesc))
		self.assertFalse(os.path.isfile(self.f_mss3_k_odesc))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumf1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumf2))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumv1))
		self.assertFalse(os.path.isfile(self.f_mss3_k_t_crumv2))

		# First bough
		self.assertTrue(os.path.isfile(self.f_msb1_flower))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_resume))
		self.assertTrue(os.path.isfile(self.tg1_f_mss1_md_grocery))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_vinstr))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_fdesc))
		self.assertTrue(os.path.isfile(self.tg1_f_mss3_k_odesc))
		# Second bough
		self.assertTrue(os.path.isdir(self.d_msb2_w))
		self.assertTrue(self.tg2_f_mss1_md_gc_ps)
		self.assertTrue(self.tg2_f_mss1_md_gc_h)
		self.assertTrue(self.tg2_f_mss3_k_t_crumv1)
		self.assertTrue(self.tg2_f_mss3_k_t_crumv2)
		# Third bough
		self.assertTrue(os.path.isfile(self.f_msb3_almost))
		self.assertTrue(os.path.isdir(self.d_msb3_a))
		self.assertTrue(os.path.isdir(self.d_msb3_t))
		self.assertTrue(self.tg3_f_mss2_c_summer)
		self.assertTrue(self.tg3_f_mss2_c_winter)
		self.assertTrue(self.tg3_f_mss2_c_autumn)
		self.assertTrue(self.tg3_f_mss2_c_spring)
		self.assertTrue(self.tg3_f_mss1_c_f1)
		self.assertTrue(self.tg3_f_mss1_c_f2)
		self.assertTrue(self.tg3_f_mss3_k_t_crumf1)
		self.assertTrue(self.tg3_f_mss3_k_t_crumf2)




		# First sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg1_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg1_f_mss1_md_gc_onion))


		# Second sprout first bough
		self.assertFalse(os.path.isdir(self.tg1_d_mss2_c))
		self.assertTrue(os.path.isfile(self.tg1_f_mss2_tasksschedule))
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
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg1_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg1_f_mss3_k_t_bc_crumb69))




		# First sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg2_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg2_f_mss1_md_gc_onion))

		# Second sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_tasksschedule))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg2_f_mss2_c_easyphilosophizing))

		# Third sprout second bough
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_o))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_t))
		self.assertFalse(os.path.isdir(self.tg2_d_mss3_k_t_bc))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_milk))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_cheese))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_f_meat))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_o_chicken))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_o_pie))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_bread))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb1))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb2))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb420))
		self.assertFalse(os.path.isfile(self.tg2_f_mss3_k_t_bc_crumb69))




		# First sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_md_gc))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_good))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_bad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_notnot))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badbad))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_badgood))
		self.assertFalse(os.path.isdir(self.tg3_d_mss1_c_goodbad))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_rock))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_paper))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_scissors))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_sadmovies))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_dumbasses))
		self.assertFalse(os.path.isfile(self.tg3_f_mss1_md_gc_onion))

		# Second sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss2_c))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_tasksschedule))
		self.assertTrue(os.path.isfile(self.tg3_f_mss2_explangraph))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardcleaning))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_hardwashing))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumcooking))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumhomework))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_mediumphysicals))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyprocrastinating))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyreflections))
		self.assertFalse(os.path.isfile(self.tg3_f_mss2_c_easyphilosophizing))

		# Third sprout third bough
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_f))
		self.assertFalse(os.path.isdir(self.tg3_d_mss3_k_o))
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







