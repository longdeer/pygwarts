import	os
import	sys
import	argparse
import	unittest
from	shutil			import rmtree
from	pygwarts.tests	import PygwartsTestCase








if	__name__ == "__main__" :

	current_test = argparse.ArgumentParser(

		prog="unit_main",
		usage="unit_main [-i {magical, irma, hagrid, filch, hedwig}] [-d PATH] [-c]",
		description=str(

			"pygwarts unit tests module.\n"
			"Current tests count:\n"
			"total:   1128\n"
			"magical: 455\n"
			"irma:    262\n"
			"hagrid:  240\n"
			"filch:   98\n"
			"hedwig:  73\n"
			"\n"
		),
		epilog=str(

			"pygwarts 1.5.1.4"
			"\nlngd\n\n"
		),
		formatter_class=argparse.RawDescriptionHelpFormatter
	)
	current_test.add_argument(

		"-i", "--include",
		help="include certain modules to run unit tests (all included if omitted)",
		default=[ "magical", "irma", "hagrid", "filch", "hedwig" ],
		nargs="+",
	)
	current_test.add_argument(

		"-d", "--directory",
		help=str(

			"set working directory for tests files "
			f"(default {os.path.expanduser('~')}{os.path.sep}pygwarts-test-folder)"
		),
	)
	current_test.add_argument(

		"-c", "--clean-up",
		action="store_true",
		help=str("erase working directory after tests run, no matter results"),
	)
	current_args = current_test.parse_args()


	if current_args.directory is not None : PygwartsTestCase._PygwartsTestCase__CWD = current_args.directory
	PygwartsTestCase.clean_up = current_args.clean_up


	for module_name in set(current_args.include):
		match module_name:

			case "magical":	from pygwarts.tests.magical.unit_magical_main	import *
			case "irma":	from pygwarts.tests.irma.unit_irma_main			import *
			case "hagrid":	from pygwarts.tests.hagrid.unit_hagrid_main		import *
			case "filch":	from pygwarts.tests.filch.unit_filch_main		import *
			case "hedwig":	from pygwarts.tests.hedwig.unit_hedwig_main		import *
			case _:

				print(f"\nInvalid module \"{module_name}\"")
				sys.exit(1)


	unittest.main(verbosity=2, argv=[ sys.argv[0] ], exit=False)
	if current_args.clean_up : rmtree(PygwartsTestCase._PygwartsTestCase__CWD)







