"""
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1

描述前一项，这个数是 1 即 “一个 1 ”，记作 11

描述前一项，这个数是 11 即 “两个 1 ” ，记作 21

描述前一项，这个数是 21 即 “一个 2 一个 1 ” ，记作 1211

描述前一项，这个数是 1211 即 “一个 1 一个 2 两个 1 ” ，记作 111221

"""
def count_num(n):
    i = 1
    a = None
    while i <= n:
        # 循环生成数字字符串
        if i == 1:
            a = "1"
        else:
            a = create_num(str(a))
        # print(a)
        i += 1
    return "第%d个数是%s"%(i-1,a)


def create_num(n):
    # 利用列表生成数字字符串
    res = []
    count = 0
    for i in range(len(n)):
        # count记录当前字符出现的次数，如果当前的字符与上一个字符相同，那么count加1
        if i > 0 and n[i] == n[i - 1]:
            count += 1
            a = str(count) + n[i]
            res[-1] = a
        else:
            count = 1
            a = str(count) + n[i]
            res.append(a)
    return "".join(res)

if __name__ == '__main__':
    result = count_num(5)
    print(result)
