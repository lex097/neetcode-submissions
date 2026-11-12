from collections import defaultdict

class Solution:

    def check(self, sMap, tMap):

        for i in tMap:
            if sMap[i] < tMap[i]:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        retL = -1
        retR = -1
        retSize = float('inf')

        tFreqs = defaultdict(int)
        for i in t:
            tFreqs[i] += 1
        
        sWindow = defaultdict(int)
        l = 0
        for r in range(len(s)):
            sWindow[s[r]] += 1

            if not self.check(sWindow, tFreqs):
                continue
            
            while self.check(sWindow, tFreqs):
                if (r - l + 1 < retSize):
                    retSize = r - l + 1
                    retL = l
                    retR = r
                
                sWindow[s[l]] -= 1
                l += 1
            print(r, l)
        
        if (retL == -1 and retR == -1):
            return ""

        return s[retL : retR + 1]







