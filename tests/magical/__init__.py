import	os
from	pathlib			import Path
from	pygwarts.tests	import PygwartsTestCase








class MagicalTestCase(PygwartsTestCase):

	"""
		pygwarts.magical tests super class
	"""


	MAGICAL_ROOT			= Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical"
	TIMETURN_TIMERS_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical" /"timers.loggy")
	KEY_SET_HANDLER			= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical" /"kchest.loggy")
	PACKED_KEY_SET_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical" /"pkchest.loggy")
	DEEP_KEY_SET_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical" /"dkchest.loggy")
	SET_HANDLER				= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical" /"chest.loggy")
	PACKED_SET_HANDLER		= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"magical" /"pchest.loggy")


	HOURS	= tuple(range(24))
	MINSEC	= tuple(range(60))
	DAYS_28	= tuple(range(1,29))
	DAYS_29	= tuple(range(1,30))
	DAYS_30	= tuple(range(1,31))
	DAYS_31	= tuple(range(1,32))
	MONTHS	= tuple(range(1,13))
	YEARS	= tuple(range(16,26))
	FYEARS	= tuple(range(2020,2026))

	DELIMETERS = ",", "\\", "/", ".", "-", ":", " ",

	travels = {

		"microseconds":	100500,
		"milliseconds":	100500,
		"seconds":		420,
		"minutes":		69,
		"hours":		42,
		"days":			17,
		"weeks":		14,
	}

	months = (

		"january",
		"february",
		"march",
		"april",
		"may",
		"june",
		"july",
		"august",
		"september",
		"october",
		"november",
		"december"
	)







