from typing									import List
from typing									import Dict
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.chests				import KeyChest
from pygwarts.magical.spells				import flagrate








class LetterBuilder(KeyChest):

	"""
		hedwig.mail core class that is a super class for letter composing objects. The KeyChest base
		allows every descent ObjectField letter field to be included for a build. That including takes
		place during initiation and further functionality implemented in following members:
			Field			- the object which upon called on a letter field will produce the final
							value for such letter field; this is the general way for building fields;
			mandatoryField	- additional field value gathering object, that makes use of "Field" and
							extends it with result verification, so means it is used for letter fields
							that must return some value;
			is_buildable	- helper method that validates the consistency of a dictionary that is to
							be obtained from a "build" method;
			build			- core method that initiates the process of letter building by invoking
							every letter field; is a super method for every builder.
	"""

	class Field(Transmutable):

		"""
			hedwig.mail letter fields main obtainer. Accepts a string "field_name" that must represent the
			key to be searched in upper layer KeyChest LetterBuilder. Also accepts "as_string" boolean
			flag that decides whether output value will be concatenated string of a list of strings right
			before concatenation. In other words "Field" gather mapped with "field_name" fields invocations
			results, and either return it as a list or as a joined string.
		"""


		def __call__(self, field_name :str, as_string=True) -> str | List[str] | None :
			self.loggy.debug(f"Obtaining {field_name} field value")


			if	hasattr(self, "_UPPER_LAYER") and isinstance(self._UPPER_LAYER, KeyChest):
				if	isinstance(field_source := self._UPPER_LAYER[field_name], list):
					current_field = str() if as_string else list()


					# Every item in "field_name" mapping must be a callable that will return string.
					# It is the interface for the letter fields objects "Field" relies on. Any other
					# items encountered will be skipped.
					for current_source in field_source:
						if	callable(current_source):
							if	isinstance(current_value := current_source(),str):


								current_field += current_value if as_string else [ current_value ]


							else:	self.loggy.debug(f"{current_source} returned not a string")
						else:		self.loggy.debug(f"{current_source} is not callable")


					flen = len(current_field)
					self.loggy.info(

						"%s field obtained %s %s%s"%(
							field_name,
							flen,
							"symbol" if as_string else "item",
							flagrate(flen)
						)
					)


					# It is a probable situation, that "current_field" end up as an empty string or list,
					# cause every processed field was just skipped, so any obtainer must account for
					# this falsy variant.
					return	current_field
				else:		self.loggy.debug(f"{field_name} field is not a list")
			else:			self.loggy.debug(f"{field_name} field cannot be included for building")




	class mandatoryField(Transmutable):

		"""
			hedwig.mail letter fields additional obtainer. Acts the same way as "Field" cause invokes it,
			but also logs a critical level message if "Field" returns a falsy value, like None it case
			"Field" could not obtain field value, or an empty list or string if all fields was skipped.
		"""

		def __call__(self, field_name :str, as_string=True) -> str | None :

			if		(field_value := self.Field(field_name, as_string)): return field_value
			else:	self.loggy.critical(f"{self._UPPER_LAYER} {field_name} field failed")




	def is_buildable(self, candidate :Dict[str,str | List[str]]) -> bool :

		"""
			Helper method that validates a dictionary that represents current letter build, which is mapping
			of typical letter fields names with corresponding values that "Field" object produces after such
			field names processing. Basically this dictionary must have 7 key-value pairs, 2 of them are
			mandatory and the rest is optional, that means for mandatory values except for optional values,
			None is not allowed. Returns boolean values that represents validation status.
		"""

		return	(

			isinstance(candidate, dict)							and
			len(candidate) == 7									and
			isinstance(candidate.get("sender"), list)			and
			isinstance(candidate.get("recipient"), str)			and
			isinstance(candidate.get("cc"), str | None)			and
			isinstance(candidate.get("bcc"), str | None)		and
			isinstance(candidate.get("subject"), str | None)	and
			isinstance(candidate.get("body"), str | None)		and
			isinstance(candidate.get("attachment"), list | None)
		)




	def build(self) -> Dict[str,str | List[str]] | None :

		"""
			The core method which is super for builders. Gathers all possible regular field names and
			creates a dictionary mapping to be returned. First verifies mandatory fields like "sender"
			and "recipient" are obtained, then goes for optional fields "cc", "bcc", "subject", "body"
			and "attachment". Returns compatible with "is_buildable" method check dictionary in case
			mandatory fields are obtained, None otherwise.
		"""

		if	isinstance(sender := self.mandatoryField("sender", as_string=False), list):
			if	isinstance(recipient := self.mandatoryField("recipient"), str):

				return	{

					"sender":		sender,
					"recipient":	recipient,
					"cc":			self.Field("cc"),
					"bcc":			self.Field("bcc"),
					"subject":		self.Field("subject"),
					"body":			self.Field("body"),
					"attachment":	self.Field("attachment", as_string=False),
				}







