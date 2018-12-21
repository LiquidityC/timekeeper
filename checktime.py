#!/usr/bin/env python

from pathlib import Path
from datetime import date
import sys
import os
import tklib

date_modifier = 0
time_modifier = 15
if len(sys.argv) > 1:
    date_modifier = int(sys.argv[1])
if len(sys.argv) > 2:
    time_modifier = int(sys.argv[2])

## Here is where we run
tklib.ensureDir()
value = 0
if os.path.exists(tklib.getTimefileName(date_modifier)):
    tfile = open(tklib.getTimefileName(date_modifier), "r")
    value = int(tfile.read())
    tfile.close()

tfile = open(tklib.getTimefileName(date_modifier), "w")
value += time_modifier
tfile.write(str(value))
tfile.close()
