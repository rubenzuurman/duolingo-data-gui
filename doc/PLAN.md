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
		3. Integrate user interface into main application.
		4. When the `Regenerate plots` button is clicked, regenerate the plots.
3. Additional functionality.
	1. Add plots with data from all languages combined.
	2. Implement loading screen for when generating and loading plots.
	3. Abstract text into separate language file in order to support multiple languages.
	4. Implement logger class for debugging purposes.
	5. Add settings menu containing settings for plot generation.
		- Line color (for single languages)
		- DPI (comprise of generation speed and resolution)
		- Line thickness
		- Current username
		- More...

### Log
### 15-02-2022
*16:04*: Start development.<br />
*16:50*: Added log messages to `src/application.py`. Added log messages to `src/generate_plots.py` where missing. Refactored `src/generate_plots.py:export_plots()` to be shorter and with less loops setting variables that get checked in if statement where a direct comparison would be shorter and more concise.<br />
*17:24*: If the user folder does not exist, a dialog is shown, the user interface is NOT initiated and the window is closed.<br />
*17:35*: The `User interface stopped` message was previously not shown if the user folder did not exist, due to the fact that the close event was bound after closing the window from the `__init__` function. The close event now gets bound before the check if the user data was ok, the message gets shown as required now.<br />

### 14-02-2022
*11:10*: Start development.<br />
*11:25*: Added `issue 3`, which contains a bug description: when the window is resized be dragging it to the left, right or top edge of the screen, the plot image is not resized correctly.<br />
*11:39*: Implemented logger class into `src/generate_plots.py:load_data()`, removed the `FileNotFoundException` and replaced it with an error message and returning `False` from the function. This value of `False` can then be caught by the calling function.<br />
*11:59*: The calling function in this case was `src/window.py:regenerate_plots()`, this function has been changed to update the `self.user_data_ok` variable by setting it to `not not result`, where `result` is the return value of the `regenerate_plots()` function. It will also not try to add the time column or export the images. The next task is to make the function `src/generate_plots.py:add_time_column()` log error- and info messages when necessary, and to catch the errors in the calling function, which is `regenerate_plots()`.<br />
*12:15*: Implemented logger class into `src/generate_plots.py:add_time_column()`. If a dataframe does not have a `date` column, the `seconds_since_epoch` column does not get added. For now, if the dataframe does not have a `date` column, it will be skipped.<br />
*12:27*: Added `issue 4`, which is a feature request: if the `date` column is missing from a data file for some reason, the `date` column could be generated automatically by assuming the last entry is from today and then counting back in time upwards in the data file. This way the data can be displayed, currently it cannot be displayed.<br />
*12:54*: Implemented logger class into function `src/generate_plots.py:export_plots()`. Language folders no longer get created if the `date` column is missing, this will be reverted once `issue 4` is implemented. Also, a check is added which checks if the requested data columns are presented, if this is not the case, the plot will not be generated. Currently, this involves a lot of if statements, which doesn't look pretty. A resolution would be to create booleans upfront which hold `True` if the plot needs to be generated, and `False` if this is not the case. It would also be good to abstract a function to export the plot, as this code is repeated four times at the moment.<br />
*13:01*: The next task is to check all source files for logger implementation first, and then check for typos and such.<br />
*13:03*: Stop development.

### 13-02-2022
*13:01*: Start development.<br />
*13:01*: Moved `milestone 2.4.3` to `milestone 2.4.4`.<br />
*13:02*: Added `milestone 2.4.3`.<br />
*13:07*: Commit changes to branch `gui-development`.<br />
*13:12*: The user interface is now executed after the plots are generated in `src/application.py`.<br />
*13:50*: Integrated the generation of plots into the wxpython window. There was a bug where the application would not quit when the window was closed. This happened due to the fact that matplotlib does not automatically delete figures from memory. This inhibited the wxpython mainloop from exiting. Adding a `plt.close("all")` call to `src/generate_plots.py:export_plots()` function resolved the issue. The `Regenerate plots` button now also works, although there is no feedback as to what it is doing when this button is clicked. The application just freezes, and unfreezes once it is done.<br />
*14:05*: The `src/window.py:regenerate_plots()` function is now complete and functional, it exports the images and (if the function was not called from the constructor) reloads the images and updates the image on the screen. This implementation satisfies `milestone 2.4`.<br />
*14:12*: Changed some comments and restructured small portions of the code.<br />
*14:14*: Added `and loading` to `milestone 3.2`.<br />
*14:16*: Added `milestone 3.5`.<br />
*14:27*: Committed changes to branch `gui-development`. Merged branch `gui-development` into branch `main`. Tried to `git push origin main` the changes, but it got rejected. Every time you start working on the project you should do a `git pull` to make sure you are up to date with the latest changes of the remote repository. The issue, in this case, was that I set up the `Bug report` and `Feature request` templates on the remote branch.<br />
*14:30*: Stop development.<br /><br />

*20:21*: Start development.<br />
*20:23*: Create branch `logger` for the logger class implementation.<br />
*20:23*: Create file `src/logger.py`.<br />
*21:04*: Implemented basic logger functionalities, which include holding a collecting of all messages submitted, distinction between the INFO, DEBUG and ERROR loglevels, and saving the log messages to a log file.<br />
*21:16*: Added/changed some comments/docstrings in `src/logger.py`.<br />
*21:18*: Commit changes to branch `logger`.<br />
*21:32*: Implemented logger class into `window.py`. The next thing to do is to implement it into `generate_plots.py`.<br />
*21:33*: Stop development.

### 12-02-2022
*13:09*: Start development.<br />
*13:49*: The dropdown menus and the `Regenerate plots` button now trigger an event which calls a function. Started development on loading the plots into a dictionary.<br />
*13:55*: Stop development.<br /><br />

*14:20*: Start development.<br />
*15:19*: Language select and plot select now have separate event functions. The language event function updates the plot selection choice to the available plots for that language, and resets the selection if the previously selected plot is not available for the selected language.<br />
*15:22*: Added `milestone 3.4`.<br />
*15:35*: The correct plot images are now shown corresponding to the selection made in the dropdown menus.<br />
*15:44*: Commit changes to branch `gui-development`.<br />
*15:45*: Stop development.<br /><br />

*17:10*: Start development.<br />
*18:33*: The plot image now resizes correctly when the window is resized. When a new plot or language is selected though, the image aligns left for some reason. After resizing the window it centers again. I have no clue how this happens.<br />
*18:35*: Stop development.<br /><br />

*21:21*: Start development.<br />
*21:23*: Set up bug report and feature request templates for the github repository using the standard templates.<br />
*21:54*: Added `issue 2`, which is a bug where the plot image misaligns if the window was resized vertically last. The bug will be ignored until I feel like fixing it.<br />
*22:09*: Added some comments and docstrings.<br />
*22:09*: Stop development.

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