#!/usr/bin/env python

import system
import os
import time
import subprocess

sfo = 'dl.py'
dfo = '/files'
sft = 'gflfs.py'
dfo = '/files'
sftr = 'gmd5hk.py'
dftr = '/files'
stsfo = 'r.sh'
stdfo = '/etc/temp/installfiles'
stsft = 'r.py'
stdft = '/etc/temp/installfiles'
stsff = 'mkdir.py'
stdff = '/etc/temp/installfiles'

print("Moveing: dl.py, gflfs.py, gmd5hk.py to: /lfset/files/")
subprocess.call("mv %s %s" % (sfo, dfo), shell=True)
subprocess.call("mv %s %s" % (sft, dft), shell=True)
subprocess.call("mv %s %s" % (sftr, dftr), shell=True)
print("Moveing: mkdir.py, r.sh, r.py, movdir.py to: 
/lfset/etc/temp/installfiles")
subprocess.call("mv %s %a" % (stsfo, stdfo), shell=True)
subprocess.call("mv %s %a" % (stsft, stdft), shell=True)
subprocess.call("mv %s %a" % (ststr, stdrt), shell=True)
subprocess.call("mv %s %a" % (stsff, stdff), shell=True)
print("Done Moveing Dir's!")
