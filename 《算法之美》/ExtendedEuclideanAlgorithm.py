"""
@Date: Saturday, March 27, 2021
@Author: Chen Zhang
@Brief: 欧几里得扩展算法 - 计算模反元素（模逆元）

算法概述：
    已知正整数a, b，可以在使用欧几里得算法求得a, b的最大公约数的同时得到整数x, y，使得它们满足贝祖等式：
        a * x + b * b = gcd(a, b)

        贝祖等式：二元一次不定方程，x与y的解是不确定的。
"""


def e_gcd(a, b):
    """
    原理：
        当递归到最后一层时a % b = 0，此时b的值即为要找的最大公约数。此时要满足贝祖等式a*x'+b*y'=gcd，
        也即要满足a*x'+b*y'=b，此时取x'=0, y'=1即可满足等式。
        为了获得(x', y')与上一层迭代中的(x, y)之间的关系，将最后一层迭代的a, b用上一层迭代中的a, b代
        替可得：

                                b * x' + (a % b) * y' = gcd

        上式中的a,b为倒数第二次递归中的a, b，将上式拆分重新合并得：

                        a * y' + b * [x' - (a // b) * y'] = gcd(a, b)

        与倒数第二层的贝祖等式a * x + b * y = gcd(a, b)对比后可得系数x, y之间的递归关系：

                                x = y'
                                y = x' - (a // b) * y'

        其中，(x', y')为较低层的贝祖等式系数，(x, y)为较高层的贝祖等式系数，a, b为较高层的输入。

    :param a: 较大的正整数
    :param b: 较小的正整数
    :return: (x, y, gcd)，贝祖系数(x, y)以及输入正整数的最大公约数
    """
    if a % b == 0:
        return 0, 1, b
    x, y, gcd_ = e_gcd(b, a % b)
    x, y = y, (x - (a // b) * y)
    return x, y, gcd_


if __name__ == '__main__':
    a, b = 50, 20
    x, y, q = e_gcd(a, b)
    print('x: %d; y: %d; 最大公约数: %d' % (x, y, q))
