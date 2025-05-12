import	os
import	re
import	unittest
from	sys									import stdout
from	shutil								import rmtree
from	logging								import Logger
from	logging								import StreamHandler
from	logging								import FileHandler
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests.irma					import IrmaTestCase
from	pygwarts.irma.contrib				import LibraryContrib








class ContribCase(IrmaTestCase):

	"""
		Testing for fields and edge cases
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.CONTRIB_HANDLER): os.remove(cls.CONTRIB_HANDLER)

	@classmethod
	def setUpClass(cls):

		super().setUpClass()
		cls.make_loggy_file(cls, cls.CONTRIB_HANDLER)


	def test_default_members(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib): pass


		self.test_case = Irma()
		self.assertTrue(hasattr(self.test_case.loggy, "handler"))
		self.assertIsInstance(self.test_case.loggy.handler, StreamHandler)
		self.assertTrue(hasattr(self.test_case.loggy, "init_name"))
		self.assertEqual(self.test_case.loggy.init_name, "fantastic logs and where to contribute them")
		self.assertTrue(hasattr(self.test_case.loggy, "init_level"))
		self.assertEqual(self.test_case.loggy.init_level, 20)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_mode"))
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(hasattr(self.test_case.loggy, "contribfmt"))
		self.assertEqual(

			self.test_case.loggy.contribfmt,
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": "%d/%m/%Y %H%M",
			}
		)

		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertFalse(self.test_case.loggy.forcing_map)

		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)




	def test_field_members(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler			= self.CONTRIB_HANDLER
				init_name		= "field_members"
				init_level		= 50
				force_handover	= False
				force_debug		= []
				force_info		= []
				force_warning	= []
				force_error		= []
				force_critical	= []
				contribfmt		= {

					"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
					"datefmt": "%Y/%d/%m %H%M",
				}


		self.test_case = Irma()
		self.assertTrue(hasattr(self.test_case.loggy, "handler"))
		self.assertIsInstance(self.test_case.loggy.handler, FileHandler)
		self.assertTrue(hasattr(self.test_case.loggy, "init_name"))
		self.assertEqual(self.test_case.loggy.init_name, "field_members")
		self.assertTrue(hasattr(self.test_case.loggy, "init_level"))
		self.assertEqual(self.test_case.loggy.init_level, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_mode"))
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(hasattr(self.test_case.loggy, "contribfmt"))
		self.assertEqual(

			self.test_case.loggy.contribfmt,
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
				"datefmt": "%Y/%d/%m %H%M",
			}
		)

		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertFalse(self.test_case.loggy.forcing_map)

		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 50 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)








	def test_argument_members(self):

		class Irma(Transmutable):	pass


		self.test_case = Irma(

			loggy=LibraryContrib(

				handler=self.CONTRIB_HANDLER,
				init_name="argument_members",
				init_level=50,
				force_handover=False,
				force_debug=[],
				force_info=[],
				force_warning=[],
				force_error=[],
				force_critical=[],
				contribfmt={

					"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
					"datefmt": "%Y/%d/%m %H%M",
				}
			)
		)
		self.assertTrue(hasattr(self.test_case.loggy, "handler"))
		self.assertIsInstance(self.test_case.loggy.handler, FileHandler)
		self.assertTrue(hasattr(self.test_case.loggy, "init_name"))
		self.assertEqual(self.test_case.loggy.init_name, "argument_members")
		self.assertTrue(hasattr(self.test_case.loggy, "init_level"))
		self.assertEqual(self.test_case.loggy.init_level, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_mode"))
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(hasattr(self.test_case.loggy, "contribfmt"))
		self.assertEqual(

			self.test_case.loggy.contribfmt,
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
				"datefmt": "%Y/%d/%m %H%M",
			}
		)

		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertFalse(self.test_case.loggy.forcing_map)

		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 50 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)








	def test_mixed_members(self):

		class Irma(Transmutable):	pass
		class loggy(LibraryContrib):

			handler			= self.CONTRIB_HANDLER
			init_level		= 50
			force_handover	= False
			force_info		= []
			force_error		= []
			contribfmt		= {

				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
				"datefmt": "%Y/%d/%m %H%M",
			}


		self.test_case = Irma(

			loggy=loggy(

				init_name="mixed_members",
				force_debug=[],
				force_warning=[],
				force_critical=[],
			)
		)
		self.assertTrue(hasattr(self.test_case.loggy, "handler"))
		self.assertIsInstance(self.test_case.loggy.handler, FileHandler)
		self.assertTrue(hasattr(self.test_case.loggy, "init_name"))
		self.assertEqual(self.test_case.loggy.init_name, "mixed_members")
		self.assertTrue(hasattr(self.test_case.loggy, "init_level"))
		self.assertEqual(self.test_case.loggy.init_level, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_mode"))
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(hasattr(self.test_case.loggy, "contribfmt"))
		self.assertEqual(

			self.test_case.loggy.contribfmt,
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
				"datefmt": "%Y/%d/%m %H%M",
			}
		)

		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertFalse(self.test_case.loggy.forcing_map)

		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 50 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)








	def test_over_members(self):

		class Irma(Transmutable):	pass
		class loggy(LibraryContrib):

			handler			= stdout
			init_name		= "not over_members"
			init_level		= 10
			force_handover	= True
			force_debug		= [ "Irma" ]
			force_info		= []
			force_warning	= []
			force_error		= []
			force_critical	= []
			contribfmt		= {

				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
				"datefmt": "%Y/%d/%m %H%M",
			}

		self.test_case = Irma(

			loggy=loggy(

				handler=self.CONTRIB_HANDLER,
				init_name="over_members",
				init_level=50,
				force_handover=False,
				force_debug=[],
				force_info=[],
				force_warning=[],
				force_error=[],
				force_critical=[],
				contribfmt={

					"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
					"datefmt": "%Y/%d/%m %H%M",
				}
			)
		)
		self.assertTrue(hasattr(self.test_case.loggy, "handler"))
		self.assertIsInstance(self.test_case.loggy.handler, FileHandler)
		self.assertTrue(hasattr(self.test_case.loggy, "init_name"))
		self.assertEqual(self.test_case.loggy.init_name, "over_members")
		self.assertTrue(hasattr(self.test_case.loggy, "init_level"))
		self.assertEqual(self.test_case.loggy.init_level, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_mode"))
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(hasattr(self.test_case.loggy, "contribfmt"))
		self.assertEqual(

			self.test_case.loggy.contribfmt,
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": "%Y/%d/%m %H%M",
			}
		)

		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertFalse(self.test_case.loggy.forcing_map)

		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 50 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)








	def test_handler_field_fails(self):

		for current in ( 1, .1, None, True, False,[ stdout ],( stdout, ),{ stdout },{ "handler": stdout} ):
			with self.subTest(handler=current):

				class Irma(Transmutable):
					class loggy(LibraryContrib):

						init_name	= f"field-handler:{current}"
						handler		= current

				self.assertRaisesRegex(

					TypeError,
					r"LibraryContrib handler must be file path string or stdout \(default\)",
					Irma
				)




	def test_handler_argument_fails(self):

		for current in ( 1, .1, True, False,[ stdout ],( stdout, ),{ stdout },{ "handler": stdout} ):
			with self.subTest(handler=current):

				self.assertRaisesRegex(

					TypeError,
					r"LibraryContrib handler must be file path string or stdout \(default\)",
					LibraryContrib,
					init_name=f"argument-handler:{current}",
					handler=current
				)




	def test_file_handler_creation(self):

		deeper_d = str(self.IRMA_ROOT /"deeper")
		deeper_f = os.path.join(deeper_d, os.path.basename(self.CONTRIB_HANDLER))
		if	os.path.isdir(deeper_d): rmtree(self.IRMA_ROOT)
		self.assertFalse(os.path.isfile(deeper_f))

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name	= "file_handler"
				handler		= deeper_f

		self.test_case = Irma()
		self.assertTrue(os.path.isfile(deeper_f))

		# closing logger cause it might not be deleted successfully if it still opened
		self.test_case.loggy.close()

		rmtree(deeper_d)
		self.assertFalse(os.path.isdir(deeper_d))
		self.assertFalse(os.path.isfile(deeper_f))




	def test_valid_levels(self):

		for i,level in enumerate(

			(
				10, 20, 30, 40, 50,
				10., 20., 30., 40., 50.,
				.10, .20, .30, .40, .50,
				"10", "20", "30", "40", "50",
				"10.", "20.", "30.", "40.", "50.",
				".10", ".20", ".30", ".40", ".50",
				1E1, 2E1, 3E1, 4E1, 5E1,
				-10, -20, -30, -40, -50,
				-10., -20., -30., -40., -50.,
				-.10, -.20, -.30, -.40, -.50,
				"-10", "-20", "-30", "-40", "-50",
				"-10.", "-20.", "-30.", "-40.", "-50.",
				"-.10", "-.20", "-.30", "-.40", "-.50",
				-1E1, -2E1, -3E1, -4E1, -5E1,
				True, False,
			)
		):
			with self.subTest(order=i, level=level):

				class Irma(Transmutable):
					class loggy(LibraryContrib):

						init_name	= f"valid_level"
						init_level	= level

				self.test_case = Irma()
				current = int(float(level))
				self.assertEqual(self.test_case.loggy.contributor.level, current)
				self.test_case.loggy.close()




	def test_invalid_levels(self):

		for i,level in enumerate(( None,( 10, ),[ 10 ],{ 10 },{ "level": 10 }, print, object )):
			with self.subTest(order=i, init_level=level):

				class Irma(Transmutable):
					class loggy(LibraryContrib):

						init_name	= f"invalid_level-{i}"
						init_level	= level

				self.assertRaisesRegex(

					TypeError,
					"LibraryContrib levels must be numeric values",
					Irma
				)




	def test_handover_mode_set_1(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name	= "handover_mode_set"
				handler		= self.CONTRIB_HANDLER


		self.test_case = Irma()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertIsNotNone(self.test_case.loggy.handover_mode)

		for positive in ( 1, 1., .1, "False",[ False ],( False, ),{ False },{ "state": False }):
			with self.subTest(state=positive):

				self.assertTrue(positive)
				self.test_case.loggy.handover_mode = positive
				self.assertTrue(self.test_case.loggy.handover_mode)
				self.assertEqual(self.test_case.loggy.handover_mode, True)
				if	positive not in ( 1,1. ): self.assertNotEqual(positive, True)


		for negative in ( 0, 0., .0, "",[],tuple(),set(),{}):
			with self.subTest(state=negative):

				self.assertFalse(negative)
				self.test_case.loggy.handover_mode = negative
				self.assertFalse(self.test_case.loggy.handover_mode)
				self.assertIsNotNone(self.test_case.loggy.handover_mode)
				self.assertEqual(self.test_case.loggy.handover_mode, False)
				if	negative not in ( 0,0. ): self.assertNotEqual(negative, False)




	def test_handover_mode_set_2(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name		= "handover_mode_set"
				handler			= self.CONTRIB_HANDLER
				force_handover	= True


		self.test_case = Irma()
		self.assertTrue(self.test_case.loggy.handover_mode)

		for negative in ( 0, 0., .0, "",[],tuple(),set(),{}):
			with self.subTest(state=negative):

				self.assertFalse(negative)
				self.test_case.loggy.handover_mode = negative
				self.assertFalse(self.test_case.loggy.handover_mode)
				self.assertIsNotNone(self.test_case.loggy.handover_mode)
				self.assertEqual(self.test_case.loggy.handover_mode, False)
				if	negative not in ( 0,0. ): self.assertNotEqual(negative, False)


		for positive in ( 1, 1., .1, "False",[ False ],( False, ),{ False },{ "state": False }):
			with self.subTest(state=positive):

				self.assertTrue(positive)
				self.test_case.loggy.handover_mode = positive
				self.assertTrue(self.test_case.loggy.handover_mode)
				self.assertEqual(self.test_case.loggy.handover_mode, True)
				if	positive not in ( 1,1. ): self.assertNotEqual(positive, True)




	def test_handover_mode_2on(self):

		hm2on_loggy = str(self.IRMA_ROOT /"hm2on.loggy")
		self.make_loggy_file(hm2on_loggy)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name	= "hm2on"
				handler		= hm2on_loggy

			class Levels(ContribCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(hm2on_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(hm2on_loggy)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(hm2on_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@hm2on-Irma.Levels.debugs INFO : Must be logged",
				"@hm2on-Irma.Levels.debugs WARNING : Must be logged",
				"@hm2on-Irma.Levels.debugs ERROR : Must be logged",
				"@hm2on-Irma.Levels.debugs CRITICAL : Must be logged",

				"@hm2on-Irma.Levels.infos INFO : Must be logged",
				"@hm2on-Irma.Levels.infos WARNING : Must be logged",
				"@hm2on-Irma.Levels.infos ERROR : Must be logged",
				"@hm2on-Irma.Levels.infos CRITICAL : Must be logged",

				"@hm2on-Irma.Levels.warnings INFO : Must be logged",
				"@hm2on-Irma.Levels.warnings WARNING : Must be logged",
				"@hm2on-Irma.Levels.warnings ERROR : Must be logged",
				"@hm2on-Irma.Levels.warnings CRITICAL : Must be logged",

				"@hm2on-Irma.Levels.errors INFO : Must be logged",
				"@hm2on-Irma.Levels.errors WARNING : Must be logged",
				"@hm2on-Irma.Levels.errors ERROR : Must be logged",
				"@hm2on-Irma.Levels.errors CRITICAL : Must be logged",

				"@hm2on-Irma.Levels.criticals INFO : Must be logged",
				"@hm2on-Irma.Levels.criticals WARNING : Must be logged",
				"@hm2on-Irma.Levels.criticals ERROR : Must be logged",
				"@hm2on-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(hm2on_loggy)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(hm2on_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",

				"@hm2on INFO : Must be logged",
				"@hm2on WARNING : Must be logged",
				"@hm2on ERROR : Must be logged",
				"@hm2on CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(hm2on_loggy): os.remove(hm2on_loggy)








	def test_handover_mode_2off(self):

		hm2off_loggy = str(self.IRMA_ROOT /"hm2off.loggy")
		self.make_loggy_file(hm2off_loggy)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name		= "hm2off"
				handler			= hm2off_loggy
				force_handover	= True

			class Levels(ContribCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(hm2off_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@hm2off-Irma.Levels.debugs INFO : Must be logged",
				"@hm2off-Irma.Levels.debugs WARNING : Must be logged",
				"@hm2off-Irma.Levels.debugs ERROR : Must be logged",
				"@hm2off-Irma.Levels.debugs CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.infos INFO : Must be logged",
				"@hm2off-Irma.Levels.infos WARNING : Must be logged",
				"@hm2off-Irma.Levels.infos ERROR : Must be logged",
				"@hm2off-Irma.Levels.infos CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.warnings INFO : Must be logged",
				"@hm2off-Irma.Levels.warnings WARNING : Must be logged",
				"@hm2off-Irma.Levels.warnings ERROR : Must be logged",
				"@hm2off-Irma.Levels.warnings CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.errors INFO : Must be logged",
				"@hm2off-Irma.Levels.errors WARNING : Must be logged",
				"@hm2off-Irma.Levels.errors ERROR : Must be logged",
				"@hm2off-Irma.Levels.errors CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.criticals INFO : Must be logged",
				"@hm2off-Irma.Levels.criticals WARNING : Must be logged",
				"@hm2off-Irma.Levels.criticals ERROR : Must be logged",
				"@hm2off-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(hm2off_loggy)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(hm2off_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@hm2off INFO : Must be logged",
				"@hm2off WARNING : Must be logged",
				"@hm2off ERROR : Must be logged",
				"@hm2off CRITICAL : Must be logged",

				"@hm2off INFO : Must be logged",
				"@hm2off WARNING : Must be logged",
				"@hm2off ERROR : Must be logged",
				"@hm2off CRITICAL : Must be logged",

				"@hm2off INFO : Must be logged",
				"@hm2off WARNING : Must be logged",
				"@hm2off ERROR : Must be logged",
				"@hm2off CRITICAL : Must be logged",

				"@hm2off INFO : Must be logged",
				"@hm2off WARNING : Must be logged",
				"@hm2off ERROR : Must be logged",
				"@hm2off CRITICAL : Must be logged",

				"@hm2off INFO : Must be logged",
				"@hm2off WARNING : Must be logged",
				"@hm2off ERROR : Must be logged",
				"@hm2off CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(hm2off_loggy)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(hm2off_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@hm2off-Irma.Levels.debugs INFO : Must be logged",
				"@hm2off-Irma.Levels.debugs WARNING : Must be logged",
				"@hm2off-Irma.Levels.debugs ERROR : Must be logged",
				"@hm2off-Irma.Levels.debugs CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.infos INFO : Must be logged",
				"@hm2off-Irma.Levels.infos WARNING : Must be logged",
				"@hm2off-Irma.Levels.infos ERROR : Must be logged",
				"@hm2off-Irma.Levels.infos CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.warnings INFO : Must be logged",
				"@hm2off-Irma.Levels.warnings WARNING : Must be logged",
				"@hm2off-Irma.Levels.warnings ERROR : Must be logged",
				"@hm2off-Irma.Levels.warnings CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.errors INFO : Must be logged",
				"@hm2off-Irma.Levels.errors WARNING : Must be logged",
				"@hm2off-Irma.Levels.errors ERROR : Must be logged",
				"@hm2off-Irma.Levels.errors CRITICAL : Must be logged",

				"@hm2off-Irma.Levels.criticals INFO : Must be logged",
				"@hm2off-Irma.Levels.criticals WARNING : Must be logged",
				"@hm2off-Irma.Levels.criticals ERROR : Must be logged",
				"@hm2off-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(hm2off_loggy): os.remove(hm2off_loggy)








	def test_handover_switch(self):

		handover_switch = str(self.IRMA_ROOT /"handover_switch.loggy")
		self.make_loggy_file(handover_switch)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler			= handover_switch
				init_name		= "handover_switch"
				force_handover	= True

			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma()
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],20)
		loggy = []
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.errors INFO : Must be logged",
				"@handover_switch-Irma.Levels.errors WARNING : Must be logged",
				"@handover_switch-Irma.Levels.errors ERROR : Must be logged",
				"@handover_switch-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = False
		self.test_case.loggy.force("*errors", level=10)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],20)
		self.test_case.Levels.errors()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.errors DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.errors INFO : Must be logged",
				"@handover_switch-Irma.Levels.errors WARNING : Must be logged",
				"@handover_switch-Irma.Levels.errors ERROR : Must be logged",
				"@handover_switch-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.errors DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.errors INFO : Must be logged",
				"@handover_switch-Irma.Levels.errors WARNING : Must be logged",
				"@handover_switch-Irma.Levels.errors ERROR : Must be logged",
				"@handover_switch-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.force("*warnings", level=10)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],20)
		self.test_case.Levels.warnings()

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.warnings DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.warnings INFO : Must be logged",
				"@handover_switch-Irma.Levels.warnings WARNING : Must be logged",
				"@handover_switch-Irma.Levels.warnings ERROR : Must be logged",
				"@handover_switch-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.criticals INFO : Must be logged",
				"@handover_switch-Irma.Levels.criticals WARNING : Must be logged",
				"@handover_switch-Irma.Levels.criticals ERROR : Must be logged",
				"@handover_switch-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.Levels.warnings()

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.warnings DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.warnings INFO : Must be logged",
				"@handover_switch-Irma.Levels.warnings WARNING : Must be logged",
				"@handover_switch-Irma.Levels.warnings ERROR : Must be logged",
				"@handover_switch-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = False
		self.test_case.loggy.force("*warnings", level=20)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],20)
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch INFO : Must be logged",
				"@handover_switch WARNING : Must be logged",
				"@handover_switch ERROR : Must be logged",
				"@handover_switch CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.errors DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.errors INFO : Must be logged",
				"@handover_switch-Irma.Levels.errors WARNING : Must be logged",
				"@handover_switch-Irma.Levels.errors ERROR : Must be logged",
				"@handover_switch-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch INFO : Must be logged",
				"@handover_switch WARNING : Must be logged",
				"@handover_switch ERROR : Must be logged",
				"@handover_switch CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = True
		self.test_case.loggy.force("*warnings", level=10)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],20)
		self.test_case.Levels.warnings()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.warnings DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.warnings INFO : Must be logged",
				"@handover_switch-Irma.Levels.warnings WARNING : Must be logged",
				"@handover_switch-Irma.Levels.warnings ERROR : Must be logged",
				"@handover_switch-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.warnings DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.warnings INFO : Must be logged",
				"@handover_switch-Irma.Levels.warnings WARNING : Must be logged",
				"@handover_switch-Irma.Levels.warnings ERROR : Must be logged",
				"@handover_switch-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.errors DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.errors INFO : Must be logged",
				"@handover_switch-Irma.Levels.errors WARNING : Must be logged",
				"@handover_switch-Irma.Levels.errors ERROR : Must be logged",
				"@handover_switch-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.warnings DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.warnings INFO : Must be logged",
				"@handover_switch-Irma.Levels.warnings WARNING : Must be logged",
				"@handover_switch-Irma.Levels.warnings ERROR : Must be logged",
				"@handover_switch-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.infos()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.infos INFO : Must be logged",
				"@handover_switch-Irma.Levels.infos WARNING : Must be logged",
				"@handover_switch-Irma.Levels.infos ERROR : Must be logged",
				"@handover_switch-Irma.Levels.infos CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(handover_switch)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(handover_switch) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handover_switch-Irma.Levels.warnings DEBUG : Must be logged",
				"@handover_switch-Irma.Levels.warnings INFO : Must be logged",
				"@handover_switch-Irma.Levels.warnings WARNING : Must be logged",
				"@handover_switch-Irma.Levels.warnings ERROR : Must be logged",
				"@handover_switch-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(handover_switch): os.remove(handover_switch)








	def test_handovers(self):

		handovers = str(self.IRMA_ROOT /"handovers.loggy")
		self.make_loggy_file(handovers)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name	= "handovers"
				handler		= handovers

			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma()
		self.assertEqual(

			self.test_case.loggy.handover_order,
			[
				"Irma",
				"Irma.Levels",
				"Irma.Levels.debugs",
				"Irma.Levels.infos",
				"Irma.Levels.warnings",
				"Irma.Levels.errors",
				"Irma.Levels.criticals",
			]
		)
		self.assertEqual(

			self.test_case.loggy.handovers(),
			[
				"Irma",
				"Irma.Levels",
				"Irma.Levels.debugs",
				"Irma.Levels.infos",
				"Irma.Levels.warnings",
				"Irma.Levels.errors",
				"Irma.Levels.criticals",
			]
		)


		loggy = []
		order = self.test_case.loggy.handovers(20)

		self.test_case.loggy.close()
		with open(handovers) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handovers-_handovers_ INFO : Irma",
				"@handovers-_handovers_ INFO : Irma.Levels",
				"@handovers-_handovers_ INFO : Irma.Levels.debugs",
				"@handovers-_handovers_ INFO : Irma.Levels.infos",
				"@handovers-_handovers_ INFO : Irma.Levels.warnings",
				"@handovers-_handovers_ INFO : Irma.Levels.errors",
				"@handovers-_handovers_ INFO : Irma.Levels.criticals",
			]
		)
		self.assertEqual(

			order,
			[
				"Irma",
				"Irma.Levels",
				"Irma.Levels.debugs",
				"Irma.Levels.infos",
				"Irma.Levels.warnings",
				"Irma.Levels.errors",
				"Irma.Levels.criticals",
			]
		)


		loggy = []
		self.make_loggy_file(handovers)
		order = self.test_case.loggy.handovers(10)

		self.test_case.loggy.close()
		with open(handovers) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handovers-_handovers_ DEBUG : Irma",
				"@handovers-_handovers_ DEBUG : Irma.Levels",
				"@handovers-_handovers_ DEBUG : Irma.Levels.debugs",
				"@handovers-_handovers_ DEBUG : Irma.Levels.infos",
				"@handovers-_handovers_ DEBUG : Irma.Levels.warnings",
				"@handovers-_handovers_ DEBUG : Irma.Levels.errors",
				"@handovers-_handovers_ DEBUG : Irma.Levels.criticals",
			]
		)
		self.assertEqual(

			order,
			[
				"Irma",
				"Irma.Levels",
				"Irma.Levels.debugs",
				"Irma.Levels.infos",
				"Irma.Levels.warnings",
				"Irma.Levels.errors",
				"Irma.Levels.criticals",
			]
		)


		loggy = []
		self.make_loggy_file(handovers)
		self.test_case.Levels.debugs()

		self.test_case.loggy.close()
		with open(handovers) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@handovers INFO : Must be logged",
				"@handovers WARNING : Must be logged",
				"@handovers ERROR : Must be logged",
				"@handovers CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(handovers): os.remove(handovers)








	def test_handover_raise(self):

		class Irma(Transmutable):	pass
		logger = LibraryContrib(init_name="handover_raise1",handler=self.CONTRIB_HANDLER)
		self.test_case = Irma(logger)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map,{ "Irma": 20 })
		self.test_case.loggy.handover_map["Irma"] = "20"
		self.assertRaisesRegex(

			ValueError,
			r"Incorrect handover mapping \"Irma\"\: \"20\"",
			getattr,
			self.test_case,
			"loggy"
		)
		logger.handler.close()

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.CONTRIB_HANDLER
				init_name	= "handover_raise2"

		self.test_case = Irma()
		self.assertEqual(self.test_case.loggy.handover_map,{ "Irma": 20 })




	def test_handover_unassign(self):

		unsloggy = str(self.IRMA_ROOT /"unsloggy.loggy")
		self.make_loggy_file(unsloggy)

		unassigned = LibraryContrib(

			handler=unsloggy,
			init_name="unassigned",
			init_level=10,
		)

		unassigned.handover("first", assign=False)
		unassigned.debug("well tried")
		unassigned.info("well tried")
		unassigned.handover("second", assign=False)
		unassigned.debug("very well")
		unassigned.info("very well")
		self.assertEqual(unassigned.handover_map,{ "first": 10, "second": 10 })
		loggy = []

		unassigned.close()
		with open(unsloggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@unassigned-first DEBUG : well tried",
				"@unassigned-first INFO : well tried",
				"@unassigned-second DEBUG : very well",
				"@unassigned-second INFO : very well",
			]
		)
		if	os.path.isfile(unsloggy): os.remove(unsloggy)








	def test_forcing_map_invalids(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name		= "forcing_map_invalids"
				handler			= self.CONTRIB_HANDLER
				force_debug		= "*.debugs",
				force_info		= "*.infos"
				force_warning	= { "*.warnings" }
				force_error		= { "name": "*.errors" }
				force_critical	= True


		self.test_case = Irma()
		self.assertEqual(len(self.test_case.loggy.handover_map),1)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertEqual(self.test_case.loggy.forcing_map,{ re.compile(".*.debugs"): 10 })








	def test_forcing_map_from_fields(self):

		fmfl_loggy = str(self.IRMA_ROOT /"fmfl.loggy")
		self.make_loggy_file(fmfl_loggy)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler			= fmfl_loggy
				init_name		= "fmfl"
				force_debug		= "*.debugs*",
				force_info		= "*.infos*",
				force_warning	= "*.warnings*",
				force_error		= "*.errors*",
				force_critical	= "*.criticals*",

			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma()
		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertEqual(

			self.test_case.loggy.forcing_map,
			{
				re.compile(".*.debugs.*"):		10,
				re.compile(".*.infos.*"):		20,
				re.compile(".*.warnings.*"):	30,
				re.compile(".*.errors.*"):		40,
				re.compile(".*.criticals.*"):	50,
			}
		)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(

			self.test_case.loggy.handover_map,
			{
				"Irma":						20,
				"Irma.Levels":				20,
				"Irma.Levels.debugs":		10,
				"Irma.Levels.infos":		20,
				"Irma.Levels.warnings":		30,
				"Irma.Levels.errors":		40,
				"Irma.Levels.criticals":	50,
			}
		)

		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(fmfl_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@fmfl-Irma.Levels.debugs DEBUG : Must be logged",
				"@fmfl-Irma.Levels.debugs INFO : Must be logged",
				"@fmfl-Irma.Levels.debugs WARNING : Must be logged",
				"@fmfl-Irma.Levels.debugs ERROR : Must be logged",
				"@fmfl-Irma.Levels.debugs CRITICAL : Must be logged",

				"@fmfl INFO : Must be logged",
				"@fmfl WARNING : Must be logged",
				"@fmfl ERROR : Must be logged",
				"@fmfl CRITICAL : Must be logged",

				"@fmfl WARNING : Must be logged",
				"@fmfl ERROR : Must be logged",
				"@fmfl CRITICAL : Must be logged",

				"@fmfl ERROR : Must be logged",
				"@fmfl CRITICAL : Must be logged",

				"@fmfl CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(fmfl_loggy): os.remove(fmfl_loggy)








	def test_forcing_map_from_arguments(self):

		fmfa_loggy = str(self.IRMA_ROOT /"fmfa.loggy")
		self.make_loggy_file(fmfa_loggy)

		class Irma(Transmutable):
			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma(
			LibraryContrib(

				handler=fmfa_loggy,
				init_name="fmfa",
				force_debug=( "*.debugs*", ),
				force_info=( "*.infos*", ),
				force_warning=( "*.warnings*", ),
				force_error=( "*.errors*", ),
				force_critical=( "*.criticals*", ),
			)
		)
		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertEqual(

			self.test_case.loggy.forcing_map,
			{
				re.compile(".*.debugs.*"):		10,
				re.compile(".*.infos.*"):		20,
				re.compile(".*.warnings.*"):	30,
				re.compile(".*.errors.*"):		40,
				re.compile(".*.criticals.*"):	50,
			}
		)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(

			self.test_case.loggy.handover_map,
			{
				"Irma":						20,
				"Irma.Levels":				20,
				"Irma.Levels.debugs":		10,
				"Irma.Levels.infos":		20,
				"Irma.Levels.warnings":		30,
				"Irma.Levels.errors":		40,
				"Irma.Levels.criticals":	50,
			}
		)


		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(fmfa_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@fmfa-Irma.Levels.debugs DEBUG : Must be logged",
				"@fmfa-Irma.Levels.debugs INFO : Must be logged",
				"@fmfa-Irma.Levels.debugs WARNING : Must be logged",
				"@fmfa-Irma.Levels.debugs ERROR : Must be logged",
				"@fmfa-Irma.Levels.debugs CRITICAL : Must be logged",

				"@fmfa INFO : Must be logged",
				"@fmfa WARNING : Must be logged",
				"@fmfa ERROR : Must be logged",
				"@fmfa CRITICAL : Must be logged",

				"@fmfa WARNING : Must be logged",
				"@fmfa ERROR : Must be logged",
				"@fmfa CRITICAL : Must be logged",

				"@fmfa ERROR : Must be logged",
				"@fmfa CRITICAL : Must be logged",

				"@fmfa CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(fmfa_loggy): os.remove(fmfa_loggy)








	def test_force_all(self):

		force_all = str(self.IRMA_ROOT /"force_all.loggy")
		self.make_loggy_file(force_all)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler		= force_all
				init_name	= "force_all"

			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma()
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],20)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_all) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_all INFO : Must be logged",
				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all INFO : Must be logged",
				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all INFO : Must be logged",
				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all INFO : Must be logged",
				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all INFO : Must be logged",
				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",
			]
		)


		forced = self.test_case.loggy.force(level=30)
		self.assertEqual(forced,7)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],30)
		self.make_loggy_file(force_all)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_all) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all WARNING : Must be logged",
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",
			]
		)


		forced = self.test_case.loggy.force(level=40)
		self.assertEqual(forced,7)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],40)
		self.make_loggy_file(force_all)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_all) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",

				"@force_all ERROR : Must be logged",
				"@force_all CRITICAL : Must be logged",
			]
		)


		forced = self.test_case.loggy.force(level=50)
		self.assertEqual(forced,7)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],50)
		self.make_loggy_file(force_all)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_all) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_all CRITICAL : Must be logged",

				"@force_all CRITICAL : Must be logged",

				"@force_all CRITICAL : Must be logged",

				"@force_all CRITICAL : Must be logged",

				"@force_all CRITICAL : Must be logged",
			]
		)


		forced = self.test_case.loggy.force(level=10)
		self.assertEqual(forced,7)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],10)
		self.make_loggy_file(force_all)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_all) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_all-Irma.Levels.debugs DEBUG : Must be logged",
				"@force_all-Irma.Levels.debugs INFO : Must be logged",
				"@force_all-Irma.Levels.debugs WARNING : Must be logged",
				"@force_all-Irma.Levels.debugs ERROR : Must be logged",
				"@force_all-Irma.Levels.debugs CRITICAL : Must be logged",

				"@force_all-Irma.Levels.infos DEBUG : Must be logged",
				"@force_all-Irma.Levels.infos INFO : Must be logged",
				"@force_all-Irma.Levels.infos WARNING : Must be logged",
				"@force_all-Irma.Levels.infos ERROR : Must be logged",
				"@force_all-Irma.Levels.infos CRITICAL : Must be logged",

				"@force_all-Irma.Levels.warnings DEBUG : Must be logged",
				"@force_all-Irma.Levels.warnings INFO : Must be logged",
				"@force_all-Irma.Levels.warnings WARNING : Must be logged",
				"@force_all-Irma.Levels.warnings ERROR : Must be logged",
				"@force_all-Irma.Levels.warnings CRITICAL : Must be logged",

				"@force_all-Irma.Levels.errors DEBUG : Must be logged",
				"@force_all-Irma.Levels.errors INFO : Must be logged",
				"@force_all-Irma.Levels.errors WARNING : Must be logged",
				"@force_all-Irma.Levels.errors ERROR : Must be logged",
				"@force_all-Irma.Levels.errors CRITICAL : Must be logged",

				"@force_all-Irma.Levels.criticals DEBUG : Must be logged",
				"@force_all-Irma.Levels.criticals INFO : Must be logged",
				"@force_all-Irma.Levels.criticals WARNING : Must be logged",
				"@force_all-Irma.Levels.criticals ERROR : Must be logged",
				"@force_all-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(force_all): os.remove(force_all)








	def test_force_some(self):

		force_some = str(self.IRMA_ROOT /"force_some.loggy")
		self.make_loggy_file(force_some)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler			= force_some
				init_name		= "force_some"
				force_debug		= "*.debugs*",
				force_info		= "*.infos*",
				force_warning	= "*.warnings*",
				force_error		= "*.errors*",
				force_critical	= "*.criticals*",

			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma()
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],50)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_some) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_some-Irma.Levels.debugs DEBUG : Must be logged",
				"@force_some-Irma.Levels.debugs INFO : Must be logged",
				"@force_some-Irma.Levels.debugs WARNING : Must be logged",
				"@force_some-Irma.Levels.debugs ERROR : Must be logged",
				"@force_some-Irma.Levels.debugs CRITICAL : Must be logged",

				"@force_some INFO : Must be logged",
				"@force_some WARNING : Must be logged",
				"@force_some ERROR : Must be logged",
				"@force_some CRITICAL : Must be logged",

				"@force_some WARNING : Must be logged",
				"@force_some ERROR : Must be logged",
				"@force_some CRITICAL : Must be logged",

				"@force_some ERROR : Must be logged",
				"@force_some CRITICAL : Must be logged",

				"@force_some CRITICAL : Must be logged",
			]
		)


		forced_1 = self.test_case.loggy.force("Irma.Levels.debugs", level=20)
		forced_2 = self.test_case.loggy.force("Irma.Levels.infos", level=30)
		forced_3 = self.test_case.loggy.force("Irma.Levels.warnings", level=40)
		forced_4 = self.test_case.loggy.force("Irma.Levels.errors", level=50)
		self.assertEqual(forced_1,1)
		self.assertEqual(forced_2,1)
		self.assertEqual(forced_3,1)
		self.assertEqual(forced_4,1)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],30)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],40)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],50)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],50)
		self.make_loggy_file(force_some)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_some) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_some INFO : Must be logged",
				"@force_some WARNING : Must be logged",
				"@force_some ERROR : Must be logged",
				"@force_some CRITICAL : Must be logged",

				"@force_some WARNING : Must be logged",
				"@force_some ERROR : Must be logged",
				"@force_some CRITICAL : Must be logged",

				"@force_some ERROR : Must be logged",
				"@force_some CRITICAL : Must be logged",

				"@force_some CRITICAL : Must be logged",

				"@force_some CRITICAL : Must be logged",
			]
		)


		forced = self.test_case.loggy.force("Irma.Levels.*", level=10)
		self.assertEqual(forced,5)
		self.assertEqual(len(self.test_case.loggy.handover_map),7)
		self.assertEqual(self.test_case.loggy.handover_map["Irma"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels"],20)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.debugs"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.infos"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.warnings"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.errors"],10)
		self.assertEqual(self.test_case.loggy.handover_map["Irma.Levels.criticals"],10)
		self.make_loggy_file(force_some)
		loggy = []
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(force_some) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_some-Irma.Levels.debugs DEBUG : Must be logged",
				"@force_some-Irma.Levels.debugs INFO : Must be logged",
				"@force_some-Irma.Levels.debugs WARNING : Must be logged",
				"@force_some-Irma.Levels.debugs ERROR : Must be logged",
				"@force_some-Irma.Levels.debugs CRITICAL : Must be logged",

				"@force_some-Irma.Levels.infos DEBUG : Must be logged",
				"@force_some-Irma.Levels.infos INFO : Must be logged",
				"@force_some-Irma.Levels.infos WARNING : Must be logged",
				"@force_some-Irma.Levels.infos ERROR : Must be logged",
				"@force_some-Irma.Levels.infos CRITICAL : Must be logged",

				"@force_some-Irma.Levels.warnings DEBUG : Must be logged",
				"@force_some-Irma.Levels.warnings INFO : Must be logged",
				"@force_some-Irma.Levels.warnings WARNING : Must be logged",
				"@force_some-Irma.Levels.warnings ERROR : Must be logged",
				"@force_some-Irma.Levels.warnings CRITICAL : Must be logged",

				"@force_some-Irma.Levels.errors DEBUG : Must be logged",
				"@force_some-Irma.Levels.errors INFO : Must be logged",
				"@force_some-Irma.Levels.errors WARNING : Must be logged",
				"@force_some-Irma.Levels.errors ERROR : Must be logged",
				"@force_some-Irma.Levels.errors CRITICAL : Must be logged",

				"@force_some-Irma.Levels.criticals DEBUG : Must be logged",
				"@force_some-Irma.Levels.criticals INFO : Must be logged",
				"@force_some-Irma.Levels.criticals WARNING : Must be logged",
				"@force_some-Irma.Levels.criticals ERROR : Must be logged",
				"@force_some-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(force_some): os.remove(force_some)








	def test_force_escalated(self):

		force_escalated = str(self.IRMA_ROOT /"force_escalated.loggy")
		self.make_loggy_file(force_escalated)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler			= force_escalated
				init_name		= "force_escalated"
				force_debug		= "*.debugs*",

			class Levels(ContribCase.Levels):	pass


		self.test_case = Irma()
		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertEqual(self.test_case.loggy.forcing_map,{ re.compile(".*.debugs.*"): 10 })
		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(

			self.test_case.loggy.handover_map,
			{
				"Irma":						20,
				"Irma.Levels":				20,
				"Irma.Levels.debugs":		10,
				"Irma.Levels.infos":		20,
				"Irma.Levels.warnings":		20,
				"Irma.Levels.errors":		20,
				"Irma.Levels.criticals":	20,
			}
		)

		loggy = []
		self.test_case.Levels.debugs()

		self.test_case.loggy.close()
		with open(force_escalated) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_escalated-Irma.Levels.debugs DEBUG : Must be logged",
				"@force_escalated-Irma.Levels.debugs INFO : Must be logged",
				"@force_escalated-Irma.Levels.debugs WARNING : Must be logged",
				"@force_escalated-Irma.Levels.debugs ERROR : Must be logged",
				"@force_escalated-Irma.Levels.debugs CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(force_escalated)
		self.test_case.loggy.force("Irma.Levels.debugs", level=20)
		self.test_case.Levels.debugs()

		self.test_case.loggy.close()
		with open(force_escalated) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_escalated INFO : Must be logged",
				"@force_escalated WARNING : Must be logged",
				"@force_escalated ERROR : Must be logged",
				"@force_escalated CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(force_escalated): os.remove(force_escalated)








	def test_force_single_debug(self):

		force_sdbg = str(self.IRMA_ROOT /"force_sdbg.loggy")
		self.make_loggy_file(force_sdbg)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler		= force_sdbg
				init_name	= "force_sdbg"

			class debugs(ContribCase.Levels.debugs):	pass


		self.test_case = Irma()
		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertFalse(self.test_case.loggy.forcing_map)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.debugs": 20, })


		loggy = []
		self.test_case.debugs()

		self.test_case.loggy.close()
		with open(force_sdbg) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_sdbg INFO : Must be logged",
				"@force_sdbg WARNING : Must be logged",
				"@force_sdbg ERROR : Must be logged",
				"@force_sdbg CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(force_sdbg)
		self.test_case.loggy.force("Irma.debugs", level=10)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.debugs": 10, })
		self.test_case.debugs()

		self.test_case.loggy.close()
		with open(force_sdbg) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_sdbg-Irma.debugs DEBUG : Must be logged",
				"@force_sdbg-Irma.debugs INFO : Must be logged",
				"@force_sdbg-Irma.debugs WARNING : Must be logged",
				"@force_sdbg-Irma.debugs ERROR : Must be logged",
				"@force_sdbg-Irma.debugs CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(force_sdbg)
		self.test_case.loggy.force("Irma.debugs", level=20)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.debugs": 20, })
		self.test_case.debugs()

		self.test_case.loggy.close()
		with open(force_sdbg) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_sdbg INFO : Must be logged",
				"@force_sdbg WARNING : Must be logged",
				"@force_sdbg ERROR : Must be logged",
				"@force_sdbg CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(force_sdbg)
		self.test_case.loggy.handover_mode = True
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.debugs": 20, })
		self.test_case.debugs()

		self.test_case.loggy.close()
		with open(force_sdbg) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_sdbg-Irma.debugs INFO : Must be logged",
				"@force_sdbg-Irma.debugs WARNING : Must be logged",
				"@force_sdbg-Irma.debugs ERROR : Must be logged",
				"@force_sdbg-Irma.debugs CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(force_sdbg)
		self.test_case.loggy.handover_mode = False
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.debugs": 20, })
		self.test_case.debugs()

		self.test_case.loggy.close()
		with open(force_sdbg) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@force_sdbg INFO : Must be logged",
				"@force_sdbg WARNING : Must be logged",
				"@force_sdbg ERROR : Must be logged",
				"@force_sdbg CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(force_sdbg): os.remove(force_sdbg)








	def test_force_invalids(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name	= "force_invalids"
				handler		= self.CONTRIB_HANDLER


		self.test_case = Irma()
		for level in enumerate(( None,( 10, ),[ 10 ],{ 10 },{ "level": 10 }, print, object )):
			with self.subTest(forcing_level=level):

				errmsg = rf"Level to force must be numeric, got \"{level}\""
				errmsg = errmsg.replace("(",r"\(").replace(")",r"\)")
				errmsg = errmsg.replace("{",r"\{").replace("}",r"\}")
				errmsg = errmsg.replace("[",r"\[").replace("]",r"\]")

				self.assertRaisesRegex(

					TypeError,
					errmsg,
					self.test_case.loggy.force,
					level=level
				)


		forced = self.test_case.loggy.force(

			"OOH", "EEH", "OOH", "AAH", "AAH", "TING", "TANG", "WALLA", "WALLA", "BING", "BANG",
			level=50
		)
		self.assertEqual(forced,0)




	def test_forced_or_init_raise(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				init_name	= "forced_or_init_raise"
				handler		= self.CONTRIB_HANDLER
				force_debug	= "*.debugs",

			class debugs(ContribCase.Levels.debugs):	pass


		self.test_case = Irma()
		current_p = re.compile(".*.debugs")
		self.assertTrue(hasattr(self.test_case.loggy, "forcing_map"))
		self.assertIsInstance(self.test_case.loggy.forcing_map, dict)
		self.assertEqual(self.test_case.loggy.forcing_map,{ current_p: 10 })
		self.assertTrue(hasattr(self.test_case.loggy, "handover_map"))
		self.assertIsInstance(self.test_case.loggy.handover_map, dict)
		self.assertEqual(

			self.test_case.loggy.handover_map,
			{
				"Irma":			20,
				"Irma.debugs":	10,
			}
		)
		del self.test_case.loggy.handover_map["Irma.debugs"]
		self.test_case.loggy.forcing_map[current_p] = "10"
		self.assertRaisesRegex(

			TypeError,
			r"Pattern \".\*.debugs\" mapped to force incorrect \"10\"",
			self.test_case.debugs,
		)




	def test_makefmt_raise(self):

		class Irma(Transmutable):
			class loggy(LibraryContrib): init_name = "makefmt_raise_1"


		self.test_case = Irma()
		del self.test_case.loggy.handler
		self.assertRaisesRegex(

			AttributeError,
			"Contributor has no handler",
			self.test_case.loggy.makefmt,
			"raises"
		)


		class Irma(Transmutable):
			class loggy(LibraryContrib): init_name = "makefmt_raise_2"


		self.test_case = Irma()
		self.test_case.loggy.handler = None
		self.assertRaisesRegex(

			ValueError,
			"Invalid contributor handler \"None\"",
			self.test_case.loggy.makefmt,
			"raises"
		)


		class Irma(Transmutable):
			class loggy(LibraryContrib): init_name = "makefmt_raise_3"


		self.test_case = Irma()
		self.test_case.loggy.contribfmt = None
		self.assertRaisesRegex(

			TypeError,
			"Invalid contributor formatting dictionary \"None\"",
			self.test_case.loggy.makefmt,
			"raises"
		)
		self.test_case.loggy.contribfmt = {}
		self.assertRaisesRegex(

			TypeError,
			"Invalid contributor formatting dictionary \"{}\"",
			self.test_case.loggy.makefmt,
			"raises"
		)








	def test_valid_fmt_field(self):

		valid_fmt_field = str(self.IRMA_ROOT /"valid_fmt_field.loggy")
		self.make_loggy_file(valid_fmt_field)

		class Irma(Transmutable):
			class loggy(LibraryContrib):

				handler		= valid_fmt_field
				init_name	= "valid_fmt_field"
				contribfmt	= {

					"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
					"datefmt": "%Y-%m-%d %H:%M",
				}


			class infos(ContribCase.Levels.infos):	pass


		self.test_case = Irma()
		loggy = []
		altdatefmt = re.compile(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d ")
		self.test_case.infos()

		self.test_case.loggy.close()
		with open(valid_fmt_field) as case_loggy:
			for line in case_loggy:

				_line = line.rstrip("\n")
				self.assertTrue(altdatefmt.fullmatch(_line[:17]))
				loggy.append(_line[17:])

		self.assertEqual(
			loggy,
			[
				"@valid_fmt_field INFO - Must be logged",
				"@valid_fmt_field WARNING - Must be logged",
				"@valid_fmt_field ERROR - Must be logged",
				"@valid_fmt_field CRITICAL - Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(valid_fmt_field)
		self.test_case.loggy.handover_mode = True
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.test_case.infos()

		self.test_case.loggy.close()
		with open(valid_fmt_field) as case_loggy:
			for line in case_loggy:

				_line = line.rstrip("\n")
				self.assertTrue(altdatefmt.fullmatch(_line[:17]))
				loggy.append(_line[17:])

		self.assertEqual(
			loggy,
			[
				"@valid_fmt_field-Irma.infos INFO - Must be logged",
				"@valid_fmt_field-Irma.infos WARNING - Must be logged",
				"@valid_fmt_field-Irma.infos ERROR - Must be logged",
				"@valid_fmt_field-Irma.infos CRITICAL - Must be logged",
			]
		)
		if	os.path.isfile(valid_fmt_field): os.remove(valid_fmt_field)








	def test_valid_fmt_arg(self):

		valid_fmt_arg = str(self.IRMA_ROOT /"valid_fmt_arg.loggy")
		self.make_loggy_file(valid_fmt_arg)

		class Irma(Transmutable):
			class infos(ContribCase.Levels.infos):	pass


		self.test_case = Irma(

			LibraryContrib(

				handler=valid_fmt_arg,
				init_name="valid_fmt_arg",
				contribfmt={

					"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s - %(message)s",
					"datefmt": "%Y-%m-%d %H:%M",
				}
			)
		)
		loggy = []
		altdatefmt = re.compile(r"\d\d\d\d-\d\d-\d\d \d\d:\d\d ")
		self.test_case.infos()

		self.test_case.loggy.close()
		with open(valid_fmt_arg) as case_loggy:
			for line in case_loggy:

				_line = line.rstrip("\n")
				self.assertTrue(altdatefmt.fullmatch(_line[:17]))
				loggy.append(_line[17:])

		self.assertEqual(
			loggy,
			[
				"@valid_fmt_arg INFO - Must be logged",
				"@valid_fmt_arg WARNING - Must be logged",
				"@valid_fmt_arg ERROR - Must be logged",
				"@valid_fmt_arg CRITICAL - Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(valid_fmt_arg)
		self.test_case.loggy.handover_mode = True
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.test_case.infos()

		self.test_case.loggy.close()
		with open(valid_fmt_arg) as case_loggy:
			for line in case_loggy:

				_line = line.rstrip("\n")
				self.assertTrue(altdatefmt.fullmatch(_line[:17]))
				loggy.append(_line[17:])

		self.assertEqual(
			loggy,
			[
				"@valid_fmt_arg-Irma.infos INFO - Must be logged",
				"@valid_fmt_arg-Irma.infos WARNING - Must be logged",
				"@valid_fmt_arg-Irma.infos ERROR - Must be logged",
				"@valid_fmt_arg-Irma.infos CRITICAL - Must be logged",
			]
		)
		if	os.path.isfile(valid_fmt_arg): os.remove(valid_fmt_arg)








	def test_invalid_fmt_field(self):

		for fmtr in (
			{
				"%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"%d/%m/%Y %H%M",
			},
			{
				"FMT": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": "%d/%m/%Y %H%M",
			},
			{
				"fmt": 42,
				"datefmt": "%d/%m/%Y %H%M",
			},
			{
				"fmt": "%(asctime)s @%(name)s %(levelname)s : %(message)s",
				"datefmt": "%d/%m/%Y %H%M",
			},
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"DATEFMT": "%d/%m/%Y %H%M",
			},
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": 42,
			},
		):
			class Irma(Transmutable):
				class loggy(LibraryContrib): contribfmt = fmtr

			self.assertRaisesRegex(

				TypeError,
				"No valid contributor formatter provided",
				Irma
			)




	def test_invalid_fmt_arg(self):

		for fmtr in (
			{
				"%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"%d/%m/%Y %H%M",
			},
			{
				"FMT": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": "%d/%m/%Y %H%M",
			},
			{
				"fmt": 42,
				"datefmt": "%d/%m/%Y %H%M",
			},
			{
				"fmt": "%(asctime)s @%(name)s %(levelname)s : %(message)s",
				"datefmt": "%d/%m/%Y %H%M",
			},
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"DATEFMT": "%d/%m/%Y %H%M",
			},
			{
				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": 42,
			},
		):	self.assertRaisesRegex(

				TypeError,
				"No valid contributor formatter provided",
				LibraryContrib,
				contribfmt=fmtr,
			)








	def test_non_Transmutable(self):

		non_transmutable = str(self.IRMA_ROOT /"non_transmutable.loggy")

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		logger1 = LibraryContrib(init_name="non1", handler=non_transmutable)
		logger2 = LibraryContrib(init_name="non2", init_level=10, handler=non_transmutable)
		logger3 = LibraryContrib(init_name="non3", init_level=30, handler=non_transmutable)
		logger4 = LibraryContrib(init_name="non4", init_level=40, handler=non_transmutable)
		logger5 = LibraryContrib(init_name="non5", init_level=50, handler=non_transmutable)

		non = NonTransmutable()

		self.make_loggy_file(non_transmutable)
		non.action(logger1)
		logger1.close()
		loggy = []

		with open(non_transmutable) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@non1 INFO : Action done",
				"@non1 WARNING : Action done",
				"@non1 ERROR : Action done",
				"@non1 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable)
		non.action(logger2)
		logger2.close()
		loggy = []

		with open(non_transmutable) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@non2 DEBUG : Action done",
				"@non2 INFO : Action done",
				"@non2 WARNING : Action done",
				"@non2 ERROR : Action done",
				"@non2 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable)
		non.action(logger3)
		logger3.close()
		loggy = []

		with open(non_transmutable) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@non3 WARNING : Action done",
				"@non3 ERROR : Action done",
				"@non3 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable)
		non.action(logger4)
		logger4.close()
		loggy = []

		with open(non_transmutable) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@non4 ERROR : Action done",
				"@non4 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable)
		non.action(logger5)
		logger5.close()
		loggy = []

		with open(non_transmutable) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@non5 CRITICAL : Action done",
			]
		)
		if	os.path.isfile(non_transmutable): os.remove(non_transmutable)








	def test_non_Transmutable_field(self):

		non_transmutable_field = str(self.IRMA_ROOT /"non_transmutable_field.loggy")

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		class One(NonTransmutable):
			def __init__(self):

				self.logger = LibraryContrib(

					init_name="nonf1",
					handler=non_transmutable_field
				)

		class Two(NonTransmutable):
			def __init__(self):

				self.logger = LibraryContrib(

					init_name="nonf2",
					init_level=10,
					handler=non_transmutable_field
				)

		class Three(NonTransmutable):
			def __init__(self):

				self.logger = LibraryContrib(

					init_name="nonf3",
					init_level=30,
					handler=non_transmutable_field
				)

		class Four(NonTransmutable):
			def __init__(self):

				self.logger = LibraryContrib(

					init_name="nonf4",
					init_level=40,
					handler=non_transmutable_field
				)

		class Five(NonTransmutable):
			def __init__(self):

				self.logger = LibraryContrib(

					init_name="nonf5",
					init_level=50,
					handler=non_transmutable_field
				)

		self.make_loggy_file(non_transmutable_field)
		one = One()
		one.action()
		one.logger.close()
		loggy = []

		with open(non_transmutable_field) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonf1 INFO : Action done",
				"@nonf1 WARNING : Action done",
				"@nonf1 ERROR : Action done",
				"@nonf1 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable_field)
		two = Two()
		two.action()
		two.logger.close()
		loggy = []

		with open(non_transmutable_field) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonf2 DEBUG : Action done",
				"@nonf2 INFO : Action done",
				"@nonf2 WARNING : Action done",
				"@nonf2 ERROR : Action done",
				"@nonf2 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable_field)
		three = Three()
		three.action()
		three.logger.close()
		loggy = []

		with open(non_transmutable_field) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonf3 WARNING : Action done",
				"@nonf3 ERROR : Action done",
				"@nonf3 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable_field)
		four = Four()
		four.action()
		four.logger.close()
		loggy = []

		with open(non_transmutable_field) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonf4 ERROR : Action done",
				"@nonf4 CRITICAL : Action done",
			]
		)

		self.make_loggy_file(non_transmutable_field)
		five = Five()
		five.action()
		five.logger.close()
		loggy = []

		with open(non_transmutable_field) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonf5 CRITICAL : Action done",
			]
		)
		if	os.path.isfile(non_transmutable_field): os.remove(non_transmutable_field)








if __name__ == "__main__" : unittest.main(verbosity=2)







