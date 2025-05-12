from os													import path as ospath
from pygwarts.magical.philosophers_stone				import Transmutable
from pygwarts.magical.philosophers_stone.transmutations	import ControlledTransmutation
from pygwarts.magical.spells							import geminio
from pygwarts.magical.spells							import flagrate
from pygwarts.magical.spells							import patronus








def byte_size_string(value :int | float | str) -> str | None :

	"""
		Utility function that accepts a numeric "value" and calculates the size in bytes which that value
		represents to return it as pretty string. The "value" must be convertible to float and will be
		finally converted to integer. The result string will consist of numbers and letters according
		to relevant bytes. The sign will be preserved, allowing to obtain strings with negative size.
		Maximum size is 999 terabyte, according to modern (2024) technologies. If "value" conversion
		failed or if "value" is more than 15 digits, None will be returned.
	"""

	try:

		byte_size = str(int(float(str(value))))
		sign = "-" if byte_size[0] == "-" else ""
		byte_size = byte_size.lstrip("-")

	except:	return
	else:
		if	len(byte_size) <16:
			return	sign + " ".join(

				f"{int(S)}{B}" for S,B in zip(

					( byte_size.zfill(15)[i:i+3] for i in range(0,16,3) ),
					( "T", "G", "M", "K", "B", )

				)	if int(S)
			)		or "0B"








class TextWrapper(ControlledTransmutation):

	"""
		pygwarts utility decorator, that serves as an instrument for text editing, which is just addition
		of a text before (header) and after (footer). As ControlledTransmutation class, accepts
		corresponding "header" and "footer" arguments, which must be strings and defaulted to empty strings,
		in case only one is needed. In mutable chain acts as a mutation - takes decorated Transmutable,
		which upon call must return a string value to be modified by the decoration. Returns final string,
		or None if only decorated object returns not a string. Doesn't handles any Exceptions, only
		explicitly converts "header" and "footer" to strings at initiation time and once again in
		decoration's interpolation.
	"""

	def __init__(self, header :str =str(), footer :str =str()):

		self.header = str(header)
		self.footer = str(footer)

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		header = self.header
		footer = self.footer


		class TextWrapping(geminio(layer)):
			def __call__(self, *args, **kwargs) -> str | None :

				if	isinstance(current_value := super().__call__(*args, **kwargs), str):

					final_value = f"{header}{current_value}{footer}"
					vlen = len(final_value)
					self.loggy.debug(f"Wrapped text now {vlen} symbol{flagrate(vlen)}")


					return	final_value


				self.loggy.debug("Text value to wrap not found")
		return	TextWrapping








class WriteWrapper(ControlledTransmutation):

	"""
		pygwarts utility decorator, that serves as an instrument for saving text to a file. As
		ControlledTransmutation class, accepts "path" as string where to write text, and two boolean
		flags, "rewrite" which decides whether "path" will be opened in "w" or "a" mode, and "text_mode"
		which decides whether written text will be returned or a "path" in case of success. In mutable chain
		acts as a mutation - takes decorated Transmutable, which upon call must return a text to be written.
		Returns None if neither text could be obtained nor an exception was raised in writing time.
	"""

	def __init__(self, path :str, *, rewrite :bool =False, text_mode :bool =True):

		self.path = path
		self.rewrite = rewrite
		self.text_mode = text_mode

	def _mutable_chain_injection(self, layer :Transmutable) -> Transmutable :

		path = self.path
		rewrite = self.rewrite
		text_mode = self.text_mode


		class WriteWrapping(geminio(layer)):
			def __call__(self, *args, **kwargs) -> str | None :


				if	isinstance(current_text := super().__call__(*args, **kwargs), str):
					self.loggy.debug(f"Writing {(tl := len(current_text))} symbol{flagrate(tl)}")


					if	isinstance(path, str):

							try:

								with open(path, "w" if rewrite else "a") as descriptor:

									descriptor.write(current_text)
									self.loggy.info(f"Written to {path}")

							except	Exception as E : self.loggy.debug(f"Writing failed due to {patronus(E)}")
							else:	return current_text if text_mode else path


					else:	self.loggy.debug("Path to write is not a string")
				else:		self.loggy.debug("Text to write not fetched")


		return	WriteWrapping







