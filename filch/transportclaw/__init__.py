







def is_valid_port(number :int | float | str) -> bool | None :

	"""
		Helper function that verifies "number" is a valid port number by string-casting to int.
		Returns True if it is 0-65535 range integer, or False otherwise. Returns None for the rest.
	"""

	try:	return 0 <= int(str(number)) <= 65535 if isinstance(number, int) else None
	except:	return




def validate_port(number :int | float | str) -> int | None :

	"""
		Helper function that takes "number" argument and triple casts it to int. If obtained int is in
		range 0-65535, returns that int. Returns None in any other cases.
	"""

	try:	port = int(float(str(number)))
	except:	return
	else:	return port if -1 <port <65536 else None







