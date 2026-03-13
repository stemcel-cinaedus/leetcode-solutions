class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = "".join(filter(str.isalnum, s)).lower()
        if p[::-1] == p[::]:
            return True
        else:
            return False