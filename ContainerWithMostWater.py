class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        m = 0
        while l < r:
            if height[l] < height[r]:
                if (height[l] * (r - l)) > m:
                    m = (height[l] * (r - l))
                l += 1
            elif height[l] >= height[r]:
                if (height[r] * (r - l)) > m:
                    m = (height[r] * (r - l))
                r -= 1
        return m
