# Plan

### Description
The goal of this project is to have a GUI in which duolingo data can be visualized.

### Milestones
1. Generate plots.
	1. Load data using `pandas`.
	2. <strike>Transform data into a usable structure.</strike> Add `seconds_since_epoch` column to all dataframes, denoting the time in seconds since Januari 1st 2010.
	3. Create necessary plots using `matplotlib` and save them to `plots` folder.
		1. Total xp
		2. Daily xp
		3. Total words learned
		4. Level
2. Create interface.
	1. Decide on global layout and create image out of it.
	2. Implement global layout in `wxPython`.
	3. Implement the components of the interface.
3. Additional functionality.
	1. Add plots with data from all languages combined.

### Log
### 09-02-2022
*13:16*: Start development.<br />
*13:32*: Started implementing function `src/generate_plots.py:export_plots(lang_dict, username)`. It automatically creates the folder `figures/{username}` if it does not exist.<br />
*13:34*: Stop development.<br /><br />

*13:59*: Start development.<br />
*14:33*: Further implemented function `src/generate_plots.py:export_plots(lang_dict, username)`. It now also creates a folder for each language in `figures/{username}/` if it does not exist. It also extracts the necessary columns and plots the `daily_xp` column with the `seconds_from_epoch` column on the x-axis. It also saves the generated plot to the respective language folders, although these plots contain an extra line at y=0 which is still a bug.<br />
*14:42*: Stop development.<br /><br />

*20:45*: Start development.<br />
*21:20*: Fixed the bug with the extra line at y=0. There was a mistake in the data where the entry after 31-12-2021 had the date 01-01-2021 attached, consistently across the entire dataset.<br />
*21:30*: Plots for all the required columns now get saved to the correct location. The only thing left to do this milestone is adding custom ticks for the x-axis.<br />
*21:48*: Implemented custom ticks for the x-axis, limits for the x-axis and applied a tight layout to all plots.<br />
*21:50*: Added `milestone 3.1`.<br />

#### 08-02-2021
*13:07*: Start development.<br />
*13:07*: Create `PLAN.md` and add `Description` and `Milestones` chapters.<br />
*13:09*: Commit changes to `main` branch.<br />
*13:30*: Done researching how to branch and merge in git: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging.<br />
*13:31*: Create branch `generate-plots`.<br />
*13:33*: Create directories `src` and `data`.<br />
*13:34*: Create directory `data/Rubenanz` for storing data about the respective account.<br />
*13:36*: Added files `data/Rubenanz/korean.csv`, `data/Rubenanz/norwegian.csv`, `data/Rubenanz/spanish.csv` and `data/Rubenanz/swedish.csv` from Backup hard drive from previous computer.<br />
*14:09*: Updated previously added data files with statistics from 15-12-2021 until 07-02-2022 using script.<br />
*14:11*: Add `src/application.py`.<br />
*14:13*: Create virtual environment.<br />
*14:15*: Add `data` folder to `.gitignore`.<br />
*14:16*: Add `src/load_data.py`.<br />
*14:18*: Install libraries `pandas` and `matplotlib` and their dependencies.<br />
*14:19*: Rename `src/load_data.py` to `src/generate_plots.py`.<br />
*14:36*: Implemented function `src/generate_plots.py:load_data(username)` which loads only the CSV files in the specified `username` folder and returns a dictionary containing dataframes generated from these files. Raises an exception if the folder `username` does not exists. This implementation satisfies `milestone 1.1`.<br />
*14:42*: Commit changes to branch `generate-plots`.<br />
*14:42*: Stop development.<br /><br />

*15:31*: Start development.<br />
*15:36*: Removed `milestone 1.2` and replaced it with the new, not struck through, milestone.<br />
*16:13*: Implemented function `src/generate_plots.py:add_time_column(lang_dict)` which adds an extra column to all dataframes named `seconds_since_epoch`, which contains the amount of seconds passed since Januari 1st 2010. This implementation satisfies `milestone 1.2`.<br />
*16:22*: Commit changes to branch `generate-plots`.<br />
*16:27*: Added substeps to `milestone 1.3` containing the four plots to generate per language.<br/>
*16:28*: Stop development.<br/><br/>