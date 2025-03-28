import re








VALID_IP4	= r"((25[0-5]|2[0-4]\d|1\d\d|0?\d\d|00\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|0?\d\d|00\d|\d)"
P_VALID_IP4	= re.compile(VALID_IP4)
G_VALID_IP4	= str(

	r"(?P<octet1>25[0-5]|2[0-4]\d|1\d\d|0?\d\d|00\d|\d)\."
	r"(?P<octet2>25[0-5]|2[0-4]\d|1\d\d|0?\d\d|00\d|\d)\."
	r"(?P<octet3>25[0-5]|2[0-4]\d|1\d\d|0?\d\d|00\d|\d)\."
	r"(?P<octet4>25[0-5]|2[0-4]\d|1\d\d|0?\d\d|00\d|\d)"
)
GP_VALID_IP4 = re.compile(G_VALID_IP4)




def is_valid_ip4(addr :str) -> bool | None :

	"""
		Helper function that verifies "addr" string argument is a valid ip version 4 address.
		Verification goes the classic way by splitting to parts and validating it is 0-255 integer
		range octets, without 0-padding. Returns True if "addr" consists of exactly four valid octets.
		Returns False if at least one part is not a valid or is 0-padded octet. Returns None for the rest.
	"""

	if	isinstance(addr, str) and len(S := addr.split(".")) == 4:

		for octet in S:

			try:	octet_int = int(octet)
			except:	return
			else:

				if	octet_int <0 or 255 <octet_int or len(str(octet_int)) != len(octet): return False
		return	True




def validate_ip4(addr :str) -> str | None :

	"""
		Helper function that takes "addr" string and returns it's sanitized version (no padding zeroes)
		if it represents valid ip version 4 address. Utilizes "is_valid_ip4" function for "addr"
		validation. Returns None if "is_valid_ip4" doesn't return True.
	"""

	if	isinstance(addr, str) and len(S := addr.split(".")) == 4:

		try:

			if	is_valid_ip4(sanit := ".".join( str(octet) for octet in map(int,S) if -1 <octet <256 )):
				return sanit
		except:	return







