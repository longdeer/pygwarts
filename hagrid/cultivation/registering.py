from typing												import List
from typing												import Tuple
from typing												import Generator
from pathlib											import Path
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.irma.shelve								import LibraryShelf








WG = "weight-global"
TG = "twigs-global"
LG = "leafs-global"
WL = "weight-local"
TL = "twigs-local"
LL = "leafs-local"








def regress(branch :Path, sprout :str, previous=None) -> Generator[Path,None,None] :

	"""
		Utility function that accepts "branch" as Path object and iterates via it's parents, until
		some parent won't represent second argument "sprout" string, or until the root folder will
		be reached. The last one condition will be met when recursive call's "branch" will be the same
		as the "previous" argument, that will be set to "branch" after very first initial call. As Path
		object's "parent" field will always return new Path object, even when the root is reached, this
		might cause RecursionError, so the "previous" argument does guard.
		Goes depth-first and yields a Path object at every step, starting from the last one, the "sprout"
		or root folder, respectively. No send, no return.
	"""

	if	isinstance(branch, Path) and branch != previous:
		if	isinstance(sprout, str):

			if		str(branch) != sprout : yield from regress(branch.parent, sprout, branch)
			yield		branch








class PlantRegister(ControlledTransmutation):

	"""
		hagrid.cultivation utility decorator class, that serves as an interceptor and preprocessor of
		"plants". It is the wrapper over the "planting" dispatcher (Flourish object) that has a midway
		access to all tuples of sprout, branch, twigs, leafs, that are currently "walked". Such access
		is used to register every "walked" branch, which means collect information about twigs and leafs
		with their weights (sizes). As ControlledTransmutation class, accepts the only argument "link",
		that must be a string identifier of a LibraryShelf object, that is to be used as a place for
		storing registration data. In mutable chain acts as a mutation - takes decorated planting
		dispatching class and extends it by declaring meta __call__ to invoke decorated __call__.
		Meta __call__ will register every received sprout's branch in linked LibraryShelf the following way:
			-	LibraryShelf.real_shelf will represent the measures tree, where each key is a folder
				string and it's value will be nested dictionary with 6 string keys mapped with
				corresponding measure integers:
					TG - twigs global, number of all downfall folders;
					LG - leafs global, number of all downfall files;
					WG - weight global, summation of all downfall files sizes;
					TL - twigs local, number of folders in current folder;
					LL - leafs local, number of files in current folder;
					WL - weight local, summation of current folder files sizes.
			-	LibraryShelf.magical_shelf will represent the replication tree, where each key is a fs item
				(folder/file) as a string, and value for a folder is nested dictionary, value for a file -
				it's size;
		After it's processing, invokes decorated object __call__ with all received arguments.
	"""


	def __init__(self, link :str):
		self.link = link

	def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :
		link = str(self.link)


		class Registration(geminio(mutable_layer)):
			def __call__(self, *plant :Tuple[str, Path, List[Path], List[Path]], **kwargs):


				if	plant and isinstance(garden := getattr(self, link, None), LibraryShelf):
					sprout, branch, twigs, leafs = plant


					thrive_path		= list(map(str, regress(branch, sprout)))
					local_twigs		= len(twigs)
					local_leafs		= len(leafs)
					local_weight	= 0


					for twig in twigs:
						if	isinstance(twig, Path):


							garden.magical_shelf(str(twig), dict(), *thrive_path, mapped=False)
							self.loggy.debug(f"Registered flourishing twig \"{twig}\"")
						else:
							self.loggy.debug(f"Skipped invalid twig \"{twig}\"")


					for leaf in leafs:
						if	isinstance(leaf, Path):


							current_weight	= leaf.stat().st_size
							local_weight  += current_weight


							garden.magical_shelf(str(leaf), current_weight, *thrive_path, mapped=False)
							self.loggy.debug(f"Registered flourishing leaf \"{leaf}\"")
						else:
							self.loggy.debug(f"Skipped invalid leaf \"{leaf}\"")


					garden.real_shelf(TL,	local_twigs,	*thrive_path, mapped=False)
					garden.real_shelf(LL,	local_leafs,	*thrive_path, mapped=False)
					garden.real_shelf(WL,	local_weight,	*thrive_path, mapped=False)


					for shoot_index in range(1,len(thrive_path) +1):


						shoot_record	= garden.real_shelf.deep(*thrive_path[:shoot_index])
						shoot_twigs		= shoot_record.get(TG)	or 0
						shoot_leafs		= shoot_record.get(LG)	or 0
						shoot_weight	= shoot_record.get(WG)	or 0

						shoot_record[TG]= shoot_twigs	+local_twigs
						shoot_record[LG]= shoot_leafs	+local_leafs
						shoot_record[WG]= shoot_weight	+local_weight


				super().__call__(*plant, **kwargs)
		return	Registration








class PlantRegisterQuerier:

	"""
		Utility class for retrieving PlantRegister information. Must be initiated with valid LibraryShelf
		object as "garden" argument, which must be populated by PlantRegister, to operate with. The basic
		method "query" allows to retrieve all PlantRegister stats:
			TG - twigs-global;
			LG - leafs-global;
			WG - weight-global;
			TL - twigs-local;
			LL - leafs-local;
			WL - weight-local.
		For convenience eponymous shorthand methods are defined. Advanced "content" method allows obtaining
		comprehensive information about directory content sizes.
	"""

	def __init__(self, garden :LibraryShelf):
		self.garden = garden if isinstance(garden, LibraryShelf) else None

	def query(self, branch :str | Path =None, sprout :str | Path =None, key :str =None) -> int | None :

		"""
			Basic method to query LibraryShelf object real_shelf, which must represent detailed
			structure of some fs tree, with PlantRegister statistics. Information might be retrieved
			for any folder that stored in "garden" by providing it as a "branch" argument. As "garden"
			might be populated with different fs trees, the second argument "sprout" might be provided
			for pointing right direction. If "sprout" is omitted, "branch" will be searched in entire
			"garden", so providing "sprout" is a speed up. If no "branch" is provided, provided "sprout"
			information will be retrieved. If both omitted, the very first sprout in "garden" information
			will be retrieved. The kind of information to retrieve must be specified by last argument
			"key", which must be one of WG, TG, LG, WL, TL, LL. Returns retrieved integer, corresponding
			valid arguments set, or None in any other case.
		"""

		if	isinstance(getattr(self, "garden", None), LibraryShelf):

			if not isinstance(branch, str | Path | None): return
			if not isinstance(sprout, str | Path | None): return


			state  = bool(key == WG or key == TG or key == LG or key == WL or key == TL or key == LL)
			state ^= bool(branch) <<1
			state ^= bool(sprout) <<2


			match state:

				# valid key provided
				# branch provided
				# sprout provided
				case 7:
					record = self.garden.real_shelf.deep(*map(str,regress(Path(branch),str(sprout))))
					if	isinstance(record, dict): return record.get(key)


				# valid key provided
				# sprout provided
				case 5:
					if	isinstance(record := self.garden[sprout], dict): return record.get(key)


				# valid key provided
				# branch provided
				case 3:
					for nest in self.garden:
						record = self.garden.real_shelf.deep(*map(str,regress(Path(branch),str(nest[0]))))

						if isinstance(record, dict): return record.get(key)


				# valid key provided
				case 1:
					for nest in self.garden:
						if isinstance(record := self.garden[nest[0]], dict): return record.get(key)




	def WG(self, branch :str | Path =None, sprout :str | Path =None, apparent :bool =False) -> int | None :

		"""
			Shorthand method for retrieving "weight-global" information for "branch" folder. Uses "query"
			method and accepts optional "sprout" argument for speed up. Also accepts optional "apparent"
			boolean flag, which once will be set to True (default False) will cause addition to retrieved
			size of 4096 (folder fs size) multiplied by descent folders number. Returns "query" result
			integer (according to "apparent") or None.
		"""

		if	isinstance(current := self.query(branch, sprout, WG), int):
			if apparent : current += self.query(branch, sprout, TG) *4096

			return current


	def WL(self, branch :str | Path =None, sprout :str | Path =None, apparent :bool =False) -> int | None :

		"""
			Shorthand method for retrieving "weight-local" information for "branch" folder. Uses "query"
			method and accepts optional "sprout" argument for speed up. Also accepts optional "apparent"
			boolean flag, which once will be set to True (default False) will cause addition to retrieved
			size of 4096 (folder fs size) multiplied by descent folders number. Returns "query" result
			integer (according to "apparent") or None.
		"""

		if	isinstance(current := self.query(branch, sprout, WL), int):
			if apparent : current += self.query(branch, sprout, TL) *4096

			return current


	def TG(self, branch :str | Path =None, sprout :str | Path =None) -> int | None :

		"""
			Shorthand method for retrieving "twigs-global" information for "branch" folder. Uses "query"
			method and accepts optional "sprout" argument for speed up. Returns "query" result integer
			or None.
		"""

		if	isinstance(current := self.query(branch, sprout, TG), int):
			return current


	def LG(self, branch :str | Path =None, sprout :str | Path =None) -> int | None :

		"""
			Shorthand method for retrieving "leafs-global" information for "branch" folder. Uses "query"
			method and accepts optional "sprout" argument for speed up. Returns "query" result integer
			or None.
		"""

		if	isinstance(current := self.query(branch, sprout, LG), int):
			return current


	def TL(self, branch :str | Path =None, sprout :str | Path =None) -> int | None :

		"""
			Shorthand method for retrieving "twigs-local" information for "branch" folder. Uses "query"
			method and accepts optional "sprout" argument for speed up. Returns "query" result integer
			or None.
		"""

		if	isinstance(current := self.query(branch, sprout, TL), int):
			return current


	def LL(self, branch :str | Path =None, sprout :str | Path =None) -> int | None :

		"""
			Shorthand method for retrieving "leafs-local" information for "branch" folder. Uses "query"
			method and accepts optional "sprout" argument for speed up. Returns "query" result integer
			or None.
		"""

		if	isinstance(current := self.query(branch, sprout, LL), int):
			return current


	def content(	self,
					branch						:str | Path	=None,
					sprout						:str | Path	=None,
					apparent					:bool		=False
				)-> List[Tuple[int,str]] | None	:

		"""
			Advanced method of querying LibraryShelf to expand "branch" directory comprehensive information.
			Information might be retrieved for any directory that stored in "garden" by providing it as a
			"branch" argument. As "garden" might be populated with different fs trees, the second argument
			"sprout" might be provided for pointing right direction. If "sprout" is omitted, "branch" will
			be searched in entire "garden", so providing "sprout" is a speed up. If no "branch" is provided,
			provided "sprout" information will be retrieved. If both omitted, the very first sprout in
			"garden" information will be retrieved, which basically may be produce unwanted result.
			Retrieved information will represent a list of tuples of integer and a string - the size in
			bytes and corresponding "branch" subfolder. Every subfolder size is a corresponding retrieved
			"weight-global". If "branch" has positive "weight-local", which means there are some files
			in it, resulting list will be appended with additional tuple of "branch" files size and the
			"branch" string itself. By default every sizes is taken not apparent, and last argument
			"apparent" is a boolean flag, which once will be set to True (default False) will cause
			addition to every size of 4096 (folder fs size) multiplied by descent folders number.
		"""

		if	isinstance(getattr(self, "garden", None), LibraryShelf):

			if	not isinstance(branch, str | Path | None): return
			if	not isinstance(sprout, str | Path | None): return


			if	branch is None or sprout is None:
				for nest in self.garden:

					branch = branch or nest[0]
					sprout = sprout or nest[0]


			record = self.garden.real_shelf.deep(*map(str,regress(Path(branch),str(sprout))))


			if	isinstance(record, dict):

				inner_weight = record.get(WL)
				content = [( inner_weight,str(branch) )] if inner_weight else []


				for key in record:
					if	key != TG and key != TL and key != LG and key != LL and key != WG and key != WL:

						current = record.get(key).get(WG)
						if apparent : current += record.get(key).get(TG) *4096


						content.append(( current,key ))
				return	content







