import os

import wx

class MainWindow(wx.Frame):
	"""
	This class represents the main window and its contents.
	"""

	def __init__(self, parent, title, username):
		"""
		Initialize superclass, add sizers with content returned from 
		functions, and show the window.
		"""
		# Initialize superclass.
		wx.Frame.__init__(self, parent, title=title, size=(1280, 720))

		# Save username variable.
		self.username = username

		# Load plot images from figures/ folder and create choice option list.
		self.load_images(username)

		# Init UI.
		self.init_ui()

		# Show window.
		self.Center()
		self.Show(True)

		# Initial image update.
		self.update_image()

		self.Bind(wx.EVT_SIZE, self.resize_event)

	def init_ui(self):
		"""
		Initialize UI.
		"""
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
		main_sizer.Add(content_sizer, proportion=1, flag=wx.ALL | wx.EXPAND)

		# Set panel sizer.
		self.panel.SetSizer(main_sizer)

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
		content_sizer.Add(plot_sizer, proportion=1, \
			flag=wx.EXPAND | wx.ALL)

		# Return sizer.
		return content_sizer

	def get_user_input_sizer(self):
		"""
		Returns the user input sizer.
		"""
		# Create user input sizer.
		user_input_sizer = wx.BoxSizer(wx.VERTICAL)

		# Create input grid.
		input_grid = wx.GridBagSizer(vgap=0, hgap=20)

		# Create language label and dropdown.
		language_options = list(self.language_options.keys())
		language_select_label = wx.StaticText(self.panel, label="Language", \
			pos=(50, 0))
		self.language_select_dropdown = wx.Choice(self.panel, \
			choices=language_options, size=wx.Size(150, 25))
		self.language_select_dropdown.SetSelection(0)
		self.Bind(wx.EVT_CHOICE, self.language_select_event, \
			self.language_select_dropdown)

		# Create plot selector label and dropdown.
		plot_options = self.language_options[language_options[0]]
		plot_select_label = wx.StaticText(self.panel, label="Plot")
		self.plot_select_dropdown = wx.Choice(self.panel, \
			choices=plot_options, size=wx.Size(150, 25))
		self.plot_select_dropdown.SetSelection(0)
		self.Bind(wx.EVT_CHOICE, self.plot_select_event, \
			self.plot_select_dropdown)

		# Create `Regenerate plots` button.
		regen_plots_button = wx.Button(self.panel, label="Regenerate plots", \
			size=(106, 27))
		self.Bind(wx.EVT_BUTTON, self.regenerate_plots, regen_plots_button)

		# Add components to input grid.
		input_grid.Add(language_select_label, pos=(0, 0), \
			flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
		input_grid.Add(self.language_select_dropdown, pos=(0, 1), \
			flag=wx.ALIGN_RIGHT)
		input_grid.Add(plot_select_label, pos=(1, 0), \
			flag=wx.ALIGN_LEFT | wx.ALIGN_CENTER_VERTICAL)
		input_grid.Add(self.plot_select_dropdown, pos=(1, 1), \
			flag=wx.ALIGN_RIGHT)
		input_grid.Add(regen_plots_button, pos=(2, 0), span=(1, 2), \
			flag=wx.ALIGN_CENTER_HORIZONTAL)

		# Add input grid to user input sizer.
		user_input_sizer.Add(input_grid, flag=wx.ALL, border=5)

		# Return user input sizer.
		return user_input_sizer

	def get_plot_sizer(self):
		"""
		Returns the plot sizer.
		"""
		# Create plot sizer, make member to be able to get its size.
		self.plot_sizer = wx.BoxSizer(wx.VERTICAL)

		# Create image control, make member to be able to update the image.
		self.plot_image_holder = wx.StaticBitmap(self.panel)

		# Add image control to plot sizer.
		self.plot_sizer.Add(self.plot_image_holder, flag=wx.EXPAND | wx.ALL, \
			border=5)

		# Return plot sizer.
		return self.plot_sizer

	def load_images(self, username=""):
		"""
		Reloads plot images from disk, changes the username if it's not empty.
		Updates the self.plots_dict dictionary. Also updates dropdown options.
		"""
		# Update username if required.
		if not username == "":
			self.username = username

		# Construct base folder.
		base_folder = f"figures/{self.username}"

		# Initialize language dropdown dictionary and plot image dictionary.
		self.plots_dict = {}
		self.language_options = {}

		# Load plot images from figures/ folder and create choice option list.
		language_folders = os.listdir(base_folder)
		for lang in language_folders:
			# Create language entry.
			lang_capitalized = f"{lang[0].upper()}{lang[1:]}"
			self.plots_dict[lang_capitalized] = {}
			self.language_options[lang_capitalized] = []

			# Load images.
			for plot_name \
				in ["daily_xp", "total_xp", "total_words_learned", "level"]:
				plot_name_capitalized = f"{plot_name[0].upper()}" \
					f"{plot_name[1:]}".replace("_", " ")
				image = wx.Image(f"{base_folder}/{lang}/{plot_name}.png", \
					wx.BITMAP_TYPE_ANY)

				if not image.IsOk():
					#print(f"Image not ok: {lang}/{plot_name}")
					continue

				self.plots_dict[lang_capitalized][plot_name_capitalized] = \
					image
				self.language_options[lang_capitalized]\
					.append(plot_name_capitalized)
				#print(f"Image ok: {lang}/{plot_name}")

	def resize_event(self, event):
		"""
		Gets called when the window is resized.
		"""
		# Run normal window resize stuff.
		event.Skip()
		# Rescale image.
		self.rescale_image()

	def language_select_event(self, event):
		"""
		Gets called when the language choice menu triggers and event. Update
		the plot options to match the available plots for the selected
		language. Reset the plot options dropdown if the currently selected
		choice does not exist for the new language. Then update the plot
		image.
		"""
		# Get currently selected plot.
		selected_plot_index = \
			self.plot_select_dropdown.GetSelection()
		selected_plot_string = \
			self.plot_select_dropdown.GetString(selected_plot_index)

		# Get currently selected language.
		selected_lang_index = \
			self.language_select_dropdown.GetSelection()
		selected_lang_string = \
			self.language_select_dropdown.GetString(selected_lang_index)

		# Update plot options dropdown.
		plot_options = self.language_options[selected_lang_string]
		self.plot_select_dropdown.Clear()
		for option in plot_options:
			self.plot_select_dropdown.Append(option)

		# Check if currently selected language also features the previously
		# selected plot.
		if selected_plot_string in plot_options:
			# Get index of previous selection in new options list.
			previous_selection_index = \
				plot_options.index(selected_plot_string)
			# Set selection id.
			self.plot_select_dropdown.SetSelection(previous_selection_index)
		else:
			# Selected language does not feature the previously selected plot
			# option, reset the selection to index 0.
			self.plot_select_dropdown.SetSelection(0)

		# Update the plot image.
		self.update_image()

	def plot_select_event(self, event):
		"""
		Gets called when the plot choice menu triggers an event. Updates the
		plot image.
		"""
		# Update the plot image.
		self.update_image()

	def update_image(self):
		"""
		Update the bitmap component of the plot image holder to the selected
		plot.
		"""
		# Get selected language in string format.
		selected_language_index = \
			self.language_select_dropdown.GetSelection()
		selected_language = \
			self.language_select_dropdown.GetString(selected_language_index)

		# Get select plot in string format.
		selected_plot_index = \
			self.plot_select_dropdown.GetSelection()
		selected_plot = \
			self.plot_select_dropdown.GetString(selected_plot_index)

		# Set plot_image to image object from dictionary.
		self.plot_image = self.plots_dict[selected_language][selected_plot]

		# Rescale the image.
		self.rescale_image()

	def rescale_image(self):
		"""
		Scales the set plot_image to match either the width or the height of
		the plot_sizer, whichever makes the image be entirely visible.
		"""
		# Get width and height of plot sizer.
		sizer_width, sizer_height = self.plot_sizer.GetSize()

		# Get width and height of image.
		image_width, image_height = self.plot_image.GetSize()
		image_aspect = image_width / image_height

		# Scale to match sizer height.
		sh_image_width  = int(sizer_height * image_aspect)
		sh_image_height = int(sizer_height)

		# Scale to match sizer width.
		sw_image_width  = int(sizer_width)
		sw_image_height = int(sizer_width / image_aspect)

		# Check if scaling by height makes the image not too wide.
		if sh_image_width <= sizer_width:
			# Scale to match height.
			image = self.plot_image.Scale(sh_image_width, sh_image_height)
			self.plot_image_holder.SetBitmap(wx.Bitmap(image))
		# Check if scaling by width makes the image not too tall.
		else:
			# Scale to match width.
			image = self.plot_image.Scale(sw_image_width, sw_image_height)
			self.plot_image_holder.SetBitmap(wx.Bitmap(image))

	def regenerate_plots(self, event):
		""""""
		# Comment.
		print("Regenerate plots")

if __name__ == "__main__":
	app = wx.App(False)
	window = MainWindow(None, "Duolingo Data Visualizer", "Rubenanz")
	app.MainLoop()