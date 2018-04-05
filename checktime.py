#!/usr/bin/env python

from pathlib import Path
from datetime import date
import os
import tklib

## Here is where we run
tklib.ensureDir()
value = 0
if os.path.exists(tklib.getTimefileName()):
    tfile = open(tklib.getTimefileName(), "r")
    value = int(tfile.read())
    tfile.close()

tfile = open(tklib.getTimefileName(), "w")
value += 15
tfile.write(str(value))
tfile.close()
