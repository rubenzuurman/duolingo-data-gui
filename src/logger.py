from datetime import datetime
from enum import Enum
import os

class LogLevel(Enum):
	"""
	Class holding all possible `LogLevel` states. Everything below a threshold
	set by the Logger will be output.
	"""
	INFO = 0
	DEBUG = 1
	ERROR = 2

	# MAX_LENGTH holds the length of the longest loglevel, useful for 
	# constructing strings from the loglevel.
	MAX_LENGTH = 5

class Logger:
	"""
	Class for collecting, holding and outputting info-, debug- and 
	error messages.
	"""
	def __init__(self, loglevel=LogLevel.INFO):
		"""
		Set loglevel, initialize messages list and construct filename.
		"""
		# Check if loglevel is an instance of LogLevel.
		assert isinstance(loglevel, LogLevel), "src/logger.py" \
			":__init__(): Parameter `loglevel` must be an instance of " \
			"the enum class LogLevel."

		# Set loglevel variable. Messages will only be output during runtime 
		# if the loglevel of the message is smaller than or equal to the 
		# loglevel of the Logger class.
		self.loglevel = loglevel

		# Initialize messages list.
		self.messages = []

		# Get start date and time.
		self.filename = datetime.now().strftime("LOG_%Y_%m_%d_%H_%M_%S.txt")

	def output_to_file(self):
		"""
		Outputs all submitted messages to a log file in the folder `logs`.
		"""
		# Check if logs folder already exists, if not: create it.
		if not os.path.isdir("logs/"):
			os.mkdir("logs/")

		# Write to log file.
		with open(f"logs/{self.filename}", "w") as file:
			# Loop over all messages.
			for message_tuple in self.messages:
				# Extract tuple components.
				dt_object, loglevel, message = message_tuple

				# Construct datetime string.
				dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")

				# Construct full line string. The spaces is the amount of 
				# spaces between loglevel and the datetime. The loglevel 
				# names have different lengths, this makes sure the datetimes
				# are aligned.
				spaces = \
					" " * (LogLevel.MAX_LENGTH.value - len(loglevel.name) + 1)
				line = f"[{loglevel.name}]{spaces}[{dt_string}] {message}\n"

				# Write to file.
				file.write(line)

	def add_message(self, loglevel, message):
		"""
		Adds the message with the loglevel and timestamp to the messages
		list. Outputs the message to the console if the loglevel parameter
		is less than or equal to self.loglevel.
		"""
		# Check if loglevel is an instance of LogLevel.
		assert isinstance(loglevel, LogLevel), "src/logger.py" \
			":add_message(): Parameter `loglevel` must be an instance of " \
			"the enum class LogLevel."

		# Construct datetime object.
		dt_object = datetime.now()

		# Add to messages list.
		self.messages.append((dt_object, loglevel, message))

		# Output message if required.
		if loglevel.value <= self.loglevel.value:
			# Construct datetime string from datetime object.
			dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
			# The spaces is the amount of spaces between loglevel and the 
			# datetime. The loglevel names have different lengths, this makes 
			# sure the datetimes are aligned.
			spaces = \
				" " * (LogLevel.MAX_LENGTH.value - len(loglevel.name) + 1)
			print(f"[{loglevel.name}]{spaces}[{dt_string}] {message}")

	def log_info(self, message):
		"""
		Adds an info message.
		"""
		# Submit message.
		self.add_message(LogLevel.INFO, message)

	def log_debug(self, message):
		"""
		Adds a debug message.
		"""
		# Submit message.
		self.add_message(LogLevel.DEBUG, message)

	def log_error(self, message):
		"""
		Adds an error message.
		"""
		# Submit message.
		self.add_message(LogLevel.ERROR, message)

	def get_loglevel(self):
		"""
		Returns the loglevel.
		"""
		# Return loglevel.
		return self.loglevel

	def set_loglevel(self, loglevel):
		"""
		Sets the loglevel.
		"""
		# Check if loglevel is an instance of LogLevel.
		assert isinstance(loglevel, LogLevel), "src/logger.py" \
			":set_loglevel(): Parameter `loglevel` must be an instance of " \
			"the enum class LogLevel."

		# Set loglevel.
		self.loglevel = loglevel

def main():
	logger = Logger()
	logger.log_error("hello error")
	logger.log_debug("hello debug")
	logger.log_info("hello info")
	logger.output_to_file()

if __name__ == "__main__":
	main()