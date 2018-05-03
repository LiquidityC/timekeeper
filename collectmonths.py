#!/usr/bin/env python

from datetime import date
from datetime import datetime
import calendar
import os
import sys
import tklib

def collectFiles(year, month):
    timefiles = []
    for root, dirs, files in os.walk(tklib.getDataDir()):
        for name in files:
            substring = "-%d-%02d-" % (year, month)
            if substring not in name:
                continue;
            timefiles.append(os.path.join(root, name))
    return timefiles

year = date.today().year
if len(sys.argv) > 1:
    year = int(sys.argv[1])

for month in range(1,12):
    total = 0
    timefiles = collectFiles(year, month)
    for tfname in timefiles:
        tfile = open(tfname, "r")
        total += int(tfile.read())
        tfile.close()

    if total == 0:
        continue

    if str(total).endswith("5"):
        total += 15

    total_hours = float(total / 60)
    print("%d/%02d (%s)\t: %.1f hours" % (year, month, calendar.month_name[month], total_hours))
