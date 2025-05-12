import	re
import	unittest
from	typing								import List
from	typing								import Generator
from	datetime							import datetime
from	pygwarts.magical.time_turner.utils	import MONTHS_NAME_P
from	pygwarts.magical.time_turner.utils	import VALID_29_DAYS
from	pygwarts.magical.time_turner.utils	import VALID_30_DAYS
from	pygwarts.magical.time_turner.utils	import VALID_31_DAYS
from	pygwarts.magical.time_turner.utils	import VALID_29_MONTHS
from	pygwarts.magical.time_turner.utils	import VALID_30_MONTHS
from	pygwarts.magical.time_turner.utils	import VALID_31_MONTHS
from	pygwarts.magical.time_turner.utils	import VALID_TIME_P
from	pygwarts.magical.time_turner.utils	import VALID_DATE_1_P
from	pygwarts.magical.time_turner.utils	import VALID_DATE_2_P
from	pygwarts.magical.time_turner.utils	import VALID_DATE_3_P
from	pygwarts.magical.time_turner.utils	import VALID_DATE_4_P
from	pygwarts.magical.time_turner.utils	import DATETIME_1_P
from	pygwarts.magical.time_turner.utils	import DATETIME_2_P
from	pygwarts.magical.time_turner.utils	import DATETIME_3_P
from	pygwarts.magical.time_turner.utils	import DATETIME_4_P
from	pygwarts.magical.time_turner.utils	import hundscale
from	pygwarts.tests.magical				import MagicalTestCase








class PatternsCases(MagicalTestCase):

	"""
		time_turner.utils
	"""

	def test_MONTHS_NAME_P_pattern(self):
		def casesgen(i :int, source :List[str]) -> Generator[str, None,None] :

			yield "".join(source)
			for j in range(i, len(source)):

				source[j] = source[j].upper()
				yield from casesgen(j +1,source)
				source[j] = source[j].lower()

		for month in self.months:
			for case in casesgen(0, list(month)):
				with self.subTest(month=month, case=case):
					self.assertTrue(MONTHS_NAME_P.fullmatch(case))

			for case in casesgen(0, list(month)[:3]):
				with self.subTest(month=month, case=case):
					self.assertTrue(MONTHS_NAME_P.fullmatch(case))




	def test_VALID_29_DAYS_pattern(self):

		for day in self.DAYS_29:
			probe1 = str(day)
			probe2 = str(day).zfill(2)

			self.assertEqual(re.fullmatch(VALID_29_DAYS, probe1).group("tnd"), probe1)
			self.assertEqual(re.fullmatch(VALID_29_DAYS, probe2).group("tnd"), probe2)




	def test_VALID_30_DAYS_pattern(self):

		for day in self.DAYS_30:
			probe1 = str(day)
			probe2 = str(day).zfill(2)

			self.assertEqual(re.fullmatch(VALID_30_DAYS, probe1).group("thd"), probe1)
			self.assertEqual(re.fullmatch(VALID_30_DAYS, probe2).group("thd"), probe2)




	def test_VALID_31_DAYS_pattern(self):

		for day in self.DAYS_31:
			probe1 = str(day)
			probe2 = str(day).zfill(2)

			self.assertEqual(re.fullmatch(VALID_31_DAYS, probe1).group("tod"), probe1)
			self.assertEqual(re.fullmatch(VALID_31_DAYS, probe2).group("tod"), probe2)




	def test_VALID_29_MONTHS_pattern(self):

		for month in self.MONTHS:
			probe1 = str(month)
			probe2 = str(month).zfill(2)

			self.assertEqual(re.fullmatch(VALID_29_MONTHS, probe1).group("allM"), probe1)
			self.assertEqual(re.fullmatch(VALID_29_MONTHS, probe2).group("allM"), probe2)




	def test_VALID_30_MONTHS_pattern(self):

		for month in self.MONTHS:
			probe1 = str(month)
			probe2 = str(month).zfill(2)

			if	month in ( 4,6,9,11 ):

				self.assertEqual(re.fullmatch(VALID_30_MONTHS, probe1).group("thdM"), probe1)
				self.assertEqual(re.fullmatch(VALID_30_MONTHS, probe2).group("thdM"), probe2)
			else:
				self.assertFalse(re.fullmatch(VALID_30_MONTHS, probe1))
				self.assertFalse(re.fullmatch(VALID_30_MONTHS, probe2))




	def test_VALID_31_MONTHS_pattern(self):

		for month in self.MONTHS:
			probe1 = str(month)
			probe2 = str(month).zfill(2)

			if	month in ( 1,3,5,7,8,10,12 ):

				self.assertEqual(re.fullmatch(VALID_31_MONTHS, probe1).group("todM"), probe1)
				self.assertEqual(re.fullmatch(VALID_31_MONTHS, probe2).group("todM"), probe2)
			else:
				self.assertFalse(re.fullmatch(VALID_31_MONTHS, probe1))
				self.assertFalse(re.fullmatch(VALID_31_MONTHS, probe2))




	def test_VALID_TIME_P_HM_pattern(self):

		for H in self.HOURS:
			for M in self.MINSEC:
				for sep in list(self.DELIMETERS) + [ "" ]:

					HH = str(H).zfill(2)
					MM = str(M).zfill(2)

					probe1 = f"{HH}{sep}{MM}"
					hh,h, mm,m = VALID_TIME_P.fullmatch(probe1).group("hh", "h", "mm", "m")

					with self.subTest(probe=probe1, hh=hh, h=h, mm=mm, m=m, delimeter=sep):

						self.assertEqual(hh, HH)
						self.assertEqual(mm, MM)
						self.assertIsNone(h)
						self.assertIsNone(m)


					if sep != "":

						probe2 = f"{H}{sep}{M}"
						hh,h, mm,m = VALID_TIME_P.fullmatch(probe2).group("hh", "h", "mm", "m")

						with self.subTest(probe=probe2, hh=hh, h=h, mm=mm, m=m, delimeter=sep):
							if	H <10 and M <10:

								self.assertEqual(h, str(H))
								self.assertEqual(m, str(M))
								self.assertIsNone(hh)
								self.assertIsNone(mm)

							elif(H <10 and 10 <= M):

								self.assertEqual(h, str(H))
								self.assertEqual(mm, MM)
								self.assertIsNone(hh)
								self.assertIsNone(m)

							elif(10 <= H and M <10):

								self.assertEqual(hh, HH)
								self.assertEqual(m, str(M))
								self.assertIsNone(h)
								self.assertIsNone(mm)

							elif(10 <= H and 10 <= M):

								self.assertEqual(hh, HH)
								self.assertEqual(mm, MM)
								self.assertIsNone(h)
								self.assertIsNone(m)




	def test_VALID_TIME_P_HMS_pattern(self):

		for H in self.HOURS:
			for M in self.MINSEC:
				for S in self.MINSEC:
					for sep in list(self.DELIMETERS) + [ "" ]:

						HH = str(H).zfill(2)
						MM = str(M).zfill(2)
						SS = str(S).zfill(2)

						probe1 = f"{HH}{sep}{MM}{sep}{SS}"
						hh,h, mm,m, ss,s = VALID_TIME_P.fullmatch(probe1).group(
							"hh", "h", "mm", "m", "ss", "s"
						)

						with self.subTest(
							probe=probe1, hh=hh, h=h, mm=mm, m=m, ss=ss, s=s, delimeter=sep
						):

							self.assertEqual(hh, HH)
							self.assertEqual(mm, MM)
							self.assertEqual(ss, SS)
							self.assertIsNone(h)
							self.assertIsNone(m)
							self.assertIsNone(s)


						if sep != "":

							probe2 = f"{H}{sep}{M}{sep}{S}"
							hh,h, mm,m, ss, s = VALID_TIME_P.fullmatch(probe2).group(
								"hh", "h", "mm", "m", "ss", "s"
							)

							with self.subTest(
								probe=probe2, hh=hh, h=h, mm=mm, m=m, delimeter=sep
							):
								if	H <10 and M <10 and S <10:

									self.assertEqual(h, str(H))
									self.assertEqual(m, str(M))
									self.assertEqual(s, str(S))
									self.assertIsNone(hh)
									self.assertIsNone(mm)
									self.assertIsNone(ss)

								elif(10 <= H and M <10 and S <10):

									self.assertEqual(hh, HH)
									self.assertEqual(m, str(M))
									self.assertEqual(s, str(S))
									self.assertIsNone(h)
									self.assertIsNone(mm)
									self.assertIsNone(ss)

								elif(H <10 and 10 <= M and S <10):

									self.assertEqual(h, str(H))
									self.assertEqual(mm, MM)
									self.assertEqual(s, str(S))
									self.assertIsNone(hh)
									self.assertIsNone(m)
									self.assertIsNone(ss)

								elif(H <10 and M <10 and 10 <= S):

									self.assertEqual(h, str(H))
									self.assertEqual(m, str(M))
									self.assertEqual(ss, SS)
									self.assertIsNone(hh)
									self.assertIsNone(mm)
									self.assertIsNone(s)

								elif(10 <= H and 10 <= M and S <10):

									self.assertEqual(hh, HH)
									self.assertEqual(mm, MM)
									self.assertEqual(s, str(S))
									self.assertIsNone(h)
									self.assertIsNone(m)
									self.assertIsNone(ss)

								elif(10 <= H and M <10 and 10 <= S):

									self.assertEqual(hh, HH)
									self.assertEqual(m, str(M))
									self.assertEqual(ss, SS)
									self.assertIsNone(h)
									self.assertIsNone(mm)
									self.assertIsNone(s)

								elif(H <10 and 10 <= M and 10 <= S):

									self.assertEqual(h, str(H))
									self.assertEqual(mm, MM)
									self.assertEqual(ss, SS)
									self.assertIsNone(hh)
									self.assertIsNone(m)
									self.assertIsNone(s)

								elif(10 <= H and 10 <= M and 10 <= S):

									self.assertEqual(hh, HH)
									self.assertEqual(mm, MM)
									self.assertEqual(ss, SS)
									self.assertIsNone(h)
									self.assertIsNone(m)
									self.assertIsNone(s)




	def test_VALID_DATE_1234_P_patterns(self):

		full_year = 2018

		for month in self.MONTHS:
			for day in self.DAYS_31:
				for sep in self.DELIMETERS:

					probe1 = f"{day}{sep}{month}{sep}{full_year}"
					with self.subTest(probe=probe1, d=day, m=month, Y=full_year, delimeter=sep):

						try:	self.assertTrue(VALID_DATE_1_P.fullmatch(probe1))
						except	AssertionError:
							self.assertRaisesRegex(

							ValueError,
							"day is out of range for month",
							datetime,
							full_year, month, day
						)

					probe2 = f"{month}{sep}{day}{sep}{full_year}"
					with self.subTest(probe=probe2, d=day, m=month, Y=full_year, delimeter=sep):

						try:	self.assertTrue(VALID_DATE_2_P.fullmatch(probe2))
						except	AssertionError:
							self.assertRaisesRegex(

							ValueError,
							"day is out of range for month",
							datetime,
							full_year, month, day
						)

					probe3 = f"{full_year}{sep}{month}{sep}{day}"
					with self.subTest(probe=probe3, d=day, m=month, Y=full_year, delimeter=sep):

						try:	self.assertTrue(VALID_DATE_3_P.fullmatch(probe3))
						except	AssertionError:
							self.assertRaisesRegex(

							ValueError,
							"day is out of range for month",
							datetime,
							full_year, month, day
						)

					probe4 = f"{full_year}{sep}{day}{sep}{month}"
					with self.subTest(probe=probe4, d=day, m=month, Y=full_year, delimeter=sep):

						try:	self.assertTrue(VALID_DATE_4_P.fullmatch(probe4))
						except	AssertionError:
							self.assertRaisesRegex(

							ValueError,
							"day is out of range for month",
							datetime,
							full_year, month, day
						)




	def test_DATETIME_1234_P_patterns(self):

		# Making a test for all datetime combinations and delimeters will end up as 7 hested
		# loops. Running such test will eat up all the memory that exist and no one knows
		# wheteher such calculations will ever be done. So following simplified cases are
		# enough to be tested. Yeah, it is end up with 10 nested loops...

		full_year = 2019

		for month in ( "JAN",6,"DeC" ):
			for day in ( 1,22 ):
				for H in ( 0,22 ):
					for M in ( 42,59 ):
						for S in ( 0,59 ):

							dd = str(day).zfill(2)
							mm = str(month).zfill(2)
							HH = str(H).zfill(2)
							MM = str(M).zfill(2)
							SS = str(S).zfill(2)

							for _d in ( day,dd ):
								for _m in ( month, mm ):
									for _H in ( H,HH ):
										for _M in ( M,MM ):
											for _S in ( S,SS ):

												tprobe	= f"{_H}:{_M}:{_S}"
												dprobe1	= f"{_d}/{_m}/{full_year}"
												dprobe2	= f"{_m}/{_d}/{full_year}"
												dprobe3	= f"{full_year}/{_m}/{_d}"
												dprobe4	= f"{full_year}/{_d}/{_m}"
												probe1	= f"{dprobe1} {tprobe}"
												probe2	= f"{dprobe2} {tprobe}"
												probe3	= f"{dprobe3} {tprobe}"
												probe4	= f"{dprobe4} {tprobe}"

												with self.subTest(

													probe=probe1,
													d=_d,m=_m,Y=full_year,
													H=_H,M=_M,S=_S,
												):
													date_time = DATETIME_1_P.fullmatch(probe1)
													date,time = date_time.group(
														"date","time"
													)
													self.assertEqual(date, dprobe1)
													self.assertEqual(time, tprobe)

												with self.subTest(

													probe=probe2,
													d=_d,m=_m,Y=full_year,
													H=_H,M=_M,S=_S,
												):
													date_time = DATETIME_2_P.fullmatch(probe2)
													date,time = date_time.group(
														"date","time"
													)
													self.assertEqual(date, dprobe2)
													self.assertEqual(time, tprobe)

												with self.subTest(

													probe=probe3,
													d=_d,m=_m,Y=full_year,
													H=_H,M=_M,S=_S,
												):
													date_time = DATETIME_3_P.fullmatch(probe3)
													date,time = date_time.group(
														"date","time"
													)
													self.assertEqual(date, dprobe3)
													self.assertEqual(time, tprobe)

												with self.subTest(

													probe=probe4,
													d=_d,m=_m,Y=full_year,
													H=_H,M=_M,S=_S,
												):
													date_time = DATETIME_4_P.fullmatch(probe4)
													date,time = date_time.group(
														"date","time"
													)
													self.assertEqual(date, dprobe4)
													self.assertEqual(time, tprobe)








	def test_hundscale_valids(self):

		results = [

			"000", "001", "003", "005", "006", "008", "010", "011", "013", "015", "016", "018",
			"020", "021", "023", "025", "026", "028", "030", "031", "033", "035", "036", "038",
			"040", "041", "043", "045", "046", "048", "050", "051", "053", "055", "056", "058",
			"060", "061", "063", "065", "066", "068", "070", "071", "073", "075", "076", "078",
			"080", "081", "083", "085", "086", "088", "090", "091", "093", "095", "096", "098"
		]
		for i,time in enumerate(list(range(60))):

			self.assertEqual(hundscale(time), results[i])
			self.assertEqual(hundscale(float(time)), results[i])
			self.assertEqual(hundscale(str(time)), results[i])




	def test_hundscale_invalids(self):

		for invalid in (

			"OOH", True, False, None, ..., hundscale,
			[ 1 ],( 1, ),{ 1 },{ "sixscale": 1 }
		):
			self.assertRaises(ValueError, hundscale, invalid)








if __name__ == "__main__" : unittest.main(verbosity=2)







