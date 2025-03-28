from pygwarts.irma.shelve import LibraryShelf








# LibraryShelf class is such extended version of KeyChest class. It consists of 2 KeyChest objects,
# "real_shelf" and "magical_shelf". "real_shelf" is the main mapping, almost all members of LibraryShelf
# are operates on "real_shelf". It also has some KeyChest members. "magical_shelf" is a kind of running
# shelf, like a buffer, according to "real_shelf". __call__ is the direct access to "magical_shelf".
shelf = LibraryShelf()
# Creates mapping in "real_shelf" and toggles "modified".
shelf.grab("shelve file path")
# Unloads "real_shelf", creates mapping in "real_shelf" and toggles "modified".
shelf.grab("shelve file path", rewrite=True)
# Creates mapping in "real_shelf" according to "_locker_" key in file (if exist) to ensure
# special order, toggles "modified".
shelf.grab("shelve file path", from_locker=True)
shelf[1] = "breakfast"			# Inserts in both "real_shelf" and "magical_shelf" and toggles "modified".
shelf(2, "lunch")				# Inserts in "magical_shelf" and toggles "modified".
shelf(3, "dinner", silent=True)	# Inserts in "magical_shelf" and doesn't toggles "modified".
shelf(1)						# Returns "breakfast" (mapping for 1 in "magical_shelf").
shelf()							# Returns "magical_shelf" reference (main way to access "magical_shelf").
shelf(4)						# Returns None (KeyChest's return for non-existent key).
shelf[1]						# Returns "breakfast" (mapping for 1 in "real_shelf")
shelf[3]						# Returns None (3 mapped only in "magical_shelf")
shelf.diff						# Returns "real_shelf" length - "magical_shelf" length.
shelf.real_diff					# Returns "real_shelf" - "magical_shelf" keys set.
shelf.magical_diff				# Returns "magical_shelf" - "real_shelf" keys set.
shelf.unload(magical=True)		# Unloads both "real_shelf" and "magical_shelf" KeyChest's.
# Saving "real_shelf" as a new shelve file (erases existent) with "_locker_" key (order list).
shelf.produce("new shelve file path", rewrite=True, locker_mode=True)
# Saving "magical_shelf" as a shelve file, ignoring "modified" flag, creates parents directories.
shelf.produce("new shelve file path", magical=True, ignore_mod=True, strict_mode=False)








# Providing "grabbing" in declaration allows "grab" invoke during initiation,
# without setting "modified" to True.
class NewShelf(LibraryShelf):

	grabbing	= "shelve file path"
	producing	= "new shelve file path"

shelf = NewShelf()				# shelve file already grabbed, "modified" NOT toggled.
shelf.produce(ignore_mod=True)	# shelve file saved to path from "producing" field.








# "reclaiming" flag allows saving new shelve file to the path of "grabbing" field.
class NewShelf(LibraryShelf):

	grabbing	= "shelve file path"
	reclaiming	= True

shelf = NewShelf()				# shelve file already grabbed, "modified" NOT toggled.
shelf.produce(ignore_mod=True)	# shelve file saved to path from "grabbing" field.







