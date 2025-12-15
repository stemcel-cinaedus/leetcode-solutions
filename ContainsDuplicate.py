class Solution(object):

    def containsDuplicate(self, nums):
        nums.sort() ## Sort nums 
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]: ## Because nums is sorted, duplicates will appear consecutively.
                return True
        return False
