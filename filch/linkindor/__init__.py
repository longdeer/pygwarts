import	re
from	pygwarts.filch.nettherin	import VALID_IP4








VALID_MAC = str(

	r"(([A-Fa-f0-9]{2}-){5}([A-Fa-f0-9]{2}))|"
	r"(([A-Fa-f0-9]{2}:){5}([A-Fa-f0-9]{2}))|"
	r"(([A-Fa-f0-9]{4}\.){2}[A-Fa-f0-9]{4})"
)
G_O1_VALID_MAC = str(

	r"(?P<octet1>[A-Fa-f0-9]{2})[:-]"
	r"(?P<octet2>[A-Fa-f0-9]{2})[:-]"
	r"(?P<octet3>[A-Fa-f0-9]{2})[:-]"
	r"(?P<octet4>[A-Fa-f0-9]{2})[:-]"
	r"(?P<octet5>[A-Fa-f0-9]{2})[:-]"
	r"(?P<octet6>[A-Fa-f0-9]{2})"
)
G_O2_VALID_MAC	= r"(?P<octets1>[A-Fa-f0-9]{4})\.(?P<octets2>[A-Fa-f0-9]{4})\.(?P<octets3>[A-Fa-f0-9]{4})"
P_VALID_MAC		= re.compile(VALID_MAC)
GP_O1_VALID_MAC	= re.compile(G_O1_VALID_MAC)
GP_O2_VALID_MAC	= re.compile(G_O2_VALID_MAC)
P_ARP_REQ		= re.compile(f"[Ww]ho has {VALID_IP4} says {VALID_IP4}")
GP_ARP_REQ		= re.compile(fr"[Ww]ho has (?P<dst>{VALID_IP4}) says (?P<src>{VALID_IP4})")
GP_ARP_REQ_LOG	= re.compile(fr"{GP_ARP_REQ.pattern} \((?P<mac>{VALID_MAC})\)")
GP_ARP_RES_LOG	= re.compile(fr"(?P<mac>{VALID_MAC}) answered")








def is_valid_MAC(addr :str) -> bool | None :

	"""
		Helper function that verifies is "addr" string argument a valid MAC address record. Verification
		goes the classic way by splitting to parts and validating it is one or two octets, according to IEEE
		EUI-48. Returns True if "addr" consists of exactly six valid octets, delimited according to IEEE
		EUI-48. Returns False if at least one part is invalid, according to IEEE EUI-48, or if it is not
		one or two valid octets part. Returns None for the rest.
	"""

	if	isinstance(addr, str):

		try:

			if	len(S := addr.split("-")) == 6 or len(S := addr.split(":")) == 6:
				return	all( 0 <= int(octet,16) <256 for octet in S )

			elif(len(S := addr.split(".")) == 3):
				return	all( 0 <= int(octets,16) <65536 for octets in S )
		except:	return




def EUI48_format(addr :str, d :str ="-") -> str | None | Exception :

	"""
		Utility function that accepts "addr" and "d" strings and does two things:
			1. verifies "addr" is a valid MAC address record string;
			2. converts "addr" to a specified by "d" delimiter char EUI-48 MAC format.
		EUI-48 suggests three types of MAC records, so this is possible formats to be returned:
			XX-XX-XX-XX-XX-XX
			XX:XX:XX:XX:XX:XX
			XXXX.XXXX.XXXX
		Handles no Exception that might be raised and raises AssertionError if "d" is invalid
		delimiter. Returns None if "addr" failed validation.
	"""


	assert	str(d) in "-:.", f"EUI-48 delimiter must be \":\", \"-\" or \".\", not \"{d}\""


	if	(match := GP_O1_VALID_MAC.fullmatch(str(addr))):
		o1,o2,o3,o4,o5,o6 = match.group("octet1","octet2","octet3","octet4","octet5","octet6")

		if	all(filter(bool,( o1,o2,o3,o4,o5,o6 ))):
			return	(

				f"{o1}{d}{o2}{d}{o3}{d}{o4}{d}{o5}{d}{o6}".lower()
				if	d in "-:" else
				f"{o1}{o2}.{o3}{o4}.{o5}{o6}".lower()
			)


	elif(match := GP_O2_VALID_MAC.fullmatch(str(addr))):
		os1,os2,os3 = match.group("octets1","octets2","octets3")

		if	all(filter(bool,( os1,os2,os3 ))):
			return	(

				f"{os1[:2]}{d}{os1[2:]}{d}{os2[:2]}{d}{os2[2:]}{d}{os3[:2]}{d}{os3[2:]}".lower()
				if	d in "-:" else
				f"{os1}.{os2}.{os3}".lower()
			)







