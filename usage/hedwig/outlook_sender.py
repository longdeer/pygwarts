from typing									import Callable
from typing									import Optional
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.irma.access.utils				import TextWrapper
from pygwarts.hedwig.mail.letter.fields		import SenderField
from pygwarts.hedwig.mail.letter.fields		import RecipientField
from pygwarts.hedwig.mail.letter.fields		import ccField
from pygwarts.hedwig.mail.letter.fields		import bccField
from pygwarts.hedwig.mail.letter.fields		import SubjectField
from pygwarts.hedwig.mail.letter.fields		import BodyField
from pygwarts.hedwig.mail.letter.fields		import AttachmentField
from pygwarts.hedwig.mail.builder.client	import OutlookBuilder
from pygwarts.hedwig.mail.utils				import EmailValidator








class Hedwig(OutlookBuilder):
	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hedwig (optional)"

	class validator(EmailValidator):	pass
	class s1(SenderField):				field_value = "send from email 1"	# 2 senders means a compose
	class s2(SenderField):				field_value = "send from email 2"	# window for each sender
	class r1(RecipientField):			field_value = "recipient email 1", "recipient email 2"		# as tuple
	class r2(RecipientField):			field_value = "recipient email 3;recipient email 4"			# or as
	class cc(ccField):					field_value = "copy to email 1", "copy to email 2"			# semicolon
	class bcc(bccField):				field_value = "blind copy to email 1; blind copy to email 2"# string

	@TextWrapper("wrapper head text for subject", "wrapper footer text for subject")
	class subject(SubjectField):

		field_value	= "{VAR} subject text"		# field_value might be with modifiers for altering during
		modifiers	= { "VAR": "VAR value" }	# building, or monolith text

	@TextWrapper("wrapper head text for body", "wrapper footer text for body")
	class body(BodyField):

		field_value	= "body text {VAR}"			# field_value might be with modifiers for altering during
		modifiers	= { "VAR": "VAR value" }	# building, or monolith text

	class a1(AttachmentField): field_value = "attachment 1 path"
	class a2(AttachmentField):

		field_value	= "attachment 2 path"
		modifiers	:Optional[Callable[[Optional[Transmutable],str],str]]








if	__name__ == "__main__" : Hedwig().build()	# Requires running Outlook app







