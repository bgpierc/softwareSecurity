import gdb
import sys
str = input()
gdb.execute('file ' + str)
gdb.execute('b greet') #should prolly not hardcode this need to integrate with jack and boot
gdb.execute('r')
gdb.execute('info frame')
gdb.execute('quit')
gdb.execute('y')
