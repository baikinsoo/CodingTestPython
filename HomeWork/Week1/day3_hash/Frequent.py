from collections import Counter
from heapq import heappush, heappop


class Solution:

    # 그냥 방법
    def Frequent(self, T:list[int], k)->list[int]:
        answer = []
        freq = Counter(T)
        for x in freq.keys():
            if freq[x] >= k:
                answer.append(x)

        return answer

    # Counter를 이용한 방법
    def Frequent_2(self, nums:list[int])-> list[int]:
        freqs = Counter(nums)
        freqsHeap = []

        # 힙에 음수로 삽입
        for f in freqs:
            # heappush를 하게 되면 알아서 매번 heapify(작은 수가 우선순위로 정렬)를 적용
            heappush(freqsHeap, (-freqs[f], f))

        topk = list()

        for _ in range(k):
            topk.append(heappop(freqsHeap)[1])
        return topk

    # 파이썬다운 방식
    def Frequent_3(self, nums, k):
        return list(zip(*Counter(nums).most_common(k)))[0]



solution = Solution()
num = [1,1,1,2,2,3,3,4,4,5,5,6,6,6,7,8,9,9,9,9,9]
k = 5
print(solution.Frequent(num,k))


