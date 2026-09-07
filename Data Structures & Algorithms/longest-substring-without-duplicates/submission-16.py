class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        ret = 0
        l, r = 0, 1
        if not s:
            return 0
        if len(s) == 1:
            return 1
        charSet.add(s[l])
        while r < len(s):
            if s[r] in charSet:
                ret = max(ret, len(s[l:r]))

                while s[r] in charSet:
                    charSet.remove(s[l])
                    l = l + 1
                charSet.add(s[r])
                r = r+1
            else:
                charSet.add(s[r])
                ret = max(ret, len(s[l:r + 1]))
                r = r+1
        return ret




# zxyxzyx