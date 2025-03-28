import	re
from	pathlib								import Path
from	typing								import Dict
from	typing								import List
from	typing								import Tuple
from	typing								import Callable
from	pygwarts.magical.spells				import patronus
from	pygwarts.hagrid.bloom				import Bloom
from	pygwarts.hagrid.thrivables			import Tree
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class Efflorescence(Bloom):

	"""
		Implementation of Bloom object that processes both folders and files, but at destination (bough)
		and by processing removing is meant. Complies the "bloom-interface":
			accepts:
				origin	- current Tree object to be processed;
				sprout	- current source root folder as a string;
				branch	- current source working directory as a Path object;
				twigs	- list of Path objects as current source folders;
				leafs	- list of Path objects as current source files.
			return:
				None.

		++++++++++++++	ATTENTION
		++++++++++++++	MUST
		++++++++++++++	BE
		++++++++++++++	PAID
		++++++++++++++	FURTHER

		As current class serves as an instrument, which will cause

											UNRECOVERABLE

											REMOVING

											OF

											DATA

		please read carefully following doc string section to prevent ANY UNWANTED CONSEQUENCES!

		This class consists of __call__, which include proper "planting" organization, and if no obstacles
		are found - initiates bough twigs/leafs (target folders/files) removing separately, by invoking
		crucial method "sprigs_trimming". Along with many arguments, which "sprigs_trimming" accepts,
		there are "sprout_sprigs" and "bough_sprigs", which must be explained a lot.
		There is some difference between "regular" Bloom object, like *Rejuvenation or **Germination, which
		takes corresponding leafs or twigs of source folder and implements "planting" to target folder.
		In "Efflorescence", for any "bough sprig" (target folder/file) to be removed, it is must be checked
		against corresponding "sprout sprig" (source folder/file), which means, that if current source branch,
		that is currently walked, exists at target location and there are some "bough sprigs" that aren't
		represented as "sprout sprigs", those "bough sprigs" will be removed. In order for such "planting"
		to be possible, "sprigs_trimming" method takes "sprout_sprigs", that are "bloom-interface" arguments
		"twigs" and "leafs", and takes "bough_sprigs", that are obtained from "current_bough" branch (target
		folder, that is correspond to current source folder, by taking source folder relative to source root
		folder path and join it to target root folder) lists of Path objects as "bough_twigs" and
		"bough_leafs", to first produce, by helper method "ingather", the list of "trimmable_sprigs", which
		is a list of Path objects that represent "twigs" and "leafs" of bough, that are not represented in
		sprout, so they can be removed, and actually removes them.
		All operations, described above, are guarded by 2 mandatory conditions for "Efflorescence" to satisfy:
			branches	- escalatable field, that must be a dictionary, that maps any "bough", that must be
						effloresced, as a string object with a tuple of strings, that represents "sprouts",
						against which efflorescence is allowed. In other words, that dictionary keys must be
						a target root folder path strings, and their values must be tuples with source folders
						path strings. Any sprout-bough pair will be checked for presence in "branches", and
						efflorescence will proceed only if this condition is satisfied. This dictionary values
						must only be tuples to ensure it was obtained the right way only.
			controllers	- for every "origin" (Tree object) to be effloresced, there must be corresponding
						escalatable "SiftingController" objects (mandatory named as twigs/leafs), that must
						have "include_field" initialized and content the item for current "origin" bough
						to be matched. In other words, the Tree object will be effloresced if it's
						corresponding "twigs" and "leafs" "controllers" will exist and will have it's
						"include_field" organized to have a match for current bough branch. Also exclude_field
						might be used to exclude some bough branches from Efflorescence.
		The last thing required by "Efflorescence" is a typical for Bloom object condition, that mandatory
		callable "trim" must be escalatable for every "origin" and must implement "planting interface"
		to accept following arguments:
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			sprig	- Path object that represents current "planting" source folder/file;
			bough	- Path object that represents current "planting" destination parent folder.
		Any Exception raised by "trim" might not be handled by "trim", as originally designed, but will be
		handled by this Bloom object. In this case, after the Exception will be handled, the iteration over
		leafs list will be continued. The iteration will be stopped if either "origin" argument is not a
		Tree object, or "origin" is a Tree object but with invalid "bough" field, or the "trim"
		implementation either not callable or not found.
		 ____________________________________________________________________________________________________
		|											RESUMING												 |
		|____________________________________________________________________________________________________|
		| The "Efflorescence" object is a callable, that implements special interface, to remove target      |
		| folders and files. Dictionary "branches" must be a reachable for "Efflorescence" object field,     |
		| that content target for folders strings mapped with tuples of source folders strings. Every Tree   |
		| object, as target, must have reachable objects "twigs" and "leafs" for execution of corresponding  |
		| folders and files removing. Each Tree object's "twigs" and "leafs" must have "include_field" that  |
		| content strings or regular expressions for target location items to be removed. "exclude_field" of |
		| every Tree object might also content strings or regular expressions for target location items to   |
		| to not be removed. The removing relies on callable object "trim", that implements special interface|
		| to handle folders and files removing.                                                              |
		|____________________________________________________________________________________________________|

		*	- refer to hagrid.bloom.leafs.Rejuvenation
		**	- refer to hagrid.bloom.leafs.Germination
	"""

	branches	:Dict[str, Tuple[str,...]]

	def ingather(self, sprout_sprigs :List[Path], bough_sprigs :List[Path]) -> List[Path] :

		"""
			Helper method that provides the way to fetch the list of sprigs to be trimmed as Path objects,
			by maintaining the difference between set of sprig names at current bough branch against set
			of sprig names at current sprout branch.
			As "bloom-interface" operates with "twigs" and "leafs" lists of Path objects, and the difference
			between sprout branch and bough branch is the corresponding Path objects "name" properties, as
			corresponding folders/files relative paths, current method produces list of Path objects,
			that are correspond to difference between set of current source names and target names.
		"""

		if	isinstance(sprout_sprigs, list) and isinstance(bough_sprigs, list):

			sprout_map	= { sprig.name: sprig for sprig in sprout_sprigs }
			bough_map	= { sprig.name: sprig for sprig in bough_sprigs }
			return		[ bough_map[name] for name in set(bough_map).difference(sprout_map) ]

		self.loggy.warning(f"{self} failed to ingather sprout and bough sprigs")




	def sprigs_trimming(
							self,
							origin			:Tree,
							sprout			:str,
							branch			:Path,
							bough_sprigs	:List[Path],
							bough			:Path,
							sprout_sprigs	:List[Path],
							trim_type		:str,
							trimmer			:Callable[[Tree, str, Path, Path, Path], None],
						):

		"""
			Efflorescence core method, which in charge for actual folders and files removing.
			Accepts following positional arguments:
				origin			- current Tree object to be processed;
				sprout			- current source root folder as a string;
				branch			- current source working directory as a Path object;
				bough_sprigs	- list of Path objects that represents current target working folder
								items (folders and files);
				bough			- current target root folder as a Path object;
				sprout_sprigs	- list of Path objects that represents current source working folder
								items (folders and files);
				trim_type		- string that represents the type of items currently processing, "twigs"
								for folders and "leafs" for files;
				trimmer			- callable "planting" object, that handles removing operation.
			Validates current "origin" to have corresponding valid "controllers". Next initiates that
			"controllers" filtering to obtain list of actual items to be removed. At last iterates
			over those "trimmable_sprigs" list and invoke provided "trimmer" callable, which must
			execute actual removing and must implements the "planting interface" to accept arguments:
				origin	- Tree object that is currently in "planting";
				sprout	- string that represents the current source root;
				branch	- Path object that represents current source folder;
				leaf	- Path object that represents current operation source file;
				bough	- Path object that represents current operation destination parent folder.
			Returns None.
		"""

		if	isinstance((controller := getattr(origin, trim_type, None)), SiftingController):
			if	hasattr(controller, "include_field"):


				trimmable_sprigs = self.ingather(sprout_sprigs, controller(bough_sprigs))
				self.loggy.debug(f"Number of trimmable {trim_type}: {len(trimmable_sprigs)}")


				for sprig in trimmable_sprigs:
					try:

						trimmer(origin, sprout, branch, sprig, bough)
						self.mark_tree(str(origin), "trim")
						self.loggy.debug(f"Effloresced \"{sprig}\"")


					except	Exception as E:

						self.loggy.warning(f"Failed to effloresce \"{sprig}\" due to {patronus(E)}")
			else:		self.loggy.debug(f"Include field for {trim_type} not found")
		else:			self.loggy.debug(f"Controller for {trim_type} not found")




	def includable(self, bough :str) -> Tuple[str,...] :

		"""
			Helper method that serves as a validator for bough-sprout pairs in "branches" dictionary.
			If "bough" string, that must represent Tree object bough field, is an existent key in
			"branches", which mapped with a tuple of strings, that must represent corresponding sprouts
			mapped with current "bough" for efflorescence, that tuple will be returned.
			In any other cases logs corresponding debug message and returns empty tuple.
		"""

		if	isinstance(getattr(self, "branches", None), dict):
			if	(sprouts := self.branches.get(str(bough))) is not None:
				if	isinstance(sprouts, tuple):


					return	sprouts
				else:
					self.loggy.debug(f"Invalid sprouts mapping for \"{bough}\"")
			else:	self.loggy.debug(f"Bough \"{bough}\" not included for Efflorescence")
		else:		self.loggy.debug("No branches included for Efflorescence")
		return		tuple()




	def __call__(self, origin :Tree, sprout :str, branch :Path, twigs :List[Path], leafs :List[Path]):


		if	isinstance(getattr(self, "branches", None), dict) and isinstance(sprout, str):
			if	isinstance(origin, Tree) and isinstance((bough := getattr(origin, "bough", None)), Path):


				# IMPORTANT: "trim" to be invoked from "origin" to ensure right escalation, as "planting"
				# invocation must be issued not from Bloom object but from Tree object to be processed.
				# Further "planting" invocation relies on callable "trim", that escalated from
				# the current Tree object, to implement "planting interface". The chain of calls,
				# that will lead to that moment assumes all arguments are valid, cause the original
				# design of "planting" object doesn't involve arguments validation. That means
				# only "origin" validation at the beginning guards possible Exceptions, that might
				# be raised in "trim" because of arguments inconsistency, and which all won't be
				# handled by original "planting" design but will be caught back in current Bloom,
				# by special method "sprigs_trimming" implementation.
				if	callable(trim := getattr(origin, "trim", None)):
					if	(current_bough := bough.joinpath(branch.relative_to(sprout))).is_dir():
						self.loggy.debug(f"Commencing efflorescence of \"{current_bough}\"")


						sprigs		= list(current_bough.iterdir())
						bough_twigs	= list(filter(Path.is_dir,	sprigs))
						bough_leafs	= list(filter(Path.is_file,	sprigs))


						if	len(bough_twigs) or len(bough_leafs):
							if	sprout in self.includable(bough):


								self.sprigs_trimming(

									origin,
									sprout,
									branch,
									bough_twigs,
									bough,
									twigs,
									"twigs",
									trim
								)
								self.sprigs_trimming(

									origin,
									sprout,
									branch,
									bough_leafs,
									bough,
									leafs,
									"leafs",
									trim
								)
							else:	self.loggy.debug(f"Sprout \"{sprout}\" not included for Efflorescence")
						else:		self.loggy.debug(f"No sprigs to effloresce \"{current_bough}\"")
					else:			self.loggy.debug(f"Bough \"{current_bough}\" not thrived")
				else:				self.announce_implement(str(origin), "trim")
			else:					self.announce_bough(str(origin), "effloresce")
		else:						self.loggy.debug("Branches not found or sprout is not a string")







