import	re
from	typing							import Literal
from	pygwarts.magical.spells			import flagrate
from	pygwarts.irma.access.volume		import LibraryVolume
from	pygwarts.irma.access.handlers	import AccessHandler








class GroupParser(AccessHandler):

	"""
		Super implementation of handler, that suggests parsing the line it receives. Parsing occurs with
		the "rpattern" filed, which must be a valid regular expression or a compilable string. Basically
		this super is just for validating "rpattern" field. If it is neither a string nor a Pattern,
		corresponding warning message will be logged and "rpattern" will stay as it is.
	"""

	rpattern :str | re.Pattern

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)


		match getattr(self, "rpattern", None):
			case str():

				self.rpattern = re.compile(self.rpattern)
				self.loggy.debug(f"Accepted string \"{self.rpattern.pattern}\"")

			case re.Pattern():	self.loggy.debug(f"Accepted pattern \"{self.rpattern.pattern}\"")
			case None:			self.loggy.warning(f"{self} doesn't have pattern for parsing")
			case _:				self.loggy.warning(f"{self} has invalid pattern for parsing")








class TargetHandler(GroupParser):

	"""
		implementation of handler, that suggests parsing single value from a line it receives, by
		the name group "target". It is implies, that "rpattern" regex must contain such name group
		"target" that must encompass desired text to catch. In case of successful parse, assigns
		caught "target" string value as it's "recap" mapping in a LibraryVolume "volume" object and
		returns True. It must be noticed, that multiple parsing will lead to reassign of "recap"
		mapping. Returns None in any other case. Doesn't handle possible regex search Exception.
	"""

	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

		if	isinstance(getattr(self, "rpattern", None), re.Pattern):
			if	(match := self.rpattern.search(line)) and (target := match.group("target")):
				if	self.registered(volume):


					volume[self]["recap"] = target
					self.loggy.debug(f"Recap set to \"{target}\"")


					return True
			else:	self.loggy.debug("No match for target")








class TargetNumberAccumulator(GroupParser):

	"""
		implementation of handler, that suggests parsing single numeric value from a line it receives, by
		the name group "target". It is implies, that "rpattern" regex must contain such name group
		"target" that must encompass desired numerical text to catch. In case of successful parse,
		adds caught "target" numerical value to it's "recap" mapping in a LibraryVolume "volume" object,
		which by default will be set to 0, and returns True. Returns None in any other case. Doesn't handle
		possible regex search Exception.
	"""

	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

		if	isinstance(getattr(self, "rpattern", None), re.Pattern):
			if	(match := self.rpattern.search(line)) and (target := match.group("target")):
				if	self.registered(volume):


					current = volume[self]["recap"] = eval(f"volume[self].setdefault('recap',0) +{target}")
					self.loggy.debug(f"Recap accumulation is \"{current}\"")


					return True
			else:	self.loggy.debug("No match for target")








class TargetStringAccumulator(GroupParser):

	"""
		implementation of handler, that suggests parsing single value from a line it receives, by
		the name group "target". It is implies, that "rpattern" regex must contain such name group
		"target" that must encompass desired text to catch. In case of successful parse, adds
		caught "target" string value to it's "recap" mapping in a LibraryVolume "volume" object, which
		by default will be set to a list, and returns True. Returns None in any other case. Doesn't
		handle possible regex search Exception, or situation when "recap" mapping already exist and
		is not a list.
	"""

	def __call__(self, line :str, volume :LibraryVolume) -> Literal[True] | None :

		if	isinstance(getattr(self, "rpattern", None), re.Pattern):
			if	(match := self.rpattern.search(line)) and (target := match.group("target")):
				if	self.registered(volume):


					volume[self].setdefault("recap",[]).append(target)
					rl = len(volume[self]["recap"])
					self.loggy.debug(f"Recap extended to {rl} item{flagrate(rl)}")


					return True
			else:	self.loggy.debug("No match for target")







