from typing									import Any
from typing									import Callable
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import tentaclifors








class Transmutation(Transmutable):

	"""
		Pygwarts core class, that serves as a super class for one layer decorators (no arguments).
		For Transmutable objects decoration means transmutation, because actual decoration here means
		taking decorated class and produce another Transmutable class. with some modifications. The
		name of such object must remain the same as original decorated class, and this is achieved
		in declaration of actual decorator. Every Transmutation subclass must consist of a callable
		"_mutable_chain_injection" that will accept the only argument - the decorated Transmutable class.
		It must declare a new Transmutable class that inherits from the argument class. This new class
		must encompass all desired "transmutations" and must be returned by "_mutable_chain_injection".
		The decorated entity might be either a Transmutable, or any other type which will be treated
		special way that will lead to an Exception raise for the upper layer. For a Transmutable, as
		it might be another Transmutation, there is another special field "_CHAIN_LAYER_HOOK", that
		serves as a trigger and buffer at the same time. As the process of decorating by a class is
		handled by decorator __init__, it accepts the only positional argument "mutable_layer", which
		represents the decorated entity. If "mutable_layer" was successfully hooked by "_MUTABLE_CHAIN_HOOK"
		it is passed as a super class argument to "_mutable_chain_injection", that must be declared for
		current decorator, and the result Transmutable will be stored in "_CHAIN_LAYER_HOOK". Thus for
		another Transmutation that is happen to be a decorator for such decorator, the first thing to
		happen is to check "_CHAIN_LAYER_HOOK", so the Transmutable from the last "transmutation" that
		will be found there will be once again, but now for another decorator that decorated last decorator,
		passed as argument to "_mutable_chain_injection" that must be declared for this decorator and putted
		to it's own "_CHAIN_LAYER_HOOK", so decorating of decorators might appear any number of times. The
		final phase for Transmutation is the upper layer Transmutable phase two, when such Transmutation,
		after described above "transmutations" of decorated layers, or it's better say the final Transmutable
		class, will be instantiated with it's upper layer as an argument. This process is handled by __call__
		method and it is only goes for the "_CHAIN_LAYER_HOOK" content, as it must store that final
		Transmutable class. The process of mutable chain initiation for Transmutation schematically:

												->		decorator1.__init__(
							@decorator1			->			decorator2.__init__(
							@decorator2			->				Transmutable
							Transmutable		->			)
												->		).__call__(upper_layer_link)

		After initiation the upper layer will have transmutated member with the name of the original
		decorated class. The behavior of such object will solely depend on decorators implementation,
		but the only rule to keep in mind is the calling order top-down again, so for __call__ schematically:

					 ->	decorator1:
		@decorator1	 ->		__call__:
		@decorator2	 ->			super().__call__() ->	decorator2:
		Transmutable ->										__call__:
					 ->											super().__call__() -> Transmutable: __call__
	"""


	_CHAIN_LAYER_HOOK	= True


	def __init__(self, mutable_layer :Transmutable):

		if	callable(getattr(self, "_mutable_chain_injection", None)):
			match (mutation := getattr(mutable_layer, "_CHAIN_LAYER_HOOK", False)):


				# This case considers decorated "mutable_layer" is another Transmutation that wrapped it's
				# "mutable_layer" Transmutable in it's "_CHAIN_LAYER_HOOK".
				case type() if hasattr(mutation, "_MUTABLE_CHAIN_HOOK"):

					self._CHAIN_LAYER_HOOK = self._mutable_chain_injection(mutable_layer._CHAIN_LAYER_HOOK)
					return


				# Following two cases in charge for Decorated "mutable_layer" is another Transmutation that
				# tried to wrap not Transmutable class and did set it's "_CHAIN_LAYER_HOOK" to None, so
				# during mutable chain initiation TypError will be raised; decorated "mutable_layer" must
				# be inspected further.
				case None:

					self._CHAIN_LAYER_HOOK = None
					return


				case _: pass


			# At this point decorated "mutable_layer" must be either a Transmutable or not. If it is
			# Transmutable, it might be either the final point where decoration was started, or it might
			# also be ControlledTransmutation decorator, which differs from Transmutation as it doesn't
			# have additional final step for mutable chain initiation only, but return by it's initiation
			# transmutated Transmutable class. So for Transmutation the "mutable_layer" trasnmutation
			# will be stored in it's "_CHAIN_LAYER_HOOK" for either it's __call__ or other decorator.
			if	isinstance(mutable_layer, type) and getattr(mutable_layer, "_MUTABLE_CHAIN_HOOK", None):

				self._CHAIN_LAYER_HOOK = self._mutable_chain_injection(mutable_layer)
				return


		# This final point ensures either current or other decorator will be notified to raise TypeError
		# as current "_CHAIN_LAYER_HOOK" will be set to "None" as a trigger. This is the handle for
		# situations when "mutable_layer" is not Transmutable or when decorator implementation doesn't
		# have "_mutable_chain_injection".
		self._CHAIN_LAYER_HOOK = None




	def __call__(self, upper_layer_link :Transmutable =None, **kwargs)-> Transmutable :

		if		self._CHAIN_LAYER_HOOK is None: raise TypeError("Not Transmutable transmutation")
		return	self._CHAIN_LAYER_HOOK(upper_layer_link, **kwargs)








class ControlledTransmutation(Transmutable):

	"""
		Pygwarts core class, that serves as a super class for two layers decorators (with arguments).
		The logic behind such decorator the same as for Transmutation, except one thing which allows
		arguments to be included to transmutation only - the decorator initiation shift.
		For ControlledTransmutation, __init__ must handle arguments. By default it takes all positional
		arguments and store it to a "layer_args" field, then in takes all keyword arguments and creates
		fields mapping. Those arguments-fields access might be provided in "_mutable_chain_injection"
		callable, that must handles transmutation of decorated class. Extracting those arguments-fields
		to a "_mutable_chain_injection" namespace variable will grant use of it for transmutated class.
		As this logic is very simple and prone to some misleading about which arguments are positional
		and which are key-word only, and as the actual implementation of any ControlledTransmutation
		decorator must rely on this, it is the best practice to implement dissent __init__ for every
		ControlledTransmutation decorator, to ensure maintaining of neccessary arguments manipulations.
		For ControlledTransmutation, __call__ will be a part of initiation where it accepts the decorated
		entity as "mutable_layer" and considers it's transmutation - whether it is Transmutable to proceed
		with or it is not Transmutable to stop the initiation. Basically ControlledTransmutation __call__
		is a Transmutation __init__, except for ControlledTransmutation it is a termination of initiation
		so it must return transmutated class or make a signal for upper layer that not a Transmutable
		object was encountered, so in this case it returns special function which when invoked will raise
		TypeError with corresponding message. It is complied to a mutable chain initiation, which for every
		hooked Transmutable will try to initiate it, so if for Transmutation there is __call__ that handles
		exactly this situation and might raise TypeError right away, ControlledTransmutation must return
		something in it's __call__, and then that something will be invoked in mutable chain initiation,
		so ControlledTransmutation either returns transmutated Transmutable or a callable which will
		raise TypeError upon it's call.
	"""

	def __init__(self, *args, **kwargs):


		self.layer_args = args
		for k,v in kwargs.items(): setattr(self, k,v)


	def __call__(self, mutable_layer :Transmutable) -> Transmutable | Callable[[Any],TypeError] :

		if	callable(getattr(self, "_mutable_chain_injection", None)):
			match (mutation := getattr(mutable_layer, "_CHAIN_LAYER_HOOK", False)):

				# This case considers decorated "mutable_layer" is another Transmutation that wrapped it's
				# "mutable_layer" Transmutable in it's "_CHAIN_LAYER_HOOK".
				case type() if hasattr(mutation, "_MUTABLE_CHAIN_HOOK"):
					return	self._mutable_chain_injection(mutable_layer._CHAIN_LAYER_HOOK)


				# Following two cases in charge for Decorated "mutable_layer" is a Transmutation that
				# tried to wrap not Transmutable class and did set it's "_CHAIN_LAYER_HOOK" to None,
				# so during mutable chain initiation TypError must be raised, or decorated "mutable_layer"
				# might be any other Transmutable class. In both cases "mutable_layer" must be inspected
				# further, so it is up to it's "_MUTABLE_CHAIN_HOOK".
				case None:	pass
				case _:		pass


			# At this point decorated "mutable_layer" must be either a Transmutable or not. If it is
			# Transmutable, it might be either the final point where decoration was started, or it might
			# also be another ControlledTransmutation decorator, which returns transmutated Transmutable.
			if	isinstance(mutable_layer, type) and getattr(mutable_layer, "_MUTABLE_CHAIN_HOOK", None):
				return	self._mutable_chain_injection(mutable_layer)


		# This final point ensures either current or other decorator issues the raise of TypeError for
		# the upper layer by returning special callable. This is the handle for situations when
		# "mutable_layer" is not Transmutable or when decorator implementation doesn't have
		# "_mutable_chain_injection".
		return	tentaclifors







