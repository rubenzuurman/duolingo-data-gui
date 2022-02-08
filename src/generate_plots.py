import errno
import os

from datetime import datetime
import pandas as pd

def load_data(username: str):
	"""
	Assumes username is a string. Loads data from all csv files present in
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
	Assumes lang_dict is a dictionary containing dataframes, as returned by
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

	# Return dictionary.
	return lang_dict