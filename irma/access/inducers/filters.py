from pygwarts.irma.access.inducers	import AccessInducer








def posnum(caller :AccessInducer, value :int | float | str) -> int | float | str :

	"""
		Helper function that filters a positive floatable "value", as a second argument, and return it.
		Returns None in case of "value" is not floatable or if it is not positive.
		By floatable value the valid result of str -> float cast is meant.
		Originally designed to accept a Transmutable object (AccessInducer) as a first argument "caller".
	"""

	try:	return value if 0 <float(str(value)) else None
	except:	return








def negnum(caller :AccessInducer, value :int | float | str) -> int | float | str :

	"""
		Helper function that filters a negative floatable "value", as a second argument, and return it.
		Returns None in case of "value" is not floatable or if it is not positive.
		By floatable value the valid result of str -> float cast is meant.
		Originally designed to accept a Transmutable object (AccessInducer) as a first argument "caller".
	"""

	try:	return value if float(str(value)) <0 else None
	except:	return








def nonnegnum(caller :AccessInducer, value :int | float | str) -> int | float | str :

	"""
		Helper function that filters a non-negative floatable "value", as a second argument, and return it.
		Returns None in case of "value" is not floatable or if it is not positive.
		By floatable value the valid result of str -> float cast is meant.
		Originally designed to accept a Transmutable object (AccessInducer) as a first argument "caller".
	"""

	try:	return value if 0 <= float(str(value)) else None
	except:	return








def nonposnum(caller :AccessInducer, value :int | float | str) -> int | float | str :

	"""
		Helper function that filters a non-positive floatable "value", as a second argument, and return it.
		Returns None in case of "value" is not floatable or if it is not positive.
		By floatable value the valid result of str -> float cast is meant.
		Originally designed to accept a Transmutable object (AccessInducer) as a first argument "caller".
	"""

	try:	return value if float(str(value)) <= 0 else None
	except:	return








def zeronum(caller :AccessInducer, value :int | float | str) -> int | float | str :

	"""
		Helper function that filters a zero floatable "value", as a second argument, and return it.
		Returns None in case of "value" is not floatable or if it is not positive.
		By floatable value the valid result of str -> float cast is meant.
		Originally designed to accept a Transmutable object (AccessInducer) as a first argument "caller".
	"""

	try:	return value if float(str(value)) == 0. else None
	except:	return








def plurnum(caller :AccessInducer, value :int | float | str) -> int | float | str :

	"""
		Helper function that filters a positive floatable "value", as a second argument, that greater
		than one and return it. Returns None in case of "value" is not floatable or if it is not positive.
		By floatable value the valid result of str -> float cast is meant.
		Originally designed to accept a Transmutable object (AccessInducer) as a first argument "caller".
	"""

	try:	return value if 1 <float(str(value)) else None
	except:	return







