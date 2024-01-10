class Solution:
    def Parenthesis(self, s):
        # 괄호 쌍을 입력한다.
        pair = {
            ')' : '(',
        }
        # 여는 괄호를 지정한다.
        opener = '('
        # 값을 넣을 스택을 구성한다.
        stack = []

        # 전달받은 문자열을 돌면서 어떤 문자인지 확인한다.
        for char in s:
            # 여는 괄호인지 확인한다.
            if char in opener:
                # 여는 문자면 스택에 넣는다
                stack.append(char)
            # 여는 문자가 아닌경우를 작성한다
            else:
                # 스택이 비어있는지 확인한다.
                if not stack:
                    # 스택이 비여있으면
                    return False
                # 스택 가장 위에 있는 문자를 꺼내고 비교한다.
                top = stack.pop()
                if pair[char] != top:
                    return False

        return not stack


solution = Solution()
n = int(input())
for _ in range(n):
    s = input()
    if solution.Parenthesis(s):
        print("YES")
    else:
        print("NO")

