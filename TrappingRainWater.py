class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        l, r = 0, len(height)-1
        ml, mr, total = 0, 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= ml:
                    ml = height[l]
                else:
                    total += ml - height[l]
                l += 1
            else:
                if height[r] >= mr:
                    mr = height[r]
                else:
                    total += mr - height[r]
                r -= 1
        return total
            
