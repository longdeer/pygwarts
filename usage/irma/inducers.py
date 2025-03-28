import	os
from	typing							import Dict
from	typing							import List
from	typing							import Optional
from	typing							import Callable
from	typing							import Sequence
from	pygwarts.magical.spells			import patronus
from	pygwarts.irma.shelve			import LibraryShelf
from	pygwarts.irma.access.inducers	import AccessInducer
from	pygwarts.irma.access.volume		import LibraryVolume
from	pygwarts.irma.shelve.casing		import shelf_case
from	pygwarts.irma.shelve.casing		import is_num
from	pygwarts.irma.shelve.casing		import is_iterable
from	pygwarts.irma.shelve.casing		import seq_diff
from	pygwarts.irma.shelve.casing		import num_diff
from	matplotlib						import pyplot








class DiffCaseRegisterRecapAccumulatorInducer(AccessInducer):

	"""
		RegisterRecapAccumulatorInducer variant that implements sequence difference and casing,
		which cannot be done by decoration correctly, so maintained internally via "case_link"
	"""

	case_link	:Optional[str]							# name of the LibraryShelf object for casing
	unique		:Optional[bool]							# flag to eliminate duplicates
	joint		:Optional[str]							# string to join elements

	def __call__(self, volume :LibraryVolume) -> str :

		if	isinstance(recap := self.get_register_recap(volume), list):
			if	getattr(self, "unique", False):


				uniqs	= set()
				accum	= [ acc for acc in map(str,recap) if not (acc in uniqs or uniqs.add(acc)) ]
			else:
				accum	= list(map(str,recap))


			if	isinstance(MAP := getattr(self, getattr(self, "case_link", ""),None), LibraryShelf|dict):


				if	str(volume) not in MAP : MAP[str(volume)] = dict()
				if	(casing := shelf_case(

					accum,
					key=str(self),
					shelf=MAP[str(volume)],
					prep=is_iterable,
					post=seq_diff,
				)):
					return str(getattr(self, "joint", " ")).join(casing)
			return	str(getattr(self, "joint", " ")).join(accum)








class FilchWatchInducer(AccessInducer):

	""" filch AccessInducer super class for DiscoveryWatch and BroadWatch """

	def filch_casing(	self,
						induce	:str | int,
						volume	:LibraryVolume,
						shelf	:LibraryShelf | dict,
						key		:str,
						prep	:Callable[[str|int|Sequence],str|int|Sequence],
						post	:Callable[[str|int|Sequence,str|int|Sequence],str],
					)->	str		:

		if	isinstance(shelf, LibraryShelf | dict):

			if	str(volume) not in shelf : shelf[str(volume)] = dict()
			if	str(self) not in shelf[str(volume)] : shelf[str(volume)][str(self)] = dict()

			if	(casing := shelf_case(

				induce,
				key=key,
				shelf=shelf[str(volume)][str(self)],
				prep=prep,
				post=post,

			))	is not None:

				return casing
		return	induce




	def filch_seq_diff(self, seq1 :Sequence, seq2 :Sequence) -> List[str] :

		delta = set(seq1) - set(seq2 or [])
		return [ f"{'(+) ' if item in delta else ''}{item}" for item in seq1 ]


	def broad_src_diff(self, src :str, value :str | None) -> str :

		return f"(+) {src}" if value != src else src




	def filch_caseamount(self, amount :int, volume :LibraryVolume) -> str:

		return self.filch_casing(

			amount,
			volume,
			getattr(self, getattr(self, "case_link", ""), None),
			"amount",
			is_num,
			num_diff
		)	or str()


	def filch_caserecords(self, records :List[str], volume :LibraryVolume) -> List[str]:

		return self.filch_casing(

			records,
			volume,
			getattr(self, getattr(self, "case_link", ""), None),
			"records",
			is_iterable,
			self.filch_seq_diff
		)	or list()




	def broad_gather(	self,
						requests	:Dict[str,Dict[str,int]],
						volume		:LibraryVolume,
						shelf		:LibraryShelf | dict,
					)->	str or None	:

		"""
			The part for BroadWatch to operate on parsed ARP traffic logs. Groups requests destination
			addresses by sources, sorting in descending order. Also implements special casing the "smart"
			way, so only the single layer receives case mark without redundant propagation.
		"""

		if	isinstance(requests, dict) and len(requests):

			requests_view	= str()
			requests_total	= int()
			sorted_sources	= sorted(

				requests,
				key=lambda src : sum(requests[src][dst] for dst in requests[src]),
				reverse=True
			)


			for src in sorted_sources:

				src_total	= int()
				src_string	= str()
				targets		= requests[src]
				reprtargets	= sorted(targets, key=lambda ip : targets[ip], reverse=True)
				casetargets	= self.filch_casing(

					reprtargets,
					volume,
					shelf,
					src,
					is_iterable,
					self.filch_seq_diff
				)
				casesrc = self.filch_casing(src, volume, shelf, f"{src}-presence", str, self.broad_src_diff)


				for i,target in enumerate(reprtargets):


					current			=	targets[target]
					src_total		+=	current
					requests_total	+=	current


					case_current = self.filch_casing(

						current,
						volume,
						shelf,
						f"{src}-{target}",
						is_num,
						num_diff
					)
					src_string += f"\t\t{target if casesrc.startswith('(+)') else casetargets[i]}"
					src_string += f": {current if casetargets[i].startswith('(+)') else case_current}\n"


				casetotal = self.filch_casing(src_total, volume, shelf, f"{src}-total", is_num, num_diff)
				casetotal = src_total if casesrc.startswith("(+)") else casetotal


				if	len(targets) >1 :	requests_view += f"\t{casesrc}: {casetotal}\n{src_string}"
				else				:	requests_view += f"\t{casesrc}:\n{src_string}"


			case_requests_total = self.filch_casing(

				requests_total,
				volume,
				shelf,
				"total",
				is_num,
				num_diff
			)
			return "%s\n%s"%(case_requests_total if 1 <requests_total else "", requests_view)




	def broad_plot(	self,
					axises		:List[int],
					title		:str,
					pngpath		:str,
					pngname		:str,
					linecolor	:str	="red",
					linewidth	:int	=1,
					fontsize	:int	=20,
					Xlength		:int	=40,
					Ylength		:int	=20,
				)-> str or None	:

		""" Helper method for plotting ARP requests graph of requests number to hours """

		pyplot.figure(figsize=(Xlength,Ylength))
		pyplot.title(title, fontsize=fontsize)


		try:	os.makedirs(pngpath, exist_ok=True)
		except	Exception as E : self.loggy.critical(f"Path {pngpath} {patronus(E)}")
		else:

			try:

				Ys = set()
				for X,Y in axises:

					Ys.add(Y)
					pyplot.vlines(

						x=X,
						ymin=0,
						ymax=Y,
						linewidth=linewidth,
						color=linecolor,
					)


			except	Exception as E : self.loggy.critical(f"Failed to plot {title} due to {patronus(E)}")
			else:

				# X-axis tuning to be 24 hours scale
				pyplot.xlabel("Hours (MSK)", fontsize=fontsize)
				pyplot.xlim(-10, 2310)
				pyplot.xticks(

					[ i for i in range(0, 2400, 100) ],
					labels=[ i for i in range(24) ],
					fontsize=fontsize,
				)

				# Y-axis tuning
				pyplot.ylabel("ARP requests", fontsize=fontsize)
				pyplot.ylim(0)
				pyplot.yticks(

					[ tick for tick in self.make_Y_ticks(max(Ys), Ylength) if tick in Ys ],
					fontsize=fontsize
				)

				savepath = os.path.join(pngpath, pngname)
				pyplot.savefig(savepath)
				pyplot.close()


				return	savepath


			finally:	pyplot.close()
		finally:		pyplot.close()




	def make_Y_ticks(self, Ymaximum :int, Ylength :int) -> range :

		if	(step := Ymaximum //(2 *Ylength)):

			return	range(Ymaximum %step, Ymaximum +1, step)
		return		range(Ymaximum +1)







