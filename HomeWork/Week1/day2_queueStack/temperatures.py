class Solution:
    def Temperatures(self, T: list[int]) -> list[int]:
        # 기다려야하는 날짜를 입력하기 위한 새로운 배열 생성
        answer = [0] * len(T)
        # 스택 생성
        stack = []

        # 각 날씨에 대해 이중 리스트 생성
        for i, cur in enumerate(T):
            # 스택에 값이 존재하고, 넘어온 온도가 stack의 제일 상단 값 보다 큰지 판별
            while stack and cur > T[stack[-1]]:
                # 위에 조건이 만족하면 가장 위의 값을 꺼낸다.
                last = stack.pop()
                # 꺼낸 값은 i 즉, 날짜가 되고, 해당 인덱스의 값을 i(해당 인덱스) - last(스택 가장 위에 있는 인덱스 값)
                answer[last] = i - last
            # while문이 참이 아니라면 stack에 날짜에 대한 인덱스 입력
            stack.append(i)
        return answer

solution = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(solution.Temperatures(T))


