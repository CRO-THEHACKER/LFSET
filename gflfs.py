#!/bin/usr/env python

import time
import system
import os

print("Getting 2 files, 'version-check.sh', 'lib-check.sh'...")
time.sleep(2)
os.system('wget http://thedarkarmy.000webhostapp.com/Lfset/version-check.sh')
os.system('wget http://thedarkarmy.000webhostapp.com/Lfset/lib-check.sh')
os.system('python3 gmd5hk.py')
