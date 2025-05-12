from re										import Pattern
from typing									import Literal
from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.magical.time_turner.utils		import DATETIME_1_P
from pygwarts.magical.spells				import patronus
from pygwarts.irma.access.volume			import LibraryVolume
from pygwarts.irma.access.handlers.parsers	import GroupParser
from pygwarts.filch.marauders_map			import MaraudersMap
from pygwarts.filch.linkindor.arp			import ARPResponseInspector
from pygwarts.filch.linkindor.arp			import ARPRequestInspector








class DiscoverywatchAccessHandler(GroupParser):

	"""
		filch hosts discovery AccessHandler. Converts parsed "loggy" to a mapping for:
			known_hosts		- successful discover of correctly mapped in MaraudersMap records;
			unknown_ip		- discover of unmapped in MaraudersMap records ip4 responses;
			unknown_mac		- discover of unmapped in MaraudersMap records MAC responses;
			mismatched_ip	- discover of responses with mismatched in MaraudersMap records ip4;
			mismatched_mac	- discover of responses with mismatched in MaraudersMap records MAC.
	"""


	Inspector	:ARPResponseInspector
	filchmap	:MaraudersMap


	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :
		if	isinstance(getattr(self, "rpattern", None), Pattern):
			if	(match := self.rpattern.search(line)) and (target := match.group("ip", "mac")):
				if	(len(target) == 2) and self.registered(volume):


					ip,mac = target
					self.loggy.debug(f"Considering {mac} discover at {ip}")


					if	(result := self.Inspector(ip, mac)) is not None:
						match result["state"]:

							case 159 | 63: volume[self].setdefault("known_hosts",list()).append(
								{
									**result,
									"description": self.filchmap.ip4map_desc(result["source ip4"])
								}
							)
							case 223: volume[self].setdefault("mismatched_mac",list()).append(dict(result))
							case 199: volume[self].setdefault("unknown_mac",list()).append(dict(result))
							case 216: volume[self].setdefault("mismatched_ip",list()).append(dict(result))
							case 224: volume[self].setdefault("unknown_ip",list()).append(dict(result))
							case rst: self.loggy.warning(f"{self} discovered unknown state {rst}")


						return True


			else:	self.loggy.debug(f"Invalid parse result for line \"{line}\"")
		else:		self.loggy.debug(f"Pattern to match not found")








class BroadwatchAccessHandler(GroupParser):

	"""
		filch ARP sniffing AccessHandler. Converts parsed "loggy" to a mapping for:
			mapped		- requests that are correctly mapped in MaraudersMap records;
			unknown		- requests with partial or no mapping in MaraudersMap records;
			ip4_lookup	- 0.0.0.0 look up if ip4 is free.
			mismatches	- requests with mismatching in MaraudersMap records;
	"""


	Inspector	:ARPRequestInspector
	filchmap	:MaraudersMap


	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :
		if	self.registered(volume) and (result := self.Inspector(line)) is not None:


			try:	DT = TimeTurner(*DATETIME_1_P.search(line).group("date", "time"))
			except	Exception as E:

				self.loggy.warning(f"Failed to obtain datetime due to {patronus(E)}")
				return


			match result["state"]:

				case 3581 | 2557 | 1533 | 509:

					volume[self].setdefault("mapped",list()).append(dict(**result, timestamp=DT))

				case 3584 | 1924 | 1536 | 1145:

					volume[self].setdefault("unknown",list()).append(dict(**result, timestamp=DT))

				case 2022 | 1926 | 1634 | 1538 | 998:

					volume[self].setdefault("ip4_lookup",list()).append(dict(**result, timestamp=DT))

				case 4093 | 3997 | 3680 | 2045 | 2020 | 1949 | 1657 | 1632 | 1561 | 1021 | 996:

					volume[self].setdefault("mismatches",list()).append(dict(**result, timestamp=DT))

				case rst: self.loggy.warning(f"{self} discovered unknown state {rst}")


			return True







