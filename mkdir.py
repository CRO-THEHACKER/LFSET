#!/usr/bin/env python

import time
import os
import sys

print("Makeing: /etc/")
os.mkdir('etc')
time.sleep(2)
print("Makeing: /files/")
os.mkdir('files')
time.sleep(2)
print("Makeing: /tools/")
os.mkdir('tools')
time.sleep(2)
print("Makeing: /etc/tools/")
os.system('cd etc/')
os.mkdir('tools')
time.sleep(2)
print("Makeing: /etc/sys/")
os.mkdir('sys')
os.system('cd ..')
print("Makeing: /etc/temp/installfiles/")
os.mkdir('temp')
os.mkdir('installfiles')
time.sleep(2)
print("Making files now!")
time.sleep(3)
os.system('clear')
os.system('python3 movfiles.py')
