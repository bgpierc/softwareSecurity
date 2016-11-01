import gdb
import sys
str = input('Filename (with extension) of your binary: ')
gdb.execute('file ' + str)
gdb.execute("b main")
gdb.execute("r")
