import array
from enum import Enum
import os
import config as conf
import toimport as imp
def execute():
	print("Started Noah's shit")
	arg = []
	arg = conf.args
	if conf.input_type == imp.Input.commandline :
		os.system("./ "+ conf.programname + " " + str(arg[0]) + ' ' + str(arg[1]))
	if conf.input_type == imp.Input.args :
		os.system("echo " + str(arg[0]) + "; echo " + str(arg[1]) + "; cat | ./" + conf.programname)
	os.system("groups")
	print("Completed Noah's shit")
