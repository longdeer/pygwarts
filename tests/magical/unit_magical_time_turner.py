import	unittest
from	typing							import Dict
from	typing							import Callable
from	typing							import Generator
from	datetime						import datetime
from	datetime						import timedelta
from	pygwarts.magical.time_turner	import TimeTurner
from	pygwarts.tests.magical			import MagicalTestCase








class InitiationCases(MagicalTestCase):

	"""
		Comprehensive initiation set
	"""

	def init_datepoint_matcher(
									self,
									turner	:Callable[[int,int,int],TimeTurner],
									pattern	:Callable[[int,int,int],str],
								):

		for full_year in self.FYEARS:
			for month in self.MONTHS:
				for day	in self.DAYS_31:
					with self.subTest(d=day, m=month, Y=full_year):

						# This looks like a weak method of testing...
						# Must be some more robust idea.
						try:	self.assertEqual(turner(day,month,full_year),pattern(day,month,full_year))
						except	ValueError:
							self.assertRaisesRegex(

								ValueError,
								"day is out of range for month",
								datetime,
								full_year, month, day
							)




	def init_timepoint_matcher(
									self,
									turner	:Callable[[int,int,int],TimeTurner],
									pattern	:Callable[[int,int,int],str],
								):

		"""
			self.HOURS and self.MINSEC are simplified
		"""

		for hour in ( 0, 10, 23 ):
			for minute in ( 0, 15, 33, 59 ):
				for second in ( 0, 28, 42, 59 ):
					with self.subTest(H=hour, M=minute, S=second):
						self.assertEqual(turner(hour, minute, second), pattern(hour, minute, second))








	def test_datepoint_sjoint_1(self):

		for sep in self.DELIMETERS:
			self.init_datepoint_matcher(

				(lambda d,m,Y : TimeTurner(f"{d}{sep}{m}{sep}{Y}").dmY_aspath),
				(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
			)
	def test_datepoint_sjoint_2(self):

		for sep in self.DELIMETERS:
			self.init_datepoint_matcher(

				(lambda d,m,Y : TimeTurner(
					f"{m}{sep}{d}{sep}{Y}").dmY_aspath
					if d <13 else
					TimeTurner(f"{m}{sep}{d}{sep}{Y}").mdY_aspath
				),
				(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
			)
	def test_datepoint_sjoint_3(self):

		for sep in self.DELIMETERS:
			self.init_datepoint_matcher(

				(lambda d,m,Y : TimeTurner(f"{Y}{sep}{m}{sep}{d}").Ymd_aspath),
				(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
			)
	def test_datepoint_sjoint_4(self):

		for sep in self.DELIMETERS:
			self.init_datepoint_matcher(

				(lambda d,m,Y : TimeTurner(
					f"{Y}{sep}{d}{sep}{m}").Ymd_aspath
					if d <13 else
					TimeTurner(f"{Y}{sep}{d}{sep}{m}").Ydm_aspath
				),
				(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
			)




	def test_datepoint_iter_int_day_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ d, str(m), str(Y) ]).dmY_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(m), d, str(Y) ]).dmY_aspath if d <13 else TimeTurner([ str(m), d, str(Y) ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ str(Y), str(m), d ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_day_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(Y), d, str(m) ]).Ymd_aspath if d <13 else TimeTurner([ str(Y), d, str(m) ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_iter_int_month_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(d), m, str(Y) ]).dmY_aspath
				),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_month_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ m, str(d), str(Y) ]).dmY_aspath if d <13 else TimeTurner([ str(m), d, str(Y) ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_month_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ str(Y), m, str(d) ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_month_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(Y), str(d), m ]).Ymd_aspath if d <13 else TimeTurner([ str(Y), str(d), m ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_iter_int_fyear_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ str(d), str(m), Y ]).dmY_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_fyear_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(m), str(d), Y ]).dmY_aspath if d <13 else TimeTurner([ str(m), str(d), Y ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_fyear_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ Y, str(m), str(d) ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_fyear_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ Y, str(d), str(m) ]).Ymd_aspath if d <13 else TimeTurner([ Y, str(d), str(m) ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_iter_int_day_month_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ d, m, str(Y) ]).dmY_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_month_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ m, d, str(Y) ]).dmY_aspath if d <13 else TimeTurner([ m, d, str(Y) ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_month_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ str(Y), m, d ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_day_month_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(Y), d, m ]).Ymd_aspath if d <13 else TimeTurner([ str(Y), d, m ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_iter_int_day_fyear_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ d, str(m), Y ]).dmY_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_fyear_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ str(m), d, Y ]).dmY_aspath if d <13 else TimeTurner([ str(m), d, Y ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_fyear_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ Y, str(m), d ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_day_fyear_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ Y, d, str(m) ]).Ymd_aspath if d <13 else TimeTurner([ Y, d, str(m) ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_iter_int_month_fyear_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ str(d), m, Y ]).dmY_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_month_fyear_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ m, str(d), Y ]).dmY_aspath if d <13 else TimeTurner([ m, str(d), Y ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_month_fyear_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ Y, m, str(d) ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_month_fyear_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ Y, str(d), m ]).Ymd_aspath if d <13 else TimeTurner([ Y, str(d), m ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_iter_int_day_month_fyear_1(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ d, m, Y ]).dmY_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(str(d).zfill(2), str(m).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_month_fyear_2(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ m, d, Y ]).dmY_aspath if d <13 else TimeTurner([ m, d, Y ]).mdY_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(str(m).zfill(2), str(d).zfill(2),Y))
		)
	def test_datepoint_iter_int_day_month_fyear_3(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner([ Y, m, d ]).Ymd_aspath),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(m).zfill(2), str(d).zfill(2)))
		)
	def test_datepoint_iter_int_day_month_fyear_4(self):
		self.init_datepoint_matcher(

			(lambda d,m,Y : TimeTurner(
				[ Y, d, m ]).Ymd_aspath if d <13 else TimeTurner([ Y, d, m ]).Ydm_aspath
			),
			(lambda d,m,Y : "%s/%s/%s"%(Y,str(d).zfill(2), str(m).zfill(2)))
		)




	def test_datepoint_epoch_init(self):

		for full_year in ( 2019,2020 ):
			for month in ( 2,6,10 ):
				for day in ( 1,7,10,22 ):
					for hour in ( 0,3,13,22 ):
						for minute in ( 0,1,11,33,42,59 ):
							for second in ( 0,2,22,36,59 ):
								with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

									stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
									self.assertIsInstance(stamp, float)
									self.assertEqual(TimeTurner(stamp).epoch, stamp)
									self.assertEqual(TimeTurner(int(stamp)).epoch, stamp)




	def test_datepoint_TimeTurner_init(self):

		full_year = 2019
		for month in ( 2,10 ):
			for day in ( 1,11,22 ):
				for hour in ( 0,13 ):
					for minute in ( 42,59 ):
						for second in ( 0,36 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(TimeTurner(TimeTurner(stamp)).epoch, stamp.timestamp())




	def test_datepoint_datetime_init(self):

		full_year = 2020
		for month in ( 6,2,5 ):
			for day in ( 7,10,25 ):
				for hour in (3,22 ):
					for minute in ( 0,59 ):
						for second in ( 36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(TimeTurner(stamp).epoch, stamp.timestamp())








	def test_timepoint_HM_sjoint(self):

		for sep in list(self.DELIMETERS) + [ "" ]:
			self.init_timepoint_matcher(

				(lambda H,M,_ : TimeTurner(
					timepoint="%s%s%s"%(str(H).zfill(2), sep, str(M).zfill(2))).HM_asjoin
				),
				(lambda H,M,_ : "%s%s"%(str(H).zfill(2), str(M).zfill(2)))
			)




	def test_timepoint_HM_iter_int_H(self):
		self.init_timepoint_matcher(

			(lambda H,M,_ : TimeTurner(timepoint=[ H,str(M) ]).HM_asjoin),
			(lambda H,M,_ : "%s%s"%(str(H).zfill(2), str(M).zfill(2)))
		)
	def test_timepoint_HM_iter_int_M(self):
		self.init_timepoint_matcher(

			(lambda H,M,_ : TimeTurner(timepoint=[ str(H),M ]).HM_asjoin),
			(lambda H,M,_ : "%s%s"%(str(H).zfill(2), str(M).zfill(2)))
		)
	def test_timepoint_HM_iter_int_HM(self):
		self.init_timepoint_matcher(

			(lambda H,M,_ : TimeTurner(timepoint=[ H,M ]).HM_asjoin),
			(lambda H,M,_ : "%s%s"%(str(H).zfill(2), str(M).zfill(2)))
		)




	def test_timepoint_HMS_sjoint(self):

		for sep in list(self.DELIMETERS) + [ "" ]:
			self.init_timepoint_matcher(

				(lambda H,M,S : TimeTurner(

					timepoint="%s%s%s%s%s"%(

						str(H).zfill(2), sep, str(M).zfill(2), sep, str(S).zfill(2))

					).HMS_asjoin
				),
				(lambda H,M,S : "%s%s%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
			)




	def test_timepoint_HMS_iter_int_H(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ H,str(M),str(S) ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)
	def test_timepoint_HMS_iter_int_M(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ str(H),M,str(S) ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)
	def test_timepoint_HMS_iter_int_S(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ str(H),str(M),S ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)
	def test_timepoint_HMS_iter_int_HM(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ H,M,str(S) ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)
	def test_timepoint_HMS_iter_int_HS(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ H,str(M),S ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)
	def test_timepoint_HMS_iter_int_MS(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ str(H),M,S ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)
	def test_timepoint_HMS_iter_int_HMS(self):
		self.init_timepoint_matcher(

			(lambda H,M,S : TimeTurner(timepoint=[ H,M,S ]).HMS_ascolon),
			(lambda H,M,S : "%s:%s:%s"%(str(H).zfill(2), str(M).zfill(2), str(S).zfill(2)))
		)




	def test_timepoint_epoch_init(self):

		stamp = datetime.now()
		self.assertIsInstance(stamp.timestamp(), float)
		self.assertEqual(TimeTurner(timepoint=stamp.timestamp()).epoch, stamp.timestamp())
		self.assertEqual(TimeTurner(timepoint=int(stamp.timestamp())).epoch, int(stamp.timestamp()))
	def test_timepoint_TimeTurner_init(self):

		stamp = datetime.now()
		self.assertEqual(TimeTurner(TimeTurner(timepoint=stamp)).epoch, stamp.timestamp())
	def test_timepoint_datetime_init(self):

		stamp = datetime.now()
		self.assertEqual(TimeTurner(timepoint=stamp).epoch, stamp.timestamp())
















	def test_datepoint_sjoint_timepoint_sjoint_epoch_match(self):

		full_year = 1991
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								self.assertEqual(

									TimeTurner(
										f"{day}/{month}/{full_year}",f"{hour}:{minute}:{second}"
									).epoch,
									datetime(full_year, month, day, hour, minute, second).timestamp()
								)




	def test_datepoint_sjoint_timepoint_iter_epoch_match(self):

		full_year = 1992
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								self.assertEqual(

									TimeTurner(
										f"{day}/{month}/{full_year}",[ hour, minute, second ]
									).epoch,
									datetime(full_year, month, day, hour, minute, second).timestamp()
								)




	def test_datepoint_sjoint_timepoint_epoch_epoch_match(self):

		full_year = 1993
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(
									TimeTurner(f"{day}/{month}/{full_year}", stamp).epoch, stamp
								)
								self.assertEqual(

									TimeTurner(f"{day}/{month}/{full_year}", int(stamp)).epoch,
									int(stamp)
								)




	def test_datepoint_sjoint_timepoint_TimeTurner_epoch_match(self):

		full_year = 1994
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(

									TimeTurner(f"{day}/{month}/{full_year}", TimeTurner(stamp)).epoch,
									stamp
								)




	def test_datepoint_sjoint_timepoint_datetime_epoch_match(self):

		full_year = 1995
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(

									TimeTurner(f"{day}/{month}/{full_year}", stamp).epoch,
									stamp.timestamp()
								)








	def test_datepoint_iter_timepoint_sjoint_epoch_match(self):

		full_year = 1996
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								self.assertEqual(

									TimeTurner(

										[ day, month, full_year ], f"{hour}:{minute}:{second}"
									).epoch,
									datetime(full_year, month, day, hour, minute, second).timestamp()
								)




	def test_datepoint_iter_timepoint_iter_epoch_match(self):

		full_year = 1997
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								self.assertEqual(

									TimeTurner(

										[ day, month, full_year ], [ hour, minute, second ]
									).epoch,
									datetime(full_year, month, day, hour, minute, second).timestamp()
								)




	def test_datepoint_iter_timepoint_epoch_epoch_match(self):

		full_year = 1998
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(
									TimeTurner([ day, month, full_year ], stamp).epoch, stamp
								)
								self.assertEqual(
									TimeTurner([ day, month, full_year ], int(stamp)).epoch, int(stamp)
								)




	def test_datepoint_iter_timepoint_TimeTurner_epoch_match(self):

		full_year = 1999
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(

									TimeTurner([ day, month, full_year ], TimeTurner(stamp)).epoch,
									stamp
								)




	def test_datepoint_iter_timepoint_datetime_epoch_match(self):

		full_year = 2000
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(

									TimeTurner([ day, month, full_year ], stamp).epoch,
									stamp.timestamp()
								)








	def test_datepoint_epoch_timepoint_sjoint_epoch_match(self):

		full_year = 2001
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(
									TimeTurner(stamp, f"{hour}:{minute}:{second}").epoch, stamp
								)
								self.assertEqual(
									TimeTurner(int(stamp), f"{hour}:{minute}:{second}").epoch, stamp
								)




	def test_datepoint_epoch_timepoint_iter_epoch_match(self):

		full_year = 2002
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(
									TimeTurner(stamp, [ hour, minute, second ]).epoch, stamp
								)
								self.assertEqual(
									TimeTurner(int(stamp), [ hour, minute, second ]).epoch, stamp
								)




	def test_datepoint_epoch_timepoint_epoch_epoch_match(self):

		full_year = 2003
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(TimeTurner(stamp, stamp).epoch, stamp)
								self.assertEqual(TimeTurner(int(stamp), stamp).epoch, stamp)
								self.assertEqual(TimeTurner(stamp, int(stamp)).epoch, int(stamp))
								self.assertEqual(TimeTurner(int(stamp), int(stamp)).epoch, int(stamp))




	def test_datepoint_epoch_timepoint_TimeTurner_epoch_match(self):

		full_year = 2004
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(TimeTurner(stamp, TimeTurner(stamp)).epoch, stamp)
								self.assertEqual(TimeTurner(int(stamp), TimeTurner(stamp)).epoch, stamp)




	def test_datepoint_epoch_timepoint_datetime_epoch_match(self):

		full_year = 2005
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(
									TimeTurner(stamp.timestamp(), stamp).epoch, stamp.timestamp()
								)
								self.assertEqual(
									TimeTurner(int(stamp.timestamp()), stamp).epoch, stamp.timestamp()
								)








	def test_datepoint_TimeTurner_timepoint_sjoint_epoch_match(self):

		full_year = 2006
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								self.assertEqual(

									TimeTurner(

										TimeTurner([ day, month, full_year ]),
										f"{hour}:{minute}:{second}"

									).epoch,
									datetime(full_year, month, day, hour, minute, second).timestamp()
								)




	def test_datepoint_TimeTurner_timepoint_iter_epoch_match(self):

		full_year = 2007
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								self.assertEqual(

									TimeTurner(

										TimeTurner([ day, month, full_year ]),
										[ hour, minute, second ]

									).epoch,
									datetime(full_year, month, day, hour, minute, second).timestamp()
								)




	def test_datepoint_TimeTurner_timepoint_epoch_epoch_match(self):

		full_year = 2008
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(

									TimeTurner(

										TimeTurner([ day, month, full_year ]), stamp
									).epoch, stamp
								)
								self.assertEqual(

									TimeTurner(TimeTurner([ day, month, full_year ]), int(stamp)
									).epoch, int(stamp)
								)




	def test_datepoint_TimeTurner_timepoint_TimeTurner_epoch_match(self):

		full_year = 2009
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second).timestamp()
								self.assertEqual(

									TimeTurner(
										TimeTurner([ day, month, full_year ]), TimeTurner(stamp)
									).epoch, stamp
								)




	def test_datepoint_TimeTurner_timepoint_datetime_epoch_match(self):

		full_year = 2010
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(

									TimeTurner(TimeTurner([ day, month, full_year ]), stamp
									).epoch, stamp.timestamp()
								)








	def test_datepoint_datetime_timepoint_sjoint_epoch_match(self):

		full_year = 2011
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(

									TimeTurner(stamp, f"{hour}:{minute}:{second}"
									).epoch, stamp.timestamp()
								)




	def test_datepoint_datetime_timepoint_iter_epoch_match(self):

		full_year = 2012
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(
									TimeTurner(stamp, [ hour, minute, second ]).epoch, stamp.timestamp()
								)




	def test_datepoint_datetime_timepoint_epoch_epoch_match(self):

		full_year = 2013
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(
									TimeTurner(stamp, stamp.timestamp()).epoch, stamp.timestamp()
								)
								self.assertEqual(

									TimeTurner(stamp, int(stamp.timestamp())).epoch,
									int(stamp.timestamp())
								)




	def test_datepoint_datetime_timepoint_TimeTurner_epoch_match(self):

		full_year = 2014
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(
									TimeTurner(stamp, TimeTurner(stamp)).epoch, stamp.timestamp()
								)




	def test_datepoint_datetime_timepoint_datetime_epoch_match(self):

		full_year = 2015
		for month in ( 2,6,10 ):
			for day in ( 1,7,10,22 ):
				for hour in ( 0,3,13,22 ):
					for minute in ( 0,1,11,33,42,59 ):
						for second in ( 0,2,22,36,59 ):
							with self.subTest(d=day, m=month, Y=full_year, H=hour, M=minute, S=second):

								stamp = datetime(full_year, month, day, hour, minute, second)
								self.assertEqual(TimeTurner(stamp, stamp).epoch, stamp.timestamp())








	def test_datetime_travel_inits(self):

		stamp = datetime(2020, 10, 20, 4, 26, 9)
		travels_keys = list(self.travels)
		L = len(travels_keys)


		def casegen(i :int, buffer :Dict[str,int]) -> Generator[Dict[str,int], None,None] :

			if	buffer : yield buffer
			for j in range(i,L):

				current_key = travels_keys[j]
				buffer[current_key] = self.travels[current_key]
				yield from casegen(j +1, buffer)

				buffer[current_key] = -self.travels[current_key]
				yield from casegen(j +1, buffer)

				del buffer[current_key]


		for case in casegen(0,{}):
			self.assertEqual(

				TimeTurner(stamp, **case).epoch,
				(stamp + timedelta(**case)).timestamp()
			)




	def test_datetime_months_travel_inits(self):

		stamp = datetime(2020, 10, 20, 4, 26, 9)

		self.assertEqual(TimeTurner(stamp, months=1).POINT, datetime(2020, 11, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=2).POINT, datetime(2020, 12, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=3).POINT, datetime(2021, 1, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=4).POINT, datetime(2021, 2, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=5).POINT, datetime(2021, 3, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=6).POINT, datetime(2021, 4, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=7).POINT, datetime(2021, 5, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=8).POINT, datetime(2021, 6, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=9).POINT, datetime(2021, 7, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=10).POINT, datetime(2021, 8, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=11).POINT, datetime(2021, 9, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=12).POINT, datetime(2021, 10, 1, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=13).POINT, datetime(2021, 11, 1, 4, 26, 9))

		self.assertEqual(TimeTurner(stamp, months=-1).POINT, datetime(2020, 9, 30, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-2).POINT, datetime(2020, 8, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-3).POINT, datetime(2020, 7, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-4).POINT, datetime(2020, 6, 30, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-5).POINT, datetime(2020, 5, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-6).POINT, datetime(2020, 4, 30, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-7).POINT, datetime(2020, 3, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-8).POINT, datetime(2020, 2, 29, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-9).POINT, datetime(2020, 1, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-10).POINT, datetime(2019, 12, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-11).POINT, datetime(2019, 11, 30, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-12).POINT, datetime(2019, 10, 31, 4, 26, 9))
		self.assertEqual(TimeTurner(stamp, months=-13).POINT, datetime(2019, 9, 30, 4, 26, 9))








	def test_datepoint_sjoint_epoch_match(self):

		for full_year in self.FYEARS:
			for month in self.MONTHS:
				for day in self.DAYS_31:
					with self.subTest(d=day, m=month, Y=full_year):

						try:

							self.assertEqual(

								TimeTurner(f"{day}/{month}/{full_year}").epoch,
								datetime(full_year, month, day).timestamp()
							)
						except	ValueError:
							self.assertRaisesRegex(

								ValueError,
								"day is out of range for month",
								datetime,
								full_year, month, day
							)




	def test_datepoint_iter_epoch_match(self):

		for full_year in self.FYEARS:
			for month in self.MONTHS:
				for day in self.DAYS_31:
					with self.subTest(d=day, m=month, Y=full_year):

						try:

							self.assertEqual(

								TimeTurner([ day, month, full_year ]).epoch,
								datetime(full_year, month, day).timestamp()
							)
						except	ValueError:
							self.assertRaisesRegex(

								ValueError,
								"day is out of range for month",
								datetime,
								full_year, month, day
							)
















class OperationsCases(MagicalTestCase):

	"""
		Operational methods and properties
	"""

	def setUp(self): self.stamp = TimeTurner([ 20, 10, 2010 ],[ 3,2,8 ])
	def test_sight(self):

		probe = self.stamp
		self.assertEqual(id(self.stamp), id(probe))

		sight = self.stamp.sight()
		self.assertEqual(self.stamp, sight)
		self.assertNotEqual(id(self.stamp), id(sight))

		sight = self.stamp.sight(months=1)
		self.assertEqual(sight.dmY_aspath, "01/11/2010")
		self.assertNotEqual(self.stamp, sight)
		self.assertNotEqual(id(self.stamp), id(sight))

		sight = self.stamp.sight(months=-1)
		self.assertEqual(sight.dmY_aspath, "30/09/2010")
		self.assertNotEqual(self.stamp, sight)
		self.assertNotEqual(id(self.stamp), id(sight))




	def test_positive_diff(self):

		probe = self.stamp
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(TimeTurner(self.stamp, minutes=-1))
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, 60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(datetime(2010, 10, 20, 3, 1, 8))
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, 60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(datetime(2010, 10, 20, 3, 1, 8).timestamp())
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, 60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(int(datetime(2010, 10, 20, 3, 1, 8).timestamp()))
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, 60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(f"{datetime(2010, 10, 20, 3, 1, 8).timestamp()}")
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, 60.)
		self.assertEqual(id(self.stamp), id(probe))




	def test_negative_diff(self):

		probe = self.stamp
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(TimeTurner(self.stamp, minutes=1))
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, -60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(datetime(2010, 10, 20, 3, 3, 8))
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, -60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(datetime(2010, 10, 20, 3, 3, 8).timestamp())
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, -60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(int(datetime(2010, 10, 20, 3, 3, 8).timestamp()))
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, -60.)
		self.assertEqual(id(self.stamp), id(probe))

		diff = self.stamp.diff(f"{datetime(2010, 10, 20, 3, 3, 8).timestamp()}")
		self.assertIsInstance(diff, float)
		self.assertEqual(diff, -60.)
		self.assertEqual(id(self.stamp), id(probe))




	def test_getattr(self):

		self.assertEqual(f"{self.stamp.dmY_aspath} {self.stamp.HMS_aspath}", "20/10/2010 03/02/08")
		self.assertEqual(f"{self.stamp.dmY_aswpath} {self.stamp.HMS_aswpath}", "20\\10\\2010 03\\02\\08")
		self.assertEqual(f"{self.stamp.dmY_ascolon} {self.stamp.HMS_ascolon}", "20:10:2010 03:02:08")
		self.assertEqual(f"{self.stamp.dmY_asjoin} {self.stamp.HMS_asjoin}", "20102010 030208")
		self.assertEqual(f"{self.stamp.dmY_spaced} {self.stamp.HMS_spaced}", "20 10 2010 03 02 08")
		self.assertEqual(f"{self.stamp.dmY_dashed} {self.stamp.HMS_dashed}", "20-10-2010 03-02-08")




	def test_travels(self):

		probe = TimeTurner(self.stamp)
		self.assertEqual(self.stamp, probe)
		self.assertNotEqual(id(self.stamp), id(probe))

		traveled = probe.travel(**self.travels)
		self.assertNotEqual(self.stamp, probe)
		self.assertNotEqual(self.stamp, traveled)
		self.assertEqual(probe, traveled)
		self.assertEqual(id(probe), id(traveled))
		self.assertNotEqual(id(self.stamp), id(probe))
		self.assertNotEqual(id(self.stamp), id(traveled))




	def test_is_first_day(self):

		self.assertFalse(self.stamp.is_first_day)
		self.assertTrue(self.stamp.sight(days=-19).is_first_day)

	def test_is_leap_year(self):

		self.assertFalse(self.stamp.is_leap_year)
		self.assertTrue(self.stamp.sight(months=-24).is_leap_year)




	def test_add(self):

		probe = self.stamp + 100500
		self.assertIsInstance(probe, TimeTurner)
		self.assertNotEqual(self.stamp, probe)
		self.assertNotEqual(id(self.stamp), id(probe))
		self.assertEqual(probe.epoch, self.stamp.epoch + 100500)




	def test_sub(self):

		probe = self.stamp - 100500
		self.assertIsInstance(probe, TimeTurner)
		self.assertNotEqual(self.stamp, probe)
		self.assertNotEqual(id(self.stamp), id(probe))
		self.assertEqual(probe.epoch, self.stamp.epoch - 100500)




	def test_eq(self):

		self.assertEqual(self.stamp, TimeTurner(self.stamp))
		self.assertEqual(self.stamp, datetime(2010, 10, 20, 3, 2, 8))
		self.assertEqual(self.stamp, self.stamp.epoch)
		self.assertEqual(self.stamp, int(self.stamp.epoch))
		self.assertEqual(self.stamp, f"{self.stamp.epoch}")
		self.assertEqual(self.stamp, f"{int(self.stamp.epoch)}")




	def test_neq(self):

		self.assertNotEqual(self.stamp, TimeTurner(self.stamp, seconds=1))
		self.assertNotEqual(self.stamp, datetime(2010, 10, 20, 3, 2, 9))
		self.assertNotEqual(self.stamp, self.stamp.epoch +1)
		self.assertNotEqual(self.stamp, int(self.stamp.epoch) +1)
		self.assertNotEqual(self.stamp, f"{self.stamp.epoch +1}")
		self.assertNotEqual(self.stamp, f"{int(self.stamp.epoch) +1}")




	def test_gt(self):

		self.assertGreater(self.stamp, TimeTurner(self.stamp, seconds=-1))
		self.assertGreater(self.stamp, datetime(2010, 10, 20, 3, 2, 7))
		self.assertGreater(self.stamp, self.stamp.epoch -1)
		self.assertGreater(self.stamp, int(self.stamp.epoch) -1)
		self.assertGreater(self.stamp, f"{self.stamp.epoch -1}")
		self.assertGreater(self.stamp, f"{int(self.stamp.epoch) -1}")




	def test_ge(self):

		self.assertGreaterEqual(self.stamp, TimeTurner(self.stamp))
		self.assertGreaterEqual(self.stamp, datetime(2010, 10, 20, 3, 2, 8))
		self.assertGreaterEqual(self.stamp, self.stamp.epoch)
		self.assertGreaterEqual(self.stamp, int(self.stamp.epoch))
		self.assertGreaterEqual(self.stamp, f"{self.stamp.epoch}")
		self.assertGreaterEqual(self.stamp, f"{int(self.stamp.epoch)}")




	def test_lt(self):

		self.assertLess(self.stamp, TimeTurner(self.stamp, seconds=1))
		self.assertLess(self.stamp, datetime(2010, 10, 20, 3, 2, 9))
		self.assertLess(self.stamp, self.stamp.epoch +1)
		self.assertLess(self.stamp, int(self.stamp.epoch) +1)
		self.assertLess(self.stamp, f"{self.stamp.epoch +1}")
		self.assertLess(self.stamp, f"{int(self.stamp.epoch) +1}")




	def test_le(self):

		self.assertLessEqual(self.stamp, TimeTurner(self.stamp))
		self.assertLessEqual(self.stamp, datetime(2010, 10, 20, 3, 2, 8))
		self.assertLessEqual(self.stamp, self.stamp.epoch)
		self.assertLessEqual(self.stamp, int(self.stamp.epoch))
		self.assertLessEqual(self.stamp, f"{self.stamp.epoch}")
		self.assertLessEqual(self.stamp, f"{int(self.stamp.epoch)}")








if __name__ == "__main__" : unittest.main(verbosity=2)







