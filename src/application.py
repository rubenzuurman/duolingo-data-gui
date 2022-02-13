import wx

import window as win

def main():
	# Show user interface.
	app = wx.App(False)
	window = win.MainWindow(None, "Duolingo Data Visualizer", "Rubenanz")
	app.MainLoop()

if __name__ == "__main__":
	main()