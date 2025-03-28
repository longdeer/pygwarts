import	re
from	pathlib								import Path
from	typing								import List
from	typing								import Tuple
from	typing								import Literal
from	typing								import Optional
from	collections.abc						import Sequence
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.spells				import patronus








class SiftingController(Transmutable):

	"""
		hagrid.cultivation core class that implements filtering of folders/files to be "planted"
		(processed).
		Consists of "controller" (the class itself) which serves as a dispatcher and the Sieve class,
		which does the actual "sifting" (filtering).
		The "controller" part operates on special fields to be provided - "include" and "exclude", which
		refers to corresponding "folders/files to be included" and "folders/files to be excluded". This
		fields might be populated by either compiled Patterns or compilable strings, which both must
		represent the desired items to be excluded/included for "planting". The item's precision is a
		tricky thing, like it is allowed to use any wild cards, even just ".+", but the end effect
		of such filtering might depend on the other factors of "planting" organization. In initiation time
		this fields will be searched for and handled by special method "pmake_field" to provide another
		corresponding fields "include_field" and "exclude_field", which will be used as arguments in
		Sieve part. It is possible to attach directly a list of strings/Patterns or new
		include_field/exclude_field processed by call to "pmake_field" at any time, or just pass some as
		optional key-word-only arguments to __call__ (the last one option always get priority over fields).
		The "controller" invocation must be granted "sprigs" argument - list of folders/files as Path
		objects to be filtered, as first and only positional argument. Additional optional key-word-only
		arguments might be provided:
			popping	-	boolean flag, which if True, allows to alter "sprigs" list by removing
						folders/files that was sifted out (this is the main reason why "sprigs" must always
						be the list, cause the original design implies "sprigs" to be obtained from object,
						which will use this altered list, so this modifications must are able to affect such
						object behavior; in other words, when popping used in *"global" folders sifting by
						default, every folder that was popped from "sprigs" list will not be processed
						further, hence that folder content will not be considered).
						False by default;
			thriving -	boolean flag, which if True, allows additional matching for "include_field". This
						matching suggests convenient usage of "include_field", such providing regular
						expression with wildcards at the end, but a real path in the beginning. When some
						parent folder of desired "includable" is considered, simple matching will not work,
						cause Sieve relies on "fullmatch" only, and as result that parent folder will be
						sifted out and desired child item won't be reached. For such cases "thriving" flag
						is toggled on by default in *"global" folders sifting for "include_field" processing
						in Sieve, so special method "thriving_check" will check if current branch will
						return True for any "includable" pattern string "startswith" method, to make final
						decision about sifting.
						False by default.
		The "controller" __call__ will return a new list of filtered folders/files as Path objects in case
		of success, or the original "sprigs" list of Path objects otherwise.
		The original design of "planting" require "SiftingController" for folders to be declared as "twigs"
		and for files as "leafs". Only this names will be searched by default in hagrid to handle any sifting.
		The very important thing, that hagrid has 2 basic "siftings": *"global" and "local".
		First one implies filtering for every Tree to be "planted", while "local" is an auxiliary option.
		In their difference lies the necessity of isolated declaration - "global" must have it's very own
		"controllers", which are reachable only for *object that implements "global" sifting; "local" might
		be declared anywhere except *"global" object, with only restriction that it must be reachable for
		the Tree objects it is belong to. As the default behavior of *"global" object and Tree objects
		include the phase of automatic sifting invocation, Tree objects might be encapsulated to Copse object
		to provide common "controllers", and also to isolate some Tree objects form another and from *"global"
		object, that Copse might be encapsulated in any more Copse objects. Last idea will allow isolate
		"controllers" of Tree objects from *"global" object when the last one doesn't have it's own, and
		they will be search by escalation. Anyway, the situation when *"global" object and Tree object share
		"controllers" is not dangerous, and, when fields are well organized, might only lead to redundant
		sifting for already sifted items. "controllers" for both "global" and "local" might be omitted.

		*	- refer to hagrid.planting.Flourish
	"""

	include	:Optional[Tuple[str | re.Pattern]]
	exclude	:Optional[Tuple[str | re.Pattern]]


	def pmake_field(self, entities :Sequence[str | re.Pattern]) -> List[re.Pattern] :

		"""
			SiftingController helper method, that accepts sequence of entities to produce list of Patterns
			objects to be used for SiftingController.Sieve. Entities must be whether compiled Patterns, or
			compilable strings. Always return list, which might be empty in case of empty "entities" or
			if no entity satisfied the above condition, with every Exception that raised being logged.
		"""

		self.loggy.debug(f"Making field from {len(entities)} entities")
		patterns = list()


		for candidate in entities:
			match candidate:


				case re.Pattern():

					patterns.append(candidate)
					self.loggy.debug(f"Added pattern \"{candidate.pattern}\"")


				case str():
					try:

						patterns.append(re.compile(candidate))
						self.loggy.debug(f"Made pattern \"{candidate}\"")


					except	Exception as E:

						self.loggy.warning(f"{self} didn't made pattern \"{candidate}\" due to {patronus(E)}")
				case _:	self.loggy.warning(f"Unpatternable type {type(candidate)}")
		return	patterns




	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		if	hasattr(self, "exclude"):
			if	isinstance(self.exclude, list | tuple) and len(self.exclude):
				if	(excludables := self.pmake_field(self.exclude)):

					self.exclude_field = list(excludables)
					self.loggy.debug(f"Exclude field length: {len(self.exclude_field)}")
			else:	self.loggy.warning(f"{self} exclude field improper, must be not empty list or tuple")
		else:		self.loggy.debug("Exclude field not implemented for sifting")




		if	hasattr(self, "include"):
			if	isinstance(self.include, list | tuple) and len(self.include):
				if	(includables := self.pmake_field(self.include)):

					self.include_field = list(includables)
					self.loggy.debug(f"Include field length: {len(self.include_field)}")
			else:	self.loggy.warning(f"{self} include field improper, must be not empty list or tuple")
		else:		self.loggy.debug("Include field not implemented for sifting")








	def __call__(
					self,
					sprigs		:List[Path],
					*,
					excludables	:Sequence[re.Pattern]	=None,
					includables	:Sequence[re.Pattern]	=None,
					popping		:bool					=False,
					thriving	:bool					=False
				)-> List[Path] :


		if	callable((sifted := getattr(self, "Sieve", None))):
			if	isinstance(sprigs, list) and not (sifted_sprigs := list()):


				for sprig in sprigs:
					if	isinstance(sprig, Path):

						siftable = str(sprig)
						self.loggy.debug(f"Considering siftable \"{siftable}\"")


						# The optional key-word-only arguments always get priority over corresponding
						# fields that might be omitted or created improperly, so the ability of using
						# different excludables/includables grants flexibility. It is important to note,
						# that excluding always goes before including, even in arguments.
						if	not sifted(
							siftable,

							exclude=excludables if excludables is not None else
							getattr(self, "exclude_field", None),

							include=includables if includables is not None else
							getattr(self, "include_field", None),

							thriving=thriving
						):
							sifted_sprigs.append(sprig)
							self.loggy.debug(f"Passed sprig \"{sprig.name}\"")
						else:
							self.loggy.debug(f"Sifted sprig \"{sprig.name}\"")
					else:	self.loggy.warning(f"{self} found invalid sprig \"{sprig}\"")




				# Removing instead of actually popping the sifted out sprigs from original list.
				# It is important, that current logic relies on maintaining "sprigs" list, that
				# was obtained from some object, which will use modified list, and it is incorrect
				# to just reassign "sprigs" to sifted sprigs.
				if	popping:
					for thorn in [ sprig for sprig in sprigs if sprig not in sifted_sprigs ]:

						sprigs.remove(thorn)
				return	sifted_sprigs
			else:		self.loggy.warning(f"{self} found invalid sprigs type {type(sprigs)}")
		else:			self.loggy.debug("Sieve not implemented for current controller")


		# Sifting gone wrong, so returning origingal sprigs
		return	sprigs








	class Sieve(Transmutable):

		"""
			hagrid.cultivation.SiftingController implementation of actual "sifting" (folders/files filtering).
			This object relies on 2 lists "exclude" and "include", which must content Patterns to matched
			with provided argument "siftable", which must be a string that represents folder/file absolute
			path to be processed. Those 2 lists are mandatory key-word-only arguments, will be iterated over
			to "fullmatch" siftable with any "excludable/includable", and "excludables" has a priority to be
			processed first. If "excludables" and "includables" are not the subjects to be provided, it must
			be provided as None both, as "controller" does by default. Last mandatory key-word-only argument
			is boolean flag "thriving", which if True, allows additional matching for "includables" by use of
			special method "thriving_check", that will check if current siftable will return True for any
			"includable" pattern string "startswith" method, to make final decision about "siftable". This
			matching suggests convenient usage of "includables", such providing regular expression with
			wildcards at the end, but a real path in the beginning. When some parent folder of desired
			"includable" is considered, simple matching will not work, cause Sieve relies on "fullmatch"
			only, and as result that parent folder will be sifted out and desired child item won't be reached.
			For such cases "thriving" option might be used, and it is used by default in *"global" folders
			sifting.
			This object's __call__ return value is boolean, which means whether provided "siftable"
			argument if sifted (filtered) out or not, so "True" is the signal for caller to NOT "plant" that
			siftable. This boolean might be obtained as follows:
				True	-	at the very beginning of __call__ if provided "siftable" is not a string.
				True	-	in "excludables" iterating, when provided "siftable" have a match.
				False	-	in not empty "includables" iterating, when provided "siftable" have a match.
				False	-	after "includables" processing, when "includables" is None.
				True	-	default return value, which will be returned by default if none of below
							happened, or if there was any trouble during "includables" iteration, as
							whether to include "siftable" is a picky moment. The "excludables" iterating
							has the opposite logic, that when any trouble occurs, "excludables" skipped,
							just like when it's None or empty.

			* - refer to hagrid.planting.Flourish
		"""

		def thriving_check(self, includable :re.Pattern, siftable :str) -> Literal[True] | None :

			"""
				Sieve helper method to check if "siftable" is a substring of "includable".
				Suggests convenient usage of "include_field", such providing regular expression with
				wildcards at the end, but a real path in the beginning. When some parent folder of desired
				"includable" is considered, simple matching will not work, cause Sieve relies on "fullmatch"
				only, and as result that parent folder will be sifted out and desired child item won't be
				reached. When current method return True it is a signal for caller, that "siftable" is a
				path to "includable" so it must not be sifted (filtered) out.
			"""

			if	isinstance(includable, re.Pattern):
				if	isinstance(siftable, str):
					if	includable.pattern.startswith(siftable):

						self.loggy.debug("Thriving check passed")
						return	True




		def __call__(
						self,
						siftable	:str,
						*,
						exclude		:List[re.Pattern] | None,
						include		:List[re.Pattern] | None,
						thriving	:bool
					)-> bool		:


			if	not isinstance(siftable, str):

				self.loggy.debug(f"Got invalid siftable \"{siftable}\"")
				return	True




			if	exclude is not None:
				if	isinstance(exclude, list):


					for excludable in exclude:


						if	isinstance(excludable, re.Pattern):
							if	excludable.fullmatch(siftable):

								self.loggy.debug(f"Exclude field triggered, \"{siftable}\" sifted")
								return	True
						else:	self.loggy.debug(f"Got invalid excludable \"{excludable}\"")
					else:		self.loggy.debug("Exclude field passed")
				else:			self.loggy.debug(f"Got invalid exclude field")
			else:				self.loggy.debug("Exclude field skipped")




			if	include is not None:
				if	isinstance(include, list):


					for includable in include:


						if	isinstance(includable, re.Pattern):
							if	includable.fullmatch(siftable) or (
								thriving and self.thriving_check(includable, siftable)
								):

								self.loggy.debug(f"Include field triggered, \"{siftable}\" passed")
								return	False
						else:	self.loggy.debug(f"Got invalid includable \"{includable}\"")
					else:		self.loggy.debug("Include field not passed")
				else:			self.loggy.debug("Got invalid include field")
			else:


				self.loggy.debug("Include field skipped")
				return	False
			return		True







