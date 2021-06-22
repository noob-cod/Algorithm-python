"""
@Date: Saturday, March 27, 2021
@Author: Chen Zhang
@Brief: 欧几里得算法（辗转相除法） - 计算两个正整数的最大公约数

算法概述：
    两个正整数的最大公约数等于其中较小的那个数和两个数相除余数的最大公约数。
    gcd(a, b) = gcd(b, a%b) （递归）
"""


def gcd(a, b):
    # 保证输入的a,b都是正整数
    assert isinstance(a, int) and isinstance(b, int),\
        print('输入的%s与%s中存在非整数数！' % (str(a), str(b)))
    # 递归结束条件
    if a % b == 0:
        return b
    # 需要接收递归结束后回溯的结果，否则当回溯到最顶层时无法获得可输出的结果
    c = gcd(b, a % b)
    return c


if __name__ == '__main__':
    a, b = 50, 20
    print('%d与%d的最大公约数为：' % (a, b), gcd(a, b))
