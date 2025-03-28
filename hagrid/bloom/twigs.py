from pathlib					import Path
from typing						import List
from pygwarts.magical.spells	import patronus
from pygwarts.hagrid.bloom		import Bloom
from pygwarts.hagrid.thrivables	import Tree








class Germination(Bloom):

	"""
		Implementation of Bloom object that processes only folders by "bloom-interface":
			accepts:
				origin	- current Tree object to be processed;
				sprout	- current source root folder as a string;
				branch	- current source working directory as a Path object;
				twigs	- list of Path objects as current source folders;
				leafs	- list of Path objects as current source files.
			return:
				None.
		The folders processing (twigs planting) for current Bloom object __call__ relies on mandatory
		"thrive" callable, which will be invoked for every single Path object folder in "twigs" list,
		which declaration must be reachable for current Tree object "origin" by escalation and which
		must implement "planting interface" to accept following arguments:
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current "planting" source folder;
			bough	- Path object that represents current "planting" destination parent folder.
		This Bloom object designed to be the dispatcher for folders creation operation and does not
		copy any folders with content. The idea that is base for "Germination" name and that laid in such
		folders creation is the replication of the fs tree structure. Any files operations must be handled
		by corresponding Bloom objects, which handles file "planting" operations.
		Any Exception raised by "thrive" might not be handled by "thrive", as originally designed, but
		will be handled by this Bloom object. In this case, after the Exception will be handled,
		the iteration over twigs list will be continued. The iteration will be stopped if either
		"origin" argument is not a Tree object, or "origin" is a Tree object but with invalid
		"bough" field, or the "thrive" implementation either not callable or not found.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, twigs :List[Path], leafs :List[Path]):


		if	isinstance(twigs, list) and len(twigs):
			if	isinstance(origin, Tree) and isinstance((bough := getattr(origin, "bough", None)), Path):
				self.loggy.debug(f"Commencing germination of {len(twigs)} \"{bough}\" twigs")


				# IMPORTANT: "thrive" to be invoked from "origin" to ensure right escalation, as "planting"
				# invocation must be issued not from Bloom object but from Tree object to be processed.
				if	callable(thrive := getattr(origin, "thrive", None)):
					for twig in twigs:


						try:

							# Actual "planting" invocation relies on callable "thrive", that escalated from
							# the current Tree object, to implement "planting interface". The chain of calls,
							# that leads to this moment assumes all arguments are valid, cause the original
							# design of "planting" object doesn't involve arguments validation. That means
							# only "origin" validation at the beginning guards possible Exceptions, that might
							# be raised in "thrive" because of arguments inconsistency, and which all won't be
							# handled by original "planting" design but will be caught back in current Bloom.
							thrive(origin, sprout, branch, twig, bough)
							self.mark_tree(str(origin), "thrive")
							self.loggy.debug(f"Germinated \"{twig}\"")


						except	Exception as E:

							self.loggy.warning(f"Failed to germinate twig \"{twig}\" due to {patronus(E)}")
				else:		self.announce_implement(str(origin), "thrive")
			else:			self.announce_bough(str(origin), "germinate")
		else:				self.loggy.debug(f"Branch \"{str(branch)}\" has no twigs to germinate")







