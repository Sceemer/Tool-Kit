# Tool Name :- Tool Kit
# Author :- Rajkumar Dusad
# Date :- 29/4/2018
# Powered By :- Aex Software's

import os
import sys
from time import sleep

def Pro1():
	print("\007\033[1;31m")
	sys.stdout.write(open("core/.Er0.aex").read())
	print("\033[1;32m")
	sys.stdout.write(open("core/.Er1.aex").read())
	print("\033[1;31m")
	sys.stdout.write(open("core/.Er2.aex").read())
	print("\007\033[0m")

def Pro2():
	print("\n\007\033[1;31m")
	sys.stdout.write(open("modules/.Er0.aex").read())
	print("\033[1;32m")
	sys.stdout.write(open("modules/.Er1.aex").read())
	print("\033[1;31m")
	sys.stdout.write(open("modules/.Er2.aex").read())
	print("\007\033[0m")

def err():
	if os.path.exists("/data/data/com.termux/files/usr/bin/pkg"):
		Pro1()
	else:
		Pro2()