"""
把一个大文件一分为二
"""
from multiprocessing import Process
import os
fname=str(input('请输入文件名:'))
# 文件上半部分
def sopen(name):
    a = os.path.getsize(name)
    sname = open(name, 'rb')
    c=a//2
    b=sname.read(c)
    xname = open(name[0:-3]+'前.'+name[-3:len(name)], 'wb')
    xname.write(b)
    sname.close()
    xname.close()

# 文件下半部分
def xopen(name):
    a = os.path.getsize(name)
    bname = open(name, 'rb')
    d=a//2
    bname.seek(d,0)
    b = bname.readline()
    xxname = open(name[0:-3]+'后.'+name[-3:len(name)], 'wb')
    xxname.write(b)
    bname.close()
    xxname.close()

#创建进程
jobs=[]
for i in [sopen,xopen]:
    p=Process(target=i,kwargs={'name':fname})
    jobs.append(p)
    p.start()
for s in jobs:
    s.join()