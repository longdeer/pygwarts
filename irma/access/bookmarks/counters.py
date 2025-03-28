from pygwarts.irma.access.bookmarks			import VolumeBookmark
from pygwarts.irma.access.handlers.counters	import AccessCounter
from pygwarts.irma.access.inducers.counters	import RegisterCounterInducer
from pygwarts.irma.access.inducers.filters	import posnum








class InfoCount(VolumeBookmark):

	""" INFO level messages counter. Induces only positive register counter. """

	trigger = "INFO : "

	class Counter(AccessCounter):
		class VolumeInducer(RegisterCounterInducer): filter = posnum








class WarningCount(VolumeBookmark):

	""" WARNING level messages counter. Induces only positive register counter.	"""

	trigger = "WARNING : "

	class Counter(AccessCounter):
		class VolumeInducer(RegisterCounterInducer): filter = posnum








class ErrorCount(VolumeBookmark):

	""" WARNING level messages counter. Induces only positive register counter.	"""

	trigger = "ERROR : "

	class Counter(AccessCounter):
		class VolumeInducer(RegisterCounterInducer): filter = posnum








class CriticalCount(VolumeBookmark):

	""" WARNING level messages counter. Induces only positive register counter.	"""

	trigger = "CRITICAL : "

	class Counter(AccessCounter):
		class VolumeInducer(RegisterCounterInducer): filter = posnum







