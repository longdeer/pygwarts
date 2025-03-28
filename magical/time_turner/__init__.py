from __future__							import annotations
from datetime							import datetime
from datetime							import timedelta
from typing								import Dict
from typing								import Tuple
from collections.abc					import Sequence
from math								import copysign
from re									import Pattern
from pygwarts.magical.time_turner.utils	import VALID_DATE_1_P
from pygwarts.magical.time_turner.utils	import VALID_DATE_2_P
from pygwarts.magical.time_turner.utils	import VALID_DATE_3_P
from pygwarts.magical.time_turner.utils	import VALID_DATE_4_P
from pygwarts.magical.time_turner.utils	import VALID_TIME_P
from pygwarts.magical.time_turner.utils	import monthmap








class TimeTurner:

	r"""
		                                           ..::::-----:::..                                           
		                                  .:-=+*##%%%%%%%%%%%%%%%%%%##*+==-:.                                 
		                            .:-+*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#+=-...                          
		                       ..:=*%%%%%%%%%%%#*+==-:::......:::--=++*#%%%%%%%%%%#+-..                       
		                     .=*%%%%%%%%#*=-:..             . ..       ..:-=+#%%%%%%%%#=:..                   
		                 ..=*%%%%%%%*+-..      .:-==++***####****+==-:...    ..:=*%%%%%%%#+:.                 
		               .-*%%%%%%#+-..   ..-=+*%%%%%%%%%%%%%%%%%%%%%%%%%%#*=-:..   .:=#%%%%%%#=.               
		             .=#%%%%%%+:. .  .-+#%%%%%%%%#*+==-+%%%%%%#-==+*##%%%%%%%#*=:.    .=#%%%%%%+:             
		           .=#%%%%%#=..  ..=*%%%%%%#+=-....    -#%%%%#*     ...:-+*%%%%%%#+:.   .:+%%%%%%*:.          
		         .-#%%%%%*:.. ..-*%%%%%#+-.             .*%%%.             .:=*%%%%%#+:.   .=%%%%%%+.         
		        .*%%%%%#:   ..=%%%%%#=:.         .:-=++**%%%%**++=-:..        ..-*%%%%%*:.   .+%%%%%#-        
		      .-%%%%%%=.   .+%%%%%*:.       .:=*#%#%%%%%*=::-+#%#%%%%%*+-.        .=#%%%%*:    :#%%%%%+..     
		     .=%%%%%*.   .=%%%%%+..     ..=*%%%%%%%%#+:.       :=*%%%%*%%%#+:.      .-#%%%%*..  .=%%%%%*.     
		    .+%%%%%+.   :#%%%%*.     ..-*%%%*-*%%#+:.            ..=**=*#%%%%#=..     .=%%%%%-.  .-%%%%%#..   
		   .+%%%%%=.   :%%%%%-      .-#%%%%%%*%*-.                  .:+%%%%#%%%%+.     .:#%%%%+.  .:%%%%%#.   
		  .=%%%%%+.   -%%%%#:.    .:#%#*%%%%%#-.                       .*%%%%%%%%%=.     .+%%%%+.  .:%%%%%*.  
		  :%%%%%*.   :%%%%#.     .=%%%%%%%%%%:..                    .....*%%%%#*%%%*..    .=%%%%+.  .-%%%%%+. 
		 .*%%%%%.  ..#%%%#.     .+%%%%+%%%%%# :--::..            ...::-- =%%%#=:*#%%#.     .+%%%%-.   +%%%%%: 
		 :%%%%%=.  .+%%%%-     .=%%%*+:+*%%%%-.:-----:::.......:::-----..#%%%%%#%%%%%#.     .#%%%%.   .%%%%%+ 
		.=%%%%%..  .%%%%#     ..%%%*+=.=+*%%%%+..:-------------------:.-#%%%%%%%%%%%%%=      =%%%%-    *%%%%#.
		*%%%%%%+. .-%%%%=     .+%%%%%%=%%%%%%%%%*-..::-----------::.:+#%%%%%%%%%%%#+%%%.     :%%%%*..:*#%%%%%*
		%%%%%%%%####%%%%-      #%%%%%%%%%%%%#*#%%%%#+-:..----:.:-=*%%%%%%#*-*%%%%%%%%%%:     .%%%%%###%%%%%%%%
		%%%%%%%%%%%%%%%%-.    .#%%#%%%%%%%%#+-*#%%%%%#*-.:---..*#%%%%%%%*+-:=*#%%%%%%%%:     .%%%%%%%%%%%%%%%%
		%%%%%%%#---+%%%%-.    .*%%%%%%%%%%%%%%%%%#+-.    .--:    .:=*%%%%%%+%%%%%%%#%%%.     .%%%%#--=%%%%%%%%
		:*%%%%%:   :%%%%+.     -%%%%##%%%%%%%%%+:.       .--.       ..-#%%%%%%%%%%%%%%*.     -%%%%+. .:*%%%%%:
		.-%%%%%:.  .#%%%%.     .#%%#=+#%%%%%%*.         ..::....       .=%%%%%%%%#%%%%:      *%%%%:   .#%%%%*.
		 .%%%%%*.  .-%%%%+.    .:#%%%%%%%#%%%......::::-------::::....  .+%%%%%#=:*%%=      :%%%%*.   -%%%%%- 
		  =%%%%%-    +%%%%=.     :#%%%%%%%%%%..:---------------------::. =%%%%%%%*%%=      .#%%%#.   .#%%%%#. 
		  .#%%%%%:.  .*%%%%=.     .*%%%%%%%%%+.:----------------------:.:%%%%%%%%%#:.    ..#%%%%:  ..*%%%%%:. 
		  ..#%%%%#..  .*%%%%+.     .-#%%%#+-*#*:.:------------------:..+%%%%%%%%%+.     .-#%%%%:.  .+%%%%%=.  
		    :%%%%%#:   .+%%%%#:.    ..-#%%#+#%%%#=..:------------::.-+%%*-*#%%%+.     ..+%%%%#.   .+%%%%%=    
		     :#%%%%#:.   -#%%%%+.      .:+#%%%%%%%%*-..:------::.:+#%%%%%#%%*-.      .-#%%%%+.   .*%%%%%=.    
		      .#%%%%%+.  ..+%%%%%+.       .:=#%%%%%%%%*=:.::..-+%%#%%%%%#+-. .     .=#%%%%*:    -#%%%%%-      
		       .+%%%%%#-.   .+%%%%%*-.      . .:=+*#%%%%%#++*%%%%%#*+=-..        :+%%%%%*-.   .+%%%%%#:..     
		        .:#%%%%%*:.  ..=#%%%%%+-.            .:::#%%%-::..           .:+#%%%%%*:.   .+%%%%%%=.        
		          .=%%%%%%*-.   .:+%%%%%%*+-:.         :-#%%%=-          .:=*%%%%%%*-..  .:+%%%%%%+.          
		           ..=%%%%%%#=.    .-+#%%%%%%%*+=-:... =%%%%%%# ...::-+*#%%%%%%%*-.    .-*%%%%%%*:.           
		              .-#%%%%%%*=..   ..-+*%%%%%%%%%%###%%%%%%%##%%%%%%%%%%#+=:.   ..-+%%%%%%%+:.             
		                .:+%%%%%%%#+-...  ...-=+*##%%%%%%%%%%%%%%%%%#*+=-:..    .:=*%%%%%%%*-..               
		                  ..-+%%%%%%%%#+-:.      ....:::------:::.....    ...-=*%%%%%%%%*=.                   
		                      .:+*%%%%%%%%%#+=-::...              ....:-=+*#%%%%%%%%#+-..                     
		                         ..-=*#%%%%%%%%%%%%##***+++++++***#%%%%%%%%%%%%%*+-..                         
		                             . .:=+*#%%%%%%%%%%%%%%%%%%%%%%%%%%%%#*+=-:..                             
		                                     ..:-==++***######***++==-::.. .                                  
		                                                          ..       
		The datetime library functionality wrapper. Takes full date in format:
			D{1,2}[,/.-\s:\](M{1,2}|NAME)[,/.-\s:\]YYYY
			(M{1,2}|NAME)[,/.-\s:\]D{1,2}[,/.-\s:\]YYYY
			YYYY[,/.-\s:\](M{1,2}|NAME)[,/.-\s:\]D{1,2}
			YYYY[,/.-\s:\]D{1,2}[,/.-\s:\](M{1,2}|NAME)
		and time in format:
			M{1,2}[,/.-\s:\]?H{1,2}[,/.-\s:\]?(S?{1,2})?
		The date sequence will be considered in four different variations, and it is up to user not to
		mess with it. The default TimeTurner sequence is DD/MM/YYYY. It is used in TimeTurner logic and
		it is recommended to adhere such format. Current implementation allow to use only full year format,
		that implies ONLY FOUR DIGITS YEAR IS ACCEPTABLE! Time sequence is considered in only one way, but
		is possible to provided in any ways, such as with or without lead digits, with or without delimiters
		and with or without seconds (hours and minutes are mandatory). Anyway, the default format defined
		by TimeTurner is HH:MM:SS and it is highly recommended to adhere such format, and to not mess with
		time sequence at all, cause different formats may be misinterpreted by the user at first place.
		Both date and time sequences are provided by "datepoint" and "timepoint" arguments. Both can be type
		string, tuple of strings/integers, float/int timestamp, dateimte or even TimeTurner objects. Both
		can be omitted, and in such case datepoint defaulted to current moment (by datetime.today call),
		timepoint defaulted to midnight. It is important to notice, that if datepoint provided as datetime
		or TimeTurner (even when defaulted to current moment by datetime.today call), the timepoint will be
		first obtained from datepoint, and then, if provided as argument, will be tuned to that value.
		There are properties that are default datetime format codes implementations and datetime
		functionality access. Any other datetime library functionality might be accessed via POINT attribute.
	"""

	REPR_MODES = {

		"aspath":	"/",
		"aswpath":	"\\",
		"asjoin":	"",
		"ascolon":	":",
		"dashed":	"-",
		"spaced":	" ",
	}




	# The following properties are default datetime format codes implementations,
	# that the 1989 C standard requires, and which work on all platforms
	# with a standard C implementation. It's almost all directives, except some
	# ISO and locale's representations.
	#
	# %a - Weekday as locale’s abbreviated name (Sun, Mon, ...);
	# %A - Weekday as locale’s full name (Sunday, Monday, …);
	# %w - Weekday as a decimal number, where 0 is Sunday and 6 is Saturday;
	# %d - Day of the month as a zero-padded decimal number;
	# %b - Month as locale’s abbreviated name (Jan, Feb, …);
	# %B - Month as locale’s full name (January, February, …);
	# %m - Month as a zero-padded decimal number;
	# %y - Year without century as a zero-padded decimal number;
	# %Y - Year with century as a decimal number;
	# %H - Hour (24-hour clock) as a zero-padded decimal number;
	# %I - Hour (12-hour clock) as a zero-padded decimal number;
	# %p - Locale’s equivalent of either AM or PM (it's literally AM or PM);
	# %M - Minute as a zero-padded decimal number;
	# %S - Second as a zero-padded decimal number;
	# %f - Microsecond as a decimal number, zero-padded to 6 digits;
	# %z - UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive);
	# %Z - Time zone name (empty string if the object is naive);
	# %j - Day of the year as a zero-padded decimal number;
	# %U - Week number of the year as a zero-padded decimal number (week start from Sunday);
	# %W - Week number of the year as a zero-padded decimal number (week start from Monday);
	@property
	def a(self) -> str : return self.POINT.strftime("%a")
	@property
	def A(self) -> str : return self.POINT.strftime("%A")
	@property
	def w(self) -> str : return self.POINT.strftime("%w")
	@property
	def d(self) -> str : return self.POINT.strftime("%d")
	@property
	def b(self) -> str : return self.POINT.strftime("%b")
	@property
	def B(self) -> str : return self.POINT.strftime("%B")
	@property
	def m(self) -> str : return self.POINT.strftime("%m")
	@property
	def y(self) -> str : return self.POINT.strftime("%y")
	@property
	def Y(self) -> str : return self.POINT.strftime("%Y")
	@property
	def H(self) -> str : return self.POINT.strftime("%H")
	@property
	def I(self) -> str : return self.POINT.strftime("%I")
	@property
	def p(self) -> str : return self.POINT.strftime("%p")
	@property
	def M(self) -> str : return self.POINT.strftime("%M")
	@property
	def S(self) -> str : return self.POINT.strftime("%S")
	@property
	def f(self) -> str : return self.POINT.strftime("%f")
	@property
	def z(self) -> str : return self.POINT.strftime("%z")
	@property
	def Z(self) -> str : return self.POINT.strftime("%Z")
	@property
	def j(self) -> str : return self.POINT.strftime("%j")
	@property
	def U(self) -> str : return self.POINT.strftime("%U")
	@property
	def W(self) -> str : return self.POINT.strftime("%W")


	# One can use this property that redirect to datetime strftime method,
	# to obtain desired special formatted strings.
	@property
	def format(self) -> datetime : return self.POINT.strftime


	# Local date corresponding to the POSIX timestamp
	@property
	def epoch(self) -> float : return self.POINT.timestamp()


	# Boolean that decide if current datetime object corresponds to
	# the very first day of the month.
	@property
	def is_first_day(self) -> bool : return self.POINT.strftime("%d") == "01"


	# Boolean that decide if current year is a leap year.
	@property
	def is_leap_year(self) -> bool :

		year = int(self.POINT.strftime("%Y"))
		return bool(not year%4 and (year%100 or not year%400))




	def travel(self, **traveling :Dict[str,int]) -> TimeTurner :

		"""
			Wrapper over timedelta to provide months delta.
			By months delta only leap to last date of previous month or first day of next month is meant.
		"""

		# Casting values to integer is the argument guard, cause timedelta itself takes arguments as
		# integers and all logic below will not account for months being float, so if desired month will
		# be float and infinity loop will occur due to integer current_month never will equal float
		# desired_month. This infinity loop will be stopped by OverflowError as 2914029 subdays
		# doesn't fit for timedelta. However, such case and other are guarded by this casts.
		_travelings = { k: int(v) for k,v in traveling.items() }


		try:

			m = _travelings["months"]
			del _travelings["months"]


			start = self.POINT


			# As month value not restricted and can be as large as possible, desired
			# month is obtained by modulo of start point month plus number of months
			# to travel. If desired month is divided by 12 it's defaulted to 12.
			current_month = int(start.strftime("%m"))
			desired_month = (int(current_month) + m)%12 or 12


			# Subdays and months_passed will be incremented in loop by difference,
			# which is solved as one day step with the sign, obtained from number
			# of months to travel, as a direction (minus for backward and plus fo forward).
			# Traveling months is the loop first stopping condition.
			subdays = 0
			months_passed = 0
			traveling_months = abs(m)
			diff = int(copysign(m**0, m))


			# By travel provided months is meant the obtaining as many days, as need to
			# to obtain such a desired month. On each iteration timedelta will be
			# summed with star point to produce subdays. When the desired month
			# will be reached, the amount of subdays will produce the last day of
			# desired month, in case of backwards traveling, or the first dat of month,
			# in case of forward traveling. This days will be passed along with the rest
			# of traveling keywords to the final timedelta constructor.
			while traveling_months != months_passed or desired_month != current_month:

				subdays += diff
				current_point = start + timedelta(days=subdays)
				new_month = int(current_point.strftime("%m"))


				if	new_month != current_month:

					months_passed += 1
					current_month = new_month


			if	"days" in _travelings:

				_travelings["days"] += subdays
			else:
				_travelings["days"] = subdays


		# KeyError means there were no months to convert, so simple timedelta object created,
		# with provided traveling. Any invalid traveling keyword argument passed will raise
		# timedelta TypeError. In case of timedelta success construction, current object POINT
		# will be modified with this timedelta, so travel happened.
		except	KeyError : pass
		self.POINT += timedelta(**_travelings)


		return	self




	def sight(self, **sightings :Dict[str,int]) -> TimeTurner :

		"""
			Duplicate current TimeTurner object and travels "sightings" keyword arguments.
			Returns new TimeTurner object, which is traveled from current.
		"""

		return	TimeTurner(self).travel(**sightings)




	def diff(	self,
				subtrahend			:TimeTurner | datetime | float | int | str	=None,
			)-> float | TypeError	:

		"""
			Method to obtain difference between current TimeTurner object and any number-like value,
			which might be derived from another TimerTurner or datetime object. The returned value is
			float seconds between current TimeTurner object timestamp and "subtrahend", with sign
			that point to the direction:
				>0 - current TimeTurner object has older timestamp
				<0 - current TimeTurner object has younger timestamp
			Raises TypeError in case of invalid "subtrahend" value.
		"""

		match subtrahend:

			case None				: return self.POINT.timestamp() - datetime.today().timestamp()
			case TimeTurner()		: return self.POINT.timestamp() - subtrahend.POINT.timestamp()
			case datetime()			: return self.POINT.timestamp() - subtrahend.timestamp()
			case float() | int()	: return self.POINT.timestamp() - subtrahend
			case str()				:

				try:	return	self.POINT.timestamp() - float(subtrahend)
				except	ValueError	: pass
			case _					: pass


		raise	TypeError(f"Can't calculate difference between \"{subtrahend}\" and TimeTurner object")




	def __str__(self) : return self.POINT.strftime("%A %d/%m/%Y %H:%M:%S")
	def __add__(self, addition :float | int | str) -> TimeTurner | TypeError :

		"""
			Addition to current TimeTurner object of seconds as any number-interpretable value,
			which will be double cast to allow floatable string to provide seconds.
			Returned value is the new TimeTurner object, simply sighted by provided "addition"
			cast value. Raises exception in case of invalid "addition" operand.
		"""

		try:	return	self.sight(seconds=int(float(addition)))
		except:	raise	TypeError(f"Value \"{addition}\" cannot be added to TimeTurner object")




	def __sub__(self, subtraction :float | int | str) -> TimeTurner | TypeError :

		"""
			Subtraction from current TimeTurner object of seconds as any number-interpretable value,
			which will be double cast to allow floatable string to provide seconds.
			Returned value is the new TimeTurner object, simply sighted by provided "subtraction"
			cast value. Raises exception in case of invalid "subtraction" operand.
		"""

		try:	return	self.sight(seconds=-int(float(subtraction)))
		except:	raise	TypeError(f"Value \"{subtraction}\" cannot be subtracted from TimeTurner object")




	def __eq__(self, other :TimeTurner | datetime | float | int | str) -> bool :

		"""
			Comparison of equality of current TimeTurner object timestamp with any number-like value,
			which might be derived from another TimerTurner or datetime object. Returns False
			in any cases, when "other" operand cannot be interpreted as number. In terms of stability,
			values comparison occurs after int cast.
		"""

		match other:

			case TimeTurner()		: return int(self.POINT.timestamp()) == int(other.epoch)
			case datetime()			: return int(self.POINT.timestamp()) == int(other.timestamp())
			case float() | int()	: return int(self.POINT.timestamp()) == int(other)
			case str()				:

				try		: return	int(self.POINT.timestamp()) == int(float(other))
				except	: pass
			case _		: pass


		return	False




	def __gt__(self, other :TimeTurner | datetime | float | int | str) -> bool | TypeError :

		"""
			Comparison of greatness of current TimeTurner object timestamp with any number-like value,
			which might be derived from another TimerTurner or datetime object. Raises exception in case
			of invalid "other" operand. In terms of stability, values comparison occurs after int cast.
		"""

		match other:

			case TimeTurner()		: return int(other.epoch)		<int(self.POINT.timestamp())
			case datetime()			: return int(other.timestamp())	<int(self.POINT.timestamp())
			case float() | int()	: return int(other)				<int(self.POINT.timestamp())
			case str()				:

				try		: return	int(float(other)) <int(self.POINT.timestamp())
				except	: pass
			case _		: pass


		raise	TypeError(f"Object \"{other}\" cannot be compared with TimeTurner object")




	def __ge__(self, other :TimeTurner | datetime | float | int | str) -> bool | TypeError :

		"""
			Comparison of greatness or equality of current TimeTurner object timestamp with any
			number-like value, which might be derived from another TimerTurner or datetime object.
			Raises exception in case of invalid "other" operand. In terms of stability,
			values comparison occurs after int cast.
		"""

		match other:

			case TimeTurner()		: return int(other.epoch)		<= int(self.POINT.timestamp())
			case datetime()			: return int(other.timestamp())	<= int(self.POINT.timestamp())
			case float() | int()	: return int(other)				<= int(self.POINT.timestamp())
			case str()				:

				try		: return	int(float(other)) <= int(self.POINT.timestamp())
				except	: pass
			case _		: pass


		raise	TypeError(f"Object \"{other}\" cannot be compared with TimeTurner object")




	def __lt__(self, other :TimeTurner | datetime | float | int | str) -> bool | TypeError :

		"""
			Comparison of lesserness of current TimeTurner object timestamp with any number-like value,
			which might be derived from another TimerTurner or datetime object. Raises exception in case
			of invalid "other" operand. In terms of stability, values comparison occurs after int cast.
		"""

		match other:

			case TimeTurner()		: return int(self.POINT.timestamp()) <int(other.epoch)
			case datetime()			: return int(self.POINT.timestamp()) <int(other.timestamp())
			case float() | int()	: return int(self.POINT.timestamp()) <int(other)
			case str()				:

				try		: return	int(self.POINT.timestamp()) <int(float(other))
				except	: pass
			case _		: pass


		raise	TypeError(f"Object \"{other}\" cannot be compared with TimeTurner object")




	def __le__(self, other :TimeTurner | datetime | float | int | str) -> bool | TypeError :

		"""
			Comparison of lesserness or equality of current TimeTurner object timestamp with any
			number-like value, which might be derived from another TimerTurner or datetime object.
			Raises exception in case of invalid "other" operand. In terms of stability,
			values comparison occurs after int cast.
		"""

		match other:

			case TimeTurner()		: return int(self.POINT.timestamp()) <= int(other.epoch)
			case datetime()			: return int(self.POINT.timestamp()) <= int(other.timestamp())
			case float() | int()	: return int(self.POINT.timestamp()) <= int(other)
			case str()				:

				try		: return	int(self.POINT.timestamp()) <= int(float(other))
				except	: pass
			case _		: pass


		raise	TypeError(f"Object \"{other}\" cannot be compared with TimeTurner object")




	def __getattr__(self, attr :str):

		"""
			Accessing attribute by parsing directives, which must be default datetime format codes,
			and join it by the representation mode (REPR_MODES key). The directives must be separated
			with mode by underscore.

			The following means TimeTurner not supposed to have attributes that starts
			with just underscore, so if such an attribute wanna be accessed, there'll be
			some raise.	Also when some non existent attribute wanna be accessed and it will lead
			to this dunder,	ValueError will be raised by extracting from split. All this raises
			will be redirected to AttributeError with special message.

			Implemented representation modes:
			_aspath		- joined by /
			_aswpath	- joined by \
			_asjoin		- joined by ""
			_ascolon	- joined by :
			_dashed		- joined by -
			_spaced		- joined by " "
		"""

		try:

			directives, mode	= attr.split("_")
			if not directives	: raise ValueError


			# For default datetime formats, that are provided by properties, getattr is used
			# to invoke corresponding property. This is used instead of strftime cause, despite
			# strftime from POINT is the proper way to handle inner logic, strftime with some
			# implicitly defined for datetime properties may break TimeTurner interface and
			# lead to undefined behavior. So to resume, if object implements some interface,
			# such interface must be used, especially if such interface is the interface to
			# some another interface.
			return	self.REPR_MODES[mode].join( getattr(self, d) for d in directives )
		except		(ValueError, KeyError):
			raise	AttributeError(f"Couldn't solve \"{attr}\" attribute")




	def __init__(
					self,
					datepoint	:str | int | float | Sequence[str|int|float] | TimeTurner | datetime =None,
					timepoint	:str | int | float | Sequence[str|int|float] | TimeTurner | datetime =None,
					**travels	:Dict[str,int],
				):

		# If datepoint contain invalid value, there'll be ValueError raise.
		# If datepoint not provided, current moment will be taken. It is important, that in this part
		# timepoint will be taken from datepoint, if it possible. Provided timepoint argument will
		# rewrite it in next part, so current TimeTurner object time will be tuned.
		match datepoint:

			case	str() | [
					str() | int(),
					str() | int(),
					str() | int()
						]			: self.POINT = datetime(*map(int, self.validate(datepoint)))
			case	int() | float()	: self.POINT = datetime.fromtimestamp(datepoint)
			case	TimeTurner()	: self.POINT = datepoint.POINT
			case	datetime()		: self.POINT = datepoint
			case	None			: self.POINT = datetime.today()
			case	_				: raise ValueError(f"Invalid datepoint \"{datepoint}\" initiation")


		# If timepoint contain invalid value, there'll be ValueError raise.
		# If timepoint not provided, current TimeTurner object time taken from datepoint.
		match timepoint:

			case	str() | [
					str() | int(), str() | int() ] | [
					str() | int(), str() | int(), str() | int() ] :

				point = self.valitime(timepoint)
				self.POINT = self.POINT.replace(

					hour=int(point[0]),
					minute=int(point[1]),
					second=int(point[2])
				)

			case	int() | float() :

				# Resolving UTC format for zero timepoint, which means timepoint initiation
				# implies strict midnight point, with no timezone reference.
				if	timepoint == 0 or timepoint == 0. :

					point = datetime.utcfromtimestamp(timepoint)
				else:
					point = datetime.fromtimestamp(timepoint)

				self.POINT = self.POINT.replace(

					hour=int(point.strftime("%H")),
					minute=int(point.strftime("%M")),
					second=int(point.strftime("%S")),
					microsecond=int(point.strftime("%f"))
				)

			case	TimeTurner() :

				self.POINT = self.POINT.replace(

					hour=int(timepoint.H),
					minute=int(timepoint.M),
					second=int(timepoint.S),
					microsecond=int(timepoint.f)
				)

			case	datetime() :

				self.POINT = self.POINT.replace(

					hour=int(timepoint.strftime("%H")),
					minute=int(timepoint.strftime("%M")),
					second=int(timepoint.strftime("%S")),
					microsecond=int(timepoint.strftime("%f"))
				)

			case	None	: pass
			case	_		: raise ValueError(f"Invalid timepoint \"{timepoint}\" initiation")


		# Final step is to maintain some traveling, if provided, and saving initiated points
		# for some further use, e.g. for sight. Points saved in form, that is default for TimeTurner.
		if	travels : self.travel(**travels)


		self.starting_datepoint = self.POINT.strftime("%d/%m/%Y")
		self.starting_timepoint = self.POINT.strftime("%H:%M:%S")




	def dsolve(self, point :str | Sequence[str]) -> Pattern | ValueError :

		"""
			Parsing out date and time using 4 different patterns:
				DD MM YYYY
				MM DD YYYY
				YYYY MM DD
				YYYY DD MM
			Returns a match if any, or raises ValueError.
		"""

		if	not isinstance(point, str):

			# Assuming any Exception at this point are cause of "point" is not iterable, or
			# iterable that containing not strings, so AttributeError must be raised.
			try:	_point = "/".join(map(str, point))
			except:	raise AttributeError(f"datepoint must be type of string or contain strings")
		else :		_point = point


		match1 = VALID_DATE_1_P.fullmatch(_point)
		if match1 : return match1


		match2 = VALID_DATE_2_P.fullmatch(_point)
		if match2 : return match2


		match3 = VALID_DATE_3_P.fullmatch(_point)
		if match3 : return match3


		match4 = VALID_DATE_4_P.fullmatch(_point)
		if match4 : return match4


		# None of 4 patterns produces result so datepoint is invalid
		raise ValueError(f"\"{_point}\" cannot be solved as valid date")




	def validate(self, point :str | Sequence[str]) -> Tuple[str,str,str] | ValueError :

		"""
			Validate date as a real date value, even accounts for leap year. Returns a tuple of
			three numeric strings, that represents year, month, day, in case of successful "point"
			solving. Raises ValueError otherwise.
		"""

		tnd, allM, thd, thdM, tod, todM, Y = self.dsolve(point).group(
			"tnd", "allM", "thd", "thdM", "tod", "todM", "y"
		)


		if	tnd == "29" and allM == "02":
			year = int(Y)

			if	not not year%4 and (year%100 or not year%400):
				raise ValueError(f"{year} is not a leap year")


		return	Y, monthmap(todM or thdM or allM), tod or thd or tnd




	def valitime(self, point :str | Sequence[str]) -> Tuple[str,str,str] | ValueError :

		"""
			Validate time as a real time value. Will try to make a string if it is not string but iterable.
			This is combined with validation cause it's much simpler then for date. Returns a tuple of
			three numeric zero-padded strings, that represents hours, minutes and seconds, in case of
			successful "point" solving. Raises ValueError otherwise.
		"""

		if	point and not isinstance(point, str):

			# Assuming any Exception at this point are cause of "point" is not iterable, or
			# iterable that containing not strings, so AttributeError must be raised.
			try:	_point = ":".join(map(lambda E : str(E).zfill(2), point))
			except:	raise AttributeError(f"timepoint must be type of string or contain strings")
		else:		_point = point
		try:

			hh,h, mm,m, ss,s = VALID_TIME_P.fullmatch(_point).group("hh","h", "mm","m", "ss","s")
			H,M,S = hh or h, mm or m, ss or s


			return	H,M, S or "00"
		except		AttributeError:
			raise	ValueError(f"Unable to validate \"{_point}\" time")







