from	__future__	import annotations
from	typing		import Optional
from	typing		import Tuple
from	typing		import List
from	typing		import Dict
from	logging		import getLogger
from	logging		import Formatter
from	logging		import StreamHandler
from	logging		import FileHandler
from	sys			import stdout
from	io			import TextIOWrapper
from	os			import path		as ospath
from	os			import makedirs
import	re








class LibraryContrib:

	"""
		                                   ..-=+++=..   
		                                ..=++-:...-#=.  
		                              .:++-.........#-. 
		                            .-*+:...:::::...+*. 
		                          .:*=....::::::::..=#. 
		                         .++:.::::::::::::..+*. 
		                       .:*-..::::::::::::...#-. 
		                      .=*..::::::=-::::::..-%.  
		                   .:=*+..:-:::=#=:::::::..#-.  
		                 .=*=++..:=::-*%=:::--::..+*=++.
		               .:#=.:+..:=-:=#%=::-=-::..=%*-.%:
		              .=#:.:=:.:-=:=##=::==::...-*:..:%.
		             .+#:.:::.::+--##+:=+-:..:.-=....+*.
		            .+#:.::::.::*:#*#=+-:::::..:....:%:.
		           .=%:.:::::.:-*+#%#=::::::....:...*+. 
		          .:%-.::::::::=###+::::::::..:::..=#.  
		          .**.:::::::::-%*#::::--:...:::..-#:   
		          :%-.::::.-:::=##=::-=-:..::::..-#--.  
		     ..   =#.::::::=:::#*#::==::.:::::..=%*##.  
		     .=+: *+.::::::=::=##=-+-::::::::..+#=.#-.  
		      -#++%=::::::.+::**%++::::::::..:#=..=#.   
		      :%:=%-::::::.*:-%*%=::::::::..=*:..:%:    
		      .%-:#=:::::::==+##+::::::::.:*+:...*+.    
		      .%=:**::::::::##+%-::::--:.=*-:...+#.     
		      .%=:-#:::::=::=%+#::::--::++::...=#.      
		      .#+::+=::::-+--#**::-=:::*=::...+#.       
		      .#+:::+::.:::+##*+:-=:::*-:::..**.        
		      .**::::-::::::**#+-+:::=-:::.:#=.         
		....   =#:::::::.:::*+#+*::::-:::.-#-.          
		.-**=-..%-:::::::..:#+#%-:::::::.=#..           
		  .=*=++##::::::::..#+#*::::::::+*:===*+:       
		   ..++:=#*::-::::::#+#=:::::::+%+=:-*-. .      
		   ...-#-:+*-:=:::::#+#+::-:::+*:::+*-=++-.     
		.-+##+++*-:-*+:==-::*+*+:=-::-#:::=*+-++:       
		   .:=*=:::::-+=-=++#***-+:::*-:::::-#-.        
		      .-*=::::::::::+*+#*-:::+:::::=#..         
		        .=*=::::::::=#=%#:::::::::=*..          
		          .-++=-::::-%=#+:::::::=*=.            
		        ..-=++*+=-:::#+*+::::=+*#==..           
		      ..=+====*%*=:::**+#::----+**++-.          
		           .-*=::::::=#=%-::::-==*#=.           
		          .-#++=====+=%=*+-++=-::....           
		          .--..    ..-#*=%*..                   
		                      :#=#-                     
		                      .#++*.                    
		                       -#=%:                    
		                       .#=+*.                   
		                        -#=#-                   
		                        .#=+#.                  
		                         -#=*=.                 
		                         .*+=#:.                
		                         ..#++#..               
		                           .:-=:.               

		This class represents the wrapper over "logging" standard library functionality. It uses minimal
		"Logger" set up either for stdout or file handling, but covers it with additional managing layer:
			modularity		- every object that accessing LibraryContrib is treated as a module. It is
							achieved by maintaining every object string representation ad identifier for
							mappings like "handover_map" that maps them with corresponding logging levels,
							or "forcing_map" that maps regular expressions to match them to activate certain
							logging level. Additional "handover_order" list storing the order each module
							made first access to LibraryContrib object.
			runtime formats	- the modularity is bound to be reflected in logging records. LibraryContrib
							field "contribfmt" is a "logging" compatible format, that must include an option
							to inject current "module" name. That means every object that want to make
							logging record must provide it's name string to be included in that logging
							record, and it is all happens in runtime.
			handover		- functionality that allows the concept of "modularity". It is mainly consist of
							eponymous method "handover" which must be called by every "module" right
							before access to the actual logging functionality. In fact, all LibraryContrib
							fields that has "handover" in names are part of handover functionality. The
							"handover_map" is being maintained right in "handover" method.
		Operates with following variables, that might be provided either as arguments or as class fields,
		or might be even omitted and defaulted in initiation:
			handler			- string that must represent file path for "FileHandler" initiating. Might be
							an absolute or relative path. Destination folder for such handler will always
							be created if does not exist, without handling e.g. PermissionError. If omitted,
							"Logger" handler is defaulted to "stdout";
			init_name		- string that must represent desired name for "Logger". This name is what usually
							"Logger" puts in log file, and what makes the difference between Loggers, so it
							is very important for some objects to not use same name Logger simultaneously,
							cause it will result a log file mess like duplication of records. If omitted,
							the default value will be some notable strings value;
			init_level		- integer value that will represent the initial Logger level. LibraryContrib
							doesn't maintain any special levels other than "logging" offers, so it's
							levels are the same:
								10 - DEBUG,
								20 - INFO,
								30 - WARNING,
								40 - ERRORS,
								50 - CRITICAL.
							This is very concise and sufficient functionality, plus, in terms of flexibility,
							LibraryContrib designed to recognize any values in between levels ranges. Default
							level is 20 - INFO;
			force_handover	- boolean value that represents a flag for LibraryContrib "handover". By default
							it's set to False and only debug level does activate handovered objects strings
							representation in records, but if "force_handover" set to True it will encompass
							every logging level, until set back to False;
			force_debug		- iterable that must content strings, which when compiled by "re" module, will
							match the "modules" names that are desired to be forced to a DEBUG logging level.
							Empty by default and if provided must not be a string;
			force_info		- iterable that must content strings, which when compiled by "re" module, will
							match the "modules" names that are desired to be forced to a INFO logging level.
							Empty by default and if provided must not be a string;
			force_warning	- iterable that must content strings, which when compiled by "re" module, will
							match the "modules" names that are desired to be forced to a WARNING logging
							level. Empty by default and if provided must not be a string;
			force_error		- iterable that must content strings, which when compiled by "re" module, will
							match the "modules" names that are desired to be forced to a ERROR logging level.
							Empty by default and if provided must not be a string;
			force_critical	- iterable that must content strings, which when compiled by "re" module, will
							match the "modules" names that are desired to be forced to a CRITICAL logging
							level. Empty by default and if provided must not be a string;
			contribfmt		- dictionary that must content "fmt" and "datefmt" strings mappings to comply
							"Formatter" patterns. The "fmt" string must always include "origin" format
							argument, that will be used for handover mentioning. The default format will
							looks like this: DD/MM/YYYY HHMM @logger-handover LEVEL : MESSAGE
		LibraryContrib might be used as a regular logger for any object, but it's real purpose is to
		work with Transmutable objects. Ability to "handover" Transmutables will always allow to track
		current object name, as suggested by Transmutable __str__. The very special field "CONTRIB_HOOK"
		by default set to True in order to allow Transmutable to hook LibraryContrib type object.
	"""


	handler			:Optional[str]
	init_name		:Optional[str]
	init_level		:Optional[int]
	force_handover	:Optional[bool]
	force_debug		:Optional[List[str] | Tuple[str]]
	force_info		:Optional[List[str] | Tuple[str]]
	force_warning	:Optional[List[str] | Tuple[str]]
	force_error		:Optional[List[str] | Tuple[str]]
	force_critical	:Optional[List[str] | Tuple[str]]
	contribfmt		:Optional[Dict[str,str]]
	CONTRIB_HOOK	=True


	def __init__(
					self,
					*,
					handler			:Optional[str]						=None,
					init_name		:Optional[str]						=None,
					init_level		:Optional[int]						=None,
					force_handover	:Optional[bool]						=None,
					force_debug		:Optional[List[str] | Tuple[str]]	=None,
					force_info		:Optional[List[str] | Tuple[str]]	=None,
					force_warning	:Optional[List[str] | Tuple[str]]	=None,
					force_critical	:Optional[List[str] | Tuple[str]]	=None,
					force_error		:Optional[List[str] | Tuple[str]]	=None,
					contribfmt		:Optional[Dict[str,str]]			=None
				):


		match (target := handler if handler is not None else getattr(self, "handler", stdout)):

			case str():
				if	ospath.isabs(target): makedirs(ospath.dirname(target), exist_ok=True)

				self.handler = FileHandler(target)
			case TextIOWrapper():
				self.handler = StreamHandler(handler)

			case _: raise TypeError("LibraryContrib handler must be file path string or stdout (default)")




		# It is allowed to provide "init_level" as any value that might be converted to integer.
		# Double float-int conversion assures almost any value (except None) that might be converted
		# to integer (floatable strings must be first converted to float) will be accepted.
		try:

			self.init_level = int(

				float(

					init_level if init_level is not None else
					getattr(self, "init_level", 20)
				)
			)

		except:	raise TypeError("LibraryContrib levels must be numeric values")




		self.init_name = str(

			init_name if init_name is not None else
			getattr(self, "init_name", "fantastic logs and where to contribute them")
		)


		self.contributor_name	= None
		self.contributor		= getLogger(self.init_name)
		self.handover_level		= self.init_level
		self.handover_map		= dict()
		self.handover_order		= list()
		self.handover_off		= True
		self.handover_name		= None


		self._handover_mode = bool(

			force_handover if force_handover is not None else
			getattr(self, "force_handover", False)
		)




		if		contribfmt is not None : fmtcandidate = contribfmt
		elif	getattr(self, "contribfmt", None) is not None : fmtcandidate = self.contribfmt
		else:	fmtcandidate = {

				"fmt": "%(asctime)s @%(name)s{origin} %(levelname)s : %(message)s",
				"datefmt": "%d/%m/%Y %H%M",
			}
		if(
			isinstance(fmtcandidate, dict)
			and
			fmtcandidate.get("fmt") is not None
			and
			isinstance(fmtcandidate.get("fmt"), str)
			and
			"{origin}" in fmtcandidate.get("fmt")
			and
			fmtcandidate.get("datefmt") is not None
			and
			isinstance(fmtcandidate.get("datefmt"), str)
		):
			self.contribfmt = fmtcandidate
		else:
			raise TypeError("No valid contributor formatter provided")


		self.makefmt("")
		self.contributor.addHandler(self.handler)
		self.contributor.setLevel(self.init_level)




		self.forcing_map = dict()
		self.forcing_map.update(
			{
				re.compile(P.replace("*",".*")): 10 for P in
				(
					force_debug if force_debug is not None and isinstance(force_debug, list | tuple)
					else
					getattr(self, "force_debug", None)
					if isinstance(getattr(self, "force_debug", None), list | tuple)
					else
					[]
				)
			}
		)
		self.forcing_map.update(
			{
				re.compile(P.replace("*",".*")): 20 for P in
				(
					force_info if force_info is not None and isinstance(force_info, list | tuple)
					else
					getattr(self, "force_info", None)
					if isinstance(getattr(self, "force_info", None), list | tuple)
					else
					[]
				)
			}
		)
		self.forcing_map.update(
			{
				re.compile(P.replace("*",".*")): 30 for P in
				(
					force_warning if force_warning is not None and isinstance(force_warning, list | tuple)
					else
					getattr(self, "force_warning", None)
					if isinstance(getattr(self, "force_warning", None), list | tuple)
					else
					[]
				)
			}
		)
		self.forcing_map.update(
			{
				re.compile(P.replace("*",".*")): 40 for P in
				(
					force_error if force_error is not None and isinstance(force_error, list | tuple)
					else
					getattr(self, "force_error", None)
					if isinstance(getattr(self, "force_error", None), list | tuple)
					else
					[]
				)
			}
		)
		self.forcing_map.update(
			{
				re.compile(P.replace("*",".*")): 50 for P in
				(
					force_critical if force_critical is not None and isinstance(force_critical, list | tuple)
					else
					getattr(self, "force_critical", None)
					if isinstance(getattr(self, "force_critical", None), list | tuple)
					else
					[]
				)
			}
		)








	def close(self): self.handler.close()
	def debug(self, message :str):
		if	self.handover_level <20:

			self.check_format(self.handover_name, self.handover_level)
			return self.contributor.debug(message)


	def info(self, message :str):
		if	self.handover_level <30:

			self.check_format(self.handover_name, self.handover_level)
			return self.contributor.info(message)


	def warning(self, message :str):
		if	self.handover_level <40:

			self.check_format(self.handover_name, self.handover_level)
			return self.contributor.warning(message)


	def error(self, message :str):
		if	self.handover_level <50:

			self.check_format(self.handover_name, self.handover_level)
			return self.contributor.error(message)


	def critical(self, message :str):
		if	self.handover_level <60:

			self.check_format(self.handover_name, self.handover_level)
			return self.contributor.critical(message)


	def log(self, level :int, message :str):

		""" Logging "log" imitation. """

		match level:
			case 10:	self.debug(message)
			case 20:	self.info(message)
			case 30:	self.warning(message)
			case 40:	self.error(message)
			case 50:	self.critical(message)
			case int():	self.contributor.log(level, message)








	def force(self, *layers :Tuple[str,...], level :int) -> int | TypeError :

		"""
			Helper method that allows altering levels for contributors.
			Accepts strings that must represent patterns that will "fullmatch" with corresponding callers
			representations in "handover_map". Any "layer" string not in "handover_map", or a "layer" with
			type that not string, will be just skipped. For every "layer" found sets corresponding level
			value to new "level", provided by mandatory keyword argument. If no "layers" provided, sets
			"level" for all objects in "handover_map".
			Maintains a counter of a number of objects which level mapping was changed and returns this
			counter. Raises TypeError in case "level" cannot be converted to int.
		"""

		try:	new_level = int(float(level))
		except:	raise TypeError(f"Level to force must be numeric, got \"{level}\"")
		else:

			counter = 0

			if	not layers:

				for name in self.handover_map : self.handover_map[name],counter = new_level,counter +1
			else:
				for layer in layers:

					if		isinstance(layer, str): current = re.compile(layer.replace("*",".*"))
					else:	continue


					for name in self.handover_map:
						if	current.fullmatch(name):

							self.handover_map[name] = new_level
							counter += 1


			return	counter


	def forced_or_init(self, name :str) -> int :

		"""
			Helper method that serves as logging level dispatcher according to "forcing_map".
			It is designed to obtain either forced or initial level for any object, that represented
			by "name" string. For such object "forcing_map" will be iterated and for very first key
			that caused "fullmatch" with "name" corresponding level will be returned. If no matches
			occurs, initial logging level will be returned. Raises TypeError if matched value is not
			an integer.
		"""

		for pattern,level in self.forcing_map.items():
			if	isinstance(pattern, re.Pattern):


				if	pattern.fullmatch(name):
					if	isinstance(level, int): return level


					raise	TypeError(f"Pattern \"{pattern.pattern}\" mapped to force incorrect \"{level}\"")
		else:		return	self.init_level








	def check_format(self, name :str, level :int, changeover=0):

		"""
			Utility method that estimates the "changeover" state for the current contribution.
			The keyword argument "changeover" will be xor'ed with corresponding bit that correspond
			to a certain state. The final value will be passed to a "bit_filter" method that must
			decide the following action for state.
			The "changeover state" comprises:
				- whether or not logging level was changed to a debug mode;
				- whether or not logging level was changed from debug mode;
				- whether or not logging object name was changed;
				- whether or handover mode is on;
				- whether or handover mode was turned on/off;
			In case of performance it is assumed that "name" and "level" are validated str and int.
			Returns None, handles no Exceptions.
		"""

		if	self.contributor.level != level:

			if		self.contributor.level <20 <= level : changeover ^= 1	# debug mode off->on (escalation)
			elif	level <20 <= self.contributor.level : changeover ^= 2	# debug mode off->on (decrease)

			self.contributor.setLevel(level)
		if	self.contributor.level == 10 :	changeover ^= 8
		if	self._handover_mode	:			changeover ^= 16
		if	self.handover_off	:			changeover ^= 32
		if	self.contributor_name != name:
			self.contributor_name = name
			changeover ^= 4


		self.bit_filter(changeover)




	def bit_filter(self, mask :int):

		"""
			Utility method that puts "mask" integer, that must represent "changeover state" for contribution,
			to a bitwise filter, with certain mask's values mapped with corresponding actions to contributor.
			This algorithm is the way to ensure proper formatting for any object, that contributes a log,
			along with minimization of such reformatting. Returns None, doesn't handle the only source of
			Exceptions from "makefmt" method.

			Changeover state mask values table for bitwise filtering:

			62 (32 + 16 + 8 + 4 + 2)	- handover off->on, debug mode off->on, name changed
			60 (32 + 16 + 8 + 4)		- handover off->on and name changed in debug mode
			58 (32 + 16 + 8 + 2)		- handover off->on, debug mode off->on
			56 (32 + 16 + 8)			- handover off->on in debug mode
			53 (32 + 16 + 4 + 1)		- handover off->on, debug mode on->off, name changed
			52 (32 + 16 + 4)			- handover off->on, name changed
			48 (32 + 16)				- handover off->on
			46 (32 + 8 + 4 + 2)			- debug mode off->on, name changed
			44 (32 + 8 + 4)				- name changed in debug mode
			42 (32 + 8 + 2)				- debug mode off->on
			37 (32 + 4 + 1)				- debug mode on->off, name changed
			33 (32 + 1)					- debug mode on->off
			30 (16 + 8 + 4 + 2)			- handover mode, debug mode off->on, name changed
			28 (16 + 8 + 4)				- handover mode, debug mode, name changed
			21 (16 + 4 + 1)				- handover mode, debug mode on->off, name changed
			20 (16 + 4)					- handover mode, name changed
			14 (8 + 4 + 2)				- handover mode on->off, debug mode off->on, name changed
			12 (8 + 4)					- handover mode on->off, debug mode, name changed
			10 (8 + 2)					- handover mode on->off, debug mode off->on
			8		 					- handover mode on->off, debug mode
			5 (4 + 1)					- handover mode on->off, debug mode on->off, name changed
			4							- handover mode on->off, name changed
			1							- handover mode on->off, debug mode on->off
			0							- handover mode on->off
		"""

		match mask:

			case 56:								self.handover_off = False
			case 10 | 8:							self.handover_off = True
			case 33 | 37:							self.makefmt("")
			case 46 | 44 | 42 | 30 | 28 | 21 | 20:	self.makefmt(f"-{self.contributor_name}")
			case 62 | 60 | 58 | 53 | 52 | 48 :

				self.makefmt(f"-{self.contributor_name}")
				self.handover_off = False

			case 14 | 12:

				self.makefmt(f"-{self.contributor_name}")
				self.handover_off = True

			case 5 | 4 | 1 | 0:

				self.makefmt("")
				self.handover_off = True




	def makefmt(self, handover_name :str) -> TypeError | ValueError | AttributeError :

		"""
			Utility method that does actual reformatting for contributor. As originally designed, there are
			only two forms of formatting for contributors:
				- general;
				- handover.
			By "handover formatting" current contributing object string representation is meant, which is
			included in the formatting string as {origin} variable. This case implies representation
			string for contributing object to be as close to object name as possible, so it was designed
			for a Transmutable class, that must returns it's full qualname as a string.
			In turn, "general formatting" omits contributing object name and makes format clear.
			It is very important, as current method relies on use of "contribfmt" dictionary as a
			pattern for reformatting, once it is subject of modification, the {origin} variable must
			be included in format string to ensure handover functionality (or such functionality must
			be ignored).
			The reformatting is handled directly on contributing "handler" object, which must be
			StreamHandler/FileHandler object. In case "contribfmt" is not a dictionary for proper
			formatting, 
			Returns None, raises Exception in case "handler"/"contribfmt" fields doesn't point
			to a valid object.
		"""

		if	hasattr(self, "handler"):
			if	callable(getattr(self.handler, "setFormatter", None)):
				if	isinstance(self.contribfmt, dict) and isinstance(self.contribfmt.get("fmt"), str):


					current_fmt = self.contribfmt.copy()
					current_fmt["fmt"] = current_fmt["fmt"].format(origin=handover_name)
					self.handler.setFormatter(Formatter(**current_fmt))


				else:	raise TypeError(f"Invalid contributor formatting dictionary \"{self.contribfmt}\"")
			else:		raise ValueError(f"Invalid contributor handler \"{self.handler}\"")
		else:			raise AttributeError("Contributor has no handler")








	def handover(self, caller :object, assign=True) -> LibraryContrib | ValueError :

		"""
			Core method that creates meta layer of maintaining contributor access.
			At the first place the "caller" object string representation is obtained. This string is
			used as a key to find corresponding logging level in "handover_map". Those two values
			will be then assigned as corresponding fields "handover_name" and "handover_level", which
			might be used then to maintain logging formatting. Additional the loggy assignment to
			a caller which level mapping is None, so it is it's first handover, is regulated by a boolean
			flag "assign". As Transmutables assign is automated, this regulation allows any other "caller"
			that not support attribute assignments to be maintained in "handover_map".
			It is assumed, that for correct formatting "handover" must be called for every object before
			such object will get access to contributing, as originally designed in Transmutable class that
			"handover" is called in every __getattribue__ method.
			As this functionality brings nothing but fancy logging for some stringable objects, it is
			might be skipped with no regrets to use contributing functionality only and directly.
			Returns itself as a pass after succesful "handover", or raises ValueError in only case,
			when "handover_map" has not an integer mapping for a "caller" string - in this case every
			call for "handover" for such "caller" will raise ValueError, even when try to remap value
			in "handover_map", so it is very important to not mess with handover mapping.
		"""


		name	= str(caller)
		level	= self.handover_map.get(name)


		match level:


			# Processing current level.
			# "None" must mean current "caller" has no mapping and hence was not assigned a contributor
			# yet, so it must go through the procedure and the level will be adjusted anyway.
			# "level" is integer means current "caller" was assigned it's contributor and mapped, so
			# the only thing need to check whether current level is differ from mapped.
			# Any other value for level means incorrect mapping and ValueError will be raised.
			case None:


				self.handover_map[name] = level = self.forced_or_init(name)
				self.handover_order.append(name)


				if	assign:
					try:	setattr(caller, "loggy", self)
					except:	pass


			case int():	pass
			case _:		raise ValueError(f"Incorrect handover mapping \"{name}\": \"{level}\"")


		self.handover_name	= name
		self.handover_level	= level


		return	self


	@property
	def handover_mode(self): return bool(self._handover_mode)
	@handover_mode.setter
	def handover_mode(self, state :bool): self._handover_mode = bool(state)
	def handovers(self, level :Optional[int] =None):

		"""
			Helper method that allows to obtain "handover_order" itself - a list of the strings, that
			represents the order in which handover was proceeded. An optional keyword argument "level"
			allows to provide an integer level which will be used as an announcer of "handover_order"
			list. Despite the level, "handover_mode" will be forced automatically to ensure informative
			logging, and by the end will be set to the state it was before the announce.
			Fields "handover_name" and "handover_level" will be set, imitating "handover" call.
			Then "log" method will be used to imitate regular logging.
		"""

		if	isinstance(level, int):

			self.handover_name	= "_handovers_"
			self.handover_level	= level
			handover_state		= self._handover_mode
			self._handover_mode	= True


			for name in self.handover_order : self.log(level, name)
			self._handover_mode = handover_state


		return	self.handover_order[::]







