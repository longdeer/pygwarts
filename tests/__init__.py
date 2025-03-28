import	os
import	unittest
from	pathlib					import Path
from	pygwarts.irma.contrib	import LibraryContrib








class PygwartsTestCase(unittest.TestCase):

	"""
		Super class with instruments.
	"""


	maxDiff		= None
	clean_up	= False
	__CWD		= Path.home().joinpath("pygwarts-test-folder")


	LOGGY_LEVELS_MAPPER	= {

		20: "INFO",
		30: "WARNING",
		40: "ERROR",
		50: "CRITICAL",
	}


	def tearDown(self):

		"""
			Common "tearDown" that assumes that any child will operate over variable "test_case" that has
			a Logger object to be closed explicitly.
		"""

		if	hasattr(self, "test_case"):
			if	hasattr(self.test_case, "loggy"):
				if	isinstance(self.test_case.loggy, LibraryContrib):
					self.test_case.loggy.close()




	def make_loggy_file(self, path :str):

		"""
			As LibraryContrib creates handler files anyway, current method serves as a cleaner,
			cause all tests takes place in DEBUG mode and hence files becomes flooded.
		"""

		loggy_folder = os.path.dirname(path)

		if		not os.path.isdir(loggy_folder):	os.makedirs(loggy_folder)
		with	open(path, "w") as loggy_F :		pass




	def fmake(self, path :str ="", content :str ="alohomora"):

		"""
			For creation of required files.
			Also may serves as a touch.
			Argument "path" must be end file absolute path.
		"""

		folder	= os.path.dirname(path)

		if		not os.path.isdir(folder):	os.makedirs(folder)
		with	open(path, "w") as F:		F.write(content)




	def no_loggy_levels(self, loggy :LibraryContrib, *levels):

		"""
			Asserts the LibraryContrib object "loggy" has not emitted "levels" levels messages.
		"""

		self.assertTrue(isinstance(loggy, list))
		self.assertTrue(levels)


		_levels = list(
			filter(

				bool,
				[
					L if
					L in self.LOGGY_LEVELS_MAPPER.values() else
					self.LOGGY_LEVELS_MAPPER.get(L)
					for L in levels
				]
			)
		)


		self.assertTrue(len(_levels) == len(levels))
		self.assertTrue(set(_levels) <= set(self.LOGGY_LEVELS_MAPPER.values()))


		for record in loggy:
			for level in _levels:

				with self.subTest(loggy=record, level=level):
					self.assertFalse(record.startswith(level))







