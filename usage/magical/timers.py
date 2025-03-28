from time									import sleep
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.time_turner.timers	import Callstamp
from pygwarts.magical.time_turner.timers	import DIRTtimer
from pygwarts.magical.time_turner.timers	import mostsec
from pygwarts.irma.contrib					import LibraryContrib








@Callstamp
class Counter(Transmutable):

	""" Object "Counter" upon called will emit INFO log about it's __call__ execution time """

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "Counter (optional)"

	def __call__(self):
		for _ in range(1E9): pass








@DIRTtimer(D=1, I=2, R=3, T=27)
class Sleeper(Transmutable):

	"""
		Object "Sleeper" upon called will sleep 27 seconds in total:
			1 second for delay timer "D", then
			10 seconds for it's __call__, then
			2 seconds post delay "I", then
			1 second for delay timer "D" (2/3 iteration of "R"), then
			10 seconds for it's __call__ (2/3 iteration of "R"), then
			2 seconds post delay "I" (2/3 iteration of "R"), then
			1 second for delay timer "D" (3/3 iteration of "R"), then
			will be stopped by "T"
	"""

	def __call__(self): sleep(10)








mostsec(31539600)		# "365 d 1 h"
mostsec(31539599)		# "365 d"
mostsec(31536000)		# "365 d"
mostsec(31535999)		# "364 d 23 h"
mostsec(90000)			# "1 d 1 h"
mostsec(89999)			# "1 d"
mostsec(86400)			# "1 d"
mostsec(86399)			# "23 h 59 m"
mostsec(3660)			# "1 h 1 m"
mostsec(3659)			# "1 h"
mostsec(3600)			# "1 h"
mostsec(3599)			# "59 m 59 s"
mostsec(119)			# "1 m 59 s"
mostsec(60)				# "1 m"
mostsec(59)				# "59 s"
mostsec(.9999)			# "999 ms"
mostsec(.1999)			# "199 ms"
mostsec(.1000)			# "100 ms"
mostsec(.0999)			# "99 ms"
mostsec(.0010)			# "1 ms"
mostsec(.0009999)		# "999 us"
mostsec(.0001000)		# "100 us"
mostsec(.0000999)		# "99 us"
mostsec(.00000100)		# "1 us"
mostsec(.0000009999)	# "999 ns"
mostsec(.0000001000)	# "100 ns"
mostsec(.0000000999)	# "99 ns"
mostsec(.0000000010)	# "1 ns"
mostsec(.0000000001)	# "<1 ns"
mostsec(0)				# "<1 ns"







