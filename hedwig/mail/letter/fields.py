from os								import path as ospath
from typing							import Optional
from typing							import Callable
from pygwarts.magical.spells		import patronus
from pygwarts.hedwig.mail.letter	import AddressField
from pygwarts.hedwig.mail.letter	import StringField
from pygwarts.hedwig.mail.letter	import TextField








class SenderField(AddressField):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.make_field("sender")


class RecipientField(AddressField):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.make_field("recipient")


class ccField(AddressField):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.make_field("cc")


class bccField(AddressField):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.make_field("bcc")


class SubjectField(TextField):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.make_field("subject")


class BodyField(TextField):
	def __init__(self, *args, **kwargs):

		super().__init__(*args, **kwargs)
		self.make_field("body")








class AttachmentField(StringField):

	"""
		hedwig.mail optional letter field class that implements handling of attachment files. It is a
		substantive letter field, which main purpose is to obtain a string "field_value", which normally
		must represent the attachment file path, verify it points to a real file and return it, so the
		letter builder will be able to attach it to the letter. Optional "modifiers" callable might
		accept "field_value" in order to make some processing beforehand and return the final file path.
		If any Exception will be raised when "modifiers" is called, it will be logged and original
		"field_value" will be considered as a final file path, means it will be the subject for
		verification. This is crucial moment for "modifiers", as if provided it will first intercept
		"field_value", so e.g. "field_value" might originally be not a real file path but some string,
		which when fed to a "modifiers" will output the real file path, may be even made by "modifiers".
		So it must be accounted that if such manipulation will fail, the original non-file "field_value"
		will not pass verification and no attachment will be provided. The other important thing about
		"modifiers" is that all files manipulation it does goes in letter construction time, so after if
		the letter builder will eventually fail, the impact to file system made by "modifiers" will stay.
		If final string will not pass the verification, or "field_value" is invalid, None will be returned.
	"""


	field_value	:str
	modifiers	:Optional[Callable[[str],str]]


	def __init__(self, *args, **kwargs):


		super().__init__(*args, **kwargs)
		self.make_field("attachment")


	def __call__(self) -> str | None :


		if	(field := super().__call__()) is not None:
			if	callable(getattr(self, "modifiers", None)):


				# As "modifiers" will be invoked as a member, it assumed current object reference will
				# be implicitly passed as a first argument to "modifiers", along with the "field_value"
				# as a second argument. Due to such particularity, any "modifiers" that are not supposed
				# initially as a member, e.g. lambda functions, must account to, in better way, gather
				# all arguments and process only the last one.
				try:	final_field = self.modifiers(field)
				except	Exception as E:

					self.loggy.error(f"AttachmentField {self} field failed due to {patronus(E)}")
					final_field = field
			else:

				self.loggy.debug("Modifiers not used")
				final_field = field

			if	ospath.isfile(final_field):

				self.loggy.debug(f"Obtained file path \"{final_field}\"")
				return final_field

			self.loggy.info(f"{self} cannot attach non-existent file \"{final_field}\"")







