from os										import access	as osaccess
from os										import W_OK
from pathlib								import Path
from typing									import List
from typing									import Optional
from pygwarts.magical.chests				import Chest
from pygwarts.magical.spells				import patronus
from pygwarts.hagrid.cultivation.sifting	import SiftingController








class Tree(Chest):

	"""
		hagrid core class, that represents destination object. Appear to be an object that is a target for
		every "planting" (processing), that hagrid handles, so every Tree object must correspond to only
		one single folder. Must have one mandatory and three optional fields:
			bough			- destination root directory;
			twigs			- optional SiftingController object for folders filtering;
			leafs			- optional SiftingController object for files filtering;
			strict_thrive	- boolean flag that decides whether or not creating of bough is allowed in case
							bough is non existent directory. If set to True, there will be attempt to create
							bough directory, including all parents. If such attempt will fail or flag is set
							to False and bough directory does not exist, tree will be discarded (means Tree
							object, as Chest object, will invoke "unload" method to become empty Chest, so
							any Bloom object that must be assigned to it's Tree object for "planting" will
							be discarded and won't "plant" current Tree object, cause it's "boughless").
		Mandatory "bough" field might be either a string, that represents destination root folder absolute
		path, or corresponding Path object. In first case string will be converted to a Path object, anyway,
		cause all "planting" relies on every Tree object will have it's "bough" as a Path object.
		Tree class is a child of a Chest class, so actually Tree object will be a container. As Tree object
		is a target of any "planting" processes, the original design assumes Tree object will content Bloom
		objects, that organizes "planting". Bloom objects implemented the way they will reach every Tree
		object they can and put itself into it, so that Tree object will be "planted" by that Bloom objects.
		Tree object might also be encapsulated in Copse object, which is like a Chest for a Tree objects. In
		initiation time Tree object will check if it's upper layer is a Copse object to put itself in it.
		Any exception during Tree initiation will lead to discarding.
	"""

	bough			:str | Path
	twigs			:Optional[SiftingController]
	leafs			:Optional[SiftingController]
	strict_thrive	:Optional[bool]


	def twigify(self, twigs :List[Path]) -> List[Path] :

		"""
			Utility method that serves as a current Tree object personal SiftingController invoker
			for "twigs" sifting (folders filtering).
			Accepts list of Path objects, that represents folders to be sifted (filtered).
			This method will search for escalatable for current Tree object SiftingController named
			"twigs" to invoke it with provided argument "twigs" to execute sifting. That "controller"
			must return list of Path objects, that will represent sifting result, so it will be the
			value to return by "twigify". If "controller" is not found, original "twigs" list returned.
		"""

		if	callable((twigs_sift := getattr(self, "twigs", None))):
			tree_twigs = twigs_sift(twigs, thriving=True)


			if	(twigifies := len(tree_twigs) != len(twigs)):
				self.loggy.debug(f"Number of twigifies: {len(tree_twigs)}")


			return	tree_twigs
		return		twigs




	def leafify(self, leafs :List[Path]) -> List[Path] :

		"""
			Utility method that serves as a current Tree object personal SiftingController invoker
			for "leafs" sifting (files filtering).
			Accepts list of Path objects, that represents files to be sifted (filtered).
			This method will search for escalatable for current Tree object SiftingController named
			"leafs" to invoke it with provided argument "leafs" to execute sifting. That "controller"
			must return list of Path objects, that will represent sifting result, so it will be the
			value to return by "leafify". If "controller" is not found, original "leafs" list returned.
		"""

		if	callable((leafs_sift := getattr(self, "leafs", None))):
			tree_leafs = leafs_sift(leafs)


			if	(leafifies := len(tree_leafs) != len(leafs)):
				self.loggy.debug(f"Number of leafifies: {len(tree_leafs)}")


			return	tree_leafs
		return		leafs




	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		try:


			if	isinstance(self.bough, str): self.bough = Path(self.bough)

			if	not isinstance(self.bough, Path) or (
				not self.bough.is_dir() and getattr(self, "strict_thrive", True)
			):	self.loggy.info(f"Bough \"{self.bough}\" is invalid")


			else:


				# At this point "bough" is a Path object anyway, or this point will be skipped and tree
				# discarded its blooms. If "bough" was a Path object which points to not existent directory,
				# "strict_thrive" not assigned or set to True causes discard too, but at this point both
				# or any of that conditions was not met. Whether "bough" path will be created by non
				# restrictive "strict_thrive", or it is already existent directory, it must be a writable
				# directory for "planting" to happen, otherwise Exception will discard tree's blooms.
				# Discarded blooms will not "plant" current tree.
				self.bough.mkdir(parents=True, exist_ok=True)
				assert osaccess(self.bough, W_OK), f"Bough \"{self.bough}\" thrive restricted"


				if	hasattr(self, "_UPPER_LAYER"):
					if	isinstance(self._UPPER_LAYER, Copse):


						self._UPPER_LAYER(self)
						self.loggy.debug(f"Thriving tree in {self._UPPER_LAYER} Copse")
					else:
						self.loggy.debug("Not thrivable upper layer")
				else:	self.loggy.debug("Thriving single tree")


				return
		except	Exception as E:	self.loggy.error(f"Tree {self} can't thrive due to {patronus(E)}")


		self.unload()
		self.loggy.debug("Discarded")








class Copse(Chest):

	"""
		hagrid core utility class, that allows Tree (destination) objects encapsulation.
		As this object is Chest child, it is a container for Tree objects. Every Tree objects, declared
		right under Copse object, will detect it and put itself in it's upper layer Copse object.
		The Copse object itself might be encapsulated in another Copse object, so in initiation time
		current object will check if it's upper layer also a Copse object, to put itself in it.
		Doesn't have mandatory fields, but shares optional fields with Tree class:
			twigs			- optional SiftingController object for folders filtering;
			leafs			- optional SiftingController object for files filtering;
			strict_thrive	- boolean flag that decides whether or not creating of bough is allowed in case
							bough is non existent directory for any Tree object encapsulated. If set to True,
							there will be attemp to create bough directory, including all parents, for every
							Tree object. If such attempt will fail or flag is set to False and bough directory
							does not exist, tree will be discarded (means Tree object, as Chest object, will
							invoke "unload" method to become empty Chest, so any Bloom object that must be
							assigned to it's Tree object for "planting" will be discarded and won't "plant"
							current Tree object, cause it's "boughless").
		The idea behind such encapsulations has to sides:
			Association	- once optional "twigs" or/and "leafs" controllers declared for Copse object, every
						Tree object encapsulated will have access to that controllers. Also Bloom objects,
						declared for Copse objects (declaration must take place right after all Tree objects,
						cause of mutable chain order; every Tree initiation includes Copse encapsulation, so
						it's must go before any Bloom object will iterate over Copse to find Trees) will also
						affect Tree objects encapsulated. So if some Tree objects have something mutual, Copse
						is the way to go.
			Isolation	- The opposite way is to isolate some objects from another. It can be used in anyway.
						The main example for such behavior is separating *"global" and "local" sifting. First
						one implies filtering for every Tree to be "planted", while "local" is an auxiliary
						option. In their difference lies the necessity of isolated declaration - "global" must
						have it's very own "controllers", which are reachable only for *object that implements
						"global" sifting; "local" might be declared anywhere except *"global" object, with
						only restriction that it must be reachable for the Tree objects it is belong to. As
						the default behavior of *"global" object and Tree objects include the phase of
						automatic sifting invocation, Tree objects might be encapsulated to Copse object to
						provide common "controllers", and also to isolate some Tree objects form another
						and from *"global" object, that Copse might be encapsulated in any more Copse objects.
						Last idea will allow isolate "controllers" of Tree objects from *"global" object when
						the last one doesn't have it's own, and they will be search by escalation. Anyway,
						the situation when *"global" object and Tree object share "controllers" is not
						dangerous, and, when fields are well organized, might only lead to redundant sifting
						for already sifted items.

		*	- refer to hagrid.planting.Flourish
	"""

	twigs			:Optional[SiftingController]
	leafs			:Optional[SiftingController]
	strict_thrive	:Optional[bool]


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		if	hasattr(self, "_UPPER_LAYER"):
			if	isinstance(self._UPPER_LAYER, Copse):


				self.loggy.debug(f"Soiling inner copse in {self._UPPER_LAYER} Copse")
				self._UPPER_LAYER(self)
			else:
				self.loggy.debug("Not thrivable upper layer")
		else:	self.loggy.debug("Outer Copse soiled")







