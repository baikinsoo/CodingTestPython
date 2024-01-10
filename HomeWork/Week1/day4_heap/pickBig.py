import heapq


class Solution:
    def PickBig(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
solution = Solution()
print(solution.PickBig(nums, k))