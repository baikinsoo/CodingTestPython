class Solution:
    def groupAnagrams(self, strs):
        # 딕셔너리 생성
        dic = {}

        for x in strs:
            # 각 문자열 정렬
            sorted_x = ''.join(sorted(x))

            # 값이 없으면 새로운 key-value 추가
            if sorted_x not in dic:
                dic[sorted_x] = []

            # 주어진 문자열을 정렬했을 때 기존의 딕셔너리에 있는 값이라면 append로 원래의 문자열 추가
            dic[sorted_x].append(x)

        # 딕셔너리의 value값들을 이중 list로 반환
        return list(dic.values())

solution = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = solution.groupAnagrams(strs)
print(result)
