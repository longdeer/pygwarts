from pygwarts.filch.marauders_map import MaraudersMap








# KeyChest child that serves as a network map class. Once populated from CSV file, stores the ip4 and MAC
# mappings as 2 dictionaries. When "CSV" method is invoked it must be supplied with path to file, delimiter
# string, number of columns to extract ip4 address, MAC address, host name and host description.
mapper = MaraudersMap()
mapper.CSV("file to CSV table", ";", IP4=0, MAC=1, NAME=2, DESC=3)
mapper.ip4								# Returns ip4 addresses mapping dictionary reference (if any, else None).
mapper.ip4map("10.1.1.1")				# Returns "10.1.1.1" mapping dictionary reference (if any, else None).
mapper.ip4map_mac("10.1.1.1")			# Returns "10.1.1.1" mapped MAC address (if any, else None).
mapper.ip4map_name("10.1.1.1")			# Returns "10.1.1.1" mapped host name (if any, else None).
mapper.ip4map_desc("10.1.1.1")			# Returns "10.1.1.1" mapped host description (if any, else None).
mapper.mac								# Returns MAC addresses mapping dictionary reference (if any, else None).
mapper.macmap("08:00:27:15:56:59")		# Returns "08:00:27:15:56:59" mapping dictionary reference (if any, else None).
mapper.macmap_ip4("08:00:27:15:56:59")	# Returns "08:00:27:15:56:59" mapped ip4 address (if any, else None).
mapper.macmap_name("08:00:27:15:56:59")	# Returns "08:00:27:15:56:59" mapped host name (if any, else None).
mapper.macmap_desc("08:00:27:15:56:59")	# Returns "08:00:27:15:56:59" mapped host description (if any, else None).







