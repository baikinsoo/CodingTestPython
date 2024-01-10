from collections import defaultdict, Counter

class Solution:

    def jAndR_1(self, J:str, S:str) -> int:
        rock = defaultdict(int)
        count = 0

        for x in S:
            rock[x] += 1

        for x in J:
            count += rock[x]

        return count

    # Counter를 사용한 방식
    def jAndR_2(self,J:str,S:str)->int:
        rock = Counter(S)
        count = 0

        for x in J:
            count += rock[x]

        return count

    # 파이썬 다운 방식
    def jAndR_3(self,J:str,S:str)->int:
        return sum(s in J for s in S)

J = input()
S = input()
solution = Solution()
print(solution.jAndR_1(J,S))
print(solution.jAndR_2(J,S))
print(solution.jAndR_3(J,S))

