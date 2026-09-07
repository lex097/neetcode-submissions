class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ret = 0
        chars = set()

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l = l+1
            ret = max(ret, r - l + 1)
            chars.add(s[r])
            r = r+1
        return ret