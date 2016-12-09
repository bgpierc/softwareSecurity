import os
import sys

input1=sys.argv[1]
print1= "	print'" + input1 + "'"

def python_write():
	f=open('newpython.py','w')
	f.write('import os\n')
	f.write('def test():\n')
	f.write(print1)
	f.write('\n')
	f.write('test()')
	f.close()

python_write()

