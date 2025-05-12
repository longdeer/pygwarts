import	os
import	unittest
from	pygwarts.hedwig.mail.letter.fields	import SenderField
from	pygwarts.hedwig.mail.letter.fields	import RecipientField
from	pygwarts.hedwig.mail.letter.fields	import ccField
from	pygwarts.hedwig.mail.letter.fields	import bccField
from	pygwarts.hedwig.mail.letter.fields	import SubjectField
from	pygwarts.hedwig.mail.letter.fields	import BodyField
from	pygwarts.hedwig.mail.letter.fields	import AttachmentField
from	pygwarts.hedwig.mail.builder.client	import ThunderbirdBuilder
from	pygwarts.hedwig.mail.builder.client	import OutlookBuilder
from	pygwarts.hedwig.mail.utils			import EmailValidator
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.irma.access.utils			import TextWrapper
from	pygwarts.tests.hedwig				import HedwigTestCase








class ClientCases(HedwigTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.HEDWIG_MAIL_CLIENT_HANDLER): os.remove(cls.HEDWIG_MAIL_CLIENT_HANDLER)

		# IMPORTANT!
		# IF CLIENT TESTS TO BE MANUALLY
		# INVOKED, BELOW REMOVES WILL NOT
		# ALLOW ATTACHMENTS TO BE INCLUDED
		if	os.path.isfile(cls.attachyone):	os.remove(cls.attachyone)
		if	os.path.isfile(cls.attachytwo):	os.remove(cls.attachytwo)

	@classmethod
	def setUpClass(cls):

		cls.make_loggy_file(cls, cls.HEDWIG_MAIL_CLIENT_HANDLER)
		cls.attachyone = str(cls.HEDWIG_ROOT /"atachy.one")
		cls.attachytwo = str(cls.HEDWIG_ROOT /"atachy.two")
		if	not os.path.isfile(cls.attachyone): cls.fmake(cls, cls.attachyone, "heil maximum build!")
		if	not os.path.isfile(cls.attachytwo): cls.fmake(cls, cls.attachytwo, "heil maximum build!")

	@unittest.skip("manual invokation only")
	def test_Thunderbird_build_minimal(self):

		class CurrentBuilder(ThunderbirdBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_CLIENT_HANDLER
				init_name	= "ThunderbirdBuilder_minimal"
				init_level	= 10

			class validator(EmailValidator):	pass
			class one(SenderField):				field_value = "example1@email.com"
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
		current = self.test_case.build()
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
	def test_Thunderbird_build_full(self):

		class CurrentBuilder(ThunderbirdBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_CLIENT_HANDLER
				init_name	= "ThunderbirdBuilder_full"
				init_level	= 10

			class validator(EmailValidator):	pass
			class s1(SenderField):				field_value = "example1@email.com"
			class s2(SenderField):				field_value = "exomple1@email.com"
			class two(RecipientField):			field_value = "example2@email.com", "example3@email.com"
			class three(ccField):				field_value = "example4@email.com", "example5@email.com"
			class four(bccField):				field_value = "example6@email.com", "example7@email.com"
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
		current = self.test_case.build()
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
	def test_Outlook_build_nomodule(self):

		class CurrentBuilder(OutlookBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_CLIENT_HANDLER
				init_name	= "OutlookBuilder_nomodule"
				init_level	= 10

			class validator(EmailValidator):	pass
			class one(SenderField):				field_value = "example1@email.com"
			class two(RecipientField):			field_value = "example2@email.com", "example3@email.com"

		with self.assertLogs("OutlookBuilder_nomodule", 20) as case_loggy:

			self.test_case = CurrentBuilder()
			current = self.test_case.build()

		self.assertEqual(len(case_loggy.output),1)
		self.assertIn(f"INFO:OutlookBuilder_nomodule:{self.test_case} is not applicable", case_loggy.output)




	@unittest.skip("manual invokation only")
	def test_Outlook_build_minimal(self):

		class CurrentBuilder(OutlookBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_CLIENT_HANDLER
				init_name	= "OutlookBuilder_minimal"
				init_level	= 10

			class validator(EmailValidator):	pass
			class s1(SenderField):				field_value = "example1@email.com"
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
		current = self.test_case.build()
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
	def test_Outlook_build_full(self):

		class CurrentBuilder(OutlookBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_CLIENT_HANDLER
				init_name	= "OutlookBuilder_full"
				init_level	= 10

			class validator(EmailValidator):	pass
			class s1(SenderField):				field_value = "example1@email.com"
			class s2(SenderField):				field_value = "exomple1@email.com"
			class two(RecipientField):			field_value = "example2@email.com", "example3@email.com"
			class three(ccField):				field_value = "example4@email.com", "example5@email.com"
			class four(bccField):				field_value = "example6@email.com", "example7@email.com"
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
		current = self.test_case.build()
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







