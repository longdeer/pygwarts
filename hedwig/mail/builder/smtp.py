from typing							import List
from typing							import Dict
from smtplib						import SMTP_SSL
from pygwarts.magical.spells		import patronus
from pygwarts.hedwig.mail.builder	import LetterBuilder








class SMTPBuilder(LetterBuilder):

	"""
		LetterBuilder implementation of standard SMTP library. Initiates SSL connection and server
		authorization, using credentials that must be provided as a dictionary for "build" method,
		preliminary verifying them with "is_connectable" helper method. Fetches letter fields by
		LetterBuilder.build and sends email only for a very first SenderField entity encountered
		immediately. Ignores all attachments. All cc and bcc fields extends recipient field. Handles
		every possible Exception that might be raised during connection, authorization and sending.
	"""

	def is_connectable(self, probe :Dict[str,str | int]) -> bool :

		"""
			Helper method that verifies connection "probe" dictionary. Checks if such dictionary has
			such necessary key-value pairs as:
				"endpoint":	email server endpoint address string,
				"port":		email server address port as integer,
				"password":	password for authorization on the server with very first SenderField address
							as login.
		"""

		valid = True

		if	isinstance(probe, dict):
			if	not isinstance(probe.get("endpoint"), str):

				self.loggy.info(f"Invalid {self} endpoint type")
				valid = False


			if	not isinstance(probe.get("port"), int):

				self.loggy.info(f"Invalid {self} port type")
				valid = False


			if	not isinstance(probe.get("password"), str):

				self.loggy.info(f"Invalid {self} password type")
				valid = False


			if		valid : self.loggy.debug("Credentials probe validated")
			return	valid




	def build(self, credentials :Dict[str,str | int]) -> Dict[str,str | List[str]] :

		"""
			Core method for LetterBuilder implementation of standard SMTP library. Accepts "credentials"
			dictionary with email server connection information, which must include such key-value pairs as:
				"endpoint":	email server endpoint address string,
				"port":		email server address port as integer,
				"password":	password for authorization on the server with very first SenderField address
							as login.
			Returns fetched by LetterBuilder.build letter dictionary in case letter was sent to every
			recipient, which means SMTP connection response for a letter sending was not a dictionary with
			rejected recipients entities.
		"""

		if	self.is_connectable(credentials):
			if	self.is_buildable(current_build := super().build()):

				current_sender	= current_build["sender"][0].rstrip(';')
				current_recip	= current_build["recipient"]
				current_subject	= current_build["subject"] or str()
				current_body	= current_build["body"] or str()
				current_cc		= current_build["cc"]
				current_bcc		= current_build["bcc"]

				if	current_cc is not None	: current_recip += current_cc
				if	current_bcc is not None	: current_recip += current_bcc

				try:

					self.loggy.info(f"{self} commence {current_sender} letter build")
					self.current_smtp_connection = SMTP_SSL(

						credentials["endpoint"],
						credentials["port"],
						timeout=30,
					)
					self.loggy.debug(f"SMTP connection established")


					login = self.current_smtp_connection.login(current_sender, credentials["password"])
					self.loggy.debug(f"Login status: {login}")


					response = self.current_smtp_connection.sendmail(

						current_sender,
						[ address.strip() for address in current_recip.split(";") if address ],
						f"From: {current_sender}\r\n"
						f"To: {current_recip}\r\n"
						f"Subject: {current_subject}\r\n\r\n"
						f"{current_body}"
					)


				except	Exception as E : self.loggy.info(f"{self} failed due to {patronus(E)}")
				else:
					if	isinstance(response, dict):
						if	len(response):
							for recipient,details in response.items():

								# Method "smtp.sendmail" will return normally if the mail is accepted for
								# at least one recipient. Otherwise it will raise an exception. If this
								# method does not raise an exception, it returns a dictionary, with one
								# entry for each recipient that was refused. Each entry contains a tuple of
								# the SMTP error code and the accompanying error message sent by the server.
								self.loggy.info(f"{self} didn't sent to {recipient} {details}")
						else:

							self.loggy.info(f"{self} all recipients accepted")
							return	current_build
					else:	self.loggy.debug(f"Unexpected response \"{response}\"")
				finally:
						if	hasattr(self, "current_smtp_connection") : self.current_smtp_connection.quit()







