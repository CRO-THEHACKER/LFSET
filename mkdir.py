#!/usr/bin/env python

import time
import os
import system

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
print("Making files now!")
time.sleep(3)
os.system('clear')
os.system('python mkfiles.py')
