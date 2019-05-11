#!/usr/bin/env python

from datetime import date
from datetime import datetime
from datetime import timedelta
from getopt import gnu_getopt as getopt
import os
import sys
import pyperclip
import tklib

def collectFiles(week):
    year = date.today().year
    cursorDate = datetime.strptime("%d-%d-1" % (year, week-1), "%Y-%W-%w")
    timefiles = []
    for i in range(0, 7):
        weekday = cursorDate + timedelta(days=i)
        fname = weekday.strftime("%W-%Y-%m-%d.dat")
        timefiles.append(os.path.join(tklib.getDataDir(), fname))

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
    date = datetime.strptime(os.path.basename(tfname), "%W-%Y-%m-%d.dat")

    # Didn't work this day I guess...
    if not os.path.exists(tfname):
        output += "%s:\t0\n" % date.strftime("%A (%d %b)")
        continue

    tfile = open(tfname, "r")
    total_mins = int(tfile.read())

    # Round up the time
    if not noRound and str(total_mins).endswith("5"):
        total_mins += 15

    hours = float(total_mins / 60)
    output += "%s:\t%.1f\n" % (date.strftime("%A (%d %b)"), hours)
    tfile.close()

pyperclip.copy(output)
print(output)
print("--- Result copied to clipboard ---")
