from pathlib											import Path
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.hagrid.thrivables							import Tree
from pygwarts.irma.shelve								import LibraryShelf








class DraftPeek(ControlledTransmutation):

	"""
		hagrid.planting utility decorator class, that serves as "planting regulator". Allows Integration
		of "sprigs" (folders/files) modification time check in to "planting" process, so "planting" invocation
		might rely on their comparison. As ControlledTransmutation class, accepts following arguments when
		initiated as a "planting" object decorator:
			renew		- by default only sprigs with old rings will be handled (that means "renew" flag
						if True restricts planting of source "sprig" if corresponding destination "sprig"
						doesn't exist);
			picky		- use floats representation of rings for pickiness (precision) or cast them to int
						(this solves situations, when cloning sprig mtime impossible and copied sprig will
						have slightly different mtime every time, so casting mtime to int must mitigate that
						effect). Defaulted to False (casting to int).
			cache		- allows (by default) caching mtimes of branches that currently walked to reuse it in
						multi-target situations for breadth-first "Flourish" algorithm.
			comparator	- callable that takes new_ring and old_ring as arguments in that only order and return
						boolean to make a decision of handing further.
		In mutable chain acts as a mutation - takes decorated "planting" class and extends it by declaring
		meta __call__ to invoke decorated __call__. Meta __call__ will consider source "sprig" modification
		time, which might be checked directly or from cache, and compare by "comparator" callable with
		corresponding destination "sprig" modification time, which always will be taken directly, or
		defaulted to zero if corresponding destination "sprig" doesn't exist. By "comparator" callable return
		value, decorated __call__ invocation will be considered. Meta __call__ designed to, and decorated
		__call__ must, accept arguments according to "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current operation source folder;
			bough	- Path object that represents current operation destination parent folder.
		Every logging will refer to the "origin" Tree object.
	"""

	def __init__(
					self,
					*,
					renew		:bool										=True,
					picky		:bool										=False,
					cache		:bool										=True,
					comparator	:Callable[[ int|float, int|float ], bool]	=None,
				):


		self.renew	= renew
		self.picky	= picky
		self.cache	= cache


		if	comparator is None : self.comparator = lambda N,O : O <N
		else:
			try:

				if	callable(comparator) and isinstance(comparator(.2,.1), bool):

					self.comparator = comparator
					return
			except:	pass
			raise	TypeError("Draft peek comparator must be Callable[[ int|float, int|float ], bool]")


	def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :


		comparator	= self.comparator
		renew		= self.renew
		picky		= self.picky
		cache		= self.cache


		# Temporary location (buffer) for a current branch that is walked, to store all it's peeks,
		# that might be useful for other Trees, cause every Tree's Bloom make a peek for a single sprig
		# every time. If somehow the new ring for some sprig will be altered during all Tree's processing
		# sprigs, it will not affect current runtime cause mtime will be cached. Basically it will not affect
		# current runtime anyway. The idea is that the very first mtime check is based and all further
		# dispatching goes along such obtain.
		walk = dict()


		class Peek(geminio(mutable_layer)):
			def __call__(self, origin :Tree, sprout :str, branch :Path, sprig :Path, bough :Path):


				if	isinstance(sprig, Path) and sprig.is_file() and not sprig.is_symlink():
					old_peek = bough.joinpath(sprig.name)


					if	cache:
						if	(current_branch := walk.get(branch)) is not None:
							if	isinstance(current_branch, dict):
								if	(cached_peek := current_branch.get(str(sprig))) is not None:
									new_ring = cached_peek
					try:

						# As "new_ring" might be taken from cache in not "picky" condition (as int)
						# the following attempt only works in opposite case, when picky cached
						# it turning to integer.
						new_ring = new_ring if picky else int(new_ring)
						origin.loggy.debug(f"Cached draft peek \"{sprig}\" new ring: {new_ring}")


					except	NameError:

						# Modification time is known to be allowed to be peeked for any file in fs,
						# no matter owning and permission bits. However, in case item to peek suddenly
						# disappears or something, wrapping operation in try-except sounds very reasonable.
						# But, such wrapping does nothing with situation, cause no peek means no handing
						# further, hence there is nothing such wrapping can do about it, except raising
						# another Exception. So, it assumed if so incredible situation will occur,
						# some dispatcher will catch it and log.
						new_ring = sprig.stat().st_mtime if picky else int(sprig.stat().st_mtime)
						origin.loggy.debug(f"New draft peek \"{sprig}\" new ring: {new_ring}")


					if	cache:


						try:	walk[branch][str(sprig)] = new_ring
						except	KeyError:

							# New branch is walked so clearing "walk" buffer to save memory
							walk.clear()
							walk[branch] = { str(sprig): new_ring }




					try:	old_ring = old_peek.stat().st_mtime
					except	FileNotFoundError:


						if	not renew:

							old_ring = 0.
						else:
							origin.loggy.debug("Flourish stopped cause draft peek only for sprigs renew")
							return


					old_ring = old_ring if picky else int(old_ring)
					origin.loggy.debug(f"Draft peek for \"{old_peek}\" old ring: {old_ring}")


					if	comparator(new_ring, old_ring):

						super().__call__(origin, sprout, branch, sprig, bough)
					else:
						origin.loggy.debug("Flourish stopped by draft peek comparator")
				else:	origin.loggy.debug(f"Not located draft peek \"{sprig}\"")
		return	Peek








class BlindPeek(ControlledTransmutation):

	"""
		hagrid.planting utility decorator class, that serves as "planting regulator". Allows Integration
		of "sprigs" (folders/files) modification time check in to "planting" process, so "planting" invocation
		might rely on their comparison. As ControlledTransmutation class, accepts following arguments wneh
		initiated as a "planting" object decorator:
			link		- the string to find escalatable LibraryShelf object;
			renew		- by default only sprigs with old rings will be handled (that means "renew" flag
						if True restricts planting of source "sprig" if corresponding destination "sprig"
						doesn't exist);
			picky		- use floats representation of rings for pickiness (precision) or cast them to int
						(this solves situations, when cloning sprig mtime impossible and copied sprig will
						have slightly different mtime every time, so casting mtime to int must mitigate that
						effect). Defaulted to False (casting to int).
			cache		- allows (by default) caching mtimes of branches that currently walked to reuse it in
						multi-target situations for breadth-first "Flourish" algorithm.
			comparator	- callable that takes new_ring and old_ring as arguments in that only order and return
						boolean to make a decision of handing furhter.
		In mutable chain acts as a mutation - takes decorated "planting" class and extends it by declaring
		meta __call__ to invoke decorated __call__. Meta __call__ will consider source "sprig" modification
		time, which might be checked directly or from cache, and compare by "comparator" callable with
		corresponding destination "sprig" modification time, which always will be taken either from
		LibraryShelf object, refered by "link" argument, or defaulted to zero if corresponding destination
		"sprig" doesn't exist, but never directly from corresponding destination "sprig". Attention must be
		payed, that BlindPeek acts really "blind". The name infered from the logic, that "peek" occurs from
		LibraryShelf storage only, despite whether destination "sprig" exists. That might create some bad flow
		when BlindPeek used in the situations, where it is not supposed to. If source "sprig" peek and
		destination record peek comparison is not satisfied, which means that destination record does exist
		in Shelf, but destination "sprig" actually doesn't exist, decorated __call__ will not be invoked by
		comparator. The nearly same situation might occur with cached peeks for source. Situations described
		are not only edge cases but the logic behind the "BlindPeek" algorithm, as it means blind to
		destination "sprigs", operating only with Shelf records. By "comparator" callable return value,
		decorated __call__ invocation will be considered. Meta __call__ designed to, and decorated __call__
		must, accept arguments according to "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current operation source folder;
			bough	- Path object that represents current operation destination parent folder.
		Every logging will refer to the "origin" Tree object.
	"""

	def __init__(
					self,
					link		:str,
					*,
					renew		:bool										=True,
					picky		:bool										=False,
					cache		:bool										=True,
					comparator	:Callable[[ int|float, int|float ], bool]	=None,
				):


		self.link	= link
		self.renew	= renew
		self.picky	= picky
		self.cache	= cache


		if	comparator is None : self.comparator = lambda N,O : O <N
		else:

			try:

				if	callable(comparator) and isinstance(comparator(.2,.1), bool):

					self.comparator = comparator
					return
			except:	pass
			raise	TypeError("Blind peek comparator must be Callable[[ int|float, int|float ], bool]")


	def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :


		comparator	= self.comparator
		link		= self.link
		renew		= self.renew
		picky		= self.picky
		cache		= self.cache


		# Temporary location (buffer) for a current branch that is walked, to store all it's peeks,
		# that might be useful for other Trees, cause every Tree's Bloom make a peek for a single sprig
		# every time. If somehow the new ring for some sprig will be altered during all Tree's processing
		# sprigs, it will not affect current runtime cause mtime will be cached. Basically it will not affect
		# current runtime anyway. The idea is that the very first mtime check is based and all further
		# dispatching goes along such obtain.
		walk = dict()


		class Peek(geminio(mutable_layer)):
			def __call__(self, origin :Tree, sprout :str, branch :Path, sprig :Path, bough :Path):


				if	isinstance(sprig, Path) and sprig.is_file() and not sprig.is_symlink():
					new_peekable = True


					if	cache:
						if	(current_branch := walk.get(branch)) is not None:
							if	isinstance(current_branch, dict):
								if	(cached_peek := current_branch.get(str(sprig))) is not None:
									new_ring, new_peekable = cached_peek, False
					try:

						new_ring = new_ring if picky else int(new_ring)
						origin.loggy.debug(f"Cached blind peek \"{sprig}\" new ring: {new_ring}")


					except	NameError:

						# Modification time is known to be allowed to be peeked for any file in fs,
						# no matter owning and permission bits. However, in case item to peek suddenly
						# disappears or something, wrapping operation in try-except sounds very reasonable.
						# But, such wrapping does nothing with situation, cause no peek means no handing
						# further, hence there is nothing such wrapping can do about it, except raising
						# another Exception. So, it assumed if so incredible situation will occur,
						# some dispatcher will catch it and log.
						new_ring = sprig.stat().st_mtime if picky else int(sprig.stat().st_mtime)
						origin.loggy.debug(f"New blind peek \"{sprig}\" new ring: {new_ring}")


					if	cache:
						try:	walk[branch][str(sprig)] = new_ring
						except	KeyError:

							# New branch is walked co clearing "walk" buffer to save memory
							walk.clear()
							walk[branch] = { str(sprig): new_ring }




					if	isinstance((seeds := getattr(self, link, None)), LibraryShelf):


						if		(old_ring := seeds[str(sprig)]) is not None: pass
						elif	(not renew): old_ring = 0.
						else:
							origin.loggy.debug("Flourish stopped cause blind peek only for sprigs renew")
							return


						old_ring = old_ring if picky else int(old_ring)
						origin.loggy.debug(f"Blind peek for \"{sprig}\" old ring: {old_ring}")


						if	comparator(new_ring, old_ring):


							# Already cached peeks are stored in temporary dictionary. That allows
							# the flag "new_peekable" to regulate seeding (shelving) by the way it is
							# trigger the "modified" flag or not. That means if current leaf is peeked
							# the very-very first time, it will be seeded. The comparator decides the
							# way it will be seeded, like the negative comparator result leads to
							# silent seeding, because there is no need to reshelve already shelved
							# values. This relies on LibraryShelf logic, when it is called it uses
							# the "magical_shelf" to store key-pairs, and silent mode do the same,
							# but doesn't modify "modified" flag. So if it appears to "modified"
							# flag becomes True on the way, all previous values already in "magical_shelf".
							if	new_peekable : seeds(str(sprig), new_ring)
							super().__call__(origin, sprout, branch, sprig, bough)
						else:
							if	new_peekable : seeds(str(sprig), new_ring, silent=True)
							origin.loggy.debug("Flourish stopped by blind peek comparator")
					else:	origin.loggy.debug("Flourish failed to find \"seeds\" for blind peek")
				else:		origin.loggy.debug(f"Not located blind peek \"{sprig}\"")
		return	Peek







