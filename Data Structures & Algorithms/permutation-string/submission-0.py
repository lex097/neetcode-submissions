class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        #s1 = "".join(s1)

        for i in range(0, len(s2) - len(s1) + 1):
            st = s2[i:i + len(s1)]
            st = sorted(st)
            if s1 == st:
                return True
        return False

