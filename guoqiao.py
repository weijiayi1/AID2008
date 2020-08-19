# 让最快的人多跑几次
# 3+1 6+1 8+1 12 = 32s
# 让慢的一起走
# 3+1 12+3 6+1 3 = 29s
# 1.小明和弟弟先走 小明回来
# 2.妈妈和爷爷走 弟弟回来
# 3.小明和爸爸走 小明回来
# 4.小明和弟弟走
import random

while True:
    # a岸
    a = [1, 3, 6, 8, 12]
    # b岸
    b = []
    # 速度
    SPEED = 0
    # 流程
    step = []

    while True:
        # 随机获取两个a中的元素
        x = random.sample(a, 2)
        # 将元素放入b中
        b.extend(x)
        # 从a中删除元素
        a.remove(x[0])
        a.remove(x[1])
        step.append(x)  # 将随机组合添加到列表
        step.append(max(x))  # 将随机组合的过河时间也添加到列表
        if not a:
            break

        # 从b中随机找一个到a
        y = random.sample(b, 1)
        a.extend(y)
        b.remove(y[0])
        step.append(y[0])  # 记录 返回的时间
        step.append('||')

    # print(step)
    for i in step:
        if type(i) == int:
            SPEED += i
    if SPEED <= 30:
        break
print(step)
print(SPEED)
