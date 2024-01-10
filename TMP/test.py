from typing import List


class Solution:
    def permute(self, numbers: List[int]) -> List[List[int]]:

        result = []
        visited = [False] * len(numbers)

        def permutation(current, depth):
            if depth == len(numbers):
                result.append(current)
            else:
                for idx in range(len(numbers)):
                    if not visited[idx]:
                        visited[idx] = True
                        permutation(current + [numbers[idx]], depth + 1)
                        visited[idx] = False

        permutation([], 0)

        return result