class Solution:
    def maraton(self, part, com):
        answer = {}  # 일반 딕셔너리 사용
        printAnswer = []

        for x in part:
            if x in answer:
                answer[x] += 1
            else:
                answer[x] = 1

        for x in com:
            if x in answer:
                answer[x] -= 1

        for y in answer.keys():
            if answer[y] > 0:
                printAnswer.append(y)

        realAnswer = ' '.join(printAnswer)
        return realAnswer

solution = Solution()
part = ["mislav", "stanko", "mislav", "ana"]
com = ["stanko", "ana", "mislav"]
print(solution.maraton(part, com))
