class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        elif len(nums) == 0:
            return -1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[mid] >= nums[l]:
                if nums[mid] > target and nums[l] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[l] > target and nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1