"""
@Created time: Friday, March 12, 2021
@Author: Chen Zhang
@Brief: 用递归的方法求输入字符的全排列
"""
import numpy as np


def fullPermutation(fixed, unfixed):
    """
    递归求全排列。
    每次迭代，将unfixed中的任意一个字符加入fixed，转化为求len(fixed+1)个字符与剩余len(unfixed-1)个字符的
    全排列。为防止后层迭代改变前层的参数，使用.copy()方法来固定本层迭代的参数，本层迭代只能使用本层的参数。
    """
    if not isinstance(unfixed, list):  # 将unfixed变为可迭代的list
        try:
            unfixed = list(unfixed)
        except TypeError:
            return -1

    n = len(unfixed)
    if n == 1:
        fixed.append(unfixed.pop())
        print(fixed)
    else:
        arr = unfixed.copy()  # 此处使用copy()方法是为了防止后面层的迭代改变当前层的unfixed
        for item in arr:
            temp_fixed = fixed.copy()  # 此处使用copy()方法是为了防止后面层的迭代改变当前层的fixed
            temp_unfixed = unfixed.copy()  # 此处使用copy()方法是为了防止后面层的迭代改变当前层的unfixed
            temp_unfixed.remove(item)
            temp_fixed.append(item)
            fullPermutation(temp_fixed, temp_unfixed)


if __name__ == '__main__':
    input = 'abcd'
    perm = []
    fullPermutation(perm, input)
