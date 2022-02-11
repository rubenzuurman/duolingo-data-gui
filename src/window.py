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
		title_sizer = self.get_title_sizer("Duolingo Data Visualizer")
		# Get content sizer.
		content_sizer = self.get_content_sizer()

		# Create main sizer and add the other sizers to it.
		main_sizer = wx.BoxSizer(wx.VERTICAL)
		# Expand all for horizontal expansion.
		main_sizer.Add(title_sizer, proportion=0, flag=wx.ALL | wx.EXPAND)
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
		title_sizer = wx.BoxSizer(wx.HORIZONTAL)

		# Create title text font.
		title_font = wx.Font(40, wx.FONTFAMILY_DECORATIVE, \
			wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

		# Create and add static text.
		title_text = wx.StaticText(self.panel, id=wx.ID_ANY, label=title, \
			style=wx.ALIGN_CENTER_HORIZONTAL)
		title_text.SetFont(title_font)
		title_sizer.Add(title_text, 1, \
			flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=5)

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
		content_sizer.Add(user_input_sizer, proportion=0, \
			flag=wx.EXPAND | wx.ALL)

		# Create and add horizontal sizer for rendering the plots.
		plot_sizer = self.get_plot_sizer()
		# Expand all for vertical expansion.
		content_sizer.Add(plot_sizer, proportion=8, \
			flag=wx.EXPAND | wx.ALL)

		# Return sizer.
		return content_sizer

	def get_user_input_sizer(self):
		""""""
		# Create user input sizer.
		user_input_sizer = wx.BoxSizer(wx.VERTICAL)

		# Create input grid.
		input_grid = wx.GridBagSizer(vgap=0, hgap=20)

		# Create language label and dropdown.
		language_select_label = wx.StaticText(self.panel, label="Language", \
			pos=(50, 0))
		language_select_dropdown = wx.Choice(self.panel, \
			choices=["Norwegian (Bokmal)", "ghghghghghghgh"], \
			size=wx.Size(150, 25))

		# Create plot selector label and dropdown.
		plot_select_label = wx.StaticText(self.panel, label="Plot")
		plot_select_dropdown = wx.Choice(self.panel, \
			choices=["Banana", "Mango"], size=wx.Size(150, 25))

		# Create `Regenerate plots` button.
		regen_plots_button = wx.Button(self.panel, label="Regenerate plots", \
			size=(106, 27))

		# Add components to input grid.
		input_grid.Add(language_select_label, pos=(0, 0), \
			flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
		input_grid.Add(language_select_dropdown, pos=(0, 1), \
			flag=wx.ALIGN_RIGHT)
		input_grid.Add(plot_select_label, pos=(1, 0), \
			flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
		input_grid.Add(plot_select_dropdown, pos=(1, 1), \
			flag=wx.ALIGN_RIGHT)
		input_grid.Add(regen_plots_button, pos=(2, 0), span=(1, 2), \
			flag=wx.ALIGN_CENTER_HORIZONTAL)

		# Add input grid to user input sizer.
		user_input_sizer.Add(input_grid, flag=wx.ALL, border=5)

		# Return user input sizer.
		return user_input_sizer

	def get_plot_sizer(self):
		""""""
		# Create plot sizer, make member to be able to get its size.
		self.plot_sizer = wx.BoxSizer(wx.VERTICAL)
		
		# Create image object, make member to be able to scale on window 
		# resize.
		self.plot_image = wx.Image(\
			"doc/images/loading_screen_layout_v1.png", wx.BITMAP_TYPE_ANY)
		# Create image control with dummy image, make member to be able to
		# update the image.
		self.plot_image_holder = wx.StaticBitmap(self.panel)
		self.plot_image_holder.SetBitmap(wx.Bitmap(self.plot_image))

		# Add image control to plot sizer.
		self.plot_sizer.Add(self.plot_image_holder, flag=wx.EXPAND | wx.ALL, \
			border=5)

		# Return plot sizer.
		return self.plot_sizer

if __name__ == "__main__":
	app = wx.App(False)
	window = MainWindow(None, "Duolingo Data Visualizer")
	app.MainLoop()