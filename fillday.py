#!/usr/bin/env python

import tklib

tklib.ensureDir()
tfile = open(tklib.getTimefileName(0), 'w')
value = 8 * 60
tfile.write(str(value))
tfile.close()
