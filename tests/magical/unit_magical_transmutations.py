import	os
import	unittest
from	pygwarts.magical.philosophers_stone					import Transmutable
from	pygwarts.magical.philosophers_stone.transmutations	import Transmutation
from	pygwarts.magical.spells								import geminio
from	pygwarts.irma.contrib								import LibraryContrib
from	pygwarts.tests.magical								import MagicalTestCase








class StoneMutationCase(MagicalTestCase):

	class Mutagen(Transmutation):
		def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

			class MutatedStone(geminio(layer)):
				def __call__(self, color :str) -> str :

					self.loggy.info(f"Darkening the {color}")
					mutated_color = f"dark-{color}"
					return	f"{super().__call__(mutated_color)}"

			return	MutatedStone


	class Mutabor(Transmutation):
		def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

			class MutaboredStone(geminio(layer)):
				def __call__(self, color :str) -> str :

					self.loggy.info(f"Controlling {color} painting")
					mutated_stone = super().__call__(color)
					return	f"The stone {mutated_stone}"

			return	MutaboredStone


	class Antigen(Transmutation):
		def whatever_injection(self, layer :Transmutable) -> Transmutable :

			class MutatedStone(geminio(layer)):
				def __call__(self, color :str) -> str :

					self.loggy.info(f"Whitening the {color}")
					mutated_color = f"white-{color}"
					return	f"{super().__call__(mutated_color)}"

			return	MutatedStone


	class Antibor(Transmutation):
		def whatever_injection(self, layer :Transmutable) -> Transmutable :

			class MutaboredStone(geminio(layer)):
				def __call__(self, color :str) -> str :

					self.loggy.info(f"Controlling {color} painting")
					mutated_stone = super().__call__(color)
					return	f"The stone {mutated_stone}"

			return	MutaboredStone


	class PaintBrash(Transmutable):
		def __call__(self, color :str) -> str :

			painting = f"will be turned {color}"
			self.loggy.info(painting)

			return	painting








	def test_transmutation(self):

		trnsmtn = str(self.MAGICAL_ROOT /"trnsmtn.loggy")
		self.make_loggy_file(trnsmtn)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= trnsmtn
				init_name	= "trnsmtn-1"

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "will be turned dark-red")
		self.test_case.loggy.close()

		with open(trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@trnsmtn-1 INFO : Darkening the red",
				"@trnsmtn-1 INFO : will be turned dark-red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= trnsmtn
				init_name	= "trnsmtn-2"
				init_level	= 10

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "will be turned dark-green")
		self.test_case.loggy.close()

		with open(trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= trnsmtn
				init_name		= "trnsmtn-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(trnsmtn): os.remove(trnsmtn)








	def test_name_transmutation(self):

		n_trnsmtn = str(self.MAGICAL_ROOT /"n_trnsmtn.loggy")
		self.make_loggy_file(n_trnsmtn)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= n_trnsmtn
				init_name	= "n_trnsmtn-1"

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("blue"), "will be turned dark-blue")
		self.test_case.loggy.close()

		with open(n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@n_trnsmtn-1 INFO : Darkening the blue",
				"@n_trnsmtn-1 INFO : will be turned dark-blue",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= n_trnsmtn
				init_name	= "n_trnsmtn-2"
				init_level	= 10

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("amber"), "will be turned dark-amber")
		self.test_case.loggy.close()

		with open(n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@n_trnsmtn-2-Stone.Paint INFO : Darkening the amber",
				"@n_trnsmtn-2-Stone.Paint INFO : will be turned dark-amber",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= n_trnsmtn
				init_name		= "n_trnsmtn-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("magenta"), "will be turned dark-magenta")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@n_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the magenta",
				"@n_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-magenta",
				"@n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(n_trnsmtn): os.remove(n_trnsmtn)








	def test_escalated_transmutation(self):

		e_trnsmtn = str(self.MAGICAL_ROOT /"e_trnsmtn.loggy")
		self.make_loggy_file(e_trnsmtn)


		class Stone(Transmutable):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class loggy(LibraryContrib):

					handler		= e_trnsmtn
					init_name	= "e_trnsmtn-1"

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("white"), "will be turned dark-white")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_trnsmtn-1 INFO : Darkening the white",
				"@e_trnsmtn-1 INFO : will be turned dark-white",
				"@e_trnsmtn-1 WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class loggy(LibraryContrib):

					handler		= e_trnsmtn
					init_name	= "e_trnsmtn-2"
					init_level	= 10

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("maroon"), "will be turned dark-maroon")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_trnsmtn-2-Stone.Paint INFO : Darkening the maroon",
				"@e_trnsmtn-2-Stone.Paint INFO : will be turned dark-maroon",
				"@e_trnsmtn-2-Stone WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= e_trnsmtn
						init_name		= "e_trnsmtn-3"
						force_handover	= True

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("yellow"), "will be turned dark-yellow")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the yellow",
				"@e_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-yellow",
				"@e_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
				"@e_trnsmtn-3-Stone WARNING : This stone is uncontrollable!",
			]
		)
		if	os.path.isfile(e_trnsmtn): os.remove(e_trnsmtn)








	def test_escalated_name_transmutation(self):

		en_trnsmtn = str(self.MAGICAL_ROOT /"en_trnsmtn.loggy")
		self.make_loggy_file(en_trnsmtn)


		class Stone(Transmutable):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= en_trnsmtn
					init_name	= "en_trnsmtn-1"

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("gray"), "will be turned dark-gray")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(en_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@en_trnsmtn-1 INFO : Darkening the gray",
				"@en_trnsmtn-1 INFO : will be turned dark-gray",
				"@en_trnsmtn-1 WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= en_trnsmtn
					init_name	= "en_trnsmtn-2"
					init_level	= 10

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(en_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("orange"), "will be turned dark-orange")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(en_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@en_trnsmtn-2-Stone.Paint INFO : Darkening the orange",
				"@en_trnsmtn-2-Stone.Paint INFO : will be turned dark-orange",
				"@en_trnsmtn-2-Stone WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= en_trnsmtn
						init_name		= "en_trnsmtn-3"
						force_handover	= True

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(en_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("pink"), "will be turned dark-pink")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(en_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@en_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the pink",
				"@en_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-pink",
				"@en_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
				"@en_trnsmtn-3-Stone WARNING : This stone is uncontrollable!",
			]
		)
		if	os.path.isfile(en_trnsmtn): os.remove(en_trnsmtn)








	def test_no_loggy_transmutation(self):
		class Stone(Transmutable):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("jade"), "will be turned dark-jade")
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
















	def test_loaded_transmutation(self):

		loaded_trnsmtn = str(self.MAGICAL_ROOT /"loaded_trnsmtn.loggy")
		self.make_loggy_file(loaded_trnsmtn)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= loaded_trnsmtn
				init_name	= "loaded_trnsmtn-1"

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(loaded_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_trnsmtn-1 INFO : Controlling red painting",
				"@loaded_trnsmtn-1 INFO : Darkening the red",
				"@loaded_trnsmtn-1 INFO : will be turned dark-red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= loaded_trnsmtn
				init_name	= "loaded_trnsmtn-2"
				init_level	= 10

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(loaded_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(loaded_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_trnsmtn-2-Stone.Paint INFO : Controlling green painting",
				"@loaded_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@loaded_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= loaded_trnsmtn
				init_name		= "loaded_trnsmtn-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(loaded_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(loaded_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_trnsmtn-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@loaded_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@loaded_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@loaded_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(loaded_trnsmtn): os.remove(loaded_trnsmtn)








	def test_loaded_name_transmutation(self):

		l_n_trnsmtn = str(self.MAGICAL_ROOT /"l_n_trnsmtn.loggy")
		self.make_loggy_file(l_n_trnsmtn)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= l_n_trnsmtn
				init_name	= "l_n_trnsmtn-1"

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(l_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_n_trnsmtn-1 INFO : Controlling red painting",
				"@l_n_trnsmtn-1 INFO : Darkening the red",
				"@l_n_trnsmtn-1 INFO : will be turned dark-red",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= l_n_trnsmtn
				init_name	= "l_n_trnsmtn-2"
				init_level	= 10

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(l_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(l_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_n_trnsmtn-2-Stone.Paint INFO : Controlling green painting",
				"@l_n_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@l_n_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= l_n_trnsmtn
				init_name		= "l_n_trnsmtn-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(l_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(l_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_n_trnsmtn-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@l_n_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@l_n_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@l_n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(l_n_trnsmtn): os.remove(l_n_trnsmtn)








	def test_loaded_escalated_transmutation(self):

		l_e_trnsmtn = str(self.MAGICAL_ROOT /"l_e_trnsmtn.loggy")
		self.make_loggy_file(l_e_trnsmtn)


		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class loggy(LibraryContrib):

					handler		= l_e_trnsmtn
					init_name	= "l_e_trnsmtn-1"

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(l_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_e_trnsmtn-1 INFO : Controlling red painting",
				"@l_e_trnsmtn-1 INFO : Darkening the red",
				"@l_e_trnsmtn-1 INFO : will be turned dark-red",
				"@l_e_trnsmtn-1 WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class loggy(LibraryContrib):

					handler		= l_e_trnsmtn
					init_name	= "l_e_trnsmtn-2"
					init_level	= 10

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(l_e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(l_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_e_trnsmtn-2-Stone.Paint INFO : Controlling green painting",
				"@l_e_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@l_e_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
				"@l_e_trnsmtn-2-Stone WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= l_e_trnsmtn
						init_name		= "l_e_trnsmtn-3"
						force_handover	= True

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(l_e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(l_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_e_trnsmtn-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@l_e_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@l_e_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@l_e_trnsmtn-3-Stone WARNING : This stone is uncontrollable!",
				"@l_e_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(l_e_trnsmtn): os.remove(l_e_trnsmtn)








	def test_loaded_escalated_name_transmutation(self):

		l_e_n_trnsmtn = str(self.MAGICAL_ROOT /"l_e_n_trnsmtn.loggy")
		self.make_loggy_file(l_e_n_trnsmtn)


		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= l_e_n_trnsmtn
					init_name	= "l_e_n_trnsmtn-1"

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(l_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_e_n_trnsmtn-1 INFO : Controlling red painting",
				"@l_e_n_trnsmtn-1 INFO : Darkening the red",
				"@l_e_n_trnsmtn-1 INFO : will be turned dark-red",
				"@l_e_n_trnsmtn-1 WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= l_e_n_trnsmtn
					init_name	= "l_e_n_trnsmtn-2"
					init_level	= 10

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(l_e_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(l_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_e_n_trnsmtn-2-Stone.Paint INFO : Controlling green painting",
				"@l_e_n_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@l_e_n_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
				"@l_e_n_trnsmtn-2-Stone WARNING : This stone is uncontrollable!",
			]
		)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= l_e_n_trnsmtn
						init_name		= "l_e_n_trnsmtn-3"
						force_handover	= True

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(l_e_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(l_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_e_n_trnsmtn-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@l_e_n_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@l_e_n_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@l_e_n_trnsmtn-3-Stone WARNING : This stone is uncontrollable!",
				"@l_e_n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(l_e_n_trnsmtn): os.remove(l_e_n_trnsmtn)








	def test_loaded_no_loggy_transmutation(self):
		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
















	def test_top_layer_transmutation(self):

		top_layer_t = str(self.MAGICAL_ROOT /"top_layer_t.loggy")
		self.make_loggy_file(top_layer_t)


		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= top_layer_t
				init_name	= "top_layer_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "will be turned dark-red")
		self.test_case.loggy.close()

		with open(top_layer_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_t-1 INFO : Darkening the red",
				"@top_layer_t-1 INFO : will be turned dark-red",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= top_layer_t
				init_name	= "top_layer_t-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(top_layer_t)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("green"), "will be turned dark-green")
		self.test_case.loggy.close()

		with open(top_layer_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_t-2-StonePaint INFO : Darkening the green",
				"@top_layer_t-2-StonePaint INFO : will be turned dark-green",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler			= top_layer_t
				init_name		= "top_layer_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(top_layer_t)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("purple"), "will be turned dark-purple")
		self.test_case.loggy.close()

		with open(top_layer_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_t-3-StonePaint INFO : Darkening the purple",
				"@top_layer_t-3-StonePaint INFO : will be turned dark-purple",
			]
		)
		if	os.path.isfile(top_layer_t): os.remove(top_layer_t)








	def test_top_layer_name_transmutation(self):

		topl_nt = str(self.MAGICAL_ROOT /"topl_nt.loggy")
		self.make_loggy_file(topl_nt)


		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= topl_nt
				init_name	= "topl_nt-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("blue"), "will be turned dark-blue")
		self.test_case.loggy.close()

		with open(topl_nt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_nt-1 INFO : Darkening the blue",
				"@topl_nt-1 INFO : will be turned dark-blue",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= topl_nt
				init_name	= "topl_nt-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(topl_nt)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("amber"), "will be turned dark-amber")
		self.test_case.loggy.close()

		with open(topl_nt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_nt-2-StonePaint INFO : Darkening the amber",
				"@topl_nt-2-StonePaint INFO : will be turned dark-amber",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler			= topl_nt
				init_name		= "topl_nt-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(topl_nt)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("magenta"), "will be turned dark-magenta")
		self.test_case.loggy.close()

		with open(topl_nt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_nt-3-StonePaint INFO : Darkening the magenta",
				"@topl_nt-3-StonePaint INFO : will be turned dark-magenta",
			]
		)
		if	os.path.isfile(topl_nt): os.remove(topl_nt)








	def test_top_layer_escalated_transmutation(self):

		topl_e_t = str(self.MAGICAL_ROOT /"topl_e_t.loggy")
		self.make_loggy_file(topl_e_t)


		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler		= topl_e_t
					init_name	= "topl_e_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("white"), "will be turned dark-white")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_e_t-1 INFO : Darkening the white",
				"@topl_e_t-1 INFO : will be turned dark-white",
				"@topl_e_t-1 WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler		= topl_e_t
					init_name	= "topl_e_t-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(topl_e_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("maroon"), "will be turned dark-maroon")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_e_t-2-StonePaint INFO : Darkening the maroon",
				"@topl_e_t-2-StonePaint INFO : will be turned dark-maroon",
				"@topl_e_t-2-StonePaint WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler			= topl_e_t
					init_name		= "topl_e_t-3"
					force_handover	= True


		loggy = []
		self.make_loggy_file(topl_e_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("yellow"), "will be turned dark-yellow")
		self.assertIsNone(self.test_case.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_e_t-3-StonePaint INFO : Darkening the yellow",
				"@topl_e_t-3-StonePaint INFO : will be turned dark-yellow",
				"@topl_e_t-3-StonePaint WARNING : This stone is uncontrollable!",
			]
		)
		if	os.path.isfile(topl_e_t): os.remove(topl_e_t)








	def test_top_layer_escalated_name_transmutation(self):

		topl_e_n_t = str(self.MAGICAL_ROOT /"topl_e_n_t.loggy")
		self.make_loggy_file(topl_e_n_t)


		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= topl_e_n_t
					init_name	= "topl_e_n_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("gray"), "will be turned dark-gray")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_e_n_t-1 INFO : Darkening the gray",
				"@topl_e_n_t-1 INFO : will be turned dark-gray",
				"@topl_e_n_t-1 WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= topl_e_n_t
					init_name	= "topl_e_n_t-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(topl_e_n_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("orange"), "will be turned dark-orange")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_e_n_t-2-StonePaint INFO : Darkening the orange",
				"@topl_e_n_t-2-StonePaint INFO : will be turned dark-orange",
				"@topl_e_n_t-2-StonePaint.Handle WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= topl_e_n_t
					init_name		= "topl_e_n_t-3"
					force_handover	= True


		loggy = []
		self.make_loggy_file(topl_e_n_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("pink"), "will be turned dark-pink")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_e_n_t-3-StonePaint INFO : Darkening the pink",
				"@topl_e_n_t-3-StonePaint INFO : will be turned dark-pink",
				"@topl_e_n_t-3-StonePaint.Handle WARNING : This stone is uncontrollable!",
			]
		)
		if	os.path.isfile(topl_e_n_t): os.remove(topl_e_n_t)








	def test_top_layer_no_loggy_transmutation(self):

		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):	pass

		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("jade"), "will be turned dark-jade")
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
















	def test_top_layer_loaded_transmutation(self):

		topl_l_t = str(self.MAGICAL_ROOT /"topl_l_t.loggy")
		self.make_loggy_file(topl_l_t)


		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= topl_l_t
				init_name	= "topl_l_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(topl_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_t-1 INFO : Controlling red painting",
				"@topl_l_t-1 INFO : Darkening the red",
				"@topl_l_t-1 INFO : will be turned dark-red",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= topl_l_t
				init_name	= "topl_l_t-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(topl_l_t)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(topl_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_t-2-StonePaint INFO : Controlling green painting",
				"@topl_l_t-2-StonePaint INFO : Darkening the green",
				"@topl_l_t-2-StonePaint INFO : will be turned dark-green",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler			= topl_l_t
				init_name		= "topl_l_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(topl_l_t)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("purple"), "The stone will be turned dark-purple")
		self.test_case.loggy.close()

		with open(topl_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_t-3-StonePaint INFO : Controlling purple painting",
				"@topl_l_t-3-StonePaint INFO : Darkening the purple",
				"@topl_l_t-3-StonePaint INFO : will be turned dark-purple",
			]
		)
		if	os.path.isfile(topl_l_t): os.remove(topl_l_t)








	def test_top_layer_loaded_name_transmutation(self):

		topl_l_n_t = str(self.MAGICAL_ROOT /"topl_l_n_t.loggy")
		self.make_loggy_file(topl_l_n_t)


		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= topl_l_n_t
				init_name	= "topl_l_n_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(topl_l_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_n_t-1 INFO : Controlling red painting",
				"@topl_l_n_t-1 INFO : Darkening the red",
				"@topl_l_n_t-1 INFO : will be turned dark-red",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= topl_l_n_t
				init_name	= "topl_l_n_t-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(topl_l_n_t)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(topl_l_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_n_t-2-StonePaint INFO : Controlling green painting",
				"@topl_l_n_t-2-StonePaint INFO : Darkening the green",
				"@topl_l_n_t-2-StonePaint INFO : will be turned dark-green",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler			= topl_l_n_t
				init_name		= "topl_l_n_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(topl_l_n_t)
		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("purple"), "The stone will be turned dark-purple")
		self.test_case.loggy.close()

		with open(topl_l_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_n_t-3-StonePaint INFO : Controlling purple painting",
				"@topl_l_n_t-3-StonePaint INFO : Darkening the purple",
				"@topl_l_n_t-3-StonePaint INFO : will be turned dark-purple",
			]
		)
		if	os.path.isfile(topl_l_n_t): os.remove(topl_l_n_t)








	def test_top_layer_loaded_escalated_transmutation(self):

		topl_l_e_t = str(self.MAGICAL_ROOT /"topl_l_e_t.loggy")
		self.make_loggy_file(topl_l_e_t)


		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler		= topl_l_e_t
					init_name	= "topl_l_e_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_l_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_e_t-1 INFO : Controlling red painting",
				"@topl_l_e_t-1 INFO : Darkening the red",
				"@topl_l_e_t-1 INFO : will be turned dark-red",
				"@topl_l_e_t-1 WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler		= topl_l_e_t
					init_name	= "topl_l_e_t-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(topl_l_e_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("green"), "The stone will be turned dark-green")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_l_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_e_t-2-StonePaint INFO : Controlling green painting",
				"@topl_l_e_t-2-StonePaint INFO : Darkening the green",
				"@topl_l_e_t-2-StonePaint INFO : will be turned dark-green",
				"@topl_l_e_t-2-StonePaint.Handle WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class loggy(LibraryContrib):

					handler			= topl_l_e_t
					init_name		= "topl_l_e_t-3"
					force_handover	= True


		loggy = []
		self.make_loggy_file(topl_l_e_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_l_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_e_t-3-StonePaint INFO : Controlling purple painting",
				"@topl_l_e_t-3-StonePaint INFO : Darkening the purple",
				"@topl_l_e_t-3-StonePaint INFO : will be turned dark-purple",
				"@topl_l_e_t-3-StonePaint.Handle WARNING : This stone is uncontrollable!",
			]
		)
		if	os.path.isfile(topl_l_e_t): os.remove(topl_l_e_t)








	def test_top_layer_loaded_escalated_name_transmutation(self):

		topl_l_e_n_t = str(self.MAGICAL_ROOT /"topl_l_e_n_t.loggy")
		self.make_loggy_file(topl_l_e_n_t)


		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= topl_l_e_n_t
					init_name	= "topl_l_e_n_t-1"


		loggy = []
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_l_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_e_n_t-1 INFO : Controlling red painting",
				"@topl_l_e_n_t-1 INFO : Darkening the red",
				"@topl_l_e_n_t-1 INFO : will be turned dark-red",
				"@topl_l_e_n_t-1 WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= topl_l_e_n_t
					init_name	= "topl_l_e_n_t-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(topl_l_e_n_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("green"), "The stone will be turned dark-green")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_l_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_e_n_t-2-StonePaint INFO : Controlling green painting",
				"@topl_l_e_n_t-2-StonePaint INFO : Darkening the green",
				"@topl_l_e_n_t-2-StonePaint INFO : will be turned dark-green",
				"@topl_l_e_n_t-2-StonePaint.Handle WARNING : This stone is uncontrollable!",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):

			class Handle(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= topl_l_e_n_t
					init_name		= "topl_l_e_n_t-3"
					force_handover	= True


		loggy = []
		self.make_loggy_file(topl_l_e_n_t)
		self.test_case = StonePaint()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertIsInstance(self.test_case.Handle, Transmutable)
		self.assertEqual(self.test_case("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Handle.loggy.warning("This stone is uncontrollable!"))
		self.test_case.loggy.close()

		with open(topl_l_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@topl_l_e_n_t-3-StonePaint INFO : Controlling purple painting",
				"@topl_l_e_n_t-3-StonePaint INFO : Darkening the purple",
				"@topl_l_e_n_t-3-StonePaint INFO : will be turned dark-purple",
				"@topl_l_e_n_t-3-StonePaint.Handle WARNING : This stone is uncontrollable!",
			]
		)
		if	os.path.isfile(topl_l_e_n_t): os.remove(topl_l_e_n_t)








	def test_top_layer_loaded_no_loggy_transmutation(self):

		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):	pass

		self.test_case = StonePaint()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
















	def test_outer_transmutation(self):

		outer_trnsmtn = str(self.MAGICAL_ROOT /"outer_trnsmtn.loggy")
		self.make_loggy_file(outer_trnsmtn)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= outer_trnsmtn
				init_name	= "outer_trnsmtn-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "will be turned dark-red")
		self.test_case.loggy.close()

		with open(outer_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_trnsmtn-1 INFO : Darkening the red",
				"@outer_trnsmtn-1 INFO : will be turned dark-red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= outer_trnsmtn
				init_name	= "outer_trnsmtn-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(outer_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "will be turned dark-green")
		self.test_case.loggy.close()

		with open(outer_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@outer_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= outer_trnsmtn
				init_name		= "outer_trnsmtn-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(outer_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(outer_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@outer_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@outer_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(outer_trnsmtn): os.remove(outer_trnsmtn)








	def test_outer_name_transmutation(self):

		out_n_trnsmtn = str(self.MAGICAL_ROOT /"out_n_trnsmtn.loggy")
		self.make_loggy_file(out_n_trnsmtn)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= out_n_trnsmtn
				init_name	= "out_n_trnsmtn-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("blue"), "will be turned dark-blue")
		self.test_case.loggy.close()

		with open(out_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_trnsmtn-1 INFO : Darkening the blue",
				"@out_n_trnsmtn-1 INFO : will be turned dark-blue",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= out_n_trnsmtn
				init_name	= "out_n_trnsmtn-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(out_n_trnsmtn)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case.Paint("amber"), "will be turned dark-amber")
		self.test_case.loggy.close()

		with open(out_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_trnsmtn-2-Stone.Paint INFO : Darkening the amber",
				"@out_n_trnsmtn-2-Stone.Paint INFO : will be turned dark-amber",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= out_n_trnsmtn
				init_name		= "out_n_trnsmtn-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(out_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("magenta"), "will be turned dark-magenta")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(out_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the magenta",
				"@out_n_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-magenta",
				"@out_n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(out_n_trnsmtn): os.remove(out_n_trnsmtn)








	def test_outer_escalated_transmutation(self):

		outer_e_trnsmtn = str(self.MAGICAL_ROOT /"outer_e_trnsmtn.loggy")
		self.make_loggy_file(outer_e_trnsmtn)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= outer_e_trnsmtn
					init_name	= "outer_e_trnsmtn-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "will be turned dark-red")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")
		self.test_case.loggy.close()

		with open(outer_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_trnsmtn-1 INFO : Darkening the red",
				"@outer_e_trnsmtn-1 INFO : will be turned dark-red",
				"@outer_e_trnsmtn-1 INFO : I am root",
				"@outer_e_trnsmtn-1 INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= outer_e_trnsmtn
					init_name	= "outer_e_trnsmtn-2"
					init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(outer_e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "will be turned dark-green")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")
		self.test_case.loggy.close()

		with open(outer_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@outer_e_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
				"@outer_e_trnsmtn-2-Stone INFO : I am root",
				"@outer_e_trnsmtn-2-Stone.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= outer_e_trnsmtn
					init_name		= "outer_e_trnsmtn-3"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(outer_e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "will be turned dark-purple")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(outer_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@outer_e_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@outer_e_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@outer_e_trnsmtn-3-Stone INFO : I am root",
				"@outer_e_trnsmtn-3-Stone.Bound INFO : I am bound",
				"@outer_e_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(outer_e_trnsmtn): os.remove(outer_e_trnsmtn)








	def test_outer_escalated_name_transmutation(self):

		out_e_n_trnsmtn = str(self.MAGICAL_ROOT /"out_e_n_trnsmtn.loggy")
		self.make_loggy_file(out_e_n_trnsmtn)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= out_e_n_trnsmtn
					init_name	= "out_e_n_trnsmtn-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "will be turned dark-red")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")
		self.test_case.loggy.close()

		with open(out_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_trnsmtn-1 INFO : Darkening the red",
				"@out_e_n_trnsmtn-1 INFO : will be turned dark-red",
				"@out_e_n_trnsmtn-1 INFO : I am root",
				"@out_e_n_trnsmtn-1 INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= out_e_n_trnsmtn
					init_name	= "out_e_n_trnsmtn-2"
					init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(out_e_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "will be turned dark-green")
		self.test_case.loggy.info("I am root")
		self.test_case.Bound.loggy.info("I am bound")
		self.test_case.loggy.close()

		with open(out_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@out_e_n_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
				"@out_e_n_trnsmtn-2-Stone INFO : I am root",
				"@out_e_n_trnsmtn-2-Stone.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= out_e_n_trnsmtn
					init_name		= "out_e_n_trnsmtn-3"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(out_e_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "will be turned dark-purple")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(out_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@out_e_n_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@out_e_n_trnsmtn-3-Stone INFO : I am root",
				"@out_e_n_trnsmtn-3-Stone.Bound INFO : I am bound",
				"@out_e_n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(out_e_n_trnsmtn): os.remove(out_e_n_trnsmtn)








	def test_outer_no_loggy_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "will be turned dark-purple")
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
















	def test_outer_loaded_transmutation(self):

		l_out_trnsmtn = str(self.MAGICAL_ROOT /"l_out_trnsmtn.loggy")
		self.make_loggy_file(l_out_trnsmtn)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= l_out_trnsmtn
				init_name	= "l_out_trnsmtn-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(l_out_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_out_trnsmtn-1 INFO : Controlling red painting",
				"@l_out_trnsmtn-1 INFO : Darkening the red",
				"@l_out_trnsmtn-1 INFO : will be turned dark-red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= l_out_trnsmtn
				init_name	= "l_out_trnsmtn-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(l_out_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(l_out_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_out_trnsmtn-2-Stone.Paint INFO : Controlling green painting",
				"@l_out_trnsmtn-2-Stone.Paint INFO : Darkening the green",
				"@l_out_trnsmtn-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= l_out_trnsmtn
				init_name		= "l_out_trnsmtn-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(l_out_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(l_out_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_out_trnsmtn-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@l_out_trnsmtn-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@l_out_trnsmtn-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@l_out_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(l_out_trnsmtn): os.remove(l_out_trnsmtn)








	def test_outer_loaded_name_transmutation(self):

		loaded_out_n_t = str(self.MAGICAL_ROOT /"loaded_out_n_t.loggy")
		self.make_loggy_file(loaded_out_n_t)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= loaded_out_n_t
				init_name	= "loaded_out_n_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(loaded_out_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_out_n_t-1 INFO : Controlling red painting",
				"@loaded_out_n_t-1 INFO : Darkening the red",
				"@loaded_out_n_t-1 INFO : will be turned dark-red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= loaded_out_n_t
				init_name	= "loaded_out_n_t-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(loaded_out_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(loaded_out_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_out_n_t-2-Stone.Paint INFO : Controlling green painting",
				"@loaded_out_n_t-2-Stone.Paint INFO : Darkening the green",
				"@loaded_out_n_t-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= loaded_out_n_t
				init_name		= "loaded_out_n_t-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(loaded_out_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(loaded_out_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_out_n_t-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@loaded_out_n_t-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@loaded_out_n_t-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@loaded_out_n_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(loaded_out_n_t): os.remove(loaded_out_n_t)








	def test_outer_loaded_escalated_transmutation(self):

		loaded_out_e_t = str(self.MAGICAL_ROOT /"loaded_out_e_t.loggy")
		self.make_loggy_file(loaded_out_e_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= loaded_out_e_t
					init_name	= "loaded_out_e_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(loaded_out_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_out_e_t-1 INFO : Controlling red painting",
				"@loaded_out_e_t-1 INFO : Darkening the red",
				"@loaded_out_e_t-1 INFO : will be turned dark-red",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= loaded_out_e_t
					init_name	= "loaded_out_e_t-2"
					init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(loaded_out_e_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(loaded_out_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_out_e_t-2-Stone.Paint INFO : Controlling green painting",
				"@loaded_out_e_t-2-Stone.Paint INFO : Darkening the green",
				"@loaded_out_e_t-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= loaded_out_e_t
					init_name		= "loaded_out_e_t-3"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(loaded_out_e_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(loaded_out_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@loaded_out_e_t-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@loaded_out_e_t-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@loaded_out_e_t-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@loaded_out_e_t-3-Stone.Grip ERROR : Cannot grip!",
				"@loaded_out_e_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(loaded_out_e_t): os.remove(loaded_out_e_t)








	def test_outer_loaded_escalated_name_transmutation(self):

		load_out_e_n_t = str(self.MAGICAL_ROOT /"load_out_e_n_t.loggy")
		self.make_loggy_file(load_out_e_n_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= load_out_e_n_t
					init_name	= "load_out_e_n_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("red"), "The stone will be turned dark-red")
		self.test_case.loggy.close()

		with open(load_out_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_out_e_n_t-1 INFO : Controlling red painting",
				"@load_out_e_n_t-1 INFO : Darkening the red",
				"@load_out_e_n_t-1 INFO : will be turned dark-red",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= load_out_e_n_t
					init_name	= "load_out_e_n_t-2"
					init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint(Transmutable):

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(load_out_e_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("green"), "The stone will be turned dark-green")
		self.test_case.loggy.close()

		with open(load_out_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_out_e_n_t-2-Stone.Paint INFO : Controlling green painting",
				"@load_out_e_n_t-2-Stone.Paint INFO : Darkening the green",
				"@load_out_e_n_t-2-Stone.Paint INFO : will be turned dark-green",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= load_out_e_n_t
					init_name		= "load_out_e_n_t-3"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(load_out_e_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(load_out_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_out_e_n_t-3-Stone.Grip.Paint INFO : Controlling purple painting",
				"@load_out_e_n_t-3-Stone.Grip.Paint INFO : Darkening the purple",
				"@load_out_e_n_t-3-Stone.Grip.Paint INFO : will be turned dark-purple",
				"@load_out_e_n_t-3-Stone.Grip ERROR : Cannot grip!",
				"@load_out_e_n_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(load_out_e_n_t): os.remove(load_out_e_n_t)








	def test_outer_loaded_no_loggy_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint(Transmutable):

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertTrue(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsInstance(self.test_case.Grip.Paint, Transmutable)
		self.assertEqual(self.test_case.Grip.Paint("purple"), "The stone will be turned dark-purple")
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_other_transmutation(self):

		other_trnsmtn = str(self.MAGICAL_ROOT /"other_trnsmtn.loggy")
		self.make_loggy_file(other_trnsmtn)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= other_trnsmtn
				init_name	= "other_trnsmtn-1"

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					return	f"will be turned {color}"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(other_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_trnsmtn-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= other_trnsmtn
				init_name	= "other_trnsmtn-2"
				init_level	= 10

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(other_trnsmtn)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(other_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_trnsmtn-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= other_trnsmtn
				init_name		= "other_trnsmtn-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(other_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(other_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_trnsmtn-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@other_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(other_trnsmtn): os.remove(other_trnsmtn)








	def test_other_name_transmutation(self):

		other_n_trnsmtn = str(self.MAGICAL_ROOT /"other_n_trnsmtn.loggy")
		self.make_loggy_file(other_n_trnsmtn)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= other_n_trnsmtn
				init_name	= "other_n_trnsmtn-1"

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					return	f"will be turned {color}"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(other_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_n_trnsmtn-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= other_n_trnsmtn
				init_name	= "other_n_trnsmtn-2"
				init_level	= 10

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(other_n_trnsmtn)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(other_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_n_trnsmtn-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= other_n_trnsmtn
				init_name		= "other_n_trnsmtn-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(other_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(other_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_n_trnsmtn-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@other_n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(other_n_trnsmtn): os.remove(other_n_trnsmtn)








	def test_other_escalated_transmutation(self):

		other_e_trnsmtn = str(self.MAGICAL_ROOT /"other_e_trnsmtn.loggy")
		self.make_loggy_file(other_e_trnsmtn)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= other_e_trnsmtn
					init_name	= "other_e_trnsmtn-1"

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					return	f"will be turned {color}"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(other_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_e_trnsmtn-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@other_e_trnsmtn-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= other_e_trnsmtn
					init_name	= "other_e_trnsmtn-2"
					init_level	= 10

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(other_e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(other_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_e_trnsmtn-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@other_e_trnsmtn-2-Stone.Bound INFO : I am bound"
			]
		)




		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= other_e_trnsmtn
					init_name		= "other_e_trnsmtn-3"
					force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(other_e_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(other_e_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@other_e_trnsmtn-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@other_e_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
				"@other_e_trnsmtn-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(other_e_trnsmtn): os.remove(other_e_trnsmtn)








	def test_other_escalated_name_transmutation(self):

		ot_e_n_trnsmtn = str(self.MAGICAL_ROOT /"ot_e_n_trnsmtn.loggy")
		self.make_loggy_file(ot_e_n_trnsmtn)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= ot_e_n_trnsmtn
					init_name	= "ot_e_n_trnsmtn-1"

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					return	f"will be turned {color}"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_e_n_trnsmtn-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@ot_e_n_trnsmtn-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= ot_e_n_trnsmtn
					init_name	= "ot_e_n_trnsmtn-2"
					init_level	= 10

			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(ot_e_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_e_n_trnsmtn-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_e_n_trnsmtn-2-Stone.Bound INFO : I am bound"
			]
		)




		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= ot_e_n_trnsmtn
					init_name		= "ot_e_n_trnsmtn-3"
					force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(ot_e_n_trnsmtn)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_n_trnsmtn) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_e_n_trnsmtn-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_e_n_trnsmtn-3-Stone.Grip ERROR : Cannot grip!",
				"@ot_e_n_trnsmtn-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(ot_e_n_trnsmtn): os.remove(ot_e_n_trnsmtn)








	def test_other_no_loggy_transmutation(self):

		class Stone(Transmutable):
			class Bound(Transmutable):	pass

			class Grip(Transmutable):

				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_other_loaded_transmutation(self):

		load_other_t = str(self.MAGICAL_ROOT /"load_other_t.loggy")
		self.make_loggy_file(load_other_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= load_other_t
				init_name	= "load_other_t-1"

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					return	f"will be turned {color}"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(load_other_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_other_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= load_other_t
				init_name	= "load_other_t-2"
				init_level	= 10

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(load_other_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(load_other_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_other_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= load_other_t
				init_name		= "load_other_t-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(load_other_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(load_other_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_other_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@load_other_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(load_other_t): os.remove(load_other_t)








	def test_other_loaded_name_transmutation(self):

		load_other_n_t = str(self.MAGICAL_ROOT /"load_other_n_t.loggy")
		self.make_loggy_file(load_other_n_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= load_other_n_t
				init_name	= "load_other_n_t-1"

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					return	f"will be turned {color}"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(load_other_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_other_n_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= load_other_n_t
				init_name	= "load_other_n_t-2"
				init_level	= 10

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(load_other_n_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(load_other_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_other_n_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation"
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= load_other_n_t
				init_name		= "load_other_n_t-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(load_other_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(load_other_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_other_n_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@load_other_n_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(load_other_n_t): os.remove(load_other_n_t)








	def test_other_loaded_escalated_transmutation(self):

		lo_other_e_t = str(self.MAGICAL_ROOT /"lo_other_e_t.loggy")
		self.make_loggy_file(lo_other_e_t)


		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:
				class loggy(LibraryContrib):

					handler		= lo_other_e_t
					init_name	= "lo_other_e_t-1"

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.test_case.loggy.close()

		with open(lo_other_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:
				class loggy(LibraryContrib):

					handler		= lo_other_e_t
					init_name	= "lo_other_e_t-2"
					init_level	= 10

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(lo_other_e_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.test_case.loggy.close()

		with open(lo_other_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint:
					class loggy(LibraryContrib):

						handler			= lo_other_e_t
						init_name		= "lo_other_e_t-3"
						force_handover	= True

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(lo_other_e_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(lo_other_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(lo_other_e_t): os.remove(lo_other_e_t)








	def test_other_loaded_escalated_name_transmutation(self):

		lo_other_e_n_t = str(self.MAGICAL_ROOT /"lo_other_e_n_t.loggy")
		self.make_loggy_file(lo_other_e_n_t)


		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:
				class shmoggy(LibraryContrib):

					handler		= lo_other_e_n_t
					init_name	= "lo_other_e_n_t-1"

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.test_case.loggy.close()

		with open(lo_other_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Mutagen
			class Paint:
				class shmoggy(LibraryContrib):

					handler		= lo_other_e_n_t
					init_name	= "lo_other_e_n_t-2"
					init_level	= 10

				def __call__(self, color :str) -> str :

					painting = f"will be turned {color}"
					self.loggy.info(painting)

					return	painting


		loggy = []
		self.make_loggy_file(lo_other_e_n_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.test_case.loggy.close()

		with open(lo_other_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint:
					class shmoggy(LibraryContrib):

						handler			= lo_other_e_n_t
						init_name		= "lo_other_e_n_t-3"
						force_handover	= True

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		loggy = []
		self.make_loggy_file(lo_other_e_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(lo_other_e_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(lo_other_e_n_t): os.remove(lo_other_e_n_t)








	def test_other_loaded_no_loggy(self):

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Mutagen
				class Paint:

					def __call__(self, color :str) -> str :

						painting = f"will be turned {color}"
						self.loggy.info(painting)

						return	painting


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
















	def test_other_top_layer_transmutation(self):

		@StoneMutationCase.Mutagen
		class StonePaint:
			class loggy(LibraryContrib): init_name = "top_layer_other-1"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint:
			class loggy(LibraryContrib): init_name = "top_layer_other-2"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)
















	def test_kws_top_layer_transmutation(self):

		top_layer_a_t = str(self.MAGICAL_ROOT /"top_layer_a_t.loggy")
		self.make_loggy_file(top_layer_a_t)


		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= top_layer_a_t
				init_name	= "top_layer_a_t-1"

			def schedule(self):

				self.loggy.debug("Start processing the schedule")
				self.loggy.info(f"Painting scheduled to {self.when}")
				return f"Painting scheduled to {self.when}"


		loggy = []
		self.test_case = StonePaint(when="the day after tomorrow")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "will be turned dark-red")
		self.assertEqual(self.test_case.schedule(), "Painting scheduled to the day after tomorrow")
		self.test_case.loggy.close()

		with open(top_layer_a_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_a_t-1 INFO : Darkening the red",
				"@top_layer_a_t-1 INFO : will be turned dark-red",
				"@top_layer_a_t-1 INFO : Painting scheduled to the day after tomorrow",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= top_layer_a_t
				init_name	= "top_layer_a_t-2"
				init_level	= 10

			def schedule(self):

				self.loggy.debug("Start processing the schedule")
				self.loggy.info(f"Painting scheduled to {self.when}")
				return f"Painting scheduled to {self.when}"


		loggy = []
		self.make_loggy_file(top_layer_a_t)
		self.test_case = StonePaint(when="the day after tomorrow")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "will be turned dark-red")
		self.assertEqual(self.test_case.schedule(), "Painting scheduled to the day after tomorrow")
		self.test_case.loggy.close()

		with open(top_layer_a_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_a_t-2-StonePaint INFO : Darkening the red",
				"@top_layer_a_t-2-StonePaint INFO : will be turned dark-red",
				"@top_layer_a_t-2-StonePaint DEBUG : Start processing the schedule",
				"@top_layer_a_t-2-StonePaint INFO : Painting scheduled to the day after tomorrow",
			]
		)




		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class Schedule(Transmutable):

				class loggy(LibraryContrib):

					handler			= top_layer_a_t
					init_name		= "top_layer_a_t-3"
					force_handover	= True

				def __call__(self):

					self.loggy.debug("Start processing the schedule")
					self.loggy.info(f"Painting scheduled to {self.when}")
					return f"Painting scheduled to {self.when}"


		loggy = []
		self.make_loggy_file(top_layer_a_t)
		self.test_case = StonePaint(when="the day after tomorrow")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Schedule"))
		self.assertEqual(self.test_case("red"), "will be turned dark-red")
		self.assertEqual(self.test_case.Schedule(), "Painting scheduled to the day after tomorrow")
		self.assertIsNone(self.test_case.loggy.debug("Stone is scheduled"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(top_layer_a_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_a_t-3-StonePaint INFO : Darkening the red",
				"@top_layer_a_t-3-StonePaint INFO : will be turned dark-red",
				"@top_layer_a_t-3-StonePaint.Schedule INFO : Painting scheduled to the day after tomorrow",
				"@top_layer_a_t-3-StonePaint INFO : I am root",
			]
		)
		if	os.path.isfile(top_layer_a_t): os.remove(top_layer_a_t)
















	def test_kws_top_layer_loaded_transmutation(self):

		top_layer_a_l_t = str(self.MAGICAL_ROOT /"top_layer_a_l_t.loggy")
		self.make_loggy_file(top_layer_a_l_t)


		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= top_layer_a_l_t
				init_name	= "top_layer_a_l_t-1"

			def schedule(self):

				self.loggy.debug("Start processing the schedule")
				self.loggy.info(f"Painting scheduled to {self.when}")
				return f"Painting scheduled to {self.when}"


		loggy = []
		self.test_case = StonePaint(when="the day after tomorrow")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.assertEqual(self.test_case.schedule(), "Painting scheduled to the day after tomorrow")
		self.test_case.loggy.close()

		with open(top_layer_a_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_a_l_t-1 INFO : Controlling red painting",
				"@top_layer_a_l_t-1 INFO : Darkening the red",
				"@top_layer_a_l_t-1 INFO : will be turned dark-red",
				"@top_layer_a_l_t-1 INFO : Painting scheduled to the day after tomorrow",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= top_layer_a_l_t
				init_name	= "top_layer_a_l_t-2"
				init_level	= 10

			def schedule(self):

				self.loggy.debug("Start processing the schedule")
				self.loggy.info(f"Painting scheduled to {self.when}")
				return f"Painting scheduled to {self.when}"


		loggy = []
		self.make_loggy_file(top_layer_a_l_t)
		self.test_case = StonePaint(when="the day after tomorrow")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.assertEqual(self.test_case.schedule(), "Painting scheduled to the day after tomorrow")
		self.test_case.loggy.close()

		with open(top_layer_a_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_a_l_t-2-StonePaint INFO : Controlling red painting",
				"@top_layer_a_l_t-2-StonePaint INFO : Darkening the red",
				"@top_layer_a_l_t-2-StonePaint INFO : will be turned dark-red",
				"@top_layer_a_l_t-2-StonePaint DEBUG : Start processing the schedule",
				"@top_layer_a_l_t-2-StonePaint INFO : Painting scheduled to the day after tomorrow",
			]
		)




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Mutagen
		class StonePaint(StoneMutationCase.PaintBrash):
			class Schedule(Transmutable):

				class loggy(LibraryContrib):

					handler			= top_layer_a_l_t
					init_name		= "top_layer_a_l_t-3"
					force_handover	= True

				def __call__(self):

					self.loggy.debug("Start processing the schedule")
					self.loggy.info(f"Painting scheduled to {self.when}")
					return f"Painting scheduled to {self.when}"


		loggy = []
		self.make_loggy_file(top_layer_a_l_t)
		self.test_case = StonePaint(when="the day after tomorrow")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Schedule"))
		self.assertEqual(self.test_case("red"), "The stone will be turned dark-red")
		self.assertEqual(self.test_case.Schedule(), "Painting scheduled to the day after tomorrow")
		self.assertIsNone(self.test_case.loggy.debug("Stone is scheduled"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(top_layer_a_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_layer_a_l_t-3-StonePaint INFO : Controlling red painting",
				"@top_layer_a_l_t-3-StonePaint INFO : Darkening the red",
				"@top_layer_a_l_t-3-StonePaint INFO : will be turned dark-red",
				"@top_layer_a_l_t-3-StonePaint.Schedule INFO : Painting scheduled to the day after tomorrow",
				"@top_layer_a_l_t-3-StonePaint INFO : I am root",
			]
		)
		if	os.path.isfile(top_layer_a_l_t): os.remove(top_layer_a_l_t)
















	def test_mutable_chain_injection_transmutation(self):

		m_c_i_t = str(self.MAGICAL_ROOT /"m_c_i_t.loggy")
		self.make_loggy_file(m_c_i_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_c_i_t
				init_name	= "m_c_i_t-1"

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_c_i_t
				init_name	= "m_c_i_t-2"
				init_level	= 10

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= m_c_i_t
				init_name		= "m_c_i_t-3"
				force_handover	= True

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_t-3-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)
		if	os.path.isfile(m_c_i_t): os.remove(m_c_i_t)








	def test_mutable_chain_injection_name_transmutation(self):

		m_c_i_n_t = str(self.MAGICAL_ROOT /"m_c_i_n_t.loggy")
		self.make_loggy_file(m_c_i_n_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_c_i_n_t
				init_name	= "m_c_i_n_t-1"

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass

		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_n_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_c_i_n_t
				init_name	= "m_c_i_n_t-2"
				init_level	= 10

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_n_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_n_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= m_c_i_n_t
				init_name		= "m_c_i_n_t-3"
				force_handover	= True

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_n_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_n_t-3-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)
		if	os.path.isfile(m_c_i_n_t): os.remove(m_c_i_n_t)








	def test_mutable_chain_injection_escalated_transmutation(self):

		m_c_i_e_t = str(self.MAGICAL_ROOT /"m_c_i_e_t.loggy")
		self.make_loggy_file(m_c_i_e_t)

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= m_c_i_e_t
						init_name		= "m_c_i_e_t"
						force_handover	= True


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_e_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(m_c_i_e_t): os.remove(m_c_i_e_t)








	def test_mutable_chain_injection_escalated_name_transmutation(self):

		m_c_i_en_t = str(self.MAGICAL_ROOT /"m_c_i_en_t.loggy")
		self.make_loggy_file(m_c_i_en_t)

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= m_c_i_en_t
						init_name		= "m_c_i_en_t"
						force_handover	= True


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_en_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(m_c_i_en_t): os.remove(m_c_i_en_t)








	def test_mutable_chain_injection_no_loggy_transmutation(self):

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
















	def test_mutable_chain_injection_loaded_transmutation(self):

		m_c_i_l_t = str(self.MAGICAL_ROOT /"m_c_i_l_t.loggy")
		self.make_loggy_file(m_c_i_l_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_c_i_l_t
				init_name	= "m_c_i_l_t-1"

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_l_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_c_i_l_t
				init_name	= "m_c_i_l_t-2"
				init_level	= 10

			@StoneMutationCase.Antigen
			@StoneMutationCase.Mutabor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_l_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_l_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= m_c_i_l_t
				init_name		= "m_c_i_l_t-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_l_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(m_c_i_l_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_l_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@m_c_i_l_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(m_c_i_l_t): os.remove(m_c_i_l_t)








	def test_mutable_chain_injection_loaded_name_transmutation(self):

		m_c_i_ln_t = str(self.MAGICAL_ROOT /"m_c_i_ln_t.loggy")
		self.make_loggy_file(m_c_i_ln_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_c_i_ln_t
				init_name	= "m_c_i_ln_t-1"

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_ln_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_ln_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_c_i_ln_t
				init_name	= "m_c_i_ln_t-2"
				init_level	= 10

			@StoneMutationCase.Antigen
			@StoneMutationCase.Mutabor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_ln_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_ln_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_ln_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= m_c_i_ln_t
				init_name		= "m_c_i_ln_t-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_ln_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(m_c_i_ln_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_ln_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@m_c_i_ln_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(m_c_i_ln_t): os.remove(m_c_i_ln_t)








	def test_mutable_chain_injection_loaded_escalated_transmutation(self):

		m_c_i_le_t = str(self.MAGICAL_ROOT /"m_c_i_le_t.loggy")
		self.make_loggy_file(m_c_i_le_t)

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= m_c_i_le_t
						init_name		= "m_c_i_le_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_le_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= m_c_i_le_t
						init_name		= "m_c_i_le_t-2"


		loggy = []
		self.make_loggy_file(m_c_i_le_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_le_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(m_c_i_le_t): os.remove(m_c_i_le_t)








	def test_mutable_chain_injection_loaded_escalated_name_transmutation(self):

		m_c_i_len_t = str(self.MAGICAL_ROOT /"m_c_i_len_t.loggy")
		self.make_loggy_file(m_c_i_len_t)

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= m_c_i_len_t
						init_name		= "m_c_i_len_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_len_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= m_c_i_len_t
						init_name		= "m_c_i_len_t-2"


		loggy = []
		self.make_loggy_file(m_c_i_len_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_len_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(m_c_i_len_t): os.remove(m_c_i_len_t)








	def test_mutable_chain_injection_loaded_no_loggy_transmutation(self):

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
















	def test_mutable_chain_injection_top_layer_transmutation(self):

		mci_tl_t = str(self.MAGICAL_ROOT /"mci_tl_t.loggy")
		self.make_loggy_file(mci_tl_t)


		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= mci_tl_t
				init_name	= "mci_tl_t"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)

		with open(mci_tl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)
		if	os.path.isfile(mci_tl_t): os.remove(mci_tl_t)
















	def test_mutable_chain_injection_top_layer_loaded_transmutation(self):

		mci_tll_t = str(self.MAGICAL_ROOT /"mci_tll_t.loggy")
		self.make_loggy_file(mci_tll_t)


		@StoneMutationCase.Mutabor
		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= mci_tll_t
				init_name	= "mci_tll_t-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)

		with open(mci_tll_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneMutationCase.Antigen
		@StoneMutationCase.Mutabor
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= mci_tll_t
				init_name	= "mci_tll_t-2"


		loggy = []
		self.make_loggy_file(mci_tll_t)
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)

		with open(mci_tll_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneMutationCase.Mutabor
		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)




		@StoneMutationCase.Antigen
		@StoneMutationCase.Mutabor
		class StonePaint(StoneMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)
		if	os.path.isfile(mci_tll_t): os.remove(mci_tll_t)
















	def test_mutable_chain_injection_outer_transmutation(self):

		mci_o_t = str(self.MAGICAL_ROOT /"mci_o_t.loggy")
		self.make_loggy_file(mci_o_t)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_o_t
				init_name	= "mci_o_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_o_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_o_t
				init_name	= "mci_o_t-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_o_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_o_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_o_t
				init_name		= "mci_o_t-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_o_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_o_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_o_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(mci_o_t): os.remove(mci_o_t)








	def test_mutable_chain_injection_outer_name_transmutation(self):

		mci_o_n_t = str(self.MAGICAL_ROOT /"mci_o_n_t.loggy")
		self.make_loggy_file(mci_o_n_t)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_o_n_t
				init_name	= "mci_o_n_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.loggy.critical("This stone is lost"))
		self.test_case.loggy.close()

		with open(mci_o_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_n_t-1 CRITICAL : This stone is lost",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_o_n_t
				init_name	= "mci_o_n_t-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_o_n_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.loggy.critical("This stone is lost"))
		self.test_case.loggy.close()

		with open(mci_o_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_n_t-2-Stone CRITICAL : This stone is lost",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_o_n_t
				init_name		= "mci_o_n_t-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_o_n_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.loggy.critical("This stone is lost"))
		self.test_case.loggy.close()

		with open(mci_o_n_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_n_t-3-Stone.Grip ERROR : Cannot grip!",
				"@mci_o_n_t-3-Stone CRITICAL : This stone is lost",
			]
		)
		if	os.path.isfile(mci_o_n_t): os.remove(mci_o_n_t)








	def test_mutable_chain_injection_outer_escalated_transmutation(self):

		mci_oe_t = str(self.MAGICAL_ROOT /"mci_oe_t.loggy")
		self.make_loggy_file(mci_oe_t)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_oe_t
					init_name		= "mci_oe_t"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_oe_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oe_t-Stone INFO : I am root",
				"@mci_oe_t-Stone.Bound INFO : I am bound",
				"@mci_oe_t-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(mci_oe_t): os.remove(mci_oe_t)








	def test_mutable_chain_injection_outer_escalated_name_transmutation(self):

		mci_oen_t = str(self.MAGICAL_ROOT /"mci_oen_t.loggy")
		self.make_loggy_file(mci_oen_t)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_oen_t
					init_name		= "mci_oen_t"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_oen_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_oen_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oen_t-Stone INFO : I am root",
				"@mci_oen_t-Stone.Bound INFO : I am bound",
				"@mci_oen_t-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(mci_oen_t): os.remove(mci_oen_t)








	def test_mutable_chain_injection_outer_no_loggy_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
















	def test_mutable_chain_injection_outer_loaded_transmutation(self):

		mci_ol_t = str(self.MAGICAL_ROOT /"mci_ol_t.loggy")
		self.make_loggy_file(mci_ol_t)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ol_t
				init_name	= "mci_ol_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Mutabor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ol_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ol_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ol_t
				init_name	= "mci_ol_t-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			@StoneMutationCase.Mutabor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_ol_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ol_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ol_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_ol_t
				init_name		= "mci_ol_t-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_ol_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_ol_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ol_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_ol_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(mci_ol_t): os.remove(mci_ol_t)








	def test_mutable_chain_injection_outer_loaded_name_transmutation(self):

		mci_oln_t = str(self.MAGICAL_ROOT /"mci_oln_t.loggy")
		self.make_loggy_file(mci_oln_t)

		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_oln_t
				init_name	= "mci_oln_t-1"
				init_level	= 10


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_oln_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oln_t-1-Stone.Grip ERROR : Cannot grip!",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_oln_t
				init_name		= "mci_oln_t-2"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_oln_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_oln_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oln_t-2-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(mci_oln_t): os.remove(mci_oln_t)








	def test_mutable_chain_injection_outer_loaded_escalated_transmutation(self):

		mci_ole_t = str(self.MAGICAL_ROOT /"mci_ole_t.loggy")
		self.make_loggy_file(mci_ole_t)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ole_t
					init_name	= "mci_ole_t-1"
					init_level	= 10


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ole_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ole_t-1-Stone.Grip ERROR : Cannot grip!",
				"@mci_ole_t-1-Stone.Bound DEBUG : I am bound, but nobody cares",
				"@mci_ole_t-1-Stone INFO : I am root",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_ole_t
					init_name		= "mci_ole_t-2"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_ole_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ole_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ole_t-2-Stone.Grip ERROR : Cannot grip!",
				"@mci_ole_t-2-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_ole_t): os.remove(mci_ole_t)








	def test_mutable_chain_injection_outer_loaded_escalated_name_transmutation(self):

		mci_olen_t = str(self.MAGICAL_ROOT /"mci_olen_t.loggy")
		self.make_loggy_file(mci_olen_t)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_olen_t
					init_name	= "mci_olen_t-1"
					init_level	= 10


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_olen_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_olen_t-1-Stone.Grip ERROR : Cannot grip!",
				"@mci_olen_t-1-Stone.Bound DEBUG : I am bound, but nobody cares",
				"@mci_olen_t-1-Stone INFO : I am root",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_olen_t
					init_name		= "mci_olen_t-2"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_olen_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_olen_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_olen_t-2-Stone.Grip ERROR : Cannot grip!",
				"@mci_olen_t-2-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_olen_t): os.remove(mci_olen_t)








	def test_mutable_chain_injection_outer_loaded_no_loggy_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Mutabor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Mutabor
				class Paint(Transmutable):	pass

		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_double_transmutation(self):

		m_c_i_d_t = str(self.MAGICAL_ROOT /"m_c_i_d_t.loggy")
		self.make_loggy_file(m_c_i_d_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_c_i_d_t
				init_name	= "m_c_i_d_t-1"

			@StoneMutationCase.Antibor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_d_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_d_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_c_i_d_t
				init_name	= "m_c_i_d_t-2"
				init_level	= 10

			@StoneMutationCase.Antigen
			@StoneMutationCase.Antibor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_d_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_d_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_d_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= m_c_i_d_t
				init_name		= "m_c_i_d_t-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_d_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(m_c_i_d_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_d_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@m_c_i_d_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(m_c_i_d_t): os.remove(m_c_i_d_t)








	def test_mutable_chain_injection_double_name_transmutation(self):

		m_c_i_dn_t = str(self.MAGICAL_ROOT /"m_c_i_dn_t.loggy")
		self.make_loggy_file(m_c_i_dn_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_c_i_dn_t
				init_name	= "m_c_i_dn_t-1"

			@StoneMutationCase.Antibor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_dn_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_dn_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_c_i_dn_t
				init_name	= "m_c_i_dn_t-2"
				init_level	= 10

			@StoneMutationCase.Antigen
			@StoneMutationCase.Antibor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_dn_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(m_c_i_dn_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_dn_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= m_c_i_dn_t
				init_name		= "m_c_i_dn_t-3"
				force_handover	= True

			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(m_c_i_dn_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(m_c_i_dn_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_c_i_dn_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@m_c_i_dn_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(m_c_i_dn_t): os.remove(m_c_i_dn_t)








	def test_mutable_chain_injection_double_escalated_transmutation(self):

		m_c_i_de_t = str(self.MAGICAL_ROOT /"m_c_i_de_t.loggy")
		self.make_loggy_file(m_c_i_de_t)

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antibor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= m_c_i_de_t
						init_name		= "m_c_i_de_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_de_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antibor
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= m_c_i_de_t
						init_name		= "m_c_i_de_t-2"


		loggy = []
		self.make_loggy_file(m_c_i_de_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_de_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class loggy(LibraryContrib):

						handler			= m_c_i_de_t
						init_name		= "m_c_i_de_t-3"


		loggy = []
		self.make_loggy_file(m_c_i_de_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_de_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(m_c_i_de_t): os.remove(m_c_i_de_t)








	def test_mutable_chain_injection_double_escalated_name_transmutation(self):

		m_c_i_den_t = str(self.MAGICAL_ROOT /"m_c_i_den_t.loggy")
		self.make_loggy_file(m_c_i_den_t)

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antibor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= m_c_i_den_t
						init_name		= "m_c_i_den_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_den_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antibor
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= m_c_i_den_t
						init_name		= "m_c_i_den_t-2"


		loggy = []
		self.make_loggy_file(m_c_i_den_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_den_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= m_c_i_den_t
						init_name		= "m_c_i_den_t-3"


		loggy = []
		self.make_loggy_file(m_c_i_den_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.test_case.loggy.close()

		with open(m_c_i_den_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(m_c_i_den_t): os.remove(m_c_i_den_t)








	def test_mutable_chain_injection_double_no_loggy_transmutation(self):

		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antibor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antibor
				class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)




		class Stone(Transmutable):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.loggy.warning("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
















	def test_mutable_chain_injection_top_layer_double_transmutation(self):

		mci_tld_t = str(self.MAGICAL_ROOT /"mci_tld_t.loggy")
		self.make_loggy_file(mci_tld_t)


		@StoneMutationCase.Antibor
		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= mci_tld_t
				init_name	= "mci_tld_t-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)

		with open(mci_tld_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneMutationCase.Antigen
		@StoneMutationCase.Antibor
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= mci_tld_t
				init_name	= "mci_tld_t-2"


		loggy = []
		self.make_loggy_file(mci_tld_t)
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)

		with open(mci_tld_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneMutationCase.Antigen
		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= mci_tld_t
				init_name	= "mci_tld_t-3"


		loggy = []
		self.make_loggy_file(mci_tld_t)
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)

		with open(mci_tld_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneMutationCase.Antibor
		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)




		@StoneMutationCase.Antigen
		@StoneMutationCase.Antibor
		class StonePaint(StoneMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)




		@StoneMutationCase.Antigen
		@StoneMutationCase.Antigen
		class StonePaint(StoneMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			StonePaint
		)
		if	os.path.isfile(mci_tld_t): os.remove(mci_tld_t)
















	def test_mutable_chain_injection_outer_double_transmutation(self):

		mci_od_t = str(self.MAGICAL_ROOT /"mci_od_t.loggy")
		self.make_loggy_file(mci_od_t)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_od_t
				init_name	= "mci_od_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Antibor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_od_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_od_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_od_t
				init_name	= "mci_od_t-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			@StoneMutationCase.Antibor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_od_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_od_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_od_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_od_t
				init_name		= "mci_od_t-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_od_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_od_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_od_t-3-Stone.Grip ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_od_t-3-Stone.Grip ERROR : Cannot grip!",
			]
		)
		if	os.path.isfile(mci_od_t): os.remove(mci_od_t)








	def test_mutable_chain_injection_outer_double_name_transmutation(self):

		mci_odn_t = str(self.MAGICAL_ROOT /"mci_odn_t.loggy")
		self.make_loggy_file(mci_odn_t)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_odn_t
				init_name	= "mci_odn_t-1"


		class Stone(Outdoor):

			@StoneMutationCase.Antibor
			@StoneMutationCase.Antigen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_odn_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_odn_t
				init_name	= "mci_odn_t-2"
				init_level	= 10


		class Stone(Outdoor):

			@StoneMutationCase.Antigen
			@StoneMutationCase.Antibor
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_odn_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_odn_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_odn_t
				init_name		= "mci_odn_t-3"
				force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_odn_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.test_case.loggy.close()

		with open(mci_odn_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_odn_t-3-Stone.Grip ERROR : Cannot grip!" ])
		if	os.path.isfile(mci_odn_t): os.remove(mci_odn_t)








	def test_mutable_chain_injection_outer_double_escalated_transmutation(self):

		mci_ode_t = str(self.MAGICAL_ROOT /"mci_ode_t.loggy")
		self.make_loggy_file(mci_ode_t)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ode_t
					init_name	= "mci_ode_t-1"


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antibor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ode_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ode_t-1 ERROR : Cannot grip!",
				"@mci_ode_t-1 INFO : I am root",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_ode_t
					init_name		= "mci_ode_t-2"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antibor
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_ode_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ode_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ode_t-2-Stone.Grip ERROR : Cannot grip!",
				"@mci_ode_t-2-Stone INFO : I am root",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ode_t
					init_name	= "mci_ode_t-3"
					init_level	= 10


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_ode_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ode_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ode_t-3-Stone.Grip ERROR : Cannot grip!",
				"@mci_ode_t-3-Stone.Bound DEBUG : I am bound, but nobody cares",
				"@mci_ode_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_ode_t): os.remove(mci_ode_t)








	def test_mutable_chain_injection_outer_double_escalated_name_transmutation(self):

		mci_oden_t = str(self.MAGICAL_ROOT /"mci_oden_t.loggy")
		self.make_loggy_file(mci_oden_t)

		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_oden_t
					init_name	= "mci_oden_t-1"


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antibor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_oden_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oden_t-1 ERROR : Cannot grip!",
				"@mci_oden_t-1 INFO : I am root",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_oden_t
					init_name		= "mci_oden_t-2"
					force_handover	= True


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antibor
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_oden_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_oden_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oden_t-2-Stone.Grip ERROR : Cannot grip!",
				"@mci_oden_t-2-Stone INFO : I am root",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_oden_t
					init_name	= "mci_oden_t-3"
					init_level	= 10


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_oden_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertIsNone(self.test_case.Grip.loggy.error("Cannot grip!"))
		self.assertIsNone(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_oden_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oden_t-3-Stone.Grip ERROR : Cannot grip!",
				"@mci_oden_t-3-Stone.Bound DEBUG : I am bound, but nobody cares",
				"@mci_oden_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_oden_t): os.remove(mci_oden_t)








	def test_mutable_chain_injection_outer_double_no_loggy_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antibor
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antibor
				class Paint(Transmutable):	pass

		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass


		class Stone(Outdoor):
			class Grip(Transmutable):

				@StoneMutationCase.Antigen
				@StoneMutationCase.Antigen
				class Paint(Transmutable):	pass

		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Grip"))
		self.assertFalse(hasattr(self.test_case.Grip, "Paint"))
		self.assertEqual(self.test_case.Grip.loggy.error("Cannot grip!"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.debug("I am bound, but nobody cares"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)








if __name__ == "__main__" : unittest.main(verbosity=2)







