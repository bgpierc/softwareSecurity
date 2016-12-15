import gdb
import sys
#str = input()
gdb.execute('file no_overflow')
gdb.execute('core-file core')
#gdb.execute('b greet') #should prolly not hardcode this need to integrate with jack and boot
#gdb.execute('r')
gdb.execute('info frame')
gdb.execute('quit')
#gdb.execute('y')
