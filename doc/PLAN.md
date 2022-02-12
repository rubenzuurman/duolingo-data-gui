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
	3. Implement the components of the interface (front-end).
	4. Implement the components of the interface (back-end).
		1. When a dropdown entry is changed, reload the image.
		2. When the window is resized, scale the image, respecting its aspect ratio.
		3. When the `Regenerate plots` button is clicked, regenerate the plots.
3. Additional functionality.
	1. Add plots with data from all languages combined.
	2. Implement loading screen for when generating plots.
	3. Abstract text into separate language file in order to support multiple languages.
	4. Implement logger class for debugging purposes.

### Log
### 12-02-2022
*13:09*: Start development.<br />
*13:49*: The dropdown menus and the `Regenerate plots` button now trigger an event which calls a function. Started development on loading the plots into a dictionary.<br />
*13:55*: Stop development.<br /><br />

*14:20*: Start development.<br />
*15:19*: Language select and plot select now have separate event functions. The language event function updates the plot selection choice to the available plots for that language, and resets the selection if the previously selected plot is not available for the selected language.<br />
*15:22*: Added `milestone 3.4`.<br />
*15:35*: The correct plot images are now shown corresponding to the selection made in the dropdown menus.<br />

### 11-02-2022
*13:30*: Start development.<br />
*13:33*: Added restriction `(front-end)` to `milestone 2.3`.<br />
*13:33*: Added `milestone 2.4`.<br />
*14:29*: Replaced the `wx.GridSizer` for user input with a `wx.GridBagSizer` because of [this stackoverflow post](https://stackoverflow.com/questions/35071802/how-can-i-make-a-wxpython-widget-span-two-cells-without-pushing-other-widgets-as), which is way easier to work with. The the labels in the gridsizer are more or less centered (the flag has been set and after a lot of tweaking I decided it is not *that* important). The `Regenerate plots` button spans two columns now.<br />
*14:32*: Stop development.<br /><br />

*15:29*: Start development.<br />
*15:33*: The title text sizer is now fixed size, which means only the plot will change size as the window changes size.<br />
*15:58*: The plot sizer now contains the dummy image `doc/images/loading_screen_layout_v1.png`. It does not yet resize with the window, this is part of back-end development.<br />
*16:01*: Changed window title and title text to `Duolingo Data Visualizer`. Window title was `Hello world` and the title text was `Duolingo Statistics Viewer`.<br />
*16:04*: Updated `doc/requirements.txt`.<br />
*16:10*: Commit changes to branch `gui-development`.<br />
*16:21*: Added three submilestones to `milestone 2.4`, outlining the steps to be taken.<br />
*16:21*: Stop development.

### 10-02-2022
*10:51*: Start development.<br />
*11:05*: Created layout images for the loading screen and the main window. These are saved as `doc/images/loading_screen_layout_v1.png` and `doc/images/main_window_layout_v1.png` respectively.<br />
*11:08*: Created branch `gui-development`.<br />
*11:35*: It took about 25 minutes to install the `wxPython` library correctly. The issue was that python 3.10 was not yet supported by `wxPython` 4.1.1. Following this [issue](https://github.com/wxWidgets/Phoenix/issues/2089) I installed `wxPython` version `4.1.2a1.dev5304+7c8318e8`, which works as expected when creating a basic window.<br />
*11:42*: Commit changes made to the `doc/images/` folder to branch `gui-development`.<br />
*11:42*: Stop development.<br /><br />

*13:08*: Start development.<br />
*13:44*: Added a panel, added a title sizer and a content sizer to the panel. Added text to the title sizer.<br />
*13:59*: Added buttons to relevant sizers to see the size of the sizers when the buttons are expanded to full sizer.<br />
*14:01*: Stop development.<br /><br />

*15:17*: Start development.<br />
*15:23*: The buttons are in place and working and ready to be replaced by actual components. This satisfies milestone 2.2.<br />
*15:25*: Commit changes to branch `gui-development`.<br />
*15:27*: Added `milestone 3.2`.<br />
*15:45*: Added `milestone 3.3`.<br />
*16:38*: Computer crashed, lost no progress.<br />
*17:12*: Still confused as to why it crashed. The last thing I did was take a screenshot with lightshot, but maybe it was just correlation.<br />
*17:15*: At this point the window has a title up top, below that it has a fixed size grid containing 2 labels on the left and 2 dropdowns on the right, and to the right of that it still has a big button representing the space reserved for plots.<br />
*17:23*: The things to do next are: center the labels vertically in the user input gridsizer, add a button to the gridsizer spanning two columns.<br />
*17:24*: Stop development.

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
*21.55*: Added `figures` folder to `.gitignore`.<br />
*21:59*: Commit changes to branch `generate-plots`.<br />
*22:03*: Merge branch `generate-plots` into `main`.<br />
*22:04*: Push to origin main (`git push origin main`) to update network graph of the github repository.<br />
*22:07*: Create file `doc/requirements.txt` from the command `pip freeze > doc/requirements.txt`. This file lists all necessary libraries.<br />
*22:09*: Delete branch `generate-plots` by running the command `git branch -d generate-plots`, as this branch is not needed anymore.<br />
*22:10*: Stop development.

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
*16:28*: Stop development.