from time												import time
from time												import sleep
from multiprocessing									import Process
from typing												import Any
from typing												import Callable
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import Transmutation
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.magical.spells							import flagrate








class Callstamp(Transmutation):

	"""
		Utility decorator, that allows timestamping __call__ invocation of the decorated Transmutable
		object. Creates 2 time.time points, one before and one after the decorated object invocation,
		calculates the difference in seconds between them and emits corresponding info message. The
		result of decorated object __call__ will be the value to return. If decorated object doesn't
		implement __call__, raises corresponding TypeError, the way any non callable should.
	"""

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :
		class Callstamped(geminio(layer)):

			def __call__(self, *args, **kwargs) -> Any :

				if	hasattr(super(), "__call__"):

					start_point	= time()
					self.loggy.debug(f"Start point {start_point} created")


					output		= super().__call__(*args, **kwargs)
					end_point	= time()


					self.loggy.debug(f"End point {end_point} created")
					self.loggy.info(f"{self} finished in {end_point - start_point} seconds")


					return	output


				raise TypeError(f"{self} object is not callable")
		return	Callstamped








def mostsec(value :int | float | str, positive=False) -> str | None :

	"""
		Utility function that converts numerical value into a concise informative string representation
		of a time period in seconds, which that numerical value represents. Accepts any floatable value,
		such as int, float, exponent and their string representations. If "value" is negative, the absolute
		value will be taken. As "value" will be mandatory converted to float beforehand, any Exception raise
		will mean invalid "value" and "mostsec" will silently return None. The logic behind actual
		converting is inferring of at most two biggest measures for the "value", so the bigger "value" the
		more it will be truncated. There are upper "day" and lower "nano second" bounds. As conversion
		logic doesn't suggest 0 as a value, "mostsec" arithmetic considers 0 to be less than 1 nano second.
		The boolean flag "positive" toggles which value will be returned for a 0 "value" conversion. If
		positive=False (by default) the return value is "<1 ns", and None otherwise. This rule refers to
		such constraint as values less than 1 nano second are considered infinitesimals, so they might
		be approximated to 0, so positive=True will refer to negation of not positive values use.

		Comprehensive description for various values conversions:

			31539600	-> 365 d 1 h
			31539599	-> 365 d
			31536000	-> 365 d
			31535999	-> 364 d 23 h
			90000		-> 1 d 1 h
			89999		-> 1 d
			86400		-> 1 d
			86399		-> 23 h 59 m
			3660		-> 1 h 1 m
			3659		-> 1 h
			3600		-> 1 h
			3599		-> 59 m 59 s
			119			-> 1 m 59 s
			60 			-> 1 m
			59 			-> 59 s
			.9999		-> 999 ms
			.1999		-> 199 ms
			.1000		-> 100 ms
			.0999		-> 99 ms
			.0010		-> 1 ms
			.0009999	-> 999 us
			.0001000	-> 100 us
			.0000999	-> 99 us
			.00000100	-> 1 us
			.0000009999	-> 999 ns
			.0000001000	-> 100 ns
			.0000000999	-> 99 ns
			.0000000010	-> 1 ns
			.0000000001	-> <1 ns
			0			-> <1 ns
	"""

	try:	TIME = abs(float(str(value)))
	except:	return
	else:

		if	not positive or (positive and TIME):

			mm,SS = divmod(TIME, 60)
			hh,MM = map(int, divmod(mm, 60))
			DD,HH = map(int, divmod(hh, 24))


			if	mm <1 :
				if	SS <1 :
					if	SS*1_000 <1 :
						if	SS*1_000_000 <1 :
							if	SS*1_000_000_000 <1 :


								return	"<1 ns"
							return	f"{int(SS*1_000_000_000)} ns"
						return	f"{int(SS*1_000_000)} us"
					return	f"{int(SS*1_000)} ms"
				return	f"{int(SS)} s"


			if	DD <1 :
				if	hh <1 :


					return	f"{MM} m" if SS <1 else f"{MM} m {int(SS)} s"
				return	f"{HH} h" if MM <1 else f"{HH} h {MM} m"
			return	f"{DD} d" if HH <1 else f"{DD} d {HH} h"








class mostsecfmt(ControlledTransmutation):

	"""
		Utility decorator that integrates "mostsec" function into mutable chain. Operates only with
		__call__ method of decorated Transmutable object. Raises TypeError in case __call__ not
		implemented for a decorated layer, the way any non callable should. As this decorator
		acts as numeric value interceptor, which must convert that value in some representing
		string, any invalid values will result None return from "mostsec", which provides conversion.
	"""

	def __init__(self, *, positive :bool): self.positive = positive
	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		positive = self.positive


		class MostSec(geminio(layer)):
			def __call__(self, *args, **kwargs) -> str | None :

				if	hasattr(super(), "__call__"):
					if	(seconds := super().__call__(*args, **kwargs)) is not None :


						self.loggy.debug(f"Received \"{seconds}\" second{flagrate(seconds)} to format")
						return	mostsec(seconds, positive)


					else:	self.loggy.debug("Seconds to format was not received")
				else:		raise TypeError(f"{self} object is not callable")


		return	MostSec








class DIRTtimer(ControlledTransmutation):

	"""
		Utility decorator that serves as a time dispatcher for a decorated Transmutable object invocation.
		Accepts following numeric only key-word arguments:
			D		- time in seconds for delay before decorated Transmutable object invocation;
			I		- time in seconds for delay after decorated Transmutable object invocation;
			R		- counter for how many times decorated Transmutable object will be invoked;
			T		- time in seconds to terminate decorated Transmutable object invocation;
			spawner	- callable object to spawn process manageable for termination.
		Four numeric values must be convertible to float, and "T","D" and "I" will remain float, cause they
		represents time in seconds. The "R" value will be additionally converted to int, cause it will be
		used as iteration counter. This decorator relies on decorated Transmutable object implements
		__call__, which will be the target for dispatching, otherwise TypeError will be raised. Basically
		all the "DIRTtimer" does it's calling decorated __call__ with delay "D" and timer "T", with post
		delay "I", and repeats it "R" times. Delays "D" and "I" are just time.sleep calls, repetition of
		"R" times is just a for loop. The most crucial thing is the implementation of termination with
		timer "T" by "spawner". If T=0 (by default) decorated __call__ will be just invoked, according to
		"D","R","I" options. For any number of seconds, other than 0, "spawner" must create a parallel
		object, which will invoke decorated __call__ and stop it when the timer "T", that is time.sleep
		invocation, will be gone. By default "spawner" utilizes "multiprocessing" standard library module,
		which "Process" object work depends on running platform. For POSIX "Process.start" will use "fork"
		context and this is the originally designed and tested feature. For NT "Process.start" uses "spawn"
		context which causes serialization error by "pickle" module, involved in "multiprocessing". In that
		case, "spawner" should be set to any other object, capable of handling "spawn" context. With T=0
		no new spawns occur, so decorated Transmutable object persist through all "D","R","I" manipulations.
		For any 0<T every new spawn means new decorated object, so no modification can persist via "R"
		repetitions. Also, as decorated __call__ repeatedly invocation is not a subject for results
		collecting, there is no return value, so this must be handled in decorated Transmutable object.

		--------------------------------------------------------------------------------------------------
		| This class designed as a very simple and concise way of objects calling manipulation, so the	 |
		| termination part ain't complies modern best practices, and since python3.12 "fork()" seems to	 |
		| be deprecated. The use of such functionality (termination) must be the subject to consider,	 |
		| unless the other solution becomes the part of pygwarts code base.								 |
		--------------------------------------------------------------------------------------------------
	"""

	def __init__(
					self,
					*,
					D		:int | float | str		=0,			# Delay timer
					I		:int | float | str		=0,			# Delay between intervals, also post delay
					R		:int | float | str		=1,			# Repetition counter
					T		:int | float | str		=0,			# Termination timer
					spawner	:Callable[[Any],Any]	=Process	# Object to spawn a terminatable process
				):


		try:	self.delay_sleep = abs(float(D))
		except:	raise ValueError(f"Delay timer \"{D}\" is invalid")


		try:	self.interval_sleep = abs(float(I))
		except:	raise ValueError(f"Interval timer \"{I}\" is invalid")


		try:	self.repeat_times = abs(int(float(R)))
		except:	raise ValueError(f"Repetition counter \"{R}\" is invalid")


		try:	self.terminate_sleep = abs(float(T))
		except:	raise ValueError(f"Termination timer \"{T}\" is invalid")


		if(
				callable(spawner) and
				callable(getattr(spawner, "start", None)) and
				callable(getattr(spawner, "terminate", None))
		):		self.spawner = spawner
		else:	raise ValueError(f"Process spawner \"{spawner}\" is invalid")


	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :


		D = self.delay_sleep
		I = self.interval_sleep
		R = self.repeat_times
		T = self.terminate_sleep
		spawner = self.spawner


		class DIRT(geminio(layer)):
			def __call__(self, *args, **kwargs):


				if	hasattr(super(), "__call__"):


					self.loggy.debug(f"Delay start timer {D} second{flagrate(D)}")
					self.loggy.debug(f"Interval delay {I} second{flagrate(I)}")
					self.loggy.debug(f"Repetition counter {R} time{flagrate(R)}")
					self.loggy.debug(f"Termination timer {T} second{flagrate(T)}")
					self.loggy.debug(f"Caller arguments: {args}")
					self.loggy.debug(f"Caller keyword arguments: {kwargs}")


					for i in range(R):
						self.loggy.debug(f"DIRT iteration {i +1}")


						if	D:
							sleep(D)
							self.loggy.debug(f"Delay {D} second{flagrate(D)} for {self} performed")


						if	T:
							self.loggy.info(f"Starting {T} second{flagrate(T)} timer for {self}")


							process = spawner(target=super().__call__, args=args, kwargs=kwargs,)
							process.start()
							sleep(T)
							process.terminate()


							self.loggy.debug(f"Process {self} terminated")
						else:
							super().__call__(*args, **kwargs)


						if	I:
							sleep(I)
							self.loggy.debug(f"Interval {I} second{flagrate(I)} for {self} performed")


				else:	raise TypeError(f"{self} object is not callable")


		return	DIRT







