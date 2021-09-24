"""
@Date: 2021/8/18 下午5:17
@Author: Chen Zhang
@Brief: 快速幂算法，将求n次幂的时间复杂度由O(n)降低至O(logn)

计算a^n的常规算法为求n个a的乘积，需要计算n-1次乘法，时间复杂度为O(n)

快速幂算法则对幂进行拆分 a^n = (a^(n/2))^2，只需要计算(n/2)+1次乘法，时间复杂度下降到了O(logn)
"""


def qpow_recursive(a, n):
    """递归形式"""
    if n == 0:
        return 1
    elif n % 2 == 1:
        return qpow_recursive(a, n-1) * a
    else:
        tmp = qpow_recursive(a, n/2)  # 此处的tmp是必要的，若写为qpow(a, n/2) * qpow(a, n/2)则时间复杂度退化为O(n)
    return tmp * tmp


def qpow(a, n):
    """非递归形式"""
    ans = 1
    while n:
        if n & 1:
            ans *= a
        a *= a
        n >>= 1
    return ans


if __name__ == '__main__':
    a = 7
    n = 10
    print('递归计算的结果为：{}'.format(qpow_recursive(a, n)))
    print('非递归计算的结果为：{}'.format(qpow(a, n)))
