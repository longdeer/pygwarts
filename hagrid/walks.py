from pathlib		import Path
from typing			import List
from typing			import Tuple
from typing			import Generator
from collections	import deque
from itertools		import filterfalse








def fstree(root :str | Path) -> Generator[Tuple[Path, List[Path], List[Path]] | List, None,None] :

	"""
		hagrid core generator, that represents iterative analogue for standard library os.walk.
		Not restricted by recursion limit and uses breadth-first algorithm, so must safe some memory. Also
		"deque" as a maintainable data structure must safe some time.
		Accepts the only argument "root" which must be a string that represents the absolute path for a
		folder to start iterative "walk" with, or a corresponding Path object. In both cases a new Path
		object will be created and used. In case of invalid "root" generator yields empty list and stops.
		When valid root provided it is putted in "deque" and the "walk" will start. The breadth of the "walk"
		is achieved by popping current "deque" and pushing new Path object, that represent subfolders, to the
		left. Every popped item must be a Path object and represent "root" subfolder. Every popped item, as a
		folder, will be iterated to make two lists of it's items - list of folders and list of files. Those
		two lists will follow current subfolder as a three objects tuple that will be yielded. In any case,
		when popped item is not a Path object that represents a subfolder, or it cannot produce somehow a
		list of Path objects by invocation of it's (perhaps absent in this case) "iterdir" Path object method,
		generator will yield an empty list and continue. Thus this generator always yields.
	"""

	try:	walk	= deque([ Path(root) ])
	except:	yield	from list()
	else:

		while	walk:

			for _ in range(len(walk)):
				branch	= walk.pop()

				try:

					sprigs	= list(branch.iterdir())
					twigs	= list(filterfalse(Path.is_symlink, filter(Path.is_dir, sprigs)))
					leafs	= list(filterfalse(Path.is_symlink, filter(Path.is_file,sprigs)))
					yield	branch, twigs, leafs
					for		twig in twigs : walk.appendleft(twig)
				except:		yield list()







