#!/usr/bin/env python

from datetime import date
from datetime import datetime
from getopt import gnu_getopt as getopt
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

##
## START OF PROG
##

if (len(sys.argv) > 1):
    week = int(sys.argv[1])
else:
    week = date.today().isocalendar()[1]

noRound = False

optlist, args = getopt(sys.argv[1:], "w:", ["week=", "no-round"])
for opt in optlist:
    flag = opt[0]
    if flag == "--week":
        week = int(opt[1])
    elif flag == "-w":
        week = int(opt[1])
    elif flag == "--no-round":
        noRound = True

timefiles = collectFiles(week)
timefiles.sort()

output = "WEEK: %d\n" % week
for tfname in timefiles:
    tfile = open(tfname, "r")
    total_mins = int(tfile.read())
    date = datetime.strptime(os.path.basename(tfname), "%W-%Y-%m-%d.dat")
    if not noRound and str(total_mins).endswith("5"):
        total_mins += 15
    hours = float(total_mins / 60)
    output += "%s:\t%.1f\n" % (date.strftime("%A (%d %b)"), hours)
    tfile.close()

pyperclip.copy(output)
print(output)
print("--- Result copied to clipboard ---")
