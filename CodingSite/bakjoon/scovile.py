'''
모든 음식을 K이상으로 스코빌 지수를 만들고 싶어 한다.

스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 섞는다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
'''
import heapq

class Solution:
    def scoville(self, T, k):

        answer = 0
        heapq.heapify(T)

        while True:
            first = heapq.heappop(T)
            if first > k:
                break
            if len(T) == 0:
                return -1
            second = heapq.heappop(T)
            heapq.heappush(T, first + second * 2)
            answer += 1
        return answer


T = [1, 2, 3, 9, 10, 12]
k = 7
solution = Solution()
print(solution.scoville(T, k))



