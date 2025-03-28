from typing									import Any
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import patronus
from pygwarts.filch.nettherin				import is_valid_ip4
from pygwarts.filch.linkindor				import EUI48_format








class HostDiscovery(Transmutable):

	"""
		Link layer class for discovering network hosts, by sending ARP request and processing corresponding
		response. Must accept positional arguments:
			target		- IP4 address of target host to be discovered, as string;
			discoverer	- callable that must accept "target", along with any additional flags as **kwargs,
						and implement actual host discovery whole process.
		Once "target" validated and "discoverer" assured callable, "discoverer" will be invoked with
		"target" and all keyword arguments from current object __call__. If "discoverer" call results
		valid MAC address, which must be a discovered host physical address as response, it will be
		returned. In any other cases, including Exception raise during "discoverer" call, corresponding
		logging will occur for identification and None will be returned.
	"""

	def __call__(self, target :str, discoverer :Callable[[Any],str], **kwargs) -> str | None :


		if	is_valid_ip4(target):
			if	callable(discoverer):


				self.loggy.debug(f"Discovering {target}")
				for k,v in kwargs.items() : self.loggy.debug(f"Using {k}: {v}")


				try:

					if	isinstance(response_MAC := EUI48_format(discoverer(target, **kwargs)), str):

						self.loggy.info(f"Received response for {target} at {response_MAC}")
						return response_MAC
					else:
						self.loggy.debug(f"No response from {target}")


				except	Exception as E:

					self.loggy.debug(f"Discovery failed due to {patronus(E)}")
			else:	self.loggy.debug(f"Invalid discoverer \"{discoverer}\"")
		else:		self.loggy.debug(f"Invalid IP4 address \"{target}\"")







