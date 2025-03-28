from collections							import defaultdict
from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.magical.time_turner.utils 	import hundscale
from pygwarts.irma.access.volume			import LibraryVolume
from pygwarts.irma.access.bookmarks			import VolumeBookmark
from pygwarts.irma.access.handlers			import AccessHandlerRegisterCounter
from pygwarts.irma.access.handlers.counters	import AccessCounter
from pygwarts.irma.access.handlers.parsers	import TargetNumberAccumulator
from pygwarts.irma.access.handlers.parsers	import TargetStringAccumulator
from pygwarts.irma.access.handlers.parsers	import TargetHandler
from pygwarts.irma.access.inducers			import AccessInducer
from pygwarts.irma.access.inducers.counters	import RegisterCounterInducer
from pygwarts.irma.access.inducers.recap	import RegisterRecapInducer
from pygwarts.irma.access.inducers.filters	import plurnum
from pygwarts.irma.access.inducers.filters	import posnum
from pygwarts.irma.access.inducers.case		import InducerCase
from pygwarts.irma.access.utils				import TextWrapper
from pygwarts.irma.shelve.casing			import is_num
from pygwarts.irma.shelve.casing			import num_diff
from pygwarts.filch.nettherin				import VALID_IP4
from pygwarts.filch.linkindor				import VALID_MAC
from pygwarts.filch.marauders_map			import MaraudersMap
from casing									import mostsec_diff
from casing									import byte_size_diff
from handlers								import DiscoverywatchAccessHandler
from handlers								import BroadwatchAccessHandler
from inducers								import DiffCaseRegisterRecapAccumulatorInducer
from inducers								import FilchWatchInducer








class CallstampActivity(VolumeBookmark):

	"""
		Bookmark that works with "Callstamp" object information about execution time.
		Collects every line from "Callstamp" activity and induces maximum three counts:
			1. total count activity lines (always induced);
			2. total activity duration sum (always induced);
			3. average activity duration (induced with 1 <activity).
	"""

	trigger	= "finished in"													# Callstamp loggy line that will trigger bookmark
	rpattern= r"finished in (?P<target>\d+)( seconds)?$"					# Pattern to extract execution time

	class Activities(AccessCounter):

		@TextWrapper("activities: ","\n")									# Inducer output text decoration (optional)
		@InducerCase("your shelf name", prep=is_num, post=num_diff)			# Inducer output casing (optional)
		class Inducer(RegisterCounterInducer): filter = plurnum

	@AccessHandlerRegisterCounter
	class Duration(TargetNumberAccumulator):

		@TextWrapper("total time: ","\n")									# Inducer output text decoration (optional)
		@InducerCase("your shelf name", prep=is_num, post=mostsec_diff)		# Inducer output casing (optional)
		class Total(RegisterRecapInducer): filter = posnum

		@TextWrapper("average time: ","\n")									# Inducer output text decoration (optional)
		@InducerCase("your shelf name", prep=is_num, post=mostsec_diff)		# Inducer output casing (optional)
		class Average(AccessInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(recap := self.get_register_recap(volume), int | float):
					if	(counter := self.get_register_counter(volume)):
						if	1 <counter:

							return str(recap /counter)








class ShelfBookmark(VolumeBookmark):

	""" irma.shelve typical bookmark for catching shelf producing or shelfs differences """

	trigger	= "operation"											# LibraryShelf loggy line that will trigger bookmark

	class Counter(AccessCounter):

		@TextWrapper("operations: ","\n")							# Inducer output text decoration (optional)
		@InducerCase("your shelf name", prep=is_num, post=num_diff)	# Inducer output casing (optional)
		class Inducer(RegisterCounterInducer): filter = posnum








class HagridPlanting(VolumeBookmark):

	"""
		hagrid typical bookmark for catching number of files/folders copied/moved/cloned/pushed/trimmed.
		"trigger" and "rpattern" might be as follows:
			operation:	Grown leaf
						Moved leaf
						Cloned leaf
						Pushed leaf
						Trimmed leaf
						Thrived twig
						Trimmed twig
	"""

	trigger	= "operation"												# Hagrid operation loggy line that will trigger bookmark
	rpattern=  r".+ operation \".+[/\\](?P<target>[^/\\]+)\"$"			# Pattern to extract operand name

	@AccessHandlerRegisterCounter
	class Accumulator(TargetStringAccumulator):

		@TextWrapper("operations done ",": ")							# Inducer output text decoration (optional)
		@InducerCase("your shelf name", prep=is_num, post=num_diff)		# Inducer output casing (optional)
		class CountInducer(RegisterCounterInducer): filter = posnum
		@TextWrapper(footer="\n")										# Inducer output text decoration (optional)
		class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):		pass








class HagridRegistering(VolumeBookmark):

	""" hagrid typical bookmark for catching a folder size/number of folders/files """

	trigger	= "stat"														# User defined loggy line that will trigger bookmark
	rpattern= r".+ stat: (?P<target>\d+)$"									# Pattern to extract stat information

	class Handler(TargetHandler):

		@TextWrapper("stat count: ","\n")									# Inducer output text decoration (optional)
		@InducerCase("your shelf name", prep=is_num, post=byte_size_diff)	# Inducer output casing (optional)
		class Inducer(RegisterRecapInducer): pass








class DiscoveryWatch(VolumeBookmark):

	""" filch hosts discovery typical bookmark, that encompasses handling and full induce """

	trigger		= "Received response for"							# HostDiscovery loggy line that will trigger bookmark
	rpattern	= rf"(?P<ip>{VALID_IP4}) at (?P<mac>{VALID_MAC})"	# Pattern to extract response ip4 and mac

	class DiscoveredHosts(DiscoverywatchAccessHandler):

		@TextWrapper("\nhosts mapped: ")
		@InducerCase("library_shelf", prep=is_num, post=num_diff)
		class MappedHosts(AccessInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(getattr(self, "filchmap", MaraudersMap)):
					if	(hosts := len(self.filchmap.ip4)):

						return str(hosts)


		@TextWrapper("\nhosts discovered: ")
		@InducerCase("library_shelf", prep=is_num, post=num_diff)
		class DiscoveredHostsInducer(RegisterCounterInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :
				if	isinstance(recap := volume[self._UPPER_LAYER], dict):

					return (

						len(recap.get("mismatched_mac",[]))
						+
						len(recap.get("mismatched_ip",[]))
						+
						len(recap.get("unknown_mac",[]))
						+
						len(recap.get("unknown_ip",[]))
						+
						len(recap.get("known_hosts",[]))
					)


		@TextWrapper("\n\nmismatched hosts: ")
		class MismatchedHostsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :
				if	isinstance(recap := volume[self._UPPER_LAYER], dict):

					misses = list()

					if	(miss_mac := recap.get("mismatched_mac")):	misses.extend(miss_mac)
					if	(miss_ip := recap.get("mismatched_ip")):	misses.extend(miss_ip)
					if	(amount := len(misses)):
						missed = [

							"%s response from %s mac"%(

								record.get("filch_mapped_host_name"),
								record.get("filch_maced_host_name")

							)	if record.get("filch_mapped_mac") is not None else

							"%s mac response from unknown %s"%(

								record.get("filch_maced_host_name"),
								record.get("discovered_ip")

							)	for record in misses
						]
						return	"%s\n\t%s"%(

							self.filch_caseamount(amount, volume),
							"\n\t".join(self.filch_caserecords(missed, volume))
						)


		@TextWrapper("\n\nunknown hosts: ")
		class UnknownHostsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :
				if	isinstance(recap := volume[self._UPPER_LAYER], dict):

					unknowns = list()

					if	(no_mac := recap.get("unknown_mac")):	unknowns.extend(no_mac)
					if	(no_ip := recap.get("unknown_ip")):		unknowns.extend(no_ip)
					if	(amount := len(unknowns)):
						unknown = [

							"%s response from unknown %s"%(

								record.get("filch_mapped_host_name")
								if record.get("filch_mapped_mac") is not None else
								record.get("discovered_ip"),
								record.get("discovered_mac")

							)	for record in unknowns
						]
						return	"%s\n\t%s"%(

							self.filch_caseamount(amount, volume),
							"\n\t".join(self.filch_caserecords(unknown, volume))
						)


		@TextWrapper("\n\nmapped up: ")
		class KnownHostsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(recap := volume[self._UPPER_LAYER], dict):
					if	(hosts := recap.get("known_hosts")) is not None:

						if	(amount := len(hosts)):
							up = [

								"%s (%s)"%(

									record.get("filch_mapped_host_name"),
									record.get("filch_mapped_description")

								)	for record in hosts
							]
							return	"%s\n\t%s"%(

								self.filch_caseamount(amount, volume),
								"\n\t".join(self.filch_caserecords(up, volume))
							)


		@TextWrapper("\n\nmapped down: ")
		class DownHostsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(recap := volume[self._UPPER_LAYER], dict):
					if	(hosts := recap.get("known_hosts")) is not None:

						up = { record.get("discovered_ip") for record in hosts }
						down = [ ip4 for ip4 in self.filchmap["IP4"] if ip4 not in up ]

						if	(amount := len(down)):
							downs = [

								"%s (%s)"%(

									self.filchmap["IP4"][record].get("NAME"),
									self.filchmap["IP4"][record].get("DESC")

								)	for record in down
							]
							return	"%s\n\t%s"%(

								self.filch_caseamount(amount, volume),
								"\n\t".join(self.filch_caserecords(downs, volume))
							)








class BroadWatch(VolumeBookmark):

	""" filch ARP sniffing typical bookmark, that encompasses handling and full induce """

	trigger		= "who has"
	rpattern	= rf"(?P<dst>{VALID_IP4}) says (?P<src>{VALID_IP4}) \((?P<mac>{VALID_MAC})\)$"

	@AccessHandlerRegisterCounter
	class TrappedRequests(BroadwatchAccessHandler):

		@TextWrapper("\nrequests trapped: ")
		@InducerCase("library_shelf", prep=is_num, post=num_diff)
		class TotalTrappedInducer(RegisterCounterInducer):		pass

		@TextWrapper("\ngraphs plotted: ")
		class Plotter(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :
				if	isinstance(recap := volume[self._UPPER_LAYER], dict):

					totals = defaultdict(int)
					requests = defaultdict(lambda : defaultdict(int))

					for record in recap.get("mapped_requests",list()):
						if	isinstance(stamp := record.get("timestamp"), TimeTurner):

							point = int(hundscale(stamp.HM_asjoin))
							totals[point] += 1
							requests[

								record.get("source_mapped_name",record.get("request_source_ip"))
							][	point
							]	+= 1

					for record in recap.get("unmapped_requests",list()):
						if	isinstance(stamp := record.get("timestamp"), TimeTurner):

							point = int(hundscale(stamp.HM_asjoin))
							totals[point] += 1
							requests[

								record.get(
									"source_mapped_name",
									record.get(
										"source_maced_name",
										record.get("request_source_ip")
									)
								)
							][	point
							]	+= 1

					for record in recap.get("mismatched_mac",list()):
						if	isinstance(stamp := record.get("timestamp"), TimeTurner):

							point = int(hundscale(stamp.HM_asjoin))
							totals[point] += 1
							requests[

								record.get("source_mapped_name",record.get("request_source_ip"))
							][	point
							]	+= 1

					for record in recap.get("mismatched_ip",list()):
						if	isinstance(stamp := record.get("timestamp"), TimeTurner):

							point = int(hundscale(stamp.HM_asjoin))
							totals[point] += 1
							requests[

								record.get("source_mapped_name",record.get("request_source_ip"))
							][	point
							]	+= 1

					for record in recap.get("ip_lookup",list()):
						if	isinstance(stamp := record.get("timestamp"), TimeTurner):

							point = int(hundscale(stamp.HM_asjoin))
							totals[point] += 1
							requests[record.get("request_source_ip")][point] += 1

					if	(amount := len(requests)):

						# In case attributes not provided Exception
						# raise will stop whole procedure for sure
						ndate = self.plotdate.dmY_aspath
						pdate = self.plotdate.dmY_asjoin
						fsdir = self.plotdir
						count = 0

						self.broad_plot(

							axises=totals.items(),
							title=f"total by {ndate}",
							pngpath=fsdir,
							pngname=f"total-{pdate}.png",
						)

						for src, mapping in requests.items():

							count += bool(

								self.broad_plot(

									axises=mapping.items(),
									title=f"{src} by {ndate}",
									pngpath=fsdir,
									pngname=f"{src}-{pdate}.png",
								)
							)

						casecount = self.filch_casing(

							count,
							volume,
							getattr(self, getattr(self, "case_link", ""), None),
							"count",
							is_num,
							num_diff
						)
						return f"{casecount}/{amount}" if count != amount else casecount


		@TextWrapper("\n\nmismatches: ")
		class MismatchedRequestsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :
				if	isinstance(recap := volume[self._UPPER_LAYER], dict):

					events	= list()
					stamps	= list()
					records	= list()
					uniques	= set()

					if	(miss_mac := recap.get("mismatched_mac")) is not None:
						records.extend(miss_mac)
					if	(miss_ip := recap.get("mismatched_ip")) is not None:
						records.extend(miss_ip)

					for record in records:

						stamp = record.get("timestamp").format("%H%M %d/%m/%Y")
						event = (
							"request with %s mac mismatching"%(
								record.get("source_mapped_name"),
							)

							if record.get("source_mapped_name") is not None else

							"request with %s ip4 mismatching"%(
								record.get("source_maced_name"),
							)

							if record.get("target_mapped_name") is not None else

							"unknown %s request with %s ip4 mismatching"%(

								record.get("request_target_ip"),
								record.get("source_maced_name"),
							)
						)

						if	(current := f"{event} at {stamp}") not in uniques:

							uniques.add(current)
							events.append(event)
							stamps.append(stamp)

					if	(amount := len(uniques)):
						return "%s\n\t%s"%(

							self.filch_caseamount(amount, volume),
							"\n\t".join(

								f"{event} at {stamp}"
								for event,stamp
								in zip(self.filch_caseamount(events, volume), stamps)
							)
						)

		@TextWrapper("\n\nip4 lookups: ")
		class LookupRequestsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(recap := volume[self._UPPER_LAYER], dict):
					if	isinstance(records := recap.get("ip_lookup"), list):

						events	= list()
						stamps	= list()
						uniques	= set()

						for record in records:

							stamp = record.get("timestamp").format("%H%M %d/%m/%Y")
							event = (

								"%s ip4 lookup"%record.get("source_maced_name")


								if	(record.get("source_maced_ip") is not None)
								and
									(record.get("source_maced_name") is not None)
								else


								"%s lookup from %s"%(

									record.get("target_mapped_name"),
									record.get("source_maced_name")
								)


								if	(record.get("source_maced_name") is not None)
								and
									(record.get("target_mapped_name") is not None)
								else


								"unknown %s lookup from %s"%(

									record.get("request_target_ip"),
									record.get("source_maced_name"),
								)


								if	(record.get("source_maced_name") is not None)
								and
									(record.get("request_target_ip") is not None)
								else


								"%s ip4 lookup from unknown %s"%(

									record.get("target_mapped_name"),
									record.get("request_source_mac"),
								)


								if	(record.get("target_mapped_ip") is not None)
								and
									(record.get("target_mapped_name") is not None)
								else


								"unknown %s lookup from unknown %s"%(

									record.get("request_target_ip"),
									record.get("request_source_mac"),
								)
							)

							if	(current := f"{event} at {stamp}") not in uniques:

								uniques.add(current)
								events.append(event)
								stamps.append(stamp)

						if	(amount := len(uniques)):
							return "%s\n\t%s"%(

								self.filch_caseamount(amount, volume),
								"\n\t".join(

									f"{event} at {stamp}"
									for event,stamp
									in zip(self.filch_caseamount(events, volume), stamps)
								)
							)


		@TextWrapper("\n\nunknown requests: ")
		class UnmappedRequestsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(recap := volume[self._UPPER_LAYER], dict):
					if	isinstance(records := recap.get("unmapped_requests"), list):

						requests = defaultdict(lambda : defaultdict(int))

						for record in records:
							if	isinstance(record, dict):

								requests[

									record.get("source_mapped_name")
									or
									record.get("request_source_ip")
								][	record.get("target_mapped_name")
									or
									record.get("request_target_ip")
								]	+= 1

						return	self.broad_gather(

							requests,
							volume,
							getattr(self, getattr(self, "case_link", ""), None)
						)


		@TextWrapper("\n\nmapped requests: ")
		class MappedRequestsInducer(FilchWatchInducer):

			def __call__(self, volume :LibraryVolume) -> str | None :

				if	isinstance(recap := volume[self._UPPER_LAYER], dict):
					if	isinstance(records := recap.get("mapped_requests"), list):

						requests = defaultdict(lambda : defaultdict(int))

						for record in records:
							if	isinstance(record, dict):

								requests[

									record.get("source_mapped_name")
								][	record.get("target_mapped_name")
								]	+= 1

						return	self.broad_gather(

							requests,
							volume,
							getattr(self, getattr(self, "case_link", ""), None)
						)







