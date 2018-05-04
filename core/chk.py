# Tool Name :- Tool Kit
# Author :- Rajkumar Dusad
# Date :- 24/11/2017
# Powered By :- Aex Software's

import os
import sys
from time import sleep

def chk():
	if os.path.exists(".Chk.aex"):
		Ox()
	else:
		os.system("python2 .Dl.aex")
		os.system("cd .. && cd .. && rm -rf .Tool-Kit")
		os.system("cd && rm -rf .Tool")
		os.system("cd /data/data/com.termux/files/usr/bin && rm -rf Tool-Kit")

def ch():
	try:
		chk()

	except KeyboardInterrupt:
	ex()
ch()
