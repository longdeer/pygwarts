from os													import access	as osaccess
from os													import path		as ospath
from os													import R_OK
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.hagrid.walks								import fstree








class fssprout(ControlledTransmutation):

	"""
		hagrid core functionality decorator, that serves as a planting dispatching automation for a
		certain root folder.
		As ControlledTransmutation class, accepts single "sprout" argument, that must be only a string
		that represents source root folder absolute path. The "sprout" for hagrid is the only path, that
		always stays as a string, cause it's role is only a starter, so no Path object conversion needed and
		all "planting" organization relies on a "sprout" to be a string.
		In mutable chain acts as a mutation - takes decorated planting dispatching class and extends it by
		declaring meta __call__ to invoke decorated __call__. Meta __call__ will "walk" from that "sprout".
		That means by the use of "fstree" function will be created generator object, that will traverse the
		file system tree, and, starting from provided "sprout" folder and for every subfolder, that generator
		will yield a tuple of three objects:
			branch	- current folder walked;
			twigs	- list of Path objects, that represents all folders in current folder;
			leafs	- list of Path objects, that represents all files in current folder.
		This tuple preceded with current sprout considered as a "plant" for a decorated dispatcher.
		This decorator implemented the way it is possible to use multiple such decorators, decorating each
		other. The Meta __call__ for each decorator will consider *args and **kwargs from decorated __call__
		as possible "plants" and pass it to decorated __call__ right after itself generator exhaust. Even if
		its own "plant" failed, all arguments will be passed to decorated object. That allows scheduling
		valid sprouts, bypassing failed.
	"""

	def __init__(self, sprout :str): self.sprout = sprout
	def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

		sprout	= self.sprout
		reason	= None
		plan	= None


		if	isinstance(self.sprout, str):
			if	ospath.isdir(self.sprout):
				if	osaccess(self.sprout, R_OK): plan = fstree(sprout)


				else:	reason = f"Sprout \"{sprout}\" is inaccessible"
			else:		reason = f"Sprout \"{sprout}\" is not thrived"
		else:			reason = f"Sprout \"{sprout}\" is invalid"


		class SproutGenerator(geminio(mutable_layer)):
			def __call__(self, *args, **kwargs):


				if	plan is not None:
					for	plant in plan:


						if plant : super().__call__(sprout, *plant)
				elif	isinstance(reason, str): self.loggy.critical(reason)


				# After current generator will exhaust, right after this and at every consecutive call to
				# current sprout layer "args" will be considered as upper layer decorator plants and will
				# be delegated to decorated layer by __call__, along with any provided key-word flags.
				super().__call__(*args, **kwargs)
		return	SproutGenerator







