import config as conf
import toimport as ti

ti.vals.offset = 0
conf.calcArgs()
print(conf.args[1])
print()
ti.vals.offset = 6
conf.calcArgs()
print(conf.args[1])
