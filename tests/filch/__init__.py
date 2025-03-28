from pathlib		import Path
from pygwarts.tests	import PygwartsTestCase








class FilchTestCase(PygwartsTestCase):

	"""
		Super for filch testing
	"""

	FILCH_ROOT			= Path(PygwartsTestCase._PygwartsTestCase__CWD) /"filch"
	APPPUF_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"filch" /"apppuf.loggy")
	TRNSPRTCLAW_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"filch" /"trnsprtclaw.loggy")
	NETTHERIN_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"filch" /"nettherin.loggy")
	LINKINDOR_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"filch" /"linkindor.loggy")
	MARAUDERS_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"filch" /"maramap.loggy")

	valid_MAC_chars	= "0123456789AaBbCcDdEeFf"
	valid_IP_chars	= list(range(256))







