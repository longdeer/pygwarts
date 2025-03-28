from pathlib								import Path
from shutil									import rmtree
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.hagrid.thrivables				import Tree








class TrimProbe(Transmutable):

	"""
		hagrid.planting object, that represents simulation of a folder/file removing operation.
		The purpose of this object is to indicate the intention of real operations, before they will really
		affect the file system.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			sprig	- Path object that represents current operation target folder/file;
			bough	- Path object that represents current operation destination parent folder.
		There are three variants for this object __call__ to do:
			1. "sprig" is a folder and corresponding probe message will be logged;
			2. "sprig" is a file and corresponding probe message will be logged;
			1. "sprig" neither a folder nor file and corresponding probe message will be logged.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, sprig :Path, bough :Path):

		if	not sprig.is_symlink():

			if	sprig.is_dir()		: origin.loggy.info(f"Twig \"{sprig}\" trim probe")
			elif(sprig.is_file())	: origin.loggy.info(f"Leaf \"{sprig}\" trim probe")
			else					: origin.loggy.warning(f"Bad sprig \"{sprig}\" to probe")
		else						: self.loggy.debug("Symbolic sprig skipped")








class SprigTrimmer(Transmutable):

	"""
		hagrid.planting object, that represents folder/file removing operation.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			sprig	- Path object that represents current operation target folder/file;
			bough	- Path object that represents current operation destination parent folder.
		As sprig can be either destination folder or file, it's type will be determined by __call__. Will be
		used shutil.rmtree for folders and Path.unlink method for files. If any other "sprig" time occurred,
		only corresponding warning message will be logged.
		No return value for __call__ is assumed, also no handling for any Exception, that might be raised
		by "rmtree" or by "Path.unlink", that must be handled by invoker object, e.g. Bloom object.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, sprig :Path, bough :Path):


		if	not sprig.is_symlink():
			if	sprig.is_dir():


				rmtree(sprig)
				origin.loggy.info(f"Trimmed twig \"{sprig}\"")


			elif(sprig.is_file()):

				sprig.unlink()
				origin.loggy.info(f"Trimmed leaf \"{sprig}\"")
			else:
				origin.loggy.warning(f"Bad sprig \"{sprig}\" to trim")
		else:	self.loggy.debug("Symbolic sprig skipped")







