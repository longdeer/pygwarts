from pathlib								import Path
from typing									import List
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse








class Bloom(Transmutable):

	"""
		hagrid core functionality super class, that serves as a Tree object (target) dispatcher.
		Must be declared under the Tree or Copse object (literally for Copse object, means declaration of
		Tree objects must precede Bloom objects). In initiation time the "innervate" method will search the
		"_UPPER_LAYER" field and check it's type. If Bloom object was not declared under the correct object,
		it will discard it self and will not participate in Tree processing. Once attached to the right
		object, the "innervate" method will scan all reachable Copses and their Trees to include itself in
		every Tree, that means every affected Tree object will be processed by current Bloom object.
		The Tree object processing refers to child class __call__ implementation, that when invoked
		must dispose source folders and files to be processed against the target folder. During every
		Bloom object call corresponding arguments (lists of folders or/and files or/and source folder
		or/and target folder) must be processed by Bloom object __call__ itself, or, how it is originally
		designed, by special callable, and in both situations this whole operation is called "planting".
		Any "planting" that will occur inside Bloom object invocation must affect only single Tree object
		that it currently processing, and only corresponding source location. In order to do that,
		__call__ must implement special "bloom-interface":
			accepts:
				origin	- current Tree object to be processed;
				sprout	- current source root folder as a string;
				branch	- current source working directory as a Path object;
				twigs	- list of Path objects as current source folders;
				leafs	- list of Path objects as current source files.
			return:
				None.
	"""

	__call__	:Callable[[Tree, str, Path, List[Path], List[Path]], None]


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		self.blooming = dict()
		self.spread_count = int()


		if	hasattr(self, "_UPPER_LAYER"):


			self.innervate(self._UPPER_LAYER)
			self.loggy.debug(f"Spreading complete, number of affected trees: {self.spread_count}")
		else:
			self.loggy.warning(f"No starting point for {self} spreading")




	def innervate(self, origin :Copse | Tree):

		"""
			The method that when called in initiation time to recursively traverse through all reachable
			Copse objects, starting from the upper layer object current Bloom object attached to, to find
			all reachable Tree object and include itself in it. As every Tree object that met during
			"innervate" traverse must be Chest object child, to be included in the Tree object means
			that Chest object simply will be called with current Bloom object as argument and putted
			in the Chest. This process called "tree affection" and maintains counter "spread_count"
			that reflects the number of Tree object that was "affected" during innervate. The further
			Tree objects processing fully relies on this logic, that affected Tree objects contain
			in it's "chests" Bloom objects, that will do the thing. The Copse object that gets in the way
			of "innervate" is the point for recursive call to find Tree object it must contain.
		"""

		match origin:

			case Copse():
				for inner in origin:

					self.loggy.debug(f"Affecting copse {origin} inner {inner}")
					self.innervate(inner)


			case Tree():

				origin(self)
				self.spread_count += 1
				self.loggy.debug(f"{origin} tree affected")
			case _:
				self.loggy.warning(f"Invalid spread point \"{origin}\" for {self}")




	def mark_tree(self, tree_name :str, planter :str):

		"""
			Helper method that allows tracking the "planting state" and "bough validation" of every
			Tree object being processed by current Bloom object, by maintaining special dictionary
			"blooming". At first time for any Tree object successfully processed, which means
			successful "planting", that Tree object will be mapped in "blooming" with nested
			dictionary, that includes key-value pairs that serves as the marks of validated "planter"
			(working "planting" invocation) and validated "bough" (target root folder) for current
			Tree object being processed. In other words current helper method must be invoked only
			in case of success and will serves as a proof and as a guide for further "planting".
			For example when Bloom object tries to "plant" some "sprigs" (folders/files) with
			broken "planting" or invalid "bough", the original design for Bloom __call__
			implementation will announce only the first occurrence of such situation to be logged
			as warning message, logging any further occurrences as debug message, in order not
			to flood the log with the same problem. This announce restriction is done by altering
			the "blooming" dictionary after the first time the trouble is met, marking "planter"
			or/and "bough" keys with corresponding values. If such troubles will gone and after
			the very first successful "planting" that goes next, those "planter" and "bough" marks
			will be again set to be validated for current Tree object.
		"""

		if	self.blooming.get(tree_name) is None :		self.blooming[tree_name] = dict()
		if	not self.blooming[tree_name].get(planter):	self.blooming[tree_name][planter] = True
		if	not self.blooming[tree_name].get("bough"):	self.blooming[tree_name]["bough"] = True




	def announce_implement(self, tree_name :str, planter :str):

		"""
			Helper method that implements current Bloom object "planting" validation, by maintaining
			the "planter" key-value pair in "blooming" nested for current Tree object dictionary.
		"""

		if		self.blooming.get(tree_name) is None : self.blooming[tree_name] = dict()
		state = self.blooming[tree_name].get(planter)


		if		state or state is None:	level,self.blooming[tree_name][planter] = 40,False
		else:	level = 10


		self.loggy.log(level, f"{tree_name} doesn't implement {planter}")




	def announce_bough(self, tree_name :str, blooming :str):

		"""
			Helper method that implements current Tree object "bough" validation, by maintaining
			the "bough" key-value pair in "blooming" nested for current Tree object dictionary.
		"""

		if		self.blooming.get(tree_name) is None : self.blooming[tree_name] = dict()
		state = self.blooming[tree_name].get("bough")


		if		state or state is None:	level,self.blooming[tree_name]["bough"] = 40,False
		else:	level = 10


		self.loggy.log(level, f"Invalid tree {tree_name} or no bough to {blooming}")







