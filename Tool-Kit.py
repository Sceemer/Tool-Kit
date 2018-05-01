# Tool Name :- Tool Kit
# Author :- Rajkumar Dusad
# Date :- 28/4/2018
# Powered By :- Aex Software's

import sys
import os
from core.er import err
from core.exit import Exit
from core.noin import ins
from modules.menu import ToolKit
from core.ux import Ux
from core.ux import ex
from core.load import load

class oschek(object):
    def ch_os(self):
	if "linux" in sys.platform:
           # Running Tool-Kit on linux ...
	   pass
	elif "darwin" in sys.platform:
	   print("Sorry, its not available for windows right now...")
	   ex()
	elif "win" in sys.platform:
	   print("Sorry, its not available for windows right now...")
	   ex()
	else:
	   print("If Tool-Kit not support for \'%s\' right now !!!" %sys.platform)

def Tool_Kit():
  try:
	oschek().ch_os()
	load()
	ToolKit()

  except KeyboardInterrupt:
	Exit()
Tool_Kit()
