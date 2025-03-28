import	os
from	pathlib								import Path
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.tests						import PygwartsTestCase








class IrmaTestCase(PygwartsTestCase):

	"""
		Irma testing super class
	"""

	IRMA_ROOT			= Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma"

	ACCESS_LIBRARY		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_l.loggy")
	ACCESS_BOOKMARK		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_b.loggy")
	ACCESS_VOLUME		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_v.loggy")
	ACCESS_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_h.loggy")
	ACCESS_INDUCER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_i.loggy")
	ACCESS_ANNEX		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_a.loggy")
	ACCESS_UTILS		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"access_u.loggy")
	CONTRIB_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"contrib.loggy")
	INTERCEPT_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"intercept.loggy")
	ITEMS_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"items.loggy")
	CASING_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"casing.loggy")
	GRABBING_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"grabbing.loggy")
	GRABBING_LOCKER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"locker.Shelf")
	GRABBING_IN_INIT	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"init_grab.loggy")
	GRABBING_NO_LOCKER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"no_locker.Shelf")
	PRODUCING_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"produce.loggy")
	PRODUCING_PRODUCABLE= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"irma" /"produce.Shelf")

	class Levels(Transmutable):
		class debugs(Transmutable):
			def __call__(self):

				self.loggy.debug("Must be logged")
				self.loggy.info("Must be logged")
				self.loggy.warning("Must be logged")
				self.loggy.error("Must be logged")
				self.loggy.critical("Must be logged")

		class infos(Transmutable):
			def __call__(self):

				self.loggy.debug("Must be logged")
				self.loggy.info("Must be logged")
				self.loggy.warning("Must be logged")
				self.loggy.error("Must be logged")
				self.loggy.critical("Must be logged")

		class warnings(Transmutable):
			def __call__(self):

				self.loggy.debug("Must be logged")
				self.loggy.info("Must be logged")
				self.loggy.warning("Must be logged")
				self.loggy.error("Must be logged")
				self.loggy.critical("Must be logged")

		class errors(Transmutable):
			def __call__(self):

				self.loggy.debug("Must be logged")
				self.loggy.info("Must be logged")
				self.loggy.warning("Must be logged")
				self.loggy.error("Must be logged")
				self.loggy.critical("Must be logged")

		class criticals(Transmutable):
			def __call__(self):

				self.loggy.debug("Must be logged")
				self.loggy.info("Must be logged")
				self.loggy.warning("Must be logged")
				self.loggy.error("Must be logged")
				self.loggy.critical("Must be logged")







