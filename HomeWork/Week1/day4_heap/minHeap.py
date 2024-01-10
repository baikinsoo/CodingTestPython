import heapq
import sys

class Solution():
    def MinHeap(self, cnt):
        heap = []
        for _ in range(cnt):
            num = int(sys.stdin.readline())
            if num != 0:
                heapq.heappush(heap, num)
            else:
                try:
                    print(heapq.heappop(heap))
                except:
                    print(0)

solution = Solution()
cnt = int(input())
print(solution.MinHeap(cnt))