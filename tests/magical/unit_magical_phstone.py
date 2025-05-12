import	os
import	unittest
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.tests.magical				import MagicalTestCase








class StoneCase(MagicalTestCase):
	def test_no_loggy(self):

		class Stone(Transmutable):
			class Mutate(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.test_case = Stone()
		self.assertEqual(self.test_case.Mutate(), "I am part of mutable chain!")
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)


		class Stone(Transmutable):	pass
		self.test_case = Stone()
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




	def test_escalated_loggy(self):

		escalated_loggy = str(self.MAGICAL_ROOT /"escalated_loggy.loggy")
		self.make_loggy_file(escalated_loggy)

		class Stone(Transmutable):
			class Mutate(Transmutable):

				class loggy(LibraryContrib):

					handler		= escalated_loggy
					init_name	= "escalated_loggy-1"

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.test_case = Stone()
		self.assertEqual(self.test_case.Mutate(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		loggy = []

		self.test_case.loggy.close()
		with open(escalated_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@escalated_loggy-1 INFO : I am part of mutable chain!",
				"@escalated_loggy-1 INFO : I am root",
			]
		)


		self.make_loggy_file(escalated_loggy)
		class Stone(Transmutable):
			class Mutate(Transmutable):

				class loggy(LibraryContrib):

					handler			= escalated_loggy
					init_name		= "escalated_loggy-2"
					force_handover	= True

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.test_case = Stone()
		self.assertEqual(self.test_case.Mutate(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		loggy = []

		self.test_case.loggy.close()
		with open(escalated_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@escalated_loggy-2-Stone.Mutate INFO : I am part of mutable chain!",
				"@escalated_loggy-2-Stone INFO : I am root",
			]
		)


		class Stone(Transmutable):
			class Mutate(Transmutable):

				class loggy(LibraryContrib):

					handler		= escalated_loggy
					init_name	= "escalated_loggy-3"
					init_level	= 10

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.make_loggy_file(escalated_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case.Mutate(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		loggy = []

		self.test_case.loggy.close()
		with open(escalated_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@escalated_loggy-3-Stone.Mutate INFO : I am part of mutable chain!",
				"@escalated_loggy-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(escalated_loggy): os.remove(escalated_loggy)








	def test_name_loggy(self):

		name_loggy = str(self.MAGICAL_ROOT /"name_loggy.loggy")
		self.make_loggy_file(name_loggy)

		class Stone(Transmutable):
			class shoggy(LibraryContrib):

				handler		= name_loggy
				init_name	= "name_loggy-1"

			class Mutate(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.test_case = Stone()
		self.assertEqual(self.test_case.Mutate(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		loggy = []

		self.test_case.loggy.close()
		with open(name_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@name_loggy-1 INFO : I am part of mutable chain!",
				"@name_loggy-1 INFO : I am root",
			]
		)


		class Stone(Transmutable):

			class Mutate(Transmutable):
				class shoggy(LibraryContrib):

					handler		= name_loggy
					init_name	= "name_loggy-2"

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.make_loggy_file(name_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case.Mutate(), "I am part of mutable chain!")
		self.assertNotEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		loggy = []

		self.test_case.loggy.close()
		with open(name_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@name_loggy-2 INFO : I am part of mutable chain!",
				"@name_loggy-2 INFO : I am root",
			]
		)
		if	os.path.isfile(name_loggy): os.remove(name_loggy)








	def test_mutual_loggy(self):

		mutual_loggy = str(self.MAGICAL_ROOT /"mutual_loggy.loggy")
		self.make_loggy_file(mutual_loggy)

		class StoneOne(Transmutable):	pass
		class StoneTwo(Transmutable):	pass

		logger = LibraryContrib(handler=mutual_loggy, init_name="mutual_loggy", force_handover=True)
		stone_one = StoneOne(logger)
		stone_two = StoneTwo(logger)

		stone_one.loggy.info("OOH")
		stone_two.loggy.info("EEH")
		stone_one.loggy.info("OOH")
		stone_two.loggy.info("AH")
		stone_one.loggy.info("AH")
		stone_two.loggy.info("TING")
		stone_one.loggy.info("TANG")
		stone_two.loggy.info("WALLA")
		stone_one.loggy.info("WALLA")
		stone_two.loggy.info("BING")
		stone_one.loggy.info("BANG")
		loggy = []

		stone_one.loggy.close()
		stone_two.loggy.close()
		with open(mutual_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mutual_loggy-StoneOne INFO : OOH",
				"@mutual_loggy-StoneTwo INFO : EEH",
				"@mutual_loggy-StoneOne INFO : OOH",
				"@mutual_loggy-StoneTwo INFO : AH",
				"@mutual_loggy-StoneOne INFO : AH",
				"@mutual_loggy-StoneTwo INFO : TING",
				"@mutual_loggy-StoneOne INFO : TANG",
				"@mutual_loggy-StoneTwo INFO : WALLA",
				"@mutual_loggy-StoneOne INFO : WALLA",
				"@mutual_loggy-StoneTwo INFO : BING",
				"@mutual_loggy-StoneOne INFO : BANG",
			]
		)


		class logger1(LibraryContrib):

			handler			= mutual_loggy
			init_name		= "mutual_loggy_1"
			force_handover	= True

		class logger2(logger1): init_name = "mutual_loggy_2"

		loggy = []
		self.make_loggy_file(mutual_loggy)
		stone_one = StoneOne(logger1)
		stone_two = StoneTwo(logger2)

		stone_one.loggy.info("OOH")
		stone_two.loggy.info("EEH")
		stone_one.loggy.info("OOH")
		stone_two.loggy.info("AH")
		stone_one.loggy.info("AH")
		stone_two.loggy.info("TING")
		stone_one.loggy.info("TANG")
		stone_two.loggy.info("WALLA")
		stone_one.loggy.info("WALLA")
		stone_two.loggy.info("BING")
		stone_one.loggy.info("BANG")
		loggy = []

		stone_one.loggy.close()
		stone_two.loggy.close()
		with open(mutual_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mutual_loggy_1-StoneOne INFO : OOH",
				"@mutual_loggy_2-StoneTwo INFO : EEH",
				"@mutual_loggy_1-StoneOne INFO : OOH",
				"@mutual_loggy_2-StoneTwo INFO : AH",
				"@mutual_loggy_1-StoneOne INFO : AH",
				"@mutual_loggy_2-StoneTwo INFO : TING",
				"@mutual_loggy_1-StoneOne INFO : TANG",
				"@mutual_loggy_2-StoneTwo INFO : WALLA",
				"@mutual_loggy_1-StoneOne INFO : WALLA",
				"@mutual_loggy_2-StoneTwo INFO : BING",
				"@mutual_loggy_1-StoneOne INFO : BANG",
			]
		)
		if	os.path.isfile(mutual_loggy): os.remove(mutual_loggy)








	def test_invalid_init(self):

		for item in (
			1,
			.1,
			"1",
			True,
			print,
			Transmutable,
			[ Transmutable ],
			( Transmutable, ),
			{ Transmutable },
			{ "upper_layer_link": Transmutable },
		):
			with self.subTest(upper_layer_link=item):

				pattern = f"\"{item}\" is inappropriate upper layer link"
				pattern = pattern.replace("[",r"\[").replace("]",r"\]")
				pattern = pattern.replace("(",r"\(").replace(")",r"\)")
				self.assertRaisesRegex(TypeError, pattern, Transmutable, item)




	def test_phase2raise(self):

		phase2raise = str(self.MAGICAL_ROOT /"phase2raise.loggy")
		self.make_loggy_file(phase2raise)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= phase2raise
				init_name	= "phase2raise-1"

			class Raisie(Transmutable):
				def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")
			class Rousie(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(phase2raise) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@phase2raise-1 ERROR : Raisie nesting caused TypeError: Raisie must be stopped!",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= phase2raise
				init_name	= "phase2raise-2"
				init_level	= 10

			class Raisie(Transmutable):
				def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")
			class Rousie(Transmutable):	pass


		loggy = []
		self.make_loggy_file(phase2raise)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(phase2raise) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@phase2raise-2-Stone ERROR : Raisie nesting caused TypeError: Raisie must be stopped!",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= phase2raise
				init_name		= "phase2raise-3"
				force_handover	= True

			class Raisie(Transmutable):
				def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")
			class Rousie(Transmutable):	pass


		loggy = []
		self.make_loggy_file(phase2raise)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(phase2raise) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@phase2raise-3-Stone ERROR : Raisie nesting caused TypeError: Raisie must be stopped!",
			]
		)


		class Stone(Transmutable):
			class Raisie(Transmutable):
				def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")
			class Rousie(Transmutable):	pass


		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		if os.path.isfile(phase2raise): os.remove(phase2raise)








	def test_deep_phase2raise(self):

		deep_phase2raise = str(self.MAGICAL_ROOT /"deep_phase2raise.loggy")
		self.make_loggy_file(deep_phase2raise)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= deep_phase2raise
				init_name	= "deep_phase2raise-1"

			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		self.assertFalse(hasattr(self.test_case.Rousie, "Raisie"))

		self.test_case.loggy.close()
		with open(deep_phase2raise) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@deep_phase2raise-1 ERROR : Raisie nesting caused TypeError: Raisie must be stopped!",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= deep_phase2raise
				init_name	= "deep_phase2raise-2"
				init_level	= 10

			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")


		loggy = []
		self.make_loggy_file(deep_phase2raise)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		self.assertFalse(hasattr(self.test_case.Rousie, "Raisie"))

		self.test_case.loggy.close()
		with open(deep_phase2raise) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@deep_phase2raise-2-Stone.Rousie ERROR : "
				"Raisie nesting caused TypeError: Raisie must be stopped!",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= deep_phase2raise
				init_name		= "deep_phase2raise-3"
				force_handover	= True

			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")


		loggy = []
		self.make_loggy_file(deep_phase2raise)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		self.assertFalse(hasattr(self.test_case.Rousie, "Raisie"))

		self.test_case.loggy.close()
		with open(deep_phase2raise) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@deep_phase2raise-3-Stone.Rousie ERROR : "
				"Raisie nesting caused TypeError: Raisie must be stopped!",
			]
		)


		class Stone(Transmutable):
			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		self.assertFalse(hasattr(self.test_case.Rousie, "Raisie"))
		if os.path.isfile(deep_phase2raise): os.remove(deep_phase2raise)








	def test_phase2drop(self):

		phase2drop = str(self.MAGICAL_ROOT /"phase2drop.loggy")
		self.make_loggy_file(phase2drop)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= phase2drop
				init_name	= "phase2drop-1"

			class Raisie(Transmutable):
				def __new__(*args, **kwargs): pass
			class Rousie(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(phase2drop) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@phase2drop-1 ERROR : Raisie nesting caused not Transmutable mutation",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= phase2drop
				init_name	= "phase2drop-2"
				init_level	= 10

			class Raisie(Transmutable):
				def __new__(*args, **kwargs): pass
			class Rousie(Transmutable):	pass


		loggy = []
		self.make_loggy_file(phase2drop)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(phase2drop) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@phase2drop-2-Stone ERROR : Raisie nesting caused not Transmutable mutation",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= phase2drop
				init_name		= "phase2drop-3"
				force_handover	= True

			class Raisie(Transmutable):
				def __new__(*args, **kwargs): pass
			class Rousie(Transmutable):	pass


		loggy = []
		self.make_loggy_file(phase2drop)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(phase2drop) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@phase2drop-3-Stone ERROR : Raisie nesting caused not Transmutable mutation",
			]
		)


		class Stone(Transmutable):
			class Raisie(Transmutable):
				def __new__(*args, **kwargs): pass
			class Rousie(Transmutable):	pass


		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		if os.path.isfile(phase2drop): os.remove(phase2drop)








	def test_deep_phase2drop(self):

		deep_phase2drop = str(self.MAGICAL_ROOT /"deep_phase2drop.loggy")
		self.make_loggy_file(deep_phase2drop)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= deep_phase2drop
				init_name	= "deep_phase2drop-1"

			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __new__(*args, **kwargs): pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(deep_phase2drop) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@deep_phase2drop-1 ERROR : Raisie nesting caused not Transmutable mutation",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= deep_phase2drop
				init_name	= "deep_phase2drop-2"
				init_level	= 10

			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __new__(*args, **kwargs): pass


		loggy = []
		self.make_loggy_file(deep_phase2drop)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(deep_phase2drop) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@deep_phase2drop-2-Stone.Rousie ERROR : Raisie nesting caused not Transmutable mutation",
			]
		)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= deep_phase2drop
				init_name		= "deep_phase2drop-3"
				force_handover	= True

			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __new__(*args, **kwargs): pass


		loggy = []
		self.make_loggy_file(deep_phase2drop)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)

		self.test_case.loggy.close()
		with open(deep_phase2drop) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@deep_phase2drop-3-Stone.Rousie ERROR : Raisie nesting caused not Transmutable mutation",
			]
		)


		class Stone(Transmutable):
			class Rousie(Transmutable):
				class Raisie(Transmutable):
					def __new__(*args, **kwargs): pass


		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Raisie"))
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		if os.path.isfile(deep_phase2drop): os.remove(deep_phase2drop)
















	def test_other(self):

		class Stone(Transmutable):
			class Raisie:
				def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")
			class Rousie(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Raisie"))
		self.assertNotIsInstance(self.test_case.Raisie, Transmutable)
		self.assertIsInstance(self.test_case.Raisie, type)
		self.assertRaisesRegex(

			TypeError,
			"Raisie must be stopped",
			self.test_case.Raisie
		)


		class Stone(Transmutable):
			class Rousie(Transmutable):
				class Raisie:
					def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertIsInstance(self.test_case.Rousie, Transmutable)
		self.assertTrue(hasattr(self.test_case.Rousie, "Raisie"))
		self.assertNotIsInstance(self.test_case.Rousie.Raisie, Transmutable)
		self.assertIsInstance(self.test_case.Rousie.Raisie, type)
		self.assertRaisesRegex(

			TypeError,
			"Raisie must be stopped",
			self.test_case.Rousie.Raisie
		)








	def test_top_layer_other(self):

		class Stone:
			class Raisie:
				def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")
			class Rousie(Transmutable):	pass


		self.test_case = Stone()
		self.assertNotIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertNotIsInstance(self.test_case.Rousie, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Raisie"))
		self.assertNotIsInstance(self.test_case.Raisie, Transmutable)
		self.assertRaisesRegex(

			TypeError,
			"Raisie must be stopped",
			self.test_case.Raisie
		)


		class Stone:
			class Rousie(Transmutable):
				class Raisie:
					def __init__(self, *args, **kwargs): raise TypeError("Raisie must be stopped!")


		self.test_case = Stone()
		self.assertNotIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Rousie"))
		self.assertNotIsInstance(self.test_case.Rousie, Transmutable)
		self.assertTrue(hasattr(self.test_case.Rousie, "Raisie"))
		self.assertNotIsInstance(self.test_case.Rousie.Raisie, Transmutable)
		self.assertRaisesRegex(

			TypeError,
			"Raisie must be stopped",
			self.test_case.Rousie.Raisie
		)
















	def test_kws_init(self):

		class Stone(Transmutable):
			class Measure(Transmutable):
				def weight(self): return self.W
				def height(self): return self.H


		self.test_case = Stone()
		self.assertRaisesRegex(

			AttributeError,
			"Attribute 'W' has no escalation to Stone",
			self.test_case.Measure.weight
		)
		self.assertRaisesRegex(

			AttributeError,
			"Attribute 'H' has no escalation to Stone",
			self.test_case.Measure.height
		)


		self.test_case = Stone(W=420, H=69)
		self.assertEqual(self.test_case.Measure.weight(), 420)
		self.assertEqual(self.test_case.Measure.height(), 69)


		class Stone(Transmutable):

			W = 42
			H = 667

			class Measure(Transmutable):
				def weight(self): return self.W
				def height(self): return self.H


		self.test_case = Stone()
		self.assertEqual(self.test_case.Measure.weight(), 42)
		self.assertEqual(self.test_case.Measure.height(), 667)
		self.test_case = Stone(W=420, H=69)
		self.assertEqual(self.test_case.Measure.weight(), 420)
		self.assertEqual(self.test_case.Measure.height(), 69)


		class Stone(Transmutable):
			class Measure(Transmutable):

				def weight(self): return self.W
				def height(self): return self.H
				W = 42
				H = 667


		self.test_case = Stone()
		self.assertEqual(self.test_case.Measure.weight(), 42)
		self.assertEqual(self.test_case.Measure.height(), 667)
		self.test_case = Stone(W=420, H=69)
		self.assertEqual(self.test_case.Measure.weight(), 42)
		self.assertEqual(self.test_case.Measure.height(), 667)
		self.assertEqual(self.test_case.Measure._UPPER_LAYER.W, 420)
		self.assertEqual(self.test_case.Measure._UPPER_LAYER.H, 69)
















	def test_outer_loggy(self):

		outer_loggy = str(self.MAGICAL_ROOT /"outer_loggy.loggy")
		self.make_loggy_file(outer_loggy)

		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= outer_loggy
				init_name	= "outer_loggy-1"

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(outer_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_loggy-1 INFO : I am part of mutable chain!",
				"@outer_loggy-1 INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= outer_loggy
				init_name	= "outer_loggy-2"
				init_level	= 10

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(outer_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_loggy-2-Stone INFO : I am part of mutable chain!",
				"@outer_loggy-2-Stone INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= outer_loggy
				init_name		= "outer_loggy-3"
				force_handover	= True

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(outer_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_loggy-3-Stone INFO : I am part of mutable chain!",
				"@outer_loggy-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(outer_loggy): os.remove(outer_loggy)








	def test_outer_name_loggy(self):

		outer_name_loggy = str(self.MAGICAL_ROOT /"outer_name_loggy.loggy")
		self.make_loggy_file(outer_name_loggy)

		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= outer_name_loggy
				init_name	= "outer_name_loggy-1"

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(outer_name_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_name_loggy-1 INFO : I am part of mutable chain!",
				"@outer_name_loggy-1 INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= outer_name_loggy
				init_name	= "outer_name_loggy-2"
				init_level	= 10

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_name_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(outer_name_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_name_loggy-2-Stone INFO : I am part of mutable chain!",
				"@outer_name_loggy-2-Stone INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= outer_name_loggy
				init_name		= "outer_name_loggy-3"
				force_handover	= True

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_name_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(outer_name_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_name_loggy-3-Stone INFO : I am part of mutable chain!",
				"@outer_name_loggy-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(outer_name_loggy): os.remove(outer_name_loggy)








	def test_outer_escalated_loggy(self):

		outer_e_loggy = str(self.MAGICAL_ROOT /"outer_e_loggy.loggy")
		self.make_loggy_file(outer_e_loggy)

		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler		= outer_e_loggy
					init_name	= "outer_e_loggy-1"

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.test_case.loggy.info("I am root")
		self.test_case.Handle.loggy.info("I ain't root")

		self.test_case.loggy.close()
		with open(outer_e_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_loggy-1 INFO : I am part of mutable chain!",
				"@outer_e_loggy-1 INFO : I am root",
				"@outer_e_loggy-1 INFO : I ain't root",
			]
		)


		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler		= outer_e_loggy
					init_name	= "outer_e_loggy-2"
					init_level	= 10

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_e_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.test_case.loggy.info("I am root")
		self.test_case.Handle.loggy.info("I ain't root")

		self.test_case.loggy.close()
		with open(outer_e_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_loggy-2-Stone INFO : I am part of mutable chain!",
				"@outer_e_loggy-2-Stone INFO : I am root",
				"@outer_e_loggy-2-Stone.Handle INFO : I ain't root",
			]
		)


		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler			= outer_e_loggy
					init_name		= "outer_e_loggy-3"
					force_handover	= True

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_e_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.test_case.loggy.info("I am root")
		self.test_case.Handle.loggy.info("I ain't root")

		self.test_case.loggy.close()
		with open(outer_e_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_loggy-3-Stone INFO : I am part of mutable chain!",
				"@outer_e_loggy-3-Stone INFO : I am root",
				"@outer_e_loggy-3-Stone.Handle INFO : I ain't root",
			]
		)
		if	os.path.isfile(outer_e_loggy): os.remove(outer_e_loggy)








	def test_outer_escalated_name_loggy(self):

		outer_e_n_loggy = str(self.MAGICAL_ROOT /"outer_e_n_loggy.loggy")
		self.make_loggy_file(outer_e_n_loggy)

		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= outer_e_n_loggy
					init_name	= "outer_e_n_loggy-1"

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.test_case.loggy.info("I am root")
		self.test_case.Handle.loggy.info("I ain't root")

		self.test_case.loggy.close()
		with open(outer_e_n_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_n_loggy-1 INFO : I am part of mutable chain!",
				"@outer_e_n_loggy-1 INFO : I am root",
				"@outer_e_n_loggy-1 INFO : I ain't root",
			]
		)


		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= outer_e_n_loggy
					init_name	= "outer_e_n_loggy-2"
					init_level	= 10

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_e_n_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.test_case.loggy.info("I am root")
		self.test_case.Handle.loggy.info("I ain't root")

		self.test_case.loggy.close()
		with open(outer_e_n_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_n_loggy-2-Stone INFO : I am part of mutable chain!",
				"@outer_e_n_loggy-2-Stone INFO : I am root",
				"@outer_e_n_loggy-2-Stone.Handle INFO : I ain't root",
			]
		)


		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= outer_e_n_loggy
					init_name		= "outer_e_n_loggy-3"
					force_handover	= True

		class Stone(Outdoor):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(outer_e_n_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.test_case.loggy.info("I am root")
		self.test_case.Handle.loggy.info("I ain't root")

		self.test_case.loggy.close()
		with open(outer_e_n_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_n_loggy-3-Stone INFO : I am part of mutable chain!",
				"@outer_e_n_loggy-3-Stone INFO : I am root",
				"@outer_e_n_loggy-3-Stone.Handle INFO : I ain't root",
			]
		)
		if	os.path.isfile(outer_e_n_loggy): os.remove(outer_e_n_loggy)








	def test_outer_no_loggy(self):

		class Outdoor(Transmutable):
			def __call__(self):

				self.loggy.info("I am part of mutable chain!")
				return	"I am part of mutable chain!"

		class Stone(Outdoor):	pass

		self.test_case = Stone()
		self.assertEqual(self.test_case(), "I am part of mutable chain!")
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_outer_nested_loggy(self):

		out_nested_loggy = str(self.MAGICAL_ROOT /"out_nested_loggy.loggy")
		self.make_loggy_file(out_nested_loggy)

		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= out_nested_loggy
				init_name	= "out_nested_loggy-1"

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(out_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_nested_loggy-1 INFO : I am part of mutable chain!",
				"@out_nested_loggy-1 INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= out_nested_loggy
				init_name	= "out_nested_loggy-2"
				init_level	= 10

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_nested_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(out_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_nested_loggy-2-Stone.Handle INFO : I am part of mutable chain!",
				"@out_nested_loggy-2-Stone INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= out_nested_loggy
				init_name		= "out_nested_loggy-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_nested_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(out_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_nested_loggy-3-Stone.Handle INFO : I am part of mutable chain!",
				"@out_nested_loggy-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(out_nested_loggy): os.remove(out_nested_loggy)








	def test_outer_name_nested_loggy(self):

		out_n_nested_loggy = str(self.MAGICAL_ROOT /"out_n_nested_loggy.loggy")
		self.make_loggy_file(out_n_nested_loggy)

		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= out_n_nested_loggy
				init_name	= "out_n_nested_loggy-1"

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(out_n_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_nested_loggy-1 INFO : I am part of mutable chain!",
				"@out_n_nested_loggy-1 INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= out_n_nested_loggy
				init_name	= "out_n_nested_loggy-2"
				init_level	= 10

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_n_nested_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(out_n_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_nested_loggy-2-Stone.Handle INFO : I am part of mutable chain!",
				"@out_n_nested_loggy-2-Stone INFO : I am root",
			]
		)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= out_n_nested_loggy
				init_name		= "out_n_nested_loggy-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_n_nested_loggy)
		self.test_case = Stone()
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")

		self.test_case.loggy.close()
		with open(out_n_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_nested_loggy-3-Stone.Handle INFO : I am part of mutable chain!",
				"@out_n_nested_loggy-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(out_n_nested_loggy): os.remove(out_n_nested_loggy)








	def test_outer_escalated_nested_loggy(self):

		out_e_nested_loggy = str(self.MAGICAL_ROOT /"out_e_nested_loggy.loggy")
		self.make_loggy_file(out_e_nested_loggy)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= out_e_nested_loggy
					init_name	= "out_e_nested_loggy-1"

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")

		self.test_case.loggy.close()
		with open(out_e_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_nested_loggy-1 INFO : I am part of mutable chain!",
				"@out_e_nested_loggy-1 INFO : I am root",
				"@out_e_nested_loggy-1 INFO : I am bound",
			]
		)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= out_e_nested_loggy
					init_name	= "out_e_nested_loggy-2"
					init_level	= 10

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_e_nested_loggy)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")

		self.test_case.loggy.close()
		with open(out_e_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_nested_loggy-2-Stone.Handle INFO : I am part of mutable chain!",
				"@out_e_nested_loggy-2-Stone INFO : I am root",
				"@out_e_nested_loggy-2-Stone.Bound INFO : I am bound",
			]
		)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= out_e_nested_loggy
					init_name		= "out_e_nested_loggy-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_e_nested_loggy)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")

		self.test_case.loggy.close()
		with open(out_e_nested_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_nested_loggy-3-Stone.Handle INFO : I am part of mutable chain!",
				"@out_e_nested_loggy-3-Stone INFO : I am root",
				"@out_e_nested_loggy-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(out_e_nested_loggy): os.remove(out_e_nested_loggy)








	def test_outer_escalated_name_nested_loggy(self):

		out_e_n_ne_loggy = str(self.MAGICAL_ROOT /"out_e_n_ne_loggy.loggy")
		self.make_loggy_file(out_e_n_ne_loggy)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= out_e_n_ne_loggy
					init_name	= "out_e_n_ne_loggy-1"

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")

		self.test_case.loggy.close()
		with open(out_e_n_ne_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_ne_loggy-1 INFO : I am part of mutable chain!",
				"@out_e_n_ne_loggy-1 INFO : I am root",
				"@out_e_n_ne_loggy-1 INFO : I am bound",
			]
		)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= out_e_n_ne_loggy
					init_name	= "out_e_n_ne_loggy-2"
					init_level	= 10

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_e_n_ne_loggy)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")

		self.test_case.loggy.close()
		with open(out_e_n_ne_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_ne_loggy-2-Stone.Handle INFO : I am part of mutable chain!",
				"@out_e_n_ne_loggy-2-Stone INFO : I am root",
				"@out_e_n_ne_loggy-2-Stone.Bound INFO : I am bound",
			]
		)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= out_e_n_ne_loggy
					init_name		= "out_e_n_ne_loggy-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		loggy = []
		self.make_loggy_file(out_e_n_ne_loggy)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")

		self.test_case.loggy.close()
		with open(out_e_n_ne_loggy) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_ne_loggy-3-Stone.Handle INFO : I am part of mutable chain!",
				"@out_e_n_ne_loggy-3-Stone INFO : I am root",
				"@out_e_n_ne_loggy-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(out_e_n_ne_loggy): os.remove(out_e_n_ne_loggy)








	def test_outer_nested_no_loggy(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):
			class Handle(Transmutable):

				def __call__(self):

					self.loggy.info("I am part of mutable chain!")
					return	"I am part of mutable chain!"


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Handle(), "I am part of mutable chain!")
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)








if __name__ == "__main__" : unittest.main(verbosity=2)







