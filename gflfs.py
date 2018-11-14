#!/bin/usr/env python

import time
import system
import os

print("Getting 2 files, 'version-check.sh', 'lib-check.sh'...")
time.sleep(5)
os.system('clear')
#version-check.sh
file = open("version-check.sh","w")
file.write("#!/bin/bash")
file.write("export LC_ALL=C")
file.write("bash --version | head -n1 | cut -d" " -f2-4")
file.write("echo "/bin/sh -> `readlink -f /bin/sh`"")
file.write("echo -n "Binutils: "; ld --version | head -n1 | cut -d" " 
-f3-")
file.write("bison --version | head -n1")
file.write("if [ -e /usr/bin/yacc ];")
file.write("	then echo "/usr/bin/yacc -> `readlink -f 
/usr/bin/yacc`")

