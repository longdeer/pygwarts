from typing												import Any
from typing												import List
from typing												import Hashable
from typing												import Optional
from typing												import Callable
from collections.abc									import Sequence
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.magical.time_turner.timers				import mostsec
from pygwarts.irma.access.utils							import byte_size_string
from pygwarts.irma.shelve								import LibraryShelf








def shelf_case(	target	:Any,
				*,
				key		:Hashable,
				shelf	:LibraryShelf | dict,
				prep	:Callable[[Any],Any],
				post	:Callable[[Any],Any],
			)->	Any		:

	"""
		irma.shelve.casing core function for "casing", or in other words for maintaining shelves on the run.
		The idea behind this function is accepting some value "target", which is to be preprocessed some
		way, shelved and return after available postprocess. The keyword-only arguments "key" and "shelf"
		are corresponding mapping name and LibraryShelf object or dict to store "target". Before storing,
		the previous value in the "shelf" will be retrieved and preprocessed too. Assertion will be made
		for preprocessed "target" is both not None and successfully shelved. Both preprocessed "target"
		value and previous value will be passed to postprocess function and immediately returned. Any
		Exception raised on the way of returning postprocessed result will be caught and skipped, so
		None will be returned. Two last keyword-only arguments "prep" and "post" are responsible for
		preprocessing both "target" and previous values separately and postprocessing both "target" and
		previous values simultaneously. "prep" must be callable which accepts single argument, handles
		it proper way, and returns desired value to replace original value. "post" must be callable which
		accepts two arguments, current and previous values, and handles it proper way to return single
		value as a final result. "shelf" must be either LibraryShelf or a dictionary with "get" method.
	"""

	try:

		T = prep(target)
		assert T is not None


		match shelf:

			case LibraryShelf():	P = prep(shelf[key])
			case dict():			P = prep(shelf.get(key))
			case _:					return


		shelf[key] = T
		assert shelf[key] == T
		return post(T,P)


	except: return








def is_num(candidate :int|float|str) -> int | float | str | None :

	"""
		Helper function, that might be used as "prep" callable for handling numerical values. Accepts
		single argument "candidate" and performs double cast:
			1 - cast to string to exclude boolean values;
			2 - cast to float to encompass numerical values.
		If no Exception raised during double cast, it must ensure "candidate" is a numerical value, so it
		will be returned. Otherwise returns None.
	"""

	try:	float(str(candidate))
	except:	return
	else:	return candidate




def is_iterable(candidate :Sequence) -> Sequence | None :

	"""
		Helper function, that might be used as "prep" callable for handling iterable values. Accepts
		single argument "candidate" and pass it to built-in "iter" function. If not Exception raised,
		it must ensure "candidate" is iterable object, so it will be returned. Otherwise returns None.
	"""

	try:	iter(candidate)
	except:	return
	else:	return candidate








def num_diff(num1 :int|float|str, num2 :int|float|str) -> str :

	"""
		Helper function, that might be used as "post" callable for handling numerical values. Accepts
		two arguments "num1" and "num2", which must be valid numerical values. This function will put
		both arguments in built-in "eval" function in order to obtain third numerical value, as difference
		between "num1" and "num2". This difference will be converted to special string, depending on it's
		sign:
			0 <difference: (+difference);
			difference <0: (-difference).
		For zero difference special string will be empty. Returns final string that will looks like:
			num1[ (+-difference)]
		Doesn't handle any Exception.
	"""

	diff = eval(f"{num1}-{num2 if num2 is not None else 0}")
	diff = f"{' (' if str(diff).startswith('-') else ' (+'}{diff})" if diff else ""

	return f"{num1}{diff}"




def seq_diff(seq1 :Sequence, seq2 :Sequence) -> List[str] :

	"""
		Helper function, that might be used as "post" callable for handling iterable objects. Accepts
		two arguments "seq1" and "seq2", which must be valid iterable objects. This function will
		compare both objects and obtain a set of "seq1" objects that are not present in "seq2".
		As a result will construct a list from all "seq1" elements, converted to strings. For every
		"seq1" element that not present in "seq2", it's string will be marked with " (+)" to identify
		the "difference" elements. Returns final list of strings. It must be noticed, that despite this
		function may work for any type of items in "seq1" and "seq2", their comparison will be direct,
		but final list will always content string representations of "seq1", so basically this function
		implies return of modified "seq1".
	"""

	delta = set(seq1) - set(seq2 or [])
	return [ f"{item}{' (+)' if item in delta else ''}" for item in seq1 ]




def mostsec_diff(num1 :int|float|str, num2 :int|float|str) -> str :

	"""
		Helper function, that might be used as "post" callable for handling numerical values, that
		represent time in seconds. Accepts "num1" and "num2", which must be valid numerical values.
		This function will obtain a difference between values with built-in "eval". Both "num1" and
		difference will be converted by "mostsec" to special strings and concatenated to final string,
		depending on difference sign:
			0 <difference: (+difference);
			difference <0: (-difference).
		For zero difference or zero "num1" both will be represented as "0 s" (zero seconds), so
		this function will always return difference part. Doesn't handle any Exception.
	"""

	diff = eval(f"{num1}-{num2 if num2 is not None else 0}")
	left = f"{' (-' if str(diff).startswith('-') else ' (+'}"

	return f"{mostsec(num1, positive=True) or '0 s'}{left}{mostsec(diff, positive=True) or '0 s'})"




def byte_size_diff(num1 :int|float|str, num2 :int|float|str) -> str :

	"""
		Helper function, that might be used as "post" callable for handling numerical values,
		that represent size in bytes. Accepts "num1" and "num2", whuch must be valid numerical
		values. This function will obtain difference between values with built-in "eval". Both
		"num1" and difference will be converted by "byte_size_string" to special strings and
		concatenated to final string, depending on difference sign:
			0 <difference: (+difference);
			difference <0: (-difference).
		For zero difference or zero "num1" both will be represented as "0B" (zero bytes) by
		"byte_size_string" logic, so this function will always return difference part. Doesn't
		handle any Exception.
	"""

	diff = eval(f"{num1}-{num2 if num2 is not None else 0}")
	left = f"{' (-' if str(diff).startswith('-') else ' (+'}"

	return f"{byte_size_string(num1)}{left}{byte_size_string(abs(diff))})"








class ShelfCase(ControlledTransmutation):

	"""
		irma.shelve utility decorator, that integrates the core "casing" functionality into mutable chain.
		As ControlledTransmutation class, accepts positional argument "link", which must be a string that
		represents the name of LibraryShelf attribute, and optional keyword only arguments "prep" and
		"post", which must be "casing" handling callables. The key for LibraryShelf will be a string
		representation of current mutable chain point, and it will be passed along with this three
		accepted arguments to "shelf_case" function. In mutable chain acts as a mutation - takes
		decorated Transmutable and overwrites it's __call__, which must return single value to be passed
		into "shelf_case" function. If "shelf_case" function returns None, that might mean it failed to
		produce final value, original value, obtained from decorated __call__ will be returned. Otherwise
		returns any value obtained from "shelf_case" function. Returns None if decorated __call__ returns
		None. This is the general type of "casing" decorator, which might be supplied with different
		"prep" and "post" for certain aims. If "shelf_case" returns None, the state of mapping in
		LibraryShelf object is undefined. By default "prep" and "post" are callables which simply returns
		it's first argument.
	"""

	def __init__(
					self,
					link	:str,
					*,
					prep	:Optional[Callable[[Any],Any]]	=(lambda T	: T),
					post	:Optional[Callable[[Any],Any]]	=(lambda T,P: T),
				):

		self.link = link
		self.prep = prep
		self.post = post

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		link = self.link
		post = self.post
		prep = self.prep


		class ShelfCasing(geminio(layer)):
			def __call__(self, *args, **kwargs) -> Any :

				if	(target := super().__call__(*args, **kwargs)) is not None:
					if	(casing := shelf_case(

						target,
						key=str(self),
						shelf=getattr(self, str(link), None),
						prep=prep,
						post=post,

					))	is not None:

						self.loggy.debug(f"Obtained shelf casing value \"{casing}\"")
						return casing


					self.loggy.debug(f"Failed to obtain shelf casing value")
					return target


		return	ShelfCasing








class NumDiffCase(ControlledTransmutation):

	"""
		irma.shelve utility decorator, that integrates special "casing" functionality into mutable chain,
		along with obtaining of special string of difference between two numerical values. As
		ControlledTransmutation class, accepts argument "link", which must be a string that represents
		the name of LibraryShelf attribute. The key for LibraryShelf will be a string representation of
		current mutable chain point, and it will be passed along with found "shelf", "is_num" prep and
		"num_diff" post to "shelf_case" function. In mutable chain acts as a mutation - takes decorated
		Transmutable and overwrites it's __call__, which must return a numerical value to be passed into
		"shelf_case" function. If "shelf_case" function returns None, that might mean it failed to validate
		either __call__ or retrieved from LibraryShelf values, or to produce final value with "post", so
		original value, obtained from decorated __call__ will be returned. Otherwise returns a string,
		corresponding to "num_diff" function. Returns None if decorated __call__ returns None.
	"""

	def __init__(self, link :str): self.link = link
	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		link = self.link


		class NumDiffCasing(geminio(layer)):
			def __call__(self, *args, **kwargs) -> str | None :

				if	(target := super().__call__(*args, **kwargs)) is not None:
					if	isinstance(

						casing := shelf_case(

							target,
							key=str(self),
							shelf=getattr(self, str(link), None),
							prep=is_num,
							post=num_diff,
						),	str
					):
						self.loggy.debug(f"Obtained number difference string \"{casing}\"")
						return casing


					self.loggy.debug("Number difference not obtained")
					return target


		return	NumDiffCasing








class SeqDiffCase(ControlledTransmutation):

	"""
		irma.shelve utility decorator, that integrates special "casing" functionality into mutable chain,
		along with comparison of iterable objects. As ControlledTransmutation class, accepts argument
		"link", which must be a string that represents the name of LibraryShelf attribute. The key for
		LibraryShelf will be a string representation of current mutable chain point, and it will be passed
		along with found "shelf", "is_iterable" prep and "seq_diff" post to "shelf_case" function. In
		mutable chain acts as a mutation - takes decorated Transmutable and overwrites it's __call__, which
		must return an iterable to be passed into "shelf_case" function. If "shelf_case" function returns
		None, that might mean it failed to validate either __call__ or retrieved from LibraryShelf values,
		or to produce final value with "post", so original value, obtained from decorated __call__ will be
		returned. Otherwise returns a string, corresponding to "num_diff" function. Returns None if
		decorated __call__ returns None.
	"""

	def __init__(self, link :str): self.link = link
	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		link = self.link


		class SeqDiffCasing(geminio(layer)):
			def __call__(self, *args, **kwargs) -> str | None :

				if	(target := super().__call__(*args, **kwargs)) is not None:
					if	isinstance(

						casing := shelf_case(

							target,
							key=str(self),
							shelf=getattr(self, str(link), None),
							prep=is_iterable,
							post=seq_diff,
						),	list
					):
						self.loggy.debug(f"Obtained sequence difference \"{casing}\"")
						return casing


					self.loggy.debug("Sequence difference not obtained")
					return target


		return	SeqDiffCasing







