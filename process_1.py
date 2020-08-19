"""
进程创建示例1
"""
import multiprocessing
import time
#进程行函数
def fun():
    print('开始')
    time.sleep(2)
    print('结束')
#实列化进程对象
p=multiprocessing.Process(target=fun)
#启动进程:此时进程诞生,自动行fun函数作为进程行内容
p.start()

#让它与子进程同时执行
print('我也想做点事')
time.sleep(3)
print('我也做完了')
#等待进程结束,回收进程
p.join()