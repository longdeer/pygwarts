from re										import Pattern
from typing									import List
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import flagrate
from pygwarts.irma.access					import LibraryAccess
from pygwarts.irma.access.volume			import LibraryVolume
from pygwarts.irma.access.bookmarks			import VolumeBookmark








class LibraryAnnex(Transmutable):

	"""
		pygwarts.irma helper class that represents the dispatcher of entire LibraryAccess object it
		declared under. When all LibraryVolume objects, that are mapped as "volume" in upper LibraryAccess
		KeyChest, will be accessed, the further process might be divided by two phases:
			1. Actual processing of every mapped LibraryVolume object, by full staging the "volume":
				- getting "volume" range as a verification;
				- generating lines of opened "volume" file;
				- generating responses of lines parsing with triggers compiled from bookmarks;
				- updating every corresponding bookmark by line that triggered.
		This phase also implies creating a runtime mapping of successfully processed "volumes" with
		lists of corresponding bookmarks, which will be created the way LibraryAccess's bookmarks
		(or common) will preceded LibraryVolume's bookmarks (or local).
			2. After all volumes were processed and gathered, their own "Annex" will be seeked and called,
		in order to fetch volume's annex string. After all such string will be obtained and concatenated,
		the final string will be returned.
		Returns None if either LibraryAnnex object is not a part of library or if final annex string
		length is zero.
	"""

	def __call__(self) -> str | None :


		if	isinstance(liblink := getattr(self, "_UPPER_LAYER", None), LibraryAccess):
			self.loggy.debug(f"Fetching library {liblink} annex")


			processed_volumes = {}
			common = liblink.keysof("bookmark")
			self.loggy.debug("Processing volumes")


			for volume in liblink.keysof("volume"):
				if	isinstance(inrange := volume.get_range(), Pattern):


					# Every "volume" will have it's own list of bookmarks, ordered the way common bookmarks
					# will preceed locals for proper "volume" viewing.
					currents = common + volume.keysof("bookmark")
					triggers = liblink.compile_triggers([ b.trigger for b in currents ])


					# Every "volume" will also have common bookmarks injected to be all included to be
					# handled in "volume" processing.
					for bookmark in common:

						volume(bookmark, "bookmark")
						volume(bookmark.trigger, bookmark)


					for line in volume.g_reading():
						if	inrange.match(line):

							self.loggy.debug(f"Triggering line \"{line}\"")

							for response in volume.g_triggering(line, triggers):
								if	(bookmark := volume[response]) is not None:
									bookmark.update(line, volume)


					processed_volumes[volume] = currents
					self.loggy.debug(f"Volume {volume} processed")


			self.loggy.debug("Viewing volumes")
			lib_resume = str()


			# As of Python3.7+ dictionaries are ordered, "processed_volumes" will guarantee "Annex"
			# invocation, and hence final annex string order will match the order they were declared.
			# Original design implies every volume must implement "Annex" callable, which will be
			# supplied with list of bookmarks to view and must return current volume annex string.
			for volume,bookmarks in processed_volumes.items():
				if	callable(getattr(volume, "Annex", None)):

					annex = volume.Annex(bookmarks)
					if	isinstance(annex, str): lib_resume += annex
				else:	self.loggy.debug(f"Volume {volume} annex cannot be fetched")


			self.loggy.debug(f"Library {liblink} annex {(RL := len(lib_resume))} symbol{flagrate(RL)}")


			if	RL: return lib_resume
		else:	self.loggy.debug("Library not found")








class VolumeAnnex(Transmutable):

	"""
		pygwarts.irma helper class that represents the dispatcher of a LibraryVolume object bookmarks
		viewing. Accepts a list of VolumeBookmark objects "bookmarks", that must be relevant to current
		LibraryVolume object and will be viewed in determined order, instead of order they were putted.
		For every relevant bookmark "view" method will be called and it's string results will be
		concatenated as a final string to be returned. Every other than VolumeBookmark "bookmarks"
		object, or every "view" result other than string will be skipped and reported by corresponding
		loggy message. Returns None in any other case, even if result string length is zero.
		Original design implies this object will be declared under every LibraryVolume object as "Annex".
	"""

	def __call__(self, bookmarks :List[VolumeBookmark]) -> str | None :

		if	isinstance(volume := getattr(self, "_UPPER_LAYER", None), LibraryVolume):
			self.loggy.info(f"Fetching volume {volume} annex")


			if	isinstance(bookmarks, list) and not (volume_view := str()):
				for bookmark in bookmarks:


					if	isinstance(bookmark, VolumeBookmark):
						if	callable(view := getattr(bookmark, "view", None)):


							match (current := view(volume)):
								case str() if (LC := len(current)):

									volume_view += current
									self.loggy.debug(f"{bookmark} bookmark view {LC} symbol{flagrate(LC)}")

								case None:	self.loggy.debug(f"{bookmark} view is None")
								case _:		self.loggy.debug(f"{bookmark} view is not a string")


						else:	self.loggy.debug(f"{bookmark} is not viewable")
					else:		self.loggy.debug(f"Invalid bookmark {bookmark}")


				self.loggy.debug(f"Volume {volume} annex {(LVV := len(volume_view))} symbol{flagrate(LVV)}")


				if	LVV : return volume_view
			else:	self.loggy.debug("Provided bookmarks invalid")
		else:		self.loggy.debug("Library not found")







