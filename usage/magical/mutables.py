from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import Transmutation
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.irma.contrib								import LibraryContrib








class NewTransmutable(Transmutable):	# Inherit from Transmutable to initiate mutable chain.
	class loggy(LibraryContrib):					# Append logger (optional, name "loggy" might be altered
													# but mutbale chain will anyway assign all LibraryContrib
		handler		= "logger file path (optional)"	# objects as "loggy" member during initiation or when
		init_name	= "mutable (optional)"			# the first "loggy" member access will happen.

	def __call__(self, *args, **kwargs):	# __call__ is the main method for Transmutable, most pygwarts
		print(args, kwargs)					# objects will rely on it's implementation.

	# Declare nested objects to be a part of mutable chain, every nested object will have access to
	# members of every upper layer by the use of "escalation" algorithm.
	class NestedTransmutable(Transmutable):

		# It is possible to attach different loggers for nested objects. Any LibraryContrib object will
		# be propagated to the most upper layer, unless it has it's own logger.
		#
		# Important note:
		# This feature has many particularities. Declaring more than one LibraryContrib objects under
		# the same Transmutable will result the single "loggy" member, so all other LibraryContrib
		# objects will be lost in namespace. Also it is bad practice to declare all LibraryContrib
		# object with "loggy" name. The best way to use multiple loggers is to declare all
		# LibraryContrib objects with different names.
		class another_loggy(LibraryContrib):

			handler		= "logger file path (optional)"
			init_name	= "nested (optional)"








# Transmutation is a decorator for Transmutable objects. It takes decorated Transmutable class
# and extends it's functionality the way it is usually works in Python. The only two conditions
# must be satisfied:
#	- Transmutation must implement method "_mutable_chain_injection" in which it will have
#	declaration of a new Transmutable, and
#	- this new Transmutable must inherit from a call to special function "geminio", which
#	will ensure mutable chain injection of a transmutation will go smooth.
class NewTransmutation(Transmutation):
	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :
		class Injection(geminio(layer)):
			def __call__(self, *args, **kwargs):
				return f"transmuted: {super().__call__(*args, **kwargs)}"
		return	Injection


# Transmutation decorators to be used during declaration. Following decoration will result
# "transmuted: 42" return value when DecoratedTransmutable instance will be called with subject=42.
@NewTransmutation
class DecoratedTransmutable(Transmutable):
	def __call__(self, subject :object) -> str :
		return str(subject)








# ControlledTransmutation is the decorator that accepts arguments or keyword arguments. Works the very
# same way as Transmutation, except localization of decorator arguments.
class NewControlledTransmutation(ControlledTransmutation):
	def __init__(self, state :str): self.state = state
	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		state = self.state	# Localization of decorator arguments

		class Injection(geminio(layer)):
			def __call__(self, *args, **kwargs):
				return f"{state}: {super().__call__(*args, **kwargs)}"
		return	Injection


# To be used during declaration the same way as Transmutation. Following decoration will result
# "number: 42" return value when DecoratedTransmutable instance will be called with subject=42.
@NewControlledTransmutation("number")
class DecoratedTransmutable(Transmutable):
	def __call__(self, subject :object) -> str :
		return str(subject)


# It is possible to stack both decorators types. The following decoration will result
# "transmuted: number: transmuted: 42" return value when DecoratedTransmutable instance
# will be called with subject=42.
@NewTransmutation
@NewControlledTransmutation("number")
@NewTransmutation
class DecoratedTransmutable(Transmutable):
	def __call__(self, subject :object) -> str :
		return str(subject)







