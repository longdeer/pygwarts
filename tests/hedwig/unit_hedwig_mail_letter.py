import	os
import	unittest
from	pygwarts.magical.philosophers_stone	import Transmutable
from	pygwarts.magical.spells				import flagrate
from	pygwarts.hedwig.mail.letter			import ObjectField
from	pygwarts.hedwig.mail.letter			import StringField
from	pygwarts.hedwig.mail.letter			import AddressField
from	pygwarts.hedwig.mail.letter			import TextField
from	pygwarts.hedwig.mail.letter.fields	import SenderField
from	pygwarts.hedwig.mail.letter.fields	import RecipientField
from	pygwarts.hedwig.mail.letter.fields	import ccField
from	pygwarts.hedwig.mail.letter.fields	import bccField
from	pygwarts.hedwig.mail.letter.fields	import AttachmentField
from	pygwarts.hedwig.mail.letter.fields	import SubjectField
from	pygwarts.hedwig.mail.letter.fields	import BodyField
from	pygwarts.hedwig.mail.utils			import EmailValidator
from	pygwarts.hedwig.mail.builder		import LetterBuilder
from	pygwarts.irma.contrib				import LibraryContrib
from	pygwarts.tests.hedwig				import HedwigTestCase








class LetterFieldsCases(HedwigTestCase):


	SAMPLE_TEXT_1	= "OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA\nBING BANG"
	SAMPLE_TEXT_2	= """OOH EEH\nOOH AH AH\nTING TANG\nWALLA WALLA\nBING BANG"""
	SAMPLE_TEXT_3	= "O"
	SAMPLE_TEXT_4	= """O"""
	SAMPLE_TEXT_5	= ""
	SAMPLE_TEXT_6	= """"""
	SAMPLE_TEXT_7	= "{first} EEH\n{first} AH AH\nTING TANG\n{second} {second}\nBING BANG"
	SAMPLE_TEXT_8	= """{first} EEH\n{first} AH AH\nTING TANG\n{second} {second}\nBING BANG"""
	SAMPLE_MODIFS	= { "first": "OOH", "second": "WALLA" }


	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.HEDWIG_MAIL_LETTER_HANDLER):

				cls.current_text.loggy.close()
				cls.current_address.loggy.close()
				os.remove(cls.HEDWIG_MAIL_LETTER_HANDLER)


	@classmethod
	def setUpClass(cls):

		class CurrentAddress(AddressField):

			class validator(EmailValidator): pass
			class loggy(LibraryContrib):

				handler		= cls.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "CurrentAddress"
				init_level	= 10
		cls.current_address	= CurrentAddress()


		class CurrentText(TextField):
			class loggy(LibraryContrib):

				handler		= cls.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "CurrentText"
				init_level	= 10
		cls.current_text	= CurrentText()
		cls.make_loggy_file(cls, cls.HEDWIG_MAIL_LETTER_HANDLER)




	def test_ObjectField_values(self):

		for i,value in enumerate((

			1, 1., "1", True, False, None, print,
			[ "information" ],
			( "information", ),
			{ "information" },
			{ "field_value": "information" },
		)):
			with self.subTest(value=value):
				class CurrentField(ObjectField):

					field_value = value
					class loggy(LibraryContrib):

						handler		= self.HEDWIG_MAIL_LETTER_HANDLER
						init_name	= f"ObjectField_values_{i}"
						init_level	= 10

				with self.assertLogs(f"ObjectField_values_{i}", 10) as case_loggy:

					self.test_case	= CurrentField()
					current_value	= self.test_case()

				self.test_case.loggy.close()
				self.assertEqual(current_value, value)
				self.assertEqual(len(case_loggy.output),1)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(

					f"DEBUG:ObjectField_values_{i}:Fetched value of {type(value)}",
					case_loggy.output
				)
				self.test_case.loggy.close()




	def test_ObjectField_novalue(self):

		class CurrentField(ObjectField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= f"ObjectField_novalue"

		with self.assertLogs(f"ObjectField_novalue", 10) as case_loggy:

			self.test_case	= CurrentField()
			current_value	= self.test_case()

		self.assertIn(f"ERROR:ObjectField_novalue:Field {self.test_case} must have value",case_loggy.output)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertEqual(len(case_loggy.output),1)
		self.assertIsNone(current_value)








	def test_StringField_valid(self):
		class CurrentField(StringField):

			field_value = "hedwig's letter"
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= f"StringField_valid"
				init_level	= 10

		with self.assertLogs(f"StringField_valid", 10) as case_loggy:

			self.test_case	= CurrentField()
			current_value	= self.test_case()

		self.assertIn(

			f"DEBUG:StringField_valid:Fetched value of {type('')}",
			case_loggy.output
		)
		self.assertIn("DEBUG:StringField_valid:Fetched 15 symbols",case_loggy.output)
		self.assertEqual(current_value, "hedwig's letter")
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),2)




	def test_StringField_invalid(self):

		for i,value in enumerate((

			1, 1., True, False, print,
			[ "information" ],
			( "information", ),
			{ "information" },
			{ "field_value": "information" },
		)):
			with self.subTest(value=value):
				class CurrentField(StringField):

					field_value = value
					class loggy(LibraryContrib):

						handler		= self.HEDWIG_MAIL_LETTER_HANDLER
						init_name	= f"StringField_invalid_{i}"
						init_level	= 10

				with self.assertLogs(f"StringField_invalid_{i}", 10) as case_loggy:

					self.test_case	= CurrentField()
					current_value	= self.test_case()

				self.test_case.loggy.close()
				self.no_loggy_levels(case_loggy.output, 50)
				self.assertEqual(len(case_loggy.output),2)
				self.assertIsNone(current_value)
				self.assertIn(

					f"DEBUG:StringField_invalid_{i}:Fetched value of {type(value)}",
					case_loggy.output
				)
				self.assertIn(

					f"ERROR:StringField_invalid_{i}:Field {self.test_case} value must be string",
					case_loggy.output
				)
				self.test_case.loggy.close()




	def test_StringField_novalue(self):

		class CurrentField(StringField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= f"StringField_novalue"
				init_level	= 10

		with self.assertLogs(f"StringField_novalue", 10) as case_loggy:

			self.test_case	= CurrentField()
			current_value	= self.test_case()

		self.assertIn(f"ERROR:StringField_novalue:Field {self.test_case} must have value",case_loggy.output)
		self.assertIn("DEBUG:StringField_novalue:No value fetched for field",case_loggy.output)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertEqual(len(case_loggy.output),2)
		self.assertIsNone(current_value)




	def test_StringField_None(self):
		class CurrentField(StringField):

			field_value = None
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= f"StringField_None"
				init_level	= 10

		with self.assertLogs(f"StringField_None", 10) as case_loggy:

			self.test_case	= CurrentField()
			current_value	= self.test_case()

		self.assertIn(f"DEBUG:StringField_None:Fetched value of {type(None)}",case_loggy.output)
		self.assertIn("DEBUG:StringField_None:No value fetched for field",case_loggy.output)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),2)
		self.assertIsNone(current_value)








	def test_AddressField_single_valid(self):

		for address in self.VALID_EMAILS:
			with self.subTest(email=address):

				self.current_address.field_value = address
				with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

				self.assertEqual(current, f"{address};")
				self.assertEqual(len(case_loggy.output),3)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address}\" validated", case_loggy.output
				)
				self.assertIn(
					f"INFO:CurrentAddress:{self.current_address} obtained 1 email", case_loggy.output
				)


	def test_AddressField_single_valid_semicol(self):

		for address in ( f"{E};" for E in self.VALID_EMAILS ):
			with self.subTest(email=address):

				self.current_address.field_value = address
				with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

				self.assertEqual(current, address)
				self.assertEqual(len(case_loggy.output),3)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address[:-1]}\" validated", case_loggy.output
				)
				self.assertIn(
					f"INFO:CurrentAddress:{self.current_address} obtained 1 email", case_loggy.output
				)


	def test_AddressField_single_invalid_str(self):

		# shrinked to not include ; and space addresses
		for address in self.INVALID_EMAILS[1:-3]:
			with self.subTest(email=address):

				self.current_address.field_value = address
				with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

				self.assertIsNone(current)
				self.assertEqual(len(case_loggy.output),3)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address}\"", case_loggy.output
				)
				self.assertIn(

					f"INFO:CurrentAddress:{self.current_address} field has no valid addresses",
					case_loggy.output
				)


	def test_AddressField_single_invalid_str_semicol(self):

		# shrinked to not include semicolumned, spaced and empty addresses
		for address in ( f"{E};" for E in self.INVALID_EMAILS[1:-3] ):
			with self.subTest(email=address):

				self.current_address.field_value = address
				with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

				self.assertIsNone(current)
				self.assertEqual(len(case_loggy.output),3)
				self.no_loggy_levels(case_loggy.output, 30,40,50)
				self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address[:-1]}\"", case_loggy.output
				)
				self.assertIn(

					f"INFO:CurrentAddress:{self.current_address} field has no valid addresses",
					case_loggy.output
				)


	def test_AddressField_joint_valid(self):

		joint_count = len(self.VALID_EMAILS)

		for valid_joint in (

			";".join(self.VALID_EMAILS),
			"; ".join(self.VALID_EMAILS),
			";	 ".join(self.VALID_EMAILS),
			"; 	".join(self.VALID_EMAILS),
			" ;".join(self.VALID_EMAILS),
			"	 ;".join(self.VALID_EMAILS),
			" 	;".join(self.VALID_EMAILS),
			" ; ".join(self.VALID_EMAILS),
			"	;".join(self.VALID_EMAILS),
			";	".join(self.VALID_EMAILS),
			"	;	".join(self.VALID_EMAILS),
		):
			self.current_address.field_value = valid_joint
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.assertEqual(len(case_loggy.output),joint_count +2)
			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} obtained {joint_count} emails",
				case_loggy.output
			)

			for address in self.VALID_EMAILS:
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address}\" validated", case_loggy.output
				)


	def test_AddressField_joint_invalid(self):

		# shrinked to not include semicolumned, spaced and empty addresses
		joint_source = self.INVALID_EMAILS[1:-3]

		for invalid_joint in (

			";".join(joint_source),
			"; ".join(joint_source),
			";	 ".join(joint_source),
			"; 	".join(joint_source),
			" ;".join(joint_source),
			"	 ;".join(joint_source),
			" 	;".join(joint_source),
			" ; ".join(joint_source),
			"	;".join(joint_source),
			";	".join(joint_source),
			"	;	".join(joint_source),
		):
			self.current_address.field_value = invalid_joint
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.assertEqual(len(case_loggy.output),len(joint_source) +2)
			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} field has no valid addresses",
				case_loggy.output
			)

			for address in joint_source:
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address}\"", case_loggy.output
				)


	def test_AddressField_joint_mixed(self):

		# shrinked to not include semicolumned, spaced and empty addresses
		invalid_joint_source = self.INVALID_EMAILS[1:-3]
		valid_count = len(self.VALID_EMAILS)
		joint_source = list(set(self.VALID_EMAILS) | set(invalid_joint_source))

		for mixed_joint in (

			";".join(joint_source),
			"; ".join(joint_source),
			";	 ".join(joint_source),
			"; 	".join(joint_source),
			" ;".join(joint_source),
			"	 ;".join(joint_source),
			" 	;".join(joint_source),
			" ; ".join(joint_source),
			"	;".join(joint_source),
			";	".join(joint_source),
			"	;	".join(joint_source),
		):
			self.current_address.field_value = mixed_joint
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),len(joint_source) +2)
			self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} obtained {valid_count} emails",
				case_loggy.output
			)

			for address in self.VALID_EMAILS:
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address}\" validated", case_loggy.output
				)
			for address in invalid_joint_source:
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address}\"", case_loggy.output
				)


	def test_AddressField_container_valid(self):

		joint_count = len(self.VALID_EMAILS)

		for valid_container in (

			self.VALID_EMAILS,
			list(self.VALID_EMAILS),
			set(self.VALID_EMAILS),
		):
			self.current_address.field_value = valid_container
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),joint_count +2)
			self.assertIn(
				f"DEBUG:CurrentAddress:Fetched value of {type(valid_container)}", case_loggy.output
			)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} obtained {joint_count} emails",
				case_loggy.output
			)

			for address in self.VALID_EMAILS:
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address}\" validated", case_loggy.output
				)


	def test_AddressField_container_invalid(self):

		# shrinked to not include semicolumned, spaced and empty addresses
		container_source = self.INVALID_EMAILS[1:-3]

		for invalid_container in (

			container_source,
			list(container_source),
			set(container_source),
		):
			self.current_address.field_value = invalid_container
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),len(container_source) +2)
			self.assertIn(
				f"DEBUG:CurrentAddress:Fetched value of {type(invalid_container)}", case_loggy.output
			)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} field has no valid addresses",
				case_loggy.output
			)

			for address in container_source:
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address}\"", case_loggy.output
				)


	def test_AddressField_continaer_mixed(self):

		# shrinked to not include semicolumned, spaced and empty addresses
		invalid_container_source = self.INVALID_EMAILS[1:-3]
		valid_count = len(self.VALID_EMAILS)
		container_source = tuple(set(self.VALID_EMAILS) | set(invalid_container_source))

		for mixed_container in (

			container_source,
			list(container_source),
			set(container_source),
		):
			self.current_address.field_value = mixed_container
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),len(container_source) +2)
			self.assertIn(
				f"DEBUG:CurrentAddress:Fetched value of {type(mixed_container)}", case_loggy.output
			)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} obtained {valid_count} emails",
				case_loggy.output
			)

			for address in self.VALID_EMAILS:
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address}\" validated", case_loggy.output
				)
			for address in invalid_container_source:
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address}\"", case_loggy.output
				)


	def test_AddressField_continaer_others_mixed(self):

		invalid_container_source = ( 1, False, print, LibraryContrib, )
		valid_count = len(self.VALID_EMAILS)
		container_source = tuple(set(self.VALID_EMAILS) | set(invalid_container_source))

		for mixed_container in (

			container_source,
			list(container_source),
			set(container_source),
		):
			self.current_address.field_value = mixed_container
			with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),len(container_source) +2)
			self.assertIn(
				f"DEBUG:CurrentAddress:Fetched value of {type(mixed_container)}", case_loggy.output
			)
			self.assertIn(

				f"INFO:CurrentAddress:{self.current_address} obtained {valid_count} emails",
				case_loggy.output
			)

			for address in self.VALID_EMAILS:
				self.assertIn(
					f"DEBUG:CurrentAddress:Email address \"{address}\" validated", case_loggy.output
				)
			for address in invalid_container_source:
				self.assertIn(
					f"INFO:CurrentAddress:Invalid email address \"{address}\"", case_loggy.output
				)


	def test_AddressField_invalid_field(self):

		for invalid_value in ( 1, 1., True, False, print, LibraryContrib, ):
			with self.subTest(value=invalid_value):
				self.current_address.field_value = invalid_value

				with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()

				self.no_loggy_levels(case_loggy.output, 50)
				self.assertEqual(len(case_loggy.output),2)
				self.assertIsNone(current)
				self.assertIn(
					f"DEBUG:CurrentAddress:Fetched value of {type(invalid_value)}", case_loggy.output
				)
				self.assertIn(

					f"ERROR:CurrentAddress:{self.current_address} field failed due to "
					f"TypeError: '{invalid_value.__class__.__name__}' object is not iterable",
					case_loggy.output
				)

		self.current_address.field_value = None
		with self.assertLogs("CurrentAddress", 10) as case_loggy : current = self.current_address()
		self.assertIn(f"DEBUG:CurrentAddress:Fetched value of {type(None)}", case_loggy.output)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),1)
		self.assertIsNone(current)


	def test_AddressField_no_validator(self):
		class CurrentAddress(AddressField):

			field_value = ""
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "AddressField_no_validator"
				init_level	= 10

		self.test_case = CurrentAddress()
		with self.assertLogs("AddressField_no_validator", 10) as case_loggy : current = self.test_case()
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertIsNone(current)
		self.assertIn(

			f"INFO:AddressField_no_validator:{self.test_case} cannot validate email address",
			case_loggy.output
		)








	def test_SenderField_nomake(self):

		class pseudo_sender(SenderField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-sender-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-sender-top", 10) as case_loggy:

			self.test_case = pseudo_sender()
			current = self.test_case.make_field("sender")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-sender-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-sender-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-sender"
				init_level	= 10

			class pseudo_sender(SenderField):	pass

		with self.assertLogs("PseudoBuilder-sender", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_sender.make_field("sender")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-sender:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-sender:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "Builder-sender"
				init_level	= 10

			class pseudo_sender(SenderField):	pass

		with self.assertLogs("Builder-sender", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_sender.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder-sender:Putted \"sender\", \"{[ self.test_case.pseudo_sender ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder-sender:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)








	def test_RecipientField_nomake(self):

		class pseudo_recip(RecipientField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-recip-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-recip-top", 10) as case_loggy:

			self.test_case = pseudo_recip()
			current = self.test_case.make_field("recipient")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-recip-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-recip-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-recip"
				init_level	= 10

			class pseudo_recip(RecipientField):	pass

		with self.assertLogs("PseudoBuilder-recip", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_recip.make_field("recipient")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-recip:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-recip:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "Builder"
				init_level	= 10

			class pseudo_recip(RecipientField):	pass

		with self.assertLogs("Builder", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_recip.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder:Putted \"recipient\", \"{[ self.test_case.pseudo_recip ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)








	def test_ccField_nomake(self):

		class pseudo_сс(ccField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-cc-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-cc-top", 10) as case_loggy:

			self.test_case = pseudo_сс()
			current = self.test_case.make_field("cc")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-cc-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-cc-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-cc"
				init_level	= 10

			class pseudo_сс(ccField):	pass

		with self.assertLogs("PseudoBuilder-cc", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_сс.make_field("cc")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-cc:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-cc:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "Builder"
				init_level	= 10

			class pseudo_сс(ccField):	pass

		with self.assertLogs("Builder", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_сс.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder:Putted \"cc\", \"{[ self.test_case.pseudo_сс ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)








	def test_bccField_nomake(self):

		class pseudo_bсс(bccField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-bcc-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-bcc-top", 10) as case_loggy:

			self.test_case = pseudo_bсс()
			current = self.test_case.make_field("bcc")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-bcc-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-bcc-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-bcc"
				init_level	= 10

			class pseudo_bсс(bccField):	pass

		with self.assertLogs("PseudoBuilder-bcc", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_bсс.make_field("bcc")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-bcc:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-bcc:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "Builder"
				init_level	= 10

			class pseudo_bсс(bccField):	pass

		with self.assertLogs("Builder", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_bсс.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder:Putted \"bcc\", \"{[ self.test_case.pseudo_bсс ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)








	def test_TextField_simple_valid(self):

		for sample in (

			self.SAMPLE_TEXT_1,
			self.SAMPLE_TEXT_2,
			self.SAMPLE_TEXT_3,
			self.SAMPLE_TEXT_4,
			self.SAMPLE_TEXT_5,
			self.SAMPLE_TEXT_6,
			self.SAMPLE_TEXT_7,
			self.SAMPLE_TEXT_8,
		):

			slen = len(sample)
			self.current_text.field_value = sample

			with self.assertLogs("CurrentText", 10) as case_loggy : current = self.current_text()

			self.assertIn(f"DEBUG:CurrentText:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentText:Fetched {slen} symbol{flagrate(slen)}", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentText:Proper modifiers not found", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentText:Obtained {slen} symbol{flagrate(slen)}", case_loggy.output)
			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),4)
			self.assertEqual(current, sample)


	def test_TextField_format_valid(self):

		self.current_text.modifiers = self.SAMPLE_MODIFS

		for sample in (

			self.SAMPLE_TEXT_1,
			self.SAMPLE_TEXT_2,
			self.SAMPLE_TEXT_3,
			self.SAMPLE_TEXT_4,
			self.SAMPLE_TEXT_5,
			self.SAMPLE_TEXT_6,
			self.SAMPLE_TEXT_7,
			self.SAMPLE_TEXT_8,
		):
			slen = len(sample)
			fsample = sample.format(**self.SAMPLE_MODIFS)
			flen = len(fsample)
			self.current_text.field_value = sample

			with self.assertLogs("CurrentText", 10) as case_loggy : current = self.current_text()

			self.assertIn(f"DEBUG:CurrentText:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentText:Fetched {slen} symbol{flagrate(slen)}", case_loggy.output)
			self.assertIn(

				f"DEBUG:CurrentText:Obtained {flen} symbol{flagrate(slen)}",
				case_loggy.output
			)
			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertEqual(len(case_loggy.output),3)
			self.assertEqual(current, fsample)

		delattr(self.current_text, "modifiers")


	def test_TextField_format_KeyError(self):

		self.current_text.modifiers = { "first": "OOH" }

		for sample in ( self.SAMPLE_TEXT_7, self.SAMPLE_TEXT_8 ):

			slen = len(sample)
			self.current_text.field_value = sample

			with self.assertLogs("CurrentText", 10) as case_loggy : current = self.current_text()

			self.assertIsNone(current)
			self.assertEqual(len(case_loggy.output),3)
			self.no_loggy_levels(case_loggy.output, 50)
			self.assertIn(f"DEBUG:CurrentText:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentText:Fetched {slen} symbol{flagrate(slen)}", case_loggy.output)
			self.assertIn(

				f"ERROR:CurrentText:{self.current_text} field failed due to "
				"KeyError: 'second'",
				case_loggy.output
			)

		delattr(self.current_text, "modifiers")


	def test_TextField_invalid_field(self):

		self.current_text.modifiers = self.SAMPLE_MODIFS

		for invalid_value in ( 1, 1., True, False, print, LibraryContrib, ):
			with self.subTest(value=invalid_value):
				self.current_text.field_value = invalid_value

				with self.assertLogs("CurrentText", 10) as case_loggy : current = self.current_text()

				self.assertIsNone(current)
				self.assertIn(
					f"DEBUG:CurrentText:Fetched value of {type(invalid_value)}", case_loggy.output
				)
				self.assertIn(

					f"ERROR:CurrentText:Field {self.current_text} value must be string",
					case_loggy.output
				)

		self.current_text.field_value = None
		with self.assertLogs("CurrentText", 10) as case_loggy : current = self.current_text()
		self.assertIn(f"DEBUG:CurrentText:Fetched value of {type(None)}", case_loggy.output)
		self.assertIn("DEBUG:CurrentText:No value fetched for field", case_loggy.output)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),2)
		self.assertIsNone(current)
		delattr(self.current_text, "modifiers")


	def test_TextField_novalue(self):

		class CurrentText(TextField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "TextField_novalue"
				init_level	= 10

		self.test_case = CurrentText()
		with self.assertLogs("TextField_novalue", 10) as case_loggy : current = self.test_case()

		self.no_loggy_levels(case_loggy.output, 50)
		self.assertEqual(len(case_loggy.output),2)
		self.assertIsNone(current)
		self.assertIn("DEBUG:TextField_novalue:No value fetched for field", case_loggy.output)
		self.assertIn(
			f"ERROR:TextField_novalue:Field {self.current_text} must have value",case_loggy.output
		)


	def test_TextField_invalid_modifiers(self):

		self.current_text.field_value = "Bypass"

		for invalid_modifiers in (

			1, 1., True, False, print, LibraryContrib,
			({ "first": "OOH", "second": "WALLA" },),
			[{ "first": "OOH", "second": "WALLA" }],
			[ "first", "OOH", "second", "WALLA" ],
			( "first", "OOH", "second", "WALLA", ),
			{ "first", "OOH", "second", "WALLA" },
		):
			self.current_text.modifiers = invalid_modifiers

			with self.assertLogs("CurrentText", 10) as case_loggy : current = self.current_text()

			self.assertEqual(current, "Bypass")
			self.assertEqual(len(case_loggy.output),4)
			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertIn(f"DEBUG:CurrentText:Fetched value of {type('')}", case_loggy.output)
			self.assertIn("DEBUG:CurrentText:Fetched 6 symbols", case_loggy.output)
			self.assertIn("DEBUG:CurrentText:Proper modifiers not found", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentText:Obtained 6 symbols", case_loggy.output)

		delattr(self.current_text, "modifiers")








	def test_SubjectField_nomake(self):

		class pseudo_subj(SubjectField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-subject-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-subject-top", 10) as case_loggy:

			self.test_case = pseudo_subj()
			current = self.test_case.make_field("subject")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-subject-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-subject-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-subject"
				init_level	= 10

			class pseudo_subj(SubjectField):	pass

		with self.assertLogs("PseudoBuilder-subject", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_subj.make_field("subject")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-subject:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-subject:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "Builder"
				init_level	= 10

			class pseudo_subj(SubjectField):	pass

		with self.assertLogs("Builder", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_subj.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder:Putted \"subject\", \"{[ self.test_case.pseudo_subj ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)








	def test_BodyField_nomake(self):

		class pseudo_body(BodyField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-body-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-body-top", 10) as case_loggy:

			self.test_case = pseudo_body()
			current = self.test_case.make_field("body")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-body-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-body-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "PseudoBuilder-body"
				init_level	= 10

			class pseudo_body(BodyField):	pass

		with self.assertLogs("PseudoBuilder-body", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_body.make_field("body")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-body:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-body:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_HANDLER
				init_name	= "Builder"
				init_level	= 10

			class pseudo_body(BodyField):	pass

		with self.assertLogs("Builder", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_body.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder:Putted \"body\", \"{[ self.test_case.pseudo_body ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
















class AttachmentFieldsCases(HedwigTestCase):

	@classmethod
	def tearDownClass(cls):

		if	cls.clean_up:
			if	os.path.isfile(cls.HEDWIG_MAIL_LETTER_AHANDLER):

				cls.current_attach.loggy.close()
				os.remove(cls.HEDWIG_MAIL_LETTER_AHANDLER)

		if	os.path.isfile(cls.attach_original): os.remove(cls.attach_original)
		if	os.path.isfile(cls.attach_modified): os.remove(cls.attach_modified)

	@classmethod
	def setUpClass(cls):

		class CurrentAttachment(AttachmentField):
			class loggy(LibraryContrib):

				handler		= cls.HEDWIG_MAIL_LETTER_AHANDLER
				init_name	= "CurrentAttachment"
				init_level	= 10
		cls.current_attach	= CurrentAttachment()
		cls.attach_original	= str(cls.HEDWIG_ROOT /"origin.attach")
		cls.attach_modified	= str(cls.HEDWIG_ROOT /"modified.attach")
		cls.attach_notexist	= str(cls.HEDWIG_ROOT /"notexist.attach")
		cls.make_loggy_file(cls, cls.HEDWIG_MAIL_LETTER_AHANDLER)

		cls.ors	= len(cls.attach_original)
		cls.mods= len(cls.attach_modified)
		cls.noe	= len(cls.attach_notexist)


	def valid_attachment_modifier(self, source :str) -> str : return self.attach_modified
	def setUp(self):

		if	not os.path.isfile(self.attach_original):	self.fmake(self.attach_original)
		if	not os.path.isfile(self.attach_modified):	self.fmake(self.attach_modified)
		if	hasattr(self.current_attach, "modifiers"):	delattr(self.current_attach, "modifiers")




	def test_AttachmentField_valid(self):

		self.current_attach.field_value = self.attach_original
		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()
		self.assertEqual(current, self.attach_original)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),4)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched {self.ors} symbols", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Modifiers not used", case_loggy.output)
		self.assertIn(
			f"DEBUG:CurrentAttachment:Obtained file path \"{self.attach_original}\"", case_loggy.output
		)


	def test_AttachmentField_modified_valid(self):

		self.current_attach.field_value	= self.attach_original
		self.current_attach.modifiers	= self.valid_attachment_modifier
		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),3)
		self.assertEqual(current, self.attach_modified)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched {self.ors} symbols", case_loggy.output)
		self.assertIn(
			f"DEBUG:CurrentAttachment:Obtained file path \"{self.attach_modified}\"", case_loggy.output
		)


	def test_AttachmentField_valid_notexist(self):

		self.current_attach.field_value = self.attach_notexist
		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()
		self.assertIsNone(current)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),4)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched {self.noe} symbols", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Modifiers not used", case_loggy.output)
		self.assertIn(

			f"INFO:CurrentAttachment:{self.current_attach} cannot attach "
			f"non-existent file \"{self.attach_notexist}\"",
			case_loggy.output
		)


	def test_AttachmentField_modified_valid_notexist_to_exist(self):

		self.current_attach.field_value	= self.attach_notexist
		self.current_attach.modifiers	= self.valid_attachment_modifier
		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),3)
		self.assertEqual(current, self.attach_modified)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched {self.noe} symbols", case_loggy.output)
		self.assertIn(
			f"DEBUG:CurrentAttachment:Obtained file path \"{self.attach_modified}\"", case_loggy.output
		)


	def test_AttachmentField_modified_valid_notexist(self):

		self.current_attach.field_value	= self.attach_notexist
		self.current_attach.modifiers	= lambda E : E
		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),3)
		self.assertIsNone(current)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched {self.noe} symbols", case_loggy.output)
		self.assertIn(

			f"INFO:CurrentAttachment:{self.current_attach} cannot attach "
			f"non-existent file \"{self.attach_notexist}\"",
			case_loggy.output
		)


	def test_AttachmentField_invalid_field(self):

		for invalid_value in ( 1, 1., True, False, print, LibraryContrib, ):
			with self.subTest(value=invalid_value):
				self.current_attach.field_value = invalid_value

				with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()

				self.no_loggy_levels(case_loggy.output, 50)
				self.assertEqual(len(case_loggy.output),2)
				self.assertIsNone(current)
				self.assertIn(
					f"DEBUG:CurrentAttachment:Fetched value of {type(invalid_value)}", case_loggy.output
				)
				self.assertIn(

					f"ERROR:CurrentAttachment:Field {self.current_attach} value must be string",
					case_loggy.output
				)

		self.current_attach.field_value = None
		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type(None)}", case_loggy.output)
		self.assertIn("DEBUG:CurrentAttachment:No value fetched for field", case_loggy.output)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.assertEqual(len(case_loggy.output),2)
		self.assertIsNone(current)


	def test_AttachmentField_novalue(self):

		class CurrentAttachment(AttachmentField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_AHANDLER
				init_name	= "CurrentAttachment_novalue"
				init_level	= 10

		self.test_case = CurrentAttachment()
		with self.assertLogs("CurrentAttachment_novalue", 10) as case_loggy : current = self.test_case()

		self.no_loggy_levels(case_loggy.output, 50)
		self.assertEqual(len(case_loggy.output),2)
		self.assertIsNone(current)
		self.assertIn("DEBUG:CurrentAttachment_novalue:No value fetched for field", case_loggy.output)
		self.assertIn(
			f"ERROR:CurrentAttachment_novalue:Field {self.test_case} must have value",case_loggy.output
		)


	def test_AttachmentField_invalid_modifiers(self):

		self.current_attach.field_value = "Bypass"

		for invalid_modifiers in (

			1, 1., True, False,
			( self.valid_attachment_modifier,),
			[ self.valid_attachment_modifier ],
			{ self.valid_attachment_modifier },
			{ "modifiers": self.valid_attachment_modifier },
		):
			self.current_attach.modifiers = invalid_modifiers

			with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()

			self.assertIsNone(current)
			self.assertEqual(len(case_loggy.output),4)
			self.no_loggy_levels(case_loggy.output, 30,40,50)
			self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentAttachment:Fetched 6 symbols", case_loggy.output)
			self.assertIn(f"DEBUG:CurrentAttachment:Modifiers not used", case_loggy.output)
			self.assertIn(

				f"INFO:CurrentAttachment:{self.current_attach} cannot attach "
				f"non-existent file \"Bypass\"",
				case_loggy.output
			)


	def test_AttachmentField_modifiers_error(self):

		self.current_attach.field_value = "Bypass"
		self.current_attach.modifiers = lambda : "Bypass"

		with self.assertLogs("CurrentAttachment", 10) as case_loggy : current = self.current_attach()

		self.assertIsNone(current)
		self.assertEqual(len(case_loggy.output),4)
		self.no_loggy_levels(case_loggy.output, 50)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched value of {type('')}", case_loggy.output)
		self.assertIn(f"DEBUG:CurrentAttachment:Fetched 6 symbols", case_loggy.output)
		self.assertIn(

			f"ERROR:CurrentAttachment:AttachmentField {self.current_attach} field failed due to "
			f"TypeError: {self.current_attach.modifiers.__qualname__}() "
			"takes 0 positional arguments but 1 was given",
			case_loggy.output
		)
		self.assertIn(

			f"INFO:CurrentAttachment:{self.current_attach} cannot attach "
			f"non-existent file \"Bypass\"",
			case_loggy.output
		)




	def test_AttachmentField_nomake(self):

		class pseudo_attach(AttachmentField):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_AHANDLER
				init_name	= "PseudoBuilder-attach-top"
				init_level	= 10


		with self.assertLogs("PseudoBuilder-attach-top", 10) as case_loggy:

			self.test_case = pseudo_attach()
			current = self.test_case.make_field("attach")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-attach-top:Builder not found",case_loggy.output)
		self.assertEqual(case_loggy.output.count(f"DEBUG:PseudoBuilder-attach-top:Builder not found"),2)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class PseudoBuilder(Transmutable):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_AHANDLER
				init_name	= "PseudoBuilder-attach"
				init_level	= 10

			class pseudo_attach(AttachmentField):	pass

		with self.assertLogs("PseudoBuilder-attach", 10) as case_loggy:

			self.test_case = PseudoBuilder()
			current = self.test_case.pseudo_attach.make_field("attach")

		self.assertIsNone(current)
		self.assertIn(f"DEBUG:PseudoBuilder-attach:Improper builder {self.test_case}",case_loggy.output)
		self.assertEqual(
			case_loggy.output.count(f"DEBUG:PseudoBuilder-attach:Improper builder {self.test_case}"),2
		)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)
		self.test_case.loggy.close()


		class Builder(LetterBuilder):
			class loggy(LibraryContrib):

				handler		= self.HEDWIG_MAIL_LETTER_AHANDLER
				init_name	= "Builder"
				init_level	= 10

			class pseudo_attach(AttachmentField):	pass

		with self.assertLogs("Builder", 10) as case_loggy:

			self.test_case = Builder()
			current = self.test_case.pseudo_attach.make_field(42)

		self.assertIsNone(current)
		self.assertIn(

			f"DEBUG:Builder:Putted \"attachment\", \"{[ self.test_case.pseudo_attach ]}\" pair",
			case_loggy.output
		)
		self.assertIn(f"DEBUG:Builder:Field name \"42\" must be a string",case_loggy.output)
		self.assertEqual(len(case_loggy.output),2)
		self.no_loggy_levels(case_loggy.output, 30,40,50)








if __name__ == "__main__" : unittest.main(verbosity=2)







