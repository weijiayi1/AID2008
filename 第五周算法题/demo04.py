"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。
"""


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    numList = [n]  # 存放所有计算出来的数，用于判断是否存在环
    while n != 1:  # 如该计算结果为1，说明该数是快乐的数
        sum = 0
        for i in str(n):
            sum += int(i) ** 2
        if sum not in numList:  # 判断是否存在环
            numList.append(sum)
        else:  # 存在环就说明该数不是快乐的数
            return False
        n = sum
    print(numList)
    return True


if __name__ == '__main__':
    print(isHappy(19))
