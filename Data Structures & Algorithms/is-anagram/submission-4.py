class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapOfS = {}
        mapOfT = {}
        for ch in s:
            mapOfS[ch] = mapOfS.get(ch, 0) + 1
        for ch in t:
            mapOfT[ch] = mapOfT.get(ch, 0) + 1
        for key in mapOfS:
            if ((key not in mapOfT) or (mapOfS[key] != mapOfT[key])):
                return False
        return True
        