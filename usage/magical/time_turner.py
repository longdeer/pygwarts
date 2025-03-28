from pygwarts.magical.time_turner import TimeTurner








today				= TimeTurner()											# Represents current moment
today_plus_sec		= TimeTurner(seconds=1)									# Represents current moment plus one second
today_plus_min		= TimeTurner(minutes=1)									# Represents current moment plus one minute
today_plus_hour		= TimeTurner(hours=1)									# Represents current moment plus one hour
today_plus_week		= TimeTurner(weeks=1)									# Represents current moment plus one week
today_minus_sec		= TimeTurner(seconds=-1)								# Represents current moment minus one second
today_minus_min		= TimeTurner(minutes=-1)								# Represents current moment minus one minute
today_minus_hour	= TimeTurner(hours=-1)									# Represents current moment minus one hour
today_minus_week	= TimeTurner(weeks=-1)									# Represents current moment minus one week
tomorrow			= TimeTurner(days=1)									# Represents tomorrow at the same time
tomorrow_start		= TimeTurner(timepoint=0, days=1)						# Represents tomorrow at midnight
yesterday			= TimeTurner(days=-1)									# Represents yesterday at the same time
yesterday_start		= TimeTurner(timepoint=0, days=-1)						# Represents yesterday at midnight
next_month			= TimeTurner(months=1)									# Represents next month first day at the same time
preious_month		= TimeTurner(months=-1)									# Represents previous month last day at the same time
this_month_start	= TimeTurner(timepoint="2359", months=-1, minutes=1)	# Represents current month first day at midnight
some_date			= TimeTurner("2/2/2022")								# Represents 2 February 2022 at midnight
some_date_moment	= TimeTurner("2/2/2022", TimeTurner())					# Represents 2 February 2022 at the same time








TimeTurner().format("%A %d/%m/%Y %H:%M:%S")		# Formatting in datetime syntax
TimeTurner().epoch								# POSIX timestamp float
TimeTurner().is_first_day						# True if it is first day of any month, False otherwise
TimeTurner().is_leap_year						# True if it is a leap year, False otherwise








TimeTurner().a		# Weekday as locale’s abbreviated name (Sun, Mon, ...)
TimeTurner().A		# Weekday as locale’s full name (Sunday, Monday, …)
TimeTurner().w		# Weekday as a decimal number, where 0 is Sunday and 6 is Saturday
TimeTurner().d		# Day of the month as a zero-padded decimal number
TimeTurner().b		# Month as locale’s abbreviated name (Jan, Feb, …)
TimeTurner().B		# Month as locale’s full name (January, February, …)
TimeTurner().m		# Month as a zero-padded decimal number
TimeTurner().y		# Year without century as a zero-padded decimal number
TimeTurner().Y		# Year with century as a decimal number
TimeTurner().H		# Hour (24-hour clock) as a zero-padded decimal number
TimeTurner().I		# Hour (12-hour clock) as a zero-padded decimal number
TimeTurner().p		# Locale’s equivalent of either AM or PM (it's literally AM or PM)
TimeTurner().M		# Minute as a zero-padded decimal number
TimeTurner().S		# Second as a zero-padded decimal number
TimeTurner().f		# Microsecond as a decimal number, zero-padded to 6 digits
TimeTurner().z		# UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive)
TimeTurner().Z		# Time zone name (empty string if the object is naive)
TimeTurner().j		# Day of the year as a zero-padded decimal number
TimeTurner().U		# Week number of the year as a zero-padded decimal number (week start from Sunday)
TimeTurner().W		# Week number of the year as a zero-padded decimal number (week start from Monday)








TimeTurner().dmY_aspath		# Gives a string day/month/year(4digit)
TimeTurner().mdY_aspath		# Gives a string month/day/year(4digit)
TimeTurner().Ymd_aspath		# Gives a string year(4digit)/month/day
TimeTurner().Ydm_aspath		# Gives a string year(4digit)/day/month
TimeTurner().dmY_aswpath	# Gives a string day\month\year(4digit)
TimeTurner().mdY_aswpath	# Gives a string month\day\year(4digit)
TimeTurner().Ymd_aswpath	# Gives a string year(4digit)\month\day
TimeTurner().Ydm_aswpath	# Gives a string year(4digit)\day\month
TimeTurner().dmY_asjoin		# Gives a string daymonthyear(4digit)
TimeTurner().mdY_asjoin		# Gives a string monthdayyear(4digit)
TimeTurner().Ymd_asjoin		# Gives a string year(4digit)monthday
TimeTurner().Ydm_asjoin		# Gives a string year(4digit)daymonth
TimeTurner().dmY_dashed		# Gives a string day-month-year(4digit)
TimeTurner().mdY_dashed		# Gives a string month-day-year(4digit)
TimeTurner().Ymd_dashed		# Gives a string year(4digit)-month-day
TimeTurner().Ydm_dashed		# Gives a string year(4digit)-day-month
TimeTurner().HMS_ascolon	# Gives a string hour:minute:second
TimeTurner().HMS_spaced		# Gives a string hour minute second







