from pygwarts.magical.time_turner				import TimeTurner
from pygwarts.magical.time_turner.timers 		import Callstamp
from pygwarts.irma.contrib						import LibraryContrib
from pygwarts.irma.shelve						import LibraryShelf
from pygwarts.irma.shelve.casing				import is_num
from pygwarts.irma.shelve.casing				import num_diff
from pygwarts.irma.access						import LibraryAccess
from pygwarts.irma.access.volume				import LibraryVolume
from pygwarts.irma.access.bookmarks				import VolumeBookmark
from pygwarts.irma.access.bookmarks.counters	import WarningCount
from pygwarts.irma.access.bookmarks.counters	import ErrorCount
from pygwarts.irma.access.bookmarks.counters	import CriticalCount
from pygwarts.irma.access.bookmarks.viewers		import ViewWrapper
from pygwarts.irma.access.bookmarks.viewers		import ViewCase
from pygwarts.irma.access.handlers				import AccessHandlerRegisterCounter
from pygwarts.irma.access.handlers.counters		import AccessCounter
from pygwarts.irma.access.handlers.parsers		import TargetHandler
from pygwarts.irma.access.handlers.parsers		import TargetNumberAccumulator
from pygwarts.irma.access.handlers.parsers		import TargetStringAccumulator
from pygwarts.irma.access.inducers				import AccessInducer
from pygwarts.irma.access.inducers.counters		import RegisterCounterInducer
from pygwarts.irma.access.inducers.recap		import RegisterRecapInducer
from pygwarts.irma.access.inducers.filters		import plurnum
from pygwarts.irma.access.inducers.filters		import posnum
from pygwarts.irma.access.inducers.case			import InducerCase
from pygwarts.irma.access.annex					import VolumeAnnex
from pygwarts.irma.access.annex					import LibraryAnnex
from pygwarts.irma.access.utils					import TextWrapper
from pygwarts.filch.marauders_map				import MaraudersMap
from casing										import mostsec_diff
from casing										import byte_size_diff
from bookmarks									import DiscoveryWatch
from bookmarks									import BroadWatch
from inducers									import DiffCaseRegisterRecapAccumulatorInducer








class Irma(LibraryAccess):

	"""
		Complex LibraryAccess class that implements various hagrid and filch loggy parsing to produce
		total report. Collects following data:
			WARNING, ERROR, CRITICAL messages count;
			total and average execution time with invocation count;
			LibraryShelf producing and removing count;
			all hagrid planting messages;
			all filch HostDiscovery information;
			all filch ARPSniffer information with requests graph plotting.
		Uses MaraudersMap hosts recognizing for filch messages. Uses TextWrapper and ViewWrapper decorators
		for formatting. Uses shelf casing functionality for statistics maintaining.
	"""

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	class filchmap(MaraudersMap):	pass
	class library_shelf(LibraryShelf):

		grabbing	= "previous stats shelf file path (optional)"
		producing	= "new stats shelf file path (optional)"

	case_link	= "library_shelf"	# LibraryShelf object attribute name for stats maintaining
	unique		= True				# Inducers flag to return only unique values (no duplicates)
	joint		= ", "				# Inducers string to join values with in final string

	@Callstamp
	class Annex(LibraryAnnex): 		pass


	@ViewWrapper("\nWARNINGS: ")
	@ViewCase("library_shelf", prep=is_num, post=num_diff)
	class Warnings(WarningCount):	pass
	@ViewWrapper("\nERRORS: ")
	@ViewCase("library_shelf", prep=is_num, post=num_diff)
	class Errors(ErrorCount):		pass
	@ViewWrapper("\nCRITICALS: ")
	@ViewCase("library_shelf", prep=is_num, post=num_diff)
	class Criticals(CriticalCount):	pass


	# Following bookmark recreated to provide "library_shelf" casing link
	class CallstampActivity(VolumeBookmark):

		trigger		= " finished in "
		rpattern	= r"finished in (?P<target>[\.\d]+)( seconds)?$"

		class Activities(AccessCounter):

			@TextWrapper("\nactivities: ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class Inducer(RegisterCounterInducer): filter = plurnum

		@AccessHandlerRegisterCounter
		class Duration(TargetNumberAccumulator):

			@TextWrapper("\ntotal time: ")
			@InducerCase("library_shelf", prep=is_num, post=mostsec_diff)
			class Total(RegisterRecapInducer): filter = posnum

			@TextWrapper("\naverage time: ")
			@InducerCase("library_shelf", prep=is_num, post=mostsec_diff)
			class Average(AccessInducer):
				def __call__(self, volume :LibraryVolume) -> str | None :

					if	isinstance(recap := self.get_register_recap(volume), int | float):
						if	isinstance(counter := self.get_register_counter(volume), int):
							if	1 <counter : return str(recap /counter)


	# Following irma and hagrid bookmarks are reflect the concrete use
	# with "library_shelf" casing link
	class ShelfTrackers(VolumeBookmark):

		trigger	= "cleaned out from original shelf"

		class Counter(AccessCounter):

			@TextWrapper("\ntrackers removed: ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class Inducer(RegisterCounterInducer): filter = posnum

	class ShelfProduces(VolumeBookmark):

		trigger	= "successfully produced"

		class Counter(AccessCounter):

			@TextWrapper("\nshelve produced: ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class Inducer(RegisterCounterInducer): filter = posnum

	class GrownCounter(VolumeBookmark):

		trigger		= "Grown leaf"
		rpattern	=  r".+ Grown leaf \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfiles copied ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class MovedCounter(VolumeBookmark):

		trigger		= "Moved leaf"
		rpattern	=  r".+ Moved leaf \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfiles moved ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class ClonedCounter(VolumeBookmark):

		trigger		= "Cloned leaf"
		rpattern	=  r".+ Cloned leaf \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfiles cloned ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class PushedCounter(VolumeBookmark):

		trigger		= "Pushed leaf"
		rpattern	=  r".+ Pushed leaf \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfiles pushed ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class ThrivedCounter(VolumeBookmark):

		trigger		= "Thrived twig"
		rpattern	=  r".+ Thrived twig \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfolders copied ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class TrimmedLeafsCounter(VolumeBookmark):

		trigger		= "Trimmed leaf"
		rpattern	=  r".+ Trimmed leaf \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfiles removed ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class TrimmedTwigsCounter(VolumeBookmark):

		trigger		= "Trimmed twig"
		rpattern	=  r".+ Trimmed twig \".+[/\\](?P<target>[^/\\]+)\"$"

		@AccessHandlerRegisterCounter
		class Accumulator(TargetStringAccumulator):

			@TextWrapper("\nfolders removed ",": ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class CountInducer(RegisterCounterInducer): filter = posnum
			class ReprInducer(DiffCaseRegisterRecapAccumulatorInducer):	pass

	class WieghtCounter(VolumeBookmark):

		trigger	= "INFO : Size:"
		rpattern= r".+ Size: (?P<target>\d+)$"

		class Handler(TargetHandler):
			@TextWrapper("\ntotal space: ")
			@InducerCase("library_shelf", prep=is_num, post=byte_size_diff)
			class Inducer(RegisterRecapInducer):						pass

	class TwigsCounter(VolumeBookmark):

		trigger	= "INFO : Twigs:"
		rpattern= r".+ Twigs: (?P<target>\d+)$"

		class Handler(TargetHandler):
			@TextWrapper("\nfolders: ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class Inducer(RegisterRecapInducer):						pass

	class LeafsCounter(VolumeBookmark):

		trigger	= "INFO : Leafs:"
		rpattern= r".+ Leafs: (?P<target>\d+)$"

		class Handler(TargetHandler):
			@TextWrapper("\nfiles: ")
			@InducerCase("library_shelf", prep=is_num, post=num_diff)
			class Inducer(RegisterRecapInducer):						pass


	class SoftSync(LibraryVolume):

		inrange		= "date string to parse loggy with"
		location	= "loggy file path to parse"
		@TextWrapper("\n\thagrid-softsync\n","\n")
		class Annex(VolumeAnnex):		pass

	class HardSync(LibraryVolume):

		inrange		= "date string to parse loggy with"
		location	= "loggy file path to parse"
		@TextWrapper("\n\thagrid-hardsync\n","\n")
		class Annex(VolumeAnnex):		pass

	class Arch(LibraryVolume):

		inrange		= "date string to parse loggy with"
		location	= "loggy file path to parse"
		@TextWrapper("\n\thagrid-arch\n","\n")
		class Annex(VolumeAnnex):		pass

	class Discovery(LibraryVolume):

		inrange		= "date string to parse loggy with"
		location	= "loggy file path to parse"
		@TextWrapper("\n\tfilch-discovery\n","\n")
		class Annex(VolumeAnnex):		pass
		class filchmap(MaraudersMap):	pass
		class Watch(DiscoveryWatch):	pass

	class Broad(LibraryVolume):

		inrange		= "date string to parse loggy with"
		location	= "loggy file path to parse"
		plotdir		= "directory for ARP requests stat graphs"
		plotdate	= TimeTurner		# TimeTurner object for graph plotting
		@TextWrapper("\n\tfilch-broadwatch\n","\n")
		class Annex(VolumeAnnex):		pass
		class Watch(BroadWatch):		pass








if	__name__ == "__main__":

	irma = Irma()
	irma.filchmap.CSV(

		"path to csv",
		";",			# delimiter for csv file parsing
		IP4=0,			# IP4 address column index
		MAC=1,			# MAC address column index
		NAME=2,			# host name column index
		DESC=3			# host description column index
	)
	irma.Discovery.filchmap.CSV(

		"path to csv",
		";",			# delimiter for csv file parsing
		IP4=0,			# IP4 address column index
		MAC=1,			# MAC address column index
		NAME=2,			# host name column index
		DESC=3			# host description column index
	)
	report = irma.Annex()
	irma.library_shelf.produce(ignore_mod=True, strict_mode=False)

	if	len(report):
		with open("file path to save report", "w") as dump:
			dump.write(report)







