class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ret = 0
        myMap = {}
        maxFreq = 0
        for r in range(len(s)):
            myMap[s[r]] = myMap.get(s[r], 0) + 1
            maxFreq = max(maxFreq, myMap[s[r]])
            if ((r - l + 1) - maxFreq) <= k:
                ret = max(ret, (r - l + 1))
            else:
                myMap[s[l]] = myMap[s[l]] - 1
                l = l + 1
        return ret