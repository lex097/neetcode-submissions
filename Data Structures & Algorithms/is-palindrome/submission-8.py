class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = s.lower()
        k = len(s) - 1
        i = 0
        while i <= k:
            if not s[i].isalnum():
                i = i + 1
                continue
            if not s[k].isalnum():
                k = k - 1
                continue
            if s[i] != s[k]:
                return False
            i = i + 1
            k = k - 1
        return True