# encodeing=utf-8

import os
import sys
print os.getcwd()
os.rmdir('foo')
os.mkdir('foo')
os.chdir('foo')
print os.getcwd()
for item in sys.argv:
    print item

print sys.executable