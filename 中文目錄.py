# encodeing=utf-8

import os
import sys
print os.getcwd().decode('ms950')
os.rmdir('foo')
os.mkdir('foo')
os.chdir('foo')
print os.getcwd().decode('ms950')
