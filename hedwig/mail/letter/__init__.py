from typing									import Any
from typing									import Dict
from typing									import Literal
from typing									import Optional
from typing									import Sequence
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import flagrate
from pygwarts.magical.spells				import patronus
from pygwarts.hedwig.mail.builder			import LetterBuilder
from pygwarts.hedwig.mail.utils				import EmailValidator








class ObjectField(Transmutable):

	"""
		hedwig.mail core super class that is the base for a letter building. Represents the object
		model that will maintains some "field_value", which is obtainable via __call__, and has the
		ability to put itself in the upper layer LetterBuilder object, as a mapping of some special
		name for current "field_value" to itself. The optional field "modifiers" might be any type
		and might serve as some modifier for a "field_value" or just as some another value to be used
		somehow. Current super class __call__ defines the basic behavior for any field that will inherit,
		that it suggest the safety way to obtain "field_value". Any ObjectField child is supposed to
		maintain it's "field_value" the same way and implement the same interface. Any ObjectField
		child as a letter field might be represented multiple times, as "make_field" method handles.
	"""


	field_value	:Any
	modifiers	:Optional[Any]


	def __call__(self) -> Any :

		if	hasattr(self, "field_value"):
			self.loggy.debug(f"Fetched value of {type(self.field_value)}")

			return	self.field_value
		else:		self.loggy.error(f"Field {self} must have value")


	def make_field(self, field_name :str) -> Literal[True] | None :

		"""
			Core method for all letter's fields functionality, that implements mapping of fields
			for building the letter. Must be called with "field_name" string value that will be used
			as a key for mapping with the object itself. The current field object must be declared
			directly under LetterBuilder class, so this method will be able to do actual mapping in
			upper layer KeyChest. By default, if upper layer KeyChest does not content any mapping
			for "field_name" yet, actual mapping will be the list that will content current field
			object. Any further invocations of "make_field" for different field object, but with
			the same "field_name" will cause mapped list population. This allows multiple values
			to be obtained for a mapped "field_name" once the LetterBuilder object will build letter.
			Returns True if mapping was successfully made for current object, or None otherwise.
		"""

		if	isinstance(field_name, str):
			if	hasattr(self, "_UPPER_LAYER"):
				if	isinstance(self._UPPER_LAYER, LetterBuilder):


					match self._UPPER_LAYER[field_name]:

						case None:		self._UPPER_LAYER[field_name] = [ self ]
						case list():	self._UPPER_LAYER[field_name].append(self)
						case _:

							self.loggy.error(f"{self._UPPER_LAYER} {field_name} field is busy")
							return
					return	True


				else:	self.loggy.debug(f"Improper builder {self._UPPER_LAYER}")
			else:		self.loggy.debug("Builder not found")
		else:			self.loggy.debug(f"Field name \"{field_name}\" must be a string")








class StringField(ObjectField):

	"""
		hedwig.mail core super class, that is a child of ObjectField, that implements maintaining of only
		"field_value" of type string. In __call__ obtained "field_value" will be checked to be a string,
		so to be returned. Otherwise None will be returned with corresponding log message. This type of
		letter field is more subjective than ObjectField, but still general, as the original design of
		hedwig letter building does not assumes any substantive field in letter to be a simple string,
		but instead there are default fields that are constructed upon StringField:
			TextField and AttachmentField.
	"""

	field_value	:str

	def __call__(self) -> str | None :

		if	(current_value := super().__call__()) is not None:
			if	isinstance(current_value, str):

				flen = len(self.field_value)
				self.loggy.debug(f"Fetched {flen} symbol{flagrate(flen)}")


				return	self.field_value


			else:	self.loggy.error(f"Field {self} value must be string")
		else:		self.loggy.debug(f"No value fetched for field")








class TextField(StringField):

	"""
		hedwig.mail core class that is a child of StringField and is a super class for key-word formatted
		letter's text fields, like substantive SubjectField and BodyField. After obtaining "field_value"
		as a string, will try to apply "modifiers", which must be a dictionary with format-keys strings
		mapped with desired strings. Either "modifiers" are not provided, or successfully applied, returns
		the final string value. For any other case, like invalid or absent "field_value" or if "modifiers"
		failed, None will be returned. This is important to note once again, that if "modifiers" applying
		failed, the original "field_value" string will not be returned.
	"""

	modifiers	:Optional[Dict[str,str]]

	def __call__(self) -> str | None :

		if	(field := super().__call__()) is not None:
			if	isinstance(getattr(self, "modifiers", None), dict):


				try:	final_field = field.format(**self.modifiers)
				except	Exception as E:

					self.loggy.error(f"{self} field failed due to {patronus(E)}")
					return
			else:
				self.loggy.debug("Proper modifiers not found")
				final_field = field


			flen = len(final_field)
			self.loggy.debug(f"Obtained {flen} symbol{flagrate(flen)}")


			return	final_field








class AddressField(ObjectField):

	"""
		hedwig.mail core super class for a email address form of letter fields. Obtained "field_value"
		must be either a single address string, or a bunch of addresses either as a semicolon separated
		string or a sequence of strings (any iterable). In first case, when "field_value" is a string,
		it will be converted to a list of strings by splitting with semicolon. All addresses will be putted
		to a "validator" callable, which is mandatory and must return boolean to decide whether address is
		valid or not. Validated addresses will be gathered and joined as semicolon separated string, which
		is suitable for any recipient like letter fields, but not for sender field, so multiple senders
		must be supplied by multiple fields. Returns joined addresses string in case of at least one
		address was validated. Otherwise, when "field_value" is invalid, or by some Exception that raised
		and logged during iterating over "field_value" or in "validator" call for any address, None will
		be returned. Is a super class for a substantive letter fields like:
			SenderField
			RecipientField
			ccField
			bccField
	"""


	field_value	:str | Sequence[str]
	validator	:EmailValidator


	def __call__(self) -> str | None :


		if	(field := super().__call__()) is not None:
			if	callable(getattr(self, "validator", None)) and not (final_field := list()):


				# At this point callable "validator" is accessible and "field" value might be either
				# a string that content already semicolon separated recipients (or a single recipient),
				# or some other value, which must be an iterable with email addresses as strings. In both
				# situations every email must be validated and then joined back together as final field.
				if	isinstance(field, str): field = ( email.strip() for email in field.split(";") if email )
				try:
					for email in field:
						if	self.validator(email) : final_field.append(email)

				except	Exception as E:

					self.loggy.error(f"{self} field failed due to {patronus(E)}")
				else:
					if	(flen := len(final_field)):

						self.loggy.info(f"{self} obtained {flen} email{flagrate(flen)}")
						return	";".join(final_field) + ";"


					else:	self.loggy.info(f"{self} field has no valid addresses")
			else:			self.loggy.info(f"{self} cannot validate email address")







