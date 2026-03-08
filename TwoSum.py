class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_nums = set(nums)
        for num in nums:
                if (target - num == num):
                    a = nums.index(num)
                    comp_nums.remove(num)
                    if num in nums[a + 1:]:
                        b = nums[a + 1:].index(num) + a + 1
                        return a, b
                if (target - num) in comp_nums:
                    return nums.index(num), nums.index(target - num)