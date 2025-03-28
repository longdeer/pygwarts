from socket									import socket
from socket									import AF_INET
from socket									import SOCK_STREAM
from pygwarts.magical.philosophers_stone	import Transmutable
from pygwarts.magical.spells				import patronus
from pygwarts.filch.nettherin				import is_valid_ip4
from pygwarts.filch.transportclaw			import is_valid_port








class PortScanner(Transmutable):

	"""
		Transport layer class for scanning host's listening ports. Must accept positional arguments:
			target_ip	- IP4 address of target host to scan, as string;
			target_port	- integer in range 0-65535 which represents a port number to scan.
		Once "target_ip" and "target_port" are validated, the classic socket instance will be created
		to try establish connection with target. If connection will be closed with exit code 0 it must
		mean the port is opened and listening, so True will be returned. Any other exit code will be
		treated as port closed, so False will be returned. In any other situations, including Exception
		raise, corresponding logging will occur for identification and None will be returned.
	"""

	def __call__(self, target_ip :str, target_port :int) -> bool | None :


		if	is_valid_ip4(target_ip):
			if	is_valid_port(target_port):
				self.loggy.debug(f"Scanning {target_ip}:{target_port}")


				try:

					with socket(AF_INET, SOCK_STREAM) as connection:
						code = connection.connect_ex(( target_ip,target_port ))


						if		code == 0: self.loggy.info(f"{target_ip}:{target_port} listening")
						else:	self.loggy.debug(f"Socket write error {code}")
						return	not code


				except	Exception as E: self.loggy.debug(f"Scanner failed with {patronus(E)}")
			else:		self.loggy.debug(f"Invalid port \"{target_port}\"")
		else:			self.loggy.debug(f"Invalid target \"{target_ip}\"")







