#!/usr/bin/env python

import sys
import os
import time
import subprocess

dir = os.getcwd()

print('''
''')
print("Moveing: dl.py, gflfs.py, gmd5hk.py to: /lfset/files/")
subprocess.call("mv dl.py files", shell=True)
subprocess.call("mv r.sh files", shell=True)
subprocess.call("mv r.py files", shell=True)
subprocess.call("mv gmd5hk.py files", shell=True)
subprocess.call("mv gflfs.py files", shell=True)
print("Moveing: mkdir.py, r.sh, r.py, movdir.py to: /lfset/etc/temp/installfiles")
subprocess.call("mv wgetftp.sh etc/temp/installfiles", shell=True)
subprocess.call("mv lfsinstallinst.py etc/temp/installfiles", shell=True)
subprocess.call("mv mkdir.py etc/temp/installfiles", shell=True)
subprocess.call("mv movdir.py etc/temp/installfiles", shell=True)
subprocess.call("mv uninstall.py etc/temp/installfiles", shell=True)
subprocess.call("mv LICENSE .git/", shell=True)
subprocess.call("mv autoremovedl.py files/", shell=True)
subprocess.call("mv wget.py files/", shell=True)
subprocess.call("mv README.md etc/temp/sys/", shell=True)
subprocess.call("mv sources.csv etc/temp/sys/", shell=True)
print("Done Moveing Dir's!")
os.system('cd .. && cd .. && cd ..')
os.system('cd files/')
os.system('python lfsinstallinst.py')
