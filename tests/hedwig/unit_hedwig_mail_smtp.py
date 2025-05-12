import	os
import	unittest
from 	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.hedwig.mail.letter.fields	import SenderField
from	pygwarts.hedwig.mail.letter.fields	import RecipientField
from	pygwarts.hedwig.mail.letter.fields	import ccField
from	pygwarts.hedwig.mail.letter.fields	import bccField
from	pygwarts.hedwig.mail.letter.fields	import SubjectField
from	pygwarts.hedwig.mail.letter.fields	import BodyField
from	pygwarts.hedwig.mail.letter.fields	import AttachmentField
from	pygwarts.hedwig.mail.builder.smtp	import SMTPBuilder
from	pygwarts.hedwig.mail.utils			import EmailValidator
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access.utils			import TextWrapper
from	pygwarts.tests.hedwig				import HedwigTestCase








class SMTPCases(HedwigTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.HEDWIG_MAIL_SMTP_HANDLER): os.remove(cls.HEDWIG_MAIL_SMTP_HANDLER)

		# IMPORTANT!
		# IF CLIENT TESTS TO BE MANUALLY
		# INVOKED, BELOW REMOVES WILL NOT
		# ALLOW ATTACHMENTS TO BE INCLUDED
		if	os.path.isfile(cls.attachyone):	os.remove(cls.attachyone)
		if	os.path.isfile(cls.attachytwo):	os.remove(cls.attachytwo)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.HEDWIG_MAIL_SMTP_HANDLER)
		cls.attachyone = str(cls.HEDWIG_ROOT /"atachy.one")
		cls.attachytwo = str(cls.HEDWIG_ROOT /"atachy.two")
		if	not os.path.isfile(cls.attachyone): cls.fmake(cls, cls.attachyone, "heil maximum build!")
		if	not os.path.isfile(cls.attachytwo): cls.fmake(cls, cls.attachytwo, "heil maximum build!")

	def test_is_connectable(self):

		class CurrentBuilder(SMTPBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_SMTP_HANDLER
				init_name	= "is_connectable"
				init_level	= 10

		self.test_case = CurrentBuilder()
		with self.assertLogs("is_connectable",10) as case_loggy:
			self.assertEqual(

				self.test_case.is_connectable(
					{
						"endpoint":	"emoil.comm",
						"port":		465,
						"password":	"qwerty",
					}
				),	True
			)
			self.assertEqual(len(case_loggy.output),1)
			self.assertIn("DEBUG:is_connectable:Credentials probe validated", case_loggy.output)




	def test_is_connectable_invalid(self):

		class CurrentBuilder(SMTPBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_SMTP_HANDLER
				init_name	= "is_connectable"
				init_level	= 10

		self.test_case = CurrentBuilder()
		for probe in (

			"probe", 1, 1., None, True, False, ..., print, Transmutable,
			[ "endpoint", "emoil.comm", "port", 465, "password", "qwerty" ],
			( "endpoint", "emoil.comm", "port", 465, "password", "qwerty" ),
			{ "endpoint", "emoil.comm", "port", 465, "password", "qwerty" },
		):	self.assertIsNone(self.test_case.is_connectable(probe))




	def test_is_connectable_wrong(self):

		class CurrentBuilder(SMTPBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_SMTP_HANDLER
				init_name	= "is_connectable_wrong"
				init_level	= 10

		self.test_case = CurrentBuilder()
		with self.assertLogs("is_connectable_wrong", 10) as case_loggy:
			self.assertEqual(
				self.test_case.is_connectable(
					{
						"not endpoint":	"emoil.com",
						"not port":		465,
						"not password":	"qwerty"
					}
				),	False
			)
		self.assertEqual(len(case_loggy.output),3)
		self.assertIn(f"INFO:is_connectable_wrong:Invalid {self.test_case} port type", case_loggy.output)
		self.assertIn(f"INFO:is_connectable_wrong:Invalid {self.test_case} endpoint type", case_loggy.output)
		self.assertIn(f"INFO:is_connectable_wrong:Invalid {self.test_case} password type", case_loggy.output)




	def test_is_connectable_fails(self):

		class CurrentBuilder(SMTPBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_SMTP_HANDLER
				init_name	= "is_connectable_fails"
				init_level	= 10

		self.test_case = CurrentBuilder()
		for fail in (

			[ "fail" ],( "fail", ),{ "fail" }, { "fail": "fail" },
			None, True, False, ..., 1, 1., print, Transmutable
		):
			with self.assertLogs("is_connectable_fails", 10) as case_loggy:
				self.assertEqual(
					self.test_case.is_connectable(
						{
							"endpoint":	fail,
							"password":	"qwerty",
							"port":		465,
						}
					),	False
				)
			self.assertEqual(len(case_loggy.output),1)
			self.assertIn(
				f"INFO:is_connectable_fails:Invalid {self.test_case} endpoint type", case_loggy.output
			)

			with self.assertLogs("is_connectable_fails", 10) as case_loggy:
				self.assertEqual(
					self.test_case.is_connectable(
						{
							"password":	fail,
							"port":		465,
							"endpoint":	"endpoint",
						}
					),	False
				)
			self.assertEqual(len(case_loggy.output),1)
			self.assertIn(
				f"INFO:is_connectable_fails:Invalid {self.test_case} password type", case_loggy.output
			)

		for fail in (

			[ 465 ],( 465, ),{ 465 }, { "port": 465 },
			None, ..., "port", print, Transmutable
		):
			with self.assertLogs("is_connectable_fails", 10) as case_loggy:
				self.assertEqual(
					self.test_case.is_connectable(
						{
							"port":		fail,
							"endpoint":	"endpoint",
							"password":	"qwerty",
						}
					),	False
				)
			self.assertEqual(len(case_loggy.output),1)
			self.assertIn(f"INFO:is_connectable_fails:Invalid {self.test_case} port type", case_loggy.output)








	@unittest.skip("manual invokation only")
	def test_SMTP_build_minimal(self):

		class CurrentBuilder(SMTPBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_SMTP_HANDLER
				init_name	= "SMTPBuilder_minimal"
				init_level	= 10

			class validator(EmailValidator):	pass
			# The email to send from, the first one and the only to be used
			class s1(SenderField):				field_value = "example1@email.com"
			# Second sender will not be used at all
			class s2(SenderField):				field_value = "nouse@email.com"
			class two(RecipientField):			field_value = "example2@email.com", "example3@email.com"
			@TextWrapper("Subject: ")
			class five(SubjectField):

				field_value	= "{level} build test"
				modifiers	= { "level": "maximum" }

			@TextWrapper(header="My ", footer=", baby!")
			class six(BodyField):

				field_value	= "congratulations! Build is {quality}"
				modifiers	= { "quality": "nice" }

		self.test_case = CurrentBuilder()
		# Must be supplied with some working SMTP credentials to get tested
		current = self.test_case.build(
			{
				"endpoint": str(),
				"port":		int(),
				"password":	str(),
			}
		)
		self.assertIsInstance(current, dict)
		self.assertEqual(len(current), 7)
		self.assertIn("sender", current)
		self.assertIn("recipient", current)
		self.assertIn("cc", current)
		self.assertIn("bcc", current)
		self.assertIn("subject", current)
		self.assertIn("body", current)
		self.assertIn("attachment", current)




	@unittest.skip("manual invokation only")
	def test_SMTP_build_full(self):

		class CurrentBuilder(SMTPBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_SMTP_HANDLER
				init_name	= "SMTPBuilder_full"
				init_level	= 10

			class validator(EmailValidator):	pass
			# The email to send from, the first one and the only to be used
			class s1(SenderField):				field_value = "example1@email.com"
			# Second sender will not be used at all
			class s2(SenderField):				field_value = "exomple1@email.com"
			class r1(RecipientField):			field_value = "example2@email.com", "example3@email.com"
			class r2(RecipientField):			field_value = "example4@email.com", "example5@email.com"
			class three(ccField):				field_value = "example6@email.com", "example7@email.com"
			class four(bccField):				field_value = "example8@email.com", "example9@email.com"
			@TextWrapper("Subject: ")
			class five(SubjectField):

				field_value	= "{level} build test"
				modifiers	= { "level": "maximum" }

			@TextWrapper(header="My ", footer=", baby!")
			class six(BodyField):

				field_value	= "congratulations! Build is {quality}"
				modifiers	= { "quality": "nice" }

			class a1(AttachmentField): field_value = self.attachyone
			class a2(AttachmentField):

				field_value	= "attachytwo"
				modifiers	= lambda *S : self.attachytwo

		self.test_case = CurrentBuilder()
		# Must be supplied with some working SMTP credentials to get tested
		current = self.test_case.build(
			{
				"endpoint": str(),
				"port":		int(),
				"password":	str(),
			}
		)
		self.assertIsInstance(current, dict)
		self.assertEqual(len(current), 7)
		self.assertIn("sender", current)
		self.assertIn("recipient", current)
		self.assertIn("cc", current)
		self.assertIn("bcc", current)
		self.assertIn("subject", current)
		self.assertIn("body", current)
		self.assertIn("attachment", current)








if __name__ == "__main__" : unittest.main(verbosity=2)







