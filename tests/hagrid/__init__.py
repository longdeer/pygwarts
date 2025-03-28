import	os
import	shutil
from	pathlib			import Path
from	pygwarts.tests	import PygwartsTestCase








class HagridTestCase(PygwartsTestCase):

	"""
		Super class for hagrid test cases
	"""

	HAGRID_ROOT			= Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid"

	INIT_SET_BOUGH_1	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_init_dst1")
	INIT_SET_BOUGH_2	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_init_dst2")
	INIT_SET_BOUGH_3	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_init_dst3")
	INIT_SET_SPROUT		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_init_src")
	INIT_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_init.loggy")
	ORDER_SET_BOUGH_1	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_order_dst1")
	ORDER_SET_BOUGH_2	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_order_dst2")
	ORDER_SET_BOUGH_3	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_order_dst3")
	PEEL_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_peels.loggy")
	DRAFT_PEEK_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_dpeeks.loggy")
	BLIND_PEEK_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_bpeeks.loggy")
	SIFT_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_sift.loggy")
	FLOURISH_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_flou.loggy")

	EASY_SET_BOUGH		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy_dst")
	EASY_SET_SPROUT		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy_src")
	EASY_SET_SEEDS		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy.seeds")
	EASY_HANDLER_1		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy1.loggy")
	EASY_HANDLER_2		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy2.loggy")
	EASY_HANDLER_3		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy3.loggy")
	EASY_HANDLER_4		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy4.loggy")
	EASY_HANDLER_5		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy5.loggy")
	EASY_HANDLER_6		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy6.loggy")
	EASY_HANDLER_7		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy7.loggy")
	EASY_HANDLER_8		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy8.loggy")
	EASY_HANDLER_9		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy9.loggy")
	EASY_HANDLER_10		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy10.loggy")
	EASY_HANDLER_11		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy11.loggy")
	EASY_HANDLER_12		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy12.loggy")
	EASY_HANDLER_13		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy13.loggy")
	EASY_HANDLER_15		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_easy15.loggy")

	MEDIUM_SET_BOUGH_1	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium_dst1")
	MEDIUM_SET_BOUGH_2	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium_dst2")
	MEDIUM_SET_BOUGH_3	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium_dst3")
	MEDIUM_SET_SPROUT_1	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium_src1")
	MEDIUM_SET_SPROUT_2	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium_src2")
	MEDIUM_SET_SPROUT_3	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium_src3")
	MEDIUM_SET_SEEDS	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium.seeds")
	MEDIUM_HANDLER_1	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium1.loggy")
	MEDIUM_HANDLER_2	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium2.loggy")
	MEDIUM_HANDLER_3	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium3.loggy")
	MEDIUM_HANDLER_4	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium4.loggy")
	MEDIUM_HANDLER_5	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium5.loggy")
	MEDIUM_HANDLER_6	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium6.loggy")
	MEDIUM_HANDLER_7	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium7.loggy")
	MEDIUM_HANDLER_8	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium8.loggy")
	MEDIUM_HANDLER_9	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium9.loggy")
	MEDIUM_HANDLER_10	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium10.loggy")
	MEDIUM_HANDLER_11	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hagrid" /"unit_medium11.loggy")
















class EasySet(HagridTestCase):

	"""
		Super for easy cases, like single sprout and single bough
	"""

	@classmethod
	def setUpClass(cls):

		"""
			Following operation must make such a tree:
			d- EASY_SET_SPROUT
				f- WitchDoctor.txt
				d- pros
			    	f- not so good.txt
			    	f- good.txt
			    	f- good so much.txt
			    	d- redundant_folder_2
			        	f- redundant_file_2
				d- cons
					f- main.txt
					f- not_main.txt
				d- redundant_folder_1
					f- redundant_file_1
		"""

		cls.file1					= os.path.join(cls.EASY_SET_SPROUT, "WitchDoctor.txt")
		cls.pros_folder				= os.path.join(cls.EASY_SET_SPROUT, "pros")
		cls.pros_file1				= os.path.join(cls.pros_folder, "not so good.txt")
		cls.pros_file2				= os.path.join(cls.pros_folder, "good.txt")
		cls.pros_file3				= os.path.join(cls.pros_folder, "good so much.txt")
		cls.cons_folder				= os.path.join(cls.EASY_SET_SPROUT, "cons")
		cls.cons_file1				= os.path.join(cls.cons_folder, "main.txt")
		cls.cons_file2				= os.path.join(cls.cons_folder, "not_main.txt")
		cls.redundant_1_folder		= os.path.join(cls.EASY_SET_SPROUT, "redundant_folder_1")
		cls.redundant_2_folder		= os.path.join(cls.EASY_SET_SPROUT, "pros", "redundant_folder_2")
		cls.redundant_1				= os.path.join(cls.redundant_1_folder, "redundant_file_1")
		cls.redundant_2				= os.path.join(cls.redundant_2_folder, "redundant_file_2")

		cls.dst_file1				= os.path.join(cls.EASY_SET_BOUGH, "WitchDoctor.txt")
		cls.dst_pros_folder			= os.path.join(cls.EASY_SET_BOUGH, "pros")
		cls.dst_pros_file1			= os.path.join(cls.dst_pros_folder, "not so good.txt")
		cls.dst_pros_file2			= os.path.join(cls.dst_pros_folder, "good.txt")
		cls.dst_pros_file3			= os.path.join(cls.dst_pros_folder, "good so much.txt")
		cls.dst_cons_folder			= os.path.join(cls.EASY_SET_BOUGH, "cons")
		cls.dst_cons_file1			= os.path.join(cls.dst_cons_folder, "main.txt")
		cls.dst_cons_file2			= os.path.join(cls.dst_cons_folder, "not_main.txt")
		cls.dst_redundant_1_folder	= os.path.join(cls.EASY_SET_BOUGH, "redundant_folder_1")
		cls.dst_redundant_2_folder	= os.path.join(cls.EASY_SET_BOUGH, "pros", "redundant_folder_2")
		cls.dst_redundant_1			= os.path.join(cls.dst_redundant_1_folder, "redundant_file_1")
		cls.dst_redundant_2			= os.path.join(cls.dst_redundant_2_folder, "redundant_file_2")

		cls.clean(cls)
		cls.fmake(cls, cls.file1, "OOH EEH OOH AH AH TING TANG WALA WALA BING BANG")
		cls.fmake(cls, cls.pros_file1, "may be ain't best way")
		cls.fmake(cls, cls.pros_file2, "probably the best way")
		cls.fmake(cls, cls.pros_file3, "definitely the best way")

		if	not os.path.isdir(cls.EASY_SET_BOUGH):	os.makedirs(cls.EASY_SET_BOUGH)
		if	not os.path.isfile(cls.cons_file1) :	cls.fmake(cls, cls.cons_file1, "might cause a headache")
		if	not os.path.isfile(cls.cons_file2) :	cls.fmake(cls, cls.cons_file2, "annihilation")
		if	not os.path.isfile(cls.redundant_1):	cls.fmake(cls, cls.redundant_1, "no use 1")
		if	not os.path.isfile(cls.redundant_2):	cls.fmake(cls, cls.redundant_2, "no use 2")

	def clean(self):

		if	os.path.isdir(self.EASY_SET_SPROUT):			shutil.rmtree(self.EASY_SET_SPROUT)
		if	os.path.isdir(self.EASY_SET_BOUGH):				shutil.rmtree(self.EASY_SET_BOUGH)
		if	os.path.isfile(self.EASY_SET_SEEDS):			os.remove(self.EASY_SET_SEEDS)
		if	os.path.isfile(self.EASY_SET_SEEDS + ".db"):	os.remove(self.EASY_SET_SEEDS + ".db")
		if	os.path.isfile(self.EASY_SET_SEEDS + ".dat"):	os.remove(self.EASY_SET_SEEDS + ".dat")
		if	os.path.isfile(self.EASY_SET_SEEDS + ".bak"):	os.remove(self.EASY_SET_SEEDS + ".bak")
		if	os.path.isfile(self.EASY_SET_SEEDS + ".dir"):	os.remove(self.EASY_SET_SEEDS + ".dir")
















class MediumSet(HagridTestCase):

	"""
		Big tests for multi sprout/bough
	"""

	@classmethod
	def setUpClass(cls):

		"""
			d- MEDIUM_SET_SPROUT_1
				d- men due
					f- rock
					f- paper
					f- scissors
					d- girls cries
						f- sad movies
						f- dumbasses (literaly)
						f- onion					- this one to be involved
				d- commons							- collection of empty folders to test Germination
					d- good
					d- not good
					d- bad
					d- not bad
					d- not not
					d- bad bad
					d- bad good
					d- good bad
			d- MEDIUM_SET_SPROUT_2
				f- tasks schedule.txt
				f- ex.plan graph.png
				d- chores
					f- hard-cleaning.task
					f- hard-washing.task
					f- medium-cooking.task
					f- medium-homework.task
					f- medium-physicals.task
					f- easy-procrastinating.task
					f- easy-reflections.task
					f- easy-philosophizing.task
			d- MEDIUM_SET_SPROUT_3
				d- kitchen
					d- fridge
						f- milk
						f- cheese
						f- meat
					d- oven
						f- chicken
						f- pie
					d- table
						d- bread container
							f- bread
							f- crumb1
							f- crumb2
							f- crumb420				- this two crumbs are looking too cool,
							f- crumb69				- so mb sift them out?
			d- MEDIUM_SET_BOUGH_1
				f- flower.weed
			d- MEDIUM_SET_BOUGH_2
				d- weeds
			d- MEDIUM_SET_BOUGH_3
				f- almost.weed						- this one must be excluded from trimming
				d- all_weeds
				d- tools							- this one must be excluded from trimming
		"""

		################################### First sprout ###################################
		cls.d_mss1_md						= os.path.join(cls.MEDIUM_SET_SPROUT_1, "men due")
		cls.f_mss1_md_rock					= os.path.join(cls.d_mss1_md, "rock")
		cls.f_mss1_md_paper					= os.path.join(cls.d_mss1_md, "paper")
		cls.f_mss1_md_scissors				= os.path.join(cls.d_mss1_md, "scissors")
		cls.d_mss1_md_gc					= os.path.join(cls.d_mss1_md, "girls cries")
		cls.f_mss1_md_gc_sadmovies			= os.path.join(cls.d_mss1_md_gc, "sad movies")
		cls.f_mss1_md_gc_dumbasses			= os.path.join(cls.d_mss1_md_gc, "dumbasses (literaly)")
		cls.f_mss1_md_gc_onion				= os.path.join(cls.d_mss1_md_gc, "onion")
		cls.d_mss1_c						= os.path.join(cls.MEDIUM_SET_SPROUT_1, "commons")
		cls.d_mss1_c_good					= os.path.join(cls.d_mss1_c, "good")
		cls.d_mss1_c_notgood				= os.path.join(cls.d_mss1_c, "not good")
		cls.d_mss1_c_bad					= os.path.join(cls.d_mss1_c, "bad")
		cls.d_mss1_c_notbad					= os.path.join(cls.d_mss1_c, "not bad")
		cls.d_mss1_c_notnot					= os.path.join(cls.d_mss1_c, "not not")
		cls.d_mss1_c_badbad					= os.path.join(cls.d_mss1_c, "bad bad")
		cls.d_mss1_c_badgood				= os.path.join(cls.d_mss1_c, "bad good")
		cls.d_mss1_c_goodbad				= os.path.join(cls.d_mss1_c, "good bad")




		################################### Second sprout ###################################
		cls.f_mss2_tasksschedule			= os.path.join(cls.MEDIUM_SET_SPROUT_2, "tasks schedule.txt")
		cls.f_mss2_explangraph				= os.path.join(cls.MEDIUM_SET_SPROUT_2, "ex.plan graph.png")
		cls.d_mss2_c						= os.path.join(cls.MEDIUM_SET_SPROUT_2, "chores")
		cls.f_mss2_c_hardcleaning			= os.path.join(cls.d_mss2_c, "hard-cleaning.task")
		cls.f_mss2_c_hardwashing			= os.path.join(cls.d_mss2_c, "hard-washing.task")
		cls.f_mss2_c_mediumcooking			= os.path.join(cls.d_mss2_c, "medium-cooking.task")
		cls.f_mss2_c_mediumhomework			= os.path.join(cls.d_mss2_c, "medium-homework.task")
		cls.f_mss2_c_mediumphysicals		= os.path.join(cls.d_mss2_c, "medium-physicals.task")
		cls.f_mss2_c_easyprocrastinating	= os.path.join(cls.d_mss2_c, "easy-procrastinating.task")
		cls.f_mss2_c_easyreflections		= os.path.join(cls.d_mss2_c, "easy-reflections.task")
		cls.f_mss2_c_easyphilosophizing		= os.path.join(cls.d_mss2_c, "easy-philosophizing.task")




		################################### Third sprout ###################################
		cls.d_mss3_k						= os.path.join(cls.MEDIUM_SET_SPROUT_3, "kitchen")
		cls.d_mss3_k_f						= os.path.join(cls.d_mss3_k, "fridge")
		cls.f_mss3_k_f_milk					= os.path.join(cls.d_mss3_k_f, "milk")
		cls.f_mss3_k_f_cheese				= os.path.join(cls.d_mss3_k_f, "cheese")
		cls.f_mss3_k_f_meat					= os.path.join(cls.d_mss3_k_f, "meat")
		cls.d_mss3_k_o						= os.path.join(cls.d_mss3_k, "oven")
		cls.f_mss3_k_o_chicken				= os.path.join(cls.d_mss3_k_o, "chicken")
		cls.f_mss3_k_o_pie					= os.path.join(cls.d_mss3_k_o, "pie")
		cls.d_mss3_k_t						= os.path.join(cls.d_mss3_k, "table")
		cls.d_mss3_k_t_bc					= os.path.join(cls.d_mss3_k_t, "bread container")
		cls.f_mss3_k_t_bc_bread				= os.path.join(cls.d_mss3_k_t_bc, "bread")
		cls.f_mss3_k_t_bc_crumb1			= os.path.join(cls.d_mss3_k_t_bc, "crumb1")
		cls.f_mss3_k_t_bc_crumb2			= os.path.join(cls.d_mss3_k_t_bc, "crumb2")
		cls.f_mss3_k_t_bc_crumb420			= os.path.join(cls.d_mss3_k_t_bc, "crumb420")
		cls.f_mss3_k_t_bc_crumb69			= os.path.join(cls.d_mss3_k_t_bc, "crumb69")




		################################### Boughs start ###################################
		cls.f_msb1_flower					= os.path.join(cls.MEDIUM_SET_BOUGH_1, "flower.weed")
		cls.d_msb2_w						= os.path.join(cls.MEDIUM_SET_BOUGH_2, "weeds")
		cls.f_msb3_almost					= os.path.join(cls.MEDIUM_SET_BOUGH_3, "almost.weed")
		cls.d_msb3_a						= os.path.join(cls.MEDIUM_SET_BOUGH_3, "all_weeds")
		cls.d_msb3_t						= os.path.join(cls.MEDIUM_SET_BOUGH_3, "tools")




		################################### First sprout first bough ###################################
		cls.tg1_d_mss1_md					= os.path.join(cls.MEDIUM_SET_BOUGH_1, "men due")
		cls.tg1_f_mss1_md_rock				= os.path.join(cls.tg1_d_mss1_md, "rock")
		cls.tg1_f_mss1_md_paper				= os.path.join(cls.tg1_d_mss1_md, "paper")
		cls.tg1_f_mss1_md_scissors			= os.path.join(cls.tg1_d_mss1_md, "scissors")
		cls.tg1_d_mss1_md_gc				= os.path.join(cls.tg1_d_mss1_md, "girls cries")
		cls.tg1_f_mss1_md_gc_sadmovies		= os.path.join(cls.tg1_d_mss1_md_gc, "sad movies")
		cls.tg1_f_mss1_md_gc_dumbasses		= os.path.join(cls.tg1_d_mss1_md_gc, "dumbasses (literaly)")
		cls.tg1_f_mss1_md_gc_onion			= os.path.join(cls.tg1_d_mss1_md_gc, "onion")
		cls.tg1_d_mss1_c					= os.path.join(cls.MEDIUM_SET_BOUGH_1, "commons")
		cls.tg1_d_mss1_c_good				= os.path.join(cls.tg1_d_mss1_c, "good")
		cls.tg1_d_mss1_c_notgood			= os.path.join(cls.tg1_d_mss1_c, "not good")
		cls.tg1_d_mss1_c_bad				= os.path.join(cls.tg1_d_mss1_c, "bad")
		cls.tg1_d_mss1_c_notbad				= os.path.join(cls.tg1_d_mss1_c, "not bad")
		cls.tg1_d_mss1_c_notnot				= os.path.join(cls.tg1_d_mss1_c, "not not")
		cls.tg1_d_mss1_c_badbad				= os.path.join(cls.tg1_d_mss1_c, "bad bad")
		cls.tg1_d_mss1_c_badgood			= os.path.join(cls.tg1_d_mss1_c, "bad good")
		cls.tg1_d_mss1_c_goodbad			= os.path.join(cls.tg1_d_mss1_c, "good bad")




		################################### Second sprout first bough ###################################
		cls.tg1_f_mss2_tasksschedule		= os.path.join(cls.MEDIUM_SET_BOUGH_1, "tasks schedule.txt")
		cls.tg1_f_mss2_explangraph			= os.path.join(cls.MEDIUM_SET_BOUGH_1, "ex.plan graph.png")
		cls.tg1_d_mss2_c					= os.path.join(cls.MEDIUM_SET_BOUGH_1, "chores")
		cls.tg1_f_mss2_c_hardcleaning		= os.path.join(cls.tg1_d_mss2_c, "hard-cleaning.task")
		cls.tg1_f_mss2_c_hardwashing		= os.path.join(cls.tg1_d_mss2_c, "hard-washing.task")
		cls.tg1_f_mss2_c_mediumcooking		= os.path.join(cls.tg1_d_mss2_c, "medium-cooking.task")
		cls.tg1_f_mss2_c_mediumhomework		= os.path.join(cls.tg1_d_mss2_c, "medium-homework.task")
		cls.tg1_f_mss2_c_mediumphysicals	= os.path.join(cls.tg1_d_mss2_c, "medium-physicals.task")
		cls.tg1_f_mss2_c_easyprocrastinating= os.path.join(cls.tg1_d_mss2_c, "easy-procrastinating.task")
		cls.tg1_f_mss2_c_easyreflections	= os.path.join(cls.tg1_d_mss2_c, "easy-reflections.task")
		cls.tg1_f_mss2_c_easyphilosophizing	= os.path.join(cls.tg1_d_mss2_c, "easy-philosophizing.task")




		################################### Third sprout first bough ###################################
		cls.tg1_d_mss3_k					= os.path.join(cls.MEDIUM_SET_BOUGH_1, "kitchen")
		cls.tg1_d_mss3_k_f					= os.path.join(cls.tg1_d_mss3_k, "fridge")
		cls.tg1_f_mss3_k_f_milk				= os.path.join(cls.tg1_d_mss3_k_f, "milk")
		cls.tg1_f_mss3_k_f_cheese			= os.path.join(cls.tg1_d_mss3_k_f, "cheese")
		cls.tg1_f_mss3_k_f_meat				= os.path.join(cls.tg1_d_mss3_k_f, "meat")
		cls.tg1_d_mss3_k_o					= os.path.join(cls.tg1_d_mss3_k, "oven")
		cls.tg1_f_mss3_k_o_chicken			= os.path.join(cls.tg1_d_mss3_k_o, "chicken")
		cls.tg1_f_mss3_k_o_pie				= os.path.join(cls.tg1_d_mss3_k_o, "pie")
		cls.tg1_d_mss3_k_t					= os.path.join(cls.tg1_d_mss3_k, "table")
		cls.tg1_d_mss3_k_t_bc				= os.path.join(cls.tg1_d_mss3_k_t, "bread container")
		cls.tg1_f_mss3_k_t_bc_bread			= os.path.join(cls.tg1_d_mss3_k_t_bc, "bread")
		cls.tg1_f_mss3_k_t_bc_crumb1		= os.path.join(cls.tg1_d_mss3_k_t_bc, "crumb1")
		cls.tg1_f_mss3_k_t_bc_crumb2		= os.path.join(cls.tg1_d_mss3_k_t_bc, "crumb2")
		cls.tg1_f_mss3_k_t_bc_crumb420		= os.path.join(cls.tg1_d_mss3_k_t_bc, "crumb420")
		cls.tg1_f_mss3_k_t_bc_crumb69		= os.path.join(cls.tg1_d_mss3_k_t_bc, "crumb69")




		################################### First sprout second bough ###################################
		cls.tg2_d_mss1_md					= os.path.join(cls.MEDIUM_SET_BOUGH_2, "men due")
		cls.tg2_f_mss1_md_rock				= os.path.join(cls.tg2_d_mss1_md, "rock")
		cls.tg2_f_mss1_md_paper				= os.path.join(cls.tg2_d_mss1_md, "paper")
		cls.tg2_f_mss1_md_scissors			= os.path.join(cls.tg2_d_mss1_md, "scissors")
		cls.tg2_d_mss1_md_gc				= os.path.join(cls.tg2_d_mss1_md, "girls cries")
		cls.tg2_f_mss1_md_gc_sadmovies		= os.path.join(cls.tg2_d_mss1_md_gc, "sad movies")
		cls.tg2_f_mss1_md_gc_dumbasses		= os.path.join(cls.tg2_d_mss1_md_gc, "dumbasses (literaly)")
		cls.tg2_f_mss1_md_gc_onion			= os.path.join(cls.tg2_d_mss1_md_gc, "onion")
		cls.tg2_d_mss1_c					= os.path.join(cls.MEDIUM_SET_BOUGH_2, "commons")
		cls.tg2_d_mss1_c_good				= os.path.join(cls.tg2_d_mss1_c, "good")
		cls.tg2_d_mss1_c_notgood			= os.path.join(cls.tg2_d_mss1_c, "not good")
		cls.tg2_d_mss1_c_bad				= os.path.join(cls.tg2_d_mss1_c, "bad")
		cls.tg2_d_mss1_c_notbad				= os.path.join(cls.tg2_d_mss1_c, "not bad")
		cls.tg2_d_mss1_c_notnot				= os.path.join(cls.tg2_d_mss1_c, "not not")
		cls.tg2_d_mss1_c_badbad				= os.path.join(cls.tg2_d_mss1_c, "bad bad")
		cls.tg2_d_mss1_c_badgood			= os.path.join(cls.tg2_d_mss1_c, "bad good")
		cls.tg2_d_mss1_c_goodbad			= os.path.join(cls.tg2_d_mss1_c, "good bad")




		################################### Second sprout second bough ###################################
		cls.tg2_f_mss2_tasksschedule		= os.path.join(cls.MEDIUM_SET_BOUGH_2, "tasks schedule.txt")
		cls.tg2_f_mss2_explangraph			= os.path.join(cls.MEDIUM_SET_BOUGH_2, "ex.plan graph.png")
		cls.tg2_d_mss2_c					= os.path.join(cls.MEDIUM_SET_BOUGH_2, "chores")
		cls.tg2_f_mss2_c_hardcleaning		= os.path.join(cls.tg2_d_mss2_c, "hard-cleaning.task")
		cls.tg2_f_mss2_c_hardwashing		= os.path.join(cls.tg2_d_mss2_c, "hard-washing.task")
		cls.tg2_f_mss2_c_mediumcooking		= os.path.join(cls.tg2_d_mss2_c, "medium-cooking.task")
		cls.tg2_f_mss2_c_mediumhomework		= os.path.join(cls.tg2_d_mss2_c, "medium-homework.task")
		cls.tg2_f_mss2_c_mediumphysicals	= os.path.join(cls.tg2_d_mss2_c, "medium-physicals.task")
		cls.tg2_f_mss2_c_easyprocrastinating= os.path.join(cls.tg2_d_mss2_c, "easy-procrastinating.task")
		cls.tg2_f_mss2_c_easyreflections	= os.path.join(cls.tg2_d_mss2_c, "easy-reflections.task")
		cls.tg2_f_mss2_c_easyphilosophizing	= os.path.join(cls.tg2_d_mss2_c, "easy-philosophizing.task")




		################################### Third sprout second bough ###################################
		cls.tg2_d_mss3_k					= os.path.join(cls.MEDIUM_SET_BOUGH_2, "kitchen")
		cls.tg2_d_mss3_k_f					= os.path.join(cls.tg2_d_mss3_k, "fridge")
		cls.tg2_f_mss3_k_f_milk				= os.path.join(cls.tg2_d_mss3_k_f, "milk")
		cls.tg2_f_mss3_k_f_cheese			= os.path.join(cls.tg2_d_mss3_k_f, "cheese")
		cls.tg2_f_mss3_k_f_meat				= os.path.join(cls.tg2_d_mss3_k_f, "meat")
		cls.tg2_d_mss3_k_o					= os.path.join(cls.tg2_d_mss3_k, "oven")
		cls.tg2_f_mss3_k_o_chicken			= os.path.join(cls.tg2_d_mss3_k_o, "chicken")
		cls.tg2_f_mss3_k_o_pie				= os.path.join(cls.tg2_d_mss3_k_o, "pie")
		cls.tg2_d_mss3_k_t					= os.path.join(cls.tg2_d_mss3_k, "table")
		cls.tg2_d_mss3_k_t_bc				= os.path.join(cls.tg2_d_mss3_k_t, "bread container")
		cls.tg2_f_mss3_k_t_bc_bread			= os.path.join(cls.tg2_d_mss3_k_t_bc, "bread")
		cls.tg2_f_mss3_k_t_bc_crumb1		= os.path.join(cls.tg2_d_mss3_k_t_bc, "crumb1")
		cls.tg2_f_mss3_k_t_bc_crumb2		= os.path.join(cls.tg2_d_mss3_k_t_bc, "crumb2")
		cls.tg2_f_mss3_k_t_bc_crumb420		= os.path.join(cls.tg2_d_mss3_k_t_bc, "crumb420")
		cls.tg2_f_mss3_k_t_bc_crumb69		= os.path.join(cls.tg2_d_mss3_k_t_bc, "crumb69")




		################################### First sprout third bough ###################################
		cls.tg3_d_mss1_md					= os.path.join(cls.MEDIUM_SET_BOUGH_3, "men due")
		cls.tg3_f_mss1_md_rock				= os.path.join(cls.tg3_d_mss1_md, "rock")
		cls.tg3_f_mss1_md_paper				= os.path.join(cls.tg3_d_mss1_md, "paper")
		cls.tg3_f_mss1_md_scissors			= os.path.join(cls.tg3_d_mss1_md, "scissors")
		cls.tg3_d_mss1_md_gc				= os.path.join(cls.tg3_d_mss1_md, "girls cries")
		cls.tg3_f_mss1_md_gc_sadmovies		= os.path.join(cls.tg3_d_mss1_md_gc, "sad movies")
		cls.tg3_f_mss1_md_gc_dumbasses		= os.path.join(cls.tg3_d_mss1_md_gc, "dumbasses (literaly)")
		cls.tg3_f_mss1_md_gc_onion			= os.path.join(cls.tg3_d_mss1_md_gc, "onion")
		cls.tg3_d_mss1_c					= os.path.join(cls.MEDIUM_SET_BOUGH_3, "commons")
		cls.tg3_d_mss1_c_good				= os.path.join(cls.tg3_d_mss1_c, "good")
		cls.tg3_d_mss1_c_notgood			= os.path.join(cls.tg3_d_mss1_c, "not good")
		cls.tg3_d_mss1_c_bad				= os.path.join(cls.tg3_d_mss1_c, "bad")
		cls.tg3_d_mss1_c_notbad				= os.path.join(cls.tg3_d_mss1_c, "not bad")
		cls.tg3_d_mss1_c_notnot				= os.path.join(cls.tg3_d_mss1_c, "not not")
		cls.tg3_d_mss1_c_badbad				= os.path.join(cls.tg3_d_mss1_c, "bad bad")
		cls.tg3_d_mss1_c_badgood			= os.path.join(cls.tg3_d_mss1_c, "bad good")
		cls.tg3_d_mss1_c_goodbad			= os.path.join(cls.tg3_d_mss1_c, "good bad")




		################################### Sceond sprout third bough ###################################
		cls.tg3_f_mss2_tasksschedule		= os.path.join(cls.MEDIUM_SET_BOUGH_3, "tasks schedule.txt")
		cls.tg3_f_mss2_explangraph			= os.path.join(cls.MEDIUM_SET_BOUGH_3, "ex.plan graph.png")
		cls.tg3_d_mss2_c					= os.path.join(cls.MEDIUM_SET_BOUGH_3, "chores")
		cls.tg3_f_mss2_c_hardcleaning		= os.path.join(cls.tg3_d_mss2_c, "hard-cleaning.task")
		cls.tg3_f_mss2_c_hardwashing		= os.path.join(cls.tg3_d_mss2_c, "hard-washing.task")
		cls.tg3_f_mss2_c_mediumcooking		= os.path.join(cls.tg3_d_mss2_c, "medium-cooking.task")
		cls.tg3_f_mss2_c_mediumhomework		= os.path.join(cls.tg3_d_mss2_c, "medium-homework.task")
		cls.tg3_f_mss2_c_mediumphysicals	= os.path.join(cls.tg3_d_mss2_c, "medium-physicals.task")
		cls.tg3_f_mss2_c_easyprocrastinating= os.path.join(cls.tg3_d_mss2_c, "easy-procrastinating.task")
		cls.tg3_f_mss2_c_easyreflections	= os.path.join(cls.tg3_d_mss2_c, "easy-reflections.task")
		cls.tg3_f_mss2_c_easyphilosophizing	= os.path.join(cls.tg3_d_mss2_c, "easy-philosophizing.task")




		################################### Third sprout third bough ###################################
		cls.tg3_d_mss3_k					= os.path.join(cls.MEDIUM_SET_BOUGH_3, "kitchen")
		cls.tg3_d_mss3_k_f					= os.path.join(cls.tg3_d_mss3_k, "fridge")
		cls.tg3_f_mss3_k_f_milk				= os.path.join(cls.tg3_d_mss3_k_f, "milk")
		cls.tg3_f_mss3_k_f_cheese			= os.path.join(cls.tg3_d_mss3_k_f, "cheese")
		cls.tg3_f_mss3_k_f_meat				= os.path.join(cls.tg3_d_mss3_k_f, "meat")
		cls.tg3_d_mss3_k_o					= os.path.join(cls.tg3_d_mss3_k, "oven")
		cls.tg3_f_mss3_k_o_chicken			= os.path.join(cls.tg3_d_mss3_k_o, "chicken")
		cls.tg3_f_mss3_k_o_pie				= os.path.join(cls.tg3_d_mss3_k_o, "pie")
		cls.tg3_d_mss3_k_t					= os.path.join(cls.tg3_d_mss3_k, "table")
		cls.tg3_d_mss3_k_t_bc				= os.path.join(cls.tg3_d_mss3_k_t, "bread container")
		cls.tg3_f_mss3_k_t_bc_bread			= os.path.join(cls.tg3_d_mss3_k_t_bc, "bread")
		cls.tg3_f_mss3_k_t_bc_crumb1		= os.path.join(cls.tg3_d_mss3_k_t_bc, "crumb1")
		cls.tg3_f_mss3_k_t_bc_crumb2		= os.path.join(cls.tg3_d_mss3_k_t_bc, "crumb2")
		cls.tg3_f_mss3_k_t_bc_crumb420		= os.path.join(cls.tg3_d_mss3_k_t_bc, "crumb420")
		cls.tg3_f_mss3_k_t_bc_crumb69		= os.path.join(cls.tg3_d_mss3_k_t_bc, "crumb69")




		cls.clean(cls)
		################################### First sprout files ###################################
		cls.fmake(cls, cls.f_mss1_md_rock, "it's about time it's about power")
		cls.fmake(cls, cls.f_mss1_md_paper, "if cut it's like the face insight is right beneath my skin")
		cls.fmake(cls, cls.f_mss1_md_scissors, "only in HD or better")
		cls.fmake(cls, cls.f_mss1_md_gc_sadmovies, "green mile, knockin' on heaven's door")
		cls.fmake(cls, cls.f_mss1_md_gc_dumbasses, "HA-HA, CLASSIC")
		cls.fmake(cls, cls.f_mss1_md_gc_onion, "makes even devil cry")
		os.makedirs(cls.d_mss1_c_good)
		os.makedirs(cls.d_mss1_c_notgood)
		os.makedirs(cls.d_mss1_c_bad)
		os.makedirs(cls.d_mss1_c_notbad)
		os.makedirs(cls.d_mss1_c_notnot)
		os.makedirs(cls.d_mss1_c_badbad)
		os.makedirs(cls.d_mss1_c_badgood)
		os.makedirs(cls.d_mss1_c_goodbad)




		################################### Second sprout files ###################################
		cls.fmake(cls, cls.f_mss2_tasksschedule, "1. get up\n2. get sad")
		cls.fmake(cls, cls.f_mss2_explangraph, "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")
		cls.fmake(cls, cls.f_mss2_c_hardcleaning, "especially vacuum")
		cls.fmake(cls, cls.f_mss2_c_hardwashing, "dishes so dishes")
		cls.fmake(cls, cls.f_mss2_c_mediumcooking, "who do you think i am, a chemist?")
		cls.fmake(cls, cls.f_mss2_c_mediumhomework, "my son homework, ofcourse")
		cls.fmake(cls, cls.f_mss2_c_mediumphysicals, "what the flip is that?")
		cls.fmake(cls, cls.f_mss2_c_easyprocrastinating, "the easiest thing ever")
		cls.fmake(cls, cls.f_mss2_c_easyreflections, "litlle harder but still easy")
		cls.fmake(cls, cls.f_mss2_c_easyphilosophizing, "not easy at all, but why not")




		################################### Third sprout files ###################################
		cls.fmake(cls, cls.f_mss3_k_f_milk, "from cow")
		cls.fmake(cls, cls.f_mss3_k_f_cheese, "from... cow")
		cls.fmake(cls, cls.f_mss3_k_f_meat, "from...")
		cls.fmake(cls, cls.f_mss3_k_o_chicken, "cooked in ~60 minutes")
		cls.fmake(cls, cls.f_mss3_k_o_pie, "already baked")
		cls.fmake(cls, cls.f_mss3_k_t_bc_bread, "always crumbles")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb1, "i barely believe it is just the first crumb")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb2, "i don't believe it is really the second crumb")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb420, "this crumb get really high")
		cls.fmake(cls, cls.f_mss3_k_t_bc_crumb69, "this crumb get really nice")




		################################### First bough ###################################
		cls.fmake(cls, cls.f_msb1_flower, "this flower was beutifull, but now effloresced")
		################################### Second bough ###################################
		os.makedirs(cls.d_msb2_w, exist_ok=True)
		################################### Third bough ###################################
		cls.fmake(cls, cls.f_msb3_almost, "as it's not weed yet, it should be left growing")
		os.makedirs(cls.d_msb3_a, exist_ok=True)
		os.makedirs(cls.d_msb3_t, exist_ok=True)





	def clean(self):

		if	os.path.isdir(self.MEDIUM_SET_SPROUT_1):			shutil.rmtree(self.MEDIUM_SET_SPROUT_1)
		if	os.path.isdir(self.MEDIUM_SET_SPROUT_2):			shutil.rmtree(self.MEDIUM_SET_SPROUT_2)
		if	os.path.isdir(self.MEDIUM_SET_SPROUT_3):			shutil.rmtree(self.MEDIUM_SET_SPROUT_3)
		if	os.path.isdir(self.MEDIUM_SET_BOUGH_1):				shutil.rmtree(self.MEDIUM_SET_BOUGH_1)
		if	os.path.isdir(self.MEDIUM_SET_BOUGH_2):				shutil.rmtree(self.MEDIUM_SET_BOUGH_2)
		if	os.path.isdir(self.MEDIUM_SET_BOUGH_3):				shutil.rmtree(self.MEDIUM_SET_BOUGH_3)
		if	os.path.isfile(self.MEDIUM_SET_SEEDS):				os.remove(self.MEDIUM_SET_SEEDS)
		if	os.path.isfile(self.MEDIUM_SET_SEEDS + ".db"):		os.remove(self.MEDIUM_SET_SEEDS + ".db")
		if	os.path.isfile(self.MEDIUM_SET_SEEDS + ".dat"):		os.remove(self.MEDIUM_SET_SEEDS + ".dat")
		if	os.path.isfile(self.MEDIUM_SET_SEEDS + ".bak"):		os.remove(self.MEDIUM_SET_SEEDS + ".bak")
		if	os.path.isfile(self.MEDIUM_SET_SEEDS + ".dir"):		os.remove(self.MEDIUM_SET_SEEDS + ".dir")







