import heapq

class Solution:
    def Maximum(self, T, k):

        list = heapq.nlargest(k, T, key=None)

        answer = (list[0] - 1) * (list[1] - 1)

        return answer

solution = Solution()
nums = [3,4,5,2]
# [5,4,3,2]
# list = [5,4]
k = 2
print(solution.Maximum(nums, k))