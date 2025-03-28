from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.chests				import Chest
from pygwarts.magical.chests				import KeyChest








# Chest is a Transmutable class, that also serves as a container for another Transmutable objects,
# implementing "list" class functionality. When Chest is used as super class, it must be accounted,
# that it's __call__ not the subject to overwrite.
class Container(Chest): pass
container = Container()
container(Transmutable())		# Appends Transmutable object to container.
container(42)					# Doesn't append not Transmutable object to container.
container[0] = Transmutable()	# Change Transmutable at index to another Transmutable.
container[0] = 42				# Value at index will not changed.
container.index(Transmutable())	# Returns the first occurrence index of Transmutable object.








# KeyChest is a Transmutable class, that also servers as a dictionary for any objects type, implementing
# "dict" class functionality. As "dict" it can only accept hashable objects as keys. Unlike "dict"
# when KeyChest used to map or indexed with an unhashable key, there will be no TypeError exception,
# only WARNING level log message. Unlike "dict" when KeyChest an absent key, there will be no KeyError
# and log messages, only None will be returned. The insertion order of mappings is always guaranteed.
class Mapper(KeyChest): pass
mapper = Mapper()
mapper[Transmutable()] = Transmutable()
mapper[Transmutable()] = 42
mapper[42] = Transmutable()
mapper[42] = 42
mapper(4,5, 1,2,3, mapped=False)		# Makes { 1: { 2: { 3: { 4: 5 }}}} in KeyChest.
mapper.deep(1,2,3,4)					# Returns 5 from KeyChest.
mapper.Inspection(20)					# Returns string representing KeyChest structure (also logs INFO).
mapper()								# Returns a dictionary copy of KeyChest structure.
mapper.keysof(42)						# Returns list of keys that mapped with 42.
mapper.unload()							# Makes KeyChest empty.







