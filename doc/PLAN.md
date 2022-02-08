# Plan

### Description
The goal of this project is to have a GUI in which duolingo data can be visualized.

### Milestones
1. Generate plots.
	1. Load data using `pandas`.
	2. Transform data into a usable structure.
	3. Create necessary plots using `matplotlib` and save them to `plots` folder.
2. Create interface.
	1. Decide on global layout and create image out of it.
	2. Implement global layout in `wxPython`.
	3. Implement the components of the interface.

### Log
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
*14:36*: Implemented function `src/generate_plots.py:load_data(username)` which loads only the CSV files in the specified `username` folder and returns a dictionary containing dataframes generated from these files. Raises an exception if the folder `username` does not exists.<br />