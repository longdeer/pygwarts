from typing									import Any
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import patronus
from pygwarts.filch.nettherin				import is_valid_ip4








class HostPing(Transmutable):

	"""
		Network layer class for sending ICMP ping request and receiving pong response. Must accept
		positional arguments:
			target	- IP4 address of target host to be discovered, as string;
			pinger	- callable that must accept "target", along with any additional flags as **kwargs,
					and implement actual ping request constructing and sending and pong response processing.
		Once "target" validated and "pinger" assured callable, "pinger" will be invoked with "target" and
		all keyword arguments from current object __call__. If "pinger" call results anything that is not
		None, which means successful pong received, this pong will be returned. In any other cases,
		including Exception raise during "pinger" call, corresponding logging will occur for identification
		and None will be returned.
	"""

	def __call__(self, target :str, pinger :Callable[[Any],Any], **kwargs) -> Any :


		if	is_valid_ip4(target):
			if	callable(pinger):


				self.loggy.debug(f"Sending {target} ping request")
				for k,v in kwargs.items() : self.loggy.debug(f"Using {k}: {v}")


				try:

					if	(pong := pinger(target, **kwargs)) is not None:

						self.loggy.info(f"Received {target} pong response")
						return pong
					else:
						self.loggy.debug(f"No response from {target}")


				except	Exception as E:

					self.loggy.debug(f"Ping failed due to {patronus(E)}")
			else:	self.loggy.debug(f"Invalid pinger \"{pinger}\"")
		else:		self.loggy.debug(f"Invalid IP4 address \"{target}\"")







