from __future__					import annotations
from typing						import Optional
from pygwarts.magical.spells	import patronus
from pygwarts.magical.spells	import wingardium_leviosa
from pygwarts.magical.spells	import evanesce
from pygwarts.irma.contrib		import LibraryContrib








class Transmutable:

	"""
                                                                           ************+=+++**=       
                                                           :****************#####**+==---+++**=       
                                                       -***###*****+********#**+=-====---+*+**=       
                                                   ****#####**++===+++*****++==--------===**#*+       
                                                 ..*######*++++=+++****+=========------===**##+..     
                                               ::######******++*****+=------======-----===*###***     
                                            .:-######*******###*+==---::::::-----------===+###***     
                                          ::+######*######***=--::::::.:..:::::--------===+####**     
                                        :-+############**+-:...................::---======+####**     
                                      --*#######*******=-.     .................:::-======+*###**     
                                    ==*#####*******#**+:...   .....................:::-===+*#****     
                                   .**###**++*+**##**=:.  ..........        .......::::-=++******     
                                 .=+###***+++***#**=-...   ......             .....:.::-=+****#**     
                                 :*###*+++++*##**+-::........              .........::-==**##****     
                               :+*##*+++****##*+-:-=-:.......    ..................::-===**#####*     
                               -*##*++**####*+-::::-=-:............................:-===+**#####*++   
                             =**##***###***+-.....::---:.........................:--====**######***   
                             +*##*#####**=:.........:::::.......................::-----+**#######**   
                           **#########*=:..........:::::::....................:::::::-+**########****.
                         ..########*+-:...........::::::::::.....   .......:::::::::=****#########*++.
                       ..**######*=-:............::::::::::::...    .....::::::::::-+****##**#####*.. 
                      .***####*+-:.:.............::::...:---::..   ...:::::::------=***####***####***.
                      .**###*+=:....      .......:::.....-=+=-:...:--:......::-----=***####****####**.
                    .:-*###*+=-:...      .................-+**==-=-:.........:---:-+***###******####*.
                    -**#%%#*+=:....     ...................:+##*+-:..........::--=+***####******####*.
                    -*#%%%#*=-....    ......................-**+-::..........:::-++**####****++*####*=
                  :-+#%%%%#+:.   ...........................:++=-:::.........::--=+**####*+**++**####*
                  =*#%%%%#+:.    ............................----:::::.......::--=+**####++++++**####*
                  =#%%%%#*-     ...............:::.........::::::::::::.......:-==+*#####++++++***###*
                -+*#%%%%*=..    ....................:::::::---::::::::......:::-=-=+**##*+++++++******
                =*#%%%%#=:.     ...:::::::..........:::--------::::::.......:::--=+==+++=======+**+++.
                +#%%%%%+-.     ....:::::::...........::-------::::::....:.::.::-==================+**.
                +#%%%%*:.      ....:::::::..........::::---::::::::... ....::-==================+=+   
              **#%%%%+:.        ....::::::::::::::::::::::::::....... ...::=+==================++     
              **#%%%+:.          ................:::::::::::::..........--=====++===========+++==     
              *#%%#+:..               ..............::::::::::........:::-====+++=========+++=-       
              ##%#+:...                 .....    .....................::-==++++==========++*:         
            ::###+-.:...                 .        ............       ..-=+***+=========++*==:         
           .**###*=.....                       ............          .-=+***++++++====++=-.           
           .**####*-..                ....  ............            .-=***+++++++==++*--              
           .**#####+...                 ...............           .:-+****+++++++++***                
            ::*#####=:.               ................        .   .-+******+++++***+::                
              **####*-:. .....       ...:............        .....:+*************+:.                  
              **#####+:.......      .....:...........       ...:=**##************=                    
              ***####*-:......      .....:...::......         :**###***********-.                     
              ***#####=::.....      ....::::::::.....     ..:.=*###***###******-                      
                +*####*::.         .....::::::::............::**##***###*****:                        
                =**###*=:.         ..........::..........::-=++*****###****                           
                  =*###+:.           .............:::-==++++++==++*******                             
                  =**##*=:.                 ....::-============+++*****++                             
                  -=+*##*-..               ...:----::.:::---=++++++***=                               
                    -**#*+-..            .::---:::....:::-=+++++++**+=-                               
                    .-=*#*+:.          ..----:....:::::-=+++++++**==:                                 
                      .**#*=..         :-=-::::::..:::-=+++++*----.                                   
                       --***:.        :--:...........:++++++--                                        
                         ***=.      .:--:  ........:=+++++*=                                          
                         ***+=.   ..--:........::---=+++*=:.                                          
                         ::**+-...:-:......:------==++*=:.                                            
                           **+=..:-:..::---=+++****....                                               
                           ..=+------===+*:........      

		Pygwarts core class, that serves as a super class for every pygwarts object. Every object, that
		inherited from Transmutable class might be either a single object, or be nested to other Transmutable
		object, forming a "mutable chain". This nesting means declaration of one Transmutable class in the
		namespace of the other Transmutable class. This nesting ensures that every nested class will become
		a nested layer object for current layer object, inferring the very top layer object, that will have
		access to all nested layers. Layers nesting means setting an object as an attribute of it's upper
		layer object, using it's declaration name. The mutable chain provides not only top-down layers
		access, but also a one way down-top access. That means for every nested layer there is a field
		"_UPPER_LAYER", which is used to access it's upper layer object namespace, so any upper layer
		member is reachable for nested layer. But it is only a direct access reachability, which means
		every nested layer may use dot notation to access members of upper layers, but not to access
		members of upper layers nested layers, that is a one way down-top access implies. This is the
		main feature of mutable chain, it is ideology, the concept. The other fundamental feature, that
		based on this concept, is a logging. It is hardcoded in pygwarts to use special name "loggy"
		as a LibraryContrib object to handle logging. It is not mandatory to declare LibraryContrib object
		as a "loggy" member, cause Transmutable will be able to find LibraryContrib object at any layer
		and reassign it as a "loggy", as it is possible to omit it too, so it will be bypassed. But it
		is very important to not use "loggy" keyword for any other objects, rather than LibraryContrib.
		The mutable chain might have different loggers for any nested layers, and all of them will be
		assigned and accessed as "loggy". One crucial moment is that any nested layer, that will encounter
		a LibraryContrib type, will not only initiate it and set it as it's "loggy" attribute, but also will
		escalate it the very top layer, if it doesn't have a LibraryContrib "loggy" attribute yet. If
		the very top layer already has it's "loggy" declared and initiated, any nested layer "loggy"
		declaration will be ignored, cause every "loggy" access has it's special preprocessing that
		first of all points to the very upper layer "loggy". If the very top layer already has it's "loggy"
		declared and initiated, but a nested layer has a LibraryContrib declared as some different name,
		this LibraryContrib will be initiated and assigned as "loggy" for current layer. If the very top
		layer doesn't has it's "loggy" declared and initiated, the very first nested layer LibraryContrib
		initiation encountered during mutable chain initiation will assigned this LibraryContrib as "loggy"
		for the very upper layer along with current layer. Any further LibraryContrib initiations for other
		nested layers will reassign this layer "loggy" if only were declared with different name.
		The mutable chain initiation is the process that include chain of initiations for every Transmutable
		class that nested to the other Transmutable class. It is consist of two phases:
			- first phase, the initial state of current Transmutable, that implies the "__init__" invoke
		itself. This phase considers the only positional argument it can receive - "upper_layer_link".
		That argument determines whether current Transmutable the very upper layer object or nested one.
			- second phase, the namespace scanning. Right after the first phase for current Transmutable,
		all members that are obtained from "__dir__" and a considered as Transmutable will be hooked and
		their phase one initiations will be invoked. It is also possible to encounter a LibraryContrib
		type member during this phase, so the events described above will occur. Such namespace scanning
		assumes a depth-first initiation for a mutable chain, cause every upper layer will invoke it's
		nested layer and proceed only after it's initiation complete. This phase also handles any Exceptions
		that might be raised during it's nested layer initiation, and also situations when somehow
		nested layer initiation results a not Transmutable object.
		After these two phases the very upper layer, as the only layer that might have keyword arguments
		provided for initiation, will process it and assign as fields. This keyword arguments might be
		any type and serves any purposes, as they doesn't impact a mutable chaining.
		As mutable chain initiation relies on hooking nested Transmutables in phase two, every Transmutable
		must have mandatory field "_MUTABLE_CHAIN_HOOK" - the main field that serves as Transmutable type
		recognition. Every nested Transmutable can only be found for upper layer by this field set to True.
		There is also one more mandatory and switchable hook "_UPPER_LAYER_HOOK", that serves as a flag
		whether current object is the very upper layer or not. By default it set to True, so for every
		Transmutable that find itself to be a nested layer, it must switch this hook to False, cause some
		things, like attribute searching, depends on this hook value.
		This super class for every pygwarts object original design implies simplicity and includes the
		only basic things that forms it's concept. Any inherited object's behavior supposed to be based
		on this concept. The main idea of a mutable chain strongly relies on declaration and it's order.
	"""


	_UPPER_LAYER				:Optional[Transmutable]
	_MUTABLE_CHAIN_HOOK	= True
	_UPPER_LAYER_HOOK		= True


	def __str__(self):

		"""
			Implements mutable chain naming representation. All upper layers for current Transmutable
			object will form a concatenation of names in dot notation, just like in accessing.
		"""

		if	not self._UPPER_LAYER_HOOK:

			return	f"{self._UPPER_LAYER}.{self.__class__.__name__}"
		return		self.__class__.__name__




	def __getattribute__(self, attr :str) -> object :

		"""
			This method implements the preprocessing of some crucial mutable chain members. The main
			job is a "loggy" attribute access handling. This is the only point where LibraryContrib
			object access might be mapped to the object that actually access it. As LibraryContrib
			object has special method "handover", every "loggy" access will be preceded with it's
			handover. Also, depending on current state of "loggy" member, if it is just encountered
			as a type, it will be initiated and also escalated to the very top layer. Any other than
			LibraryContrib entity, which is also can be determined by "CONTRIB_HOOK" field set to True,
			that discovered as a "loggy" member will cause TypeError.
		"""

		if	attr == "__qualname__" and attr not in dir(self) : return self.__class__.__name__


		_attr = super().__getattribute__(attr)


		if	attr == "loggy":
			match _attr:


				case	LibraryContrib(): return _attr.handover(self)

				case	type() if getattr(_attr, "CONTRIB_HOOK", None):		_attr = _attr()
				case	object() if getattr(_attr, "CONTRIB_HOOK", None):	_attr = _attr()()

				case _:	raise TypeError(f"\"loggy\" reserved for LibraryContrib, got {type(_attr)}")


			_attr.handover(self)
			_attr.CONTRIB_HOOK = False


			if	not self._UPPER_LAYER_HOOK : wingardium_leviosa(self, "loggy", _attr)
		return	_attr




	def __getattr__(self, attr :str) -> object :

		"""
			This method means __getattribute__ failed to obtain some attribute, so, as mutable chain
			structure suppose, every attribute will be searched to the very top layer. That means
			via "_UPPER_LAYER" accessing to the current Transmutable upper layer Transmutable, the
			attribute will be considered as a member of upper layer Transmutable. The truthy hook
			means the very top layer is reached and final AttributeError must be raised, cause
			desired attribute is not a part of mutable chain. There is the only exception for "loggy"
			attribute. If the very top layer is reached and there is no "loggy", special object
			"evanesce" will be returned to bypass "loggy" member necessity.
		"""

		if	attr == "loggy":
			if	self._UPPER_LAYER_HOOK : return evanesce


			# This is the point where some nested layer requested "loggy" from it's upper layer. That means
			# this nested layer had not yet encountered "loggy" object and handovered it. When "loggy" will
			# be finally found at some upper layer, built-in getattr function will put it through some
			# validation procedure, so it is guaranteed that result is a LibraryContrib object. For every
			# layer on the way to that LibraryContrib object, when descending back to a requester, handover
			# will ensure corresponding "loggy" assignment.
			_attr = getattr(self._UPPER_LAYER, attr)
			_attr.handover(self)


			return	_attr


		elif	not self._UPPER_LAYER_HOOK: return getattr(self._UPPER_LAYER, attr)
		raise	AttributeError(f"Attribute '{attr}' has no escalation to {self}")




	def __init__(self, upper_layer_link=None, **kwargs):


		# As mutable chain initiation is quiet simple and straightforward, hence there is no need in
		# logging during this process, and in terms of not messing up with handovers and so on, all
		# initiation phases goes silent, means with no logging, as it is probably useless.
		# Here starts first phase of initiation.
		match upper_layer_link:

			# This is the main case for mutable chain initiation. The "upper_layer_link" as Transmutable
			# itself means current Transmutable object is a nested layer for "upper_layer_link" and this
			# point was reached by "upper_layer_link" phase two of initiation, where current Transmutable
			# class was hooked and it's initiation was invoked.
			case Transmutable():

				self._UPPER_LAYER_HOOK = False
				self._UPPER_LAYER = upper_layer_link
				upper_layer_link.loggy.handover(self)


			# Following two cases covers mutable chain most upper layer initiation, as if LibraryContrib
			# object or class was passed as argument for initiation. As regular mutable chain initiation
			# suggests obtaining "loggy" via phase two of initiation, when it is encountered as declared
			# member, current two cases ensures an option of using some outer LibraryContrib entity.
			case LibraryContrib(): upper_layer_link.handover(self)
			case type() if getattr(upper_layer_link, "CONTRIB_HOOK", False):

				upper_layer_link().handover(self)
				self.loggy.CONTRIB_HOOK = False


			# Last two cases are regular case for most upper layer initiation, when "loggy" to be find
			# as any descent declared member in phase two of initiation, or even just omitted, and the
			# case when "upper_layer_link" neither Transmutable nor LibraryContrib entity, which is
			# mutable chain initiation violation, so a TypeError will be raised.
			case None:	pass
			case _:		raise TypeError(f"\"{upper_layer_link}\" is inappropriate upper layer link")




		# Here starts the second phase of initiation. It encompasses scanning the whole namespace
		# of the current Transmutable object, by the use of "__dir__" default method, instead of
		# built-in function "dir", which does not grant the iteration in order, that members were
		# declared. It is crucial in mutable chain initiation, cause, despite the original design
		# insist on mutable chain members independence, it is not strictly prohibited, so some
		# Transmutable's design must have the ability to rely on initiation in certain order to work.
		# The following scanning will search only Transmutable classes, which names not starts
		# with underscore and which has special fields named hooks that set to True. This is the
		# signal for current object that a nested layer Transmutable is encountered and must be
		# initiated as a member of a mutable chain.
		for inner in self.__dir__():
			if	not inner.startswith("_"):


				# It is crucial moment, that at this point the LibraryContrib class that declared as
				# "loggy", wherever it will be founded, will be handled very special way. As it is
				# mandatory goes via "getattr" built-in function, which invokes "__getattribute__"
				# method, the "loggy" name will trigger special handle for LibraryContrib class.
				# It is truly for the case when LibraryContrib is only declared as "loggy", so it
				# was never initiated yet. The declaration place is no matter, whether it is very
				# top layer or any nested one. The other case of "loggy" is a LibraryContrib object,
				# already initiated, is the most regular situation for any nested Transmutable that
				# was initiated by it's upper layer that already has "loggy" object assigned. Despite
				# this "loggy" was already assigned in first initiation phase for current Transmutable,
				# the fact it is will be accessed here, in second phase, and putted to the same processing
				# again, is not a redundant, but a additional layer of validation!
				layer_hook = getattr(self, inner)


				# This is the case when LibraryContrib is declared as any other name than "loggy".
				# It is possible for different mutable chain layers to have it's own "loggy" members,
				# so it is not only obvious for such members to be declared with different names, but
				# also very important, cause handling of "loggy" member has critical particularity:
				# if there will be more than one LibraryContrib class (means class with CONTRIB_HOOK
				# which is set to True by default) that will have different name, this object will
				# be set as loggy for current layer; if the same name "loggy" will be declared for
				# different layers, it is always the upper layer "loggy" will be returned as already
				# initiated, so other "loggy" declarations will be skipped.
				if	getattr(layer_hook, "CONTRIB_HOOK", None):
					setattr(self, "loggy", layer_hook)
					getattr(self, "loggy")
					continue


				# For a Transmutable the "_MUTABLE_CHAIN_HOOK" set to True is a trigger to consider
				# this "layer" as a Transmutable to be initiated. At this point any encountered
				# entity that has "_MUTABLE_CHAIN_HOOK" is considered to be a Transmutable type.
				elif	getattr(layer_hook, "_MUTABLE_CHAIN_HOOK", None):	layer = layer_hook
				else:	continue


				# The ending step for every mutable chain member candidate. At this point a "layer"
				# must be a Transmutable class which, when will be invoked with an "upper_layer_link"
				# as a current layer Transmutable object, will start it's own descent mutable chain
				# initiation, and will return a Transmutable object to be assigned as a nested layer
				# for current Transmutable object. Such assignment is just a setting an attribute
				# that points to an object, using it's declaration name "inner". Any possible exceptions,
				# that might occur during nested Transmutable initiation, will be caught and basically
				# skipped, means the global initiation of mutable chain will not be interrupted, but
				# current layer will try to log corresponding error message. If somehow "layer"
				# initiation will result not a Transmutable object, and in case "layer" initiation
				# caused Exception raise, such "inner" member will be deleted from current Transmutable
				# namespace, to prevent undefined behavior for improperly initiated mutable chain members,
				# cause it remained as a type.
				try:	mutable = layer(self)
				except	Exception as E : self.loggy.error(f"{inner} nesting caused {patronus(E)}")
				else:
					if	isinstance(mutable, Transmutable):
						setattr(self, inner, mutable)
						continue


					self.loggy.error(f"{inner} nesting caused not Transmutable mutation")
				delattr(self.__class__, inner)




		# The last step for phase two of initiation is an optional keyword processing. That stands
		# for maintaining any keyword arguments at the very top layer of mutable chain, cause
		# probably there is no way any nested layer could be initiated with any arguments other
		# than "upper_layer_link". It is also the place where such keyword arguments are accessible
		# for any descent mutable chain member. The purpose of such keyword arguments is the same
		# as for declarable fields, so fields could be overwritten, but only on the very top layer,
		# any descent fields are out of touch and are reachable at the first place for members
		# they are declared under. But the very top layer arguments are still reachable for any
		# member, even with it's own fields with same names, via the "_UPPER_LAYER" chaining calls,
		# so the very top layer can provide "defaults". Anyway, no descent member should rely on
		# such keyword arguments in their initiation phases, cause this keyword arguments will become
		# a part of mutable chain in the very last moment.
		for k,v in kwargs.items() : setattr(self, k,v)







