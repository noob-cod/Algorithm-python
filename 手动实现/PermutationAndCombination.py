"""
@Date: 2021/7/29 下午7:50
@Author: Chen Zhang
@Brief: 求数组中元素的排列与组合的算法

排列与组合的区别：
    相同元素的不同排列方式分别是不同的排列结果，但都是同一种组合的结果

基于回溯算法的求排列组合的过程的区别：
    在求排列的算法中，仅仅用到了回溯算法；
    在求组合的算法中，在回溯算法的基础上，引入了一个变量start来控制下一个元素的搜索方向，防止重复的发生。

对于可能包含相同元素的数组与数组中元素均不相同的数组求排列组合的异同：
    在可能包含相同元素的数组中求排列组合，处于同一层级的元素不能出现重复，否则结果中就一定会出现重复，因此
    引入一个哈希表used来记录同一层级中已经使用过的元素，在回溯推进的过程中，若遇到used中已经存在的元素，
    则跳过该元素。
"""


def permutation(nums):
    """对于不含重复元素的数组，基于回溯算法的获得数组元素的排列"""
    def dfs(subset, size):
        if len(subset) == size:
            res.append(subset[:])  # 更新res
            return
        else:
            for i in range(n):
                if nums[i] != '':
                    subset.append(nums[i])
                    nums[i] = ''  # 剪枝
                    dfs(subset, size)  # dfs
                    nums[i] = subset.pop()  # 回溯

    n = len(nums)
    if n == 0:
        return [[]]

    res = []
    for k in range(n):
        dfs([], k + 1)

    return res


def permutation2(nums):
    """对于可能包含重复元素的数组，基于回溯算法的获得数组元素的排列"""
    def dfs(subset, size):
        if len(subset) == size:
            res.append(subset[:])  # 更新res
            return
        else:
            used = {}
            for i in range(n):
                if nums[i] != '':
                    if nums[i] in used:
                        continue
                    used[nums[i]] = 0
                    subset.append(nums[i])
                    nums[i] = ''  # 剪枝
                    dfs(subset, size)  # dfs
                    nums[i] = subset.pop()  # 回溯

    n = len(nums)
    if n == 0:
        return [[]]

    res = []
    nums.sort()
    for k in range(n):
        dfs([], k + 1)

    return res


def combination(nums):
    """对于不含重复元素的数组，基于回溯算法的获得数组元素的组合"""
    def dfs(subset, size, start):
        if len(subset) == size:
            res.append(subset[:])  # 更新res
            return
        else:
            for i in range(start, n):
                if (size - len(subset)) > (n - start):
                    continue
                if nums[i] != '':
                    subset.append(nums[i])
                    nums[i] = ''  # 剪枝
                    dfs(subset, size, i)  # dfs
                    nums[i] = subset.pop()  # 回溯

    n = len(nums)
    if n == 0:
        return [[]]

    res = [[]]
    for k in range(n):
        dfs([], k + 1, 0)

    return res


def combination2(nums):
    """对于可能包含重复元素的数组，基于回溯算法的获得数组元素的组合"""
    def dfs(subset, size, start):
        if len(subset) == size:
            res.append(subset[:])
            return
        else:
            used = {}  # 记录同一层级中使用过的元素
            for i in range(start, n):
                if (size - len(subset)) > (n - start):
                    continue
                if nums[i] != '':
                    if nums[i] in used:
                        continue  # 若使用过则跳过该元素
                    used[nums[i]] = 0
                    subset.append(nums[i])
                    nums[i] = ''  # 剪枝
                    dfs(subset, size, i)  # DFS
                    nums[i] = subset.pop()  # 回溯

    n = len(nums)
    res = [[]]
    if n == 1:
        res.append(nums[:])
    else:
        nums.sort()
        for k in range(n):
            dfs([], k + 1, 0)

    return res


def combination3(nums):
    """对于可能包含重复元素的数组，基于一次遍历获得数组元素的组合"""
    res = [[]]
    nums.sort()  # 排序也是为了便于处理重复元素
    new_subsets = []  # new_subsets用于将“旧的结果”与“新的元素参与组合产生的新结果”相隔离。便于对重复的新元素进行处理
    for i in range(len(nums)):
        if i >= 1 and nums[i] == nums[i - 1]:
            # 当元素重复时，不能与res中的每种结果组合，否则会出现重复结果。只能与new_subsets中的结果继续组合。
            new_subsets = [subset + [nums[i]] for subset in new_subsets]
        else:
            # 当元素不重复时，可以与res中的每一种结果组合出新的结果，保存在new_subsets中
            new_subsets = [subset + [nums[i]] for subset in res]
        res = new_subsets + res  # 更新res
    return res


if __name__ == '__main__':
    inputs = [1, 2, 2]
    result = permutation2(inputs)
    print(result)
