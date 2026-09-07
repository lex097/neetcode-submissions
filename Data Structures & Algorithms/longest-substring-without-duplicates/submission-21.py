class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myMap = {}
        l = 0
        ret = 0

        for r in range(0, len(s)):
            if s[r] in myMap:
                l = max(myMap[s[r]] + 1, l)
                
                # move left pointer to where the new substring will be unique
            myMap[s[r]] = r
            ret = max(ret, r - l + 1)
        return ret