class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        b = sorted(nums1 + nums2)
        if len(b) % 2 == 0:
            return ((b[len(b) // 2] + b[(len(b) // 2) -1])) / 2
        else:
            return b[len(b) // 2]
