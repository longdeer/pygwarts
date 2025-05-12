from __future__								import annotations
from shelve									import open		as shopen
from os										import access	as osaccess
from os										import path		as ospath
from os										import R_OK
from os										import makedirs
from typing									import Hashable
from typing									import Any
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.chests				import KeyChest
from pygwarts.magical.spells				import patronus
from pygwarts.magical.spells				import flagrate








class LibraryShelf(Transmutable):

	"""
		irma core class, that represents the wrapper over standard library "shelve" functionality, that
		integrated in mutable chain. Such integration allows not only maintain the shelf object as
		dictionary, with ability to store and load it as files, but also maintain another one, auxiliary
		shelf object as dictionary. Those shelf are:
			"real_shelf"	- the "main" dictionary for LibraryShelf object, which means it is the
							LibraryShelf object. Every method or property (except __call__) operates
							with "real_shelf". When "grab" method works it populates exactly "real_shelf".
			"magical_shelf"	- the shelf which serves as some sort of buffer for "real_shelf". Operations
							via __setitem__ and __delitem__ works for both shelf, setting and deleting
							mapping in both "real_shelf" and "magical_shelf", correspondingly. The only
							method __call__ works only for "magical_shelf" and serves as a way to operate
							with it the way it is possible to operate with "real_shelf" with LibraryShelf
							members.
		As both "real_shelf" and "magical_shelf" are KeyChest objects, all operations on them might be
		considered identical. The main idea of maintaining "magical_shelf" is that when "real_shelf"
		being populated, the further operations might all be reflected in "magical_shelf", so it will
		be the newer version of "real_shelf". It is recommended to use only defined members to operate
		with LibraryShelf object, and not direct access to "real_shelf" and "magical_shelf", cause
		LibraryShelf object changes are tracked by "modified" field, which reacts to the events that are
		actually modifies LibraryShelf object. Direct access to "real_shelf" will not alter the "modified"
		state properly, so "produce" method might not work and shelf will not be produced as file.
		Main helper methods to maintain input and output shelf files:
			grab	- opens shelf file as a dictionary and puts it's key-value pairs to the "real_shelf".
			produce	- opens shelf file as a dictionary and puts "real_shelf" or "magical_shelf" key-value
					pairs to that file, so it will be saved as a file.
		Fields that helps maintain input and output shelf files.
			grabbing	- input file absolute path to extract shelf from
			producing	- output file absolute path to save current shelf dictionary
			reclaiming	- boolean flag that indicates whether or not use input file absolute path
						("grabbing") as path for output file. If "producing" provided too, it will
						be ignored.
	"""


	grabbing	:str	=None
	producing	:str	=None
	reclaiming	:bool	=False


	class real_shelf(KeyChest):		pass
	class magical_shelf(KeyChest):	pass


	def __hash__(self) -> int:	return id(self)
	def __len__(self) -> int :	return len(self.real_shelf)
	def __contains__(self, K :Hashable)	-> bool			: return K in self.real_shelf
	def __getitem__(self, K :Hashable)	-> Any | None	: return self.real_shelf[K]
	def __setitem__(self, K :Hashable, V :Any):

		"""
			Assigning for both "real_shelf" and "magical_shelf".
			The "modified" flag will be set to True if all following conditions are met:
				- either key was not present in "real_shelf" or mapped value is different;
				- key-value successfully mapped for "real_shelf";
				- key-value successfully mapped for "magical_shelf";
		"""

		presence	= K in self.real_shelf
		valueness	= self.real_shelf[K] == V


		real = self.real_shelf(K,V)
		magical = self.magical_shelf(K,V)


		if(
			(not presence or not valueness)
			and real is not None
			and magical is not None
		):	self.modified = True




	def __delitem__(self, K :Hashable):

		""" Delete for both "real_shelf" and "magical_shelf". """

		current = len(self.real_shelf)


		del self.real_shelf[K]
		del self.magical_shelf[K]
		if	len(self.real_shelf) <current : self.modified = True




	def __eq__(self, other :LibraryShelf | KeyChest | dict) -> bool :

		"""
			Comparison of equality of current Shelf "real_shelf" with other Shelf "real_shelf",
			or another KeyChest or just a dict object.
		"""

		match other:

			case LibraryShelf()		: return 	self.real_shelf == other.real_shelf
			case KeyChest() | dict(): return 	self.real_shelf == other
			case _					: return 	False




	def __gt__(self, other :LibraryShelf | KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of greatness of current Shelf "real_shelf" with other Shelf "real_shelf",
			or another KeyChest or just a dict object.
		"""

		match other:

			case LibraryShelf()		: return	len(self.real_shelf) > len(other.real_shelf)
			case KeyChest() | dict(): return	len(self.real_shelf) > len(other)
			case _					: raise		TypeError(f"Object \"{other}\" cannot be compared with {self}")




	def __ge__(self, other :LibraryShelf | KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of greatness or equality of current Shelf "real_shelf" with other Shelf "real_shelf",
			or another KeyChest or just a dict object.
		"""

		match other:

			case LibraryShelf()		: return	len(self.real_shelf) >= len(other.real_shelf)
			case KeyChest() | dict(): return	len(self.real_shelf) >= len(other)
			case _					: raise		TypeError(f"Object \"{other}\" cannot be compared with {self}")




	def __lt__(self, other :LibraryShelf | KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of lesserness of current Shelf "real_shelf" with other Shelf "real_shelf",
			or another KeyChest or just a dict object.
		"""

		match other:

			case LibraryShelf()		: return	len(self.real_shelf) < len(other.real_shelf)
			case KeyChest() | dict(): return	len(self.real_shelf) < len(other)
			case _					: raise		TypeError(f"Object \"{other}\" cannot be compared with {self}")




	def __le__(self, other :LibraryShelf | KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of lesserness or equality of current Shelf "real_shelf" with other Shelf "real_shelf",
			or another KeyChest or just a dict object.
		"""

		match other:

			case LibraryShelf()		: return	len(self.real_shelf) <= len(other.real_shelf)
			case KeyChest() | dict(): return	len(self.real_shelf) <= len(other)
			case _					: raise		TypeError(f"Object \"{other}\" cannot be compared with {self}")




	# Any iteration for current Shelf occurs along "real_shelf", so it's dunders just delegated to it,
	# implementing the very same way it should with the "real_shelf" KeyChest.
	def __iter__(self)		: yield		from self.real_shelf
	def __next__(self)		: return	next(self.real_shelf)
	def __reversed__(self)	: yield		from reversed(self.real_shelf)




	def __call__(self, *load, silent :bool =False) -> Any :

		"""
			Maintains "magical_shelf" functionality. Providing one argument will be treated as indexing
			to "magical_shelf" so the mapped value will be returned. Providing two arguments as key-value
			pair will lead to populating shelf. Argument "silent" allow to not trigger "modified" flag
			when putting. No arguments provides direct access to "magical_shelf".
		"""

		match load:

			case ( K, )	:	return	self.magical_shelf[K]
			case ( K,V ):

				presence	= K in self.magical_shelf
				valueness	= self.magical_shelf[K] == V
				magical		= self.magical_shelf(K,V)


				if	(not presence or not valueness) and magical is not None:

					if		not silent: self.modified = True
					else:	self.magical_shelf.loggy.debug("Silent mode operational")


			case ()	: return self.magical_shelf
			case _	: self.loggy.warning(f"Unable to put \"{load}\" in magical Shelf")




	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		self.modified = False
		if	self.grab() is None : self.loggy.debug("New Shelf successfully initiated")




	# Property that calculates and returns current difference between "real_shelf" and "magical_shelf"
	# lengths. As calculation suggest subtraction of "magical_shelf" length from "real_shelf", the
	# results must be interpreted as wollows:
	# 0  - shelves have same lengths;
	# N  - "real_shelf" bigger than "magical_shelf" by N items;
	# -N - "magical_shelf" bigger than "real_shelf" by N items;
	# Also properties that returns the set of keys which are differs for real to magical or vice versa.
	@property
	def diff(self) -> int : return len(self.real_shelf) - len(self.magical_shelf)
	@property
	def real_diff(self) -> Set[Hashable]	: return set(self.keys()) - set(self.magical_shelf.keys())
	@property
	def magical_diff(self) -> Set[Hashable]	: return set(self.magical_shelf.keys()) - set(self.keys())




	# Utility methods that are redirections to "real_shelf" implementations of "Inspection",
	# "keysof" and "keys". Must work absolutely the same way as "real_shelf" implies.
	def Inspection(self, level :int =None) -> str	: return self.real_shelf.Inspection(level)
	def keysof(self, value :Any) -> List[Hashable]	: return self.real_shelf.keysof(value)
	def keys(self) -> List[Hashable]				: return self.real_shelf.keys()




	def grab(	self,
				grabbing_path	:str	=None,
				*,
				rewrite			:bool	=False,
				from_locker		:bool	=True
			)-> str | None		:

		"""
			Helper method that allows to populate "real_shelf" with key-value pairs from a shelve file.
			Path to the file might be provided by an argument, or will be taken from "grabbing" field,
			and must be an existent shelve file. Argument "rewrite" allows to preliminary clear current
			"real_shelf". The "from_locker" flag decides whether to iterate through special _locker_ key
			in shelved file, which might be produced by LibraryShelf, and use it for indexing shelved file,
			hence the order of "real_shelf" populating will be the same. By default it is True, cause
			there is no difference for final "real_shelf" length whether to insert values in "_inside_" and
			"_locker_" of "real_shelf" KeyChest in, probably found another "_locker_", order or not.
			If invoked within initiation, using grabbing field, "modified" flag not toggled to True.
			If invoked as a method with "grabbing_path" argument, "modified" flag considered to be True
			if "real_shelf" length have changed. The logic behind such particular behavior is that when
			LibraryShelf is initiated it either an empty or grabbed from file, which is the same in terms
			of "modified" flag. Even regrabbing from "grabbing" field doesn't lead to "modified" flag
			toggling, cause the LibraryShelf object might be already "modified". Only grabbing with
			argument provided will change "modified" flag. Return grabbed file path in case of success,
			None otherwise.
		"""

		if	(grabbable := grabbing_path or self.grabbing) is not None:
			if	isinstance(grabbable, str):
				if(
					(
						ospath.isfile(grabbable)
						or
						ospath.isfile(grabbable + ".db")
						or
						ospath.isfile(grabbable + ".dat")
					)
					and
					(
						osaccess(grabbable, R_OK)
						or
						osaccess(grabbable + ".db", R_OK)
						or
						osaccess(grabbable + ".dat", R_OK)
					)
				):


					self.loggy.debug(f"Grabbing Shelf \"{grabbable}\"")
					L = len(self.real_shelf)


					try:

						with shopen(grabbable) as outer:
							self.loggy.debug(f"Shelf size {len(outer)} keys")


							if	rewrite: self.real_shelf.unload()


							# As KeyChests maintains "_locker_" attribute as a list of keys to preserve
							# the order keys were added to chest, such an attribute will be assigned to
							# the Shelf by "produce" method. By obtaining this, grabbing will occurs
							# along keys in it. In case "_locker_" couldn't be find, order might break.
							if	from_locker and (locker := outer.get("_locker_")) is not None:
								self.loggy.debug(f"Obtained locker of length {len(locker)}")


								for k in locker : self.real_shelf(k, outer[k])


							else:
								if from_locker: self.loggy.debug("Locker not obtained, order not granted")
								else: self.loggy.debug("Locker skipped, order not granted")


								for k,v in outer.items():
									if	k != "_locker_" : self.real_shelf(k,v)


							self.loggy.debug(f"Shelf \"{grabbable}\" successfully grabbed")


							# The point of decision on whether LibraryShelf object might be considered
							# modified or not, based on whether "grab" was in __init__ time (not modified)
							# or by provided "grabbing_path" argument (modified).
							if		grabbing_path is not None : self.modified = len(self.real_shelf) != L
							return	grabbable


					except Exception as E:


						self.loggy.warning(f"Failed to grab \"{grabbable}\" due to: {patronus(E)}")
				else:	self.loggy.info(f"Shelf \"{grabbable}\" to grab does not exist or inaccessible")
			else:		self.loggy.warning(f"Invalid grabbing path type \"{type(grabbable)}\"")
		else:			self.loggy.debug("Shelf to grab not provided")




	def produce(	self,
					producing_path	:str	=None,
					*,
					rewrite			:bool	=False,
					magical			:bool	=False,
					ignore_mod		:bool	=False,
					strict_mode		:bool	=True,
					locker_mode		:bool	=False,
				)-> str | None		:

		"""
			Helper method that produces current object "real_shelf" or "magical_shelf" to a shelve file.
			Path to the file might be provided by an argument, or will be derived from either "producing"
			field or from grabbing field, in case of "reclaiming" flag set to True ("producing" has
			priority over "reclaiming"). With argument "rewrite" it is possible to fully clear producible
			shelve file, as it is opened as a new or as already existent file. Decision of which shelf to
			produce is made by flag "magical", which is False by default to produce "real_shelf".
			Argument "ignore_mod" allows to produce even if there was no Shelfs modification, described by
			falsy flag "modified". With "strict_mode" set to True it is assumed, that file destination
			is in existent folder, and Exception will be caught otherwise, but if False, check-creation
			will be granted. The "locker_mode" is disabled by default, cause it leads to end up mapping
			changes by LibraryShelf, so such feature must be turned on with full understanding of further
			consequences, pros and cons of one more key "_locker_" in mapping. Returns produced file path
			in case of success, None otherwise.
		"""

		if	self.modified or ignore_mod:
			if(

				producible := producing_path
				or
				self.producing
				or
				(self.grabbing if self.reclaiming else None)

			)	is not None:

				shl = len(self.magical_shelf if magical else self.real_shelf)
				self.loggy.debug(f"Producing Shelf \"{producible}\"")
				self.loggy.debug("Source is %s Shelf with %s key%s"%(
					"magical" if magical else "real", shl, flagrate(shl)
				))

				try:

					# Boolean flag "strict_mode" disallow creating non-existing parents directories
					# for Shelf file producing, by default. Toggled to False allows check-creation.
					if	not strict_mode : makedirs(ospath.dirname(producible), exist_ok=True)
					if	ignore_mod : self.loggy.debug("Shelf modification flag ignored")


					with shopen(producible, "n" if rewrite else "c") as outer:
						for k,v in self.magical_shelf if magical else self.real_shelf:


							outer[k] = v
							self.loggy.debug(f"Produced key \"{k}\"")


						# Saving current procssed Shelf "_locker_" as a special key in the producible,
						# to allow further grabbing keep the order it was in KeyChest.
						if	locker_mode:

							locker = (self.magical_shelf if magical else self.real_shelf)._locker_
							outer["_locker_"] = locker
							self.loggy.debug(f"Locker of length {len(locker)} produced")


						if rewrite:	self.loggy.info(f"Rewritten Shelf \"{producible}\"")
						else:		self.loggy.info(f"Produced Shelf \"{producible}\"")


						return	producible


				except	Exception as E:


					self.loggy.warning(f"Producing \"{producible}\" failed with {patronus(E)}")
			else:	self.loggy.debug("Shelf to produce not provided")
		else:		self.loggy.debug("Shelf was not modified")




	def unload(self, magical :bool =False):

		"""
			Executes both real and magical KeyChests "unload" operation, that completely clears both
			KeyChests key-pairs and lockers, and reset their corresponding counters. Also set "modified"
			flag to False, meaning full initiation imitation.
		"""

		self.modified = False
		self.real_shelf.unload()
		self.loggy.info(f"{self} real shelf was unloaded")

		if	magical:

			self.magical_shelf.unload()
			self.loggy.info(f"{self} magical shelf was unloaded")







