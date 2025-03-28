magical
-------
As magic is the basis of the basics, ``magical`` is the core module for ``pygwarts``. First of all ``philosophers_stone.Transmutable`` is the base class of ``pygwarts`` object model. Almost all ``pygwarts`` objects are inherited from this class. Such object model implies nesting ``Transmutable`` objects in each other, which implements the following concept:
<br>
* <b>modularity</b> - by declaring ``Transmutable`` objects, every functionality might be altered the way another ``Transmutable`` is implemented;
* <b>escalation</b> - all nested ``Transmutable`` objects have an access to all members of it's upper layer;
* <b>logging</b> - special class ``LibraryContrib`` implements crucial feature for ``Transmutable`` logging, which offers structure and performance.
<br>Such concept is name "mutable chain" and fully relies on ``Transmutable`` declaration. Another way of altering existent ``Transmutable`` behavior is decorators, so ``magical`` offers ``Transmutation`` and ``ControlledTransmutation`` wrappers, which integrates in "mutable chain". Another fundamental classes are ``Chest`` and ``KeyChest``, which implements mutable containers concept. Utility ``TimeTurner`` is one of not a ``Transmutable`` classes, offers standard library ``datetime`` ultimate wrapper.

irma
----
This module is about library and offers three submodules:
<br>
* <b>contrib</b> - not ``Transmutable`` class ``LibraryContrib`` is a wrapper over standard library ``logging`` module, which might work for any objects,
but offers special features exactly for "mutable chain"; it also has it's own decorator ``ContribInterceptor`` to maintain logging;
* <b>access</b> - all ``LibraryContrib`` log files might be parsed and explored with this submodule;
* <b>shelve</b> - wrapping over standard library ``shelve`` module, integrated into "mutable chain".

hagrid
------
Perhaps the most useful module, that suggests files and folders manipulations. ``hagrid`` can synchronize whole trees, along with statistical information maintaining.
The core feature is working with files by exploring it's modification time, treating them like "leafs" of the "tree" folders. ``hagrid`` is built upon standard library
``pathlib`` module and is robust for vast of synchronization techniques.

filch
-----
Network module, which is not strong enough to have it's own implementations of working with actual network, but has some classes that allows processing outputs from third party objects.
Some base classes are represented as a concept of accepting some callable objects to do all the work, and postprocessing it after.

hedwig
------
Module that allows sending emails (suddenly).