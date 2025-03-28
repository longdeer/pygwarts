import re








MONTHS_NAME_P	= re.compile(

	"([Jj][Aa][Nn]([Uu][Aa][Rr][Yy])?)|"
	"([Ff][Ee][Bb]([Rr][Uu][Aa][Rr][Yy])?)|"
	"([Mm][Aa][Rr]([Cc][Hh])?)|"
	"([Aa][Pp][Rr]([Ii][Ll])?)|"
	"([Mm][Aa][Yy])|"
	"([Jj][Uu][Nn]([Ee])?)|"
	"([Jj][Uu][Ll]([Yy])?)|"
	"([Aa][Uu][Gg]([Uu][Ss][Tt])?)|"
	"([Ss][Ee][Pp]([Tt][Ee][Mm][Bb][Ee][Rr])?)|"
	"([Oo][Cc][Tt]([Oo][Bb][Ee][Rr])?)|"
	"([Nn][Oo][Vv]([Ee][Mm][Bb][Ee][Rr])?)|"
	"([Dd][Ee][Cc]([Ee][Mm][Bb][Ee][Rr])?)"
)




VALID_29_DAYS	= r"(?P<tnd>[12][0-9]|0?[1-9])"
VALID_30_DAYS	= r"(?P<thd>30|[12][0-9]|0?[1-9])"
VALID_31_DAYS	= r"(?P<tod>3[01]|[12][0-9]|0?[1-9])"
VALID_29_MONTHS	= fr"(?P<allM>{MONTHS_NAME_P.pattern}|1[0-2]|0?[1-9])"
VALID_30_MONTHS	= fr"(?P<thdM>{MONTHS_NAME_P.pattern}|11|0?[469])"
VALID_31_MONTHS	= fr"(?P<todM>{MONTHS_NAME_P.pattern}|1[02]|0?[13578])"
VALID_YEAR		= fr"(?P<y>[12]\d\d\d)"
VALID_DELIMITER	= r"[,\\/\.\-\s\:]"
HUNDSCALE_P		= re.compile(r"(?P<base>\d+)?(?P<scale>[0-5]\d)$")




VALID_TIME_P	= re.compile(
	rf"""
		(
			(
				(?P<hh>[0-1]\d|2[0-3]){VALID_DELIMITER}?
			)
			|
			(
				(?P<h>\d){VALID_DELIMITER}
			)
		)
		(
			(?P<mm>[0-5]\d){VALID_DELIMITER}?
			|
			(
				(?P<m>\d)
				(
					{VALID_DELIMITER}(?=\d)
				)?
			)
		)
		(
			(?P<ss>[0-5]\d)|(?P<s>\d)
		)?
	""",
	re.VERBOSE
)




# DD/MM/YYYY
VALID_DATE_1_P	= re.compile(

	f"({VALID_29_DAYS}{VALID_DELIMITER}{VALID_29_MONTHS}"
    f"|{VALID_30_DAYS}{VALID_DELIMITER}{VALID_30_MONTHS}"
    f"|{VALID_31_DAYS}{VALID_DELIMITER}{VALID_31_MONTHS})"
    f"{VALID_DELIMITER}{VALID_YEAR}"
)
DATETIME_1_P	= re.compile(

	fr"(?P<date>{VALID_DATE_1_P.pattern})\ (?P<time>{VALID_TIME_P.pattern})",
	re.VERBOSE
)




# MM/DD/YYYY
VALID_DATE_2_P	= re.compile(

	f"({VALID_29_MONTHS}{VALID_DELIMITER}{VALID_29_DAYS}"
    f"|{VALID_30_MONTHS}{VALID_DELIMITER}{VALID_30_DAYS}"
    f"|{VALID_31_MONTHS}{VALID_DELIMITER}{VALID_31_DAYS})"
    f"{VALID_DELIMITER}{VALID_YEAR}"
)
DATETIME_2_P	= re.compile(

	fr"(?P<date>{VALID_DATE_2_P.pattern})\ (?P<time>{VALID_TIME_P.pattern})",
	re.VERBOSE
)




# YYYY/MM/DD
VALID_DATE_3_P	= re.compile(

    f"{VALID_YEAR}{VALID_DELIMITER}"
	f"({VALID_29_MONTHS}{VALID_DELIMITER}{VALID_29_DAYS}"
    f"|{VALID_30_MONTHS}{VALID_DELIMITER}{VALID_30_DAYS}"
    f"|{VALID_31_MONTHS}{VALID_DELIMITER}{VALID_31_DAYS})"
)
DATETIME_3_P	= re.compile(

	fr"(?P<date>{VALID_DATE_3_P.pattern})\ (?P<time>{VALID_TIME_P.pattern})",
	re.VERBOSE
)




# YYYY/DD/MM
VALID_DATE_4_P	= re.compile(

    f"{VALID_YEAR}{VALID_DELIMITER}"
	f"({VALID_29_DAYS}{VALID_DELIMITER}{VALID_29_MONTHS}"
    f"|{VALID_30_DAYS}{VALID_DELIMITER}{VALID_30_MONTHS}"
    f"|{VALID_31_DAYS}{VALID_DELIMITER}{VALID_31_MONTHS})"
)
DATETIME_4_P	= re.compile(

	fr"(?P<date>{VALID_DATE_4_P.pattern})\ (?P<time>{VALID_TIME_P.pattern})",
	re.VERBOSE
)








def hundscale(sixscale :str | int | float) -> str | Exception :

	"""
		Converts 60 scaled time string to 100 scaled string. Argument "sixscale" might be string,
		integer or float. It must represent the scalable value, which means it's last one or two
		digits have to be in range 0-59. It must be numerical value. The rest, from the beginning,
		will be taken as a base value to concatenate with obtained scaled value. The base value
		might be defaulted to zero for string concatenation. In other words this is conversion
		of hours:minutes or minutes:seconds values that represent time, to fit to the hundred
		scale plot, for example. E.g. 420 become 433, 19 become 031, 6 become 010, 0 become 000,
		e.t.c. Returns concatenated strings with leading zeros sometimes. Raises Exception in case
		of any fail.
	"""

	try:

		scalable = str(int(float(str(sixscale)))).zfill(2)
		BASE, scale = HUNDSCALE_P.fullmatch(scalable).group("base", "scale")

	except	Exception as E : raise ValueError(f"Unscalable argument \"{sixscale}\"")
	else:

		BASE	= BASE or "0"
		SCALE	= str(int(scale)*100 //60).zfill(2)

		return	BASE + SCALE








def monthmap(month	:str) -> str | None :

	""" Mapping english month word with corresponding month number as a string with leading zero """

	if month is not None:

		try:

			parsed_groups	= MONTHS_NAME_P.match(month).groups()
			found_month		= [ i for i,M in enumerate(parsed_groups) if M ][0]


			# After regex been parsed, the very first matched index will point to the month name
			# that matched, so by such indices correspondence, numerical string obtained.
			match found_month:

				case 0	: return "01"
				case 2	: return "02"
				case 4	: return "03"
				case 6	: return "04"
				case 8	: return "05"
				case 9	: return "06"
				case 11	: return "07"
				case 13	: return "08"
				case 15	: return "09"
				case 17	: return "10"
				case 19	: return "11"
				case 21	: return "12"


		# After regex parsing failed, trying to infer month numeric string from the argument.
		except AttributeError:
			match month:

				case "1"	| "01" | 1	: return "01"
				case "2"	| "02" | 2	: return "02"
				case "3"	| "03" | 3	: return "03"
				case "4"	| "04" | 4	: return "04"
				case "5"	| "05" | 5	: return "05"
				case "6"	| "06" | 6	: return "06"
				case "7"	| "07" | 7	: return "07"
				case "8"	| "08" | 8	: return "08"
				case "9"	| "09" | 9	: return "09"
				case "10"	| 10 		: return "10"
				case "11"	| 11 		: return "11"
				case "12"	| 12 		: return "12"







