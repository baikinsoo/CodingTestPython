# 1. 가장 긴 문자열을 찾아야 한다.
# 2. 투 포인터를 이용해서 기준을 잡곡 양쪽으로 이동하면서 문자가 같은지 판별한다.
class Solution(object):
    def longestPalindrome(self, s):

        # 문자가 한글자일 때 계속 실패해서 넣은 코드
        if len(s) < 2 :
            return s

        result = ''

        # max를 이용하여 최대길이 값을 찾고,
        for i in range(len(s) - 1):
            result = max(result, self.find(i, i + 1, s), self.find(i, i, s), key=len)

        return result

    # 문자열과 왼쪽 오른쪽의 기준을 전달 받고 팰린드롬을 찾는다.
    def find(self, left, right, s):
        # 좌측은 0보다 우측은 문자열보다 짧을 동안 또 문자가 같을 동안만 찾는다.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # 문자가 다른 부분까지 검사하기 때문에 해당 부분은 제외하고 문자열을 반환한다
        return s[left + 1:right]

solution = Solution()
s = "babbbasdfkl;djksafdklsadfljfl;asd"
print(solution.longestPalindrome(s))


