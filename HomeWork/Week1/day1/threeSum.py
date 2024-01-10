class Solution:
    def threeSum(self, nums):
        # 빈 배열 생성
        results=[]

        # 배열 정렬
        nums.sort()

        # 투 포인터를 사용할 것이기 때문에
        for i in range(len(nums) -2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 기준 제외 투 포인터 설정
            left, right = i + 1, len(nums) - 1
            while left<right:
                # 세 수의 합 계산
                sum = nums[i] + nums[left] + nums[right]
                # 정렬되어 있기 때문에 음수면 큰수쪽으로 이동
                if sum < 0:
                    left += 1
                # 양수면 작은쪽으로 이동
                elif sum > 0:
                    right -= 1
                # 0인 경우 정답 배열 넣기
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    # sum이 0인 이후에
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return results

solution = Solution()
nums = [-1,0,1,2,-1,-4]
print(solution.threeSum(nums))