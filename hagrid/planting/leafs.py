from pathlib								import Path
from shutil									import copy2
from shutil									import copyfile
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.hagrid.thrivables				import Tree








class LeafProbe(Transmutable):

	"""
		hagrid.planting object, that represents simulation of file copying operation.
		The purpose of this object is to indicate the intention of real file operations, before they will
		really affect the file system. There two things that this object __call__ actually does: logging
		debug message if target parent folder doesn't exist (to be created beforehand) and logs info message
		for source file probe.
		If a source file doesn't exist at the start of operation, e.g. that might happen when processing
		some not small files in multi-bough Flourish, the process will be stopped with corresponding log.
		This object __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current operation source file;
			bough	- Path object that represents current operation destination parent folder.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

		if	not leaf.is_symlink():

			target	= bough.joinpath(leaf.name)
			shoot	= target.parent


			if	leaf.is_file():
				if	not shoot.is_dir() : origin.loggy.debug(f"Bough \"{shoot}\" probe")


				origin.loggy.info(f"Leaf \"{target}\" probe")
			else:
				origin.loggy.debug(f"Branch \"{leaf}\" not located")
		else:	origin.loggy.debug(f"Symbolic leaf skipped")








class LeafGrowth(Transmutable):

	"""
		hagrid.planting object, that represents file copying operation.
		The whole process divided to 2 stages: first is the check for target file path folder and
		creating it if it doesn't exist, second is the actual copying.
		The copy function that used (shutil.copyfile) doesn't preserve source file meta data.
		No return value for __call__ is assumed, also no handling for any Exception, that might be raised
		by copy function or by parent directory creation (Path.mkdir) function, that must be handled
		by invoker object, e.g. Bloom object.
		If a source file doesn't exist at the start of operation, e.g. that might happen when processing
		some not small files in multi-bough Flourish, the process will be stopped with corresponding log.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current operation source file;
			bough	- Path object that represents current operation destination parent folder.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

		if	not leaf.is_symlink():

			target	= bough.joinpath(leaf.name)
			shoot	= target.parent


			if	leaf.is_file():
				if	not shoot.is_dir() : shoot.mkdir(parents=True)


				copyfile(leaf, target, follow_symlinks=False)
				origin.loggy.info(f"Grown leaf \"{target}\"")
			else:
				origin.loggy.debug(f"Branch \"{leaf}\" not located")
		else:	origin.loggy.debug(f"Symbolic leaf skipped")








class LeafMove(Transmutable):

	"""
		hagrid.planting object, that represents file moving operation.
		The whole process divided to 3 stages: first is the check for target file path folder and
		creating it if it doesn't exist; second is the file copying and third is removing of the source
		file in cause of successful copying.
		It is important to note, that copy function that used (shutil.copyfile) doesn't preserve source
		file meta data, and must raise Exception in case of any failure of copying, cause the condition
		to remove source file considers success of previous operation the existence of target file, not
		matter it's modification time, so source might be removed.
		No return value for __call__ is assumed, also no handling for any Exception, that might be raised
		by copy function or by parent directory creation (Path.mkdir) function, or by source removing
		(Path.unlink) function that must be handled by invoker object, e.g. Bloom object.
		If a source file doesn't exist at the start of operation, e.g. that might happen when processing
		some not small files in multi-bough Flourish, the process will be stopped with corresponding log.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current operation source file;
			bough	- Path object that represents current operation destination parent folder.
		IMPORTANT: the unit tests for this object must be inspected for implementation complines,
		cause some tests directly imitates this object behavior.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

		if	not leaf.is_symlink():

			target	= bough.joinpath(leaf.name)
			shoot	= target.parent


			if	leaf.is_file():
				if	not shoot.is_dir() : shoot.mkdir(parents=True)


				copyfile(leaf, target, follow_symlinks=False)


				if	target.is_file():

					leaf.unlink()
					origin.loggy.info(f"Moved leaf \"{target}\"")
				else:
					origin.loggy.info(f"Leaf \"{target}\" move failed")
			else:	origin.loggy.debug(f"Branch \"{leaf}\" not located")
		else:		origin.loggy.debug(f"Symbolic leaf skipped")








class LeafClone(Transmutable):

	"""
		hagrid.planting object, that represents operation of copying a file with it's meta data.
		The whole process divided to 3 stages: first is the check for target file path folder and
		creating it if it doesn't exist, second is the actual copying of file and it's meta data,
		third is optional and occurs when the second stage causes Exception raise.
		The copy function that used (shutil.copy2) will try to preserve source file meta data, but this
		process might fail, for example, when doing it between different file systems. In such cases the
		file will be first copied and then file meta data change will be given a try. If this process
		will lead to Exception, like any other option that will cause Exception, it will be tried to be
		handled in place. The target file existent will be considered and it's modification time will be
		compared with modification time before start of operation (if existed for that moment). If target
		file exist and it's modification time greater than value at the start (which defaulted to 0) the
		planting considered half-successful and corresponding info message will be logged, that it is
		grown instead of moved. If any of the above conditions not met, operation considered failed and
		such Exception will be propagated to the invoker, e.g. Bloom object.
		No return value for __call__ is assumed.
		If a source file doesn't exist at the start of operation, e.g. that might happen when processing
		some not small files in multi-bough Flourish, the process will be stopped with corresponding log.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current operation source file;
			bough	- Path object that represents current operation destination parent folder.
		IMPORTANT: the unit tests for this object must be inspected for implementation complines,
		cause some tests directly imitates this object behavior.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

		if	not leaf.is_symlink():

			target	= bough.joinpath(leaf.name)
			shoot	= target.parent
			state	= target.stat().st_mtime if target.is_file() else 0


			if	leaf.is_file():
				if	not shoot.is_dir() : shoot.mkdir(parents=True)


				try:

					copy2(leaf, target, follow_symlinks=False)
					origin.loggy.info(f"Cloned leaf \"{target}\"")


				except:
					if	target.is_file():
						if	state <target.stat().st_mtime:

							origin.loggy.info(f"Leaf \"{target}\" cloning stuck, grown instead")
							return
					raise
			else:	origin.loggy.debug(f"Branch \"{leaf}\" not located")
		else:		origin.loggy.debug(f"Symbolic leaf skipped")








class LeafPush(Transmutable):

	"""
		hagrid.planting object, that represents operation of moving a file with it's meta data.
		The whole process divided to 4 stages: first is the check for target file path folder and
		creating it if it doesn't exist; second is the actual moving of file and it's meta data; third is
		the removing of the source file in cause of successful copying and fourth is optional and occurs
		when the second or third stages causes Exception raise.
		The copy function that used (shutil.copy2) will try to preserve source file meta data, and must
		raise Exception in case of any failure of copying, cause the condition to remove source file
		considers success of previous operation the existence of target file, not matter it's modification
		time, so source might be removed. Eventually the process described might fail, for example, when
		doing it between different file systems. In such cases the file will be first copied and then
		file meta data change will be given a try. If the process of copying file with meta data will lead
		to Exception, like any other option that will cause Exception, it will be tried to be handled
		in place. The target file existent will be considered and it's modification time will be compared
		with modification time before start of operation (if existed for that moment). If target file exist
		and it's modification time greater than value at the start (which defaulted to 0) the planting
		considered half-successful and corresponding info message will be logged, that it is grown instead
		of moved. If any of the above conditions not met, operation considered failed and such Exception
		will be propagated to the invoker, e.g. Bloom object.
		No return value for __call__ is assumed.
		If a source file doesn't exist at the start of operation, e.g. that might happen when processing
		some not small files in multi-bough Flourish, the process will be stopped with corresponding log.
		This object's __call__ accepts arguments that implement the "planting interface":
			origin	- Tree object that is currently planting, used especially for emitting logging messages;
			sprout	- string that represents the current source root;
			branch	- Path object that represents current source folder;
			leaf	- Path object that represents current operation source file;
			bough	- Path object that represents current operation destination parent folder.
		IMPORTANT: the unit test for this object must be inspected for implementation complines,
		cause some tests directly imitates this object behavior.
	"""

	def __call__(self, origin :Tree, sprout :str, branch :Path, leaf :Path, bough :Path):

		if	not leaf.is_symlink():

			target	= bough.joinpath(leaf.name)
			shoot	= target.parent
			state	= target.stat().st_mtime if target.is_file() else 0


			if	leaf.is_file():
				if	not shoot.is_dir() : shoot.mkdir(parents=True)


				try:

					copy2(leaf, target, follow_symlinks=False)


					if	target.is_file() and leaf.stat().st_mtime == target.stat().st_mtime:

						leaf.unlink()
						origin.loggy.info(f"Pushed leaf \"{target}\"")
					else:
						origin.loggy.info(f"Leaf \"{target}\" push failed")


				except:
					if	target.is_file():
						if	state <target.stat().st_mtime:

							origin.loggy.info(f"Leaf \"{target}\" pushing stuck, grown instead")
							return
					raise
			else:	origin.loggy.debug(f"Branch \"{leaf}\" not located")
		else:		origin.loggy.debug(f"Symbolic leaf skipped")







