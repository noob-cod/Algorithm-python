"""
@Created Time: Friday, March 12, 2021
@Author: Chen Zhang
@Brief: 递归 - 汉诺塔
"""


def Hanoi(num, x, y, z):
    """
    计算n个盘片在汉诺塔中从柱子x移动到柱子z的移动方法

    :param num: 盘片数量
    :param x: 柱子x
    :param y: 柱子y
    :param z: 柱子z
    """
    assert isinstance(x, str), print('x should be string type')
    assert isinstance(y, str), print('y should be string type')
    assert isinstance(z, str), print('z should be string type')

    if num == 1:
        print('%s --> %s' % (x, z))
    else:
        Hanoi(num-1, x, z, y)
        print('%s --> %s' % (x, z))
        Hanoi(num-1, y, x, z)


if __name__ == '__main__':
    n = 3
    Hanoi(3, 'A柱', 'B柱', 'C柱')
