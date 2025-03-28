







def patronus(spell :Exception) -> str :

	"""
		Helper function that accepts Exception and provide pretty formatted message.
		P.S.: it must be "excepto_patronus", but in terms of conciseness it's just "patronus".
	"""

	return	f"{spell.__class__.__name__}: {spell}" if isinstance(spell, Exception) else str(spell)








def geminio(layer :type) -> type :

	"""
		Utility function that accepts Transmutable type class and declares a new class, that inherits from
		first one and forces it's self name to mimic the first one's, so the returned class is like a twin.
	"""

	class Transmute(layer):
		def __init__(self, *args, **kwargs):

			self.__class__.__name__ = layer.__name__
			super().__init__(*args, **kwargs)


	return	Transmute








def tentaclifors(*args, **kwargs) -> TypeError :

	"""
		Utility function that serves as a tool for ControlledTransmutation decorator to notify it's upper
		layer, or it's caller, about mutable chain initiation violation. That means every time in mutable
		chain initiation ControlledTransmutation class encounter not Transmutable class, this function will
		be returned by that ControlledTransmutation class, and as it is must be mandatory supplied with
		"_MUTABLE_CHAIN_HOOK" set to True, and it is not a class, it will be propagated to the very top
		layer, or caller, instead of used in mutable chain initiation.
	"""

	raise TypeError("Not Transmutable transmutation")

tentaclifors._MUTABLE_CHAIN_HOOK = True








def flagrate(counter :int | float | str) -> str :

	"""
		Utility function that returns either letter "s" or an empty string, depending on "counter".
		Basically this function upon calling with some quantity, allows to decide whether some
		string should be used in plural form or not. Argument "counter" must be of any numeric type,
		or in other words any value that if taken as an absolute value after float conversion will
		be legal for comparison with 1. All floating point "counter" values are plural by default.
		If "counter" is invalid, empty string will be returned.
	"""

	match counter:

		case float():	return "s"
		case int():		return "s" if abs(counter) != 1 else ""
		case str():

			try:	plural = abs(float(counter))
			except:	return str()
			else:	return "s" if "." in counter or plural != 1 else ""
		case _:		return str()








class Evanesco:

	""" Special magic object with spell that allows bypassing "loggy". """

	def vanishing(self, *args, **kwargs):	return NotImplemented
	def __getattribute__(self, attr :str):	return super().__getattribute__("vanishing")

evanesce = Evanesco()








def wingardium_leviosa(caller :object, attr :str, value :object, rebind =False):

	"""
		Utility function that accepts a Transmutable object "caller" and performs an escalation
		of a "value" with "attr" name right to the very top layer of a "caller". Any object other than
		Transmutable, which will not has an "_UPPER_LAYER_HOOK", will be just ignored.
	"""

	if	hasattr(caller, "_UPPER_LAYER_HOOK"):
		if	caller._UPPER_LAYER_HOOK:

			if(
				(attr == "loggy" and getattr(caller, "loggy") == evanesce or rebind)
				or
				(not hasattr(caller, attr) or rebind)

			):	setattr(caller, attr, value)
		else:	wingardium_leviosa(caller._UPPER_LAYER, attr, value, rebind)







