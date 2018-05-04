# Tool Name :- Tool Kit
# Author :- Rajkumar Dusad
# Date :- 28/4/2018
# Powered By :- Aex Software's

import os

def rload():
	if os.path.exists("/usr/lib/sudo"):
		os.system("sudo rm -rf core/loaded")
	else:
		os.system("rm -rf core/loaded")