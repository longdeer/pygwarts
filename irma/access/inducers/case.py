from typing												import Optional
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.irma.access.volume						import LibraryVolume
from pygwarts.irma.shelve								import LibraryShelf
from pygwarts.irma.shelve.casing						import shelf_case








class InducerCase(ControlledTransmutation):

	"""
		irma.shelve.casing utility decorator variant, that integrates the core "casing" functionality into
		mutable chain, by maintaining AccessInducer output. As ControlledTransmutation class, accepts
		positional argument "link", which must be a string that represents the name of LibraryShelf
		attribute, and optional keyword-only arguments "prep" and "post", which must be "casing" handling
		callables. The key for LibraryShelf will be a string representation of current mutable chain point,
		and it will be passed along with this three accepted arguments to "shelf_case" function. In
		mutable chain acts as a mutation - takes decorated Transmutable, which must be an AccessInducer
		class which accepts LibraryVolume object as argument to be used to obtain AccessInducer original
		output, along with maintaining a LibraryVolume mapping in LibraryShelf, where current "key" will be
		mapped with "shelf_case" result value. If "shelf_case" return value is not None it will be returned.
		Otherwise returns original AccessInducer output. Despite AccessInducer must always must return
		string, this decoration doesn't restrict "post" return value, but suggests it will either return
		a string or will be passed to another object, which will return string.
	"""

	def __init__(
					self,
					link	:str,
					*,
					prep	:Optional[Callable[[str],str]]		=(lambda T	: T),
					post	:Optional[Callable[[str,str],str]]	=(lambda T,P: T),
				):

		self.link = link
		self.prep = prep
		self.post = post

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		link = self.link
		post = self.post
		prep = self.prep


		class InducerCasing(geminio(layer)):
			def __call__(self, volume :LibraryVolume) -> str :


				if	(induce := super().__call__(volume)) is not None:
					if	isinstance(mapping := getattr(self, str(link), None), LibraryShelf | dict):


						if	str(volume) not in mapping : mapping[str(volume)] = dict()
						if	(casing := shelf_case(

							induce,
							key=str(self),
							shelf=mapping[str(volume)],
							prep=prep,
							post=post,

						))	is not None:

							self.loggy.debug(f"Obtained induce casing value \"{casing}\"")
							return casing


					self.loggy.debug(f"Failed to obtain induce casing value")
					return induce


		return	InducerCasing







