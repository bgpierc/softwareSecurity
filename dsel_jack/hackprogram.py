import config as conf
import toimport as ti
import re

#accepts string in format "ffffd5b0"
def formatEip(hexstring):
	formatedStr = ""
	for x in range(6, -2, -2):
		formatedStr += (r'\x' + hexstring[x:x+2])
	return bytes(formatedStr, "utf-8").decode("unicode_escape")

def parseEipFromGdb(string):
	matchObj = re.search(r'eip at 0x(.*)$', string)
	match = ""
	if matchObj:
		match = matchObj.group(1)
	return match

print(formatEip(parseEipFromGdb("Stack level 0, frame at 0xffffd6c4:\neip = 0x61616161; saved eip = 0x61616161\ncalled by frame at 0xffffd6c8\nArglist at 0xffffd6bc, args: \nLocals at 0xffffd6bc, Previous frame's sp is 0xffffd6c4\nSaved registers:\neip at 0xffffd6c0")))


#ti.vals.offset = 0
#conf.calcArgs()
#print(conf.args[1])
#print()
#ti.vals.offset = 6
#conf.calcArgs()
#print(conf.args[1])
