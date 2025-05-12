from typing									import List
from typing									import Dict
from csv									import reader	as csv_reader
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.chests				import KeyChest
from pygwarts.magical.spells				import patronus
from pygwarts.magical.spells				import flagrate
from pygwarts.filch.linkindor				import EUI48_format
from pygwarts.filch.nettherin				import validate_ip4








class MaraudersMap(KeyChest):

	"""
		filch utility class that serves as a runtime database for network traffic. Allows mapping of
		hosts addresses with corresponding information to be accessed as a dictionary. For current
		implementation following mapping can be maintained in "IP4" subdictionary:
							MAC		(host physical address)
			IP4 address		NAME	(host alias/netbios name)
							DESC	(host description)
		and also in "MAC" subdictionary:
							IP4		(host IP version 4 address)
			MAC address		NAME	(host alias/netbios name)
							DESC	(host description)
		According to scheme above, there will be two dictionaries in a KeyChest, IP4 and MAC. Every IP4
		and MAC addresses will be mapped with each other in corresponding dictionary, along with two
		additional fields. It is possible to have only IP4 or MAC for mapping, so it will be mapped with
		Nones and represents the addresses collection.
	"""

	@property
	def ip4(self) -> Dict[str,Dict[str,str]] | None :

		""" Property that returns a dictionary mapped to "IP4" or None. """

		if	isinstance(mapping := self["IP4"], dict): return mapping


	def ip4map(self, addr :str) -> Dict[str,str] | None :

		"""
			Mapping method that accepts IP4 address string and searches for corresponding mapping.
			If mapping found and it is a dictionary, returns it, no matter it's content.
			Returns None in all other cases.
		"""

		if	isinstance(self.ip4, dict) and isinstance(mapping := self.ip4.get(str(addr)), dict):
			return mapping


	def ip4map_mac(self, addr :str) -> str | None :

		"""
			Mapping method that accepts IP4 address string and searches for corresponding mapping.
			If mapping found and it is a dictionary that has "MAC" mapped to a string, returns it.
			Returns None in all other cases.
		"""

		if	isinstance(mapping := self.ip4map(addr), dict) and isinstance(mac := mapping.get("MAC"), str):
			return mac


	def ip4map_name(self, addr :str) -> str | None :

		"""
			Mapping method that accepts IP4 address string and searches for corresponding mapping.
			If mapping found and it is a dictionary that has "NAME" mapped to a string, returns it.
			Returns None in all other cases.
		"""

		if	isinstance(mapping := self.ip4map(addr), dict) and isinstance(name := mapping.get("NAME"), str):
			return name


	def ip4map_desc(self, addr :str) -> str | None :

		"""
			Mapping method that accepts IP4 address string and searches for corresponding mapping.
			If mapping found and it is a dictionary that has "DESC" mapped to a string, returns it.
			Returns None in all other cases.
		"""

		if	isinstance(mapping := self.ip4map(addr), dict) and isinstance(desc := mapping.get("DESC"), str):
			return desc




	@property
	def mac(self) -> Dict[str,Dict[str,str]] | None :

		""" Property that returns a dictionary mapped to "MAC" or None. """

		if	isinstance(mapping := self["MAC"], dict): return mapping


	def macmap(self, addr :str) -> Dict[str,str] | None :

		"""
			Mapping method that accepts physical address string and searches for corresponding mapping.
			If mapping found and it is a dictionary, returns it, no matter it's content.
			Returns None in all other cases.
		"""

		if	isinstance(self.mac, dict) and isinstance(mapping := self.mac.get(str(addr)), dict):
			return mapping


	def macmap_ip4(self, addr :str) -> str | None :

		"""
			Mapping method that accepts physical address string and searches for corresponding mapping.
			If mapping found and it is a dictionary that has "IP4" mapped to a string, returns it.
			Returns None in all other cases.
		"""

		if	isinstance(mapping := self.macmap(addr), dict) and isinstance(ip4 := mapping.get("IP4"), str):
			return ip4


	def macmap_name(self, addr :str) -> str | None :

		"""
			Mapping method that accepts physical address string and searches for corresponding mapping.
			If mapping found and it is a dictionary that has "NAME" mapped to a string, returns it.
			Returns None in all other cases.
		"""

		if	isinstance(mapping := self.macmap(addr), dict) and isinstance(name := mapping.get("NAME"), str):
			return name


	def macmap_desc(self, addr :str) -> str | None :

		"""
			Mapping method that accepts physical address string and searches for corresponding mapping.
			If mapping found and it is a dictionary that has "DESC" mapped to a string, returns it.
			Returns None in all other cases.
		"""

		if	isinstance(mapping := self.macmap(addr), dict) and isinstance(desc := mapping.get("DESC"), str):
			return desc








	class CSV(Transmutable):

		"""
			Helper class that serves as an instrument of maintaining the upper layer "database" by
			populating it from readable csv file. Must be supplied with two positional arguments
			"path" that represents path to csv file and "delimiter" to parse file. It also accepts
			keyword-only arguments that must represents the indices of corresponding fields in
			csv file lines. For every index provided, if it fits into csv file line, corresponding value
			will be extracted. For crucial IP4 and MAC fields corresponding value will be verified.
			If some value cannot be obtained it will be set to None. IP4 and MAC mapping will proceed
			only for validated values.
		"""

		def __call__(
						self,
						path		:str,
						delimiter	:str	=",",
						*,
						IP4			:int	=None,
						MAC			:int	=None,
						NAME		:int	=None,
						DESC		:int	=None,
					):

			self.loggy.debug(f"Reading csv from \"{path}\"")
			IP4_state = len(self._UPPER_LAYER["IP4"]) if self._UPPER_LAYER["IP4"] is not None else 0
			MAC_state = len(self._UPPER_LAYER["MAC"]) if self._UPPER_LAYER["MAC"] is not None else 0
			count = 0

			try:

				with open(path) as map_source:
					for row in csv_reader(map_source, delimiter=delimiter):


						current_IP4		= validate_ip4(self.extract(IP4, row))
						current_MAC		= EUI48_format(self.extract(MAC, row))
						current_NAME	= self.extract(NAME, row)
						current_DESC	= self.extract(DESC, row)
						count += 1


						if	current_IP4 is not None:

							self._UPPER_LAYER(

								current_IP4,
								{
									"MAC":	current_MAC,
									"NAME":	current_NAME,
									"DESC":	current_DESC,
								},
								"IP4",
								mapped=False,
							)
							self.loggy.debug(f"IP version 4 address {current_IP4} mapping done")


						if	current_MAC is not None:

							self._UPPER_LAYER(

								current_MAC,
								{
									"IP4":	current_IP4,
									"NAME":	current_NAME,
									"DESC":	current_DESC,
								},
								"MAC",
								mapped=False,
							)
							self.loggy.debug(f"Physical address {current_MAC} mapping done")


				self.loggy.debug(f"{count} record{flagrate(count)} read")


			except	Exception as E : self.loggy.debug(f"Failed to open CSV due to {patronus(E)}")
			else:

				if	self._UPPER_LAYER["IP4"] is not None:

					IP4_new = (ip4l := len(self._UPPER_LAYER["IP4"])) - IP4_state
					self.loggy.debug(f"{IP4_new} new IP4 mapping{flagrate(IP4_new)} done")
					self.loggy.debug(f"{ip4l} IP4 mapping{flagrate(ip4l)} total")


				if	self._UPPER_LAYER["MAC"] is not None:

					MAC_new = (macl := len(self._UPPER_LAYER["MAC"])) - MAC_state
					self.loggy.debug(f"{MAC_new} new MAC mapping{flagrate(MAC_new)} done")
					self.loggy.debug(f"{macl} MAC mapping{flagrate(macl)} total")




		def extract(self, index :int, source :List[str]) -> str | None :

			"""
				Utility method that will try to extract "index" value from "source" list and return
				it. Assumes "source" is a list of strings. Returns None if "source" is not a list or
				"index" is not an integer in range of "source" length.
			"""

			if	isinstance(source, list):
				if	isinstance(index, int):
					if	-1 <index <len(source):


						record = source[index]
						self.loggy.debug(f"Index {index} record \"{record}\" obtained")


						return	record
					else:		self.loggy.debug(f"Out of range index {index}")
				else:			self.loggy.debug(f"Invalid index {index}")
			else:				self.loggy.debug(f"Invalid source {source}")







