import	os
from	pathlib			import Path
from	pygwarts.tests	import PygwartsTestCase








class HedwigTestCase(PygwartsTestCase):

	"""
		pygwarts.hedwig tests super class
	"""

	HEDWIG_ROOT					= Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig"
	HEDWIG_MAIL_UTILS_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig" /"mu.loggy")
	HEDWIG_MAIL_LETTER_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig" /"ml.loggy")
	HEDWIG_MAIL_LETTER_AHANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig" /"mla.loggy")
	HEDWIG_MAIL_BUILDER_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig" /"mb.loggy")
	HEDWIG_MAIL_CLIENT_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig" /"mc.loggy")
	HEDWIG_MAIL_SMTP_HANDLER	= str(Path(PygwartsTestCase._PygwartsTestCase__CWD) /"hedwig" /"ms.loggy")
	VALID_EMAILS = (

		"email@example.com",
		"firstname.lastname@example.com",
		"EMAIL@subdomain.example.com",
		"firstname+lastname@example.com",
		"email@123.123.123.123",
		"1234567890@example.com",
		"email@example-one.com",
		"_______@example.com",
		"email@example.name",
		"email@example.museum",
		"email@example.co.jp",
		"firstname-lastname@example.com",
		"email@example.web",
		"email@111.222.333.44444",
	)
	INVALID_EMAILS = (

		"",
		"plainaddress",
		"#@%^%#$@#$@#.com",
		"@example.com",
		"Joe Smith <email@example.com>",
		"email.example.com",
		"email@example@example.com",
		".email@example.com",
		"email.@example.com",
		"email..email@example.com",
		"email@[123.123.123.123]",
		"email@example.com (Joe Smith)",
		"email@example",
		"email@-example.com",
		"email@example..com",
		"Abc..123@example.com",
		" email@example.com",
		"em;ail@example.com",
		"email@ex;ample.com",
	)







