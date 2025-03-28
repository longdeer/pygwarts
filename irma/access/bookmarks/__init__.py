from typing									import Literal
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.chests				import KeyChest
from pygwarts.magical.spells				import patronus
from pygwarts.irma.access					import LibraryAccess
from pygwarts.irma.access.volume			import LibraryVolume








class VolumeBookmark(KeyChest):

	"""
		irma.access core super class that serves as a dispatcher for handlers and inducers. As the library
		access implies, for every LibraryVolume object to be "accessed", or in other words to be processed,
		corresponding AccessHandler objects will do the thing. After LibraryVolume is done with processing
		it's content, corresponding AccessInducer will represent processed data. The VolumeBookmark object
		is the way AccessHandler and AccessInducer objects will communicate with VolumeBookmark. By
		declaring right under corresponding LibraryVolume object, VolumeBookmark will be able to put itself
		to it in two ways:
			1. as VolumeBookmark: "bookmark" mapping to ensure it might be accessed from LibraryVolume;
			2. as VolumeBookmark.trigger: VolumeBookmark mapping to allow access by it's trigger in text.
		It is also possible to declare VolumeBookmark under the toppest LibraryAccess object. In this case
		it will put itself as VolumeBookmark: "bookmark" mapping and will be reachable to every
		LibraryVolume in current library, so it will be named a common bookmark. When the access to library
		will occur, every LibraryVolume object will read the files it is points to and exposes every line
		of text it encounters. By the field "trigger", that must contain a string, every assigned volume's
		or common VolumeBookmark might be triggered, if it's "trigger" string is a substring of line being
		processing. After such triggering, method "update" will be invoked for every triggered
		VolumeBookmark, which means AccessHandler objects will be invoked. At the end of the access, method
		"view" might be invoked to, in turn, invoke every AccessInducer object.
	"""

	trigger	:str

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		if	isinstance(bookmark_trigger := getattr(self, "trigger", None), str):
			if	self.library_assignment(bookmark_trigger, getattr(self, "_UPPER_LAYER", None)): return
		else:	self.loggy.debug(f"Incomplete bookmark")


		self.loggy.info(f"Bookmark {self} not assigned to library")




	def library_assignment(	self,
							trigger	:str,
							liblink	:LibraryAccess | LibraryVolume | None
						)-> Literal[True] | None :

		"""
			Helper method that checks "liblink" object to be either LibraryVolume or LibraryAccess type.
			For a LibraryVolume it will put itself in two ways:
				1. as VolumeBookmark: "bookmark" mapping to ensure it might be accessed from LibraryVolume;
				2. as VolumeBookmark.trigger: VolumeBookmark mapping to allow access by it's trigger in text.
			For a LibraryAccess it will put itself as VolumeBookmark: "bookmark" mapping so it will be
			reachable to every LibraryVolume in current library. Returns True in case of successful
			assignment, or None otherwise.
		"""

		match liblink:
			case LibraryAccess():

				liblink(self, "bookmark")
				self.loggy.debug(f"Assigned to library {liblink}")
				return	True


			case LibraryVolume():

				liblink(self, "bookmark")
				liblink(trigger, self)
				self.loggy.debug(f"Assigned to volume {liblink}")
				return	True


			case None	: self.loggy.debug("Upper layer not found")
			case _		: self.loggy.debug("Invalid upper layer")




	def update(self, line :str, volume :LibraryVolume):

		"""
			Helper method, that accepts current "line" being processing and current LibraryVolume "volume"
			object being processing, and invokes AccessHandler objects, that was registered to current
			VolumeBookmark object, passing both arguments. As every AccessHandler invocation is putted
			in try block, any Exception caught will be logged and skipped. Doesn't suppose to return
			anything.
		"""

		for handler in self.keysof("handler"):

			try:	handler(line, volume)
			except	Exception as E : self.loggy.debug(f"{handler} failed due to {patronus(E)}")




	def view(self, volume :LibraryVolume) -> str | None :

		"""
			Helper method, that accepts current LibraryVolume "volume" object being processing, and invokes
			AccessInducer objects, that was registered to current VolumeBookmark object, passing "volume".
			Assumes that every AccessInducer will result a string. Will collect and concatenate all
			AccessInducer result strings and return it. Returns None if no string fetched from AccessInducer
			objects. As every AccessInducer invocation is putted in try block, any Exception caught will be
			logged and skipped.
		"""

		current_view = str()

		for inducer in self.keysof("inducer"):

			# Inducers must take volume and use it to index in it to maintain it's recaps/counters
			try:	current_view += inducer(volume)
			except	Exception as E : self.loggy.debug(f"{inducer} failed due to {patronus(E)}")


		if		current_view: return current_view
		else:	self.loggy.debug(f"No view volume {volume}")







