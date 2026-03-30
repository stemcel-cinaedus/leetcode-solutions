class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = []
        for n in range(0, len(nums)):
            if n == 0:
                z.append(nums[len(nums) - 1])
            else:
                z.append(nums[(len(nums) - 1) - n] * z[n-1])
        answer = []
        i, lp = 0, 1
        while i < len(nums):
            if i == 0:
                answer.append(z[len(z) - 2])
            elif i == len(nums) - 1:
                lp = lp * nums[i - 1]
                answer.append(lp)
            else:
                lp = lp * nums[i - 1]
                answer.append(lp * z[len(z) - 2 - i])
            i += 1
        return answer
