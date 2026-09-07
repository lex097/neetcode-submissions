class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        desiredFreqMap = {}
        for i in s1:
            desiredFreqMap[i] = desiredFreqMap.get(i, 0) + 1
        l = 0
        FreqMap = {}
        for r in range(len(s2)):
            FreqMap[s2[r]] = FreqMap.get(s2[r], 0) + 1
            if FreqMap == desiredFreqMap:
                return True
            if (r - l + 1) == len(s1):
                FreqMap[s2[l]] = FreqMap[s2[l]] - 1
                if FreqMap[s2[l]] == 0:
                    FreqMap.pop(s2[l])
                l = l+1
        return False