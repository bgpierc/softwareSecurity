from enum import Enum
class Input(Enum):
    commandline = 1
    args = 2
class ToImp:
    def __init__(self):
        self.NOP = "\\x90" #replace with 1 slash after debugging
        self.offset = 0 #will be overidden by program to try different offsets
        self.shellcode = "gimme those privledges" #put actuall shellcode here

vals = ToImp()
