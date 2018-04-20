#!/usr/bin/env python

from datetime import date
from datetime import datetime
import os
import sys
import pyperclip
import tklib

def collectFiles(week):
    timefiles = []
    for root, dirs, files in os.walk(tklib.getDataDir()):
        for name in files:
            if not name.startswith(str(week) + "-"):
                continue;
            timefiles.append(os.path.join(root, name))
    return timefiles

week = date.today().isocalendar()[1]
if len(sys.argv) > 1:
    week = int(sys.argv[1])

timefiles = collectFiles(week)
timefiles.sort()

output = "WEEK: %d\n" % week
for tfname in timefiles:
    tfile = open(tfname, "r")
    total_mins = int(tfile.read())
    date = datetime.strptime(os.path.basename(tfname), "%W-%Y-%m-%d.dat")
    mins = total_mins % 60
    if mins == 15 or mins == 45:
        total_mins += 15
        mins = total_mins % 60
    hours = (total_mins - mins) / 60
    output += "%s:\t%d:%02d\n" % (date.strftime("%A (%d %b)"), hours, mins)
    tfile.close()

pyperclip.copy(output)
print(output)
print("--- Result copied to clipboard ---")
