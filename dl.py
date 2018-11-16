#!/usr/bin/env python

import os
import sys
import time

print("Removeing: r.sh, r.py...")
os.system('rm -rf r.sh && rm -rf s.py')
print("Getting PKG's...")
os.system('python3 gflfs.py')
print("Getting MD5 Hash Key...")
os.system('./gmd5hk.py')
print("Running: lib-check.sh and then version-check.sh...")
os.system('./wget.py')
os.system('bash lib-check.sh')
print("If files = 'not found' all good if files = 'All found' all good but, if all file = 'found this but not this install files. Look up on INET...")
arefilesgood = raw_input('All good? (Y/n): ')
if arefilesgood == 'n':
	print("Look at the internet, please.")
	os.system('exit')
if arefilesgood == 'Y':
	os.system('clear')
	os.system('bash version-check.sh')
	filesaregoodtwo = raw_input('Are all good? (N/y): ')
	if filesaregoodtwo == 'y':
		print('done for now...')
	if filesaregoodtwo == 'N':
		print("Get them' PKG's and run dl.py again.")
