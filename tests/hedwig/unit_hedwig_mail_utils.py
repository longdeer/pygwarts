import	os
import	unittest
from	typing								import Any
from 	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.spells				import flagrate
from	pygwarts.hedwig.mail.letter			import ObjectField
from	pygwarts.hedwig.mail.letter			import StringField
from	pygwarts.hedwig.mail.letter			import TextField
from	pygwarts.hedwig.mail.letter			import AddressField
from	pygwarts.hedwig.mail.letter.fields	import SenderField
from	pygwarts.hedwig.mail.letter.fields	import RecipientField
from	pygwarts.hedwig.mail.letter.fields	import ccField
from	pygwarts.hedwig.mail.letter.fields	import bccField
from	pygwarts.hedwig.mail.letter.fields	import SubjectField
from	pygwarts.hedwig.mail.letter.fields	import BodyField
from	pygwarts.hedwig.mail.utils			import EMAIL_REGEX_PATTERN
from	pygwarts.hedwig.mail.utils			import EmailValidator
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access.utils			import TextWrapper
from	pygwarts.tests.hedwig				import HedwigTestCase








class MailUtilsCases(HedwigTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.HEDWIG_MAIL_UTILS_HANDLER):

				cls.email_validator.loggy.close()
				os.remove(cls.HEDWIG_MAIL_UTILS_HANDLER)

	@classmethod
	def setUpClass(cls):

		class CurrentValidator(EmailValidator):
			class loggy(LibraryContrib):

				handler		= cls.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "EmailValidator"
				init_level	= 10
		cls.email_validator = CurrentValidator()
		cls.make_loggy_file(cls, cls.HEDWIG_MAIL_UTILS_HANDLER)


	def test_EMAIL_REGEX_PATTERN_valid(self):

		for address in self.VALID_EMAILS : self.assertTrue(EMAIL_REGEX_PATTERN.fullmatch(address))

	def test_EMAIL_REGEX_PATTERN_invalid(self):

		for address in self.INVALID_EMAILS : self.assertIsNone(EMAIL_REGEX_PATTERN.fullmatch(address))

	def test_EmailValidator_valid(self):

		for address in self.VALID_EMAILS:

			with self.subTest(email=address):
				with self.assertLogs("EmailValidator", 10) as case_loggy:

					self.assertTrue(self.email_validator(address))
				self.assertIn(
					f"DEBUG:EmailValidator:Email address \"{address}\" validated", case_loggy.output
				)


	def test_EmailValidator_invalid(self):

		for address in (

			*self.INVALID_EMAILS,
			1, 1., 1E1, True, False, None, ..., print, type,
			[ "email@example.com" ],
			( "email@example.com", ),
			{ "email@example.com" },
			{ "email": "email@example.com" },
		):
			with self.subTest(email=address):
				with self.assertLogs("EmailValidator", 20) as case_loggy:

					self.assertFalse(self.email_validator(address))
				self.assertIn(f"INFO:EmailValidator:Invalid email address \"{address}\"", case_loggy.output)








	def test_TextWrapper_Transmutable(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(Transmutable):

			def __call__(self): return "generated text"
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_Transmutable"
				init_level	= 10

		with self.assertLogs("TextWrapper_Transmutable", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),1)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn("DEBUG:TextWrapper_Transmutable:Wrapped text now 29 symbols", case_loggy.output)
		self.assertEqual(current, "this is generated text, baby!")




	def test_TextWrapper_Transmutable_args(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(Transmutable):

			def __call__(self, what :Any): return f"generated {what}"
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_Transmutable_args"
				init_level	= 10

		self.test_case = TextGenerator()
		for arg in (

			"text",( "text", ),[ "text" ],{ "text" },{ "what": "text" },
			None, print, ..., 1, .1, True, False, Transmutable, self.test_case
		):
			with self.subTest(arg=arg):
				with self.assertLogs("TextWrapper_Transmutable_args", 10) as case_loggy:

					current = self.test_case(arg)

				L = len(current)
				self.assertEqual(len(case_loggy.output),1)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(

					f"DEBUG:TextWrapper_Transmutable_args:Wrapped text now {L} symbol{flagrate(L)}",
					case_loggy.output
				)
				self.assertEqual(current, f"this is generated {arg}, baby!")




	def test_TextWrapper_Transmutable_invalid_args(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(Transmutable):

			def __call__(self, what :Any): return what
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "Transmutable_invalid_args"
				init_level	= 10

		self.test_case = TextGenerator()
		for arg in (

			( "text", ),[ "text" ],{ "text" },{ "what": "text" },
			None, print, ..., 1, .1, True, False, Transmutable, self.test_case
		):
			with self.subTest(arg=arg):
				with self.assertLogs("Transmutable_invalid_args", 10) as case_loggy:

					current = self.test_case(arg)

				self.assertEqual(len(case_loggy.output),1)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(

					f"DEBUG:Transmutable_invalid_args:Text value to wrap not found",
					case_loggy.output
				)
				self.assertIsNone(current)








	def test_TextWrapper_ObjectField(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(ObjectField):

			field_value = "generated text"
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_ObjectField"
				init_level	= 10

		with self.assertLogs("TextWrapper_ObjectField", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(f"DEBUG:TextWrapper_ObjectField:Fetched value of {type('')}", case_loggy.output)
		self.assertIn("DEBUG:TextWrapper_ObjectField:Wrapped text now 29 symbols", case_loggy.output)
		self.assertEqual(current, "this is generated text, baby!")




	def test_TextWrapper_ObjectField_fail(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(ObjectField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_ObjectField_fail"
				init_level	= 10

		with self.assertLogs("TextWrapper_ObjectField_fail", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertIn(
			f"ERROR:TextWrapper_ObjectField_fail:Field {self.test_case} must have value", case_loggy.output
		)
		self.assertIn("DEBUG:TextWrapper_ObjectField_fail:Text value to wrap not found", case_loggy.output)
		self.assertIsNone(current)








	def test_TextWrapper_StringField(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(StringField):

			field_value = "generated text"
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_StringField"
				init_level	= 10

		with self.assertLogs("TextWrapper_StringField", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),3)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(f"DEBUG:TextWrapper_StringField:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:TextWrapper_StringField:Fetched 14 symbols", case_loggy.output)
		self.assertIn("DEBUG:TextWrapper_StringField:Wrapped text now 29 symbols", case_loggy.output)
		self.assertEqual(current, "this is generated text, baby!")




	def test_TextWrapper_StringField_fail(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(StringField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_StringField_fail"
				init_level	= 10

		with self.assertLogs("TextWrapper_StringField_fail", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),3)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertIn(
			f"ERROR:TextWrapper_StringField_fail:Field {self.test_case} must have value", case_loggy.output
		)
		self.assertIn(f"DEBUG:TextWrapper_StringField_fail:No value fetched for field", case_loggy.output)
		self.assertIn("DEBUG:TextWrapper_StringField_fail:Text value to wrap not found", case_loggy.output)
		self.assertIsNone(current)








	def test_TextWrapper_TextField(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(TextField):

			field_value = "generated text"
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_TextField"
				init_level	= 10

		with self.assertLogs("TextWrapper_TextField", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),5)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(f"DEBUG:TextWrapper_TextField:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:TextWrapper_TextField:Fetched 14 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:TextWrapper_TextField:Proper modifiers not found", case_loggy.output)
		self.assertIn(f"DEBUG:TextWrapper_TextField:Obtained 14 symbols", case_loggy.output)
		self.assertIn("DEBUG:TextWrapper_TextField:Wrapped text now 29 symbols", case_loggy.output)
		self.assertEqual(current, "this is generated text, baby!")




	def test_TextWrapper_TextField_modifiers(self):

		@TextWrapper("this is ", ", baby!")
		class TextGenerator(TextField):

			field_value	= "generated {what}"
			modifiers	= { "what": "text" }
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_TextField_modifiers"
				init_level	= 10

		with self.assertLogs("TextWrapper_TextField_modifiers", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),4)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(f"DEBUG:TextWrapper_TextField_modifiers:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:TextWrapper_TextField_modifiers:Fetched 16 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:TextWrapper_TextField_modifiers:Obtained 14 symbols", case_loggy.output)
		self.assertIn("DEBUG:TextWrapper_TextField_modifiers:Wrapped text now 29 symbols", case_loggy.output)
		self.assertEqual(current, "this is generated text, baby!")




	def test_TextWrapper_TextField_fail(self):

		@TextWrapper(header="this is ", footer=", baby!")
		class TextGenerator(TextField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_TextField_fail"
				init_level	= 10

		with self.assertLogs("TextWrapper_TextField_fail", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),3)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertIn(
			f"ERROR:TextWrapper_TextField_fail:Field {self.test_case} must have value", case_loggy.output
		)
		self.assertIn(f"DEBUG:TextWrapper_TextField_fail:No value fetched for field", case_loggy.output)
		self.assertIn("DEBUG:TextWrapper_TextField_fail:Text value to wrap not found", case_loggy.output)
		self.assertIsNone(current)




	def test_TextWrapper_TextField_modifiers_fail(self):

		@TextWrapper(footer=", baby!", header="this is ")
		class TextGenerator(TextField):

			field_value	= "generated {what}"
			modifiers	= { "where": "text" }
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_UTILS_HANDLER
				init_name	= "TextWrapper_TextField_modifiers_fail"
				init_level	= 10

		with self.assertLogs("TextWrapper_TextField_modifiers_fail", 10) as case_loggy:

			self.test_case = TextGenerator()
			current = self.test_case()

		self.assertEqual(len(case_loggy.output),4)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertIn(

			f"DEBUG:TextWrapper_TextField_modifiers_fail:Fetched value of {type('')}",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:TextWrapper_TextField_modifiers_fail:Fetched 16 symbols",
			case_loggy.output
		)
		self.assertIn(

			f"ERROR:TextWrapper_TextField_modifiers_fail:{self.test_case} field failed due to "
			"KeyError: 'what'",
			case_loggy.output
		)
		self.assertIn(

			"DEBUG:TextWrapper_TextField_modifiers_fail:Text value to wrap not found",
			case_loggy.output
		)
		self.assertIsNone(current)








if __name__ == "__main__" : unittest.main(verbosity=2)







