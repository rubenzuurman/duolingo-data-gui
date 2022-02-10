import wx

class MainWindow(wx.Frame):
	"""
	This class represents the main window and its contents.
	"""

	def __init__(self, parent, title):
		"""
		Initialize superclass, add sizers with content returned from 
		functions, and show the window.
		"""
		# Initialize superclass.
		wx.Frame.__init__(self, parent, title=title, size=(1280, 720))

		# Create a top level panel so it looks correct on all platforms.
		self.panel = wx.Panel(self, wx.ID_ANY)

		# Get program title sizer.
		title_sizer = self.get_title_sizer("Duolingo Statistics Viewer")
		# Get content sizer.
		content_sizer = self.get_content_sizer()

		# Create main sizer and add the other sizers to it.
		main_sizer = wx.BoxSizer(wx.VERTICAL)
		# Expand all for horizontal expansion.
		main_sizer.Add(title_sizer, proportion=1, flag=wx.ALL | wx.EXPAND)
		# Expand all for horizontal expansion.
		main_sizer.Add(content_sizer, proportion=9, flag=wx.ALL | wx.EXPAND)

		# Set panel sizer.
		self.panel.SetSizer(main_sizer)

		# Show window.
		self.Show(True)

	def get_title_sizer(self, title):
		"""
		Assumes title is a string. Creates and returns a horizontal sizer 
		containing the title as text.
		"""
		# Create vertical sizer.
		title_sizer = wx.BoxSizer(wx.VERTICAL)

		# Create and add static text.
		#title_text = wx.StaticText(self.panel, id=wx.ID_ANY, label=title)
		#title_sizer.Add(title_text, flag=wx.ALIGN_CENTER_HORIZONTAL)

		btn = wx.Button(self.panel, id=wx.ID_ANY)
		title_sizer.Add(btn, 1, flag=wx.EXPAND | wx.ALL)

		# Return sizer.
		return title_sizer

	def get_content_sizer(self):
		"""
		Creates the content sizer and adds the user input sizer and the plot
		sizer to it. Then returns the sizer.
		"""
		# Create horizontal sizer.
		content_sizer = wx.BoxSizer(wx.HORIZONTAL)

		# Create and add horizontal sizer for user input.
		user_input_sizer = self.get_user_input_sizer()
		# Expand all for vertical expansion.
		content_sizer.Add(user_input_sizer, proportion=2, flag=wx.EXPAND | wx.ALL)

		# Create and add horizontal sizer for rendering the plots.
		plot_sizer = self.get_plot_sizer()
		# Expand all for vertical expansion.
		content_sizer.Add(plot_sizer, proportion=8, flag=wx.EXPAND | wx.ALL)

		# Return sizer.
		return content_sizer

	def get_user_input_sizer(self):
		""""""
		user_input_sizer = wx.BoxSizer(wx.VERTICAL)

		btn = wx.Button(self.panel, id=wx.ID_ANY)
		user_input_sizer.Add(btn, 1, flag=wx.EXPAND | wx.ALL)

		return user_input_sizer

	def get_plot_sizer(self):
		""""""
		plot_sizer = wx.BoxSizer(wx.VERTICAL)

		btn = wx.Button(self.panel, id=wx.ID_ANY)
		plot_sizer.Add(btn, 1, flag=wx.EXPAND | wx.ALL)

		return plot_sizer

app = wx.App(False)
window = MainWindow(None, "Hello world")
app.MainLoop()