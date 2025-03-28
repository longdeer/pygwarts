from operator							import getitem
from ipaddress							import ip_network
from pygwarts.irma.contrib				import LibraryContrib
from pygwarts.filch.linkindor.discovery	import HostDiscovery
from scapy.all							import srp
from scapy.all							import Ether
from scapy.all							import ARP








class Filch(HostDiscovery):
	class loggy(LibraryContrib):

		handler		= "file handler path (optional)"
		init_name	= "filch (optional)"

	def discoverer(self, addr :str, **kwargs) -> str | None :

		""" scapy ARP request builder """

		R = srp(Ether(dst="ff:ff:ff:ff:ff:ff") /ARP(pdst=addr), **kwargs)
		if len(R) and len(R[0]): return getattr(getattr(getitem(getitem(R,0),0),"answer"),"src")








if	__name__ == "__main__":

	filch = Filch()

	# scan network without 0 and 255 addresses (slicing)
	# no verbose output, no retries, 1 sec timeout
	for ip4 in list(ip_network("ip4 network address/mask length"))[1:-1]:
		filch(str(ip4), filch.discoverer, retry=0, timeout=1, verbose=0)







