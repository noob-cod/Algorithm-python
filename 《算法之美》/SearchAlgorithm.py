"""
Created on Tuesday, March 9, 2021
@Author: Chen Zhang

自学《算法之美——python语言实现》中的一些搜索算法的实现
"""
import time


class Search:
    """Implement of several search algorithm."""
    def __init__(self):
        pass

    @staticmethod
    def LinearSearch(array, key, mode='single'):
        """数组线型查找，适用于有序或无序数组"""
        _num = len(array)

        if mode is 'single':  # 搜索单个满足条件的对象
            for ind in range(_num):
                if array[ind] == key:
                    return ind  # 找到则返回下标
            return -1  # 未找到则返回-1

        elif mode is 'all':  # 搜索全部满足条件的对象
            ind = 0
            ind_list = []
            while ind < _num:
                if array[ind] == key:
                    ind_list.append(ind)
                ind += 1
            if len(ind_list) == 0:
                return -1
            else:
                return ind_list

        else:
            pass

    @staticmethod
    def BinarySearch(array, key):
        """二分查找，适用于有序数组，默认输入array有序"""
        _num = len(array)  # 数组长度
        left = 0  # 左指针
        right = _num - 1  # 右指针
        while left <= right:  # 直到左指针等于右指针，二分结果只有一个元素时停止搜索
            mid = (left + right) // 2  # 计算二分中点
            if array[mid] == key:  # 若找到key，则返回其下标
                return mid
            elif array[mid] < key:  # 若key大于二分中点，则检索范围缩小至二分中点右侧
                left = mid + 1
            else:
                right = mid - 1  # 若key小于二分中点，则检索范围缩小至二分中点左侧
        return -1  # 未找到返回-1

    @staticmethod
    def InterpolationSearch(array, key):
        """插值查找，适用于有序数列，默认输入为有序数列"""
        _num = len(array)  # 数组长度
        left = 0  # 左指针
        right = _num - 1  # 右指针
        while left <= right:  # 直到左指针等于右指针，二分结果只有一个元素时停止搜索
            mid = left + int((key - array[left]) * (right - left) / (array[right] - array[left]))  # 计算二分中点
            if array[mid] == key:  # 若找到key，则返回其下标
                return mid
            elif array[mid] < key:  # 若key大于二分中点，则检索范围缩小至二分中点右侧
                left = mid + 1
            else:
                right = mid - 1  # 若key小于二分中点，则检索范围缩小至二分中点左侧
        return -1  # 未找到返回-1

    @staticmethod
    def FibonacciSearch(array, key):
        """斐波那契查找，适用于有序数列，在二分查找的基础上根据斐波那契数列作为下标对数据进行分割"""
        _num = len(array)  # 原始数组长度

        # 产生斐波那契数列
        i = 1
        fib_list = [1, 1]  # 保存斐波那契数列
        while fib_list[i] <= _num:
            fib_list.append(fib_list[i-1] + fib_list[i])
            i += 1

        # 对输入数组进行预处理
        left = 0
        right = _num - 1  # array最右元素下标
        f = fib_list[i]  # 最近的斐波那契数
        j = 0
        while j < f - _num:  # 用array的最后一个元素将array的长度补充到之后最近的一个斐波那契数
            array.append(array[right])
            j += 1

        # 斐波那契查找
        n = len(fib_list)  # 斐波那契数列长度
        while left <= right:  # 直到左指针不小于右指针为止
            # 确定mid下标
            if n < 2:
                mid = left  # 若斐波那契数列小于2，则mid等于left
            else:
                mid = left + fib_list[n-1] - 1  # mid等于斐波那契数列最后一个值-1

            if key < array[mid]:  # 当key小于下标为mid的值时，将检索范围移动到mid左侧，斐波那契数组左移1位
                right = mid - 1
                n -= 1
            elif key > array[mid]:  # 当key大于下标为mid的值时，将检索范围移动到mid右侧，斐波那契数组左移2位，因为len(arr[:mid]) + len(array[mid:]) = fib_list[n-1] + fib_list[n-2]
                left = mid + 1
                n -= 2
            else:  # 若找到了key
                if mid <= right:  # 若不在数组扩增的部分内
                    return mid
                else:  # 若在数组扩增的部分内
                    return right
        return -1

    @staticmethod
    def BlockSearch(array, key, index, n):
        """分块查找，适用于在块间有序、块内无序的数据内查找，应用于分布式数据库数据存储及查询"""
        # 首先通过块找出块范围
        block_max = -1
        j = 0  # 块索引
        for i in index:  # index位块内最大值索引数列
            j += 1
            if key <= i:
                block_max = i
                break
        if block_max == -1:
            return -1

        # 在目标块中使用线性搜索算法
        result = Search.LinearSearch(array[(j - 1) * n: (j * n - 1)], key)  # 块内线性查找，n位每个块内的数据量
        if result == -1:
            return -1  # 未找到则返回-1
        else:
            return (j - 1) * n + result  # 找到则返回换算后的下标

    class HashSearch:
        """哈希查找，时间复杂度为O(1)，适用于有序或无序数组，应用于大数据存储及查找"""
        def __init__(self, capacity=20):
            self.capacity = capacity  # 哈希表的容量，默认值为20
            self.HashTable = {i: None for i in range(self.capacity)}  # 建立空的哈希表

        def Hash(self, value):
            """哈希函数"""
            address = value % self.capacity  # 计算哈希地址
            if self.HashTable[address] is None:  # 若地址指向的位置为空，则该地址可用
                return address
            else:  # 否则，尝试将地址+1
                while address <= self.capacity:
                    address += 1
                    if self.HashTable[address] is None:
                        return address
            return -1  # 若未找到合适的地址，则返回-1

        def buildHashTable(self, values):
            """构建哈希表"""
            for value in values:
                address = self.Hash(value)  # 计算哈希地址
                if address is not -1:
                    self.HashTable[address] = value
                else:
                    print('HashTable内存不足')

        def search(self, key):
            """搜索函数"""
            address = self.Hash(key)  # 计算哈希地址
            if address is -1:  # 若超出地址范围，则返回-1
                return -1
            else:
                if self.HashTable[address] == key:  # 若找到key，则返回地址address
                    return address
                else:  # 否则尝试将address+1继续寻找，直到找完哈希表最后一个元素
                    while address <= self.capacity:
                        address += 1
                        if self.HashTable[address] == key:  # 若找到key，则返回当前address
                            return address
                    return -1  # 未找到则返回-1


if __name__ == '__main__':
    input_array = [3, 1, 9, 6, 4, 7, 8, 2, 5]
    input_array_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 5

    begin = time.time()
    result = Search.FibonacciSearch(input_array_sorted, key)
    end = time.time()
    print('Result: ', result)
    print('Running time: ', end-begin)
