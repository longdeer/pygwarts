from pygwarts.irma.contrib						import LibraryContrib
from pygwarts.irma.shelve						import LibraryShelf
from pygwarts.irma.access.utils					import byte_size_string
from pygwarts.hagrid.thrivables					import Copse
from pygwarts.hagrid.sprouts					import fssprout
from pygwarts.hagrid.planting					import Flourish
from pygwarts.hagrid.cultivation.registering	import PlantRegister
from pygwarts.hagrid.cultivation.registering	import PlantRegisterQuerier








r1 = "first source folder"
r2 = "second source folder"
r3 = "third source folder"








class Hagrid(Copse):

	""" Hagrid scheme for only gathering fs information about source folders """

	class loggy(LibraryContrib):

		handler		= "logger file path (optional)"
		init_name	= "hagrid (optional)"

	@fssprout(r3)
	@fssprout(r2)
	@fssprout(r1)
	@PlantRegister("garden")
	class walk(Flourish):		pass
	class garden(LibraryShelf):	pass








if	__name__ == "__main__":

	hagrid = Hagrid()
	hagrid.walk()

	prq = PlantRegisterQuerier(hagrid.garden)

	r1_size = byte_size_string(prq.WG(r1, apparent=True))
	r2_size = byte_size_string(prq.WG(r2, apparent=True))
	r3_size = byte_size_string(prq.WG(r3, apparent=True))

	r1_tree = sorted(prq.content(r1,r1), reverse=True)
	r2_tree = sorted(prq.content(r2,r2), reverse=True)
	r3_tree = sorted(prq.content(r3,r3), reverse=True)

	r1_dirs = prq.TG(r1)
	r2_dirs = prq.TG(r2)
	r3_dirs = prq.TG(r3)

	r1_files = prq.LG(r1)
	r2_files = prq.LG(r2)
	r3_files = prq.LG(r3)

	hagrid.loggy.info(f"{r1} summary")
	for w,b in r1_tree : hagrid.loggy.info(f"{b}: {byte_size_string(w)}")
	hagrid.loggy.info(f"Total size: {r1_size}")
	hagrid.loggy.info(f"Total folders: {r1_dirs}")
	hagrid.loggy.info(f"Total files: {r1_files}")

	hagrid.loggy.info(f"{r2} summary")
	for w,b in r2_tree : hagrid.loggy.info(f"{b}: {byte_size_string(w)}")
	hagrid.loggy.info(f"Total size: {r2_size}")
	hagrid.loggy.info(f"Total folders: {r2_dirs}")
	hagrid.loggy.info(f"Total files: {r2_files}")

	hagrid.loggy.info(f"{r3} summary")
	for w,b in r3_tree : hagrid.loggy.info(f"{b}: {byte_size_string(w)}")
	hagrid.loggy.info(f"Total size: {r3_size}")
	hagrid.loggy.info(f"Total folders: {r3_dirs}")
	hagrid.loggy.info(f"Total files: {r3_files}")







