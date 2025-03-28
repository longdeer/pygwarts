from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.magical.time_turner.timers	import DIRTtimer
from pygwarts.irma.contrib					import LibraryContrib
from pygwarts.filch.linkindor				import EUI48_format
from pygwarts.filch.linkindor				import P_ARP_REQ
from pygwarts.filch.linkindor.sniffing		import ARPSniffer
from scapy.all								import sniff
from scapy.all								import Ether
from scapy.all								import ARP








if	__name__ == "__main__":

	# Initiating sniffing timer to 23 o'clock (for example, optional)
	if	(kill_timer := TimeTurner().diff(subtrahend=TimeTurner(timepoint="2300"))) <0:

		@DIRTtimer(T=-kill_timer)
		class Filch(ARPSniffer):

			class loggy(LibraryContrib):

				handler		= "file handler path (optional)"
				init_name	= "filch (optional)"

			def trap(self, FRAME :Ether):

				if	(MAC := EUI48_format(FRAME.src)) is not None:
					match FRAME[ARP].op:

						case 1:	self.loggy.info(f"{P_ARP_REQ.search(FRAME.summary()).group()} ({MAC})")
						case 2:	self.loggy.debug(f"{MAC} answer")
						case _:	self.loggy.debug(FRAME.summary())








		filch = Filch()
		filch(sniff, filter="arp", prn=filch.trap)







