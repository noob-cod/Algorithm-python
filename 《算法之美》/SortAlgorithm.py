"""
Created on Sunday, March 7, 2021
@Author: Chen Zhang
自学《算法之美——python语言实现》中的一些排序算法的实现

np.random.randint(0, 100, size=n)测试的算法运行时间：
   排序算法    时间复杂度      n=10          n=100       n=1,000      n=10,000     n=30,000    n=100,000      n=1,000,000
1、冒泡排序     O(n^2)    0.00002121s    0.0008471s   0.08966s      8.975s       80.87s          max             max
2、选择排序     O(n^2)    0.00001979s    0.0004456s   0.04678s      4.162s       37.04s          max             max
3、插入排序     O(n^2)    0.00001979s    0.0003808s   0.03872s      3.916s       35.19s          max             max
4、希尔排序     O(nlogn)  0.00002289s    0.0002508s   0.004087s     0.06164s     0.2082s       0.8666s         10.65s
5、快速排序     O(nlogn)  0.00002217s    0.0001361s   0.002134s     0.06075s     0.4365s       4.439s            max
6、归并排序     O(nlogn)  0.00004935s    0.0002993s   0.003014s     0.03491s     0.1104s       0.4064s         4.623s
"""
import time
import numpy as np


class Sort:
    """冒泡排序、选择排序、插入排序、希尔排序、快速排序、归并排序"""

    def __init__(self, sourceCollection):
        """创建排序对象，加载待排序的数列"""
        self._list = []  # 保存输入数列的空列表
        for item in sourceCollection:
            self._list.append(item)

        self._num = len(self._list)  # 数列的长度

    def BubbleSort(self, log=False):
        """冒泡排序"""
        if self._num == 1:
            return self._list
        exchange_num = 0  # 交换未发生标志位，若为True，则说明输入数列为有序数列，不需要继续排序
        for i in range(self._num):  # 冒泡循环次数控制
            for j in range(self._num-i-1):  # 冒泡每循环一次，末尾向前缩1
                if self._list[j] > self._list[j+1]:  # 若前一个数大于后一个数，则交换它们的位置
                    self._list[j], self._list[j+1] = self._list[j+1], self._list[j]
                    exchange_num += 1
            if exchange_num == 0:
                print('输入数列为有序数列!')
                break
        if log:  # 输出记录的交换发生次数
            print('总共发生了%d次交换.' % exchange_num)
            return self._list
        return self._list

    def SelectSort(self):
        """选择排序"""
        if self._num == 1:  # 若数列只有1个元素，则直接返回
            return self._list

        for i in range(self._num):  # 控制选择排序的循环次数
            min_index = i  # 初始化最小值的索引
            for j in range(i, self._num):  # 每循环一次，循环首位向后移动1，搜索本次循环内的最小值
                if self._list[j] < self._list[min_index]:  # 若当前值小于min_index所指向的值，则变更min_index
                    min_index = j
            self._list[i], self._list[min_index] = self._list[min_index], self._list[i]  # 每次循环最后，将最小值插入当前循环的首位

        return self._list

    def InsertSort(self):
        """插入排序"""
        if self._num == 1:  # 若数列只有1个元素，则直接返回
            return self._list

        for i in range(self._num-1):  # 选择排序只正向遍历数列一次
            # index = i  # 记录比较值要插入的位置的下标
            temp = self._list[i+1]  # 获取当前未排序的值
            for j in range(i, -1, -1):  # 与有序部分的数值进行倒序比较
                if temp < self._list[j]:  # 若比较值小于被比较值，则被比较值向后移动一位，插入未排序的值
                    self._list[j+1] = self._list[j]
                    self._list[j] = temp
                else:  # 若比较值不小于被比较值，则比较值的位置不变
                    self._list[j+1] = temp
                    break
            # temp = self._list[i+1]  # 中间变量存储比较值
            # for k in range(i+1, index, -1):  # 移位
            #     self._list[k] = self._list[k-1]
            # self._list[index] = temp  # 将比较值插入下标index处

        return self._list

    def ShellSort(self):
        """希尔排序，主要思路是减少插入排序中元素移动的次数以加快排序速度"""
        if self._num == 1:  # 若数列只有1个元素，则直接返回
            return self._list

        space = self._num // 2  # 设置希尔增量
        while space >= 1:
            for i in range(space):  # 控制每一个希尔增量对应的循环次数（分组数）
                for j in range(i+space, self._num, space):  # 每一个分组内使用插入排序
                    temp = self._list[j]
                    for k in range(j-space, -1, -space):
                        if temp < self._list[k]:
                            self._list[k+space] = self._list[k]
                            self._list[k] = temp
                        else:
                            self._list[k+space] = temp
                            break
            space = space // 2

        return self._list

    def QuickSort(self, low_index, high_index):
        """快速排序"""
        def move_help(array, low, high):
            """将数组中小于基准的元素移动到基准的右侧，大于基准的元素移动到基准的左侧"""
            pivot = array[high]  # 选择一个基准
            cursor_l = low  # 指针low
            cursor_h = high  # 指针high

            exchange = 0
            while cursor_l != cursor_h:
                if exchange % 2 is 0:
                    if array[cursor_l] < pivot:
                        cursor_l += 1
                    else:
                        array[cursor_h] = array[cursor_l]
                        exchange += 1
                else:
                    if array[cursor_h] >= pivot:
                        cursor_h -= 1
                    else:
                        array[cursor_l] = array[cursor_h]
                        exchange += 1
            array[cursor_h] = pivot

            return cursor_h

        if low_index < high_index:
            pivot = move_help(self._list, low_index, high_index)
            self._list = self.QuickSort(low_index, pivot-1)
            self._list = self.QuickSort(pivot+1, high_index)

        return self._list

    @staticmethod
    def MergeSort(array):
        """归并排序"""
        if len(array) == 1:
            return array

        def Merge(left_part, right_part):
            """将内部有序的两个数组left_part与right_part合并"""
            l_cursor, r_cursor = 0, 0
            temp = []  # 临时列表记录归并过程
            l_max = len(left_part)
            r_max = len(right_part)

            while l_cursor < l_max and r_cursor < r_max:  # 将left_part与right_part合并，每个数组最后至少会剩余1个元素
                if left_part[l_cursor] <= right_part[r_cursor]:
                    temp.append(left_part[l_cursor])
                    l_cursor += 1
                else:
                    temp.append(right_part[r_cursor])
                    r_cursor += 1
            temp += list(left_part[l_cursor:])  # 将剩余元素添加到temp后
            temp += list(right_part[r_cursor:])  # 将剩余元素添加到temp后

            return temp

        mid = len(array) // 2  # 找中位点
        left = Sort.MergeSort(array[: mid])  # 对左侧递归
        right = Sort.MergeSort(array[mid:])  # 对右侧递归
        return Merge(left, right)  # 返回归并结果


def test(input_array, mode, print_result=False):
    sorted = Sort(input_array)
    sorted_arr = None

    if mode is 'BubbleSort':
        sorted_arr = sorted.BubbleSort()
    elif mode is 'SelectSort':
        sorted_arr = sorted.SelectSort()
    elif mode is 'InsertSort':
        sorted_arr = sorted.InsertSort()
    elif mode is 'ShellSort':
        sorted_arr = sorted.ShellSort()
    elif mode is 'QuickSort':
        h = len(input_array) - 1
        sorted_arr = sorted.QuickSort(0, h)
    elif mode is 'MergeSort':
        sorted_arr = Sort.MergeSort(input_array)
    else:
        pass

    if print_result is True:
        print('%s的结果为：', end='\n')
        print(sorted_arr)


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(100000)

    arr = np.random.randint(0, 100, size=1000000)
    print('Random integer array is:', end='\n')
    # print(arr)

    mode = ['BubbleSort', 'SelectSort', 'InsertSort', 'ShellSort', 'QuickSort', 'MergeSort']
    k = 3

    begin = time.time()
    test(arr, mode[k], print_result=False)
    end = time.time()
    print('%s耗时为%.10f秒' % (mode[k], end-begin))
