"""
@Date: 2021/7/14 上午10:01
@Author: Chen Zhang
@Brief:
"""


class Solution:
    def subsets(self, nums):
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


if __name__ == '__main__':
    input = [9,0,3,5,7]
    print(Solution().subsets(input))
