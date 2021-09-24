"""
@Date: 2021/8/20 上午11:35
@Author: Chen Zhang
@Brief: 求给定整数数组中所有和为target的不重复三元组

排序 + 双指针
时间复杂度：O(n^2)
空间复杂度：O(n/3)
"""
from typing import List


def sum_of_3_numbers(nums: List, target: int) -> List[List[int]]:
    """DFS+剪枝+回溯+排序"""
    n = len(nums)
    if n < 3:
        return []

    res = []
    nums.sort()  # 这里排序的目的是方便后续操作去重

    def dfs(subset, start):
        if len(subset) == 3:
            if sum(subset) == target:
                res.append(subset[:])
            return
        for i in range(start, n):
            if (n - start) < (3 - len(subset)):
                continue
            if i != start and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            dfs(subset, i+1)
            subset.pop()

    dfs([], 0)
    return res


if __name__ == '__main__':
    inputs = [-1, 0, 1, 2, -1, -4]
    print('nums = [-1, 0, 1, 2, -1, -4], target =  0')
    print('standard result is: [[-1, -1, 2], [-1, 0, 1]]')
    print('my result is:', '\n', sum_of_3_numbers(inputs, 0))

    print('nums = [-1, 0, 1, 2, -1, -4], target =  1')
    print('standard result is: [[-1, 0, 2]]')
    print('my result is:', '\n', sum_of_3_numbers(inputs, 1))
