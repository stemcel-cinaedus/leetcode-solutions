class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def spread(m: int) -> List[int]:
            mval = nums[m]
            l, r = m, m
            while l > 0:
                if nums[l - 1] == mval:
                    l -=1
                else:
                    break
            while r < len(nums) - 1:
                if nums[r + 1] == mval:
                    r += 1
                else:
                    break
            return [l, r]

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return spread(m)
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return [-1, -1]