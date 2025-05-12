from pygwarts.irma.contrib				import LibraryContrib
from pygwarts.irma.contrib.intercept	import STDOUTL








# Besides mutable chain, LibraryContrib might be used by any other entities, by just
# declaring it and initiating the way it is usually goes in Python. All functionality,
# except "handover", will be available.
logger = LibraryContrib(handler="path to file", init_name="logger name", init_level=10)
logger.debug("Logger is used")
logger.info("Logger is used")
logger.warning("Logger is used")
logger.error("Logger is used")
logger.critical("Logger is used")








# It is also possible to use interceptors outside mutable chain with LibraryContrib, by either
# declaring the whole decorated class,
@STDOUTL
class DualLogger(LibraryContrib):

	handler		= "path to file"
	init_name	= "logger name"
	init_level	= 10

wrapper = DualLogger()
logger = wrapper()
logger.debug("Logger is used")
logger.info("Logger is used")
logger.warning("Logger is used")
logger.error("Logger is used")
logger.critical("Logger is used")








# or by inheriting and initiating,
@STDOUTL
class DualLogger(LibraryContrib): pass
wrapper = DualLogger()
logger = wrapper(handler="path to file", init_name="logger name", init_level=10)
logger.debug("Logger is used")
logger.info("Logger is used")
logger.warning("Logger is used")
logger.error("Logger is used")
logger.critical("Logger is used")








# or by the old school method, by directly passing LibraryContrib as argument to decorator.
outer_wrapper = STDOUTL(LibraryContrib)
inner_wrapper = outer_wrapper()
logger = inner_wrapper(handler="path to file", init_name="logger name", init_level=10)
logger.debug("Logger is used")
logger.info("Logger is used")
logger.warning("Logger is used")
logger.error("Logger is used")
logger.critical("Logger is used")







