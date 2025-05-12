from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.irma.shelve					import LibraryShelf
from pygwarts.irma.shelve.casing			import shelf_case
from pygwarts.irma.shelve.casing			import is_num
from pygwarts.irma.shelve.casing			import num_diff
from pygwarts.irma.shelve.casing			import ShelfCase








# Function, that is "syntax sugar" for LibraryShelf (or dict) manipulation, that allows
# following features:
#	- maintains the key-value mapping in LibraryShelf (or dict);
#	- implements preprocessing of value;
#	- implements postprocessing of current value and value, that was stored in LibraryShelf
#	(or dict) previously.
# Following example uses "is_num" for validation and "num_diff" to produce string like this:
#	CURRENT_VALUE (+-DIFFERENCE_WITH_PREVIOUS_VALUE)
# If previous value is not stored, "num_diff" will set it to 0.
shelf_case(

	"42",							# Current value.
	key="days without incidents",	# Current key.
	shelf=LibraryShelf | dict,		# Mapping object reference.
	prep=is_num,					# Preprocessing callable.
	post=num_diff,					# PostProcessing callable.
)








# Casing decorators allows injecting shelf_case functionality into mutable chain. First and only
# positional argument for decorator must be name of the mapping attribute. "prep" and "post" might
# be omitted for simple storing current value.
@ShelfCase("SomeShelf", prep=is_num, post=num_diff)
class Doubler(Transmutable):
	class SomeShelf(LibraryShelf):	pass
	def __call__(self, number :int) -> int : return number *2







