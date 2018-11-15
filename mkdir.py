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
os.mkdir('etc/tools/')
time.sleep(2)
print("Makeing: /etc/sys/")
os.mkdir('etc/sys/')
print("Makeing: /etc/temp/installfiles/")
os.mkdir('etc/temp/')
os.mkdir('etc/temp/installfiles/')
time.sleep(2)
print("Files done..."
time.sleep(3)
os.system('clear')
os.system('python3 movfiles.py')
