import	os
from	typing							import List
from	typing							import Dict
from	pygwarts.hedwig.mail.builder	import LetterBuilder
from	pygwarts.magical.spells			import patronus








class ThunderbirdBuilder(LetterBuilder):

	"""
		LetterBuilder implementation of Thunderbird client. Fetches letter fields by LetterBuilder.build
		and invokes cli compose option by os.system for every SenderField entity provided. By default
		Thunderbird client will automatically use default account for sender if provided one not found.
		Thunderbird binary must be included in path environment variable in order to os.system be able
		to call it. Handles no Exceptions that might be raised during os.system call.
	"""

	def build(self) -> Dict[str,str | List[str]] | None :

		"""
			Core method for LetterBuilder implementation of Thunderbird client. Handles no Exceptions.
			Returns fetched by LetterBuilder.build letter dictionary in case of successful sending,
			which is decided by the exit code of compose command, or None otherwise.
		"""

		if	self.is_buildable(current_build := super().build()):

			current_recip	= current_build["recipient"]
			current_cc		= current_build["cc"]
			current_bcc		= current_build["bcc"]
			current_subject	= current_build["subject"]
			current_body	= current_build["body"]
			current_attach	= current_build["attachment"]
			current_call	= f"',to='{current_recip}'"


			if	current_cc is not None		: current_call += f",cc='{current_cc}'"
			if	current_bcc is not None		: current_call += f",bcc='{current_bcc}'"
			if	current_subject is not None : current_call += f",subject='{current_subject}'"
			if	current_body is not None	: current_call += f",body='{current_body}'"
			if	current_attach is not None	: current_call += f",attachment='{','.join(current_attach)}'"


			for sender in current_build["sender"]:
				self.loggy.info(f"{self} commence {sender.rstrip(';')} letter build")

				if	os.name == "posix":

					final_call = f"thunderbird -compose \"from='{sender}{current_call}\""
				else:
					final_call = str(

						"C:\\\"Program Files\"\\\"Mozilla Thunderbird\"\\thunderbird.exe"
						f" -compose \"from='{sender}{current_call}\""
					)

				if		not os.system(final_call): self.loggy.info("Letter successfully composed")
				else:	self.loggy.warning("Compose exit code was not 0")
			return		current_build
		else:			self.loggy.info(f"{self} letter build check failed")








class OutlookBuilder(LetterBuilder):

	"""
		LetterBuilder implementation of Outlook client. First of all will try to import win api module and
		to dispatch Outlook application. If ModuleNotFoundError or any other Exception raised during this,
		it is assumed current builder is not applicable for current system. In case of success will fetches
		letter fields by LetterBuilder.build and uses Outlook api to build and explicitly send letter, which
		means there will be no automatic sending, but the constructor window invocation, filled with built
		letter fields. As building goes for every SenderField entity provided, and Outlook restricts sender
		field usage, every SenderField entity will be checked in list of current session accounts beforehand.
		Handles no Exceptions after Outlook application dispatching.
	"""

	def build(self) -> Dict[str,str | List[str]] | None :

		"""
			Core method for LetterBuilder implementation of Outlook client. Handles only win api Exceptions.
			As letter sending for clients is oriented to letter window construction, return value is
			fetched by LetterBuilder.build letter dictionary in case "build" was handed to a window,
			which is only decided by the api call, or None otherwise.
		"""

		try:

			import win32com.client as win
			app = win.Dispatch("Outlook.Application")

		except	ModuleNotFoundError	: self.loggy.info(f"{self} is not applicable")
		except	Exception as E		: self.loggy.info(f"{self} failed due to {patronus(E)}")
		else:
			if	self.is_buildable(current_build := super().build()):


				self.loggy.debug(f"Found application {app}")
				accounts = { f"{acc};": acc for acc in app.Session.Accounts }


				current_cc		= current_build["cc"]
				current_bcc		= current_build["bcc"]
				current_subject	= current_build["subject"]
				current_body	= current_build["body"]
				current_attach	= current_build["attachment"]


				for sender in current_build["sender"]:
					if	(current_sender := accounts.get(sender)) is not None:


						self.loggy.info(f"{self} commence {sender.rstrip(';')} letter build")


						current_call	= app.CreateItem(0)
						current_call.To = current_build["recipient"]


						if	current_cc is not None		: current_call.CC = current_cc
						if	current_bcc is not None		: current_call.BCC = current_bcc
						if	current_subject is not None	: current_call.Subject = current_subject
						if	current_body is not None	: current_call.HTMLBody = current_body
						if	current_attach is not None	:

							for attachment in current_build["attachment"]:
								current_call.Attachments.Add(attachment)


						current_call._oleobj_.Invoke(64209, 0, 8, 0, current_sender)
						current_call.Display(True)
						self.loggy.info(f"Letter was handed to {app}")


					else:	self.loggy.info(f"Account for {sender.rstrip(';')} not found")
				return		current_build
			else:			self.loggy.info(f"{self} letter build check failed")







