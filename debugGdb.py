import gdb
import sys
str = input()
gdb.execute('file ' + str)
gdb.execute('b greet')
gdb.execute('r')
gdb.execute('info frame')
gdb.execute('quit')
gdb.execute('y')
