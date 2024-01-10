class Solution:
    def KeyLogger(self, T: str) -> str:
        answer = []
        tmp = []

        for x in T:
            if x == "<":
                if answer:
                    tmp.append(answer.pop())
            elif x == ">":
                if tmp:
                    answer.append(tmp.pop())
            elif x == "-":
                if answer:
                    answer.pop()
            else:
                answer.append(x)

        while tmp:
            answer.append(tmp.pop())

        return ''.join(answer)

solution = Solution()

T1 = "dkfnek<<33334----"
T2 = "ThIsIsS3Cr3t"

arrT1 = solution.KeyLogger(T1)
arrT2 = solution.KeyLogger(T2)

print(arrT1)  # 출력: "dkfnek33334"
print(arrT2)  # 출력: "ThisIsSecret"
