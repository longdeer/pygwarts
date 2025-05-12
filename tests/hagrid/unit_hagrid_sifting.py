import	re
import	os
import	unittest
from	pathlib								import Path
from	pygwarts.tests.hagrid				import HagridTestCase
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.hagrid.cultivation.sifting	import SiftingController








class SiftingCases(HagridTestCase):

	"""
		Sifting logic
	"""

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.SIFT_HANDLER): os.remove(cls.SIFT_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.SIFT_HANDLER)
	def test_controller_unpatternables(self):

		unpatternables = None, True, 42, .69, SiftingController, [], {}, set(), tuple(),

		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "controller_unpatternables"
				handler		= self.SIFT_HANDLER

			include	= unpatternables[:4]
			exclude	= unpatternables[4:]


		with self.assertLogs("controller_unpatternables", 10) as case_loggy:

			self.test_case = SiftingCase()
			for candidate in unpatternables:

				self.assertIn(
					f"WARNING:controller_unpatternables:Unpatternable type {type(candidate)}",
					case_loggy.output
				)
			self.assertFalse(hasattr(self.test_case, "exclude_field"))
			self.assertFalse(hasattr(self.test_case, "include_field"))




	def test_controller_wrong(self):

		unpatternables = None, True, 42, .69, SiftingController, [], {}, set(), tuple(),

		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "controller_wrongs"
				handler		= self.SIFT_HANDLER

			include	= tuple()
			exclude	= "tuple()"


		with self.assertLogs("controller_wrongs", 10) as case_loggy:

			self.test_case = SiftingCase()
			for candidate in unpatternables:

				self.assertIn(
					"WARNING:controller_wrongs:"
					f"{self.test_case} exclude field improper, must be not empty list or tuple",
					case_loggy.output
				)
				self.assertIn(
					"WARNING:controller_wrongs:"
					f"{self.test_case} include field improper, must be not empty list or tuple",
					case_loggy.output
				)
			self.assertFalse(hasattr(self.test_case, "exclude_field"))
			self.assertFalse(hasattr(self.test_case, "include_field"))




	def test_controller_sprigs(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "controller_sprigs"
				handler		= self.SIFT_HANDLER


		self.test_case = SiftingCase()
		invalid_types = "sprigs", ( "sprigs", ), { "sprigs" }, iter([ "sprigs" ]),
		invalid_sprigs = [ "sprigs" ], [( "sprigs", )], [{ "sprigs" }], [ iter([ "sprigs" ])],


		for item1 in invalid_types:
			with self.assertLogs("controller_sprigs", 10) as case_loggy:

				self.test_case(item1)
				self.assertIn(
					f"WARNING:controller_sprigs:{self.test_case} found invalid sprigs type {type(item1)}",
					case_loggy.output
				)


		for item2 in invalid_sprigs:
			with self.assertLogs("controller_sprigs", 10) as case_loggy:

				self.test_case(item2)
				self.assertIn(
					f"WARNING:controller_sprigs:{self.test_case} found invalid sprig \"{item2[0]}\"",
					case_loggy.output
				)




	def test_controller_no_Sieve(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "controller_no_Sieve"
				handler		= self.SIFT_HANDLER


		self.test_case = SiftingCase()
		self.test_case.Sieve = "Sieve"


		with self.assertLogs("controller_no_Sieve", 10) as case_loggy:

			self.test_case("sprigs")
			self.assertIn(
				"DEBUG:controller_no_Sieve:Sieve not implemented for current controller",
				case_loggy.output
			)




	def test_controller_fields(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "controller_fields"
				handler		= self.SIFT_HANDLER


		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case = SiftingCase()
			self.assertIn(
				"DEBUG:controller_fields:Exclude field not implemented for sifting", case_loggy.output
			)
			self.assertIn(
				"DEBUG:controller_fields:Exclude field not implemented for sifting", case_loggy.output
			)
			self.assertFalse(hasattr(self.test_case, "exclude_field"))
			self.assertFalse(hasattr(self.test_case, "include_field"))




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case([ Path("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Exclude field skipped", case_loggy.output
			)
			self.assertIn(
				"DEBUG:controller_fields:Exclude field skipped", case_loggy.output
			)
			self.assertFalse(hasattr(self.test_case, "exclude_field"))
			self.assertFalse(hasattr(self.test_case, "include_field"))




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.include_field = []
			self.test_case([ Path("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Exclude field skipped", case_loggy.output
			)
			self.assertIn(
				"DEBUG:controller_fields:Sifted sprig \"False\"", case_loggy.output
			)
			self.assertFalse(hasattr(self.test_case, "exclude_field"))
			self.assertTrue(hasattr(self.test_case, "include_field"))




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.exclude_field = []
			self.test_case([ Path("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Exclude field passed", case_loggy.output
			)
			self.assertIn(
				"DEBUG:controller_fields:Sifted sprig \"False\"", case_loggy.output
			)
			self.assertTrue(hasattr(self.test_case, "exclude_field"))
			self.assertTrue(hasattr(self.test_case, "include_field"))




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.include_field = [ re.compile("False") ]
			self.test_case([ Path("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Exclude field passed", case_loggy.output
			)
			self.assertIn(
				"DEBUG:controller_fields:Passed sprig \"False\"", case_loggy.output
			)
			self.assertTrue(hasattr(self.test_case, "exclude_field"))
			self.assertTrue(hasattr(self.test_case, "include_field"))




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.exclude_field = [ re.compile("False") ]
			self.test_case([ Path("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Sifted sprig \"False\"", case_loggy.output
			)
			self.assertTrue(hasattr(self.test_case, "exclude_field"))
			self.assertTrue(hasattr(self.test_case, "include_field"))




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.exclude_field = self.test_case.pmake_field([])
			self.assertIn(
				"DEBUG:controller_fields:Making field from 0 entities", case_loggy.output
			)

			self.test_case.include_field = self.test_case.pmake_field([])
			self.assertIn(
				"DEBUG:controller_fields:Making field from 0 entities", case_loggy.output
			)

			self.assertFalse(self.test_case.exclude_field)
			self.assertFalse(self.test_case.include_field)

			self.test_case.include_field = self.test_case.pmake_field([ "False" ])
			self.assertTrue(self.test_case.include_field)
			self.assertIn(
				"DEBUG:controller_fields:Making field from 1 entities", case_loggy.output
			)

			self.test_case([ Path("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Passed sprig \"False\"", case_loggy.output
			)




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.exclude_field = 42
			self.test_case.include_field = 42

			self.assertEqual(self.test_case.exclude_field, 42)
			self.assertEqual(self.test_case.include_field, 42)

			self.test_case([ Path("False") ], excludables=[], includables=[])
			self.assertIn(
				"DEBUG:controller_fields:Sifted sprig \"False\"", case_loggy.output
			)




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.exclude_field = 420
			self.test_case.include_field = 420

			self.assertEqual(self.test_case.exclude_field, 420)
			self.assertEqual(self.test_case.include_field, 420)

			self.test_case([ Path("False") ], excludables=[], includables=[ re.compile("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Passed sprig \"False\"", case_loggy.output
			)




		with self.assertLogs("controller_fields", 10) as case_loggy:

			self.test_case.exclude_field = 69
			self.test_case.include_field = 69

			self.assertEqual(self.test_case.exclude_field, 69)
			self.assertEqual(self.test_case.include_field, 69)

			self.test_case(

				[ Path("False") ],
				excludables=[ re.compile("False") ],
				includables=[ re.compile("False") ])
			self.assertIn(
				"DEBUG:controller_fields:Sifted sprig \"False\"", case_loggy.output
			)








	def test_Sieve_siftable(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "Sieve_siftable"
				handler		= self.SIFT_HANDLER


		self.test_case = SiftingCase()


		with self.assertLogs("Sieve_siftable", 10) as case_loggy:

			sifted = self.test_case.Sieve(False, exclude=None, include=None, thriving=False)
			self.assertIn(
				"DEBUG:Sieve_siftable:Got invalid siftable \"False\"", case_loggy.output
			)
			self.assertTrue(sifted)




	def test_Sieve_empties(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "Sieve_empties"
				handler		= self.SIFT_HANDLER


		self.test_case = SiftingCase()


		with self.assertLogs("Sieve_empties", 10) as case_loggy:

			sifted = self.test_case.Sieve("False", exclude=[], include=[], thriving=False)
			self.assertIn(
				"DEBUG:Sieve_empties:Exclude field passed", case_loggy.output
			)
			self.assertIn(
				"DEBUG:Sieve_empties:Include field not passed", case_loggy.output
			)
			self.assertTrue(sifted)




	def test_Sieve_Nones(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "Sieve_Nones"
				handler		= self.SIFT_HANDLER


		self.test_case = SiftingCase()


		with self.assertLogs("Sieve_Nones", 10) as case_loggy:

			sifted = self.test_case.Sieve("False", exclude=None, include=None, thriving=False)
			self.assertIn(
				"DEBUG:Sieve_Nones:Exclude field skipped", case_loggy.output
			)
			self.assertIn(
				"DEBUG:Sieve_Nones:Include field skipped", case_loggy.output
			)
			self.assertFalse(sifted)




	def test_Sieve_fields(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "Sieve_fields"
				handler		= self.SIFT_HANDLER

			exclude_field	= "excludable",
			include_field	= "includable",


		self.test_case = SiftingCase()


		with self.assertLogs("Sieve_fields", 10) as case_loggy:

			sifted = self.test_case.Sieve(

				"False",
				exclude=self.test_case.exclude_field,
				include=self.test_case.include_field,
				thriving=False
			)
			self.assertIn(
				f"DEBUG:Sieve_fields:Got invalid exclude field", case_loggy.output
			)
			self.assertIn(
				f"DEBUG:Sieve_fields:Got invalid include field", case_loggy.output
			)
			self.assertTrue(sifted)




	def test_Sieve_invalids(self):
		class SiftingCase(SiftingController):
			class loggy(LibraryContrib):

				init_level	= 10
				init_name	= "Sieve_invalids"
				handler		= self.SIFT_HANDLER

			exclude_field	= [ "not Path" ]
			include_field	= [ "not Path" ]


		self.test_case = SiftingCase()


		with self.assertLogs("Sieve_invalids", 10) as case_loggy:

			sifted = self.test_case.Sieve(

				"False",
				exclude=self.test_case.exclude_field,
				include=self.test_case.include_field,
				thriving=False
			)
			self.assertIn(

				f"DEBUG:Sieve_invalids:Got invalid excludable \"not Path\"",
				case_loggy.output
			)
			self.assertIn(
				"DEBUG:Sieve_invalids:Got invalid includable \"not Path\"", case_loggy.output
			)
			self.assertTrue(sifted)
















	def test_fs_strings(self):
		if	os.name == "posix":

			class SiftingCase(SiftingController):
				class loggy(LibraryContrib):

					init_level	= 10
					init_name	= "controller_strings"
					handler		= self.SIFT_HANDLER

				include	= (

					r".+\.mp[34]",
					rf".+/good/[^/]+",	# The end folder is good for any file
				)
				exclude	= rf".+scooter.+",


			self.test_case = SiftingCase()
			current_case = {

				"/home/user/music/prodigy":		[

					"thier law.mp3", "thier law.mp4", "thier law.mp5",
					"baby's got a temper.mp3", "baby's got a temper.mp4", "baby's got a temper.mp5",
					"breath.mp3", "breath.mp4", "breath.mp5"
				],
				"/home/user/music/scooter":		[ "how much is the fish.mp3" ],
				"/srv/web/cache":				[ "not.trojan" ],
				"/srv/storage/memories/good":	[ "day1.jpg", "day2.jpg" ],
				"/srv/storage/days/good/photos":[ "day1.jpg", "day2.jpg" ],
			}


			with self.assertLogs("controller_strings", 10) as case_loggy:
				self.assertEqual(

					[
						p.name for p in self.test_case(
							[
								Path(f"/home/user/music/prodigy/{item}")
								for item in current_case["/home/user/music/prodigy"]
							]
						)
					],	[
							"thier law.mp3", "thier law.mp4",
							"baby's got a temper.mp3", "baby's got a temper.mp4",
							"breath.mp3", "breath.mp4",
						]
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"thier law.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"thier law.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"thier law.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"baby's got a temper.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"baby's got a temper.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"baby's got a temper.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"breath.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"breath.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"breath.mp5\"", case_loggy.output
				)


			with self.assertLogs("controller_strings", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[
							Path(f"/home/user/music/scooter/{item}") for item in
							current_case["/home/user/music/scooter"]
						]
					),	[]
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"how much is the fish.mp3\"", case_loggy.output
				)


			with self.assertLogs("controller_strings", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[ Path(f"/srv/web/cache/{item}") for item in current_case["/srv/web/cache"] ]
					),	[]
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"not.trojan\"", case_loggy.output
				)


			with self.assertLogs("controller_strings", 10) as case_loggy:
				self.assertEqual(
					[
						p.name for p in self.test_case(
							[
								Path(f"/srv/storage/memories/good/{item}") for item in
								current_case["/srv/storage/memories/good"]
							]
						)
					],	[ "day1.jpg", "day2.jpg" ]
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Passed sprig \"day2.jpg\"", case_loggy.output
				)


			with self.assertLogs("controller_strings", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[
							Path(f"/srv/storage/days/good/photos/{item}") for item in
							current_case["/srv/storage/days/good/photos"]
						]
					),	[]
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_strings:Sifted sprig \"day2.jpg\"", case_loggy.output
				)




		elif(os.name == "nt"):

			class SiftingCase(SiftingController):
				class loggy(LibraryContrib):

					init_level	= 10
					init_name	= "otherfs_controller_strings"
					handler		= self.SIFT_HANDLER

				include	= (

					r".+\.mp[34]",
					rf".+\\good\\[^(\\)]+",	# The end folder is good for any file
				)
				exclude	= rf".+scooter.+",


			self.test_case = SiftingCase()
			current_case = {

				"D:\\music\\prodigy":				[

					"thier law.mp3", "thier law.mp4", "thier law.mp5",
					"baby's got a temper.mp3", "baby's got a temper.mp4", "baby's got a temper.mp5",
					"breath.mp3", "breath.mp4", "breath.mp5"
				],
				"D:\\music\\scooter":				[ "how much is the fish.mp3" ],
				"C:\\Program Files":				[ "not.trojan" ],
				"E:\\storage\\memories\\good":		[ "day1.jpg", "day2.jpg" ],
				"F:\\storage\\days\\good\\photos":	[ "day1.jpg", "day2.jpg" ],
			}


			with self.assertLogs("otherfs_controller_strings", 10) as case_loggy:
				self.assertEqual(

					[
						p.name for p in self.test_case(
							[
								Path(f"D:\\music\\prodigy\\{item}")
								for item in  current_case["D:\\music\\prodigy"]
							]
						)
					],	[
						"thier law.mp3", "thier law.mp4",
						"baby's got a temper.mp3", "baby's got a temper.mp4",
						"breath.mp3", "breath.mp4",
						]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"thier law.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"thier law.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Sifted sprig \"thier law.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"baby's got a temper.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"baby's got a temper.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Sifted sprig \"baby's got a temper.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"breath.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"breath.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Sifted sprig \"breath.mp5\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_strings", 10) as case_loggy:
				self.assertEqual(
					self.test_case(

						[ Path(f"D:\\music\\scooter\\{item}") for item in current_case["D:\\music\\scooter"] ]
					),	[]
				)
				self.assertIn(

					"DEBUG:otherfs_controller_strings:Sifted sprig \"how much is the fish.mp3\"",
					case_loggy.output
				)


			with self.assertLogs("otherfs_controller_strings", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[ Path(f"C:\\Program Files\\{item}") for item in current_case["C:\\Program Files"] ]
					),	[]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Sifted sprig \"not.trojan\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_strings", 10) as case_loggy:
				self.assertEqual(
					[
						p.name for p in self.test_case(
							[
								Path(f"E:\\storage\\memories\\good\\{item}") for item in
								current_case["E:\\storage\\memories\\good"]
							]
						)
					],	[ "day1.jpg", "day2.jpg" ]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Passed sprig \"day2.jpg\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_strings", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[
							Path(f"F:\\storage\\days\\good\\photos\\{item}") for item in
							current_case["F:\\storage\\days\\good\\photos"]
						]
					),	[]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Sifted sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_strings:Sifted sprig \"day2.jpg\"", case_loggy.output
				)
		else:	self.assertFalse("OS neither posix nor windows")








	def test_fs_Patterns(self):
		if	os.name == "posix":

			class SiftingCase(SiftingController):
				class loggy(LibraryContrib):

					init_level	= 10
					init_name	= "controller_Patterns"
					handler		= self.SIFT_HANDLER

				include	= (

					re.compile(r".+\.mp[34]"),
					re.compile(rf".+/good/[^/]+"),	# The end folder is good for any file
				)
				exclude	= re.compile(rf".+scooter.+"),


			self.test_case = SiftingCase()
			current_case = {

				"/home/user/music/prodigy":		[

					"thier law.mp3", "thier law.mp4", "thier law.mp5",
					"baby's got a temper.mp3", "baby's got a temper.mp4", "baby's got a temper.mp5",
					"breath.mp3", "breath.mp4", "breath.mp5"
				],
				"/home/user/music/scooter":		[ "how much is the fish.mp3" ],
				"/srv/web/cache":				[ "not.trojan" ],
				"/srv/storage/memories/good":	[ "day1.jpg", "day2.jpg" ],
				"/srv/storage/days/good/photos":[ "day1.jpg", "day2.jpg" ],
			}


			with self.assertLogs("controller_Patterns", 10) as case_loggy:
				self.assertEqual(

					[
						p.name for p in self.test_case(
							[
								Path(f"/home/user/music/prodigy/{item}")
								for item in current_case["/home/user/music/prodigy"]
							]
						)
					],	[
							"thier law.mp3", "thier law.mp4",
							"baby's got a temper.mp3", "baby's got a temper.mp4",
							"breath.mp3", "breath.mp4",
						]
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"thier law.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"thier law.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"thier law.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"baby's got a temper.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"baby's got a temper.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"baby's got a temper.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"breath.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"breath.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"breath.mp5\"", case_loggy.output
				)


			with self.assertLogs("controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[
							Path(f"/home/user/music/scooter/{item}") for item in
							current_case["/home/user/music/scooter"]
						]
					),	[]
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"how much is the fish.mp3\"", case_loggy.output
				)


			with self.assertLogs("controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[ Path(f"/srv/web/cache/{item}") for item in current_case["/srv/web/cache"] ]
					),	[]
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"not.trojan\"", case_loggy.output
				)


			with self.assertLogs("controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					[
						p.name for p in self.test_case(
							[
								Path(f"/srv/storage/memories/good/{item}") for item in
								current_case["/srv/storage/memories/good"]
							]
						)
					],	[ "day1.jpg", "day2.jpg" ]
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Passed sprig \"day2.jpg\"", case_loggy.output
				)


			with self.assertLogs("controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[
							Path(f"/srv/storage/days/good/photos/{item}") for item in
							current_case["/srv/storage/days/good/photos"]
						]
					),	[]
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:controller_Patterns:Sifted sprig \"day2.jpg\"", case_loggy.output
				)




		elif(os.name == "nt"):

			class SiftingCase(SiftingController):
				class loggy(LibraryContrib):

					init_level	= 10
					init_name	= "otherfs_controller_Patterns"
					handler		= self.SIFT_HANDLER

				include	= (

					re.compile(r".+\.mp[34]"),
					re.compile(rf".+\\good\\[^(\\)]+"),	# The end folder is good for any file
				)
				exclude	= re.compile(rf".+scooter.+"),


			self.test_case = SiftingCase()
			current_case = {

				"D:\\music\\prodigy":				[

					"thier law.mp3", "thier law.mp4", "thier law.mp5",
					"baby's got a temper.mp3", "baby's got a temper.mp4", "baby's got a temper.mp5",
					"breath.mp3", "breath.mp4", "breath.mp5"
				],
				"D:\\music\\scooter":				[ "how much is the fish.mp3" ],
				"C:\\Program Files":				[ "not.trojan" ],
				"E:\\storage\\memories\\good":		[ "day1.jpg", "day2.jpg" ],
				"F:\\storage\\days\\good\\photos":	[ "day1.jpg", "day2.jpg" ],
			}


			with self.assertLogs("otherfs_controller_Patterns", 10) as case_loggy:
				self.assertEqual(

					[
						p.name for p in self.test_case(
							[
								Path(f"D:\\music\\prodigy\\{item}")
								for item in  current_case["D:\\music\\prodigy"]
							]
						)
					],	[
						"thier law.mp3", "thier law.mp4",
						"baby's got a temper.mp3", "baby's got a temper.mp4",
						"breath.mp3", "breath.mp4",
						]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"thier law.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"thier law.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"thier law.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"baby's got a temper.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"baby's got a temper.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"baby's got a temper.mp5\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"breath.mp3\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"breath.mp4\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"breath.mp5\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[ Path(f"D:\\music\\scooter\\{item}") for item in current_case["D:\\music\\scooter"] ]
					),	[]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"how much is the fish.mp3\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[ Path(f"C:\\Program Files\\{item}") for item in current_case["C:\\Program Files"] ]
					),	[]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"not.trojan\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					[
						p.name for p in self.test_case(
							[
								Path(f"E:\\storage\\memories\\good\\{item}") for item in
								current_case["E:\\storage\\memories\\good"]
							]
						)
					],	[ "day1.jpg", "day2.jpg" ]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Passed sprig \"day2.jpg\"", case_loggy.output
				)


			with self.assertLogs("otherfs_controller_Patterns", 10) as case_loggy:
				self.assertEqual(
					self.test_case(
						[
							Path(f"F:\\storage\\days\\good\\photos\\{item}") for item in
							current_case["F:\\storage\\days\\good\\photos"]
						]
					),	[]
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"day1.jpg\"", case_loggy.output
				)
				self.assertIn(
					"DEBUG:otherfs_controller_Patterns:Sifted sprig \"day2.jpg\"", case_loggy.output
				)
		else:	self.assertFalse("OS neither posix nor windows")








if __name__ == "__main__" : unittest.main(verbosity=2)







