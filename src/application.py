import wx

import logger as log
import window as win

def main():
	# Initialize logger class.
	logger = log.Logger(loglevel=log.LogLevel.ERROR)

	# Create log program start message.
	logger.log_info("Application started")

	# Run user interface.
	app = wx.App(False)
	window = win.MainWindow(None, "Duolingo Data Visualizer", "Rubenanz", \
		logger)
	app.MainLoop()

	# Create log program end message.
	logger.log_info("Application stopped")

	# Export log to `logs` folder.
	logger.output_to_file()

if __name__ == "__main__":
	main()