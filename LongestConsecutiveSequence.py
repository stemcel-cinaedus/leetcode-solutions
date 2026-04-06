class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        s = set(nums)
        m = 0
        for i in s.copy():
            if i not in s:
                continue
            locallen = 1
            if i - 1 in s or i + 1 in s:
                l, r = i - 1, i + 1
                while l in s:
                    locallen += 1
                    s.remove(l)
                    l -= 1
                while r in s:
                    locallen += 1
                    s.remove(r)
                    r += 1
                if locallen > m:
                    m = locallen
            else:
                if locallen > m:
                    m = locallen
        return m
