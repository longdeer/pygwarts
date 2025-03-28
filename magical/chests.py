from __future__								import annotations
from typing									import Any
from typing									import List
from typing									import Hashable
from pygwarts.magical.philosophers_stone	import Transmutable








class Chest(Transmutable):

	"""
				         ..~>%######%%%??!!>;:=~-,....                                                    
		   .._=>?#&?<::::::::::::::;><<!?%#%%??!!>;:++=~---___----~~~~--__,,....... ....          
		.-:%@B$%??!!!!!!???????????!!!<<>>;;:::::;>><!!???%%%%???!!!!!??%%%%%###%%%%%????!!!!<<>+.
		@#!<<>;;::::::::::::::::::::;;;>>><<!!!!!!?????!!<<<<<<>>>;::::::::::::::::::><?%%#&&##&@.
		@?::::::;;;;::::::::::::::::::::::::::::::::::;;>>>><<<!!!??????????!<>!?%##&#%????????#@.
		?&:#?<;>@!!!??#:::;!?<:::::<!!>:::::::::::::::::::::::::::::::::::::;#&%????????????&&?&#.
		>@:%!#<:@;%?#!$:::&>;?#:::>#<:#>::::::::::<%?%!::!????;::::;>>>;:::::!&????#&&#???#%$&?$>.
		+B::::::@;<?!;$:::><::!#%!<<!?%;::::::::::@>??>:<#:::>@>::>&<<<<!&;>?;$?%&?%@??????##?&B?.
		=B#%%%%%B%%???@!!<<>>;;::>>>;:::::::::::::>%?!<?&;::!!%;:::&>%?&;&;??;#%?&&##?????%#$@#%B>
		~B;:::::!#;;;$!>><<!!???????????!!<>;::::::::;>;::::::::::;#;?!!;&::::?&??????%#&&@%;@??&#
		~B;:::::!%;;;@::::::::::::::::::;><!!?????????!!<<>>;;::::<%;;;;;&::::#&?%#&$$#%??#%;@%##$
		~B::::::<%;;;$::::::::::::::::::::::::::::::::;>><<!!??????$$%%%%@%%##$@&&$>%#???%&#;!?@#@
		=B::::::<#;;>&::::::::::::::::>?#%%%%????>:::::::::::::::::<$;;;>&::::<$??B;##?%%%#?;<&?%$
		=B:::##??<;;>#???%%>:::::::::##<;;;;;;;;>%&>:::::::::::::::;@;;;<%::::>$??@?>?!?B%?%&&??%&
		+@:::;%#>;;;;;;;!$!:::::::::>$;;;;;;;;;;<;<@:::::::::::::::;B;;;%!::::>@?##>;;>$%???????##
		+B:::::;?%>;;;<&?::::::::::;$#<;;;;;;;;;;;##:::::::::::::%%?>;;;!%??<:;@?%&?><$%????????#%
		+B:::::::;?#!%?;:::::::::::;@!;;;;;;;;;;;;!%%;:::::::::::<&?;;;;;;?&<::B???%#&??????%#%?&?
		=B::::::::::<>::::::::::::%$!;;;;;;;;;;;;;%#?;:::::::::::::!&!;;!&!::::@????????????&#$?#?
		-B;::::::::::::::::::::::::<%%!;;;;;;;;;;;?#!::::::::::::::::!##<::::::$????%????????%??#?
		.B>::::::::$#$$::::::::::::::%#;;;;;;;;;;!%%$<:::::::::::::::::::::::::&%???$$#????%$&&?#%
		.$<::::::::>??>:::::::::::::>@%%%#!;?%!;!#::::::::::::::::::::<!>::::::#%???%%???????%??##
		.#!:::::::::::::::::::::::::::::::##<:>?%::::::::::::::::::::<$%@>:::::%#???###?????%???##
		.?%:::::::;<>:::::::::::::::::::::::::::::::::::::::::::::::::><>::::::?&???###????%&!#$#$
		.<#:::::::<$$&:::::::::::>!!<>>>><<<<<<<<<<<<<<<<>>>:::::::::::::::::::!&??????????#;!@?#B
		.;$::::::::;;::::::::::::;<<!!<<<<<<>>>>>>>>>>><<<<<>::::::::::::::::::>$?????????$??;%$B?
		 :@::::::::<?%>::::::::;%%%?!!<<<>>>>>>>>>>>>>>;;;:::::::::::::%%!;::::;@??%&%??????&<<B>.
		 =B;::::;%#!;>%#>:::::::::;>><<!!!!!!!!!!!!!!!????%#!::::::::::%?#<:::::@??#!><!?&%?#$&-. 
		 _B<:::;@%>;;;;;%%;:::::::::::::::::::::::::::::::::::::::::::::>>::::::@??@!%>>&#?%@?..  
		 .@!::::;>##;;>%?%@<::::::::>#%%>::::::::::::::::::::::::::::;%#!?#<::::$%?%%@>>@?#@:.    
		 .#%::::::&!;;;@;;>>:>?!!:::;?><@::::::::;&%#<:::>??%;:::::>##>;;;;!#<::#%???$!;#B&_.     
		 .<&;::::;B;;;;@:::::#;:<%?!<!%#<:::::::::&!<;:<#?:>&?::::>B&%!;;;>!?@!:%#???&&>$!.       
		  ,;?%###$@??!!$!>>;;::::::;>;:::::::::::::!%%%!;::;;::::::::&%;;;?#;:::?&????B@;.        
		     ...,_-~=++:;;><<!???%%%###%%??!!<<>>>;;:::::::::::::::::@>;;;%!::::!&??%$&~.         
		                        ........,__-~~==+::;;>>>><<<<!!!!???#@%###@&##%%#&%?>~..          
		Mutable chain implementation of container with Transmutables. It is a special list, as all logic
		lies behind maintaining "_inside_" list, to be a part of mutable chain.
		Any Transmutables can be puted into Chest by calling the Chest, providing them as argument.
		Providing no arguments during Chest call will simply return a copy of "_inside_" list
		of Transmutables (calling with arguments to put Transmutables in Chest will also return such copy).
		Chest can be iterated, compared to be equal to another Chest or a list, compared to be
		greater (or equal)/lesser (or equal) than another Chest or list (comparison will take place
		against lengths), Transmutable items can be assigned/obtained/deleted. The built-in function
		"next" will take place instantly, so Chest is iterator by default. There is no "full exhaustion"
		of such iterator, so after StopIteration raised when all "_inside_" elements passed, the next
		call of "next" (after call that raised StopIteration), the iteration starts over again.
	"""

	def __len__(self) -> int : return len(self._inside_)
	def __hash__(self) -> int : return id(self)
	def __contains__(self, item :Transmutable) -> bool : return item in self._inside_
	def __getitem__	(self, index :int) -> Transmutable | None :

		"""
			Trying to index into "_inside_" list to get corresponding Transmutable.
			If index is out of "_inside_" range or "_inside_" length is 0, there'll be no Exception
			and simply None returned.
		"""

		if	len(self._inside_) and (0 <= index < len(self._inside_) or 0 >= index >= -len(self._inside_)):
			return self._inside_[index]




	def __setitem__(self, index :int, item :Transmutable):

		"""
			Assigning "_inside_" index to a Transmutable item. If item is not Transmutable or index
			is out of "_inside_" range, no modification to "_inside_" will be made and corresponding
			warning message will be logged with no exception raising.
		"""

		if	isinstance(item, Transmutable):
			if	index < len(self._inside_):

				self._inside_[index] = item
				self.loggy.debug(f"{item} packed at index {index}")


			else:	self.loggy.warning(f"Index {index} is out of {self} Chest range, {item} not putted")
		else:		self.loggy.warning(f"Can't put \"{type(item)}\" in {self} Chest")




	def __delitem__(self, index :int):

		"""
			Removing Transmutable from "_inside_" list. If index out of "_inside_" range, corresponding
			warning message will be logged with no "_inside_" modification and no exception raising.
		"""

		if	len(self._inside_) and (0 <= index < len(self._inside_) or 0 >= index >= -len(self._inside_)):

			item = self._inside_[index]
			del self._inside_[index]

			self.loggy.info(f"Removed {item} from {self} Chest")


		else:
			self.loggy.warning(f"Index {index} out of {self} Chest range, no removing made")




	def __eq__(self, other :Chest | List[Transmutable]) -> bool :

		"""
			Comparison of equality of current Chest "_inside_" list with another
			Chest object's "_inside_" list or with any other list object.
		"""

		match other:

			case Chest()	: return	self._inside_ == other._inside_
			case list()		: return	self._inside_ == other
			case _			: return	False




	def __gt__(self, other :Chest | List[Transmutable]) -> bool | TypeError :

		"""
			Comparison of greatness of current Chest "_inside_" list length with another Chest object's
			"_inside_" list or with any other list object's length.
		"""

		match other:

			case Chest()	: return	len(self._inside_) > len(other._inside_)
			case list()		: return	len(self._inside_) > len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} Chest")




	def __ge__(self, other :Chest | List[Transmutable]) -> bool | TypeError :

		"""
			Comparison of greatness or equality of current Chest "_inside_" list length with another
			Chest object's "_inside_" list or with any other list object's length.
		"""

		match other:

			case Chest()	: return	len(self._inside_) >= len(other._inside_)
			case list()		: return	len(self._inside_) >= len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} Chest")




	def __lt__(self, other :Chest | List[Transmutable]) -> bool | TypeError :

		"""
			Comparison of lesserness of current Chest "_inside_" list length with another Chest object's
			"_inside_" list or with any other list object's length.
		"""

		match other:

			case Chest()	: return	len(self._inside_) < len(other._inside_)
			case list()		: return	len(self._inside_) < len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} Chest")




	def __le__(self, other :Chest | List[Transmutable]) -> bool | TypeError :

		"""
			Comparison of lesserness or equality of current Chest "_inside_" list length with another
			Chest object's "_inside_" list or with any other list object's length.
		"""

		match other:

			case Chest()	: return	len(self._inside_) <= len(other._inside_)
			case list()		: return	len(self._inside_) <= len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} Chest")




	def __iter__(self):

		"""
			Iterator implementation. Logs debug message before every item yield. If there is no items
			in "_inside_", corresponding debug message will be logged.
		"""

		if	len(self._inside_):
			for item in self._inside_:

				self.loggy.debug(f"Yielding \"{item}\"")
				yield item
		else:	self.loggy.debug(f"Chest is empty")




	def __next__(self):

		"""
			Chest the iterator by default, so calling "next" will iterate through "_inside_".
			Apart to generator like iteration, Chest iteration will be reset every time StopIteration
			is raised after "_inside_" exhausted, so it might be iterated over and over again. This is
			possible by the "_current" field which tracks the "_inside_" length and resets every time
			the "_inside_" exhausted. To make "next" calls work classic way, it is possible to call it
			over "iter" call on current Chest.
		"""

		if	self._current < len(self._inside_):

			_next_ = self._inside_[self._current]
			self._current += 1


			return _next_


		self._current = 0
		raise StopIteration




	def __call__(self, *load) -> List[Transmutable,] | None:

		"""
			When single Transmutable provided in load, it is "_inside_" adding process.
			More than one argument in load will cause to check every argument to be Transmutable and put
			it to the Chest, discarding non Transmutables.
			With no arguments it is simply "_inside_" copy returning, cause __str__ will never return
			"_inside_", so such call with no arguments is the way to obtain "_inside_" list copy.
			Any other situation will cause no Chest modification, corresponding warning message
			and None as the return value, that should inform about problems.
		"""

		match load:
			case ( Transmutable(), ):

				self._inside_.append(*load)
				self.loggy.debug(f"Putted \"{load[0]}\"")

			case ( *multiple_load, ) if 1 <len(multiple_load):

				for item in multiple_load:
					if	isinstance(item, Transmutable):


						self._inside_.append(item)
						self.loggy.debug(f"Putted \"{item}\"")
					else:
						self.loggy.debug(f"Discarding \"{item}\" load")
			case ()	:	pass
			case _	:

				self.loggy.warning(f"Can't put \"{load[0]}\" in {self} Chest")
				return


		# Additional wrapping of "_inside_" to a list will cause no modification of current Chest
		# "_inside_" directly through this __call__ return value, as any modifications are supposed
		# to be maintained only with Chest functionality.
		return list(self._inside_)




	def __init__(self, *args, **kwargs):

		# Initiating Chest core fields first allows putting during initiation.
		self.unload()
		super().__init__(*args, **kwargs)




	def unload(self):

		"""
			Wipes "_inside_" items completely by reinitiating with "_current".
			Also used as initiation by itself.
		"""

		self._inside_ = list()
		self._current = 0





	def index(self, item :Transmutable) -> int | None :

		"""
			Find item in "_inside_" list and return it's first occurrence index. If item not present in
			"_inside_", or if item is not Transmutable, None will be returned and corresponding debug
			messages will be logged.
		"""

		if	isinstance(item, Transmutable):
			for i,inner in enumerate(self._inside_):
				if	inner == item:

					self.loggy.debug(f"Found {item} at index {i}")
					return i
			else:	self.loggy.debug(f"Item {item} not found")
		else:		self.loggy.debug(f"Item {item} type \"{type(item)}\" cannot be searched")








class KeyChest(Transmutable):

	"""
				         ..~>%######%%%??!!>;:=~-,....                                                    
		   .._=>?#&?<::::::::::::::;><<!?%#%%??!!>;:++=~---___----~~~~--__,,....... ....          
		.-:%@B$%??!!!!!!???????????!!!<<>>;;:::::;>><!!???%%%%???!!!!!??%%%%%###%%%%%????!!!!<<>+.
		@#!<<>;;::::::::::::::::::::;;;>>><<!!!!!!?????!!<<<<<<>>>;::::::::::::::::::><?%%#&&##&@.
		@?::::::;;;;::::::::::::::::::::::::::::::::::;;>>>><<<!!!??????????!<>!?%##&#%????????#@.
		?&:#?<;>@!!!??#:::;!?<:::::<!!>:::::::::::::::::::::::::::::::::::::;#&%????????????&&?&#.
		>@:%!#<:@;%?#!$:::&>;?#:::>#<:#>::::::::::<%?%!::!????;::::;>>>;:::::!&????#&&#???#%$&?$>.
		+B::::::@;<?!;$:::><::!#%!<<!?%;::::::::::@>??>:<#:::>@>::>&<<<<!&;>?;$?%&?%@??????##?&B?.
		=B#%%%%%B%%???@!!<<>>;;::>>>;:::::::::::::>%?!<?&;::!!%;:::&>%?&;&;??;#%?&&##?????%#$@#%B>
		~B;:::::!#;;;$!>><<!!???????????!!<>;::::::::;>;::::::::::;#;?!!;&::::?&??????%#&&@%;@??&#
		~B;:::::!%;;;@::::::::::::::::::;><!!?????????!!<<>>;;::::<%;;;;;&::::#&?%#&$$#%??#%;@%##$
		~B::::::<%;;;$::::::::::::::::::::::::::::::::;>><<!!??????$$%%%%@%%##$@&&$>%#???%&#;!?@#@
		=B::::::<#;;>&::::::::::::::::>?#%%%%????>:::::::::::::::::<$;;;>&::::<$??B;##?%%%#?;<&?%$
		=B:::##??<;;>#???%%>:::::::::##<;<!???!;>%&>:::::::::::::::;@;;;<%::::>$??@?>?!?B%?%&&??%&
		+@:::;%#>;;;;;;;!$!:::::::::>$;;@@$$&&$B<;<@:::::::::::::::;B;;;%!::::>@?##>;;>$%???????##
		+B:::::;?%>;;;<&?::::::::::;$#<;%@$&&@B@>;##:::::::::::::%%?>;;;!%??<:;@?%&?><$%????????#%
		+B:::::::;?#!%?;:::::::::::;@!;;;>@&&@$;;;!%%;:::::::::::<&?;;;;;;?&<::B???%#&??????%#%?&?
		=B::::::::::<>::::::::::::%$!;;;;;B&&&B>;;%#?;:::::::::::::!&!;;!&!::::@????????????&#$?#?
		-B;::::::::::::::::::::::::<%%!;;;$@$$$>;;?#!::::::::::::::::!##<::::::$????%????????%??#?
		.B>::::::::$#$$::::::::::::::%#;;;;;;;;;;!%%$<:::::::::::::::::::::::::&%???$$#????%$&&?#%
		.$<::::::::>??>:::::::::::::>@%%%#!;?%!;!#::::::::::::::::::::<!>::::::#%???%%???????%??##
		.#!:::::::::::::::::::::::::::::::##<:>?%::::::::::::::::::::<$%@>:::::%#???###?????%???##
		.?%:::::::;<>:::::::::::::::::::::::::::::::::::::::::::::::::><>::::::?&???###????%&!#$#$
		.<#:::::::<$$&:::::::::::>!!<>>>><<<<<<<<<<<<<<<<>>>:::::::::::::::::::!&??????????#;!@?#B
		.;$::::::::;;::::::::::::;<<!!<<<<<<>>>>>>>>>>><<<<<>::::::::::::::::::>$?????????$??;%$B?
		 :@::::::::<?%>::::::::;%%%?!!<<<>>>>>>>>>>>>>>;;;:::::::::::::%%!;::::;@??%&%??????&<<B>.
		 =B;::::;%#!;>%#>:::::::::;>><<!!!!!!!!!!!!!!!????%#!::::::::::%?#<:::::@??#!><!?&%?#$&-. 
		 _B<:::;@%>;;;;;%%;:::::::::::::::::::::::::::::::::::::::::::::>>::::::@??@!%>>&#?%@?..  
		 .@!::::;>##;;>%?%@<::::::::>#%%>::::::::::::::::::::::::::::;%#!?#<::::$%?%%@>>@?#@:.    
		 .#%::::::&!;;;@;;>>:>?!!:::;?><@::::::::;&%#<:::>??%;:::::>##>;;;;!#<::#%???$!;#B&_.     
		 .<&;::::;B;;;;@:::::#;:<%?!<!%#<:::::::::&!<;:<#?:>&?::::>B&%!;;;>!?@!:%#???&&>$!.       
		  ,;?%###$@??!!$!>>;;::::::;>;:::::::::::::!%%%!;::;;::::::::&%;;;?#;:::?&????B@;.        
		     ...,_-~=++:;;><<!???%%%###%%??!!<<>>>;;:::::::::::::::::@>;;;%!::::!&??%$&~.         
		                        ........,__-~~==+::;;>>>><<<<!!!!???#@%###@&##%%#&%?>~..          
		Mutable chain implementation of mapped container with objects of any type.
		It is a special dict, as all logic lies behind maintaining "_inside_" dict and "_locker_" list,
		containing only keys, to be a part of mutable chain.
		One can put whatever key-value pair into KeyChest by calling the KeyChest, providing
		key-value pair as arguments. All arguments after key-value pair will be considered as nesting keys,
		so by the special flag "mapped" their will either be created or not, with warnings logs.
		Providing no arguments during KeyChest call will simply return a copy of "_inside_" dict
		(calling with arguments to put in KeyChest will also return such copy).
		KeyChest can be iterated, compared to be equal to another KeyChest or a dict, compared to be
		greater (or equal)/lesser (or equal) than another KeyChest or dict (comparison will take place
		against lengths), key-value pairs can be assigned/obtained/deleted. The built-in function
		"next" will take place instantly, so KeyChest is iterator by default. There is no "full exhaustion"
		of such iterator, so after StopIteration raised when all "_inside_" elements passed, the next
		call of "next" (after call that raised StopIteration), the iteration starts over again.
		It is prohibited to modify "_inside_" and "_locker_" directly, cause it might brake KeyChest!
	"""

	def __len__(self) -> int : return len(self._inside_)
	def __hash__(self) -> int : return id(self)
	def __getitem__(self, K :Hashable) -> Any | None :

		"""
			Despite python core logic implies TypeError raise when unhashable key is accessed
			even with "get" method, KeyChest "__getitem__" implementation return None in such
			situation, because pygwarts is about magic.
		"""

		try:	return		self._inside_.get(K)
		except	TypeError : return




	def __contains__(self, K :Hashable)	-> bool	:

		"""
			Despite python core logic implies TypeError raise when unhashable key is even peeked
			for presence in dictionary, KeyChest "__contains__" implementation return False in such
			situation, because pygwarts is about magic.
		"""

		try:	return		K in self._inside_
		except	TypeError : return	False




	def __setitem__(self, K :Hashable, V :Any):

		"""
			Assigning "_inside_" dict key-value pair, along with maintenance of "_locker_" list of keys.
			If key is a new one, both "_inside_" and "_locker_" will be updated. If key is already present,
			only "_inside_" will be modified. If key is not hashable type, TypeError will be caught and
			warning message will be logged, with no KeyChest object modification.
		"""

		try:

			presence = K in self._inside_
			self._inside_[K] = V


			if	presence : self.loggy.debug(f"Replaced \"{K}\", \"{V}\" pair")
			else:

				self._locker_.append(K)
				self.loggy.debug(f"Putted \"{K}\", \"{V}\" pair")
		except	TypeError : self.loggy.warning(f"Can't put \"{K}\", \"{V}\" pair in {self} KeyChest")




	def __delitem__(self, K :Hashable):

		"""
			Removing key from "_inside_" dict and "_locker_" list. If key is not present in KeyChest,
			corresponding debug message will be logged. If key is not hashable type, TypeError will be
			caught and corresponding warning message will be logged.
		"""

		try:

			if	K in self._inside_:

				V = self._inside_[K]
				I = self._locker_.index(K)


				del self._inside_[K]
				del self._locker_[I]


				self.loggy.debug(f"Removed \"{K}\", \"{V}\" pair")
			else:
				self.loggy.debug(f"Key \"{K}\" not in {self} KeyChest")
		except	TypeError :	self.loggy.warning(f"Impossible key \"{K}\" for {self} KeyChest")
		except	ValueError: self.loggy.warning(f"Key \"{K}\" not found in locker")




	def __eq__(self, other :KeyChest | dict) -> bool :

		"""
			Comparison of equality of current KeyChest "_inside_" dict with another KeyChest
			object's "_inside_" dict or with any other dict object.
		"""

		match other:

			case KeyChest()	: return	self._inside_ == other._inside_
			case dict()		: return	self._inside_ == other
			case _			: return	False




	def __gt__(self, other :KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of greatness of current KeyChest "_inside_" dict length with another KeyChest
			object's "_inside_" dict or with any other dict object's length.
		"""

		match other:

			case KeyChest()	: return	len(self._inside_) > len(other._inside_)
			case dict()		: return	len(self._inside_) > len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} KeyChest")




	def __ge__(self, other :KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of greatness or equality of current KeyChest "_inside_" dict length with another
			KeyChest object's "_inside_" dict or with any other dict object's length.
		"""

		match other:

			case KeyChest()	: return	len(self._inside_) >= len(other._inside_)
			case dict()		: return	len(self._inside_) >= len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} KeyChest")




	def __lt__(self, other :KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of lesserness of current KeyChest "_inside_" dict length with another KeyChest
			object's "_inside_" dict or with any other dict object's length.
		"""

		match other:

			case KeyChest()	: return	len(self._inside_) < len(other._inside_)
			case dict()		: return	len(self._inside_) < len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} KeyChest")




	def __le__(self, other :KeyChest | dict) -> bool | TypeError :

		"""
			Comparison of lesserness or equality of current KeyChest "_inside_" dict length with another
			KeyChest object's "_inside_" dict or with any other dict object's length.
		"""

		match other:

			case KeyChest()	: return	len(self._inside_) <= len(other._inside_)
			case dict()		: return	len(self._inside_) <= len(other)
			case _			: raise		TypeError(f"Object \"{other}\" cannot be compared with {self} KeyChest")




	def __iter__(self):

		"""
			Iterator implementation. Iteration occurs along "_locker_" list, which contain only keys
			to index into "_inside_" dict. Such logic implements the ordered by injection iteration
			by default in any situation. Yields a tuple of both key and value on every iteration.
			Logs a debug message before every yield. If there is no keys in "_locker_", logs
			corresponding debug message.
		"""

		if	len(self._locker_):
			for K in self._locker_:

				V = self._inside_[K]
				self.loggy.debug(f"Yielding \"{K}\", \"{V}\" pair")


				yield K,V
		else:	self.loggy.debug(f"KeyChest is empty")




	def __next__(self):

		"""
			KeyChest the iterator by default, so calling next will iterate through "_locker_" keys,
			yielding a tuple of both key and value. Apart to generator like iteration,
			KeyChest iteration will be reset every time StopIteration is raised after "_locker_" exhausted,
			so it might be iterated over and over again. To make "next" calls work classic way,
			it is possible to call it over "iter" call on current KeyChest.
		"""

		if	self._current < len(self._locker_):

			_next_key_ = self._locker_[self._current]
			self._current += 1


			return	_next_key_, self._inside_[_next_key_]


		self._current = 0
		raise	StopIteration




	def __reversed__(self):

		""" Reversion along "_locker_" to obtain "_inside_" backward. """

		for key in reversed(self._locker_) : yield key, self._inside_[key]




	def __call__(self, *load, mapped=True) -> dict | None :

		"""
			When load is a two items tuple, they will be assigned as corresponding key value pair
			for "_inside_" dict. If such key is not already present in "_inside_" dict, it will be
			added to the "_locker_" list, that maintains only keys of current KeyChest.
			Any arguments after key-value pair will be considered as nesting keys, which will be
			tried to be created, in case of their absent and "mapped" toggled to False, or indexed
			to put key-value pair at the very end, with corresponding warning loggs in case of any
			trouble and None as the returned value.
			An empty load is simply "_inside_" copy returning, cause __str__ will never return
			"_inside_", so such call with no arguments is the way to obtain "_inside_" dict copy.
			Any other situation will cause no KeyChest modification, corresponding warning message
			and None as the returned value.
		"""

		match load:

			# Regular put. Key-value pair (K,V) will be either putted or replaced, depending on
			# whether current KeyChest already contain such key or not.
			case ( K,V ):
				try:

					presence = K in self._inside_
					self._inside_[K] = V


					# Maintaining "_locker_" list, that tracks root keys in order their appears.
					if	presence : self.loggy.debug(f"Replaced \"{K}\", \"{V}\" pair")
					else:

						self._locker_.append(K)
						self.loggy.debug(f"Putted \"{K}\", \"{V}\" pair")


				# Must be unhashable key raise.
				except	TypeError:

					self.loggy.warning(f"Failed to put unhashable key \"{K}\" in {self} KeyChest")
					return




			# Nested put. Key-value pair (K,V) will be putted to nested dictionary, that must be found
			# by following through the dictionary, that must be nested in "_inside_", with keys, that
			# packed in "nest". Boolean "mapped" value is opposite to whether keys from "nest" pack
			# might be created or not (this boolean value means if such keys must present or not).
			case ( K,V, *nest ):

				nesting		= self._inside_
				nest_root	= nest[0]


				try:

					presence = nest_root in nesting
					self.loggy.debug(f"Root key \"{nest_root}\" nesting")


				except	TypeError:

					self.loggy.warning(f"Unhashable root key \"{nest_root}\" for {self} KeyChest")
					return




				for key in nest:
					try:

						if	(next_nesting := nesting.get(key)) is not None:

							self.loggy.debug(f"Nesting key \"{key}\"")
							nesting = next_nesting


						# Nesting KeyChest with dictionaries.
						elif not mapped:

							nesting[key] = dict()
							nesting = nesting[key]
							self.loggy.debug(f"Mapped nested key \"{key}\"")


						else:
							self.loggy.warning(f"Can't nest unmapped key \"{key}\" in {self} KeyChest")
							return


					# Must be unhashable key raise.
					except	TypeError:

						self.loggy.warning(f"Failed to nest unhashable key \"{key}\" in {self} KeyChest")
						return

					# nesting value must be dict or implement get method.
					except	AttributeError:

						self.loggy.warning(f"Unnestable value \"{nesting}\" in {self} KeyChest")
						return




				if	not isinstance(nesting, dict):

					self.loggy.warning(f"Value \"{nesting}\" cannot be nested in {self} KeyChest")
					return


				try:

					# NP - Nested Presence.
					NP = K in nesting
					nesting[K] = V


					if	NP:	self.loggy.debug(f"Replaced nested \"{K}\", \"{V}\" pair")
					else:	self.loggy.debug(f"Putted nested \"{K}\", \"{V}\" pair")


				# Must be unhashable key raise.
				except	TypeError:

					self.loggy.warning(f"Failed to nest unhashable key \"{K}\" in {self} KeyChest")
					return




				# Maintaining "_locker_" list, that tracks root keys in order their appears.
				if	presence: self.loggy.debug(f"Changed root key \"{nest_root}\" nested values")
				else:

					self._locker_.append(nest_root)
					self.loggy.debug(f"Putted nested root key \"{nest_root}\"")




			case ()	: pass
			case _	:

				self.loggy.warning(f"Can't put \"{load}\" in {self} KeyChest")
				return


		# The returned value is intentionally set up to be a copy of an "_inside_" dict, with
		# keys set to be strings. The purpose of such modification is to maintain Transmutable
		# keys to be easy to read, as such dictionary, that __call__ returning, is an another way
		# just to inspect KeyChest, not to interact with it.
		return	{ str(K):V for K,V in self._inside_.items() }




	def __init__(self, *args, **kwargs):

		# Initiating KeyChest core fields first allows putting during initiation.
		self.unload()
		super().__init__(*args, **kwargs)




	def deep(self, *depth) -> Any | None :

		"""
			Deep keying into a KeyChest nestings.
			First argument will be considered as KeyChest root key, all consequent arguments are nested
			keys to go deep in KeyChest. Return nested value or None if neither root key nor any of nested
			keys doesn't exist in KeyChest.
		"""

		if	depth:

			root, *rest = depth
			self.loggy.debug(f"Diving depth {len(rest)}")


			if	(bottom := self._inside_.get(root)) is not None:


				for deep_key in rest:
					if	(bottom := bottom.get(deep_key)) is not None : continue


					self.loggy.debug(f"Deep-key \"{deep_key}\" not found")
					break
				else:
					self.loggy.debug(f"Deep-value found: \"{bottom}\"")
					return	bottom
			else:	self.loggy.debug(f"Root-key \"{root}\" not found")
		else:		self.loggy.debug(f"No depth to go deep")




	def keys(self) -> List[Hashable]:

		"""
			Classic dictionary method implementation. Returns "_locker_" list copy (as new list).
			This method along with "__getitem__" must ensure KeyChest object will be recognized
			to implement mapping protocol.
		"""

		return	list(self._locker_)




	def keysof(self, value :Any) -> List[Hashable] | List :

		"""
			Finding list of keys, that are matched with "value". The returned list of keys is ordered by
			key injection, as it is obtained from "_locker_", just like the iteration. If no match found,
			empty list will be returned and corresponding debug message will be logged.
		"""

		if	value in self._inside_.values():

			self.loggy.debug(f"Matched keys for \"{value}\" are found")
			return	[ K for K in self._locker_ if self._inside_.get(K) == value ]


		self.loggy.debug(f"No matched keys for \"{value}\" are found")
		return	list()




	def unload(self):

		"""
			Wipes "_inside_" and "_locker_" items completely by reinitiating with "_current".
			Also used as initiation by itself.
		"""

		self._inside_ = dict()
		self._locker_ = list()
		self._current = 0








	class Inspection(Transmutable):

		"""
			Producer of an elegant and easy to read string of current KeyChest content.
			The produced string is kind of "pretty print" implemented.
			Also allow logging content in any level, that must be provided (no logging by default).
		"""

		def __call__(self, level :int =None) -> str :

			self.loggy.info(f"Commencing {self._UPPER_LAYER} inspection")
			self.view = str()


			self.inspecting(log=level)
			self.loggy.debug(f"Inspection result {len(self.view)} symbols")


			return	self.view




		def inspecting(self, log, layer :dict =None, deep :int =0):

			for k,v in (_layer := layer.items() if layer else self._UPPER_LAYER) :

				_k = deep *"\t" +str(k)
				self.view += f"{_k}:\n"
				if	log : self.loggy.log(log, _k)


				if	v and isinstance(v, dict) : self.inspecting(log, v, deep +1)
				else:

					_v = (deep +1) *"\t" +str(v)
					self.view += f"{_v}\n"
					if	log : self.loggy.log(log, _v)







