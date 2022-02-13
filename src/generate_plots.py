from datetime import datetime
import errno
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(username: str):
	"""
	Assumes `username` is a string. Loads data from all csv files present in
	the folder `data/{username}/` into a dictionary of dataframes, where the
	keys are the respective filenames without extension. Returns the
	aforementioned dictionary.
	"""
	# Define folder.
	userfolder = f"data/{username}/"

	# Check if the folder exists.
	if not os.path.exists(userfolder):
		raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), \
			userfolder)

	# Initiate dictionary.
	lang_dict = {}

	# Loop all files in the directory.
	for file in os.listdir(f"data/{username}/"):
		# Check if filename has the extension `csv`.
		if not file.endswith(".csv"):
			continue

		# Construct full relative filename.
		filename = userfolder + file

		# Load file into dataframe using pandas.
		df = pd.read_csv(filename, delimiter=";")
		
		# Add dataframe to dictionary.
		lang_dict[".".join(file.split(".")[:-1])] = df

	# Return dictionary.
	return lang_dict

def add_time_column(lang_dict: dict):
	"""
	Assumes `lang_dict` is a dictionary containing dataframes, as returned by
	the function load_data(). Adds a column to every dataframe named
	`seconds_since_epoch`, which will contain the amount of seconds passed
	since Januari 1st 2010 for every entry. Duolingo was founded late in 2011
	[https://en.wikipedia.org/wiki/Duolingo] so this should cover all
	possible dates. This will be used for the x-axis values of the plots.
	Returns the dictionary with added columns to the dataframes.
	"""
	# Define epoch date.
	epoch_date = datetime.strptime("01-01-2010", "%d-%m-%Y")
	
	# Loop over all entries in the dictionary.
	for lang, df in lang_dict.items():
		# Initialize list of seconds since epoch.
		seconds_since_epoch_list = []

		# Loop all rows in the dataframe.
		for index, row in df.iterrows():
			# Convert `date` entry to seconds since epoch and add to list.
			current_date = datetime.strptime(row["date"], "%d-%m-%Y")
			seconds_since_epoch = (current_date - epoch_date).total_seconds()
			seconds_since_epoch_list.append(seconds_since_epoch)

		# Add column to dataframe.
		df["seconds_since_epoch"] = seconds_since_epoch_list
		# Convert column from float64 to int64.
		df["seconds_since_epoch"] = df["seconds_since_epoch"].astype(np.int64)

	# Return dictionary.
	return lang_dict

def export_plots(lang_dict: dict, username: str):
	"""
	Assumes `lang_dict` is a dictionary containing dataframes, as returned by
	the function add_time_column(). Assumes `username` is a string and 
	identical to the `username` supplied to load_data(). Exports a plot for 
	every language for the columns `daily_xp`, `total_xp`, 
	`total_words_learned` and `level`. These plots will have automatic x- and 
	y-limits and will be saved to `figures/{username}/`.
	"""
	# Create `figures` folder if it does not exist.
	if not os.path.isdir("figures"):
		os.mkdir("figures")

	# Create `figures/{username}` folder if it does not exist.
	if not os.path.isdir(f"figures/{username}"):
		os.mkdir(f"figures/{username}")

	# Create folders for every language if it does not exist.
	for lang in lang_dict.keys():
		if not os.path.isdir(f"figures/{username}/{lang}"):
			os.mkdir(f"figures/{username}/{lang}")

	# Calculate xticks values and construct ticks list and labels list.
	# Initialize lists.
	xticks = []
	xlabels = []

	# Initialize epoch datetime object.
	epoch = datetime.strptime("01-01-2010", "%d-%m-%Y")
	# Loop from 2010 until the current year.
	for year in range(2010, datetime.now().year + 1):
		# Loop from month 1 to month 12.
		for month in range(1, 13):
			# Create datetime object from year and month.
			cur_date = datetime.strptime(f"01-{month}-{year}", "%d-%m-%Y")

			# Calculate seconds since epoch and add to xticks list.
			delta_seconds = (cur_date - epoch).total_seconds()
			xticks.append(delta_seconds)

			# Construct label and add to xlabels list.
			month_str = f"{month}" if month > 9 else f"0{month}"
			year_str = f"{year}"
			label = f"{month_str}/{year_str}"
			xlabels.append(label)

	# Loop over all dataframes and generate plots.
	for lang, df in lang_dict.items():
		# Extract columns.
		daily_xp_col = df["daily_xp"]
		total_xp_col = df["total_xp"]
		total_words_learned_col = df["total_words_learned"]
		level_col = df["level"]
		seconds_since_epoch_col = df["seconds_since_epoch"]

		# Define save paths.
		daily_xp_path = f"figures/{username}/{lang}/daily_xp.png"
		total_xp_path = f"figures/{username}/{lang}/total_xp.png"
		total_words_learned_path = \
			f"figures/{username}/{lang}/total_words_learned.png"
		level_path = f"figures/{username}/{lang}/level.png"

		# Calculate xmin and xmax, subtract month from xmin and add month to
		# xmax.
		extra_days = 10
		xmin = min(seconds_since_epoch_col) - (86400 * extra_days)
		xmax = max(seconds_since_epoch_col) + (86400 * extra_days)
		xticks_rotation = 60
		plot_dpi = 400

		# Plot daily xp and save to file.
		fig, ax = plt.subplots()
		ax.plot(seconds_since_epoch_col, daily_xp_col, "b-", linewidth=1)
		ax.set_xlabel("Date")
		ax.set_ylabel("Experience")
		ax.set_title("Daily Experience")
		ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
		ax.set_xlim(xmin, xmax)
		fig.tight_layout()
		fig.savefig(daily_xp_path, dpi=plot_dpi)

		# Plot total xp and save to file.
		fig, ax = plt.subplots()
		ax.plot(seconds_since_epoch_col, total_xp_col, "b-", linewidth=1)
		ax.set_xlabel("Date")
		ax.set_ylabel("Experience")
		ax.set_title("Total Experience")
		ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
		ax.set_xlim(xmin, xmax)
		fig.tight_layout()
		fig.savefig(total_xp_path, dpi=plot_dpi)

		# Plot total words learned and save to file.
		fig, ax = plt.subplots()
		ax.plot(seconds_since_epoch_col, total_words_learned_col, "b-", \
			linewidth=1)
		ax.set_xlabel("Date")
		ax.set_ylabel("Words")
		ax.set_title("Total Words Learned")
		ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
		ax.set_xlim(xmin, xmax)
		fig.tight_layout()
		fig.savefig(total_words_learned_path, dpi=plot_dpi)

		# Plot level and save to file.
		fig, ax = plt.subplots()
		ax.plot(seconds_since_epoch_col, level_col, "b-", linewidth=1)
		ax.set_xlabel("Date")
		ax.set_ylabel("Level")
		ax.set_title("Level")
		ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
		ax.set_xlim(xmin, xmax)
		fig.tight_layout()
		fig.savefig(level_path, dpi=plot_dpi)

	# Close all figures, if this is not done memory will stay allocated and
	# wxpython will not be able to exit the mainloop. Also if this is not done
	# matplotlib will keep the figures in memory and throw a warning once the
	# number of figures in memory exceeds 20.
	plt.close("all")