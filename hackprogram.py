import config as conf
import toimport as ti

print(conf.args[1])
ti.vals.offset = 6
conf.calcArgs()
print(conf.args[1])
