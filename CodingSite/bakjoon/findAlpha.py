import string

class Solution:
    def alpha(self, str):
        result = [-1]*len(string.ascii_lowercase)
        for i in range(len(str)):
            char = str[i]
            for j in range(len(string.ascii_lowercase)):
                lo = string.ascii_lowercase[j]
                if result[j] == -1 and char == lo:
                    result[j] = i
        return result  # 결과를 반환하도록 수정

    def alpha2(self, str):
        result = [-1] * len(string.ascii_lowercase)
        for i in range(len(str)):
            idx = ord(str[i]) - ord('a')
#             ord : 문자를(알파벳 대소문자) -> 숫자로 바꿔준다.
# a -> 97, b -> 98
            if result[idx] == -1:
                result[idx] = i
        return result



solution = Solution()
answer = solution.alpha("bakjoon")
answer2 = solution.alpha2("bakjoon")
print(' '.join([str(num) for num in answer]))
print(' '.join([str(num) for num in answer2]))
