# encodeing=utf-8

import os
import sys
print os.getcwd()
os.rmdir('foo')
os.mkdir('foo')
os.chdir('foo')
print os.getcwd()
# 印出本身的檔案，然後取得後面加入的所有參數
# 第0個參數是檔案本身
# 命令列的參數從第一個開始

# D:\PycharmProjects\py2_0829>python 目錄與檔案.py -a -b -c a=b
# D:\PycharmProjects\py2_0829
# D:\PycharmProjects\py2_0829\foo
# 目錄與檔案.py
# -a
# -b
# -c
# a=b
# D:\Python27\python.exe

for item in sys.argv:
    print item

print sys.executable