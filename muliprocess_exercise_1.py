"""
求100000以内质数之和分别用单个进程和多个进程
"""
from multiprocessing import Process
from time import *

for i in range(2, 100001):
    for x in range(2, i):
        if i % x == 0:
            pass
