#!/bin/sh/
touch output
echo "executable: "
gdb -q -x $1  > output #arg1 = pythonscript.py
