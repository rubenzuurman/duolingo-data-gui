from datetime import datetime
import errno
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def load_data(username: str, logger):
	"""
	Assumes `username` is a string. Loads data from all csv files present in
	the folder `data/{username}/` into a dictionary of dataframes, where the
	keys are the respective filenames without extension. Returns the
	aforementioned dictionary.
	"""
	# Create start log message.
	logger.log_info(f"Loading data files for user `{username}`...")

	# Define folder.
	userfolder = f"data/{username}/"

	# Check if the folder exists.
	if not os.path.exists(userfolder):
		logger.log_error(f"Userfolder does not exist `{userfolder}`!")
		logger.log_error(f"Failed loading data files for user `{username}`!")
		return False

	# Initiate dictionary.
	lang_dict = {}

	# Loop all files in the directory.
	for file in os.listdir(f"data/{username}/"):
		# Check if filename has the extension `csv`.
		if not file.endswith(".csv"):
			continue

		# Construct full relative filename.
		filename = userfolder + file

		# Log start of loading file.
		logger.log_info(f"Loading data file `{filename}`...")

		# Load file into dataframe using pandas. Catch any error while reading
		# the file and log it.
		try:
			df = pd.read_csv(filename, delimiter=";")
		except Exception as e:
			logger.log_error(f"Failed to load file `{filename}`: {e}")
		
		# Add dataframe to dictionary.
		lang_dict[".".join(file.split(".")[:-1])] = df

		# Log end of loading file.
		logger.log_info(f"Done loading data file `{filename}`")

	# Create end log message.
	logger.log_info(f"Done loading data files for user `{username}`")

	# Return dictionary.
	return lang_dict

def add_time_column(lang_dict: dict, logger):
	"""
	Assumes `lang_dict` is a dictionary containing dataframes, as returned by
	the function load_data(). Adds a column to every dataframe named
	`seconds_since_epoch`, which will contain the amount of seconds passed
	since Januari 1st 2010 for every entry. Duolingo was founded late in 2011
	[https://en.wikipedia.org/wiki/Duolingo] so this should cover all
	possible dates. This will be used for the x-axis values of the plots.
	Returns the dictionary with added columns to the dataframes.
	"""
	# Create start log message.
	logger.log_info("Adding time column to dataframes...")

	# Create list of failed languages.
	failed_langs = []

	# Define epoch date.
	epoch_date = datetime.strptime("01-01-2010", "%d-%m-%Y")
	
	# Loop over all entries in the dictionary.
	for lang, df in lang_dict.items():
		# Initialize list of seconds since epoch.
		seconds_since_epoch_list = []

		# Check if the language dataframe has a column named `date`.
		if not "date" in df.columns:
			logger.log_error("Failed to add time column to dataframe for " \
				f"language `{lang}`: missing column `date`!")
			failed_langs.append(lang)
			continue

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

	# Create end log message.
	logger.log_info("Done adding time column to dataframes")

	# Return dictionary.
	return lang_dict

def export_plots(lang_dict: dict, username: str, logger):
	"""
	Assumes `lang_dict` is a dictionary containing dataframes, as returned by
	the function add_time_column(). Assumes `username` is a string and 
	identical to the `username` supplied to load_data(). Exports a plot for 
	every language for the columns `daily_xp`, `total_xp`, 
	`total_words_learned` and `level`. These plots will have automatic x- and 
	y-limits and will be saved to `figures/{username}/`.
	"""
	# Create start log message.
	logger.log_info("Exporting plots...")

	# Set up variables to count how many images loaded successfully, and 
	# how many failed.
	successful = 0
	failed = 0

	# Create `figures` folder if it does not exist.
	if not os.path.isdir("figures"):
		os.mkdir("figures")

	# Create `figures/{username}` folder if it does not exist.
	if not os.path.isdir(f"figures/{username}"):
		os.mkdir(f"figures/{username}")

	# Create folders for every language if it does not exist.
	for lang in lang_dict.keys():
		# Check if the language has a date column, when issue 4 is 
		# implemented, this check can be removed, as plots will be exported
		# regardless.
		if not "date" in lang_dict[lang].columns:
			logger.log_error(f"Folder `figures/{username}/{lang}/` not " \
				"created: missing column `date`")
			continue
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
		# If the date column is not present, skip the language.
		if "date" in df.columns:
			seconds_since_epoch_col = df["seconds_since_epoch"]
		else:
			failed += 4
			continue

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
		if "daily_xp" in df.columns:
			# Get data.
			daily_xp_col = df["daily_xp"]

			# Create and export plot.
			fig, ax = plt.subplots()
			ax.plot(seconds_since_epoch_col, daily_xp_col, "b-", linewidth=1)
			ax.set_xlabel("Date")
			ax.set_ylabel("Experience")
			ax.set_title("Daily Experience")
			ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
			ax.set_xlim(xmin, xmax)
			fig.tight_layout()
			fig.savefig(daily_xp_path, dpi=plot_dpi)

			logger.log_info(f"Successfully exported plot `daily_xp` for " \
				f"language `{lang}`")

			successful += 1
		else:
			logger.log_error(f"Failed to export plot `daily_xp` for " \
				f"language `{lang}`: missing column `daily_xp`!")

			failed += 1

		# Plot total xp and save to file.
		if "total_xp" in df.columns:
			# Get data.
			total_xp_col = df["total_xp"]

			# Create and export plot.
			fig, ax = plt.subplots()
			ax.plot(seconds_since_epoch_col, total_xp_col, "b-", linewidth=1)
			ax.set_xlabel("Date")
			ax.set_ylabel("Experience")
			ax.set_title("Total Experience")
			ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
			ax.set_xlim(xmin, xmax)
			fig.tight_layout()
			fig.savefig(total_xp_path, dpi=plot_dpi)

			logger.log_info(f"Successfully exported plot `total_xp` for " \
				f"language `{lang}`")

			successful += 1
		else:
			logger.log_error(f"Failed to export plot `total_xp` for " \
				f"language `{lang}`: missing column `total_xp`!")

			failed += 1

		# Plot total words learned and save to file.
		if "total_words_learned" in df.columns:
			# Get data.
			total_words_learned_col = df["total_words_learned"]

			# Create and export plot.
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

			logger.log_info(f"Successfully exported plot " \
				f"`total_words_learned` for language `{lang}`")

			successful += 1
		else:
			logger.log_error(f"Failed to export plot " \
				f"`total_words_learned` for language `{lang}`: missing " \
				"column `total_words_learned`!")

			failed += 1

		# Plot level and save to file.
		if "level" in df.columns:
			# Get data.
			level_col = df["level"]

			# Create and export plot.
			fig, ax = plt.subplots()
			ax.plot(seconds_since_epoch_col, level_col, "b-", linewidth=1)
			ax.set_xlabel("Date")
			ax.set_ylabel("Level")
			ax.set_title("Level")
			ax.set_xticks(xticks, xlabels, rotation=xticks_rotation)
			ax.set_xlim(xmin, xmax)
			fig.tight_layout()
			fig.savefig(level_path, dpi=plot_dpi)

			logger.log_info(f"Successfully exported plot `level` for " \
				f"language `{lang}`")

			successful += 1
		else:
			logger.log_error(f"Failed to export plot `level` for " \
				f"language `{lang}`: missing column `level`!")

			failed += 1

	# Close all figures, if this is not done memory will stay allocated and
	# wxpython will not be able to exit the mainloop. Also if this is not done
	# matplotlib will keep the figures in memory and throw a warning once the
	# number of figures in memory exceeds 20.
	plt.close("all")

	# Create end log message.
	logger.log_info(f"Done exporting plots ({successful} successful, " \
		f"{failed} failed)")