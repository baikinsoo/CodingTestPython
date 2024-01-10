class Solution:

    # 투 포인터를 사용하여 길이를 구하는 방법!!! 투 포인터!!! 투 포인터!!!
    # 투 포인터를 이용하여 길이를 구할 것이다.
    def Longest(self, s:str)->str:
        # 사용된 알파벳(key)과 해당 알파벳의 인덱스 위치(value)를 갖는 딕셔너리 생성
        used={}
        # 가장 긴 글자의 길이 및 시작지점 0으로 초기화 -> 이후 투 포인터를 이용하여 index의 위치에서 start를 빼서 길이를 구할 것이다.
        maxLength = left = 0
        # s로 넘어온 문자열을 index : char 쌍으로 생성
        for right, char in enumerate(s):
            # 만약 검사중인 알파벳이 딕셔너리 key로 존재하는 문자이면서, start의 값이 기존의 해당 알파벳의 위치보다 작은 경우
            if char in used and left <= used[char]:
                # 알파벳이 중복되면 안되기 때문에 이전 알파벳의 위치 + 1 지점을 start로 한다.
                left = used[char] + 1
            else:
                # 그냥 투 포인터를 통해 길이를 구하는 방법
                maxLength = max(maxLength, right - left + 1)

            # 현재 알파벳의 value(위치)를 변경한다.
            used[char] = right

        return maxLength

solution = Solution()
s = "asdfqwerzxcv"
print(solution.Longest(s))
