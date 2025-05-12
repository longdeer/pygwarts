import	os
import	unittest
from	typing												import Callable
from	pygwarts.magical.philosophers_stone					import Transmutable
from	pygwarts.magical.philosophers_stone.transmutations	import Transmutation
from	pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from	pygwarts.magical.spells								import geminio
from	pygwarts.irma.contrib								import LibraryContrib
from	pygwarts.tests.magical								import MagicalTestCase








class StoneControlledMutationCase(MagicalTestCase):

	class Mutagen(ControlledTransmutation):
		def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

			color = self.layer_args[0]
			operation = self.operation

			class Transmute(geminio(mutable_layer)):

				def __call__(self, obj :str) -> str :

					job = super().__call__(obj)
					job = f"{job} {operation} {color}"

					self.loggy.info(job)
					return	job


			return	Transmute




	class KWMutagen(ControlledTransmutation):
		def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

			color = self.layer_args[0]
			operation = self.operation

			class Transmute(geminio(mutable_layer)):

				def __call__(self, obj :str) -> str :

					job = super().__call__(obj)
					job = f"{self.which} {job} {operation} {color}"

					self.loggy.info(job)
					return	job


			return	Transmute




	class Antigen(ControlledTransmutation):
		def whatever_injection(self, mutable_layer :Transmutable) -> Transmutable :

			color = self.layer_args[0]
			operation = self.operation

			class Transmute(geminio(mutable_layer)):

				def __call__(self, obj :str) -> str :

					job = super().__call__(obj)
					job = f"{job} {operation} {color}"

					self.loggy.info(job)
					return	job


			return	Transmute




	class Mutabor(ControlledTransmutation):
		def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

			when = self.layer_args[0]

			class Transmute(geminio(mutable_layer)):

				def __call__(self, obj :str) -> str :

					job = super().__call__(obj)
					job = f"{when} {job}"

					self.loggy.info(job)
					return	job


			return	Transmute




	class KWMutabor(ControlledTransmutation):
		def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

			when = self.layer_args[0]

			class Transmute(geminio(mutable_layer)):

				def __call__(self, obj :str) -> str :

					job = super().__call__(obj)
					job = f"{when} {job}, {self.sure}"

					self.loggy.info(job)
					return	job


			return	Transmute




	class Antibor(ControlledTransmutation):
		def whatever_injection(self, mutable_layer :Transmutable) -> Transmutable :

			when = self.layer_args[0]

			class Transmute(geminio(mutable_layer)):

				def __call__(self, obj :str) -> str :

					job = super().__call__(obj)
					job = f"{when} {job}"

					self.loggy.info(job)
					return	job


			return	Transmute




	class Patogen(Transmutation):
		def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

			class MutatedStone(geminio(mutable_layer)):
				def __call__(self, color :str) -> str :

					mutated_color = f"dark-{color}"
					return	f"{super().__call__(mutated_color)}"

			return	MutatedStone




	class KWPatogen(Transmutation):
		def _mutable_chain_injection(self, mutable_layer :Transmutable) -> Transmutable :

			class MutatedStone(geminio(mutable_layer)):
				def __call__(self, color :str) -> str :

					mutated_color = f"dark-{color} {self.subst}"
					return	f"{super().__call__(mutated_color)}"

			return	MutatedStone




	class Pathogen(Transmutation):
		def whatever_injection(self, mutable_layer :Transmutable) -> Transmutable :

			class MutatedStone(geminio(mutable_layer)):
				def __call__(self, color :str) -> str :

					mutated_color = f"dark-{color}"
					return	f"{super().__call__(mutated_color)}"

			return	MutatedStone




	class PaintBrash(Transmutable):
		def __call__(self, obj :str) -> str :

			job = f"The {obj} will be"
			self.loggy.info(job)
			return job




	class KWPaintBrash(Transmutable):
		def __call__(self, obj :str) -> str :

			job = f"{obj} {self.how} will be"
			self.loggy.info(job)
			return job








	def test_controlled_transmutation(self):

		ctrl_t = str(self.MAGICAL_ROOT /"ctrl_t.loggy")
		self.make_loggy_file(ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ctrl_t
				init_name	= "ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ctrl_t-1 INFO : The stone will be",
				"@ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ctrl_t
				init_name	= "ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ctrl_t-2-Stone.Paint INFO : The stone will be",
				"@ctrl_t-2-Stone.Paint INFO : The stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= ctrl_t
				init_name		= "ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ctrl_t): os.remove(ctrl_t)








	def test_name_controlled_transmutation(self):

		n_ctrl_t = str(self.MAGICAL_ROOT /"n_ctrl_t.loggy")
		self.make_loggy_file(n_ctrl_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= n_ctrl_t
				init_name	= "n_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@n_ctrl_t-1 INFO : The stone will be",
				"@n_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= n_ctrl_t
				init_name	= "n_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@n_ctrl_t-2-Stone.Paint INFO : The stone will be",
				"@n_ctrl_t-2-Stone.Paint INFO : The stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= n_ctrl_t
				init_name		= "n_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(n_ctrl_t): os.remove(n_ctrl_t)








	def test_escalated_controlled_transmutation(self):

		e_ctrl_t = str(self.MAGICAL_ROOT /"e_ctrl_t.loggy")
		self.make_loggy_file(e_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= e_ctrl_t
					init_name	= "e_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_ctrl_t-1 INFO : The stone will be",
				"@e_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= e_ctrl_t
						init_name	= "e_ctrl_t-2"
						init_level	= 10

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_ctrl_t-2-Stone.Handle.Paint INFO : The stone will be",
				"@e_ctrl_t-2-Stone.Handle.Paint INFO : The stone will be turned red",
				"@e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= e_ctrl_t
							init_name		= "e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@e_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@e_ctrl_t-3-Stone INFO : I am root",
				"@e_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(e_ctrl_t): os.remove(e_ctrl_t)








	def test_escalated_name_controlled_transmutation(self):

		e_n_ctrl_t = str(self.MAGICAL_ROOT /"e_n_ctrl_t.loggy")
		self.make_loggy_file(e_n_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= e_n_ctrl_t
					init_name	= "e_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_n_ctrl_t-1 INFO : The stone will be",
				"@e_n_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= e_n_ctrl_t
						init_name	= "e_n_ctrl_t-2"
						init_level	= 10

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_n_ctrl_t-2-Stone.Handle.Paint INFO : The stone will be",
				"@e_n_ctrl_t-2-Stone.Handle.Paint INFO : The stone will be turned red",
				"@e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= e_n_ctrl_t
							init_name		= "e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@e_n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@e_n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@e_n_ctrl_t-3-Stone INFO : I am root",
				"@e_n_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(e_n_ctrl_t): os.remove(e_n_ctrl_t)








	def test_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):
					class Bound(Transmutable):	pass

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_loaded_controlled_transmutation(self):

		load_ctrl_t = str(self.MAGICAL_ROOT /"load_ctrl_t.loggy")
		self.make_loggy_file(load_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= load_ctrl_t
				init_name	= "load_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(load_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_ctrl_t-1 INFO : the stone will be",
				"@load_ctrl_t-1 INFO : the stone will be turned red",
				"@load_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= load_ctrl_t
				init_name	= "load_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(load_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(load_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_ctrl_t-2-Stone.Paint INFO : the stone will be",
				"@load_ctrl_t-2-Stone.Paint INFO : the stone will be turned red",
				"@load_ctrl_t-2-Stone.Paint INFO : Today the stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= load_ctrl_t
				init_name		= "load_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(load_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(load_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@load_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@load_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@load_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@load_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(load_ctrl_t): os.remove(load_ctrl_t)








	def test_loaded_name_controlled_transmutation(self):

		load_n_ctrl_t = str(self.MAGICAL_ROOT /"load_n_ctrl_t.loggy")
		self.make_loggy_file(load_n_ctrl_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= load_n_ctrl_t
				init_name	= "load_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(load_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_n_ctrl_t-1 INFO : the stone will be",
				"@load_n_ctrl_t-1 INFO : the stone will be turned red",
				"@load_n_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= load_n_ctrl_t
				init_name	= "load_n_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(load_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(load_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_n_ctrl_t-2-Stone.Paint INFO : the stone will be",
				"@load_n_ctrl_t-2-Stone.Paint INFO : the stone will be turned red",
				"@load_n_ctrl_t-2-Stone.Paint INFO : Today the stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= load_n_ctrl_t
				init_name		= "load_n_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(load_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(load_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@load_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@load_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@load_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@load_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(load_n_ctrl_t): os.remove(load_n_ctrl_t)








	def test_loaded_escalated_controlled_transmutation(self):

		load_e_ctrl_t = str(self.MAGICAL_ROOT /"load_e_ctrl_t.loggy")
		self.make_loggy_file(load_e_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= load_e_ctrl_t
					init_name	= "load_e_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(load_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_e_ctrl_t-1 INFO : the stone will be",
				"@load_e_ctrl_t-1 INFO : the stone will be turned red",
				"@load_e_ctrl_t-1 INFO : Today the stone will be turned red",
				"@load_e_ctrl_t-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= load_e_ctrl_t
						init_name	= "load_e_ctrl_t-2"
						init_level	= 10

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(load_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(load_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_e_ctrl_t-2-Stone.Handle.Paint INFO : the stone will be",
				"@load_e_ctrl_t-2-Stone.Handle.Paint INFO : the stone will be turned red",
				"@load_e_ctrl_t-2-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@load_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@load_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= load_e_ctrl_t
							init_name		= "load_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(load_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(load_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_e_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@load_e_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@load_e_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@load_e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@load_e_ctrl_t-3-Stone INFO : I am root",
				"@load_e_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(load_e_ctrl_t): os.remove(load_e_ctrl_t)








	def test_loaded_escalated_name_controlled_transmutation(self):

		load_e_n_ctrl_t = str(self.MAGICAL_ROOT /"load_e_n_ctrl_t.loggy")
		self.make_loggy_file(load_e_n_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= load_e_n_ctrl_t
					init_name	= "load_e_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(load_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_e_n_ctrl_t-1 INFO : the stone will be",
				"@load_e_n_ctrl_t-1 INFO : the stone will be turned red",
				"@load_e_n_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= load_e_n_ctrl_t
						init_name	= "load_e_n_ctrl_t-2"
						init_level	= 10

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(load_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(load_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_e_n_ctrl_t-2-Stone.Handle.Paint INFO : the stone will be",
				"@load_e_n_ctrl_t-2-Stone.Handle.Paint INFO : the stone will be turned red",
				"@load_e_n_ctrl_t-2-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@load_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@load_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= load_e_n_ctrl_t
							init_name		= "load_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(load_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(load_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@load_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@load_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@load_e_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@load_e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@load_e_n_ctrl_t-3-Stone INFO : I am root",
				"@load_e_n_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(load_e_n_ctrl_t): os.remove(load_e_n_ctrl_t)








	def test_loaded_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):
					class Bound(Transmutable):	pass

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_mixed_controlled_transmutation(self):

		mix_ctrl_t = str(self.MAGICAL_ROOT /"mix_ctrl_t.loggy")
		self.make_loggy_file(mix_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mix_ctrl_t
				init_name	= "mix_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(mix_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_ctrl_t-1 INFO : the dark-stone will be",
				"@mix_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@mix_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mix_ctrl_t
				init_name	= "mix_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(mix_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(mix_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@mix_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@mix_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mix_ctrl_t
				init_name		= "mix_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(mix_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mix_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@mix_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@mix_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@mix_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mix_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mix_ctrl_t): os.remove(mix_ctrl_t)








	def test_mixed_name_controlled_transmutation(self):

		mix_n_ctrl_t = str(self.MAGICAL_ROOT /"mix_n_ctrl_t.loggy")
		self.make_loggy_file(mix_n_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mix_n_ctrl_t
				init_name	= "mix_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(mix_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_n_ctrl_t-1 INFO : the dark-stone will be",
				"@mix_n_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@mix_n_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mix_n_ctrl_t
				init_name	= "mix_n_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(mix_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(mix_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@mix_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@mix_n_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mix_n_ctrl_t
				init_name		= "mix_n_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(mix_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mix_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@mix_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@mix_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@mix_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mix_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mix_n_ctrl_t): os.remove(mix_n_ctrl_t)








	def test_mixed_escalated_controlled_transmutation(self):

		mix_e_ctrl_t = str(self.MAGICAL_ROOT /"mix_e_ctrl_t.loggy")
		self.make_loggy_file(mix_e_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mix_e_ctrl_t
					init_name	= "mix_e_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(mix_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_e_ctrl_t-1 INFO : the dark-stone will be",
				"@mix_e_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@mix_e_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mix_e_ctrl_t
						init_name	= "mix_e_ctrl_t-2"
						init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(mix_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mix_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_e_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@mix_e_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@mix_e_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
				"@mix_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@mix_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= mix_e_ctrl_t
							init_name		= "mix_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(mix_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))

		self.test_case.loggy.close()

		with open(mix_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_e_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@mix_e_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@mix_e_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@mix_e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mix_e_ctrl_t-3-Stone INFO : I am root",
				"@mix_e_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mix_e_ctrl_t): os.remove(mix_e_ctrl_t)








	def test_mixed_escalated_name_controlled_transmutation(self):

		mix_e_n_ctrl_t = str(self.MAGICAL_ROOT /"mix_e_n_ctrl_t.loggy")
		self.make_loggy_file(mix_e_n_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mix_e_n_ctrl_t
					init_name	= "mix_e_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(mix_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_e_n_ctrl_t-1 INFO : the dark-stone will be",
				"@mix_e_n_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@mix_e_n_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mix_e_n_ctrl_t
						init_name	= "mix_e_n_ctrl_t-2"
						init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(mix_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mix_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_e_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@mix_e_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@mix_e_n_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
				"@mix_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@mix_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= mix_e_n_ctrl_t
							init_name		= "mix_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(mix_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))

		self.test_case.loggy.close()

		with open(mix_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mix_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@mix_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@mix_e_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@mix_e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mix_e_n_ctrl_t-3-Stone INFO : I am root",
				"@mix_e_n_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mix_e_n_ctrl_t): os.remove(mix_e_n_ctrl_t)








	def test_mixed_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Handle(Transmutable):	pass

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):	pass

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):	pass
					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_top_layer_controlled_transmutation(self):

		top_ctrl_t = str(self.MAGICAL_ROOT /"top_ctrl_t.loggy")
		self.make_loggy_file(top_ctrl_t)


		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= top_ctrl_t
				init_name	= "top_ctrl_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(top_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_ctrl_t-1 INFO : The stone will be",
				"@top_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= top_ctrl_t
				init_name	= "top_ctrl_t-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(top_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(top_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_ctrl_t-2-Stone INFO : The stone will be",
				"@top_ctrl_t-2-Stone INFO : The stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler			= top_ctrl_t
				init_name		= "top_ctrl_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(top_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(top_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_ctrl_t-3-Stone INFO : The stone will be",
				"@top_ctrl_t-3-Stone INFO : The stone will be turned red",
				"@top_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(top_ctrl_t): os.remove(top_ctrl_t)








	def test_top_layer_name_controlled_transmutation(self):

		top_n_ctrl_t = str(self.MAGICAL_ROOT /"top_n_ctrl_t.loggy")
		self.make_loggy_file(top_n_ctrl_t)


		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class shmoggy(LibraryContrib):

				handler		= top_n_ctrl_t
				init_name	= "top_n_ctrl_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(top_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_n_ctrl_t-1 INFO : The stone will be",
				"@top_n_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class shmoggy(LibraryContrib):

				handler		= top_n_ctrl_t
				init_name	= "top_n_ctrl_t-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(top_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(top_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_n_ctrl_t-2-Stone INFO : The stone will be",
				"@top_n_ctrl_t-2-Stone INFO : The stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class shmoggy(LibraryContrib):

				handler			= top_n_ctrl_t
				init_name		= "top_n_ctrl_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(top_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(top_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_n_ctrl_t-3-Stone INFO : The stone will be",
				"@top_n_ctrl_t-3-Stone INFO : The stone will be turned red",
				"@top_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(top_n_ctrl_t): os.remove(top_n_ctrl_t)








	def test_top_layer_escalated_controlled_transmutation(self):

		top_e_ctrl_t = str(self.MAGICAL_ROOT /"top_e_ctrl_t.loggy")
		self.make_loggy_file(top_e_ctrl_t)


		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= top_e_ctrl_t
					init_name	= "top_e_ctrl_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(top_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_e_ctrl_t-1 INFO : The stone will be",
				"@top_e_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= top_e_ctrl_t
					init_name	= "top_e_ctrl_t-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(top_e_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(top_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_e_ctrl_t-2-Stone INFO : The stone will be",
				"@top_e_ctrl_t-2-Stone INFO : The stone will be turned red",
				"@top_e_ctrl_t-2-Stone.Bound INFO : I am bound",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler			= top_e_ctrl_t
						init_name		= "top_e_ctrl_t-3"
						force_handover	= True


		loggy = []
		self.make_loggy_file(top_e_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(top_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_e_ctrl_t-3-Stone INFO : The stone will be",
				"@top_e_ctrl_t-3-Stone INFO : The stone will be turned red",
				"@top_e_ctrl_t-3-Stone INFO : I am root",
				"@top_e_ctrl_t-3-Stone.Handle WARNING : I am just a handle",
				"@top_e_ctrl_t-3-Stone.Handle.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(top_e_ctrl_t): os.remove(top_e_ctrl_t)








	def test_top_layer_escalated_name_controlled_transmutation(self):

		top_e_n_ctrl_t = str(self.MAGICAL_ROOT /"top_e_n_ctrl_t.loggy")
		self.make_loggy_file(top_e_n_ctrl_t)


		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= top_e_n_ctrl_t
					init_name	= "top_e_n_ctrl_t-1"


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(top_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_e_n_ctrl_t-1 INFO : The stone will be",
				"@top_e_n_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= top_e_n_ctrl_t
					init_name	= "top_e_n_ctrl_t-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(top_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(top_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_e_n_ctrl_t-2-Stone INFO : The stone will be",
				"@top_e_n_ctrl_t-2-Stone INFO : The stone will be turned red",
				"@top_e_n_ctrl_t-2-Stone.Bound INFO : I am bound",
			]
		)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= top_e_n_ctrl_t
						init_name		= "top_e_n_ctrl_t-3"
						force_handover	= True


		loggy = []
		self.make_loggy_file(top_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(top_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@top_e_n_ctrl_t-3-Stone INFO : The stone will be",
				"@top_e_n_ctrl_t-3-Stone INFO : The stone will be turned red",
				"@top_e_n_ctrl_t-3-Stone INFO : I am root",
				"@top_e_n_ctrl_t-3-Stone.Handle WARNING : I am just a handle",
				"@top_e_n_ctrl_t-3-Stone.Handle.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(top_e_n_ctrl_t): os.remove(top_e_n_ctrl_t)








	def test_top_layer_no_loggy_controlled_transmutation(self):

		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "The stone will be turned red")
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_top_layer_loaded_controlled_transmutation(self):

		tl_l_ctrl_t = str(self.MAGICAL_ROOT /"tl_l_ctrl_t.loggy")
		self.make_loggy_file(tl_l_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= tl_l_ctrl_t
				init_name	= "tl_l_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_l_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_ctrl_t-1 INFO : the stone will be",
				"@tl_l_ctrl_t-1 INFO : the stone will be turned red",
				"@tl_l_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= tl_l_ctrl_t
				init_name	= "tl_l_ctrl_t-2"
				init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_l_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_ctrl_t-2-Stone INFO : the stone will be",
				"@tl_l_ctrl_t-2-Stone INFO : the stone will be turned red",
				"@tl_l_ctrl_t-2-Stone INFO : Today the stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler			= tl_l_ctrl_t
				init_name		= "tl_l_ctrl_t-3"
				force_handover	= True

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(tl_l_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_ctrl_t-3-Stone INFO : the stone will be",
				"@tl_l_ctrl_t-3-Stone INFO : the stone will be turned red",
				"@tl_l_ctrl_t-3-Stone INFO : Today the stone will be turned red",
				"@tl_l_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(tl_l_ctrl_t): os.remove(tl_l_ctrl_t)








	def test_top_layer_loaded_name_controlled_transmutation(self):

		tl_l_n_ctrl_t = str(self.MAGICAL_ROOT /"tl_l_n_ctrl_t.loggy")
		self.make_loggy_file(tl_l_n_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class shmoggy(LibraryContrib):

				handler		= tl_l_n_ctrl_t
				init_name	= "tl_l_n_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_l_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_n_ctrl_t-1 INFO : the stone will be",
				"@tl_l_n_ctrl_t-1 INFO : the stone will be turned red",
				"@tl_l_n_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= tl_l_n_ctrl_t
				init_name	= "tl_l_n_ctrl_t-2"
				init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_l_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_n_ctrl_t-2-Stone INFO : the stone will be",
				"@tl_l_n_ctrl_t-2-Stone INFO : the stone will be turned red",
				"@tl_l_n_ctrl_t-2-Stone INFO : Today the stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler			= tl_l_n_ctrl_t
				init_name		= "tl_l_n_ctrl_t-3"
				force_handover	= True

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(tl_l_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_n_ctrl_t-3-Stone INFO : the stone will be",
				"@tl_l_n_ctrl_t-3-Stone INFO : the stone will be turned red",
				"@tl_l_n_ctrl_t-3-Stone INFO : Today the stone will be turned red",
				"@tl_l_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(tl_l_n_ctrl_t): os.remove(tl_l_n_ctrl_t)








	def test_top_layer_loaded_escalated_controlled_transmutation(self):

		tl_l_e_ctrl_t = str(self.MAGICAL_ROOT /"tl_l_e_ctrl_t.loggy")
		self.make_loggy_file(tl_l_e_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= tl_l_e_ctrl_t
					init_name	= "tl_l_e_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_l_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_e_ctrl_t-1 INFO : the stone will be",
				"@tl_l_e_ctrl_t-1 INFO : the stone will be turned red",
				"@tl_l_e_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= tl_l_e_ctrl_t
					init_name	= "tl_l_e_ctrl_t-2"
					init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_e_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_l_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_e_ctrl_t-2-Stone INFO : the stone will be",
				"@tl_l_e_ctrl_t-2-Stone INFO : the stone will be turned red",
				"@tl_l_e_ctrl_t-2-Stone INFO : Today the stone will be turned red",
				"@tl_l_e_ctrl_t-2-Stone.Bound INFO : I am bound",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler			= tl_l_e_ctrl_t
						init_name		= "tl_l_e_ctrl_t-3"
						force_handover	= True

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_e_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_l_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_e_ctrl_t-3-Stone INFO : the stone will be",
				"@tl_l_e_ctrl_t-3-Stone INFO : the stone will be turned red",
				"@tl_l_e_ctrl_t-3-Stone INFO : Today the stone will be turned red",
				"@tl_l_e_ctrl_t-3-Stone INFO : I am root",
				"@tl_l_e_ctrl_t-3-Stone.Handle WARNING : I am just a handle",
				"@tl_l_e_ctrl_t-3-Stone.Handle.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(tl_l_e_ctrl_t): os.remove(tl_l_e_ctrl_t)








	def test_top_layer_loaded_escalated_name_controlled_transmutation(self):

		tl_l_e_n_ctrl_t = str(self.MAGICAL_ROOT /"tl_l_e_n_ctrl_t.loggy")
		self.make_loggy_file(tl_l_e_n_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= tl_l_e_n_ctrl_t
					init_name	= "tl_l_e_n_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_l_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_e_n_ctrl_t-1 INFO : the stone will be",
				"@tl_l_e_n_ctrl_t-1 INFO : the stone will be turned red",
				"@tl_l_e_n_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= tl_l_e_n_ctrl_t
					init_name	= "tl_l_e_n_ctrl_t-2"
					init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_l_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_e_n_ctrl_t-2-Stone INFO : the stone will be",
				"@tl_l_e_n_ctrl_t-2-Stone INFO : the stone will be turned red",
				"@tl_l_e_n_ctrl_t-2-Stone INFO : Today the stone will be turned red",
				"@tl_l_e_n_ctrl_t-2-Stone.Bound INFO : I am bound",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= tl_l_e_n_ctrl_t
						init_name		= "tl_l_e_n_ctrl_t-3"
						force_handover	= True

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_l_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_l_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_l_e_n_ctrl_t-3-Stone INFO : the stone will be",
				"@tl_l_e_n_ctrl_t-3-Stone INFO : the stone will be turned red",
				"@tl_l_e_n_ctrl_t-3-Stone INFO : Today the stone will be turned red",
				"@tl_l_e_n_ctrl_t-3-Stone INFO : I am root",
				"@tl_l_e_n_ctrl_t-3-Stone.Handle WARNING : I am just a handle",
				"@tl_l_e_n_ctrl_t-3-Stone.Handle.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(tl_l_e_n_ctrl_t): os.remove(tl_l_e_n_ctrl_t)








	def test_top_layer_loaded_no_loggy_controlled_transmutation(self):

		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today The stone will be turned red")
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today The stone will be turned red")
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_top_layer_mixed_controlled_transmutation(self):

		tl_m_ctrl_t = str(self.MAGICAL_ROOT /"tl_m_ctrl_t.loggy")
		self.make_loggy_file(tl_m_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone(StoneControlledMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= tl_m_ctrl_t
				init_name	= "tl_m_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_m_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_ctrl_t-1 INFO : the dark-stone will be",
				"@tl_m_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@tl_m_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler		= tl_m_ctrl_t
				init_name	= "tl_m_ctrl_t-2"
				init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_m_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_m_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_ctrl_t-2-Stone INFO : the dark-stone will be",
				"@tl_m_ctrl_t-2-Stone INFO : the dark-stone will be turned red",
				"@tl_m_ctrl_t-2-Stone INFO : Today the dark-stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):	pass
			class loggy(LibraryContrib):

				handler			= tl_m_ctrl_t
				init_name		= "tl_m_ctrl_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(tl_m_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertEqual(self.test_case("stone"), "Today The dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(tl_m_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_ctrl_t-3-Stone INFO : The dark-stone will be",
				"@tl_m_ctrl_t-3-Stone INFO : The dark-stone will be turned red",
				"@tl_m_ctrl_t-3-Stone INFO : Today The dark-stone will be turned red",
				"@tl_m_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@tl_m_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(tl_m_ctrl_t): os.remove(tl_m_ctrl_t)








	def test_top_layer_mixed_name_controlled_transmutation(self):

		tl_m_n_ctrl_t = str(self.MAGICAL_ROOT /"tl_m_n_ctrl_t.loggy")
		self.make_loggy_file(tl_m_n_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone(StoneControlledMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= tl_m_n_ctrl_t
				init_name	= "tl_m_n_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_m_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_n_ctrl_t-1 INFO : the dark-stone will be",
				"@tl_m_n_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@tl_m_n_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler		= tl_m_n_ctrl_t
				init_name	= "tl_m_n_ctrl_t-2"
				init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_m_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_m_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_n_ctrl_t-2-Stone INFO : the dark-stone will be",
				"@tl_m_n_ctrl_t-2-Stone INFO : the dark-stone will be turned red",
				"@tl_m_n_ctrl_t-2-Stone INFO : Today the dark-stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):	pass
			class shmoggy(LibraryContrib):

				handler			= tl_m_n_ctrl_t
				init_name		= "tl_m_n_ctrl_t-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(tl_m_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertEqual(self.test_case("stone"), "Today The dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(tl_m_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_n_ctrl_t-3-Stone INFO : The dark-stone will be",
				"@tl_m_n_ctrl_t-3-Stone INFO : The dark-stone will be turned red",
				"@tl_m_n_ctrl_t-3-Stone INFO : Today The dark-stone will be turned red",
				"@tl_m_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@tl_m_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(tl_m_n_ctrl_t): os.remove(tl_m_n_ctrl_t)








	def test_top_layer_mixed_escalated_controlled_transmutation(self):

		tl_m_e_ctrl_t = str(self.MAGICAL_ROOT /"tl_m_e_ctrl_t.loggy")
		self.make_loggy_file(tl_m_e_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= tl_m_e_ctrl_t
					init_name	= "tl_m_e_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_m_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_e_ctrl_t-1 INFO : the dark-stone will be",
				"@tl_m_e_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@tl_m_e_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= tl_m_e_ctrl_t
					init_name	= "tl_m_e_ctrl_t-2"
					init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_m_e_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_m_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_e_ctrl_t-2-Stone INFO : the dark-stone will be",
				"@tl_m_e_ctrl_t-2-Stone INFO : the dark-stone will be turned red",
				"@tl_m_e_ctrl_t-2-Stone INFO : Today the dark-stone will be turned red",
				"@tl_m_e_ctrl_t-2-Stone.Bound INFO : I am bound",
			]
		)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler			= tl_m_e_ctrl_t
						init_name		= "tl_m_e_ctrl_t-3"
						force_handover	= True


		loggy = []
		self.make_loggy_file(tl_m_e_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today The dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_m_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_e_ctrl_t-3-Stone INFO : The dark-stone will be",
				"@tl_m_e_ctrl_t-3-Stone INFO : The dark-stone will be turned red",
				"@tl_m_e_ctrl_t-3-Stone INFO : Today The dark-stone will be turned red",
				"@tl_m_e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@tl_m_e_ctrl_t-3-Stone INFO : I am root",
				"@tl_m_e_ctrl_t-3-Stone.Handle.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(tl_m_e_ctrl_t): os.remove(tl_m_e_ctrl_t)








	def test_top_layer_mixed_escalated_name_controlled_transmutation(self):

		tl_m_e_n_ctrl_t = str(self.MAGICAL_ROOT /"tl_m_e_n_ctrl_t.loggy")
		self.make_loggy_file(tl_m_e_n_ctrl_t)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= tl_m_e_n_ctrl_t
					init_name	= "tl_m_e_n_ctrl_t-1"

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(tl_m_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_e_n_ctrl_t-1 INFO : the dark-stone will be",
				"@tl_m_e_n_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@tl_m_e_n_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= tl_m_e_n_ctrl_t
					init_name	= "tl_m_e_n_ctrl_t-2"
					init_level	= 10

			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(tl_m_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_m_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_e_n_ctrl_t-2-Stone INFO : the dark-stone will be",
				"@tl_m_e_n_ctrl_t-2-Stone INFO : the dark-stone will be turned red",
				"@tl_m_e_n_ctrl_t-2-Stone INFO : Today the dark-stone will be turned red",
				"@tl_m_e_n_ctrl_t-2-Stone.Bound INFO : I am bound",
			]
		)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= tl_m_e_n_ctrl_t
						init_name		= "tl_m_e_n_ctrl_t-3"
						force_handover	= True


		loggy = []
		self.make_loggy_file(tl_m_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today The dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(tl_m_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@tl_m_e_n_ctrl_t-3-Stone INFO : The dark-stone will be",
				"@tl_m_e_n_ctrl_t-3-Stone INFO : The dark-stone will be turned red",
				"@tl_m_e_n_ctrl_t-3-Stone INFO : Today The dark-stone will be turned red",
				"@tl_m_e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@tl_m_e_n_ctrl_t-3-Stone INFO : I am root",
				"@tl_m_e_n_ctrl_t-3-Stone.Handle.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(tl_m_e_n_ctrl_t): os.remove(tl_m_e_n_ctrl_t)








	def test_top_layer_mixed_no_loggy_controlled_transmutation(self):

		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Bound(Transmutable):	pass
			def __call__(self, obj :str) -> str :

				job = f"the {obj} will be"
				self.loggy.info(job)
				return job


		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class Handle(Transmutable):
				class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today The dark-stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_outer_controlled_transmutation(self):

		out_ctrl_t = str(self.MAGICAL_ROOT /"out_ctrl_t.loggy")
		self.make_loggy_file(out_ctrl_t)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= out_ctrl_t
				init_name	= "out_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(out_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_ctrl_t-1 INFO : The stone will be",
				"@out_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= out_ctrl_t
				init_name	= "out_ctrl_t-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(out_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_ctrl_t-2-Stone.Paint INFO : The stone will be",
				"@out_ctrl_t-2-Stone.Paint INFO : The stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= out_ctrl_t
				init_name		= "out_ctrl_t-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(out_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@out_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@out_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@out_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(out_ctrl_t): os.remove(out_ctrl_t)








	def test_outer_name_controlled_transmutation(self):

		out_n_ctrl_t = str(self.MAGICAL_ROOT /"out_n_ctrl_t.loggy")
		self.make_loggy_file(out_n_ctrl_t)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= out_n_ctrl_t
				init_name	= "out_n_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(out_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_ctrl_t-1 INFO : The stone will be",
				"@out_n_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= out_n_ctrl_t
				init_name	= "out_n_ctrl_t-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(out_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_ctrl_t-2-Stone.Paint INFO : The stone will be",
				"@out_n_ctrl_t-2-Stone.Paint INFO : The stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= out_n_ctrl_t
				init_name		= "out_n_ctrl_t-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(out_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@out_n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@out_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@out_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(out_n_ctrl_t): os.remove(out_n_ctrl_t)








	def test_outer_escalated_controlled_transmutation(self):

		out_e_ctrl_t = str(self.MAGICAL_ROOT /"out_e_ctrl_t.loggy")
		self.make_loggy_file(out_e_ctrl_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= out_e_ctrl_t
					init_name	= "out_e_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(out_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_ctrl_t-1 INFO : The stone will be",
				"@out_e_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= out_e_ctrl_t
						init_name	= "out_e_ctrl_t-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(out_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_ctrl_t-2-Stone.Paint INFO : The stone will be",
				"@out_e_ctrl_t-2-Stone.Paint INFO : The stone will be turned red",
				"@out_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@out_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= out_e_ctrl_t
					init_name		= "out_e_ctrl_t-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(out_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@out_e_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@out_e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@out_e_ctrl_t-3-Stone INFO : I am root",
				"@out_e_ctrl_t-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(out_e_ctrl_t): os.remove(out_e_ctrl_t)








	def test_outer_escalated_name_controlled_transmutation(self):

		out_e_n_ctrl_t = str(self.MAGICAL_ROOT /"out_e_n_ctrl_t.loggy")
		self.make_loggy_file(out_e_n_ctrl_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= out_e_n_ctrl_t
					init_name	= "out_e_n_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.test_case.loggy.close()

		with open(out_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_ctrl_t-1 INFO : The stone will be",
				"@out_e_n_ctrl_t-1 INFO : The stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= out_e_n_ctrl_t
						init_name	= "out_e_n_ctrl_t-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(out_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_ctrl_t-2-Stone.Paint INFO : The stone will be",
				"@out_e_n_ctrl_t-2-Stone.Paint INFO : The stone will be turned red",
				"@out_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@out_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= out_e_n_ctrl_t
					init_name		= "out_e_n_ctrl_t-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(out_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(out_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@out_e_n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be",
				"@out_e_n_ctrl_t-3-Stone.Handle.Paint INFO : The stone will be turned red",
				"@out_e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@out_e_n_ctrl_t-3-Stone INFO : I am root",
				"@out_e_n_ctrl_t-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(out_e_n_ctrl_t): os.remove(out_e_n_ctrl_t)








	def test_outer_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "The stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "The stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_outer_loaded_controlled_transmutation(self):

		l_o_ctrl_t = str(self.MAGICAL_ROOT /"l_o_ctrl_t.loggy")
		self.make_loggy_file(l_o_ctrl_t)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= l_o_ctrl_t
				init_name	= "l_o_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(l_o_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_ctrl_t-1 INFO : the stone will be",
				"@l_o_ctrl_t-1 INFO : the stone will be turned red",
				"@l_o_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= l_o_ctrl_t
				init_name	= "l_o_ctrl_t-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(l_o_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(l_o_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_ctrl_t-2-Stone.Paint INFO : the stone will be",
				"@l_o_ctrl_t-2-Stone.Paint INFO : the stone will be turned red",
				"@l_o_ctrl_t-2-Stone.Paint INFO : Today the stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= l_o_ctrl_t
				init_name		= "l_o_ctrl_t-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(l_o_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(l_o_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@l_o_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@l_o_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@l_o_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@l_o_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(l_o_ctrl_t): os.remove(l_o_ctrl_t)








	def test_outer_loaded_name_controlled_transmutation(self):

		l_o_n_ctrl_t = str(self.MAGICAL_ROOT /"l_o_n_ctrl_t.loggy")
		self.make_loggy_file(l_o_n_ctrl_t)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= l_o_n_ctrl_t
				init_name	= "l_o_n_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(l_o_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_n_ctrl_t-1 INFO : the stone will be",
				"@l_o_n_ctrl_t-1 INFO : the stone will be turned red",
				"@l_o_n_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= l_o_n_ctrl_t
				init_name	= "l_o_n_ctrl_t-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(l_o_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(l_o_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_n_ctrl_t-2-Stone.Paint INFO : the stone will be",
				"@l_o_n_ctrl_t-2-Stone.Paint INFO : the stone will be turned red",
				"@l_o_n_ctrl_t-2-Stone.Paint INFO : Today the stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= l_o_n_ctrl_t
				init_name		= "l_o_n_ctrl_t-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(l_o_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(l_o_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@l_o_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@l_o_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@l_o_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@l_o_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(l_o_n_ctrl_t): os.remove(l_o_n_ctrl_t)








	def test_outer_loaded_escalated_controlled_transmutation(self):

		l_o_e_ctrl_t = str(self.MAGICAL_ROOT /"l_o_e_ctrl_t.loggy")
		self.make_loggy_file(l_o_e_ctrl_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= l_o_e_ctrl_t
					init_name	= "l_o_e_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(l_o_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_e_ctrl_t-1 INFO : the stone will be",
				"@l_o_e_ctrl_t-1 INFO : the stone will be turned red",
				"@l_o_e_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= l_o_e_ctrl_t
						init_name	= "l_o_e_ctrl_t-2"
						init_level	= 10

		class Stone(Outdoor):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(l_o_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(l_o_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_e_ctrl_t-2-Stone.Paint INFO : the stone will be",
				"@l_o_e_ctrl_t-2-Stone.Paint INFO : the stone will be turned red",
				"@l_o_e_ctrl_t-2-Stone.Paint INFO : Today the stone will be turned red",
				"@l_o_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@l_o_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= l_o_e_ctrl_t
							init_name		= "l_o_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(l_o_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(l_o_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_e_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@l_o_e_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@l_o_e_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@l_o_e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@l_o_e_ctrl_t-3-Stone INFO : I am root",
				"@l_o_e_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(l_o_e_ctrl_t): os.remove(l_o_e_ctrl_t)








	def test_outer_loaded_escalated_name_controlled_transmutation(self):

		l_o_e_n_ctrl_t = str(self.MAGICAL_ROOT /"l_o_e_n_ctrl_t.loggy")
		self.make_loggy_file(l_o_e_n_ctrl_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= l_o_e_n_ctrl_t
					init_name	= "l_o_e_n_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.test_case.loggy.close()

		with open(l_o_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_e_n_ctrl_t-1 INFO : the stone will be",
				"@l_o_e_n_ctrl_t-1 INFO : the stone will be turned red",
				"@l_o_e_n_ctrl_t-1 INFO : Today the stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= l_o_e_n_ctrl_t
						init_name	= "l_o_e_n_ctrl_t-2"
						init_level	= 10

		class Stone(Outdoor):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(l_o_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(l_o_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_e_n_ctrl_t-2-Stone.Paint INFO : the stone will be",
				"@l_o_e_n_ctrl_t-2-Stone.Paint INFO : the stone will be turned red",
				"@l_o_e_n_ctrl_t-2-Stone.Paint INFO : Today the stone will be turned red",
				"@l_o_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@l_o_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= l_o_e_n_ctrl_t
							init_name		= "l_o_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(l_o_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(l_o_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@l_o_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be",
				"@l_o_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the stone will be turned red",
				"@l_o_e_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the stone will be turned red",
				"@l_o_e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@l_o_e_n_ctrl_t-3-Stone INFO : I am root",
				"@l_o_e_n_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(l_o_e_n_ctrl_t): os.remove(l_o_e_n_ctrl_t)








	def test_outer_loaded_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

		class Stone(Outdoor):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):	pass
					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_outer_mixed_controlled_transmutation(self):

		m_o_ctrl_t = str(self.MAGICAL_ROOT /"m_o_ctrl_t.loggy")
		self.make_loggy_file(m_o_ctrl_t)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_o_ctrl_t
				init_name	= "m_o_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(m_o_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_ctrl_t-1 INFO : the dark-stone will be",
				"@m_o_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@m_o_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= m_o_ctrl_t
				init_name	= "m_o_ctrl_t-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(m_o_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(m_o_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@m_o_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@m_o_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= m_o_ctrl_t
				init_name		= "m_o_ctrl_t-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(m_o_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(m_o_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@m_o_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@m_o_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@m_o_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@m_o_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(m_o_ctrl_t): os.remove(m_o_ctrl_t)








	def test_outer_mixed_name_controlled_transmutation(self):

		m_o_n_ctrl_t = str(self.MAGICAL_ROOT /"m_o_n_ctrl_t.loggy")
		self.make_loggy_file(m_o_n_ctrl_t)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_o_n_ctrl_t
				init_name	= "m_o_n_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(m_o_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_n_ctrl_t-1 INFO : the dark-stone will be",
				"@m_o_n_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@m_o_n_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= m_o_n_ctrl_t
				init_name	= "m_o_n_ctrl_t-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(m_o_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(m_o_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@m_o_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@m_o_n_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= m_o_n_ctrl_t
				init_name		= "m_o_n_ctrl_t-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(m_o_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(m_o_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@m_o_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@m_o_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@m_o_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@m_o_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(m_o_n_ctrl_t): os.remove(m_o_n_ctrl_t)








	def test_outer_mixed_escalated_controlled_transmutation(self):

		m_o_e_ctrl_t = str(self.MAGICAL_ROOT /"m_o_e_ctrl_t.loggy")
		self.make_loggy_file(m_o_e_ctrl_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= m_o_e_ctrl_t
					init_name	= "m_o_e_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(m_o_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_e_ctrl_t-1 INFO : the dark-stone will be",
				"@m_o_e_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@m_o_e_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= m_o_e_ctrl_t
						init_name	= "m_o_e_ctrl_t-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(m_o_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(m_o_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_e_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@m_o_e_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@m_o_e_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
				"@m_o_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@m_o_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= m_o_e_ctrl_t
							init_name		= "m_o_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(m_o_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))

		self.test_case.loggy.close()

		with open(m_o_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_e_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@m_o_e_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@m_o_e_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@m_o_e_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@m_o_e_ctrl_t-3-Stone INFO : I am root",
				"@m_o_e_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(m_o_e_ctrl_t): os.remove(m_o_e_ctrl_t)








	def test_outer_mixed_escalated_name_controlled_transmutation(self):

		m_o_e_n_ctrl_t = str(self.MAGICAL_ROOT /"m_o_e_n_ctrl_t.loggy")
		self.make_loggy_file(m_o_e_n_ctrl_t)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= m_o_e_n_ctrl_t
					init_name	= "m_o_e_n_ctrl_t-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.test_case.loggy.close()

		with open(m_o_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_e_n_ctrl_t-1 INFO : the dark-stone will be",
				"@m_o_e_n_ctrl_t-1 INFO : the dark-stone will be turned red",
				"@m_o_e_n_ctrl_t-1 INFO : Today the dark-stone will be turned red",
			]
		)




		class Outdoor(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= m_o_e_n_ctrl_t
						init_name	= "m_o_e_n_ctrl_t-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(m_o_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(m_o_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_e_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be",
				"@m_o_e_n_ctrl_t-2-Stone.Paint INFO : the dark-stone will be turned red",
				"@m_o_e_n_ctrl_t-2-Stone.Paint INFO : Today the dark-stone will be turned red",
				"@m_o_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@m_o_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= m_o_e_n_ctrl_t
							init_name		= "m_o_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(m_o_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"))

		self.test_case.loggy.close()

		with open(m_o_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@m_o_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be",
				"@m_o_e_n_ctrl_t-3-Stone.Handle.Paint INFO : the dark-stone will be turned red",
				"@m_o_e_n_ctrl_t-3-Stone.Handle.Paint INFO : Today the dark-stone will be turned red",
				"@m_o_e_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@m_o_e_n_ctrl_t-3-Stone INFO : I am root",
				"@m_o_e_n_ctrl_t-3-Stone.Handle.Paint.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(m_o_e_n_ctrl_t): os.remove(m_o_e_n_ctrl_t)








	def test_outer_mixed_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):
			class Bound(Transmutable):	pass

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Paint"))
		self.assertIsInstance(self.test_case.Paint, Transmutable)
		self.assertEqual(self.test_case.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):	pass
					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsInstance(self.test_case.Handle.Paint, Transmutable)
		self.assertTrue(hasattr(self.test_case.Handle.Paint, "Bound"))
		self.assertEqual(self.test_case.Handle.Paint("stone"), "Today the dark-stone will be turned red")
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Paint.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_other_controlled_transmutation(self):

		ot_ctrl_t = str(self.MAGICAL_ROOT /"ot_ctrl_t.loggy")
		self.make_loggy_file(ot_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_ctrl_t
				init_name	= "ot_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,[ "@ot_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation" ]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_ctrl_t
				init_name	= "ot_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_ctrl_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= ot_ctrl_t
				init_name		= "ot_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ot_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_ctrl_t-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ot_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ot_ctrl_t): os.remove(ot_ctrl_t)








	def test_other_name_controlled_transmutation(self):

		ot_n_ctrl_t = str(self.MAGICAL_ROOT /"ot_n_ctrl_t.loggy")
		self.make_loggy_file(ot_n_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_n_ctrl_t
				init_name	= "ot_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,[ "@ot_n_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation" ]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_n_ctrl_t
				init_name	= "ot_n_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_n_ctrl_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_n_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= ot_n_ctrl_t
				init_name		= "ot_n_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ot_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_n_ctrl_t-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ot_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ot_n_ctrl_t): os.remove(ot_n_ctrl_t)








	def test_other_escalated_controlled_transmutation(self):

		ot_e_ctrl_t = str(self.MAGICAL_ROOT /"ot_e_ctrl_t.loggy")
		self.make_loggy_file(ot_e_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= ot_e_ctrl_t
					init_name	= "ot_e_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@ot_e_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@ot_e_ctrl_t-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= ot_e_ctrl_t
						init_name	= "ot_e_ctrl_t-2"
						init_level	= 10

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_e_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@ot_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@ot_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:
					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= ot_e_ctrl_t
							init_name		= "ot_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(ot_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertFalse(loggy)
		if	os.path.isfile(ot_e_ctrl_t): os.remove(ot_e_ctrl_t)








	def test_other_escalated_name_controlled_transmutation(self):

		ot_e_n_ctrl_t = str(self.MAGICAL_ROOT /"ot_e_n_ctrl_t.loggy")
		self.make_loggy_file(ot_e_n_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= ot_e_n_ctrl_t
					init_name	= "ot_e_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(
			loggy,
			[
				"@ot_e_n_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@ot_e_n_ctrl_t-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= ot_e_n_ctrl_t
						init_name	= "ot_e_n_ctrl_t-2"
						init_level	= 10

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_e_n_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@ot_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:
					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= ot_e_n_ctrl_t
							init_name		= "ot_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(ot_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertFalse(loggy)
		if	os.path.isfile(ot_e_n_ctrl_t): os.remove(ot_e_n_ctrl_t)








	def test_other_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Bound(Transmutable):	pass

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"The {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):	pass
					def __call__(self, obj :str) -> str :

						job = f"The {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_other_loaded_controlled_transmutation(self):

		ot_l_ctrl_t = str(self.MAGICAL_ROOT /"ot_l_ctrl_t.loggy")
		self.make_loggy_file(ot_l_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_l_ctrl_t
				init_name	= "ot_l_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_l_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_l_ctrl_t
				init_name	= "ot_l_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_l_ctrl_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_l_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= ot_l_ctrl_t
				init_name		= "ot_l_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_l_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ot_l_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_ctrl_t-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_l_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ot_l_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ot_l_ctrl_t): os.remove(ot_l_ctrl_t)








	def test_other_loaded_name_controlled_transmutation(self):

		ot_l_n_ctrl_t = str(self.MAGICAL_ROOT /"ot_l_n_ctrl_t.loggy")
		self.make_loggy_file(ot_l_n_ctrl_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= ot_l_n_ctrl_t
				init_name	= "ot_l_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_l_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_n_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= ot_l_n_ctrl_t
				init_name	= "ot_l_n_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_l_n_ctrl_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_l_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_n_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= ot_l_n_ctrl_t
				init_name		= "ot_l_n_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_l_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ot_l_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_n_ctrl_t-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_l_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ot_l_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ot_l_n_ctrl_t): os.remove(ot_l_n_ctrl_t)








	def test_other_loaded_escalated_controlled_transmutation(self):

		ot_l_e_ctrl_t = str(self.MAGICAL_ROOT /"ot_l_e_ctrl_t.loggy")
		self.make_loggy_file(ot_l_e_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= ot_l_e_ctrl_t
					init_name	= "ot_l_e_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_l_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_e_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@ot_l_e_ctrl_t-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= ot_l_e_ctrl_t
						init_name	= "ot_l_e_ctrl_t-2"
						init_level	= 10

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_l_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_l_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_e_ctrl_t-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_l_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@ot_l_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= ot_l_e_ctrl_t
							init_name		= "ot_l_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_l_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(ot_l_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(ot_l_e_ctrl_t): os.remove(ot_l_e_ctrl_t)








	def test_other_loaded_escalated_name_controlled_transmutation(self):

		ot_l_e_n_ctrl_t = str(self.MAGICAL_ROOT /"ot_l_e_n_ctrl_t.loggy")
		self.make_loggy_file(ot_l_e_n_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= ot_l_e_n_ctrl_t
					init_name	= "ot_l_e_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_l_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_e_n_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
				"@ot_l_e_n_ctrl_t-1 INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= ot_l_e_n_ctrl_t
						init_name	= "ot_l_e_n_ctrl_t-2"
						init_level	= 10

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_l_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_l_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_l_e_n_ctrl_t-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_l_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@ot_l_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= ot_l_e_n_ctrl_t
							init_name		= "ot_l_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_l_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(ot_l_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(ot_l_e_n_ctrl_t): os.remove(ot_l_e_n_ctrl_t)








	def test_other_loaded_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Bound(Transmutable):	pass

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):	pass
					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_other_mixed_controlled_transmutation(self):

		ot_m_ctrl_t = str(self.MAGICAL_ROOT /"ot_m_ctrl_t.loggy")
		self.make_loggy_file(ot_m_ctrl_t)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_m_ctrl_t
				init_name	= "ot_m_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_m_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= ot_m_ctrl_t
				init_name	= "ot_m_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_m_ctrl_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_m_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= ot_m_ctrl_t
				init_name		= "ot_m_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_m_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ot_m_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_ctrl_t-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_m_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ot_m_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ot_m_ctrl_t): os.remove(ot_m_ctrl_t)








	def test_other_mixed_name_controlled_transmutation(self):

		ot_m_n_ctrl_t = str(self.MAGICAL_ROOT /"ot_m_n_ctrl_t.loggy")
		self.make_loggy_file(ot_m_n_ctrl_t)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= ot_m_n_ctrl_t
				init_name	= "ot_m_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_m_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_n_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= ot_m_n_ctrl_t
				init_name	= "ot_m_n_ctrl_t-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_m_n_ctrl_t)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_m_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_n_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= ot_m_n_ctrl_t
				init_name		= "ot_m_n_ctrl_t-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_m_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(ot_m_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_n_ctrl_t-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_m_n_ctrl_t-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@ot_m_n_ctrl_t-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(ot_m_n_ctrl_t): os.remove(ot_m_n_ctrl_t)








	def test_other_mixed_escalated_controlled_transmutation(self):

		ot_m_e_ctrl_t = str(self.MAGICAL_ROOT /"ot_m_e_ctrl_t.loggy")
		self.make_loggy_file(ot_m_e_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= ot_m_e_ctrl_t
					init_name	= "ot_m_e_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_m_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_e_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= ot_m_e_ctrl_t
						init_name	= "ot_m_e_ctrl_t-2"
						init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_m_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_m_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_e_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_m_e_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@ot_m_e_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= ot_m_e_ctrl_t
							init_name		= "ot_m_e_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_m_e_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)

		self.test_case.loggy.close()

		with open(ot_m_e_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(ot_m_e_ctrl_t): os.remove(ot_m_e_ctrl_t)








	def test_other_mixed_escalated_name_controlled_transmutation(self):

		ot_m_e_n_ctrl_t = str(self.MAGICAL_ROOT /"ot_m_e_n_ctrl_t.loggy")
		self.make_loggy_file(ot_m_e_n_ctrl_t)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= ot_m_e_n_ctrl_t
					init_name	= "ot_m_e_n_ctrl_t-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(ot_m_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_e_n_ctrl_t-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= ot_m_e_n_ctrl_t
						init_name	= "ot_m_e_n_ctrl_t-2"
						init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		loggy = []
		self.make_loggy_file(ot_m_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(ot_m_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@ot_m_e_n_ctrl_t-2-Stone ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@ot_m_e_n_ctrl_t-2-Stone.Handle WARNING : I am just a handle",
				"@ot_m_e_n_ctrl_t-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= ot_m_e_n_ctrl_t
							init_name		= "ot_m_e_n_ctrl_t-3"
							force_handover	= True

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(ot_m_e_n_ctrl_t)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)

		self.test_case.loggy.close()

		with open(ot_m_e_n_ctrl_t) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(ot_m_e_n_ctrl_t): os.remove(ot_m_e_n_ctrl_t)








	def test_other_mixed_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Bound(Transmutable):	pass

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint:

				def __call__(self, obj :str) -> str :

					job = f"the {obj} will be"
					self.loggy.info(job)
					return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				class Paint:

					class Bound(Transmutable):	pass
					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_other_top_layer_controlled_transmutation(self):

		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone:
			class loggy(LibraryContrib):	pass


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone:
			class loggy(LibraryContrib):	pass


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone:
			class loggy(LibraryContrib):	pass


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone:
			class loggy(LibraryContrib):	pass


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Mutagen("red", operation="turned")
		class Stone:
			class loggy(LibraryContrib):	pass


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)
















	def test_kws_top_layer_controlled_transmutation(self):

		kws_tl_ctrlt = str(self.MAGICAL_ROOT /"kws_tl_ctrlt.loggy")
		self.make_loggy_file(kws_tl_ctrlt)


		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class loggy(LibraryContrib):

				handler		= kws_tl_ctrlt
				init_name	= "kws_tl_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="Cool")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.test_case.loggy.close()

		with open(kws_tl_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_ctrlt-1 INFO : stone definitely will be",
				"@kws_tl_ctrlt-1 INFO : Cool stone definitely will be turned red",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


			class loggy(LibraryContrib):

				handler		= kws_tl_ctrlt
				init_name	= "kws_tl_ctrlt-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(kws_tl_ctrlt)
		self.test_case = Stone(which="Cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.test_case.loggy.close()

		with open(kws_tl_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_ctrlt-2-Stone INFO : stone definitely will be",
				"@kws_tl_ctrlt-2-Stone INFO : Cool stone definitely will be turned red",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class loggy(LibraryContrib):

				handler			= kws_tl_ctrlt
				init_name		= "kws_tl_ctrlt-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(kws_tl_ctrlt)
		self.test_case = Stone(how="definitely", which="Cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.test_case.loggy.close()

		with open(kws_tl_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_ctrlt-3-Stone INFO : stone definitely will be",
				"@kws_tl_ctrlt-3-Stone INFO : Cool stone definitely will be turned red",
				"@kws_tl_ctrlt-3-Stone INFO : I am definitely root",
			]
		)
		if	os.path.isfile(kws_tl_ctrlt): os.remove(kws_tl_ctrlt)








	def test_kws_top_layer_name_controlled_transmutation(self):

		kws_tl_n_ctrlt = str(self.MAGICAL_ROOT /"kws_tl_n_ctrlt.loggy")
		self.make_loggy_file(kws_tl_n_ctrlt)


		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class shmoggy(LibraryContrib):

				handler		= kws_tl_n_ctrlt
				init_name	= "kws_tl_n_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="Cool")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.test_case.loggy.close()

		with open(kws_tl_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_n_ctrlt-1 INFO : stone definitely will be",
				"@kws_tl_n_ctrlt-1 INFO : Cool stone definitely will be turned red",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


			class shmoggy(LibraryContrib):

				handler		= kws_tl_n_ctrlt
				init_name	= "kws_tl_n_ctrlt-2"
				init_level	= 10


		loggy = []
		self.make_loggy_file(kws_tl_n_ctrlt)
		self.test_case = Stone(which="Cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.test_case.loggy.close()

		with open(kws_tl_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_n_ctrlt-2-Stone INFO : stone definitely will be",
				"@kws_tl_n_ctrlt-2-Stone INFO : Cool stone definitely will be turned red",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class shmoggy(LibraryContrib):

				handler			= kws_tl_n_ctrlt
				init_name		= "kws_tl_n_ctrlt-3"
				force_handover	= True


		loggy = []
		self.make_loggy_file(kws_tl_n_ctrlt)
		self.test_case = Stone(how="definitely", which="Cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.test_case.loggy.close()

		with open(kws_tl_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_n_ctrlt-3-Stone INFO : stone definitely will be",
				"@kws_tl_n_ctrlt-3-Stone INFO : Cool stone definitely will be turned red",
				"@kws_tl_n_ctrlt-3-Stone INFO : I am definitely root",
			]
		)
		if	os.path.isfile(kws_tl_n_ctrlt): os.remove(kws_tl_n_ctrlt)








	def test_kws_top_layer_escalated_controlled_transmutation(self):

		kws_tl_e_ctrlt = str(self.MAGICAL_ROOT /"kws_tl_e_ctrlt.loggy")
		self.make_loggy_file(kws_tl_e_ctrlt)


		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= kws_tl_e_ctrlt
					init_name	= "kws_tl_e_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="Cool")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.test_case.loggy.close()

		with open(kws_tl_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_e_ctrlt-1 INFO : stone definitely will be",
				"@kws_tl_e_ctrlt-1 INFO : Cool stone definitely will be turned red",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= kws_tl_e_ctrlt
					init_name	= "kws_tl_e_ctrlt-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(kws_tl_e_ctrlt)
		self.test_case = Stone(which="Cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kws_tl_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_e_ctrlt-2-Stone INFO : stone definitely will be",
				"@kws_tl_e_ctrlt-2-Stone INFO : Cool stone definitely will be turned red",
				"@kws_tl_e_ctrlt-2-Stone.Bound INFO : I am definitely bound",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler			= kws_tl_e_ctrlt
						init_name		= "kws_tl_e_ctrlt-3"
						force_handover	= True


		loggy = []
		self.make_loggy_file(kws_tl_e_ctrlt)
		self.test_case = Stone(how="definitely", which="Cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning(f"I am {self.test_case.how} just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kws_tl_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_e_ctrlt-3-Stone INFO : stone definitely will be",
				"@kws_tl_e_ctrlt-3-Stone INFO : Cool stone definitely will be turned red",
				"@kws_tl_e_ctrlt-3-Stone INFO : I am definitely root",
				"@kws_tl_e_ctrlt-3-Stone.Handle WARNING : I am definitely just a handle",
				"@kws_tl_e_ctrlt-3-Stone.Handle.Bound INFO : I am definitely bound",
			]
		)
		if	os.path.isfile(kws_tl_e_ctrlt): os.remove(kws_tl_e_ctrlt)








	def test_kws_top_layer_escalated_name_controlled_transmutation(self):

		kws_tl_en_ctrlt = str(self.MAGICAL_ROOT /"kws_tl_en_ctrlt.loggy")
		self.make_loggy_file(kws_tl_en_ctrlt)


		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= kws_tl_en_ctrlt
					init_name	= "kws_tl_en_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="Cool")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.test_case.loggy.close()

		with open(kws_tl_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_en_ctrlt-1 INFO : stone definitely will be",
				"@kws_tl_en_ctrlt-1 INFO : Cool stone definitely will be turned red",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= kws_tl_en_ctrlt
					init_name	= "kws_tl_en_ctrlt-2"
					init_level	= 10


		loggy = []
		self.make_loggy_file(kws_tl_en_ctrlt)
		self.test_case = Stone(which="Cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kws_tl_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_en_ctrlt-2-Stone INFO : stone definitely will be",
				"@kws_tl_en_ctrlt-2-Stone INFO : Cool stone definitely will be turned red",
				"@kws_tl_en_ctrlt-2-Stone.Bound INFO : I am definitely bound",
			]
		)




		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= kws_tl_en_ctrlt
						init_name		= "kws_tl_en_ctrlt-3"
						force_handover	= True


		loggy = []
		self.make_loggy_file(kws_tl_en_ctrlt)
		self.test_case = Stone(how="definitely", which="Cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning(f"I am {self.test_case.how} just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kws_tl_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kws_tl_en_ctrlt-3-Stone INFO : stone definitely will be",
				"@kws_tl_en_ctrlt-3-Stone INFO : Cool stone definitely will be turned red",
				"@kws_tl_en_ctrlt-3-Stone INFO : I am definitely root",
				"@kws_tl_en_ctrlt-3-Stone.Handle WARNING : I am definitely just a handle",
				"@kws_tl_en_ctrlt-3-Stone.Handle.Bound INFO : I am definitely bound",
			]
		)
		if	os.path.isfile(kws_tl_en_ctrlt): os.remove(kws_tl_en_ctrlt)








	def test_kws_top_layer_no_loggy_controlled_transmutation(self):

		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Transmutable):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job

			class Handle(Transmutable):
				class Bound(Transmutable):	pass


		self.test_case = Stone(how="definitely", which="Cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Cool stone definitely will be turned red")
		self.assertEqual(self.test_case.loggy.info(f"I am {self.test_case.how} root"), NotImplemented)
		self.assertEqual(

			self.test_case.Handle.loggy.warning(f"I am {self.test_case.how} just a handle"),
			NotImplemented
		)
		self.assertEqual(

			self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.how} bound"),
			NotImplemented
		)
















	def test_kws_top_layer_loaded_controlled_transmutation(self):

		kw_tll_ctrlt = str(self.MAGICAL_ROOT /"kw_tll_ctrlt.loggy")
		self.make_loggy_file(kw_tll_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.KWPaintBrash):

			class loggy(LibraryContrib):

				handler		= kw_tll_ctrlt
				init_name	= "kw_tll_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.test_case.loggy.close()

		with open(kw_tll_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_ctrlt-1 INFO : stone definitely will be",
				"@kw_tll_ctrlt-1 INFO : cool stone definitely will be turned red",
				"@kw_tll_ctrlt-1 INFO : Today cool stone definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class loggy(LibraryContrib):

				handler		= kw_tll_ctrlt
				init_name	= "kw_tll_ctrlt-2"
				init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tll_ctrlt)
		self.test_case = Stone(sure="100%", which="cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.test_case.loggy.close()

		with open(kw_tll_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_ctrlt-2-Stone INFO : stone definitely will be",
				"@kw_tll_ctrlt-2-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_ctrlt-2-Stone INFO : Today cool stone definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler			= kw_tll_ctrlt
				init_name		= "kw_tll_ctrlt-3"
				force_handover	= True

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tll_ctrlt)
		self.test_case = Stone(butWhy="dunno", which="cool", sure="100%", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.test_case.loggy.close()

		with open(kw_tll_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_ctrlt-3-Stone INFO : stone definitely will be",
				"@kw_tll_ctrlt-3-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_ctrlt-3-Stone INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_ctrlt-3-Stone INFO : I am definitely root",
			]
		)
		if	os.path.isfile(kw_tll_ctrlt): os.remove(kw_tll_ctrlt)








	def test_kws_top_layer_loaded_name_controlled_transmutation(self):

		kw_tll_n_ctrlt = str(self.MAGICAL_ROOT /"kw_tll_n_ctrlt.loggy")
		self.make_loggy_file(kw_tll_n_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.KWPaintBrash):

			class shmoggy(LibraryContrib):

				handler		= kw_tll_n_ctrlt
				init_name	= "kw_tll_n_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.test_case.loggy.close()

		with open(kw_tll_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_n_ctrlt-1 INFO : stone definitely will be",
				"@kw_tll_n_ctrlt-1 INFO : cool stone definitely will be turned red",
				"@kw_tll_n_ctrlt-1 INFO : Today cool stone definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class shmoggy(LibraryContrib):

				handler		= kw_tll_n_ctrlt
				init_name	= "kw_tll_n_ctrlt-2"
				init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tll_n_ctrlt)
		self.test_case = Stone(sure="100%", which="cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.test_case.loggy.close()

		with open(kw_tll_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_n_ctrlt-2-Stone INFO : stone definitely will be",
				"@kw_tll_n_ctrlt-2-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_n_ctrlt-2-Stone INFO : Today cool stone definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler			= kw_tll_n_ctrlt
				init_name		= "kw_tll_n_ctrlt-3"
				force_handover	= True

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tll_n_ctrlt)
		self.test_case = Stone(butWhy="dunno", which="cool", sure="100%", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.test_case.loggy.close()

		with open(kw_tll_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_n_ctrlt-3-Stone INFO : stone definitely will be",
				"@kw_tll_n_ctrlt-3-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_n_ctrlt-3-Stone INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_n_ctrlt-3-Stone INFO : I am definitely root",
			]
		)
		if	os.path.isfile(kw_tll_n_ctrlt): os.remove(kw_tll_n_ctrlt)








	def test_kws_top_layer_loaded_escalated_controlled_transmutation(self):

		kw_tll_e_ctrlt = str(self.MAGICAL_ROOT /"kw_tll_e_ctrlt.loggy")
		self.make_loggy_file(kw_tll_e_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.KWPaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= kw_tll_e_ctrlt
					init_name	= "kw_tll_e_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kw_tll_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_e_ctrlt-1 INFO : stone definitely will be",
				"@kw_tll_e_ctrlt-1 INFO : cool stone definitely will be turned red",
				"@kw_tll_e_ctrlt-1 INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_e_ctrlt-1 INFO : I am definitely bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= kw_tll_e_ctrlt
					init_name	= "kw_tll_e_ctrlt-2"
					init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tll_e_ctrlt)
		self.test_case = Stone(sure="100%", which="cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kw_tll_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_e_ctrlt-2-Stone INFO : stone definitely will be",
				"@kw_tll_e_ctrlt-2-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_e_ctrlt-2-Stone INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_e_ctrlt-2-Stone.Bound INFO : I am definitely bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler			= kw_tll_e_ctrlt
						init_name		= "kw_tll_e_ctrlt-3"
						force_handover	= True

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tll_e_ctrlt)
		self.test_case = Stone(butWhy="dunno", which="cool", sure="100%", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning(f"I am {self.test_case.how} just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kw_tll_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_e_ctrlt-3-Stone INFO : stone definitely will be",
				"@kw_tll_e_ctrlt-3-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_e_ctrlt-3-Stone INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_e_ctrlt-3-Stone INFO : I am definitely root",
				"@kw_tll_e_ctrlt-3-Stone.Handle WARNING : I am definitely just a handle",
				"@kw_tll_e_ctrlt-3-Stone.Handle.Bound INFO : I am definitely bound",
			]
		)
		if	os.path.isfile(kw_tll_e_ctrlt): os.remove(kw_tll_e_ctrlt)








	def test_kws_top_layer_loaded_escalated_name_controlled_transmutation(self):

		kw_tll_en_ctrlt = str(self.MAGICAL_ROOT /"kw_tll_en_ctrlt.loggy")
		self.make_loggy_file(kw_tll_en_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.KWPaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= kw_tll_en_ctrlt
					init_name	= "kw_tll_en_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kw_tll_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_en_ctrlt-1 INFO : stone definitely will be",
				"@kw_tll_en_ctrlt-1 INFO : cool stone definitely will be turned red",
				"@kw_tll_en_ctrlt-1 INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_en_ctrlt-1 INFO : I am definitely bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= kw_tll_en_ctrlt
					init_name	= "kw_tll_en_ctrlt-2"
					init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tll_en_ctrlt)
		self.test_case = Stone(sure="100%", which="cool", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kw_tll_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_en_ctrlt-2-Stone INFO : stone definitely will be",
				"@kw_tll_en_ctrlt-2-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_en_ctrlt-2-Stone INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_en_ctrlt-2-Stone.Bound INFO : I am definitely bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= kw_tll_en_ctrlt
						init_name		= "kw_tll_en_ctrlt-3"
						force_handover	= True

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tll_en_ctrlt)
		self.test_case = Stone(butWhy="dunno", which="cool", sure="100%", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertIsNone(self.test_case.loggy.info(f"I am {self.test_case.how} root"))
		self.assertIsNone(self.test_case.Handle.loggy.warning(f"I am {self.test_case.how} just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.how} bound"))
		self.test_case.loggy.close()

		with open(kw_tll_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tll_en_ctrlt-3-Stone INFO : stone definitely will be",
				"@kw_tll_en_ctrlt-3-Stone INFO : cool stone definitely will be turned red",
				"@kw_tll_en_ctrlt-3-Stone INFO : Today cool stone definitely will be turned red, 100%",
				"@kw_tll_en_ctrlt-3-Stone INFO : I am definitely root",
				"@kw_tll_en_ctrlt-3-Stone.Handle WARNING : I am definitely just a handle",
				"@kw_tll_en_ctrlt-3-Stone.Handle.Bound INFO : I am definitely bound",
			]
		)
		if	os.path.isfile(kw_tll_en_ctrlt): os.remove(kw_tll_en_ctrlt)








	def test_kws_top_layer_loaded_no_loggy_controlled_transmutation(self):

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(StoneControlledMutationCase.KWPaintBrash):
			class Bound(Transmutable):	pass


		self.test_case = Stone(how="definitely", which="cool", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertEqual(self.test_case.Bound.loggy.info(f"I am {self.test_case.how} bound"), NotImplemented)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		self.test_case = Stone(butWhy="dunno", which="cool", sure="100%", how="definitely")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case("stone"), "Today cool stone definitely will be turned red, 100%")
		self.assertEqual(self.test_case.loggy.info(f"I am {self.test_case.how} root"), NotImplemented)
		self.assertEqual(

			self.test_case.Handle.loggy.warning(f"I am {self.test_case.how} just a handle"),
			NotImplemented
		)
		self.assertEqual(

			self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.how} bound"),
			NotImplemented
		)
















	def test_kws_top_layer_mixed_controlled_transmutation(self):

		kw_tlm_ctrlt = str(self.MAGICAL_ROOT /"kw_tlm_ctrlt.loggy")
		self.make_loggy_file(kw_tlm_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		@StoneControlledMutationCase.KWPatogen
		class Stone(StoneControlledMutationCase.KWPaintBrash):
			class loggy(LibraryContrib):

				handler		= kw_tlm_ctrlt
				init_name	= "kw_tlm_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%", subst="material")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.test_case.loggy.close()

		with open(kw_tlm_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_ctrlt-1 INFO : dark-stone material definitely will be",
				"@kw_tlm_ctrlt-1 INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_ctrlt-1 INFO : Today cool dark-stone material definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class loggy(LibraryContrib):

				handler		= kw_tlm_ctrlt
				init_name	= "kw_tlm_ctrlt-2"
				init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tlm_ctrlt)
		self.test_case = Stone(subst="material", which="cool", how="definitely", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.test_case.loggy.close()

		with open(kw_tlm_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_ctrlt-2-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_ctrlt-2-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_ctrlt-2-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class loggy(LibraryContrib):

				handler			= kw_tlm_ctrlt
				init_name		= "kw_tlm_ctrlt-3"
				force_handover	= True

		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			class Handle(Transmutable):	pass
			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tlm_ctrlt)
		self.test_case = Stone(how="definitely", sure="100%", subst="material", which="cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(
			self.test_case.Handle.loggy.error(f"This stone is {self.test_case.sure} uncontrollable!")
		)
		self.assertIsNone(self.test_case.loggy.info(f"I am root {self.test_case.subst}"))
		self.test_case.loggy.close()

		with open(kw_tlm_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_ctrlt-3-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_ctrlt-3-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_ctrlt-3-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				r"@kw_tlm_ctrlt-3-Stone.Handle ERROR : This stone is 100% uncontrollable!",
				"@kw_tlm_ctrlt-3-Stone INFO : I am root material",
			]
		)
		if	os.path.isfile(kw_tlm_ctrlt): os.remove(kw_tlm_ctrlt)








	def test_kws_top_layer_mixed_name_controlled_transmutation(self):

		kw_tlm_n_ctrlt = str(self.MAGICAL_ROOT /"kw_tlm_n_ctrlt.loggy")
		self.make_loggy_file(kw_tlm_n_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		@StoneControlledMutationCase.KWPatogen
		class Stone(StoneControlledMutationCase.KWPaintBrash):
			class shmoggy(LibraryContrib):

				handler		= kw_tlm_n_ctrlt
				init_name	= "kw_tlm_n_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%", subst="material")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.test_case.loggy.close()

		with open(kw_tlm_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_n_ctrlt-1 INFO : dark-stone material definitely will be",
				"@kw_tlm_n_ctrlt-1 INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_n_ctrlt-1 INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class shmoggy(LibraryContrib):

				handler		= kw_tlm_n_ctrlt
				init_name	= "kw_tlm_n_ctrlt-2"
				init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tlm_n_ctrlt)
		self.test_case = Stone(subst="material", which="cool", how="definitely", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.test_case.loggy.close()

		with open(kw_tlm_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_n_ctrlt-2-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_n_ctrlt-2-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_n_ctrlt-2-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class shmoggy(LibraryContrib):

				handler			= kw_tlm_n_ctrlt
				init_name		= "kw_tlm_n_ctrlt-3"
				force_handover	= True

		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			class Handle(Transmutable):	pass
			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tlm_n_ctrlt)
		self.test_case = Stone(how="definitely", sure="100%", subst="material", which="cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(
			self.test_case.Handle.loggy.error(f"This stone is {self.test_case.sure} uncontrollable!")
		)
		self.assertIsNone(self.test_case.loggy.info(f"I am root {self.test_case.subst}"))
		self.test_case.loggy.close()

		with open(kw_tlm_n_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_n_ctrlt-3-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_n_ctrlt-3-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_n_ctrlt-3-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				r"@kw_tlm_n_ctrlt-3-Stone.Handle ERROR : This stone is 100% uncontrollable!",
				"@kw_tlm_n_ctrlt-3-Stone INFO : I am root material",
			]
		)
		if	os.path.isfile(kw_tlm_n_ctrlt): os.remove(kw_tlm_n_ctrlt)








	def test_kws_top_layer_mixed_escalated_controlled_transmutation(self):

		kw_tlm_e_ctrlt = str(self.MAGICAL_ROOT /"kw_tlm_e_ctrlt.loggy")
		self.make_loggy_file(kw_tlm_e_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		@StoneControlledMutationCase.KWPatogen
		class Stone(StoneControlledMutationCase.KWPaintBrash):

			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= kw_tlm_e_ctrlt
					init_name	= "kw_tlm_e_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%", subst="material")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.which} bound"))
		self.test_case.loggy.close()

		with open(kw_tlm_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_e_ctrlt-1 INFO : dark-stone material definitely will be",
				"@kw_tlm_e_ctrlt-1 INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_e_ctrlt-1 INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				"@kw_tlm_e_ctrlt-1 INFO : I am cool bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= kw_tlm_e_ctrlt
					init_name	= "kw_tlm_e_ctrlt-2"
					init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tlm_e_ctrlt)
		self.test_case = Stone(subst="material", which="cool", how="definitely", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.which} bound"))
		self.test_case.loggy.close()

		with open(kw_tlm_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_e_ctrlt-2-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_e_ctrlt-2-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_e_ctrlt-2-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				"@kw_tlm_e_ctrlt-2-Stone.Bound INFO : I am cool bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler			= kw_tlm_e_ctrlt
						init_name		= "kw_tlm_e_ctrlt-3"
						force_handover	= True

		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tlm_e_ctrlt)
		self.test_case = Stone(how="definitely", sure="100%", subst="material", which="cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(
			self.test_case.Handle.loggy.error(f"This stone is {self.test_case.sure} uncontrollable!")
		)
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.which} bound"))
		self.assertIsNone(self.test_case.loggy.info(f"I am root {self.test_case.subst}"))
		self.test_case.loggy.close()

		with open(kw_tlm_e_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_e_ctrlt-3-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_e_ctrlt-3-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_e_ctrlt-3-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				r"@kw_tlm_e_ctrlt-3-Stone.Handle ERROR : This stone is 100% uncontrollable!",
				"@kw_tlm_e_ctrlt-3-Stone.Handle.Bound INFO : I am cool bound",
				"@kw_tlm_e_ctrlt-3-Stone INFO : I am root material",
			]
		)
		if	os.path.isfile(kw_tlm_e_ctrlt): os.remove(kw_tlm_e_ctrlt)








	def test_kws_top_layer_mixed_escalated_name_controlled_transmutation(self):

		kw_tlm_en_ctrlt = str(self.MAGICAL_ROOT /"kw_tlm_en_ctrlt.loggy")
		self.make_loggy_file(kw_tlm_en_ctrlt)


		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		@StoneControlledMutationCase.KWPatogen
		class Stone(StoneControlledMutationCase.KWPaintBrash):

			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= kw_tlm_en_ctrlt
					init_name	= "kw_tlm_en_ctrlt-1"


		loggy = []
		self.test_case = Stone(how="definitely", which="cool", sure="100%", subst="material")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.which} bound"))
		self.test_case.loggy.close()

		with open(kw_tlm_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_en_ctrlt-1 INFO : dark-stone material definitely will be",
				"@kw_tlm_en_ctrlt-1 INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_en_ctrlt-1 INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				"@kw_tlm_en_ctrlt-1 INFO : I am cool bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.KWPaintBrash):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= kw_tlm_en_ctrlt
					init_name	= "kw_tlm_en_ctrlt-2"
					init_level	= 10

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):	pass


		loggy = []
		self.make_loggy_file(kw_tlm_en_ctrlt)
		self.test_case = Stone(subst="material", which="cool", how="definitely", sure="100%")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(self.test_case.Bound.loggy.info(f"I am {self.test_case.which} bound"))
		self.test_case.loggy.close()

		with open(kw_tlm_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_en_ctrlt-2-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_en_ctrlt-2-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_en_ctrlt-2-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				"@kw_tlm_en_ctrlt-2-Stone.Bound INFO : I am cool bound",
			]
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler			= kw_tlm_en_ctrlt
						init_name		= "kw_tlm_en_ctrlt-3"
						force_handover	= True

		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		loggy = []
		self.make_loggy_file(kw_tlm_en_ctrlt)
		self.test_case = Stone(how="definitely", sure="100%", subst="material", which="cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertIsNone(
			self.test_case.Handle.loggy.error(f"This stone is {self.test_case.sure} uncontrollable!")
		)
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.which} bound"))
		self.assertIsNone(self.test_case.loggy.info(f"I am root {self.test_case.subst}"))
		self.test_case.loggy.close()

		with open(kw_tlm_en_ctrlt) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@kw_tlm_en_ctrlt-3-Stone INFO : dark-stone material definitely will be",
				"@kw_tlm_en_ctrlt-3-Stone INFO : cool dark-stone material definitely will be turned red",
				"@kw_tlm_en_ctrlt-3-Stone INFO : "
				"Today cool dark-stone material definitely will be turned red, 100%",
				r"@kw_tlm_en_ctrlt-3-Stone.Handle ERROR : This stone is 100% uncontrollable!",
				"@kw_tlm_en_ctrlt-3-Stone.Handle.Bound INFO : I am cool bound",
				"@kw_tlm_en_ctrlt-3-Stone INFO : I am root material",
			]
		)
		if	os.path.isfile(kw_tlm_en_ctrlt): os.remove(kw_tlm_en_ctrlt)








	def test_kws_top_layer_mixed_no_loggy_controlled_transmutation(self):

		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		@StoneControlledMutationCase.KWPatogen
		class Stone(StoneControlledMutationCase.KWPaintBrash):
			class Bound(Transmutable):	pass


		self.test_case = Stone(how="definitely", which="cool", sure="100%", subst="material")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertEqual(
			self.test_case.Bound.loggy.info(f"I am {self.test_case.which} bound"), NotImplemented
		)




		class Outdoor(StoneControlledMutationCase.PaintBrash):
			class Handle(Transmutable):
				class Bound(Transmutable):	pass

		@StoneControlledMutationCase.KWPatogen
		@StoneControlledMutationCase.KWMutabor("Today")
		@StoneControlledMutationCase.KWMutagen("red", operation="turned")
		class Stone(Outdoor):

			def __call__(self, obj :str) -> str :

				job = f"{obj} {self.how} will be"
				self.loggy.info(job)
				return job


		self.test_case = Stone(how="definitely", sure="100%", subst="material", which="cool", butWhy="dunno")
		self.assertIsInstance(self.test_case, Transmutable)
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(
			self.test_case("stone"), "Today cool dark-stone material definitely will be turned red, 100%"
		)
		self.assertEqual(
			self.test_case.Handle.loggy.error(f"This stone is {self.test_case.sure} uncontrollable!"),
			NotImplemented
		)
		self.assertEqual(
			self.test_case.Handle.Bound.loggy.info(f"I am {self.test_case.which} bound"), NotImplemented
		)
		self.assertEqual(self.test_case.loggy.info(f"I am root {self.test_case.subst}"), NotImplemented)
















	def test_mutable_chain_injection_controlled_transmutation(self):

		mci_ct = str(self.MAGICAL_ROOT /"mci_ct.loggy")
		self.make_loggy_file(mci_ct)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ct
				init_name	= "mci_ct-1"

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ct
				init_name	= "mci_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_ct
				init_name		= "mci_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_ct): os.remove(mci_ct)








	def test_mutable_chain_injection_name_controlled_transmutation(self):

		mci_n_ct = str(self.MAGICAL_ROOT /"mci_n_ct.loggy")
		self.make_loggy_file(mci_n_ct)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_n_ct
				init_name	= "mci_n_ct-1"

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_n_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_n_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_n_ct
				init_name	= "mci_n_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_n_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_n_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_n_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_n_ct
				init_name		= "mci_n_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_n_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_n_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_n_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_n_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_n_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_n_ct): os.remove(mci_n_ct)








	def test_mutable_chain_injection_escalated_controlled_transmutation(self):

		mci_e_ct = str(self.MAGICAL_ROOT /"mci_e_ct.loggy")
		self.make_loggy_file(mci_e_ct)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_e_ct
					init_name	= "mci_e_ct-1"

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_e_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_e_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_e_ct
						init_name	= "mci_e_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_e_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_e_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_e_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_e_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_e_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= mci_e_ct
							init_name		= "mci_e_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_e_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_e_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_e_ct): os.remove(mci_e_ct)








	def test_mutable_chain_injection_escalated_name_controlled_transmutation(self):

		mci_en_ct = str(self.MAGICAL_ROOT /"mci_en_ct.loggy")
		self.make_loggy_file(mci_en_ct)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_en_ct
					init_name	= "mci_en_ct-1"

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_en_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_en_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_en_ct
						init_name	= "mci_en_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_en_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_en_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_en_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_en_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_en_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= mci_en_ct
							init_name		= "mci_en_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_en_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_en_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_en_ct): os.remove(mci_en_ct)








	def test_mutable_chain_injection_no_loggy_controlled_transmutation(self):
		class Stone(Transmutable):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass
				class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_mutable_chain_injection_loaded_controlled_transmutation(self):

		mci_l_ct = str(self.MAGICAL_ROOT /"mci_l_ct.loggy")
		self.make_loggy_file(mci_l_ct)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_l_ct
				init_name	= "mci_l_ct-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_l_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_l_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_l_ct
				init_name	= "mci_l_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Mutabor("Today")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_l_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_l_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_l_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_l_ct
				init_name		= "mci_l_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass

		loggy = []
		self.make_loggy_file(mci_l_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_l_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_l_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_l_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_l_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_l_ct): os.remove(mci_l_ct)








	def test_mutable_chain_injection_loaded_name_controlled_transmutation(self):

		mci_ln_ct = str(self.MAGICAL_ROOT /"mci_ln_ct.loggy")
		self.make_loggy_file(mci_ln_ct)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_ln_ct
				init_name	= "mci_ln_ct-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ln_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ln_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_ln_ct
				init_name	= "mci_ln_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Mutabor("Today")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_ln_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ln_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ln_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_ln_ct
				init_name		= "mci_ln_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					def __call__(self, obj :str) -> str :

						job = f"the {obj} will be"
						self.loggy.info(job)
						return job


		loggy = []
		self.make_loggy_file(mci_ln_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ln_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ln_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_ln_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ln_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_ln_ct): os.remove(mci_ln_ct)








	def test_mutable_chain_injection_loaded_escalated_controlled_transmutation(self):

		mci_le_ct = str(self.MAGICAL_ROOT /"mci_le_ct.loggy")
		self.make_loggy_file(mci_le_ct)


		class Stone(Transmutable):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_le_ct
					init_name	= "mci_le_ct-1"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_le_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_le_ct-1 INFO : I am bound" ])




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_le_ct
						init_name	= "mci_le_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Mutabor("Today")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_le_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_le_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_le_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_le_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_le_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= mci_le_ct
							init_name		= "mci_le_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_le_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_le_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_le_ct): os.remove(mci_le_ct)








	def test_mutable_chain_injection_loaded_escalated_name_controlled_transmutation(self):

		mci_len_ct = str(self.MAGICAL_ROOT /"mci_len_ct.loggy")
		self.make_loggy_file(mci_len_ct)


		class Stone(Transmutable):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_len_ct
					init_name	= "mci_len_ct-1"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_len_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_len_ct-1 INFO : I am bound" ])




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_len_ct
						init_name	= "mci_len_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Mutabor("Today")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_len_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_len_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_len_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_len_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_len_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= mci_len_ct
							init_name		= "mci_len_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_len_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_len_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_len_ct): os.remove(mci_len_ct)








	def test_mutable_chain_injection_loaded_no_loggy_controlled_transmutation(self):
		class Stone(Transmutable):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Mutabor("Today")
				class Paint(Transmutable):	pass
				class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_mutable_chain_injection_double_controlled_transmutation(self):

		mci_d_ct = str(self.MAGICAL_ROOT /"mci_d_ct.loggy")
		self.make_loggy_file(mci_d_ct)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_d_ct
				init_name	= "mci_d_ct-1"

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_d_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_d_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_d_ct
				init_name	= "mci_d_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_d_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_d_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_d_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_d_ct
				init_name		= "mci_d_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_d_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_d_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_d_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_d_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_d_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_d_ct): os.remove(mci_d_ct)








	def test_mutable_chain_injection_double_name_controlled_transmutation(self):

		mci_dn_ct = str(self.MAGICAL_ROOT /"mci_dn_ct.loggy")
		self.make_loggy_file(mci_dn_ct)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_dn_ct
				init_name	= "mci_dn_ct-1"

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_dn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_dn_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_dn_ct
				init_name	= "mci_dn_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_dn_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_dn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_dn_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_dn_ct
				init_name		= "mci_dn_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_dn_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_dn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_dn_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_dn_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_dn_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_dn_ct): os.remove(mci_dn_ct)








	def test_mutable_chain_injection_double_escalated_controlled_transmutation(self):

		mci_de_ct = str(self.MAGICAL_ROOT /"mci_de_ct.loggy")
		self.make_loggy_file(mci_de_ct)


		class Stone(Transmutable):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_de_ct
					init_name	= "mci_de_ct-1"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_de_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_de_ct-1 INFO : I am bound" ])




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_de_ct
						init_name	= "mci_de_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_de_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_de_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_de_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_de_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_de_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= mci_de_ct
							init_name		= "mci_de_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_de_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_de_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_de_ct): os.remove(mci_de_ct)








	def test_mutable_chain_injection_double_escalated_name_controlled_transmutation(self):

		mci_den_ct = str(self.MAGICAL_ROOT /"mci_den_ct.loggy")
		self.make_loggy_file(mci_den_ct)


		class Stone(Transmutable):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_den_ct
					init_name	= "mci_den_ct-1"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_den_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_den_ct-1 INFO : I am bound" ])




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_den_ct
						init_name	= "mci_den_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_den_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_den_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_den_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_den_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_den_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= mci_den_ct
							init_name		= "mci_den_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_den_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_den_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_den_ct): os.remove(mci_den_ct)








	def test_mutable_chain_injection_double_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(Transmutable):	pass
				class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)
















	def test_mutable_chain_injection_triple_controlled_transmutation(self):

		mci_t_ct = str(self.MAGICAL_ROOT /"mci_t_ct.loggy")
		self.make_loggy_file(mci_t_ct)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_t_ct
				init_name	= "mci_t_ct-1"

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_t_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_t_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_t_ct
				init_name	= "mci_t_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_t_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_t_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_t_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_t_ct
				init_name		= "mci_t_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_t_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_t_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_t_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_t_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_t_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_t_ct): os.remove(mci_t_ct)








	def test_mutable_chain_injection_triple_name_controlled_transmutation(self):

		mci_tn_ct = str(self.MAGICAL_ROOT /"mci_tn_ct.loggy")
		self.make_loggy_file(mci_tn_ct)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_tn_ct
				init_name	= "mci_tn_ct-1"

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_tn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_tn_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_tn_ct
				init_name	= "mci_tn_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_tn_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_tn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_tn_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_tn_ct
				init_name		= "mci_tn_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_tn_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_tn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_tn_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_tn_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_tn_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_tn_ct): os.remove(mci_tn_ct)








	def test_mutable_chain_injection_triple_escalated_controlled_transmutation(self):

		mci_te_ct = str(self.MAGICAL_ROOT /"mci_te_ct.loggy")
		self.make_loggy_file(mci_te_ct)


		class Stone(Transmutable):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(Transmutable):	pass
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_te_ct
					init_name	= "mci_te_ct-1"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_te_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_te_ct-1 INFO : I am bound" ])




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_te_ct
						init_name	= "mci_te_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_te_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_te_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_te_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_te_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_te_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= mci_te_ct
							init_name		= "mci_te_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_te_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_te_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_te_ct): os.remove(mci_te_ct)








	def test_mutable_chain_injection_triple_escalated_name_controlled_transmutation(self):

		mci_ten_ct = str(self.MAGICAL_ROOT /"mci_ten_ct.loggy")
		self.make_loggy_file(mci_ten_ct)


		class Stone(Transmutable):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(Transmutable):	pass
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_ten_ct
					init_name	= "mci_ten_ct-1"


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ten_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[ "@mci_ten_ct-1 INFO : I am bound" ])




		class Stone(Transmutable):
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_ten_ct
						init_name	= "mci_ten_ct-2"
						init_level	= 10

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_ten_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ten_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ten_ct-2-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_ten_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_ten_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= mci_ten_ct
							init_name		= "mci_ten_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_ten_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		self.test_case.loggy.close()

		with open(mci_ten_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])
		if	os.path.isfile(mci_ten_ct): os.remove(mci_ten_ct)








	def test_mutable_chain_injection_triple_no_loggy_controlled_transmutation(self):
		class Stone(Transmutable):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(Transmutable):	pass
			class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertEqual(self.test_case.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(Transmutable):	pass
				class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(Transmutable):
					class Bound(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_mixed_controlled_transmutation(self):

		mci_m_ct = str(self.MAGICAL_ROOT /"mci_m_ct.loggy")
		self.make_loggy_file(mci_m_ct)


		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_m_ct
				init_name	= "mci_m_ct-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_m_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_m_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_m_ct
				init_name	= "mci_m_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_m_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_m_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_m_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_m_ct
				init_name		= "mci_m_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				@StoneControlledMutationCase.Patogen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_m_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_m_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_m_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_m_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_m_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_m_ct): os.remove(mci_m_ct)








	def test_mutable_chain_injection_mixed_name_controlled_transmutation(self):

		mci_mn_ct = str(self.MAGICAL_ROOT /"mci_mn_ct.loggy")
		self.make_loggy_file(mci_mn_ct)


		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_mn_ct
				init_name	= "mci_mn_ct-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_mn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_mn_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_mn_ct
				init_name	= "mci_mn_ct-2"
				init_level	= 10

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_mn_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_mn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_mn_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_mn_ct
				init_name		= "mci_mn_ct-3"
				force_handover	= True

			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				@StoneControlledMutationCase.Patogen
				class Paint(Transmutable):	pass


		loggy = []
		self.make_loggy_file(mci_mn_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_mn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_mn_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_mn_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_mn_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_mn_ct): os.remove(mci_mn_ct)








	def test_mutable_chain_injection_mixed_escalated_controlled_transmutation(self):

		mci_me_ct = str(self.MAGICAL_ROOT /"mci_me_ct.loggy")
		self.make_loggy_file(mci_me_ct)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_me_ct
					init_name	= "mci_me_ct-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_me_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_me_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Handle(Transmutable):

				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_me_ct
						init_name	= "mci_me_ct-2"
						init_level	= 10


		loggy = []
		self.make_loggy_file(mci_me_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_me_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_me_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_me_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				@StoneControlledMutationCase.Patogen
				class Paint(Transmutable):

					class Bound(Transmutable):
						class loggy(LibraryContrib):

							handler			= mci_me_ct
							init_name		= "mci_me_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_me_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		if	os.path.isfile(mci_me_ct): os.remove(mci_me_ct)








	def test_mutable_chain_injection_mixed_escalated_name_controlled_transmutation(self):

		mci_men_ct = str(self.MAGICAL_ROOT /"mci_men_ct.loggy")
		self.make_loggy_file(mci_men_ct)


		class Stone(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_men_ct
					init_name	= "mci_men_ct-1"

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_men_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_men_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Stone(Transmutable):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):	pass
			class Handle(Transmutable):

				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_men_ct
						init_name	= "mci_men_ct-2"
						init_level	= 10


		loggy = []
		self.make_loggy_file(mci_men_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_men_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_men_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_men_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				@StoneControlledMutationCase.Patogen
				class Paint(Transmutable):

					class Bound(Transmutable):
						class shmoggy(LibraryContrib):

							handler			= mci_men_ct
							init_name		= "mci_men_ct-3"
							force_handover	= True


		loggy = []
		self.make_loggy_file(mci_men_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
		if	os.path.isfile(mci_men_ct): os.remove(mci_men_ct)








	def test_mutable_chain_injection_mixed_no_loggy_controlled_transmutation(self):

		class Stone(Transmutable):
			class Bound(Transmutable):	pass

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))




		class Stone(Transmutable):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Mutagen("red", operation="turned")
			class Paint(Transmutable):		pass
			class Handle(Transmutable):

				class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertEqual(self.test_case.Handle.loggy.warning("I am just a handle"), NotImplemented)
		self.assertEqual(self.test_case.Handle.Bound.loggy.info("I am bound"), NotImplemented)




		class Stone(Transmutable):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Mutagen("red", operation="turned")
				@StoneControlledMutationCase.Patogen
				class Paint(Transmutable):

					class Bound(Transmutable):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_top_layer_controlled_transmutation(self):

		mci_tl_ct = str(self.MAGICAL_ROOT /"mci_tl_ct.loggy")
		self.make_loggy_file(mci_tl_ct)


		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_ct
				init_name	= "mci_tl_ct-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)
		if	os.path.isfile(mci_tl_ct): os.remove(mci_tl_ct)
















	def test_mutable_chain_injection_top_layer_loaded_controlled_transmutation(self):

		mci_tl_l_ct = str(self.MAGICAL_ROOT /"mci_tl_l_ct.loggy")
		self.make_loggy_file(mci_tl_l_ct)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_l_ct
				init_name	= "mci_tl_l_ct-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_l_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Mutabor("Today")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_l_ct
				init_name	= "mci_tl_l_ct-2"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_l_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Mutabor("Today")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)
		if	os.path.isfile(mci_tl_l_ct): os.remove(mci_tl_l_ct)
















	def test_mutable_chain_injection_top_layer_double_controlled_transmutation(self):

		mci_tl_d_ct = str(self.MAGICAL_ROOT /"mci_tl_d_ct.loggy")
		self.make_loggy_file(mci_tl_d_ct)


		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_d_ct
				init_name	= "mci_tl_d_ct-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_d_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Antibor("Today")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_d_ct
				init_name	= "mci_tl_d_ct-2"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_d_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_d_ct
				init_name	= "mci_tl_d_ct-3"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_d_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Antibor("Today")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)
		if	os.path.isfile(mci_tl_d_ct): os.remove(mci_tl_d_ct)
















	def test_mutable_chain_injection_top_layer_triple_controlled_transmutation(self):

		mci_tl_t_ct = str(self.MAGICAL_ROOT /"mci_tl_t_ct.loggy")
		self.make_loggy_file(mci_tl_t_ct)


		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Pathogen
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_t_ct
				init_name	= "mci_tl_t_ct-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_t_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Pathogen
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_t_ct
				init_name	= "mci_tl_t_ct-2"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_t_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Pathogen
		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_t_ct
				init_name	= "mci_tl_t_ct-3"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_t_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Pathogen
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Pathogen
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Pathogen
		@StoneControlledMutationCase.Antibor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)
		if	os.path.isfile(mci_tl_t_ct): os.remove(mci_tl_t_ct)
















	def test_mutable_chain_injection_top_layer_mixed_controlled_transmutation(self):

		mci_tl_m_ct = str(self.MAGICAL_ROOT /"mci_tl_m_ct.loggy")
		self.make_loggy_file(mci_tl_m_ct)


		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_m_ct
				init_name	= "mci_tl_m_ct-1"


		loggy = []
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_m_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_m_ct
				init_name	= "mci_tl_m_ct-2"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_m_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):

			class loggy(LibraryContrib):

				handler		= mci_tl_m_ct
				init_name	= "mci_tl_m_ct-3"


		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)

		with open(mci_tl_m_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		@StoneControlledMutationCase.Patogen
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)




		@StoneControlledMutationCase.Patogen
		@StoneControlledMutationCase.Mutabor("Today")
		@StoneControlledMutationCase.Antigen("red", operation="turned")
		class Stone(StoneControlledMutationCase.PaintBrash):	pass
		self.assertRaisesRegex(

			TypeError,
			"Not Transmutable transmutation",
			Stone
		)
		if	os.path.isfile(mci_tl_m_ct): os.remove(mci_tl_m_ct)
















	def test_mutable_chain_injection_outer_controlled_transmutation(self):

		mci_o_ct = str(self.MAGICAL_ROOT /"mci_o_ct.loggy")
		self.make_loggy_file(mci_o_ct)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_o_ct
				init_name	= "mci_o_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_o_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_o_ct
				init_name	= "mci_o_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_o_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_o_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_o_ct
				init_name		= "mci_o_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_o_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_o_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_o_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_o_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_o_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_o_ct): os.remove(mci_o_ct)








	def test_mutable_chain_injection_outer_name_controlled_transmutation(self):

		mci_on_ct = str(self.MAGICAL_ROOT /"mci_on_ct.loggy")
		self.make_loggy_file(mci_on_ct)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_on_ct
				init_name	= "mci_on_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_on_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_on_ct
				init_name	= "mci_on_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_on_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_on_ct
				init_name		= "mci_on_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_on_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_on_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_on_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_on_ct): os.remove(mci_on_ct)








	def test_mutable_chain_injection_outer_escalated_controlled_transmutation(self):

		mci_oe_ct = str(self.MAGICAL_ROOT /"mci_oe_ct.loggy")
		self.make_loggy_file(mci_oe_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_oe_ct
					init_name	= "mci_oe_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_oe_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_oe_ct
						init_name	= "mci_oe_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oe_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oe_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_oe_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_oe_ct
					init_name		= "mci_oe_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_oe_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oe_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oe_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_oe_ct-3-Stone INFO : I am root",
				"@mci_oe_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_oe_ct): os.remove(mci_oe_ct)








	def test_mutable_chain_injection_outer_escalated_name_controlled_transmutation(self):

		mci_oen_ct = str(self.MAGICAL_ROOT /"mci_oen_ct.loggy")
		self.make_loggy_file(mci_oen_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_oen_ct
					init_name	= "mci_oen_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_oen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_oen_ct
						init_name	= "mci_oen_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oen_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_oen_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_oen_ct
					init_name		= "mci_oen_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_oen_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oen_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_oen_ct-3-Stone INFO : I am root",
				"@mci_oen_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_oen_ct): os.remove(mci_oen_ct)








	def test_mutable_chain_injection_outer_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_outer_loaded_controlled_transmutation(self):

		mci_ol_ct = str(self.MAGICAL_ROOT /"mci_ol_ct.loggy")
		self.make_loggy_file(mci_ol_ct)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ol_ct
				init_name	= "mci_ol_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ol_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ol_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ol_ct
				init_name	= "mci_ol_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Mutabor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ol_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ol_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ol_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_ol_ct
				init_name		= "mci_ol_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ol_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ol_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ol_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_ol_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ol_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_ol_ct): os.remove(mci_ol_ct)








	def test_mutable_chain_injection_outer_loaded_name_controlled_transmutation(self):

		mci_oln_ct = str(self.MAGICAL_ROOT /"mci_oln_ct.loggy")
		self.make_loggy_file(mci_oln_ct)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_oln_ct
				init_name	= "mci_oln_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_oln_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_oln_ct
				init_name	= "mci_oln_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Mutabor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_oln_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_oln_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_oln_ct
				init_name		= "mci_oln_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_oln_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_oln_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oln_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_oln_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_oln_ct): os.remove(mci_oln_ct)








	def test_mutable_chain_injection_outer_loaded_escalated_controlled_transmutation(self):

		mci_ole_ct = str(self.MAGICAL_ROOT /"mci_ole_ct.loggy")
		self.make_loggy_file(mci_ole_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ole_ct
					init_name	= "mci_ole_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ole_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_ole_ct
						init_name	= "mci_ole_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Mutabor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ole_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ole_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_ole_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_ole_ct
					init_name		= "mci_ole_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ole_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ole_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ole_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ole_ct-3-Stone INFO : I am root",
				"@mci_ole_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_ole_ct): os.remove(mci_ole_ct)








	def test_mutable_chain_injection_outer_loaded_escalated_name_controlled_transmutation(self):

		mci_olen_ct = str(self.MAGICAL_ROOT /"mci_olen_ct.loggy")
		self.make_loggy_file(mci_olen_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_olen_ct
					init_name	= "mci_olen_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_olen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_olen_ct
						init_name	= "mci_olen_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Mutabor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_olen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_olen_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_olen_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_olen_ct
					init_name		= "mci_olen_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_olen_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_olen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_olen_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_olen_ct-3-Stone INFO : I am root",
				"@mci_olen_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_olen_ct): os.remove(mci_olen_ct)








	def test_mutable_chain_injection_outer_loaded_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Mutabor("Today")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_outer_double_controlled_transmutation(self):

		mci_od_ct = str(self.MAGICAL_ROOT /"mci_od_ct.loggy")
		self.make_loggy_file(mci_od_ct)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_od_ct
				init_name	= "mci_od_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_od_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_od_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_od_ct
				init_name	= "mci_od_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_od_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_od_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_od_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_od_ct
				init_name		= "mci_od_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_od_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_od_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_od_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_od_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_od_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_od_ct): os.remove(mci_od_ct)








	def test_mutable_chain_injection_outer_double_name_controlled_transmutation(self):

		mci_odn_ct = str(self.MAGICAL_ROOT /"mci_odn_ct.loggy")
		self.make_loggy_file(mci_odn_ct)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_odn_ct
				init_name	= "mci_odn_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_odn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_odn_ct
				init_name	= "mci_odn_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_odn_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_odn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_odn_ct
				init_name		= "mci_odn_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_odn_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_odn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_odn_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_odn_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_odn_ct): os.remove(mci_odn_ct)








	def test_mutable_chain_injection_outer_double_escalated_controlled_transmutation(self):

		mci_ode_ct = str(self.MAGICAL_ROOT /"mci_ode_ct.loggy")
		self.make_loggy_file(mci_ode_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ode_ct
					init_name	= "mci_ode_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ode_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_ode_ct
						init_name	= "mci_ode_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ode_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ode_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_ode_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_ode_ct
					init_name		= "mci_ode_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ode_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ode_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ode_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ode_ct-3-Stone INFO : I am root",
				"@mci_ode_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_ode_ct): os.remove(mci_ode_ct)








	def test_mutable_chain_injection_outer_double_escalated_name_controlled_transmutation(self):

		mci_oden_ct = str(self.MAGICAL_ROOT /"mci_oden_ct.loggy")
		self.make_loggy_file(mci_oden_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_oden_ct
					init_name	= "mci_oden_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_oden_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_oden_ct
						init_name	= "mci_oden_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Antibor("Today")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oden_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oden_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_oden_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_oden_ct
					init_name		= "mci_oden_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_oden_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oden_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oden_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_oden_ct-3-Stone INFO : I am root",
				"@mci_oden_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_oden_ct): os.remove(mci_oden_ct)








	def test_mutable_chain_injection_outer_double_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Antibor("Today")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_outer_triple_controlled_transmutation(self):

		mci_ot_ct = str(self.MAGICAL_ROOT /"mci_ot_ct.loggy")
		self.make_loggy_file(mci_ot_ct)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ot_ct
				init_name	= "mci_ot_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ot_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ot_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_ot_ct
				init_name	= "mci_ot_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ot_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ot_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ot_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_ot_ct
				init_name		= "mci_ot_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ot_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_ot_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ot_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_ot_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ot_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_ot_ct): os.remove(mci_ot_ct)








	def test_mutable_chain_injection_outer_triple_name_controlled_transmutation(self):

		mci_otn_ct = str(self.MAGICAL_ROOT /"mci_otn_ct.loggy")
		self.make_loggy_file(mci_otn_ct)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_otn_ct
				init_name	= "mci_otn_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_otn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_otn_ct
				init_name	= "mci_otn_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_otn_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_otn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_otn_ct
				init_name		= "mci_otn_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_otn_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_otn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_otn_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_otn_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_otn_ct): os.remove(mci_otn_ct)








	def test_mutable_chain_injection_outer_triple_escalated_controlled_transmutation(self):

		mci_ote_ct = str(self.MAGICAL_ROOT /"mci_ote_ct.loggy")
		self.make_loggy_file(mci_ote_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ote_ct
					init_name	= "mci_ote_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ote_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_ote_ct
						init_name	= "mci_ote_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ote_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ote_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_ote_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_ote_ct
					init_name		= "mci_ote_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ote_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ote_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ote_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ote_ct-3-Stone INFO : I am root",
				"@mci_ote_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_ote_ct): os.remove(mci_ote_ct)








	def test_mutable_chain_injection_outer_triple_escalated_name_controlled_transmutation(self):

		mci_oten_ct = str(self.MAGICAL_ROOT /"mci_oten_ct.loggy")
		self.make_loggy_file(mci_oten_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_oten_ct
					init_name	= "mci_oten_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Pathogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_oten_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_oten_ct
						init_name	= "mci_oten_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Antibor("Today")
			@StoneControlledMutationCase.Pathogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oten_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oten_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_oten_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_oten_ct
					init_name		= "mci_oten_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_oten_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_oten_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_oten_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_oten_ct-3-Stone INFO : I am root",
				"@mci_oten_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_oten_ct): os.remove(mci_oten_ct)








	def test_mutable_chain_injection_outer_triple_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Pathogen
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)





		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Pathogen
				@StoneControlledMutationCase.Antibor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)
















	def test_mutable_chain_injection_outer_mixed_controlled_transmutation(self):

		mci_om_ct = str(self.MAGICAL_ROOT /"mci_om_ct.loggy")
		self.make_loggy_file(mci_om_ct)


		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_om_ct
				init_name	= "mci_om_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_om_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_om_ct-1 ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler		= mci_om_ct
				init_name	= "mci_om_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_om_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_om_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_om_ct-2-Stone ERROR : Paint nesting caused TypeError: Not Transmutable transmutation",
			]
		)




		class Outdoor(Transmutable):
			class loggy(LibraryContrib):

				handler			= mci_om_ct
				init_name		= "mci_om_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_om_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_om_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_om_ct-3-Stone.Handle ERROR : Paint nesting caused TypeError: "
				"Not Transmutable transmutation",
				"@mci_om_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_om_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_om_ct): os.remove(mci_om_ct)








	def test_mutable_chain_injection_outer_mixed_name_controlled_transmutation(self):

		mci_omn_ct = str(self.MAGICAL_ROOT /"mci_omn_ct.loggy")
		self.make_loggy_file(mci_omn_ct)


		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_omn_ct
				init_name	= "mci_omn_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_omn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler		= mci_omn_ct
				init_name	= "mci_omn_ct-2"
				init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_omn_ct)
		self.test_case = Stone()
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_omn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class shmoggy(LibraryContrib):

				handler			= mci_omn_ct
				init_name		= "mci_omn_ct-3"
				force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_omn_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.test_case.loggy.close()

		with open(mci_omn_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_omn_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_omn_ct-3-Stone INFO : I am root",
			]
		)
		if	os.path.isfile(mci_omn_ct): os.remove(mci_omn_ct)








	def test_mutable_chain_injection_outer_mixed_escalated_controlled_transmutation(self):

		mci_ome_ct = str(self.MAGICAL_ROOT /"mci_ome_ct.loggy")
		self.make_loggy_file(mci_ome_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler		= mci_ome_ct
					init_name	= "mci_ome_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_ome_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class loggy(LibraryContrib):

						handler		= mci_ome_ct
						init_name	= "mci_ome_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ome_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ome_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_ome_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class loggy(LibraryContrib):

					handler			= mci_ome_ct
					init_name		= "mci_ome_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_ome_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_ome_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_ome_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_ome_ct-3-Stone INFO : I am root",
				"@mci_ome_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_ome_ct): os.remove(mci_ome_ct)








	def test_mutable_chain_injection_outer_mixed_escalated_name_controlled_transmutation(self):

		mci_omen_ct = str(self.MAGICAL_ROOT /"mci_omen_ct.loggy")
		self.make_loggy_file(mci_omen_ct)


		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler		= mci_omen_ct
					init_name	= "mci_omen_ct-1"

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			@StoneControlledMutationCase.Patogen
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.test_case.loggy.close()

		with open(mci_omen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(loggy,[])




		class Outdoor(Transmutable):
			class Handle(Transmutable):
				class Bound(Transmutable):
					class shmoggy(LibraryContrib):

						handler		= mci_omen_ct
						init_name	= "mci_omen_ct-2"
						init_level	= 10

		class Stone(Outdoor):

			@StoneControlledMutationCase.Mutabor("Today")
			@StoneControlledMutationCase.Patogen
			@StoneControlledMutationCase.Antigen("red", operation="turned")
			class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertTrue(hasattr(self.test_case.Handle, "Bound"))
		self.assertFalse(hasattr(self.test_case, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.warning("I am just a handle"))
		self.assertIsNone(self.test_case.Handle.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_omen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_omen_ct-2-Stone.Handle WARNING : I am just a handle",
				"@mci_omen_ct-2-Stone.Handle.Bound INFO : I am bound",
			]
		)




		class Outdoor(Transmutable):
			class Bound(Transmutable):
				class shmoggy(LibraryContrib):

					handler			= mci_omen_ct
					init_name		= "mci_omen_ct-3"
					force_handover	= True

		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		loggy = []
		self.make_loggy_file(mci_omen_ct)
		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Bound"))
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertIsNone(self.test_case.Handle.loggy.error("This stone is uncontrollable!"))
		self.assertIsNone(self.test_case.loggy.info("I am root"))
		self.assertIsNone(self.test_case.Bound.loggy.info("I am bound"))
		self.test_case.loggy.close()

		with open(mci_omen_ct) as case_loggy:
			for line in case_loggy : loggy.append(line.rstrip("\n")[16:])

		self.assertEqual(

			loggy,
			[
				"@mci_omen_ct-3-Stone.Handle ERROR : This stone is uncontrollable!",
				"@mci_omen_ct-3-Stone INFO : I am root",
				"@mci_omen_ct-3-Stone.Bound INFO : I am bound",
			]
		)
		if	os.path.isfile(mci_omen_ct): os.remove(mci_omen_ct)








	def test_mutable_chain_injection_outer_mixed_no_loggy_controlled_transmutation(self):

		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				@StoneControlledMutationCase.Patogen
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)





		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)




		class Outdoor(Transmutable):	pass
		class Stone(Outdoor):
			class Handle(Transmutable):

				@StoneControlledMutationCase.Patogen
				@StoneControlledMutationCase.Mutabor("Today")
				@StoneControlledMutationCase.Antigen("red", operation="turned")
				class Paint(StoneControlledMutationCase.PaintBrash):	pass


		self.test_case = Stone()
		self.assertTrue(hasattr(self.test_case, "Handle"))
		self.assertFalse(hasattr(self.test_case.Handle, "Paint"))
		self.assertEqual(self.test_case.Handle.loggy.error("This stone is uncontrollable!"), NotImplemented)
		self.assertEqual(self.test_case.loggy.info("I am root"), NotImplemented)








if __name__ == "__main__" : unittest.main(verbosity=2)







