class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def dfs(l, r):
            if (l < 0) or (r >= len(s)) or (s[l] != s[r]):
                return 0
            
            return 1 + dfs(l - 1, r + 1)

        ret = 0

        for i in range(len(s)):
            ret = ret + dfs(i, i + 1) + dfs(i, i)
        return ret