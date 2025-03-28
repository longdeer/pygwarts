from typing									import Any
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import patronus








class ARPSniffer(Transmutable):

	"""
		Link layer class for listening broadcast ARP traffic. Must accept callable object "sniffer", which
		once provided with all keyword arguments "kwargs" must establish an ARP trap. Implementation of
		"sniffer" must account for all needs, such as working time or received packets handlers, which
		might be provided with "kwargs". Any Exception raised during "sniffer" working will be caught
		and logged, and this will cause "sniffer" to stop.
	"""

	def __call__(self, sniffer :Callable[[Any],Any], **kwargs):


		if	callable(sniffer):


			self.loggy.info(f"Establishing ARP trap")
			for k,v in kwargs.items() : self.loggy.debug(f"Using {k}: {v}")


			try:	sniffer(**kwargs)
			except	Exception as E : self.loggy.debug(f"ARP trap failed due to {patronus(E)}")
			else:	self.loggy.info("ARP trap ended")
		else:		self.loggy.debug(f"Invalid sniffer \"{sniffer}\"")







