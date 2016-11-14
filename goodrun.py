import array
from enum import Enum
import os
import config as conf
arg = []
x = 2
conf.input_type = 1
for i in range(x):
	arg.append(i)
if conf.input_type == 1 :
	os.system("./a.out " + str(arg[0]) + ' ' + str(arg[1]))
if conf.input_type == 2 :
	os.system("./a.out")
	os.system(arg[0])
	os.system(arg[1])
