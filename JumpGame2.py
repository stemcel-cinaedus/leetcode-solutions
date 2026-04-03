class Solution:
    def jump(self, nums: List[int]) -> int:
        stepcount, dist, m, i = 0, 0, 0, 0
        while i < len(nums) - 1:
            m = max(m, i + nums[i])
            if i == dist:
                stepcount += 1
                dist = m
            i += 1
        return stepcount
        
