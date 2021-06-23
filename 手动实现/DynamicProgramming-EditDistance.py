"""
@Date: 2021/6/23 下午7:27
@Author: Chen Zhang
@Brief: 动态规划 - 两个字符串之间的编辑距离的计算

编辑距离（Levenshtein）简介：
    1.编辑距离：在两个单词<w1, w2>之间，由其中一个单词w1转化为另一个单词w2所需要的最少单字符编辑操作次数。
    2.单字符编辑操作：
        插入一个字符
        删除一个字符
        替换一个字符

递归思路：
    (容易想到，但时间复杂度高，不适合长字符串间的计算)
    1 当两个字符串<w1, w2>中存在空字符串时
        编辑距离等于另一个字符串的长度，即 Levenshtein(w1, w2) = max(len(w1), len(w2))
    2 当两个字符串<w1, w2>都不为空时
        2.1 当w1与w2的最后一个字符相同时
            w1与w2同时去掉最后一个字符后，二者的编辑距离不变，即 Levenshtein(w1, w2) = Levenshtein(w1[:-1], w2[:-1])
        2.2 当w1与w2的最后一个字符不同时
            假设w1的长度不小于w2的长度，则w1与w2的编辑距离为以下三种情况中的最小值。

                情况1：将w1的最后一个字符替换为w2的最后一个字符后，w1与w2的编辑距离等于w1[:-1]与w2[:-1]的编辑距离加1，即
                    Levenshtein(w1, w2) = Levenshtein(w1[:-1], w2[:-1]) + 1
                情况2：将w1的最后一个字符删除后，w1与w2的编辑距离等于w1[:-1]与w2的编辑距离加1，即
                    Levenshtein(w1, w2) = Levenshtein(w1[:-1], w2) + 1
                情况3：在w2的末尾添加一个w1的最后一位字符后，w1与w2的编辑距离等于w1[:-1]与w2的编辑距离加1，即
                    Levenshtein(w1, w2) = Levenshtein(w1[:-1], w2) + 1

            合并后可得 Levenshtein(w1, w2) = min(Levenshtein(w1[:-1], w2[:-1]) + 1, Levenshtein(w1[:-1], w2) + 1)

动态规划思路：
    （不容易想到，但时间复杂度相对较低，在长字符串计算上优于递归思路）
    构建状态变量dp[i, j]，表示字符串w1的前i个字符与字符串w2前j个字符之间的编辑距离。
    各种情况下的状态转移：
        1. 当 i = j = 0时，若w1的第1个字符与w2的第1个字符相同，则编辑距离为0，否则为1。即
            1) w1[i] == w2[j], dp[i, j] = 0
            2) w1[i] != w2[j], dp[i, j] = 1
        2. 当 i = 0且 j ≠ 0时，若w1的第1个字符与w2的第j个字符相等，则编辑距离等于j-1，否则等于w1与w2[:-1]的编辑距离加1。即
            1) w1[i] == w2[j], dp[i, j] = j - 1
            2) w1[i] != w2[j], dp[i, j] = dp[i, j-1] + 1
        3. 当 j = 0且 i ≠ 0时，若w2的第1个字符与w1的第i个字符相等，则编辑距离等于i-1，否则等于w2与w1[:-1]的编辑距离加1。即
            1) w2[j] == w1[i], dp[i, j] = i - 1
            2) w2[j] != w1[i], dp[i, j] = dp[i-1, j] + 1
        4. 当 i ≠ 0且 j ≠ 0时，若w1的第i个字符与w2的第j个字符相等，则编辑距离等于w1[:-1]与w2[:-1]的编辑距离。否则等于w1替
        换末尾字符为w2的末尾字符后，w1[:-1]与w2[:-1]的编辑距离dp[i-1, j-1]加1；或较长字符串w1删去末尾字符后，w1[:-1]与w2
        的编辑距离dp[i-1, j]加1；或较段字符串w2添加一个w1的末尾字符后，w1[:-1]与w2的编辑距离dp[i, j-1]加1的结果中的最小值。
        即
            1) w1[i] == w2[j], dp[i, j] = dp[i-1], j-1]
            2) w1[i] != w2[j], dp[i, j] = min(dp[i-1, j-1] + 1, dp[i-1, j] + 1, dp[i, j-1] + 1)
    最后，dp[len(w1)-1, len(w2)-1]即为w1与w2的编辑距离。
"""


def levenshtein_recur(str1, str2):
    """
    递归计算编辑距离
    """
    assert isinstance(str1, str) and isinstance(str2, str), "Illegal input!"
    str1, str2 = str1.lower(), str2.lower()  # 忽略大小写
    n1, n2 = len(str1), len(str2)
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    if n1 < n2:
        str1, str2 = str2, str1
        n1, n2 = n2, n1
    if str1[n1-1] == str2[n2-1]:
        return levenshtein_recur(str1[:-1], str2[:-1])
    else:
        return min(levenshtein_recur(str1[:-1], str2[:-1])+1, levenshtein_recur(str1[:-1], str2) + 1)


def levenshtein_dp(str1, str2):
    """
    动态规划计算编辑距离
    """
    assert isinstance(str1, str) and isinstance(str2, str), "Illegal input!"
    str1, str2 = str1.lower(), str2.lower()  # 忽略大小写
    n1, n2 = len(str1), len(str2)
    if n1 == 0 or n2 == 0:
        return max(n1, n2)
    if n1 < n2:
        str1, str2 = str2, str1
        n1, n2 = n2, n1
    dp = [[0] * n2 for _ in range(n1)]  # 列代表str1，行代表str2
    for i in range(n1):
        for j in range(n2):
            if i == 0 and j == 0:
                dp[i][j] = 1 * (str1[i] != str2[j])
            elif i == 0:
                dp[i][j] = dp[i][j-1] + 1 * (str1[i] != str2[j])
            elif j == 0:
                dp[i][j] = dp[i-1][j] + 1 * (str1[i] != str2[j])
            else:
                if str1[i] == str2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)  # 替换、长字符串删除、短字符串增加
    return dp[-1][-1]


if __name__ == '__main__':
    mode = 1
    string1 = "ab"
    string2 = "bc"
    if mode == 0:  # 递归
        print('{}与{}之间的编辑距离为：{}'.format(string1, string2, levenshtein_recur(string1, string2)))
    elif mode == 1:  # 动态规划
        print('{}与{}之间的编辑距离为：{}'.format(string1, string2, levenshtein_dp(string1, string2)))
    else:
        pass
