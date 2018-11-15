#!/bin/usr/env python
# -*- codeing: UTF-8 -*-

import time
import sys
import os

print('''
 ____ ___      .__                 __         .__  .__                                .____   __________________________________________
|    |   \____ |__| ____   _______/  |______  |  | |  |      ______ ___.__.           |    |  \_   _____/   _____/\_   _____/\__    ___/
|    |   /    \|  |/    \ /  ___/\   __\__  \ |  | |  |      \____ <   |  |   ______  |    |   |    __) \_____  \  |    __)_   |    |   
|    |  /   |  \  |   |  \\___ \  |  |  / __ \|  |_|  |__    |  |_> >___  |  /_____/  |    |___|     \  /        \ |        \  |    |   
|______/|___|  /__|___|  /____  > |__| (____  /____/____/ /\ |   __// ____|           |_______ \___  / /_______  //_______  /  |____|   
             \/        \/     \/            \/            \/ |__|   \/                        \/   \/          \/         \/            
''')

ch = raw_input('Do you REALLY want to uninstall LFSET? (N/y): ')
if ch == 'N':
	print("Have a good day!")
elif ch == 'y':
	print('sorry you didnt like it :( BUT, HAVE A GOOD DAY :))))')
	time.sleep(5)
	os.system('clear')
	os.system('rmdir -rf etc')
	os.system('rmdir -rf files')
	os.system('rmdir -rf tools')
	os.system('rmdir -rf .git')
	os.system('rm -rf LICENSE.md')
	print('All files uninstalled, after 10sec this file will be del...')
	time.sleep(10)
	os.system('sudo rm -rf uninstall.py')
