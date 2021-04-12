"""
Created on Wednesday, March 10, 2021
@Author: Chen Zhang
自学《算法之美——python语言实现》中的一些字符串相关算法的实现
"""
import time


class String:
    """String Related Algorithms"""
    def __init__(self, input_string):
        assert isinstance(input_string, type('str')), 'Wrong input'
        self.string = input_string
        self.length = len(self.string)  # 字符串长度

    def ViolentSearch(self, key_string):
        """暴力搜索算法，输入要找的关键字，输出(关键字首字符下标列表，找到的关键字个数)"""
        i = 0  # 记录外部搜索进度
        n = len(key_string)  # 模式字符串长度
        inds = []  # 存放所有找到的字符串的首个字符的下标
        while i <= self.length - n:
            j = 0  # 记录内部搜索进度
            while j <= n - 1:
                if key_string[j] != self.string[i + j]:
                    break
                j += 1
            if j == n:  # 找到一个
                inds.append(i)
            i += 1

        if len(inds) is 0:
            print('字符串中不包含与该关键字相同的字段！')
            return inds, -1
        else:
            print('共找到%d个相同的字段。' % len(inds))
            return inds, len(inds)  # 返回首个字符的下标列表与找到的字符数量

    def BMSearch(self, key_string):
        """Boyer-Moore搜素算法"""

        def GoodIndex(keys):  # 好后缀子算法
            n = len(keys)
            m = n
            p = n  # 好后缀在模式串里出现的最左边的位置
            last = keys[n-1]  # 最后一个字符，看做好字符
            while n > 1:  # 检查模式串里左边是否有一样的好字符
                if keys[n-2] == last:  # 有一样的好字符，记录下标的位置，只记录最靠近last的一个好字符
                    p = n - 2
                n -= 1
            return m - p  # 返后缀在模式串里的右长度（从最右边开始往左数）

        def CountBadIndex(keys, bad):  # 坏字符子算法
            n = len(keys)
            j = n
            while j > 0:
                if keys[j - 1] == bad:
                    return n - j
                j -= 1
            return n  # 坏字符在模式串中不存在

        def CompareAndSearch(arr, keys):
            last_count = GoodIndex(keys)  # 好后缀，获得最后一个字母在模式串里出现的位置右长度
            print('最后一个字符在前面的重复次数%d' % last_count)
            FindNum = 0  # 用于统计查找到的模式串的个数
            text_n = len(arr)
            k_n = len(keys)
            move = 0
            while move <= text_n - k_n:  # 循环移动，查找模式串个数
                j = k_n - 1
                print('移动位置%d' % move)
                while j >= 0:  # 比较是否存在坏字符
                    if arr[move+j] != keys[j]:
                        bad = arr[move+j]
                        break  # 存在坏字符
                    j -= 1
                if j == -1:  # 在文本串里找到一个模式串
                    FindNum += 1  # 累加统计
                    move += k_n  # 向右移动一个模式串
                else:
                    if j == k_n - 1:  # 最后一个不一致，出现坏字符bad
                        print('坏字符为%s' % bad)
                        d = CountBadIndex(keys, bad)  # 判断坏字符在模式串里的位置
                        print('增加的坏字符长度为%d' % d)
                        move += d
                    else:  # 存在好后缀，检查最后一个字母在模式串前面出现的次数
                        move += k_n - last_count  # 向右移动模式串长度-好后缀在模式串里出现的右长度
            print('模式串%s在文本串里找到的次数为%d' % (keys, FindNum))

        CompareAndSearch(self.string, key_string)

    def SundaySearch(self, key_string):
        """Sunday搜索算法"""
        def CheckKeys(keys, endi):
            """检查模式串尾+1对应的文本串字符在模式串里的位置"""
            n = len(keys)
            j = n - 1
            while j >= 0:
                if keys[j] == endi:
                    print('%s的距末位置%d' % (endi, j))
                    return n - j  # 移动相对位置数n-j
                j -= 1
            return n + 1  # 模式串不存在，移动相对位置数n+1

        count = 0  # 找到字符串的数量
        i = 0
        t_n = self.length - 1  # 文本串长度-1
        k_m = len(key_string) - 1  # 模式串长度-1
        while i <= t_n:
            j = 0
            m = 0
            while j <= k_m:  # 比较模式串与文本串对应的字符
                if self.string[i + j] != key_string[j]:  # 如果字符串不相等
                    if i + k_m + 1 > t_n:  # 模式串与文本串比较时，i+k_m+1不能超过文本串的长度
                        m = -1
                        i += k_m + 1
                        break  # 最后一次比较时，剩余文本串长度小于模式串，退出循环
                    endi = self.string[i + k_m + 1]
                    m = CheckKeys(key_string, endi)
                    begin = self.string[i + j]
                    i += m
                    print('开始比对字符串%s，末尾+1出%s，移动下标到%d处，移动了%d' % (begin, endi, i, m))
                    break
                j += 1
            if m == 0:
                count += 1
                print('找到%s开始下标%d' % (key_string, i))
                i += k_m + 1
        print('%s在文本串里找到%d次' % (key_string, count))

    @staticmethod
    def to_SuffixExpression(input):
        """逆波兰公式（后缀表达式）转化算法，运算符压入S之前，要把S末尾的高优先级运算符弹出压入L，优先级高的运算符先进L。
        逆波兰公式可能不唯一"""
        n = len(input)  # 输入字符串的长度
        S = []  # 临时存放运算符
        L = []  # 存放逆波兰公式
        for ind in range(n):  # 逐个扫描input中字符
            try:
                value = int(input[ind])  # 若value是数值，则直接追加到L末尾
                L.append(value)
            except ValueError:
                value = input[ind]
                if value == '(':  # 若value是'('，则直接压入S
                    S.append(value)
                elif value == ')':  # 若value是')', 则将S中最接近栈顶的'('之后的运算符全部弹出并压入L，之后丢弃'('
                    for i in range(len(S)-1, -1, -1):
                        if S[i] != '(':
                            temp = S.pop()
                            L.append(temp)
                        else:
                            S.pop()
                            break
                else:
                    if len(S) == 0 or S[-1] != '(':  # 若value是'+'或'-'，且S为空或S末尾不为'('，则直接将value压入S
                        if len(S) != 0 and S[-1] in ['*', '/']:
                            j = len(S) - 1
                            while j != -1 and S[j] != '(':
                                if S[j] in ['*', '/']:
                                    L.append(S.pop())
                                j -= 1
                        S.append(value)
                    else:  # 其余情况则将value直接压入S
                        S.append(value)
        while len(S) != 0:
            L.append(S.pop())
        return L

    @staticmethod
    def is_Palindrome(input):
        """回文字符串判断函数"""
        n = len(input)
        i = 0
        j = n - 1
        while i < j:
            if input[i] != input[j]:  # 发现不对称的位置
                print('False')
                return 0
            i += 1
            j -= 1
        print('True')
        return 1


if __name__ == '__main__':
    keys = 'China'
    pal_keys = 'abcba'
    formula = '3/(6*4/3*8)'
    s1 = 'I am from China. I am a student. I live in Tianjin China. I love Python. Are you from China'

    string = String(s1)

    print('============暴力搜索=============')
    begin = time.time()
    string.ViolentSearch(keys)
    end = time.time()
    print('暴力搜索耗时%.10f秒' % (end-begin))
    print('\n')

    print('============BM搜索=============')
    begin = time.time()
    string.BMSearch(keys)
    end = time.time()
    print('BM搜索耗时%.10f秒' % (end - begin))
    print('\n')

    print('============Sunday搜索=============')
    begin = time.time()
    string.SundaySearch(keys)
    end = time.time()
    print('Sunday搜索耗时%.10f秒' % (end - begin))
    print('\n')

    print('============逆波兰公式转换=============')
    result = string.to_SuffixExpression(formula)
    print('%s转换后的逆波兰公式为：' % formula, end='\n')
    print(result)
    print('\n')

    print('============回文字符串判断=============')
    print('%s是否为回文字符串：', keys)
    string.is_Palindrome(keys)
    print('\n')
    print('%s是否为回文字符串：', pal_keys)
    string.is_Palindrome(pal_keys)
    print('\n')
