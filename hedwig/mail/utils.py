import	re
from	pygwarts.magical.philosophers_stone	import Transmutable








EMAIL_REGEX_PATTERN = re.compile(

	r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")"
	"@"
	r"[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?(\.[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?)+"
)








class EmailValidator(Transmutable):

	"""
		Utility class to validate email address. Accepts string, that must represent an email to
		validate. Returns a string argument "address" if it is valid email address, None otherwise - if
		validation failed or if "email" argument is not a string.
		Validation goes by "EMAIL_REGEX_PATTERN" regex, that is:
			1.	have a local part (part before the @-sign) that is strictly compliant with RFC 5321/5322;
			2.	have a domain part (part after the @-sign) that is a host name with at least two labels,
				each of which is at most 63 characters long.
	"""

	def __call__(self, email :str) -> str | None :

		if	isinstance(email, str):
			if	EMAIL_REGEX_PATTERN.fullmatch(email):

				self.loggy.debug(f"Email address \"{email}\" validated")
				return	email

		self.loggy.info(f"Invalid email address \"{email}\"")







