"""
@Date: Tuesday, 16 March, 2021
@Author: Chen Zhang
@Brief: 牛客网动态规划习题 - 合唱队形

https://www.nowcoder.com/practice/6d9d69e3898f45169a441632b325c7b4?tpId=37&tags=&title=&diffculty=0&judgeStatus=0&rp=1&tab=answerKey

题目描述：
    计算最少出列多少位同学，使得剩下的同学排成合唱队形。
    说明：
    N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
    合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，
    则他们的身高满足存在i（1<=i<=K）使得T1<T2<......<Ti-1<Ti>Ti+1>......>TK。
    你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

    注意不允许改变队列元素的先后顺序 。
"""
import sys

while True:
    line = sys.stdin.readline().strip('\n')
    if line == '':
        break
    else:
        try:
            n = int(line)
            continue
        except:
            heights = list(map(lambda x: int(x), line.split(' ')))

            # 左侧最长递增子序列
            left = [0] * n
            for i in range(n):
                for j in range(i):
                    if heights[j] < heights[i]:
                        left[i] += 1
            # 右侧最长递增子序列
            right = [0] * n
            for i in range(n):
                for j in range(i + 1, n):
                    if heights[i] > heights[j]:
                        right[j] += 1

            mid = [0] * n
            for i in range(n):
                mid[i] = left[i] + right[i] + 1

            print(n - max(mid))