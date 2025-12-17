class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Anagrams must be the same length
            return False
        
        t = list(t)  # Convert string to list so letters can be removed
        for char in s:
            if char in t:
                t.remove(char)
            else:
                return False
        return True # If all characters in s can be removed from t then the strings are anagrams.
