# Tool Name :- Tool Kit
# Author :- Rajkumar Dusad
# Date :- 24/11/2017
# Powered By :- Aex Software's

import os
import sys
from time import sleep
from core.er import err
from core.ux import Ux

def Noti():
	print ('''\n\n\n\n\033[1;32m
        _____           _   _  _  _  /|
       |_   _|__   ___ | | | |/ /(_)| |_
         | |/ _ \ / _ \| | | ' / | || __|
         | | (_) | (_) | | | . \ | || |_
         |_|\___/ \___/|_| |_|\_\|_|\___|
\033[1;m

\033[1;33m ===============================================\033[1;m
\033[1;33m|\033[1;m              \033[1;32m Hacker's Tool-Kit.\033[1;m              \033[1;33m|\033[1;m
\033[1;33m ===============================================\033[1;m

\033[1;33m  [+] \033[1;32mWe can't do anything for you.\033[1;m
\033[1;33m  [+] \033[1;32mBeacuse Tool-Kit is not installed.
\033[1;33m  [+] \033[1;32mSo please install Tool-Kit.
\033[1;33m  [+] \033[1;32mif you can't install Tool-Kit.
\033[1;33m  [+] \033[1;32mso we have nothing for you.....L\033[1;m
\033[1;33m_________________________________________________\033[1;m
\033[1;33m=================================================\033[1;m''')

def ins():
 Ux()
 while True:
		while os.path.exists("/data/data/com.termux/files/usr/lib/.Tool-Kit"):
			print("checking.....")

		else:
			Noti()
			Toolo = raw_input("\033[1;32m Press Y to continue. [Y/n] >>> \033[1;m")
			if Toolo == "Y":
				os.system("cd .. && sh Install")
				os.system("cd && Tool-Kit")
				sys.exit()
			elif Toolo == "y":
				os.system("cd .. && sh Install")
				os.system("cd && Tool-Kit")
				sys.exit()
			elif Toolo == "N":
				sys.exit()
			elif Toolo == "n":
				sys.exit()
			else:
				err()
				sleep(1)
				ins()
