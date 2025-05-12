import	os
import	unittest
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.hedwig.mail.letter.fields	import SenderField
from	pygwarts.hedwig.mail.letter.fields	import RecipientField
from	pygwarts.hedwig.mail.letter.fields	import ccField
from	pygwarts.hedwig.mail.letter.fields	import bccField
from	pygwarts.hedwig.mail.letter.fields	import SubjectField
from	pygwarts.hedwig.mail.letter.fields	import BodyField
from	pygwarts.hedwig.mail.letter.fields	import AttachmentField
from	pygwarts.hedwig.mail.builder		import LetterBuilder
from	pygwarts.hedwig.mail.utils			import EmailValidator
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access.utils			import TextWrapper
from	pygwarts.tests.hedwig				import HedwigTestCase








class BuilderCases(HedwigTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.HEDWIG_MAIL_BUILDER_HANDLER): os.remove(cls.HEDWIG_MAIL_BUILDER_HANDLER)

	@classmethod
	def setUpClass(cls): cls.make_loggy_file(cls, cls.HEDWIG_MAIL_BUILDER_HANDLER)
	def test_no_mandatories_build(self):

		class CurrentBuilder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_BUILDER_HANDLER
				init_name	= "no_mandatories_build"
				init_level	= 10

		self.test_case = CurrentBuilder()
		with self.assertLogs("no_mandatories_build", 10) as case_loggy : self.test_case.build()
		self.assertEqual(len(case_loggy.output),3)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining sender field value", case_loggy.output)
		self.assertIn("DEBUG:no_mandatories_build:sender field is not a list", case_loggy.output)
		self.assertIn(

			f"CRITICAL:no_mandatories_build:{self.test_case} sender field failed",
			case_loggy.output
		)


		self.test_case("sender", [ 42 ])
		with self.assertLogs("no_mandatories_build", 10) as case_loggy : self.test_case.build()
		self.assertEqual(len(case_loggy.output),4)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining sender field value", case_loggy.output)
		self.assertIn(

			f"DEBUG:no_mandatories_build:{self.test_case['sender'][0]} is not callable",
			case_loggy.output
		)
		self.assertIn("INFO:no_mandatories_build:sender field obtained 0 items", case_loggy.output)
		self.assertIn(

			f"CRITICAL:no_mandatories_build:{self.test_case} sender field failed",
			case_loggy.output
		)


		self.test_case("sender", [ lambda : 42 ])
		with self.assertLogs("no_mandatories_build", 10) as case_loggy : self.test_case.build()
		self.assertEqual(len(case_loggy.output),4)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining sender field value", case_loggy.output)
		self.assertIn(

			f"DEBUG:no_mandatories_build:{self.test_case['sender'][0]} returned not a string",
			case_loggy.output
		)
		self.assertIn("INFO:no_mandatories_build:sender field obtained 0 items", case_loggy.output)
		self.assertIn(

			f"CRITICAL:no_mandatories_build:{self.test_case} sender field failed",
			case_loggy.output
		)


		self.test_case("sender", [ lambda : "example@email.com" ])
		with self.assertLogs("no_mandatories_build", 10) as case_loggy : self.test_case.build()
		self.assertEqual(len(case_loggy.output),5)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining sender field value", case_loggy.output)
		self.assertIn("INFO:no_mandatories_build:sender field obtained 1 item", case_loggy.output)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining recipient field value", case_loggy.output)
		self.assertIn("DEBUG:no_mandatories_build:recipient field is not a list", case_loggy.output)
		self.assertIn(

			f"CRITICAL:no_mandatories_build:{self.test_case} recipient field failed",
			case_loggy.output
		)


		self.test_case("recipient", [ lambda : 42 ])
		with self.assertLogs("no_mandatories_build", 10) as case_loggy : self.test_case.build()
		self.assertEqual(len(case_loggy.output),6)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining sender field value", case_loggy.output)
		self.assertIn("INFO:no_mandatories_build:sender field obtained 1 item", case_loggy.output)
		self.assertIn("DEBUG:no_mandatories_build:Obtaining recipient field value", case_loggy.output)
		self.assertIn(

			f"DEBUG:no_mandatories_build:{self.test_case['recipient'][0]} returned not a string",
			case_loggy.output
		)
		self.assertIn("INFO:no_mandatories_build:recipient field obtained 0 symbols", case_loggy.output)
		self.assertIn(

			f"CRITICAL:no_mandatories_build:{self.test_case} recipient field failed",
			case_loggy.output
		)




	def test_mandatories_build(self):

		class CurrentBuilder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_BUILDER_HANDLER
				init_name	= "mandatories_build"
				init_level	= 10

			class validator(EmailValidator):	pass
			class one(SenderField):				field_value = "example1@email.com"
			class two(RecipientField):			field_value = "example2@email.com"

		with self.assertLogs("mandatories_build", 10) as case_loggy:

			self.test_case = CurrentBuilder()
			self.assertIn("sender", self.test_case)
			self.assertIsInstance(self.test_case["sender"][0], SenderField)
			self.assertIn("recipient", self.test_case)
			self.assertIsInstance(self.test_case["recipient"][0], RecipientField)
			current_build = self.test_case.build()

		self.assertEqual(len(case_loggy.output),22)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:mandatories_build:Putted \"sender\", \"{[ self.test_case.one ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:mandatories_build:Putted \"recipient\", \"{[ self.test_case.two ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining sender field value", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Fetched value of {type('')}", case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:mandatories_build:Fetched value of {type('')}"),2
		)
		self.assertIn(
			f"DEBUG:mandatories_build:Email address \"example1@email.com\" validated", case_loggy.output
		)
		self.assertIn(f"INFO:mandatories_build:sender field obtained 1 item", case_loggy.output)
		self.assertIn(f"INFO:mandatories_build:{self.test_case.one} obtained 1 email", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining recipient field value", case_loggy.output)
		self.assertIn(
			f"DEBUG:mandatories_build:Email address \"example2@email.com\" validated", case_loggy.output
		)
		self.assertIn(f"INFO:mandatories_build:recipient field obtained 19 symbols", case_loggy.output)
		self.assertIn(f"INFO:mandatories_build:{self.test_case.two} obtained 1 email", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining cc field value", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:cc field is not a list", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining bcc field value", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:bcc field is not a list", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining subject field value", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:subject field is not a list", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining body field value", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:body field is not a list", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:Obtaining attachment field value", case_loggy.output)
		self.assertIn(f"DEBUG:mandatories_build:attachment field is not a list", case_loggy.output)

		self.assertIsInstance(current_build, dict)
		self.assertEqual(len(current_build), 7)
		self.assertIn("sender", current_build)
		self.assertIn("recipient", current_build)
		self.assertIn("cc", current_build)
		self.assertIn("bcc", current_build)
		self.assertIn("subject", current_build)
		self.assertIn("body", current_build)
		self.assertIn("attachment", current_build)
		self.assertEqual(current_build["sender"],[ "example1@email.com;" ])
		self.assertEqual(current_build["recipient"], "example2@email.com;")
		self.assertIsNone(current_build["cc"])
		self.assertIsNone(current_build["bcc"])
		self.assertIsNone(current_build["subject"])
		self.assertIsNone(current_build["body"])
		self.assertIsNone(current_build["attachment"])








	def test_Field_outter_fail(self):
		class NotBuilder(Transmutable):

			class Field(LetterBuilder.Field):	pass
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_BUILDER_HANDLER
				init_name	= "Field_outter_fail"
				init_level	= 10


		with self.assertLogs("Field_outter_fail", 10) as case_loggy:

			self.test_case = NotBuilder()
			current = self.test_case.Field("sender")

		self.assertIsNone(current)
		self.assertIn("DEBUG:Field_outter_fail:Obtaining sender field value", case_loggy.output)
		self.assertIn(
			"DEBUG:Field_outter_fail:sender field cannot be included for building", case_loggy.output
		)








	def test_full_build(self):

		attachyone = str(self.HEDWIG_ROOT /"atachy.one")
		if	not os.path.isfile(attachyone): self.fmake(attachyone, "heil full build!")
		self.assertTrue(os.path.isfile(attachyone))

		class CurrentBuilder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_BUILDER_HANDLER
				init_name	= "full_build"
				init_level	= 10

			class validator(EmailValidator):	pass
			class one(SenderField):				field_value = "example1@email.com"
			class two(RecipientField):			field_value = "example2@email.com"
			class three(ccField):				field_value = "example3@email.com"
			class four(bccField):				field_value = "example4@email.com"
			class five(SubjectField):			field_value = "full build test"
			class six(BodyField):				field_value = "congratulations! build is nice"
			class seven(AttachmentField):		field_value = attachyone

		with self.assertLogs("full_build", 10) as case_loggy:

			self.test_case = CurrentBuilder()

			self.assertIsInstance(self.test_case["sender"], list)
			self.assertIsInstance(self.test_case["recipient"], list)
			self.assertIsInstance(self.test_case["cc"], list)
			self.assertIsInstance(self.test_case["bcc"], list)
			self.assertIsInstance(self.test_case["subject"], list)
			self.assertIsInstance(self.test_case["body"], list)
			self.assertIsInstance(self.test_case["attachment"], list)
			self.assertIsInstance(self.test_case["sender"][0], SenderField)
			self.assertIsInstance(self.test_case["recipient"][0], RecipientField)
			self.assertIsInstance(self.test_case["cc"][0], ccField)
			self.assertIsInstance(self.test_case["bcc"][0], bccField)
			self.assertIsInstance(self.test_case["subject"][0], SubjectField)
			self.assertIsInstance(self.test_case["body"][0], BodyField)
			self.assertIsInstance(self.test_case["attachment"][0], AttachmentField)

			current_build = self.test_case.build()

		self.assertEqual(len(case_loggy.output),45)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:full_build:Putted \"sender\", \"{[ self.test_case.one ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:full_build:Putted \"recipient\", \"{[ self.test_case.two ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:full_build:Putted \"cc\", \"{[ self.test_case.three ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:full_build:Putted \"bcc\", \"{[ self.test_case.four ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:full_build:Putted \"subject\", \"{[ self.test_case.five ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:full_build:Putted \"body\", \"{[ self.test_case.six ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:full_build:Putted \"attachment\", \"{[ self.test_case.seven ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:full_build:Obtaining sender field value", case_loggy.output)
		self.assertIn(f"DEBUG:full_build:Fetched value of {type('')}", case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:full_build:Fetched value of {type('')}"),7)
		self.assertIn(
			"DEBUG:full_build:Email address \"example1@email.com\" validated", case_loggy.output
		)
		self.assertIn("INFO:full_build:sender field obtained 1 item", case_loggy.output)
		self.assertIn(f"INFO:full_build:{self.test_case.one} obtained 1 email", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtaining recipient field value", case_loggy.output)
		self.assertIn(
			"DEBUG:full_build:Email address \"example2@email.com\" validated", case_loggy.output
		)
		self.assertIn("INFO:full_build:recipient field obtained 19 symbols", case_loggy.output)
		self.assertIn(f"INFO:full_build:{self.test_case.two} obtained 1 email", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtaining cc field value", case_loggy.output)
		self.assertIn(
			"DEBUG:full_build:Email address \"example3@email.com\" validated", case_loggy.output
		)
		self.assertIn("INFO:full_build:cc field obtained 19 symbols", case_loggy.output)
		self.assertIn(f"INFO:full_build:{self.test_case.three} obtained 1 email", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtaining bcc field value", case_loggy.output)
		self.assertIn(
			"DEBUG:full_build:Email address \"example4@email.com\" validated", case_loggy.output
		)
		self.assertIn("INFO:full_build:bcc field obtained 19 symbols", case_loggy.output)
		self.assertIn(f"INFO:full_build:{self.test_case.four} obtained 1 email", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtaining subject field value", case_loggy.output)
		self.assertIn("DEBUG:full_build:Proper modifiers not found", case_loggy.output)
		self.assertEqual(case_loggy.output.count("DEBUG:full_build:Proper modifiers not found"), 2)
		self.assertIn("DEBUG:full_build:Fetched 15 symbols", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtained 15 symbols", case_loggy.output)
		self.assertIn("INFO:full_build:subject field obtained 15 symbols", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtaining body field value", case_loggy.output)
		self.assertIn("DEBUG:full_build:Fetched 30 symbols", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtained 30 symbols", case_loggy.output)
		self.assertIn("INFO:full_build:body field obtained 30 symbols", case_loggy.output)
		self.assertIn("DEBUG:full_build:Obtaining attachment field value", case_loggy.output)
		self.assertIn(f"DEBUG:full_build:Fetched {len(attachyone)} symbols", case_loggy.output)
		self.assertIn("DEBUG:full_build:Modifiers not used", case_loggy.output)
		self.assertIn(f"DEBUG:full_build:Obtained file path \"{attachyone}\"", case_loggy.output)
		self.assertIn(
			f"INFO:full_build:attachment field obtained 1 item", case_loggy.output
		)
		self.assertIsInstance(current_build, dict)
		self.assertEqual(len(current_build), 7)
		self.assertIn("sender", current_build)
		self.assertIn("recipient", current_build)
		self.assertIn("cc", current_build)
		self.assertIn("bcc", current_build)
		self.assertIn("subject", current_build)
		self.assertIn("body", current_build)
		self.assertIn("attachment", current_build)
		self.assertEqual(current_build["sender"],[ "example1@email.com;" ])
		self.assertEqual(current_build["recipient"], "example2@email.com;")
		self.assertEqual(current_build["cc"], "example3@email.com;")
		self.assertEqual(current_build["bcc"], "example4@email.com;")
		self.assertEqual(current_build["subject"], "full build test")
		self.assertEqual(current_build["body"], "congratulations! build is nice")
		self.assertEqual(current_build["attachment"],[ attachyone ])

		if	os.path.isfile(attachyone): os.remove(attachyone)
		self.assertFalse(os.path.isfile(attachyone))








	def test_maximum_build(self):

		attachytwo = str(self.HEDWIG_ROOT /"atachy.two")
		if	not os.path.isfile(attachytwo): self.fmake(attachytwo, "heil maximum build!")
		self.assertTrue(os.path.isfile(attachytwo))

		class CurrentBuilder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_BUILDER_HANDLER
				init_name	= "maximum_build"
				init_level	= 10

			class validator(EmailValidator):	pass
			class one(SenderField):				field_value = "example1@email.com", "exomple1@email.com"
			class two(RecipientField):			field_value = "example2@email.com", "example3@email.com"
			class three(ccField):				field_value = "example4@email.com; example5@email.com"
			class four(bccField):				field_value = "example6@email.com; example7@email.com"
			@TextWrapper("Subject: ")
			class five(SubjectField):

				field_value	= "{level} build test"
				modifiers	= { "level": "maximum" }

			@TextWrapper(header="My ", footer=", baby!")
			class six(BodyField):

				field_value	= "congratulations! Build is {quality}"
				modifiers	= { "quality": "nice" }

			class seven(AttachmentField):

				field_value	= "attachytwo"
				modifiers	= lambda *S : attachytwo

		with self.assertLogs("maximum_build", 10) as case_loggy:

			self.test_case = CurrentBuilder()

			self.assertIsInstance(self.test_case["sender"], list)
			self.assertIsInstance(self.test_case["recipient"], list)
			self.assertIsInstance(self.test_case["cc"], list)
			self.assertIsInstance(self.test_case["bcc"], list)
			self.assertIsInstance(self.test_case["subject"], list)
			self.assertIsInstance(self.test_case["body"], list)
			self.assertIsInstance(self.test_case["attachment"], list)
			self.assertIsInstance(self.test_case["sender"][0], SenderField)
			self.assertIsInstance(self.test_case["recipient"][0], RecipientField)
			self.assertIsInstance(self.test_case["cc"][0], ccField)
			self.assertIsInstance(self.test_case["bcc"][0], bccField)
			self.assertIsInstance(self.test_case["subject"][0], SubjectField)
			self.assertIsInstance(self.test_case["body"][0], BodyField)
			self.assertIsInstance(self.test_case["attachment"][0], AttachmentField)

			current_build = self.test_case.build()

		self.assertEqual(len(case_loggy.output),48)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"sender\", \"{[ self.test_case.one ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"recipient\", \"{[ self.test_case.two ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"cc\", \"{[ self.test_case.three ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"bcc\", \"{[ self.test_case.four ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"subject\", \"{[ self.test_case.five ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"body\", \"{[ self.test_case.six ]}\" pair",
			case_loggy.output
		)
		self.assertIn(

			f"DEBUG:maximum_build:Putted \"attachment\", \"{[ self.test_case.seven ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:maximum_build:Obtaining sender field value", case_loggy.output)
		self.assertIn(f"DEBUG:maximum_build:Fetched value of {type(tuple())}", case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:maximum_build:Fetched value of {type(tuple())}"),2)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example1@email.com\" validated", case_loggy.output
		)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"exomple1@email.com\" validated", case_loggy.output
		)
		self.assertIn(f"INFO:maximum_build:{self.test_case.one} obtained 2 emails", case_loggy.output)
		self.assertIn("INFO:maximum_build:sender field obtained 1 item", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtaining recipient field value", case_loggy.output)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example2@email.com\" validated", case_loggy.output
		)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example3@email.com\" validated", case_loggy.output
		)
		self.assertIn(f"INFO:maximum_build:{self.test_case.two} obtained 2 emails", case_loggy.output)
		self.assertIn("INFO:maximum_build:recipient field obtained 38 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtaining cc field value", case_loggy.output)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example4@email.com\" validated", case_loggy.output
		)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example5@email.com\" validated", case_loggy.output
		)
		self.assertIn(f"INFO:maximum_build:{self.test_case.three} obtained 2 emails", case_loggy.output)
		self.assertIn("INFO:maximum_build:cc field obtained 38 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtaining bcc field value", case_loggy.output)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example6@email.com\" validated", case_loggy.output
		)
		self.assertIn(
			"DEBUG:maximum_build:Email address \"example7@email.com\" validated", case_loggy.output
		)
		self.assertIn(f"INFO:maximum_build:{self.test_case.four} obtained 2 emails", case_loggy.output)
		self.assertIn("INFO:maximum_build:bcc field obtained 38 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtaining subject field value", case_loggy.output)
		self.assertIn(f"DEBUG:maximum_build:Fetched value of {type('')}", case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:maximum_build:Fetched value of {type('')}"),5)
		self.assertIn("DEBUG:maximum_build:Fetched 18 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtained 18 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Wrapped text now 27 symbols", case_loggy.output)
		self.assertIn("INFO:maximum_build:subject field obtained 27 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtaining body field value", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Fetched 35 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtained 30 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Wrapped text now 40 symbols", case_loggy.output)
		self.assertIn("INFO:maximum_build:body field obtained 40 symbols", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Obtaining attachment field value", case_loggy.output)
		self.assertIn("DEBUG:maximum_build:Fetched 10 symbols", case_loggy.output)
		self.assertIn(f"DEBUG:maximum_build:Obtained file path \"{attachytwo}\"", case_loggy.output)
		self.assertIn(
			f"INFO:maximum_build:attachment field obtained 1 item", case_loggy.output
		)
		self.assertIsInstance(current_build, dict)
		self.assertEqual(len(current_build), 7)
		self.assertIn("sender", current_build)
		self.assertIn("recipient", current_build)
		self.assertIn("cc", current_build)
		self.assertIn("bcc", current_build)
		self.assertIn("subject", current_build)
		self.assertIn("body", current_build)
		self.assertIn("attachment", current_build)
		self.assertEqual(current_build["sender"],[ "example1@email.com;exomple1@email.com;" ])
		self.assertEqual(current_build["recipient"], "example2@email.com;example3@email.com;")
		self.assertEqual(current_build["cc"], "example4@email.com;example5@email.com;")
		self.assertEqual(current_build["bcc"], "example6@email.com;example7@email.com;")
		self.assertEqual(current_build["subject"], "Subject: maximum build test")
		self.assertEqual(current_build["body"], "My congratulations! Build is nice, baby!")
		self.assertEqual(current_build["attachment"],[ attachytwo ])

		if	os.path.isfile(attachytwo): os.remove(attachytwo)
		self.assertFalse(os.path.isfile(attachytwo))








	def test_multiple_fields_build(self):

		f1 = str(self.HEDWIG_ROOT /"f1.two")
		f2 = str(self.HEDWIG_ROOT /"f2.two")
		f3 = str(self.HEDWIG_ROOT /"f3.two")
		f4 = str(self.HEDWIG_ROOT /"f4.two")
		f5 = str(self.HEDWIG_ROOT /"f5.two")

		if	not os.path.isfile(f1): self.fmake(f1, "OOH EEH")
		if	not os.path.isfile(f2): self.fmake(f2, "OOH AH AH")
		if	not os.path.isfile(f3): self.fmake(f3, "TING TANG")
		if	not os.path.isfile(f4): self.fmake(f4, "WALLA WALLA")
		if	not os.path.isfile(f5): self.fmake(f5, "BING BANG")

		self.assertTrue(os.path.isfile(f1))
		self.assertTrue(os.path.isfile(f2))
		self.assertTrue(os.path.isfile(f3))
		self.assertTrue(os.path.isfile(f4))
		self.assertTrue(os.path.isfile(f5))

		class CurrentBuilder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_BUILDER_HANDLER
				init_name	= "multiple_fields_build"
				init_level	= 10

			class validator(EmailValidator):	pass
			class from1(SenderField):			field_value = "example1@email.com"
			class from2(SenderField):			field_value = "example2@email.com"
			class to1(RecipientField):			field_value = "example3@email.com;example4@email.com;"
			class to2(RecipientField):			field_value = "example5@email.com", "example6@email.com"
			class with1(ccField):				field_value = [ "example7@email.com", "example8@email.com" ]
			class with2(ccField):				field_value = { "example9@email.com" }
			class also1(bccField):				field_value = { "e1@m.com": 1, "e2@m.com": 1 }
			class also2(bccField):				field_value = "example10@email.com"
			class also3(bccField):				field_value = "example11@email.com"
			@TextWrapper("QTC: ")
			@TextWrapper("Subject: ")
			class subj1(SubjectField):

				field_value	= "{level} build"
				modifiers	= { "level": "maximum" }

			class subj2(SubjectField):	field_value = " test"
			class subj3(SubjectField):	field_value = "!"
			@TextWrapper(header="My ", footer=", baby!")
			class b1(BodyField):

				field_value	= "congratulations! Build is {quality}"
				modifiers	= { "quality": "nice" }

			class b2(BodyField):		field_value = "\n\nauthor: me"
			class b3(BodyField):		field_value = " (no doubt)"
			class A1(AttachmentField):	field_value	= f1
			class A2(AttachmentField):	field_value	= f2
			class A3(AttachmentField):	field_value	= f3
			class A4(AttachmentField):	field_value	= f4
			class A5(AttachmentField):	field_value	= f5


		with self.assertLogs("multiple_fields_build", 10) as case_loggy:

			self.test_case = CurrentBuilder()

			self.assertIsInstance(self.test_case["sender"], list)
			self.assertIsInstance(self.test_case["recipient"], list)
			self.assertIsInstance(self.test_case["cc"], list)
			self.assertIsInstance(self.test_case["bcc"], list)
			self.assertIsInstance(self.test_case["subject"], list)
			self.assertIsInstance(self.test_case["body"], list)
			self.assertIsInstance(self.test_case["attachment"], list)
			self.assertEqual(len(self.test_case["sender"]),2)
			self.assertIsInstance(self.test_case["sender"][0], SenderField)
			self.assertIsInstance(self.test_case["sender"][1], SenderField)
			self.assertEqual(len(self.test_case["recipient"]),2)
			self.assertIsInstance(self.test_case["recipient"][0], RecipientField)
			self.assertIsInstance(self.test_case["recipient"][1], RecipientField)
			self.assertEqual(len(self.test_case["cc"]),2)
			self.assertIsInstance(self.test_case["cc"][0], ccField)
			self.assertIsInstance(self.test_case["cc"][1], ccField)
			self.assertEqual(len(self.test_case["bcc"]),3)
			self.assertIsInstance(self.test_case["bcc"][0], bccField)
			self.assertIsInstance(self.test_case["bcc"][1], bccField)
			self.assertIsInstance(self.test_case["bcc"][2], bccField)
			self.assertEqual(len(self.test_case["subject"]),3)
			self.assertIsInstance(self.test_case["subject"][0], SubjectField)
			self.assertIsInstance(self.test_case["subject"][1], SubjectField)
			self.assertIsInstance(self.test_case["subject"][2], SubjectField)
			self.assertEqual(len(self.test_case["body"]),3)
			self.assertIsInstance(self.test_case["body"][0], BodyField)
			self.assertIsInstance(self.test_case["body"][1], BodyField)
			self.assertIsInstance(self.test_case["body"][2], BodyField)
			self.assertEqual(len(self.test_case["attachment"]),5)
			self.assertIsInstance(self.test_case["attachment"][0], AttachmentField)
			self.assertIsInstance(self.test_case["attachment"][1], AttachmentField)
			self.assertIsInstance(self.test_case["attachment"][2], AttachmentField)
			self.assertIsInstance(self.test_case["attachment"][3], AttachmentField)
			self.assertIsInstance(self.test_case["attachment"][4], AttachmentField)

			current_build = self.test_case.build()

		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIsInstance(current_build, dict)
		self.assertEqual(len(current_build), 7)
		self.assertIn("sender", current_build)
		self.assertIn("recipient", current_build)
		self.assertIn("cc", current_build)
		self.assertIn("bcc", current_build)
		self.assertIn("subject", current_build)
		self.assertIn("body", current_build)
		self.assertIn("attachment", current_build)
		self.assertEqual(current_build["sender"],[ "example1@email.com;", "example2@email.com;" ])
		self.assertEqual(

			current_build["recipient"],
			"example3@email.com;example4@email.com;example5@email.com;example6@email.com;"
		)
		self.assertEqual(

			current_build["cc"],
			"example7@email.com;example8@email.com;example9@email.com;"
		)
		self.assertEqual(

			current_build["bcc"],
			"e1@m.com;e2@m.com;example10@email.com;example11@email.com;"
		)
		self.assertEqual(current_build["subject"], "QTC: Subject: maximum build test!")
		self.assertEqual(

			current_build["body"],
			"My congratulations! Build is nice, baby!\n\nauthor: me (no doubt)"
		)
		self.assertEqual(current_build["attachment"],[ f1, f2, f3, f4, f5 ])

		if	os.path.isfile(f1): os.remove(f1)
		if	os.path.isfile(f2): os.remove(f2)
		if	os.path.isfile(f3): os.remove(f3)
		if	os.path.isfile(f4): os.remove(f4)
		if	os.path.isfile(f5): os.remove(f5)

		self.assertFalse(os.path.isfile(f1))
		self.assertFalse(os.path.isfile(f2))
		self.assertFalse(os.path.isfile(f3))
		self.assertFalse(os.path.isfile(f4))
		self.assertFalse(os.path.isfile(f5))








if __name__ == "__main__" : unittest.main(verbosity=2)







