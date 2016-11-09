#!/bin/sh/
touch output
gdb -q -x $1 > output #arg1 = pythonscript.py
