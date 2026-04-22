class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        for c in t:
            if c in tmap:
                tmap[c] += 1
            else:
                tmap[c] = 1
        
        l, r, shortest = 0, 0, ""
        minlen, minstart = len(s) + 1, 0
        count = len(t)
        
        while r < len(s):
            if s[r] in tmap:
                if tmap[s[r]] > 0:
                    count -= 1
                tmap[s[r]] -= 1
            while count == 0:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    minstart = l
                if s[l] in tmap:
                    #bc im going to be moving l up, we need to stop counting the character its on rn
                    tmap[s[l]] += 1
                    #every matching char in s will have its hashmap value decremented, so if its greater than 0 after excluding l, that means count needs to be increased commensurately
                    if tmap[s[l]] > 0:
                        count += 1
                l += 1
            r += 1
        if minlen == len(s) + 1:
            return ""
        else:
            return s[minstart:(minstart + minlen)]