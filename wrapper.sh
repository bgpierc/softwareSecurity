#!/bin/sh/
touch output
echo "executable: " #need to integrate with boot
gdb -q -x $1  > output #arg1 = pythonscript.py
