from pathlib								import Path
from typing									import List
from typing									import Tuple
from typing									import Optional
from typing									import Generator
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse
from pygwarts.hagrid.bloom					import Bloom
from pygwarts.hagrid.cultivation.sifting	import SiftingController








def unplantable(*plant :Tuple[str, Path, List[Path], List[Path]]) -> None | str :

	"""
		Helper function that validates "plant" consistency.
		All collected "plant" items must represent a tuple of four objects:
			1. a string representing "sprout" for current plant;
			2. a Path object representing current branch for current plant;
			3. list of Path objects representing current branch twigs for current plant;
			4. list of Path objects representing current branch leafs for current plant.
		If "plant" fully suffices returns None, otherwise the string message what is wrong.
	"""

	if	(pcount := len(plant)) != 4:		return	f"Invalid plant length {pcount}"
	elif(not isinstance(plant[0], str)):	return	f"Invalid plant sprout \"{plant[0]}\""
	elif(not isinstance(plant[1], Path)):	return	f"Invalid plant branch \"{plant[1]}\""
	elif(not isinstance(plant[2], list)):	return	f"Invalid plant twigs {type(plant[2])}"
	elif(not isinstance(plant[3], list)):	return	f"Invalid plant leafs {type(plant[3])}"








class Flourish(Transmutable):

	"""
		hagrid core functionality class, that serves as a "planting dispatcher", which means the Flourish
		object is responsible for every Tree object processing.
		Flourish implementation suggests __call__ will accept the Tree object that represent current target
		object and a tuple of four objects: string object representing current sprout (source root folder),
		Path object representing branch (current source folder to be processed) and two lists of Path objects,
		that are twigs and leafs (current source folder folders and files).
		This is mandatory interface and Folurish is guarded by precheks. In __call__ "unplantable" helper
		function is used to check "plant" consistency, so every "plant", that not a tuple of valid four, will
		be skipped. Such strict interface requirements must ensure right usage, as was originally designed.
		For valid "plant" there are three steps of "planting" (processing) in Flourish:
			1.	Global sifting phase (or first step filter). This is the main folders/files filtering, that
		will affect every Tree object participated in Flourish. For this phase there must be SiftingController
		objects to be reachable for Flourish object (declared in escalation) - "twigs" for folders and
		"leafs" for files. The best way to declare them is right under the Flourish object, cause that will
		ensure reachability and also isolation from any Tree/Copse objects. Any or both might be omitted.
			2.	Local sifting phase (or Tree objects extra sifting). After global sifting, "innervate" will
		start it's primary job - starting from the "origin" argument, that must be the upper layer Copse or
		Tree object, "innervate" will find every Tree object in vicinity, iterating over upper layer Copse
		object and it's Copse objects respectively, in order to start "planting" it (processing). This phase
		is transitional, means it allows the start of final third phase for every Tree object found, but
		before this will happen, "innervate" invokes SiftingController objects for every Tree object as extra
		filtering. As every valid Tree objects implemented to have 2 special methods "twigify" for "twigs"
		and "leafify" for leafs, those methods will try to invoke "controllers" if they will find some.
			3. Trees blooming (processing every reachable Tree object). Every Tree object, that yielded by
		"grove" helper method, will be iterated and every Bloom object assigned to its Tree will be invoked.
		This invocation relies every Bloom object implements "bloom-interface":
			accepts:
				origin	- current Tree object to be processed;
				sprout	- current source root folder as a string;
				branch	- current source working directory as a Path object;
				twigs	- list of Path objects as current source folders;
				leafs	- list of Path objects as current source files.
			return:
				None.
		For Flourish object to get it's job done, it's upper layer must be a single Tree or an upper Copse
		object, that encapsulates all possible Tree and other Copse objects.
	"""


	twigs	:Optional[SiftingController]
	leafs	:Optional[SiftingController]


	def grove(self, origin :Copse | Tree) -> Generator[Tree, None,None] | None:

		"""
			Helper method that searches for Tree objects in some scope.
			The only argument "origin" serves as a entering point for search when it's first time called.
			If it is a Tree object, it is yielded and "grove" stops. If it is a Copse object, it will be
			iterated and every Tree object found will be yielded, while every nested Copse object will be
			used as "origin" for recursive call. Any other object is skipped and logged with warning.
		"""

		match origin:

			case Copse():
				for inner in origin:

					self.loggy.debug(f"Walking copse {origin} inner {inner}")
					yield	from	self.grove(inner)
			case Tree():	yield	origin
			case _:			self.loggy.warning(f"Invalid thrivable \"{origin}\" for flourish")


	def innervate(self, origin :Copse | Tree, *plant :Tuple[str, Path, List[Path], List[Path]]):

		"""
			Flourish core method that responsible for innervating "planting" for every Tree object.
			Accepts first positional argument "origin", which must refer to the entering point for "grove"
			helper method. All further arguments will be collected as "plant" and considered to be a tuple
			of sprout (source root folder) as a string, current branch as Path object, current branch
			twigs and leafs as lists of Path objects. The "plant" validation must occur beforehand, as it
			is in __call__ by the use of "unplantable" helper function.
			Consists of three phases:
				1.	Global sifting phase (or first step filter). This is the main folders/files filtering,
			that will affect every Tree object. For this phase there must be SiftingController objects
			to be reachable.
				2.	Local sifting phase (or Tree objects extra sifting). After global sifting, "innervate"
			will start it's primary job - starting from the "origin" argument, that must be the upper layer
			Copse or Tree object, "innervate" will find every Tree object in vicinity, iterating over upper
			layer Copse object and it's Copse objects respectively, in order to start "planting" it. This
			phase is transitional, means it allows the start of final third phase for every Tree object
			found, but before this will happen, "innervate" invokes SiftingController objects for every Tree
			object as extra filtering.
				3. Trees blooming (processing every reachable Tree object). Every Tree object, that yielded
			by "grove" helper method, will be iterated and every Bloom object assigned to its Tree will be
			invoked. This invocation relies on every Bloom object implements "bloom-interface":
				accepts:
					origin	- current Tree object to be processed;
					sprout	- current source root folder as a string;
					branch	- current source working directory as a Path object;
					twigs	- list of Path objects as current source folders;
					leafs	- list of Path objects as current source files.
				return:
					None.
		"""


		sprout, branch, branch_twigs, branch_leafs = plant
		branch_twigs_count = len(branch_twigs)
		branch_leafs_count = len(branch_leafs)


		self.loggy.debug(f"Current branch \"{branch}\"")
		self.loggy.debug(f"Number of twigs: {branch_twigs_count}")
		self.loggy.debug(f"Number of leafs: {branch_leafs_count}")




		# Twigs main sifting, or folders first step filter. This is the only place where
		# SiftingController invoked with two boolean flags toggled to True.
		# "thriving" turned on means after a branch failed to "fullmatch" the only includable,
		# there will be a check if the whole branch is a prefix of that includable. As this
		# technic is used only for twigs sifting, it allows to not sift out the branch that
		# would lead to included targets. The necessity to keep that twigs is related to
		# second toggled flag "popping", which means that sifting twigs happens literally.
		# When the twig is sifted out it is popped from the input list, so "plant" Generator
		# will refer to modified list of folders, where there'll be no folders, that are
		# either not included or excluded, so the walk will not occur, hence no Flourish
		# for that branches.
		if	callable((twigs_sift := getattr(self, "twigs", None))):
			current_twigs = twigs_sift(branch_twigs, thriving=True, popping=True)

			if	(twigified := len(current_twigs)) != branch_twigs_count:

				self.loggy.debug(f"Twigs after sifting: {twigified}")
		else:	current_twigs = branch_twigs


		# Leafs of current branch sifting that is general for every bough, so it must be clear
		# that include and exclude fields for this controller will affect every Tree Flourish.
		if	callable((leafs_sift := getattr(self, "leafs", None))):
			current_leafs = leafs_sift(branch_leafs)

			if	(leafified := len(current_leafs)) != branch_leafs_count:

				self.loggy.debug(f"Leafs after sifting: {leafified}")
		else:	current_leafs = branch_leafs




		for tree in self.grove(origin):
			if	isinstance(tree, Tree):


				# Twigs extra sifting of every Tree object.
				# This must be pointed, that twigs sifting for every Tree object, that is
				# to be escalated "SiftingController", is invoked with "thriving" flag on
				# and "popping" flag off. The first one means that it is, like in "Flourish"
				# twigs sifting, every walked branch will be checked to be a prefix for any
				# includable, which is the way to include final branch in pattern. The second
				# one means the list of twigs will not be altered (no pops) by sifting twigs.
				# Unlike the global "Flourish" twigs sifting, where "popping" is set on by
				# default to ensure sifting twigs from walking, local Tree sifting is actually
				# filter for twigs thriving (Germination). For purposes of filtering files
				# from certain folders, "leafs" sifting must be used.
				tree_twigs = tree.twigify(current_twigs)
				tree_leafs = tree.leafify(current_leafs)


				for bloom in tree:
					if	isinstance(bloom, Bloom):


						self.loggy.debug(f"Invoking {tree} tree {bloom} blooming")
						bloom(tree, sprout, branch, tree_twigs, tree_leafs)
					else:
						self.loggy.debug(f"Invalid Bloom \"{bloom}\" to flourish")


	def __call__(self, *plant :Tuple[str, Path, List[Path], List[Path]]):


		if	hasattr(self, "_UPPER_LAYER"):
			if	plant:

				if isinstance(reason := unplantable(*plant), str): self.loggy.warning(reason)
				else:

					self.loggy.debug(f"Flourishing {plant[0]}")
					self.innervate(self._UPPER_LAYER, *plant)
			else:	self.loggy.debug(f"No plants to flourish")
		else:		self.loggy.critical(f"{self} failed to start flourish")







