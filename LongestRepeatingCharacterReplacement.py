class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = {}
        res, m = 0, 0
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            
            m = max(freq.values())

            while (r - l + 1 - m) > k:
                freq[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res