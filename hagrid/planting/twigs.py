from pathlib								import Path
from typing									import NoReturn
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.hagrid.thrivables				import Tree








class TwigProbe(Transmutable):

	"""
		hagrid.planting object, that represents simulation of catalog creation operation.
		The purpose of this object is to indicate the intention of real folders operations, before they
		will really affect the file system. There two things that this object __call__ actually does: logging
		probe info message if target folder doesn't exist (to be created), and logging debug message otherwise
		(already exist and no creation need).
		If a source folder doesn't exist at the start of operation, e.g. that might happen when processing
		some not small catalogs in multi-bough Flourish, the process will be stopped with corresponding log.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current operation source folder;
			bough	- Path object that represents current operation destination parent folder.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, twig :Path, bough :Path):


		if	not twig.is_symlink():
			target = bough.joinpath(twig.name)


			if	twig.is_dir():

				if	not target.is_dir() : origin.loggy.info(f"Twig \"{target}\" probe")
				else:	origin.loggy.debug(f"Passed probe \"{target}\"")
			else:		origin.loggy.debug(f"Branch \"{twig}\" not located")
		else:			origin.loggy.debug(f"Symbolic twig skipped")








class TwigThrive(Transmutable):

	"""
		hagrid.planting object, that represents catalog creating operation.
		The process consist of prechecking the existence of target folder and creating the target folder
		with all parents, in case of it doesn't exist (no recreation of already existent folders).
		The catalog creation function that used (Path.mkdir) doesn't preserve source file meta data.
		No return value for __call__ is assumed, also no handling for any Exception, that might be raised
		by catalog creation function, that must be handled by invoker object, e.g. Bloom object.
		If a source folder doesn't exist at the start of operation, e.g. that might happen when processing
		some not small catalogs in multi-bough Flourish, the process will be stopped with corresponding log.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			twig	- Path object that represents current operation source folder;
			bough	- Path object that represents current operation destination parent folder.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, twig :Path, bough :Path) -> None | NoReturn :


		if	not twig.is_symlink():
			target = bough.joinpath(twig.name)


			if	twig.is_dir():
				if	not target.is_dir():


					target.mkdir(parents=True)
					origin.loggy.info(f"Thrived twig \"{target}\"")
				else:
					origin.loggy.debug(f"Passed twig \"{target}\"")
			else:	origin.loggy.debug(f"Branch \"{twig}\" not located")
		else:		origin.loggy.debug(f"Symbolic twig skipped")







