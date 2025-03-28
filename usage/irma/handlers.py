from re										import Pattern
from typing									import Dict
from typing									import Literal
from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.magical.time_turner.utils		import DATETIME_1_P
from pygwarts.magical.spells				import patronus
from pygwarts.irma.access.volume			import LibraryVolume
from pygwarts.irma.access.handlers.parsers	import GroupParser
from pygwarts.filch.marauders_map			import MaraudersMap








class FilchAccessHandler(GroupParser):

	"""
		filch instruments
	"""

	filchmap :MaraudersMap

	def get_filchmap(self, attr :str, *args, **kwargs) -> Dict[str,Dict[str,str] | str] | str | None :

		""" filch MaraudersMap safe accessing method """

		match attr:

			case "ip4":

				try:	return	self.filchmap.ip4 or dict()
				except:	return	dict()

			case "ip4map":

				try:	return	self.filchmap.ip4map(args[0])
				except:	return	args[0]

			case "macmap":

				try:	return	self.filchmap.macmap(args[0])
				except:	return	args[0]

			case "ip4map_name":

				try:	return	self.filchmap.ip4map_name(args[0])
				except:	return	args[0]

			case _:		raise	AttributeError(f"Invalid attribute \"{attr}\" for map")








class DiscoverywatchAccessHandler(FilchAccessHandler):

	"""
		filch hosts discovery AccessHandler. Converts parsed "loggy" to a mapping for:
			known_hosts		- successful discover of correctly mapped in MaraudersMap records;
			unknown_ip		- discover of unmapped in MaraudersMap records ip4 responses;
			unknown_mac		- discover of unmapped in MaraudersMap records mac responses;
			mismatched_ip	- discover of responses with mismatched in MaraudersMap records ip4;
			mismatched_mac	- discover of responses with mismatched in MaraudersMap records mac.
	"""

	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

		if	isinstance(getattr(self, "rpattern", None), Pattern):
			if	(match := self.rpattern.search(line)) and (target := match.group("ip", "mac")):
				if	(len(target) == 2) and self.registered(volume):


					ip,mac = target
					self.loggy.debug(f"Considering {ip} at {mac} discover")


					if	ip in self.get_filchmap("ip4"):
						self.loggy.debug("Discovered ip mapped by filch")


						mapping		= self.get_filchmap("ip4map", ip)
						mapped_mac	= mapping["MAC"]
						host_name	= mapping["NAME"]
						desc		= mapping["DESC"]


						if	mac == mapped_mac:
							self.loggy.debug("Discovered mac mapped by filch")


							volume[self].setdefault("known_hosts",list()).append(

								dict(

									discovered_ip=ip,
									filch_mapped_mac=mapped_mac,
									filch_mapped_host_name=host_name,
									filch_mapped_description=desc,
									discovered_mac=mac,
									filch_maced_ip=None,
									filch_maced_host_name=None,
									filch_maced_description=None,
								)
							)


						elif(record := self.get_filchmap("macmap", mac)) is not None :
							self.loggy.debug("Discovered mac mapped by another host")


							maced_ip		= record["IP4"]
							maced_host_name	= record["NAME"]
							maced_desc		= record["DESC"]


							volume[self].setdefault("mismatched_mac",list()).append(

								dict(

									discovered_ip=ip,
									filch_mapped_mac=mapped_mac,
									filch_mapped_host_name=host_name,
									filch_mapped_description=desc,
									discovered_mac=mac,
									filch_maced_ip=maced_ip,
									filch_maced_host_name=maced_host_name,
									filch_maced_description=maced_desc,
								)
							)


						else:


							self.loggy.debug("Discovered unknown mac mapped by known ip")
							volume[self].setdefault("unknown_mac",list()).append(

								dict(

									discovered_ip=ip,
									filch_mapped_mac=mapped_mac,
									filch_mapped_host_name=host_name,
									filch_mapped_description=desc,
									discovered_mac=mac,
									filch_maced_ip=None,
									filch_maced_host_name=None,
									filch_maced_description=None,
								)
							)




					# Unknowns handle, None check for sure, cause if it somehow None, due to "parse"
					# implementation, it is not enough just mapper presence check.
					elif ip is not None and ip not in self.get_filchmap("ip4"):
						if	(record := self.get_filchmap("macmap", mac)) is not None :
							self.loggy.debug("Discovered mapped mac with unknown ip")


							# Trying to find parsed MAC to be in mapper, cause it's might be
							# a mismatch or spoofing.
							maced_ip		= record["IP4"]
							maced_host_name	= record["NAME"]
							maced_desc		= record["DESC"]


							volume[self].setdefault("mismatched_ip",list()).append(

								dict(

									discovered_ip=ip,
									filch_mapped_mac=None,
									filch_mapped_host_name=None,
									filch_mapped_description=None,
									discovered_mac=mac,
									filch_maced_ip=maced_ip,
									filch_maced_host_name=maced_host_name,
									filch_maced_description=maced_desc,
								)
							)


						else:


							self.loggy.debug("Discovered unkonwn host")
							volume[self].setdefault("unknown_ip",list()).append(

								dict(

									discovered_ip=ip,
									filch_mapped_mac=None,
									filch_mapped_host_name=None,
									filch_mapped_description=None,
									discovered_mac=mac,
									filch_maced_ip=None,
									filch_maced_host_name=None,
									filch_maced_description=None,
								)
							)




					return	True


				self.loggy.warning(f"Handler {self} invalid parse result for line \"{line}\"")








class BroadwatchAccessHandler(FilchAccessHandler):

	"""
		filch ARP sniffing AccessHandler. Converts parsed "loggy" to a mapping for:
			mapped_requests		- requests that are correctly mapped in MaraudersMap records;
			unmapped_requests	- requests with no mapping in MaraudersMap records;
			mismatched_ip		- requests with mismatched in MaraudersMap records ip4;
			mismatched_mac		- requests with mismatched in MaraudersMap records mac;
			ip_lookup			- 0.0.0.0 look up if ip4 is free.
	"""

	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

		if	isinstance(getattr(self, "rpattern", None), Pattern):
			if	(match := self.rpattern.search(line)) and (target := match.group("dst", "src", "mac")):
				if	(len(target) == 3) and self.registered(volume):


					dst,src,mac = target
					self.loggy.debug(f"Considering {dst} request from {src} at {mac}")


					try:	DT = TimeTurner(*DATETIME_1_P.search(line).group("date", "time"))
					except	Exception as E:

						self.loggy.warning(f"Failed to obtain datetime due to {patronus(E)}")
						return




					if	src in self.get_filchmap("ip4"):

						mapping = self.get_filchmap("ip4map", src)
						mapped_mac = mapping["MAC"]
						mapped_name = mapping["NAME"]

						if	dst in self.get_filchmap("ip4"):
							DST = self.get_filchmap("ip4map_name", dst)


							# The following relies on loggy file to be formatted the way it is
							# defaulted for LibraryContrib class, so any changes in format
							# must be maintained for datetime obtaining in this section.
							if	mac != mapped_mac:

								self.loggy.debug(f"Spoofguard triggered")
								# source {mapped_name} mac mismatching @ DT
								volume[self].setdefault("mismatched_mac",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=mapped_name,
										source_mapped_mac=mapped_mac,
										source_maced_ip=None,
										source_maced_name=None,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=DST,
										timestamp=DT,
									)
								)


							else:
								self.loggy.debug("Mapped request")
								volume[self].setdefault("mapped_requests",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=mapped_name,
										source_mapped_mac=mapped_mac,
										source_maced_ip=None,
										source_maced_name=None,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=DST,
										timestamp=DT,
									)
								)


						else:
							self.loggy.debug("Unmapped destination request")
							volume[self].setdefault("unmapped_requests",list()).append(

								dict(

									request_source_ip=src,
									request_source_mac=mac,
									source_mapped_name=mapped_name,
									source_mapped_mac=mapped_mac,
									source_maced_ip=None,
									source_maced_name=None,
									request_target_ip=dst,
									target_mapped_ip=None,
									target_mapped_name=None,
									timestamp=DT,
								)
							)




					elif	src == "0.0.0.0":
						if	(record := self.get_filchmap("macmap", mac)) is not None :

							maced_ip = record["IP4"]
							maced_host_name = record["NAME"]

							if	maced_ip == dst:

								self.loggy.debug("Mapped ip lookup")
								volume[self].setdefault("ip_lookup",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=None,
										source_mapped_mac=None,
										source_maced_ip=maced_ip,
										source_maced_name=maced_host_name,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=None,
										timestamp=DT,
									)
								)


							elif	dst in self.get_filchmap("ip4"):

								self.loggy.debug("Mapped mac mismatched mapped ip lookup")
								dst_name = self.get_filchmap("ip4map_name", dst)
								volume[self].setdefault("ip_lookup",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=None,
										source_mapped_mac=None,
										source_maced_ip=None,
										source_maced_name=maced_host_name,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=dst_name,
										timestamp=DT,
									)
								)


							else:
								self.loggy.debug("Mapped mac mismatched unmapped ip lookup")
								volume[self].setdefault("ip_lookup",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=None,
										source_mapped_mac=None,
										source_maced_ip=None,
										source_maced_name=maced_host_name,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=None,
										timestamp=DT,
									)
								)


						elif	dst in self.get_filchmap("ip4"):

							record = self.get_filchmap("ip4map", dst)
							dst_mac = record["MAC"]
							dst_name = record["NAME"]
							self.loggy.debug("Mapped target lookup from unmapped address")
							volume[self].setdefault("ip_lookup",list()).append(

								dict(

									request_source_ip=src,
									request_source_mac=mac,
									source_mapped_name=None,
									source_mapped_mac=None,
									source_maced_ip=None,
									source_maced_name=None,
									request_target_ip=dst,
									target_mapped_ip=dst,
									target_mapped_name=dst_name,
									timestamp=DT,
								)
							)


						else:
							self.loggy.debug("Unmapped target lookup from unmapped address")
							volume[self].setdefault("ip_lookup",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=None,
										source_mapped_mac=None,
										source_maced_ip=None,
										source_maced_name=None,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=None,
										timestamp=DT,
									)
								)




					elif	src is not None:
						if	(record := self.get_filchmap("macmap", mac)) is not None :

							maced_ip = record["IP4"]
							maced_host_name = record["NAME"]

							if	dst in self.get_filchmap("ip4"):

								DST = self.get_filchmap("ip4map_name", dst)
								self.loggy.debug("Mapped target request from mismatched ip")
								volume[self].setdefault("mismatched_ip",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=None,
										source_mapped_mac=None,
										source_maced_ip=None,
										source_maced_name=maced_host_name,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=DST,
										timestamp=DT,
									)
								)

							else:
								self.loggy.debug("Unknown target request from mismatched ip")
								# unknown {dst} request from mismatched {maced_name} ip @ DT
								volume[self].setdefault("mismatched_ip",list()).append(

									dict(

										request_source_ip=src,
										request_source_mac=mac,
										source_mapped_name=None,
										source_mapped_mac=None,
										source_maced_ip=None,
										source_maced_name=maced_host_name,
										request_target_ip=dst,
										target_mapped_ip=None,
										target_mapped_name=None,
										timestamp=DT,
									)
								)


						elif	dst in self.get_filchmap("ip4"):

							DST = self.get_filchmap("ip4map_name", dst)
							self.loggy.debug("Mapped target request from unmapped source")
							volume[self].setdefault("unmapped_requests",list()).append(

								dict(

									request_source_ip=src,
									request_source_mac=mac,
									source_mapped_name=None,
									source_mapped_mac=None,
									source_maced_ip=None,
									source_maced_name=None,
									request_target_ip=dst,
									target_mapped_ip=None,
									target_mapped_name=DST,
									timestamp=DT,
								)
							)


						else:
							self.loggy.debug("Unmapped target request from unmapped source")
							volume[self].setdefault("unmapped_requests",list()).append(

								dict(

									request_source_ip=src,
									request_source_mac=mac,
									source_mapped_name=None,
									source_mapped_mac=None,
									source_maced_ip=None,
									source_maced_name=None,
									request_target_ip=dst,
									target_mapped_ip=None,
									target_mapped_name=None,
									timestamp=DT,
								)
							)


					return True


				self.loggy.warning(f"Handler {self} invalid parse result for line \"{line}\"")







