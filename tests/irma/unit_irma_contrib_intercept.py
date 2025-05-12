import	os
import	unittest
from	time								import sleep
from	logging								import Logger
from	logging								import StreamHandler
from	logging								import FileHandler
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.time_turner.timers	import DIRTtimer
from	pygwarts.tests.irma					import IrmaTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.contrib.intercept		import ContribInterceptor
from	pygwarts.irma.contrib.intercept		import PoolHoist








class ContribInterceptingCase(IrmaTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.INTERCEPT_HANDLER): os.remove(cls.INTERCEPT_HANDLER)


	class DebugAugmentor(ContribInterceptor):

		def __call__(self):
			class Interceptor(self.layer):

				def debug(self, message :str): return super().debug(f"{message} (augmented)")
			return	Interceptor

	class InfoAugmentor(ContribInterceptor):

		def __call__(self):
			class Interceptor(self.layer):

				def info(self, message :str): return super().info(f"{message} (augmented)")
			return	Interceptor

	class WarningAugmentor(ContribInterceptor):

		def __call__(self):
			class Interceptor(self.layer):

				def warning(self, message :str): return super().warning(f"{message} (augmented)")
			return	Interceptor

	class ErrorAugmentor(ContribInterceptor):

		def __call__(self):
			class Interceptor(self.layer):

				def error(self, message :str): return super().error(f"{message} (augmented)")
			return	Interceptor

	class CriticalAugmentor(ContribInterceptor):

		def __call__(self):
			class Interceptor(self.layer):

				def critical(self, message :str): return super().critical(f"{message} (augmented)")
			return	Interceptor

	class InfoHoist(ContribInterceptor):

		def __call__(self):
			class Interceptor(self.layer):

				def info(self, message :str):
					logged = super().info(message)
					if hasattr(self, "buffer_insert"): self.buffer_insert(message)
					return logged
			return	Interceptor

	class ReleaseWriter1(ContribInterceptor):
		def __call__(self):

			class Interceptor(self.layer):
				def buffer_release(self, *args, **kwargs):

					buffer_dump = super().buffer_release(*args, **kwargs)
					with open(

						IrmaTestCase.IRMA_ROOT /"ih2w1.release",
						"w"
					)	as	writer:
						for line in buffer_dump : writer.write(f"{line}\n")
			return	Interceptor

	class ReleaseWriter2(PoolHoist):
		def __call__(self):

			class Interceptor(super().__call__()):
				def buffer_release(self, *args, **kwargs):

					buffer_dump = super().buffer_release(*args, **kwargs)
					with open(

						IrmaTestCase.IRMA_ROOT /"ih2w2.release",
						"w"
					)	as	writer:
						for line in buffer_dump : writer.write(f"{line}\n")
			return	Interceptor


	def test_PoolHoist_default_members(self):
		class Irma(Transmutable):

			@PoolHoist
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

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_name_default_members(self):
		class Irma(Transmutable):

			@PoolHoist
			class shmoggy(LibraryContrib): pass


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

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_escalated_default_members(self):

		class Irma(Transmutable):
			class Shirma(Transmutable):

				@PoolHoist
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
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.Shirma": 20 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma.Shirma", "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_escalated_name_default_members(self):

		class Irma(Transmutable):
			class Shirma(Transmutable):

				@PoolHoist
				class shmoggy(LibraryContrib): pass


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
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.Shirma": 20 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma.Shirma", "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_field_members(self):
		class Irma(Transmutable):

			@PoolHoist
			class loggy(LibraryContrib):

				handler			= self.INTERCEPT_HANDLER
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

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_name_field_members(self):
		class Irma(Transmutable):

			@PoolHoist
			class shmoggy(LibraryContrib):

				handler			= self.INTERCEPT_HANDLER
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

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_escalated_field_members(self):

		class Irma(Transmutable):
			class Shirma(Transmutable):

				@PoolHoist
				class loggy(LibraryContrib):

					handler			= self.INTERCEPT_HANDLER
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
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 50, "Irma.Shirma": 50 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma.Shirma", "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_PoolHoist_escalated_name_field_members(self):

		class Irma(Transmutable):
			class Shirma(Transmutable):

				@PoolHoist
				class shmoggy(LibraryContrib):

					handler			= self.INTERCEPT_HANDLER
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
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 50, "Irma.Shirma": 50 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma.Shirma", "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_outer_PoolHoist_default_members(self):
		class Outdoor(Transmutable):

			@PoolHoist
			class loggy(LibraryContrib):	pass
		class Irma(Outdoor):				pass


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

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_outer_PoolHoist_name_default_members(self):
		class Outdoor(Transmutable):

			@PoolHoist
			class shmoggy(LibraryContrib):	pass
		class Irma(Outdoor):				pass


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

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_outer_PoolHoist_escalated_default_members(self):

		class Outdoor(Transmutable):
			class Shirma(Transmutable):

				@PoolHoist
				class loggy(LibraryContrib):	pass
		class Irma(Outdoor):					pass


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
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.Shirma": 20 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma.Shirma", "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_outer_PoolHoist_escalated_name_default_members(self):

		class Outdoor(Transmutable):
			class Shirma(Transmutable):

				@PoolHoist
				class shmoggy(LibraryContrib):	pass
		class Irma(Outdoor):					pass


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
		self.assertEqual(self.test_case.loggy.handover_map, { "Irma": 20, "Irma.Shirma": 20 })

		self.assertTrue(hasattr(self.test_case.loggy, "contributor_name"))
		self.assertIsNone(self.test_case.loggy.contributor_name)
		self.assertTrue(hasattr(self.test_case.loggy, "handover_order"))
		self.assertEqual(self.test_case.loggy.handover_order, [ "Irma.Shirma", "Irma" ])
		self.assertTrue(hasattr(self.test_case.loggy, "contributor"))
		self.assertIsInstance(self.test_case.loggy.contributor, Logger)

		self.assertTrue(hasattr(self.test_case.loggy, "POOL_TIMER"))
		self.assertEqual(self.test_case.loggy.POOL_TIMER, 5)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_LIMIT"))
		self.assertEqual(self.test_case.loggy.POOL_LIMIT, 50)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_NAME"))
		self.assertIsInstance(self.test_case.loggy.POOL_NAME, str)
		self.assertTrue(hasattr(self.test_case.loggy, "POOL_STATE"))
		self.assertEqual(self.test_case.loggy.POOL_STATE, 0)
		self.assertTrue(hasattr(self.test_case.loggy, "BUFFER"))
		self.assertEqual(self.test_case.loggy.BUFFER, [])








	def test_debug_augmentor(self):

		debug_aug = str(self.IRMA_ROOT /"debug_aug.loggy")
		self.make_loggy_file(debug_aug)

		class Irma(Transmutable):

			@ContribInterceptingCase.DebugAugmentor
			class loggy(LibraryContrib):

				handler		= debug_aug
				init_name	= "debug_aug"
				init_level	= 10

			class Levels(ContribInterceptingCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(debug_aug) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@debug_aug-Irma.Levels.debugs DEBUG : Must be logged (augmented)",
				"@debug_aug-Irma.Levels.debugs INFO : Must be logged",
				"@debug_aug-Irma.Levels.debugs WARNING : Must be logged",
				"@debug_aug-Irma.Levels.debugs ERROR : Must be logged",
				"@debug_aug-Irma.Levels.debugs CRITICAL : Must be logged",

				"@debug_aug-Irma.Levels.infos DEBUG : Must be logged (augmented)",
				"@debug_aug-Irma.Levels.infos INFO : Must be logged",
				"@debug_aug-Irma.Levels.infos WARNING : Must be logged",
				"@debug_aug-Irma.Levels.infos ERROR : Must be logged",
				"@debug_aug-Irma.Levels.infos CRITICAL : Must be logged",

				"@debug_aug-Irma.Levels.warnings DEBUG : Must be logged (augmented)",
				"@debug_aug-Irma.Levels.warnings INFO : Must be logged",
				"@debug_aug-Irma.Levels.warnings WARNING : Must be logged",
				"@debug_aug-Irma.Levels.warnings ERROR : Must be logged",
				"@debug_aug-Irma.Levels.warnings CRITICAL : Must be logged",

				"@debug_aug-Irma.Levels.errors DEBUG : Must be logged (augmented)",
				"@debug_aug-Irma.Levels.errors INFO : Must be logged",
				"@debug_aug-Irma.Levels.errors WARNING : Must be logged",
				"@debug_aug-Irma.Levels.errors ERROR : Must be logged",
				"@debug_aug-Irma.Levels.errors CRITICAL : Must be logged",

				"@debug_aug-Irma.Levels.criticals DEBUG : Must be logged (augmented)",
				"@debug_aug-Irma.Levels.criticals INFO : Must be logged",
				"@debug_aug-Irma.Levels.criticals WARNING : Must be logged",
				"@debug_aug-Irma.Levels.criticals ERROR : Must be logged",
				"@debug_aug-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(debug_aug): os.remove(debug_aug)




	def test_info_augmentor(self):

		info_aug = str(self.IRMA_ROOT /"info_aug.loggy")
		self.make_loggy_file(info_aug)

		class Irma(Transmutable):

			@ContribInterceptingCase.DebugAugmentor
			@ContribInterceptingCase.InfoAugmentor
			class loggy(LibraryContrib):

				handler		= info_aug
				init_name	= "info_aug"
				init_level	= 10

			class Levels(ContribInterceptingCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(info_aug) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@info_aug-Irma.Levels.debugs DEBUG : Must be logged (augmented)",
				"@info_aug-Irma.Levels.debugs INFO : Must be logged (augmented)",
				"@info_aug-Irma.Levels.debugs WARNING : Must be logged",
				"@info_aug-Irma.Levels.debugs ERROR : Must be logged",
				"@info_aug-Irma.Levels.debugs CRITICAL : Must be logged",

				"@info_aug-Irma.Levels.infos DEBUG : Must be logged (augmented)",
				"@info_aug-Irma.Levels.infos INFO : Must be logged (augmented)",
				"@info_aug-Irma.Levels.infos WARNING : Must be logged",
				"@info_aug-Irma.Levels.infos ERROR : Must be logged",
				"@info_aug-Irma.Levels.infos CRITICAL : Must be logged",

				"@info_aug-Irma.Levels.warnings DEBUG : Must be logged (augmented)",
				"@info_aug-Irma.Levels.warnings INFO : Must be logged (augmented)",
				"@info_aug-Irma.Levels.warnings WARNING : Must be logged",
				"@info_aug-Irma.Levels.warnings ERROR : Must be logged",
				"@info_aug-Irma.Levels.warnings CRITICAL : Must be logged",

				"@info_aug-Irma.Levels.errors DEBUG : Must be logged (augmented)",
				"@info_aug-Irma.Levels.errors INFO : Must be logged (augmented)",
				"@info_aug-Irma.Levels.errors WARNING : Must be logged",
				"@info_aug-Irma.Levels.errors ERROR : Must be logged",
				"@info_aug-Irma.Levels.errors CRITICAL : Must be logged",

				"@info_aug-Irma.Levels.criticals DEBUG : Must be logged (augmented)",
				"@info_aug-Irma.Levels.criticals INFO : Must be logged (augmented)",
				"@info_aug-Irma.Levels.criticals WARNING : Must be logged",
				"@info_aug-Irma.Levels.criticals ERROR : Must be logged",
				"@info_aug-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(info_aug): os.remove(info_aug)




	def test_warn_augmentor(self):

		warn_aug = str(self.IRMA_ROOT /"warn_aug.loggy")
		self.make_loggy_file(warn_aug)

		class Irma(Transmutable):

			@ContribInterceptingCase.WarningAugmentor
			@ContribInterceptingCase.InfoAugmentor
			@ContribInterceptingCase.DebugAugmentor
			@PoolHoist
			class loggy(LibraryContrib):

				handler		= warn_aug
				init_name	= "warn_aug"
				init_level	= 10

			class Levels(ContribInterceptingCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(warn_aug) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@warn_aug-Irma.Levels.debugs DEBUG : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.debugs INFO : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.debugs WARNING : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.debugs ERROR : Must be logged",
				"@warn_aug-Irma.Levels.debugs CRITICAL : Must be logged",

				"@warn_aug-Irma.Levels.infos DEBUG : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.infos INFO : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.infos WARNING : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.infos ERROR : Must be logged",
				"@warn_aug-Irma.Levels.infos CRITICAL : Must be logged",

				"@warn_aug-Irma.Levels.warnings DEBUG : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.warnings INFO : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.warnings WARNING : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.warnings ERROR : Must be logged",
				"@warn_aug-Irma.Levels.warnings CRITICAL : Must be logged",

				"@warn_aug-Irma.Levels.errors DEBUG : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.errors INFO : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.errors WARNING : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.errors ERROR : Must be logged",
				"@warn_aug-Irma.Levels.errors CRITICAL : Must be logged",

				"@warn_aug-Irma.Levels.criticals DEBUG : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.criticals INFO : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.criticals WARNING : Must be logged (augmented)",
				"@warn_aug-Irma.Levels.criticals ERROR : Must be logged",
				"@warn_aug-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(warn_aug): os.remove(warn_aug)




	def test_error_augmentor(self):

		error_aug = str(self.IRMA_ROOT /"error_aug.loggy")
		self.make_loggy_file(error_aug)

		class Irma(Transmutable):

			@ContribInterceptingCase.WarningAugmentor
			@ContribInterceptingCase.InfoAugmentor
			@PoolHoist
			@ContribInterceptingCase.DebugAugmentor
			@ContribInterceptingCase.ErrorAugmentor
			class loggy(LibraryContrib):

				handler		= error_aug
				init_name	= "error_aug"
				init_level	= 10

			class Levels(ContribInterceptingCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(error_aug) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@error_aug-Irma.Levels.debugs DEBUG : Must be logged (augmented)",
				"@error_aug-Irma.Levels.debugs INFO : Must be logged (augmented)",
				"@error_aug-Irma.Levels.debugs WARNING : Must be logged (augmented)",
				"@error_aug-Irma.Levels.debugs ERROR : Must be logged (augmented)",
				"@error_aug-Irma.Levels.debugs CRITICAL : Must be logged",

				"@error_aug-Irma.Levels.infos DEBUG : Must be logged (augmented)",
				"@error_aug-Irma.Levels.infos INFO : Must be logged (augmented)",
				"@error_aug-Irma.Levels.infos WARNING : Must be logged (augmented)",
				"@error_aug-Irma.Levels.infos ERROR : Must be logged (augmented)",
				"@error_aug-Irma.Levels.infos CRITICAL : Must be logged",

				"@error_aug-Irma.Levels.warnings DEBUG : Must be logged (augmented)",
				"@error_aug-Irma.Levels.warnings INFO : Must be logged (augmented)",
				"@error_aug-Irma.Levels.warnings WARNING : Must be logged (augmented)",
				"@error_aug-Irma.Levels.warnings ERROR : Must be logged (augmented)",
				"@error_aug-Irma.Levels.warnings CRITICAL : Must be logged",

				"@error_aug-Irma.Levels.errors DEBUG : Must be logged (augmented)",
				"@error_aug-Irma.Levels.errors INFO : Must be logged (augmented)",
				"@error_aug-Irma.Levels.errors WARNING : Must be logged (augmented)",
				"@error_aug-Irma.Levels.errors ERROR : Must be logged (augmented)",
				"@error_aug-Irma.Levels.errors CRITICAL : Must be logged",

				"@error_aug-Irma.Levels.criticals DEBUG : Must be logged (augmented)",
				"@error_aug-Irma.Levels.criticals INFO : Must be logged (augmented)",
				"@error_aug-Irma.Levels.criticals WARNING : Must be logged (augmented)",
				"@error_aug-Irma.Levels.criticals ERROR : Must be logged (augmented)",
				"@error_aug-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(error_aug): os.remove(error_aug)




	def test_critical_augmentor(self):

		crit_aug = str(self.IRMA_ROOT /"crit_aug.loggy")
		self.make_loggy_file(crit_aug)

		class Irma(Transmutable):

			@PoolHoist
			@ContribInterceptingCase.CriticalAugmentor
			@ContribInterceptingCase.ErrorAugmentor
			@ContribInterceptingCase.WarningAugmentor
			@ContribInterceptingCase.InfoAugmentor
			@ContribInterceptingCase.DebugAugmentor
			class loggy(LibraryContrib):

				handler		= crit_aug
				init_name	= "crit_aug"
				init_level	= 10

			class Levels(ContribInterceptingCase.Levels):	pass


		loggy = []
		self.test_case = Irma()
		self.test_case.Levels.debugs()
		self.test_case.Levels.infos()
		self.test_case.Levels.warnings()
		self.test_case.Levels.errors()
		self.test_case.Levels.criticals()


		self.test_case.loggy.close()
		with open(crit_aug) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@crit_aug-Irma.Levels.debugs DEBUG : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.debugs INFO : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.debugs WARNING : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.debugs ERROR : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.debugs CRITICAL : Must be logged (augmented)",

				"@crit_aug-Irma.Levels.infos DEBUG : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.infos INFO : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.infos WARNING : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.infos ERROR : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.infos CRITICAL : Must be logged (augmented)",

				"@crit_aug-Irma.Levels.warnings DEBUG : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.warnings INFO : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.warnings WARNING : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.warnings ERROR : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.warnings CRITICAL : Must be logged (augmented)",

				"@crit_aug-Irma.Levels.errors DEBUG : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.errors INFO : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.errors WARNING : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.errors ERROR : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.errors CRITICAL : Must be logged (augmented)",

				"@crit_aug-Irma.Levels.criticals DEBUG : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.criticals INFO : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.criticals WARNING : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.criticals ERROR : Must be logged (augmented)",
				"@crit_aug-Irma.Levels.criticals CRITICAL : Must be logged (augmented)",
			]
		)
		if	os.path.isfile(crit_aug): os.remove(crit_aug)








	def test_PoolHoist_handover_switch(self):

		pool_handover = str(self.IRMA_ROOT /"pool_handover.loggy")
		self.make_loggy_file(pool_handover)

		class Irma(Transmutable):

			@PoolHoist
			class loggy(LibraryContrib):

				handler			= pool_handover
				init_name		= "pool_handover"
				force_handover	= True

			class Levels(ContribInterceptingCase.Levels):	pass


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
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.errors INFO : Must be logged",
				"@pool_handover-Irma.Levels.errors WARNING : Must be logged",
				"@pool_handover-Irma.Levels.errors ERROR : Must be logged",
				"@pool_handover-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
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
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.errors DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.errors INFO : Must be logged",
				"@pool_handover-Irma.Levels.errors WARNING : Must be logged",
				"@pool_handover-Irma.Levels.errors ERROR : Must be logged",
				"@pool_handover-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.errors DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.errors INFO : Must be logged",
				"@pool_handover-Irma.Levels.errors WARNING : Must be logged",
				"@pool_handover-Irma.Levels.errors ERROR : Must be logged",
				"@pool_handover-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
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
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.warnings DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.warnings INFO : Must be logged",
				"@pool_handover-Irma.Levels.warnings WARNING : Must be logged",
				"@pool_handover-Irma.Levels.warnings ERROR : Must be logged",
				"@pool_handover-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.Levels.criticals()

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.criticals INFO : Must be logged",
				"@pool_handover-Irma.Levels.criticals WARNING : Must be logged",
				"@pool_handover-Irma.Levels.criticals ERROR : Must be logged",
				"@pool_handover-Irma.Levels.criticals CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.Levels.warnings()

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.warnings DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.warnings INFO : Must be logged",
				"@pool_handover-Irma.Levels.warnings WARNING : Must be logged",
				"@pool_handover-Irma.Levels.warnings ERROR : Must be logged",
				"@pool_handover-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
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
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover INFO : Must be logged",
				"@pool_handover WARNING : Must be logged",
				"@pool_handover ERROR : Must be logged",
				"@pool_handover CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.errors DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.errors INFO : Must be logged",
				"@pool_handover-Irma.Levels.errors WARNING : Must be logged",
				"@pool_handover-Irma.Levels.errors ERROR : Must be logged",
				"@pool_handover-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover INFO : Must be logged",
				"@pool_handover WARNING : Must be logged",
				"@pool_handover ERROR : Must be logged",
				"@pool_handover CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
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
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.warnings DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.warnings INFO : Must be logged",
				"@pool_handover-Irma.Levels.warnings WARNING : Must be logged",
				"@pool_handover-Irma.Levels.warnings ERROR : Must be logged",
				"@pool_handover-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.warnings DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.warnings INFO : Must be logged",
				"@pool_handover-Irma.Levels.warnings WARNING : Must be logged",
				"@pool_handover-Irma.Levels.warnings ERROR : Must be logged",
				"@pool_handover-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.errors()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.errors DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.errors INFO : Must be logged",
				"@pool_handover-Irma.Levels.errors WARNING : Must be logged",
				"@pool_handover-Irma.Levels.errors ERROR : Must be logged",
				"@pool_handover-Irma.Levels.errors CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.warnings DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.warnings INFO : Must be logged",
				"@pool_handover-Irma.Levels.warnings WARNING : Must be logged",
				"@pool_handover-Irma.Levels.warnings ERROR : Must be logged",
				"@pool_handover-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = True
		self.test_case.Levels.infos()
		self.assertTrue(self.test_case.loggy.handover_mode)
		self.assertFalse(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.infos INFO : Must be logged",
				"@pool_handover-Irma.Levels.infos WARNING : Must be logged",
				"@pool_handover-Irma.Levels.infos ERROR : Must be logged",
				"@pool_handover-Irma.Levels.infos CRITICAL : Must be logged",
			]
		)


		loggy = []
		self.make_loggy_file(pool_handover)
		self.test_case.loggy.handover_mode = False
		self.test_case.Levels.warnings()
		self.assertFalse(self.test_case.loggy.handover_mode)
		self.assertTrue(self.test_case.loggy.handover_off)

		self.test_case.loggy.close()
		with open(pool_handover) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@pool_handover-Irma.Levels.warnings DEBUG : Must be logged",
				"@pool_handover-Irma.Levels.warnings INFO : Must be logged",
				"@pool_handover-Irma.Levels.warnings WARNING : Must be logged",
				"@pool_handover-Irma.Levels.warnings ERROR : Must be logged",
				"@pool_handover-Irma.Levels.warnings CRITICAL : Must be logged",
			]
		)
		if	os.path.isfile(pool_handover): os.remove(pool_handover)








	def test_info_hoist_to_writer1(self):

		ih2w1 = str(self.IRMA_ROOT /"ih2w1.loggy")
		self.make_loggy_file(ih2w1)


		ih2w1_release = str(self.IRMA_ROOT /"ih2w1.release")
		if os.path.isfile(ih2w1_release): os.remove(ih2w1_release)
		self.assertFalse(os.path.isfile(ih2w1_release))


		class Irma(Transmutable):
			def __init__(self, *args, **kwargs):

				super().__init__(*args, **kwargs)
				self.loggy.info("Irma entered the library")

			@ContribInterceptingCase.InfoHoist
			@ContribInterceptingCase.ReleaseWriter1
			@PoolHoist
			class loggy(LibraryContrib):

				handler		= ih2w1
				init_name	= "ih2w1"
				init_level	= 10

			class Levels(ContribInterceptingCase.Levels):	pass
			def __call__(self):

				self.Levels.debugs()
				self.Levels.infos()
				self.Levels.warnings()
				self.Levels.errors()
				self.Levels.criticals()


		loggy = []
		self.test_case = Irma()
		self.test_case()


		self.assertTrue(self.test_case.loggy.POOL_STATE)
		sleep(10.5)
		self.assertFalse(self.test_case.loggy.POOL_STATE)


		self.test_case.loggy.close()
		with open(ih2w1) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@ih2w1-Irma INFO : Irma entered the library",

				"@ih2w1-loggy.pool DEBUG : (pool-id-0) 24 symbols message inserted",
				"@ih2w1-loggy.pool DEBUG : (pool-id-0) buffer extended to 1 item",
				"@ih2w1-loggy.pool DEBUG : (pool-id-0) starting new thread",


				"@ih2w1-Irma.Levels.debugs DEBUG : Must be logged",
				"@ih2w1-Irma.Levels.debugs INFO : Must be logged",

				"@ih2w1-loggy.pool DEBUG : (pool-id-1) 14 symbols message inserted",
				"@ih2w1-loggy.pool DEBUG : (pool-id-1) buffer extended to 2 items",

				"@ih2w1-Irma.Levels.debugs WARNING : Must be logged",
				"@ih2w1-Irma.Levels.debugs ERROR : Must be logged",
				"@ih2w1-Irma.Levels.debugs CRITICAL : Must be logged",

				"@ih2w1-Irma.Levels.infos DEBUG : Must be logged",
				"@ih2w1-Irma.Levels.infos INFO : Must be logged",
				"@ih2w1-Irma.Levels.infos WARNING : Must be logged",
				"@ih2w1-Irma.Levels.infos ERROR : Must be logged",
				"@ih2w1-Irma.Levels.infos CRITICAL : Must be logged",
				"@ih2w1-Irma.Levels.warnings DEBUG : Must be logged",
				"@ih2w1-Irma.Levels.warnings INFO : Must be logged",
				"@ih2w1-Irma.Levels.warnings WARNING : Must be logged",
				"@ih2w1-Irma.Levels.warnings ERROR : Must be logged",
				"@ih2w1-Irma.Levels.warnings CRITICAL : Must be logged",
				"@ih2w1-Irma.Levels.errors DEBUG : Must be logged",
				"@ih2w1-Irma.Levels.errors INFO : Must be logged",
				"@ih2w1-Irma.Levels.errors WARNING : Must be logged",
				"@ih2w1-Irma.Levels.errors ERROR : Must be logged",
				"@ih2w1-Irma.Levels.errors CRITICAL : Must be logged",
				"@ih2w1-Irma.Levels.criticals DEBUG : Must be logged",
				"@ih2w1-Irma.Levels.criticals INFO : Must be logged",
				"@ih2w1-Irma.Levels.criticals WARNING : Must be logged",
				"@ih2w1-Irma.Levels.criticals ERROR : Must be logged",
				"@ih2w1-Irma.Levels.criticals CRITICAL : Must be logged",

				"@ih2w1-loggy.pool DEBUG : (pool-id-0) timer extended",
				"@ih2w1-loggy.pool DEBUG : (pool-id-0) was 10 seconds",
				"@ih2w1-loggy.pool DEBUG : (pool-id-0) was 2 items",
			]
		)


		self.assertTrue(os.path.isfile(ih2w1_release))
		buffer_content = []


		self.test_case.loggy.close()
		with open(ih2w1_release) as buffer:
			for line in buffer : buffer_content.append(line)


		self.assertEqual(buffer_content,[ "Irma entered the library\n", "Must be logged\n" ])
		if	os.path.isfile(ih2w1):			os.remove(ih2w1)
		if	os.path.isfile(ih2w1_release):	os.remove(ih2w1_release)








	@unittest.skipIf(os.name == "nt", "cannot test termination, cause windows cannot fork")
	def test_info_forked_hoist_to_writer2(self):

		ih2w2 = str(self.IRMA_ROOT /"ih2w2.loggy")
		self.make_loggy_file(ih2w2)


		ih2w2_release = str(self.IRMA_ROOT /"ih2w2.release")
		if os.path.isfile(ih2w2_release): os.remove(ih2w2_release)
		self.assertFalse(os.path.isfile(ih2w2_release))


		@DIRTtimer(T=1.5)
		class Irma(Transmutable):
			def __init__(self, *args, **kwargs):

				super().__init__(*args, **kwargs)
				self.loggy.info("Irma entered the library")

			@ContribInterceptingCase.ReleaseWriter2
			@ContribInterceptingCase.InfoHoist
			class loggy(LibraryContrib):

				handler		= ih2w2
				init_name	= "ih2w2"
				init_level	= 10
				pool_timer	= .5

			class Levels(ContribInterceptingCase.Levels):	pass
			def __call__(self):

				self.Levels.debugs()
				self.loggy.info("OOH EEH OOH AH AH")
				self.Levels.infos()
				self.Levels.warnings()
				self.loggy.info("TING TANG")
				self.Levels.errors()
				self.Levels.criticals()
				self.loggy.info("WALA WALA BING BANG")


		loggy = []
		self.test_case = Irma()
		self.test_case()
		sleep(1.5)


		self.test_case.loggy.close()
		with open(ih2w2) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])


		self.assertEqual(
			loggy,
			[
				"@ih2w2-Irma INFO : Irma entered the library",

				"@ih2w2-loggy.pool DEBUG : (pool-id-0) 24 symbols message inserted",
				"@ih2w2-loggy.pool DEBUG : (pool-id-0) buffer extended to 1 item",
				"@ih2w2-loggy.pool DEBUG : (pool-id-0) starting new thread",

				"@ih2w2-Irma DEBUG : Delay start timer 0.0 seconds",
				"@ih2w2-Irma DEBUG : Interval delay 0.0 seconds",
				"@ih2w2-Irma DEBUG : Repetition counter 1 time",
				"@ih2w2-Irma DEBUG : Termination timer 1.5 seconds",
				"@ih2w2-Irma DEBUG : Caller arguments: ()",
				r"@ih2w2-Irma DEBUG : Caller keyword arguments: {}",
				"@ih2w2-Irma DEBUG : DIRT iteration 1",
				"@ih2w2-Irma INFO : Starting 1.5 seconds timer for Irma",

				"@ih2w2-loggy.pool DEBUG : (pool-id-1) 35 symbols message inserted",
				"@ih2w2-loggy.pool DEBUG : (pool-id-1) buffer extended to 2 items",

				"@ih2w2-Irma.Levels.debugs DEBUG : Must be logged",
				"@ih2w2-Irma.Levels.debugs INFO : Must be logged",

				"@ih2w2-loggy.pool DEBUG : (pool-id-2) switching from MainProcess to Process-1",
				"@ih2w2-loggy.pool DEBUG : (pool-id-2) wiping 2 items buffer",
				"@ih2w2-loggy.pool DEBUG : (pool-id-2) 14 symbols message inserted",
				"@ih2w2-loggy.pool DEBUG : (pool-id-2) buffer extended to 1 item",
				"@ih2w2-loggy.pool DEBUG : (pool-id-2) starting new thread",

				"@ih2w2-Irma.Levels.debugs WARNING : Must be logged",
				"@ih2w2-Irma.Levels.debugs ERROR : Must be logged",
				"@ih2w2-Irma.Levels.debugs CRITICAL : Must be logged",

				"@ih2w2-Irma INFO : OOH EEH OOH AH AH",

				"@ih2w2-loggy.pool DEBUG : (pool-id-3) 17 symbols message inserted",
				"@ih2w2-loggy.pool DEBUG : (pool-id-3) buffer extended to 2 items",

				"@ih2w2-Irma.Levels.infos DEBUG : Must be logged",
				"@ih2w2-Irma.Levels.infos INFO : Must be logged",
				"@ih2w2-Irma.Levels.infos WARNING : Must be logged",
				"@ih2w2-Irma.Levels.infos ERROR : Must be logged",
				"@ih2w2-Irma.Levels.infos CRITICAL : Must be logged",
				"@ih2w2-Irma.Levels.warnings DEBUG : Must be logged",
				"@ih2w2-Irma.Levels.warnings INFO : Must be logged",
				"@ih2w2-Irma.Levels.warnings WARNING : Must be logged",
				"@ih2w2-Irma.Levels.warnings ERROR : Must be logged",
				"@ih2w2-Irma.Levels.warnings CRITICAL : Must be logged",

				"@ih2w2-Irma INFO : TING TANG",

				"@ih2w2-loggy.pool DEBUG : (pool-id-4) 9 symbols message inserted",
				"@ih2w2-loggy.pool DEBUG : (pool-id-4) buffer extended to 3 items",

				"@ih2w2-Irma.Levels.errors DEBUG : Must be logged",
				"@ih2w2-Irma.Levels.errors INFO : Must be logged",
				"@ih2w2-Irma.Levels.errors WARNING : Must be logged",
				"@ih2w2-Irma.Levels.errors ERROR : Must be logged",
				"@ih2w2-Irma.Levels.errors CRITICAL : Must be logged",
				"@ih2w2-Irma.Levels.criticals DEBUG : Must be logged",
				"@ih2w2-Irma.Levels.criticals INFO : Must be logged",
				"@ih2w2-Irma.Levels.criticals WARNING : Must be logged",
				"@ih2w2-Irma.Levels.criticals ERROR : Must be logged",
				"@ih2w2-Irma.Levels.criticals CRITICAL : Must be logged",

				"@ih2w2-Irma INFO : WALA WALA BING BANG",

				"@ih2w2-loggy.pool DEBUG : (pool-id-5) 19 symbols message inserted",
				"@ih2w2-loggy.pool DEBUG : (pool-id-5) buffer extended to 4 items",

				"@ih2w2-loggy.pool DEBUG : (pool-id-0) timer extended",
				"@ih2w2-loggy.pool DEBUG : (pool-id-0) was 1.0 seconds",
				"@ih2w2-loggy.pool DEBUG : (pool-id-0) was 2 items",

				"@ih2w2-loggy.pool DEBUG : (pool-id-2) timer extended",
				"@ih2w2-loggy.pool DEBUG : (pool-id-2) was 1.0 seconds",
				"@ih2w2-loggy.pool DEBUG : (pool-id-2) was 4 items",

				"@ih2w2-Irma DEBUG : Process Irma terminated",
			]
		)


		self.assertTrue(os.path.isfile(ih2w2_release))
		buffer_content = []


		self.test_case.loggy.close()
		with open(ih2w2_release) as buffer:
			for line in buffer : buffer_content.append(line)


		self.assertEqual(
			buffer_content,
			[
				"Must be logged\n",
				"OOH EEH OOH AH AH\n",
				"TING TANG\n",
				"WALA WALA BING BANG\n",
			]
		)
		if	os.path.isfile(ih2w2):			os.remove(ih2w2)
		if	os.path.isfile(ih2w2_release):	os.remove(ih2w2_release)








	def test_pool_limit(self):
		class Irma(Transmutable):

			@PoolHoist
			@ContribInterceptingCase.InfoHoist
			class loggy(LibraryContrib):

				handler		= self.INTERCEPT_HANDLER
				init_name	= "pool_limit"
				init_level	= 10
				pool_timer	= .1
				pool_limit	= 1

			class Levels(ContribInterceptingCase.Levels):	pass

		with self.assertLogs("pool_limit", 10) as case_loggy:

			self.test_case = Irma()
			for i in range(20):

				self.test_case.loggy.info(f"Current is {i}")
				sleep(.08)

		sleep(1)
		self.assertIn("DEBUG:pool_limit:(pool-id-0) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-0) buffer extended to 1 item", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-0) starting new thread", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-1) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-1) buffer extended to 2 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-2) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-2) buffer extended to 3 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-3) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-3) buffer extended to 4 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-4) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-4) buffer extended to 5 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-5) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-5) buffer extended to 6 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-6) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-6) buffer extended to 7 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-7) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-7) buffer extended to 8 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-8) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-8) buffer extended to 9 items", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-9) 12 symbols message inserted", case_loggy.output)
		self.assertIn("DEBUG:pool_limit:(pool-id-9) buffer extended to 10 items", case_loggy.output)

		# Following spaghetti is the monkey-patching for floats to be calculated very funny.
		# Originally was found that current test "loggy.pool" "buffer_time" will not be able to
		# succesfully sum up to 1.0, so for some different cases below handlings.
		try:			self.assertIn("DEBUG:pool_limit:(pool-id-0) was 10 items", case_loggy.output)
		except:
			try:		self.assertIn("DEBUG:pool_limit:(pool-id-0) was 11 items", case_loggy.output)
			except:
				try:	self.assertIn("DEBUG:pool_limit:(pool-id-0) was 12 items", case_loggy.output)
				except:	self.assertIn("DEBUG:pool_limit:(pool-id-0) was 13 items", case_loggy.output)








	def test_non_Transmutable_intercept(self):

		non_transmutable_i = str(self.IRMA_ROOT /"non_transmutable_i.loggy")

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		noni = NonTransmutable()

		@ContribInterceptingCase.InfoAugmentor
		class ContribOne(LibraryContrib):

			handler		= non_transmutable_i
			init_name	= "noni1"

		logger1 = ContribOne()()
		self.make_loggy_file(non_transmutable_i)
		noni.action(logger1)
		logger1.close()
		loggy = []

		with open(non_transmutable_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@noni1 INFO : Action done (augmented)",
				"@noni1 WARNING : Action done",
				"@noni1 ERROR : Action done",
				"@noni1 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.DebugAugmentor
		class ContribTwo(LibraryContrib):

			handler		= non_transmutable_i
			init_name	= "noni2"
			init_level	= 10

		logger2 = ContribTwo()()
		self.make_loggy_file(non_transmutable_i)
		noni.action(logger2)
		logger2.close()
		loggy = []

		with open(non_transmutable_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@noni2 DEBUG : Action done (augmented)",
				"@noni2 INFO : Action done",
				"@noni2 WARNING : Action done",
				"@noni2 ERROR : Action done",
				"@noni2 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.WarningAugmentor
		class ContribThree(LibraryContrib):

			handler		= non_transmutable_i
			init_name	= "noni3"
			init_level	= 30

		logger3 = ContribThree()()
		self.make_loggy_file(non_transmutable_i)
		noni.action(logger3)
		logger3.close()
		loggy = []

		with open(non_transmutable_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@noni3 WARNING : Action done (augmented)",
				"@noni3 ERROR : Action done",
				"@noni3 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.ErrorAugmentor
		class ContribFour(LibraryContrib):

			handler		= non_transmutable_i
			init_name	= "noni4"
			init_level	= 40

		logger4 = ContribFour()()
		self.make_loggy_file(non_transmutable_i)
		noni.action(logger4)
		logger4.close()
		loggy = []

		with open(non_transmutable_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@noni4 ERROR : Action done (augmented)",
				"@noni4 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.CriticalAugmentor
		class ContribFive(LibraryContrib):

			handler		= non_transmutable_i
			init_name	= "noni5"
			init_level	= 50

		logger5 = ContribFive()()
		self.make_loggy_file(non_transmutable_i)
		noni.action(logger5)
		logger5.close()
		loggy = []

		with open(non_transmutable_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@noni5 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_i): os.remove(non_transmutable_i)








	def test_non_Transmutable_args_intercept(self):

		non_transmutable_ai = str(self.IRMA_ROOT /"non_transmutable_ai.loggy")

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		nonai = NonTransmutable()

		@ContribInterceptingCase.InfoAugmentor
		class ContribOne(LibraryContrib):	pass
		logger1 = ContribOne()(handler=non_transmutable_ai, init_name="nonai1")
		self.make_loggy_file(non_transmutable_ai)
		nonai.action(logger1)
		logger1.close()
		loggy = []

		with open(non_transmutable_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonai1 INFO : Action done (augmented)",
				"@nonai1 WARNING : Action done",
				"@nonai1 ERROR : Action done",
				"@nonai1 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.DebugAugmentor
		class ContribTwo(LibraryContrib):	pass
		logger2 = ContribTwo()(handler=non_transmutable_ai, init_name="nonai2", init_level=10)
		self.make_loggy_file(non_transmutable_ai)
		nonai.action(logger2)
		logger2.close()
		loggy = []

		with open(non_transmutable_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonai2 DEBUG : Action done (augmented)",
				"@nonai2 INFO : Action done",
				"@nonai2 WARNING : Action done",
				"@nonai2 ERROR : Action done",
				"@nonai2 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.WarningAugmentor
		class ContribThree(LibraryContrib):	pass
		logger3 = ContribThree()(handler=non_transmutable_ai, init_name="nonai3", init_level=30)
		self.make_loggy_file(non_transmutable_ai)
		nonai.action(logger3)
		logger3.close()
		loggy = []

		with open(non_transmutable_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonai3 WARNING : Action done (augmented)",
				"@nonai3 ERROR : Action done",
				"@nonai3 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.ErrorAugmentor
		class ContribFour(LibraryContrib):	pass
		logger4 = ContribFour()(handler=non_transmutable_ai, init_name="nonai4", init_level=40)
		self.make_loggy_file(non_transmutable_ai)
		nonai.action(logger4)
		logger4.close()
		loggy = []

		with open(non_transmutable_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonai4 ERROR : Action done (augmented)",
				"@nonai4 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.CriticalAugmentor
		class ContribFive(LibraryContrib):	pass
		logger5 = ContribFive()(handler=non_transmutable_ai, init_name="nonai5", init_level=50)
		self.make_loggy_file(non_transmutable_ai)
		nonai.action(logger5)
		logger5.close()
		loggy = []

		with open(non_transmutable_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonai5 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_ai): os.remove(non_transmutable_ai)








	def test_non_Transmutable_field_intercept(self):

		non_transmutable_f_i = str(self.IRMA_ROOT /"non_transmutable_f_i.loggy")

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		@ContribInterceptingCase.InfoAugmentor
		class ContribOne(LibraryContrib):

			handler		= non_transmutable_f_i
			init_name	= "nonfi1"

		class One(NonTransmutable):
			def __init__(self): self.logger = ContribOne()()

		self.make_loggy_file(non_transmutable_f_i)
		one = One()
		one.action()
		one.logger.close()
		loggy = []

		with open(non_transmutable_f_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfi1 INFO : Action done (augmented)",
				"@nonfi1 WARNING : Action done",
				"@nonfi1 ERROR : Action done",
				"@nonfi1 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.DebugAugmentor
		class ContribTwo(LibraryContrib):

			handler		= non_transmutable_f_i
			init_name	= "nonfi2"
			init_level	= 10

		class Two(NonTransmutable):
			def __init__(self): self.logger = ContribTwo()()

		self.make_loggy_file(non_transmutable_f_i)
		two = Two()
		two.action()
		two.logger.close()
		loggy = []

		with open(non_transmutable_f_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfi2 DEBUG : Action done (augmented)",
				"@nonfi2 INFO : Action done",
				"@nonfi2 WARNING : Action done",
				"@nonfi2 ERROR : Action done",
				"@nonfi2 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.WarningAugmentor
		class ContribThree(LibraryContrib):

			handler		= non_transmutable_f_i
			init_name	= "nonfi3"
			init_level	= 30

		class Three(NonTransmutable):
			def __init__(self): self.logger = ContribThree()()

		self.make_loggy_file(non_transmutable_f_i)
		three = Three()
		three.action()
		three.logger.close()
		loggy = []

		with open(non_transmutable_f_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfi3 WARNING : Action done (augmented)",
				"@nonfi3 ERROR : Action done",
				"@nonfi3 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.ErrorAugmentor
		class ContribFour(LibraryContrib):

			handler		= non_transmutable_f_i
			init_name	= "nonfi4"
			init_level	= 40

		class Four(NonTransmutable):
			def __init__(self): self.logger = ContribFour()()

		self.make_loggy_file(non_transmutable_f_i)
		four = Four()
		four.action()
		four.logger.close()
		loggy = []

		with open(non_transmutable_f_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfi4 ERROR : Action done (augmented)",
				"@nonfi4 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.CriticalAugmentor
		class ContribFive(LibraryContrib):

			handler		= non_transmutable_f_i
			init_name	= "nonfi5"
			init_level	= 50

		class Five(NonTransmutable):
			def __init__(self): self.logger = ContribFive()()

		self.make_loggy_file(non_transmutable_f_i)
		five = Five()
		five.action()
		five.logger.close()
		loggy = []

		with open(non_transmutable_f_i) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfi5 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_f_i): os.remove(non_transmutable_f_i)








	def test_non_Transmutable_field_args_intercept(self):

		non_transmutable_f_ai = str(self.IRMA_ROOT /"non_transmutable_f_ai.loggy")

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		@ContribInterceptingCase.InfoAugmentor
		class ContribOne(LibraryContrib):	pass
		class One(NonTransmutable):
			def __init__(self):
				self.logger = ContribOne()(
					handler=non_transmutable_f_ai, init_name="nonfai1"
				)

		self.make_loggy_file(non_transmutable_f_ai)
		one = One()
		one.action()
		one.logger.close()
		loggy = []

		with open(non_transmutable_f_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfai1 INFO : Action done (augmented)",
				"@nonfai1 WARNING : Action done",
				"@nonfai1 ERROR : Action done",
				"@nonfai1 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.DebugAugmentor
		class ContribTwo(LibraryContrib):	pass
		class Two(NonTransmutable):
			def __init__(self):
				self.logger = ContribTwo()(
					handler=non_transmutable_f_ai, init_name="nonfai2", init_level=10
				)

		self.make_loggy_file(non_transmutable_f_ai)
		two = Two()
		two.action()
		two.logger.close()
		loggy = []

		with open(non_transmutable_f_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfai2 DEBUG : Action done (augmented)",
				"@nonfai2 INFO : Action done",
				"@nonfai2 WARNING : Action done",
				"@nonfai2 ERROR : Action done",
				"@nonfai2 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.WarningAugmentor
		class ContribThree(LibraryContrib):	pass
		class Three(NonTransmutable):
			def __init__(self):
				self.logger = ContribThree()(
					handler=non_transmutable_f_ai, init_name="nonfai3", init_level=30
				)

		self.make_loggy_file(non_transmutable_f_ai)
		three = Three()
		three.action()
		three.logger.close()
		loggy = []

		with open(non_transmutable_f_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfai3 WARNING : Action done (augmented)",
				"@nonfai3 ERROR : Action done",
				"@nonfai3 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.ErrorAugmentor
		class ContribFour(LibraryContrib):	pass
		class Four(NonTransmutable):
			def __init__(self):
				self.logger = ContribFour()(
					handler=non_transmutable_f_ai, init_name="nonfai4", init_level=40
				)

		self.make_loggy_file(non_transmutable_f_ai)
		four = Four()
		four.action()
		four.logger.close()
		loggy = []

		with open(non_transmutable_f_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfai4 ERROR : Action done (augmented)",
				"@nonfai4 CRITICAL : Action done",
			]
		)

		@ContribInterceptingCase.CriticalAugmentor
		class ContribFive(LibraryContrib):	pass
		class Five(NonTransmutable):
			def __init__(self):
				self.logger = ContribFive()(
					handler=non_transmutable_f_ai, init_name="nonfai5", init_level=50
				)

		self.make_loggy_file(non_transmutable_f_ai)
		five = Five()
		five.action()
		five.logger.close()
		loggy = []

		with open(non_transmutable_f_ai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfai5 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_f_ai): os.remove(non_transmutable_f_ai)








	def test_non_Transmutable_object(self):

		non_transmutable_oi = str(self.IRMA_ROOT /"non_transmutable_oi.loggy")

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		nonoi = NonTransmutable()

		logger1 = ContribInterceptingCase.InfoAugmentor(
			LibraryContrib
		)()(handler=non_transmutable_oi, init_name="nonoi1")

		self.make_loggy_file(non_transmutable_oi)
		nonoi.action(logger1)
		logger1.close()
		loggy = []

		with open(non_transmutable_oi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonoi1 INFO : Action done (augmented)",
				"@nonoi1 WARNING : Action done",
				"@nonoi1 ERROR : Action done",
				"@nonoi1 CRITICAL : Action done",
			]
		)

		logger2 = ContribInterceptingCase.DebugAugmentor(
			LibraryContrib
		)()(handler=non_transmutable_oi, init_name="nonoi2", init_level=10)

		self.make_loggy_file(non_transmutable_oi)
		nonoi.action(logger2)
		logger2.close()
		loggy = []

		with open(non_transmutable_oi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonoi2 DEBUG : Action done (augmented)",
				"@nonoi2 INFO : Action done",
				"@nonoi2 WARNING : Action done",
				"@nonoi2 ERROR : Action done",
				"@nonoi2 CRITICAL : Action done",
			]
		)

		logger3 = ContribInterceptingCase.WarningAugmentor(
			LibraryContrib
		)()(handler=non_transmutable_oi, init_name="nonoi3", init_level=30)

		self.make_loggy_file(non_transmutable_oi)
		nonoi.action(logger3)
		logger3.close()
		loggy = []

		with open(non_transmutable_oi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonoi3 WARNING : Action done (augmented)",
				"@nonoi3 ERROR : Action done",
				"@nonoi3 CRITICAL : Action done",
			]
		)

		logger4 = ContribInterceptingCase.ErrorAugmentor(
			LibraryContrib
		)()(handler=non_transmutable_oi, init_name="nonoi4", init_level=40)

		self.make_loggy_file(non_transmutable_oi)
		nonoi.action(logger4)
		logger4.close()
		loggy = []

		with open(non_transmutable_oi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonoi4 ERROR : Action done (augmented)",
				"@nonoi4 CRITICAL : Action done",
			]
		)

		logger5 = ContribInterceptingCase.CriticalAugmentor(
			LibraryContrib
		)()(handler=non_transmutable_oi, init_name="nonoi5", init_level=50)

		self.make_loggy_file(non_transmutable_oi)
		nonoi.action(logger5)
		logger5.close()
		loggy = []

		with open(non_transmutable_oi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonoi5 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_oi): os.remove(non_transmutable_oi)








	def test_non_Transmutable_object_field(self):

		non_transmutable_ofi = str(self.IRMA_ROOT /"non_transmutable_ofi.loggy")

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		class One(NonTransmutable):
			def __init__(self):
				self.logger = ContribInterceptingCase.InfoAugmentor(
					LibraryContrib
				)()(handler=non_transmutable_ofi, init_name="nonofi1")

		self.make_loggy_file(non_transmutable_ofi)
		one = One()
		one.action()
		one.logger.close()
		loggy = []

		with open(non_transmutable_ofi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonofi1 INFO : Action done (augmented)",
				"@nonofi1 WARNING : Action done",
				"@nonofi1 ERROR : Action done",
				"@nonofi1 CRITICAL : Action done",
			]
		)

		class Two(NonTransmutable):
			def __init__(self):
				self.logger = ContribInterceptingCase.DebugAugmentor(
					LibraryContrib
				)()(handler=non_transmutable_ofi, init_name="nonofi2", init_level=10)

		self.make_loggy_file(non_transmutable_ofi)
		two = Two()
		two.action()
		two.logger.close()
		loggy = []

		with open(non_transmutable_ofi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonofi2 DEBUG : Action done (augmented)",
				"@nonofi2 INFO : Action done",
				"@nonofi2 WARNING : Action done",
				"@nonofi2 ERROR : Action done",
				"@nonofi2 CRITICAL : Action done",
			]
		)

		class Three(NonTransmutable):
			def __init__(self):
				self.logger = ContribInterceptingCase.WarningAugmentor(
					LibraryContrib
				)()(handler=non_transmutable_ofi, init_name="nonofi3", init_level=30)

		self.make_loggy_file(non_transmutable_ofi)
		three = Three()
		three.action()
		three.logger.close()
		loggy = []

		with open(non_transmutable_ofi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonofi3 WARNING : Action done (augmented)",
				"@nonofi3 ERROR : Action done",
				"@nonofi3 CRITICAL : Action done",
			]
		)

		class Four(NonTransmutable):
			def __init__(self):
				self.logger = ContribInterceptingCase.ErrorAugmentor(
					LibraryContrib
				)()(handler=non_transmutable_ofi, init_name="nonofi4", init_level=40)

		self.make_loggy_file(non_transmutable_ofi)
		four = Four()
		four.action()
		four.logger.close()
		loggy = []

		with open(non_transmutable_ofi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonofi4 ERROR : Action done (augmented)",
				"@nonofi4 CRITICAL : Action done",
			]
		)

		class Five(NonTransmutable):
			def __init__(self):
				self.logger = ContribInterceptingCase.CriticalAugmentor(
					LibraryContrib
				)()(handler=non_transmutable_ofi, init_name="nonofi5", init_level=50)

		self.make_loggy_file(non_transmutable_ofi)
		five = Five()
		five.action()
		five.logger.close()
		loggy = []

		with open(non_transmutable_ofi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonofi5 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_ofi): os.remove(non_transmutable_ofi)








	def test_non_Transmutable_multi_intercept(self):

		non_transmutable_mi = str(self.IRMA_ROOT /"non_transmutable_mi.loggy")
		self.make_loggy_file(non_transmutable_mi)

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		nonmi = NonTransmutable()

		@ContribInterceptingCase.CriticalAugmentor
		@ContribInterceptingCase.ErrorAugmentor
		@ContribInterceptingCase.WarningAugmentor
		@ContribInterceptingCase.InfoAugmentor
		class MultiContrib(LibraryContrib):

			handler		= non_transmutable_mi
			init_name	= "nonmi"

		logger = MultiContrib()()
		nonmi.action(logger)
		logger.close()
		loggy = []

		with open(non_transmutable_mi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonmi INFO : Action done (augmented)",
				"@nonmi WARNING : Action done (augmented)",
				"@nonmi ERROR : Action done (augmented)",
				"@nonmi CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_mi): os.remove(non_transmutable_mi)




	def test_non_Transmutable_args_multi_intercept(self):

		non_transmutable_mai = str(self.IRMA_ROOT /"non_transmutable_mai.loggy")
		self.make_loggy_file(non_transmutable_mai)

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		nonmai = NonTransmutable()

		@ContribInterceptingCase.CriticalAugmentor
		@ContribInterceptingCase.ErrorAugmentor
		@ContribInterceptingCase.WarningAugmentor
		@ContribInterceptingCase.InfoAugmentor
		class MultiContrib(LibraryContrib):	pass

		logger = MultiContrib()(handler=non_transmutable_mai, init_name="nonmai1")
		nonmai.action(logger)
		logger.close()
		loggy = []

		with open(non_transmutable_mai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonmai1 INFO : Action done (augmented)",
				"@nonmai1 WARNING : Action done (augmented)",
				"@nonmai1 ERROR : Action done (augmented)",
				"@nonmai1 CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_mai): os.remove(non_transmutable_mai)




	def test_non_Transmutable_field_multi_intercept(self):

		non_transmutable_f_mi = str(self.IRMA_ROOT /"non_transmutable_f_mi.loggy")
		self.make_loggy_file(non_transmutable_f_mi)

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		@ContribInterceptingCase.CriticalAugmentor
		@ContribInterceptingCase.ErrorAugmentor
		@ContribInterceptingCase.WarningAugmentor
		@ContribInterceptingCase.InfoAugmentor
		class MultiContrib(LibraryContrib):

			handler		= non_transmutable_f_mi
			init_name	= "nonfmi"

		class Non(NonTransmutable):
			def __init__(self): self.logger = MultiContrib()()

		non = Non()
		non.action()
		non.logger.close()
		loggy = []

		with open(non_transmutable_f_mi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfmi INFO : Action done (augmented)",
				"@nonfmi WARNING : Action done (augmented)",
				"@nonfmi ERROR : Action done (augmented)",
				"@nonfmi CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_f_mi): os.remove(non_transmutable_f_mi)




	def test_non_Transmutable_field_args_multi_intercept(self):

		non_transmutable_f_mai = str(self.IRMA_ROOT /"non_transmutable_f_mai.loggy")
		self.make_loggy_file(non_transmutable_f_mai)

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		@ContribInterceptingCase.CriticalAugmentor
		@ContribInterceptingCase.ErrorAugmentor
		@ContribInterceptingCase.WarningAugmentor
		@ContribInterceptingCase.InfoAugmentor
		class MultiContrib(LibraryContrib):	pass
		class Non(NonTransmutable):
			def __init__(self):
				self.logger = MultiContrib()(handler=non_transmutable_f_mai, init_name="nonfmai")

		non = Non()
		non.action()
		non.logger.close()
		loggy = []

		with open(non_transmutable_f_mai) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonfmai INFO : Action done (augmented)",
				"@nonfmai WARNING : Action done (augmented)",
				"@nonfmai ERROR : Action done (augmented)",
				"@nonfmai CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_f_mai): os.remove(non_transmutable_f_mai)




	def test_non_Transmutable_multi_object(self):

		non_transmutable_moi = str(self.IRMA_ROOT /"non_transmutable_moi.loggy")
		self.make_loggy_file(non_transmutable_moi)

		class NonTransmutable:
			def action(self, logger :LibraryContrib):

				logger.debug("Action done")
				logger.info("Action done")
				logger.warning("Action done")
				logger.error("Action done")
				logger.critical("Action done")

		nonmoi = NonTransmutable()

		logger = ContribInterceptingCase.InfoAugmentor(
			ContribInterceptingCase.WarningAugmentor(
				ContribInterceptingCase.ErrorAugmentor(
					ContribInterceptingCase.CriticalAugmentor(
						LibraryContrib)
					)
				)
			)()(handler=non_transmutable_moi, init_name="nonmoi")

		nonmoi.action(logger)
		logger.close()
		loggy = []

		with open(non_transmutable_moi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonmoi INFO : Action done (augmented)",
				"@nonmoi WARNING : Action done (augmented)",
				"@nonmoi ERROR : Action done (augmented)",
				"@nonmoi CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_moi): os.remove(non_transmutable_moi)




	def test_non_Transmutable_multi_object_field(self):

		non_transmutable_mofi = str(self.IRMA_ROOT /"non_transmutable_mofi.loggy")
		self.make_loggy_file(non_transmutable_mofi)

		class NonTransmutable:
			def action(self):

				self.logger.debug("Action done")
				self.logger.info("Action done")
				self.logger.warning("Action done")
				self.logger.error("Action done")
				self.logger.critical("Action done")

		class Non(NonTransmutable):
			def __init__(self):
				self.logger = ContribInterceptingCase.CriticalAugmentor(
					ContribInterceptingCase.ErrorAugmentor(
						ContribInterceptingCase.WarningAugmentor(
							ContribInterceptingCase.InfoAugmentor(
								LibraryContrib)
							)
						)
					)()(handler=non_transmutable_mofi, init_name="nonmofi")

		non = Non()
		non.action()
		non.logger.close()
		loggy = []

		with open(non_transmutable_mofi) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@nonmofi INFO : Action done (augmented)",
				"@nonmofi WARNING : Action done (augmented)",
				"@nonmofi ERROR : Action done (augmented)",
				"@nonmofi CRITICAL : Action done (augmented)",
			]
		)
		if	os.path.isfile(non_transmutable_mofi): os.remove(non_transmutable_mofi)








if __name__ == "__main__" : unittest.main(verbosity=2)







