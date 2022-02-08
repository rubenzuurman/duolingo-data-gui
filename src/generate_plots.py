import errno
import os

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