import gdb
import sys
srt = input()
gdb.execute('file ' + srt)
gdb.execute('b printf()')
gdb.execute('echo -1; python -c 'print 'a' * 256'; cat | ')
gdb.execute('generate-core-file')
