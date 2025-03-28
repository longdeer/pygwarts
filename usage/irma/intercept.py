import	re
from	typing							import List
from	time							import sleep
from	requests						import get as GET
from	pygwarts.irma.contrib.intercept	import PoolHoist
from	pygwarts.magical.spells			import patronus








class TelegramHoist(PoolHoist):

	"""
		irma.contrib.intercept.PoolHoist implementation for reporting logging messages to telegram.
		Intercepts all levels, except DEBUG. Level INFO triggers only watchdog algorithm, so INFO
		messages are hoisted only for certain objects, which names are provided by LibraryContrib
		parent object field "watchdog", the same way force fields are provided. For higher levels
		messages immediately hoisted. After "buffer_release" will try to send concatenated dump
		via telegram api.
	"""

	def __call__(self):
		class Interceptor(super().__call__()):

			def __init__(self, *args, **kwargs):
				super().__init__(*args, **kwargs)

				if	isinstance(getattr(self, "watchdog", None), tuple):
					self.watchdog_map = { re.compile(P.replace("*",".*")) for P in self.watchdog }

			def info(self, message :str):

				if	isinstance(getattr(self, "watchdog_map", None), set):
					for pattern in self.watchdog_map:

						if	isinstance(pattern, re.Pattern):
							if	pattern.fullmatch(self.handover_name):

								self.buffer_insert(f"{self.handover_name} watchdog: {message}")

				return super().info(message)

			def warning(self, message :str):

				self.buffer_insert(f"{self.handover_name} WARNING: {message}")
				return super().warning(message)

			def error(self, message :str):

				self.buffer_insert(f"{self.handover_name} ERROR: {message}")
				return super().error(message)

			def critical(self, message :str):

				self.buffer_insert(f"{self.handover_name} CRITICAL: {message}")
				return super().critical(message)

			def buffer_release(self, *args, **kwargs) -> List[str] :

				buffer_dump = super().buffer_release(*args, **kwargs)
				dump_message = "\n".join(buffer_dump)
				delay = 0

				try:

					# Sending dump by chunks cause Telegram
					# has limit 4096 symbols per message
					for i in range(0, len(dump_message), 4096):
						sleep(delay)

						GET(

							"https://api.telegram.org/bot"
							"TELEGRAM BOT TOKEN"					# Telegram bot token string goes here
							"/sendMessage",
							{
								"chat_id":	"CHAT ID",				# Telegram chat id string goes here
								"text":		dump_message[i:i+4096],
							}
						)

						delay += 1

				except	Exception as E : self.pool_debug(f"Buffer chunk {delay} failed due to {patronus(E)}")
				return	buffer_dump


		return	Interceptor







