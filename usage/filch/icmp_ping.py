from pygwarts.irma.contrib			import LibraryContrib
from pygwarts.filch.nettherin.icmp	import HostPing
from scapy.all						import sr
from scapy.all						import IP
from scapy.all						import ICMP








class Filch(HostPing):
	class loggy(LibraryContrib):

		handler		= "file handler path (optional)"
		init_name	= "filch (optional)"

	def pinger(self, addr :str, **kwargs) -> str | None :

		""" scapy ICMP ping request builder """

		R = sr(IP(dst=addr) /ICMP(), **kwargs)
		if len(R) and len(R[0]): return addr








if	__name__ == "__main__":

	filch = Filch()

	# send typical ping request
	# no verbose output, no retries, 1 sec timeout
	filch("ip4 address to ping", filch.pinger, retry=0, timeout=1, verbose=0)







