"""
@Date: Saturday, March 13, 2021
@Author: Chen Zhang
@Brief: 线型动态规划方法案例实现 - 求文本最长升序序列（前面一个英文字母的ASCII码小于后一个的）

线型动态规划：
    前后状态都只有一个一对一的关系，呈线性的逐步决策过程。
"""
import time


def LongestOrder(string):
    """找到输入中最长的升序序列"""
    assert isinstance(string, str), TypeError
    inputs = list(string)  # 将输入字符串转化为可迭代的数组
    ord_list = []  # 保存字符串及其长度状态值
    state = 1  # 长度状态值，序列长度，初始值为1
    i = 0
    s = ''
    while i < len(string):
        if len(s) == 0:  # 若初始序列首位为空，则将当前值赋给s
            s = inputs[i]
            i += 1
            continue
        if ord(s[-1]) < ord(inputs[i]):
            state += 1  # 状态值+1
            s += inputs[i]  # 序列延长
        else:
            ord_list.append((s+'_'+str(i-1), state))  # 存储上一组序列('序列_序列下标', 状态值)
            state = 1
            s = inputs[i]
        i += 1
    ord_list.append((s+'_'+str(i-1), state))
    ord_list.sort(key=lambda x: x[1], reverse=True)
    print('最长的升序序列为%s，它位于字符串中的第%d个字母到第%d个字母，长度为%d' %
          (ord_list[0][0].split('_')[0], int(ord_list[0][0].split('_')[1])-ord_list[0][1]+2,
           int(ord_list[0][0].split('_')[1])+1, ord_list[0][1])
          )  # 打印结果
    return ord_list[0]


def solve(string):
    """
    《算法之美》所给的代码。

    代码特点：
        1、用数组存储状态值；
        2、当前状态值仅受前一状态值的影响；
        3、前后状态是一对一的线型关系；、
    """
    dp = [1, ]
    len1 = len(string)
    j = 0
    max1 = 1
    while j < len1 - 1:
        if string[j] < string[j+1]:
            dp.append(dp[j] + 1)
            if dp[-1] > max1:
                max1 = dp[-1]
        else:
            dp.append(1)
        j += 1
    print('最大子串长度为：%d' % max1)


def Op_LongestOrder(string):
    """找到输入中最长的升序序列"""
    ord_list = []  # 保存字符串及其长度状态值
    state = 1  # 长度状态值，序列长度，初始值为1
    i = 0
    s = ''
    while i < len(string):
        if len(s) == 0:  # 若初始序列首位为空，则将当前值赋给s
            s += string[i]
            i += 1
            continue
        if s[-1] < string[i]:
            state += 1  # 状态值+1
            s += string[i]  # 序列延长
        else:
            ord_list.append((s+'_'+str(i-1), state))  # 存储上一组序列('序列_序列下标', 状态值)
            state = 1
            s = string[i]
        i += 1
    ord_list.append((s+'_'+str(i-1), state))
    ord_list.sort(key=lambda x: x[1], reverse=True)
    print('最长的升序序列为%s，它位于字符串中的第%d个字母到第%d个字母，长度为%d' %
          (ord_list[0][0].split('_')[0], int(ord_list[0][0].split('_')[1])-ord_list[0][1]+2,
           int(ord_list[0][0].split('_')[1])+1, ord_list[0][1])
          )  # 打印结果
    return ord_list[0]


if __name__ == '__main__':
    text1 = 'ABCABCDEFEOT'

    begin = time.time()
    LongestOrder(text1)
    end = time.time()
    print('自定义函数的运行时间为%.10fs' % (end-begin))  # 0.0000262260s
    print('\n')

    begin = time.time()
    solve(text1)
    end = time.time()
    print('书中所给函数的运行时间为%.10fs' % (end-begin))  # 0.0000061989s
    print('\n')

    begin = time.time()
    Op_LongestOrder(text1)
    end = time.time()
    print('优化后的自定义函数运行时间为%.10fs' % (end-begin))  # 0.0000095367s
