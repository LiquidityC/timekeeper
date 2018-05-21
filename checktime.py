#!/usr/bin/env python

from pathlib import Path
from datetime import date
import sys
import os
import tklib

modifier = 15
if len(sys.argv) > 1:
    modifier = int(sys.argv[1])

## Here is where we run
tklib.ensureDir()
value = 0
if os.path.exists(tklib.getTimefileName()):
    tfile = open(tklib.getTimefileName(), "r")
    value = int(tfile.read())
    tfile.close()

tfile = open(tklib.getTimefileName(), "w")
value += modifier
tfile.write(str(value))
tfile.close()
