class Solution:
    def numDecodings(self, s: str) -> int:
        memo = [-1] * len(s)

        def dfs(l):
            if (l >= len(s)):
                return 1
            if (s[l] == "0"):
                return 0
            
            if memo[l] != -1:
                return memo[l]
            
            memo[l] = dfs(l + 1)

            if (l + 1 < len(s)) and (int(s[l:l + 2]) <= 26):
                memo[l] = memo[l] + dfs(l + 2)
            
            return memo[l]
        
        return dfs(0)