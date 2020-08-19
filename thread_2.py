"""
线程示例2
"""
from time import sleep
from threading import *

#含有
def fun(sec,name):
    print('含有参数的线程函数')
    sleep(sec)
    print(name,'执行完毕')

jobs=[]
for i in range(5):
    t=Thread(target=fun,args='')
