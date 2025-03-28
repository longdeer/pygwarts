from os													import sep
from pathlib											import Path
from typing												import Tuple
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import Transmutation
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.hagrid.thrivables							import Tree








class GrowingPeel(Transmutation):

	"""
		hagrid.planting utility decorator class, that helps in obtaining corresponding destination "sprigs"
		(folders/files) as Path objects. As Transmutation class, in mutable chain takes decorated "planting"
		class and extends it by declaring meta __call__ to invoke decorated __call__. Meta __call__ designed
		to, and decorated __call__ must, accept arguments according to "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current operation source folder;
			bough	- Path object that represents current operation destination parent folder.
		Meta __call__ will take current source "sprig", which must be Path object "branch", obtain relative
		to it's source root subpath and concatenate it to destination root "bough". This final concatenation
		will represent corresponding destination "sprig".
		Every logging will refer to the "origin" Tree object.
	"""

	def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :
		class Peel(geminio(mutable_layer)):


			def __call__(self, origin :Tree, sprout :str, branch :Path, sprig :Path, bough :Path):


				if	isinstance(branch, Path):
					if	isinstance(bough, Path):


						grown_bough = bough.joinpath(branch.relative_to(sprout))
						origin.loggy.debug(f"Peeled growing bough \"{grown_bough}\"")
						super().__call__(origin, sprout, branch, sprig, grown_bough)
					else:
						self.loggy.debug(f"Bough \"{bough}\" is not a Path object")
				else:	self.loggy.debug(f"Branch \"{branch}\" is not a Path object")
		return	Peel








class ThrivingPeel(ControlledTransmutation):

	"""
		hagrid.planting utility decorator class, that helps in obtaining corresponding destination "sprigs"
		(folders/files) as Path objects. As ControlledTransmutation class, accepts all positional arguments
		as "thrivings", which must be strings that represent intermediate folders to be integrated in final
		destination "sprig" path. Also accepts boolean flag "to_peak" which regulates whether collected
		"thrivings" must be added to the very end of destination "sprig" path or in the middle (defaulted
		to True - to the top). In mutable chain acts as a mutation - takes decorated "planting" class and
		extends it by declaring meta __call__ to invoke decorated __call__. Meta __call__ designed to, and
		decorated __call__ must, accept arguments according to "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current operation source folder;
			bough	- Path object that represents current operation destination parent folder.
		Meta __call__ will take current source "sprig", which must be Path object "branch", obtain relative
		to it's source root subpath, merge it with "thrivings" subfolders and concatenate it to destination
		root "bough". This final concatenation will represent corresponding destination "sprig".
		Every logging will refer to the "origin" Tree object.
		ThrivingPeel with "to_peak" set to True has some sort of side effect when used with "Germination",
		which causes every folder to be created with preceeding "thrivings". For files this behaviour is
		desired, but for folders this is might be an unpredictable source of bags in execution scripts.
		As "Germination" designed for full replication of source tree, it is not recommended to decorate
		it with ThrivingPeel.
	"""

	def __init__(self, *thrivings :Tuple[str,], to_peak=True):


		self.to_peak = to_peak
		self.thrivings = list()


		# The only condition to comply for thriving target directory, is that such "thriving"
		# argument is a string. To avoid something like PermissionError when "thriving" provided
		# with leading fs-separation symbol, it's stripped out.
		for thriving in thrivings:

			assert isinstance(thriving, str), f"Thriving must be with strings, not \"{type(thriving)}\""
			self.thrivings.append(thriving.lstrip(sep))


	def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :


		thrivings	= self.thrivings
		to_peak		= self.to_peak


		class Peel(geminio(mutable_layer)):
			def __call__(self, origin :Tree, sprout :str, branch :str, sprig :str, bough :str):


				if	isinstance(branch, Path):
					if	isinstance(bough, Path):
						if	to_peak:


							thrived_bough = bough.joinpath(branch.relative_to(sprout), *thrivings)
						else:
							thrived_bough = bough.joinpath(*thrivings, branch.relative_to(sprout))


						origin.loggy.debug(f"Peeled thriving bough \"{thrived_bough}\"")
						super().__call__(origin, sprout, branch, sprig, thrived_bough)
					else:
						self.loggy.debug(f"Bough \"{bough}\" is not a Path object")
				else:	self.loggy.debug(f"Branch \"{branch}\" is not a Path object")
		return	Peel







