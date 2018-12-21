#!/usr/bin/env python

from pathlib import Path
from datetime import date, timedelta
import os

TIMEKEEPER_DIR = ".timekeeper"

def getDataDir():
    return os.path.join(str(Path.home()), TIMEKEEPER_DIR)

def ensureDir():
    if not os.path.exists(getDataDir()):
        os.mkdir(getDataDir());

def getDateString(dayOffset):
    d = date.today() + timedelta(days=dayOffset)
    return d.strftime("%W-%Y-%m-%d")

def getTimefileName(dayOffset):
    return getDataDir() + "/" + getDateString(dayOffset) + ".dat"
