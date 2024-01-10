'''
각 배열의 1 갯수를 딕셔너리에 넣는다
'''
import heapq
from typing import List


class Solution:
    def Matrix(self, mat:List[List[int]], k:int)->List[int]:

        heap = []
        answer = []
        for i in range(len(mat)):
            # 각 배열의 1의 갯수를 센다
            cnt = mat[i].count(1)
            # heap에 1의 갯수 및 해당 인덱스를 저장한다. heap의 경우 0번 인덱스를 기준으로 정렬한다.
            heapq.heappush(heap, [cnt, i])

        for _ in range(k):
            num = heapq.heappop(heap)[1]
            answer.append(num)

        return answer

    def kWeakestRows(mat, k):
        answer = []
        for i, tot in enumerate(mat):
            total = sum(tot)
            answer.append((i, total))
        answer.sort(key=lambda x: x[1])
        print(answer)
        return [dad for dad, _ in answer[:k]]

mat = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
k = 2
solution = Solution()
print(solution.Matrix(mat,k))
