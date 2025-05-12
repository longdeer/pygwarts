from typing									import Any
from typing									import Dict
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import patronus
from pygwarts.filch.nettherin				import is_valid_ip4
from pygwarts.filch.linkindor				import EUI48_format
from pygwarts.filch.linkindor				import GP_ARP_REQ_LOG
from pygwarts.filch.marauders_map			import MaraudersMap








class ARPDiscovery(Transmutable):

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








class ARPRequestInspector(Transmutable):

	"""
		Utility object, that implements pygwarts ARP request (MAC added) processing and obtaining "state"
		according to fully covered "filchmap" mapping. Returns a dictionary with discovered hosts addresses
		and names, along with "state" integer, that describes "filchmap" inspection result:
			509  - multi mapped host request between it's ip4;
			996  - host with MAC mapped with target ip4 made request from unknown ip4;
			998  - ip4 lookup from mapped host;
			1021 - host with MAC mapped with target ip4 made request from another host mapped ip4;
			1145 - mapped host requested unknown ip4;
			1533 - mapped host requested mapped ip4;
			1536 - host with unknown MAC from unknown ip4 requested unknown ip4;
			1538 - host with unknown MAC made ip4 lookup for unknown ip4;
			1561 - host with unknown MAC requested unknown ip4 from mapped ip4;
			1632 - host with mapped MAC requested unknown ip4 from unknown ip4;
			1634 - host with mapped MAC made ip4 lookup for unknown ip4;
			1657 - host with mapped MAC requested unknown ip4 from another host mapped ip4;
			1924 - host with unknown MAC requested mapped ip4 from unknown ip4;
			1926 - host with unknown MAC made mapped ip4 lookup;
			1949 - host with unknown MAC requested mapped ip4 from mapped ip4;
			2020 - host with mapped MAC requested mapped ip4 from unknown ip4;
			2022 - host with mapped MAC made another host mapped ip4 lookup;
			2045 - host with mapped MAC requested mapped ip4 from another host mapped ip4;
			2557 - host with mapped MAC made gratuitous request;
			3581 - multi mapped host gratuitous request;
			3584 - host with unknown MAC made unknown ip4 gratuitous request;
			3680 - host with mapped MAC made unknown ip4 gratuitous request;
			3997 - host with unknown MAC made mapped ip4 gratuitous request;
			4093 - host with mapped MAC made another host mapped ip4 gratuitous request.
		If request parsing failed or valid "filchmap" is absent, returns None. 
	"""

	filchmap :MaraudersMap

	def __call__(self, request :str) -> Dict[str,int|str] | None :

		try:	dstip, srcip, srcmac = GP_ARP_REQ_LOG.search(request).group("dst", "src", "mac")
		except:	self.loggy.debug(f"Failed to inspect request: \"{request}\"")
		else:

			state  = srcip in self.filchmap.ip4
			state ^= (srcip == "0.0.0.0") <<1
			state ^= (dstip in self.filchmap.ip4) <<2
			state ^= bool(mapped_mac := self.filchmap.ip4map_mac(srcip)) <<3
			state ^= bool(mapped_name := self.filchmap.ip4map_name(srcip)) <<4
			state ^= bool(maced_ip := self.filchmap.macmap_ip4(srcmac)) <<5
			state ^= bool(maced_name := self.filchmap.macmap_name(srcmac)) <<6
			state ^= bool(mapped_dst_mac := self.filchmap.ip4map_mac(dstip)) <<7
			state ^= bool(mapped_dst_name := self.filchmap.ip4map_name(dstip)) <<8
			state ^= (srcmac != mapped_mac) <<9
			state ^= (dstip != maced_ip) <<10
			state ^= (dstip == srcip) <<11

			return {

				"state":				state,
				"source ip4":			srcip,
				"target ip4":			dstip,
				"source MAC":			srcmac,
				"source ip4 to MAC":	mapped_mac,
				"source ip4 to name":	mapped_name,
				"source MAC to ip4":	maced_ip,
				"source MAC to name":	maced_name,
				"target ip4 to MAC":	mapped_dst_mac,
				"target ip4 to name":	mapped_dst_name,
			}








class ARPResponseInspector(Transmutable):

	"""
		Utility object, that implements processing with fully covered "filchmap" of ip4 and MAC addresses,
		that are taken as a response to ARP request. Returns a dictionary with inspected hosts addresses
		and names, along with "state" integer, that describes "filchmap" inspection result:
			63  - mapped host answer;
			159 - multi mapped host answer;
			199 - host with unknown MAC responded from mapped ip4;
			216 - host with mapped MAC responded from unknown ip4;
			223 - host with mapped MAC responded from another host mapped ip4;
			224 - host with unknown MAC responded from unknown ip4.
		If response parsing failed or valid "filchmap" is absent, returns None.
	"""

	filchmap :MaraudersMap

	def __call__(self, srcip :str, srcmac :str) -> Dict[str,int|str] | None :

		try:

			state  = srcip in self.filchmap.ip4
			state ^= bool(mapped_mac := self.filchmap.ip4map_mac(srcip)) <<1
			state ^= bool(mapped_name := self.filchmap.ip4map_name(srcip)) <<2
			state ^= bool(maced_ip := self.filchmap.macmap_ip4(srcmac)) <<3
			state ^= bool(maced_name := self.filchmap.macmap_name(srcmac)) <<4
			state ^= (mapped_name == maced_name) <<5
			state ^= (srcmac != mapped_mac) <<6
			state ^= (srcip != maced_ip) <<7

		except:	self.loggy.debug(f"Failed to inspect {srcip} and {srcmac} from response")
		else:	return {

				"state":				state,
				"source ip4":			srcip,
				"source MAC":			srcmac,
				"source ip4 to MAC":	mapped_mac,
				"source ip4 to name":	mapped_name,
				"source MAC to ip4":	maced_ip,
				"source MAC to name":	maced_name,
			}







