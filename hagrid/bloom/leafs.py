from pathlib					import Path
from typing						import List
from pygwarts.magical.spells	import patronus
from pygwarts.hagrid.bloom		import Bloom
from pygwarts.hagrid.thrivables	import Tree








class Rejuvenation(Bloom):

	"""
		Implementation of Bloom object that processes only files by "bloom-interface":
			accepts:
				origin	- current Tree object to be processed;
				sprout	- current source root folder as a string;
				branch	- current source working directory as a Path object;
				twigs	- list of Path objects as current source folders;
				leafs	- list of Path objects as current source files.
			return:
				None.
		The files processing (leafs planting) for current Bloom object __call__ relies on mandatory
		"grow" callable, which will be invoked for every single Path object file in "leafs" list,
		which declaration must be reachable for current Tree object "origin" by escalation and which
		must implement "planting interface" to accept following arguments:
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current "planting" source file;
			bough	- Path object that represents current "planting" destination parent folder.
		This Bloom object designed to be the dispatcher for file-copying operations, and name "Rejuvenation"
		based on this idea. The idea of separation of copying and moving operations is flexibility
		and security. One can use moving "planting" along with this object, but it must be noted, that
		the logging information that emitted by this object will reflect the process of file copying,
		as was originally designed.
		Any Exception raised by "grow" might not be handled by "grow", as originally designed, but
		will be handled by this Bloom object. In this case, after the Exception will be handled,
		the iteration over leafs list will be continued. The iteration will be stopped if either
		"origin" argument is not a Tree object, or "origin" is a Tree object but with invalid
		"bough" field, or the "grow" implementation either not callable or not found.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, twigs :List[Path], leafs :List[Path]):


		if	isinstance(leafs, list) and len(leafs):
			if	isinstance(origin, Tree) and isinstance((bough := getattr(origin, "bough", None)), Path):
				self.loggy.debug(f"Commencing rejuvenation of {len(leafs)} \"{str(bough)}\" leafs")


				# IMPORTANT: "grow" to be invoked from "origin" to ensure right escalation, as "planting"
				# invocation must be issued not from Bloom object but from Tree object to be processed.
				if	callable(grow := getattr(origin, "grow", None)):
					for leaf in leafs:


						try:

							# Actual "planting" invocation relies on callable "grow", that escalated from
							# the current Tree object, to implement "planting interface". The chain of calls,
							# that leads to this moment assumes all arguments are valid, cause the original
							# design of "planting" object doesn't involve arguments validation. That means
							# only "origin" validation at the beginning guards possible Exceptions, that might
							# be raised in "grow" because of arguments inconsistency, and which all won't be
							# handled by original "planting" design but will be caught back in current Bloom.
							grow(origin, sprout, branch, leaf, bough)
							self.mark_tree(str(origin), "grow")
							self.loggy.debug(f"Rejuvenated \"{leaf}\"")


						except	Exception as E:

							self.loggy.warning(f"Failed to rejuve leaf \"{leaf}\" due to {patronus(E)}")
				else:		self.announce_implement(str(origin), "grow")
			else:			self.announce_bough(str(origin), "rejuve")
		else:				self.loggy.debug(f"Branch \"{str(branch)}\" has no leafs to rejuve")








class Transfer(Bloom):

	"""
		Implementation of Bloom object that processes only files by "bloom-interface":
			accepts:
				origin	- current Tree object to be processed;
				sprout	- current source root folder as a string;
				branch	- current source working directory as a Path object;
				twigs	- list of Path objects as current source folders;
				leafs	- list of Path objects as current source files.
			return:
				None.
		The files processing (leafs planting) for current Bloom object __call__ relies on mandatory
		"graft" callable, which will be invoked for every single Path object file in "leafs" list,
		which declaration must be reachable for current Tree object "origin" by escalation and which
		must implement "planting interface" to accept following arguments:
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current "planting" source file;
			bough	- Path object that represents current "planting" destination parent folder.
		This Bloom object designed to be the dispatcher for file-moving operations, and name "Transfer"
		based on this idea. The idea of separation of copying and moving operations is flexibility
		and security. One can use copying "planting" along with this object, but it must be noted, that
		the logging information that emitted by this object will reflect the process of file moving,
		as was originally designed.
		Any Exception raised by "graft" might not be handled by "graft", as originally designed, but
		will be handled by this Bloom object. In this case, after the Exception will be handled,
		the iteration over leafs list will be continued. The iteration will be stopped if either
		"origin" argument is not a Tree object, or "origin" is a Tree object but with invalid
		"bough" field, or the "graft" implementation either not callable or not found.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :str, twigs :List[str], leafs :List[str]):


		if	isinstance(leafs, list) and len(leafs):
			if	isinstance(origin, Tree) and isinstance((bough := getattr(origin, "bough", None)), Path):
				self.loggy.debug(f"Commencing transfer of {len(leafs)} \"{bough}\" leafs")


				# IMPORTANT: "graft" to be invoked from "origin" to ensure right escalation, as "planting"
				# invocation must be issued not from Bloom object but from Tree object to be processed.
				if	callable(graft := getattr(origin, "graft", None)):
					for leaf in leafs:


						try:

							# Actual "planting" invocation relies on callable "graft", that escalated from
							# the current Tree object, to implement "planting interface". The chain of calls,
							# that leads to this moment assumes all arguments are valid, cause the original
							# design of "planting" object doesn't involve arguments validation. That means
							# only "origin" validation at the beginning guards possible Exceptions, that might
							# be raised in "graft" because of arguments inconsistency, and which all won't be
							# handled by original "planting" design but will be caught back in current Bloom.
							graft(origin, sprout, branch, leaf, bough)
							self.mark_tree(str(origin), "graft")
							self.loggy.debug(f"Transferred \"{leaf}\"")


						except	Exception as E:

							self.loggy.warning(f"Failed to transfer leaf \"{leaf}\" due to {patronus(E)}")
				else:		self.announce_implement(str(origin), "graft")
			else:			self.announce_bough(str(origin), "transfer")
		else:				self.loggy.debug(f"Branch \"{str(branch)}\" has no leafs to transfer")







