from pygwarts.magical.time_turner			import TimeTurner
from pygwarts.hagrid.sprouts				import fssprout
from pygwarts.hagrid.thrivables				import Tree
from pygwarts.hagrid.thrivables				import Copse
from pygwarts.hagrid.bloom.leafs			import Transfer
from pygwarts.hagrid.planting				import Flourish
from pygwarts.hagrid.planting.leafs			import LeafPush
from pygwarts.hagrid.planting.peels			import ThrivingPeel
from pygwarts.hagrid.planting.peeks			import DraftPeek
from pygwarts.hagrid.cultivation.sifting	import SiftingController








if	__name__ == "__main__" :	
	if	(t := TimeTurner(timepoint=0)).w in "60":


		if t.w == "0" : t.travel(days=-1)


		friday		= t.sight(days=-1)
		thursday	= friday.sight(days=-1)
		wednesday	= thursday.sight(days=-1)
		tuesday		= wednesday.sight(days=-1)
		monday		= tuesday.sight(days=-1)


		friday_comp		= lambda N,O : friday.epoch		<= N <t.epoch
		thursday_comp	= lambda N,O : thursday.epoch	<= N <friday.epoch
		wednesday_comp	= lambda N,O : wednesday.epoch	<= N <thursday.epoch
		tuesday_comp	= lambda N,O : tuesday.epoch	<= N <wednesday.epoch
		monday_comp		= lambda N,O : monday.epoch		<= N <tuesday.epoch


		class Hagrid(Copse):

			"""
				hagrid archivation-sorting script, that implies invocation every Saturday or Sunday, to walk
				all source folders and move some files, according to what day of week it was last modified.
				The final destination for every file will be corresponding day folder, where first fill be
				created year folder and month folder in it, so destined files will be moved in such archive.
				TimeTurner objects attributes for ThrivingPeel might be also chosen according to OS type
				as single value, like "Ymd_aspath" for UNIX or "Ymd_aswpath" for windows. Also it must be
				noted, that "LeafPush" is used for preserving moved file meta data, which might cause a lot
				of warnings when destination folder need special permissions for meta data manipulations.
			"""

			class files(Transfer):		pass
			class Monday(Tree):

				@ThrivingPeel(monday.Y, monday.m, monday.d, to_peak=False)
				@DraftPeek(renew=False, comparator=monday_comp)
				class graft(LeafPush):	pass
				bough = "destination path for monday files"

			class Tuesday(Tree):

				@ThrivingPeel(tuesday.Y, tuesday.m, tuesday.d, to_peak=False)
				@DraftPeek(renew=False, comparator=tuesday_comp)
				class graft(LeafPush):	pass
				bough = "destination path for tuesday files"

			class Wednesday(Tree):

				@ThrivingPeel(wednesday.Y, wednesday.m, wednesday.d, to_peak=False)
				@DraftPeek(renew=False, comparator=wednesday_comp)
				class graft(LeafPush):	pass
				bough = "destination path for wednesday files"

			class Thursday(Tree):

				@ThrivingPeel(thursday.Y, thursday.m, thursday.d, to_peak=False)
				@DraftPeek(renew=False, comparator=thursday_comp)
				class graft(LeafPush):	pass
				bough = "destination path for thursday files"

			class Friday(Tree):

				@ThrivingPeel(friday.Y, friday.m, friday.d, to_peak=False)
				@DraftPeek(renew=False, comparator=friday_comp)
				class graft(LeafPush):	pass
				bough = "destination path for friday files"

			@fssprout("source path 3")	# Order does matter cause every sprout packs itself
			@fssprout("source path 2")	# before previous sprout, so the nearest to dispatcher
			@fssprout("source path 1")	# sprout will be processed first
			class arch(Flourish):

				class twigs(SiftingController):

					# Include in arch and/or exclude from arch some folders (optional).
					# IMPORTANT: by including some folders, all other neighbor folders that are not included
					# are automatically excluded!
					include	= "include such folder", "include such folder"
					exclude	= "exclude such folder", "exclude such folder"

				class leafs(SiftingController):

					# Include in arch and/or exclude from arch some files (optional).
					# IMPORTANT: by including some file patterns, all other different patterns
					# are automatically excluded!
					include	= "include such file", "include such file"
					exclude	= "exclude such file", "exclude such file"








		Hagrid().arch()







