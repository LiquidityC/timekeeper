# A tool to track time
I use this to keep track of how long my workstation has been running during the day.
It updates time in 15 minute increments every time the script is run.

### checktime.py
It's intended that you put this in a cron script or some other form of scheduler and make it run every 15 minutes while the computer is on.

### collecttime.py
Run this to gather all the time information stored from a given week or the current week.
The data is copied to clipboard for easy pasting into a spreadsheet for example.

### Config
You can only config one thing and that is the dir where the data files are stored under $HOME.
Just modify the TIMEKEEPER_DIR variable in tklib.py to change this. The rest should work out of the box.

### Deps
You need to install the pyperclip library [https://github.com/asweigart/pyperclip](https://github.com/asweigart/pyperclip)
I think it exists in the package managers for most linux distributions.
