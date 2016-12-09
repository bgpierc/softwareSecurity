import array
from enum import Enum
import os
import config as conf
arg = []
arg = conf.args
if conf.input_type == 1 :
	os.system("./a.out " + str(arg[0]) + ' ' + str(arg[1]))
if conf.input_type == 2 :
	os.system("echo " + str(arg[0]) + "; echo " + str(arg[1]) + " | ./a.out")
