"""
罗马数字转整数:

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000


示例 1:
    输入: "III"
    输出: 3

示例 2:
    输入: "IV"
    输出: 4
示例 3:
输入: "IX"
    输出: 9
    示例 4:

示例 4：
    输入: "LVIII"
    输出: 58
"""


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    for i in range(len(s) - 1):
        # 如果前一个数字比后一个数字小，则减去前一个数字，否则加上前一个数字
        if convert[s[i]] < convert[s[i + 1]]:
            sum -= convert[s[i]]
        else:
            sum += convert[s[i]]
    # 加上最后一个数字
    sum += convert[s[-1]]
    return sum


if __name__ == '__main__':
    print(romanToInt("VI"))
