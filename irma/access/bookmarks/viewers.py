from typing												import Any
from typing												import Optional
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.magical.spells							import flagrate
from pygwarts.irma.shelve								import LibraryShelf
from pygwarts.irma.access.volume						import LibraryVolume
from pygwarts.irma.shelve.casing						import shelf_case








class ViewWrapper(ControlledTransmutation):

	"""
		irma.access utility decorator, that serves as an instrument for text editing, which is just addition
		of a text before (header) and after (footer), specially for VolumeBookmark objects. As
		ControlledTransmutation class, accepts corresponding "header" and "footer" arguments, which must be
		strings and defaulted to empty strings, in case only one is needed. In mutable chain acts as a
		mutation - takes decorated Transmutable, which must be a VolumeBookmark class with "view" method
		defined, and overwrites it to return wrapped string. Returns final string, if super.view returns
		string, or None otherwise, as super.view must do. If "view" not found as decorated Transmutable
		class member, no mutation will happen and original Transmutable will be propagated. Doesn't handles
		any Exceptions, only explicitly converts header" and "footer" to strings at initiation time and
		once again in decoration's interpolation.
	"""

	def __init__(self, header :str =str(), footer :str =str()):

		self.header = str(header)
		self.footer = str(footer)

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		header = self.header
		footer = self.footer


		if	hasattr(layer, "view"):
			class ViewWrapping(geminio(layer)):

				def view(self, volume :LibraryVolume) -> str | None :
					if	isinstance(current_view := super().view(volume), str):

						final_value = f"{header}{current_view}{footer}"
						vlen = len(final_value)
						self.loggy.debug(f"Wrapped view now {vlen} symbol{flagrate(vlen)}")


						return	final_value


					self.loggy.debug("View to wrap not found")
			return	ViewWrapping
		return		layer








class ViewCase(ControlledTransmutation):

	"""
		irma.shelve utility decorator, that integrates the core "casing" functionality into mutable chain,
		by maintaining VolumeBookmark "view" method return. As ControlledTransmutation class, accepts
		positional argument "link", which must be a string that represents the name of LibraryShelf
		attribute, and optional keyword only arguments "prep" and "post", which must be "casing" handling
		callables. The key for LibraryShelf will be a string representation of current mutable chain point,
		and it will be passed along with this three accepted arguments to "shelf_case" function. In
		mutable chain acts as a mutation - takes decorated Transmutable, which must be a VolumeBookmark
		class with "view" method defined, and overwrites it to pass it's returned string value to
		"shelf_case" function. If "shelf_case" return value is not None it will be returned. Otherwise
		returns original "view" string. Returns None if overwritten "view" returns None. Despite "view"
		always must return string, this decoration doesn't restrict "post" return value, but suggests
		it will either return a string or will be passed to another object, which will return string.
	"""

	def __init__(
					self,
					link	:str,
					*,
					prep	:Optional[Callable[[str],str]]	=(lambda T	: T),
					post	:Optional[Callable[[str],str]]	=(lambda T,P: T),
				):

		self.link = link
		self.prep = prep
		self.post = post

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		link = self.link
		post = self.post
		prep = self.prep


		if	hasattr(layer, "view"):
			class ViewCasing(geminio(layer)):

				def view(self, volume :LibraryVolume) -> Any | None :
					if	isinstance(current_view := super().view(volume), str):
						if	isinstance(mapping := getattr(self, str(link), None), LibraryShelf | dict):


							if	str(volume) not in mapping : mapping[str(volume)] = dict()
							if	(casing := shelf_case(

								current_view,
								key=str(self),
								shelf=mapping[str(volume)],
								prep=prep,
								post=post,

							))	is not None:

								self.loggy.debug(f"Obtained view casing value \"{casing}\"")
								return casing


						self.loggy.debug("View casing value not obtained")
						return current_view


					self.loggy.debug("View to case not found")
			return	ViewCasing
		return		layer







