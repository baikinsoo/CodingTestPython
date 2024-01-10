class Solution:
    def findPassword(self):

        dic = {}
        findCom = []
        answer = []

        # 회사 수 찾는 회사 수 입력
        comNum, findComNum = map(int, input().split())

        # 입력받은 회사 및 패스워드 입력
        for _ in range(comNum):
            comName, password = input().rstrip().split()
            dic[comName] = password

        # 찾을 회사 입력
        for _ in range(findComNum):
            findComName = input().rstrip()
            findCom.append(findComName)

        for x in findCom:
            answer.append(dic[x])

        answer = "\n".join(answer)

        return answer

    def findPassword_2(self):
        n, m = map(int, input().split())
        password_dict = {}

        for _ in range(n):
            address, password = input().split()
            password_dict[address] = password

        for _ in range(m):
            target_site = input()
            print(password_dict[target_site])

solution = Solution()
print(solution.findPassword())