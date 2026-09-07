class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxString = ''
        def dfs(r, l):
            if (l < 0) or (r >= len(s)):
                return s[l + 1: r]
            if (s[r] != s[l]): 
                return s[l + 1: r]

            return dfs(r +1 , l - 1)
        
        for i in range(len(s)):
            maxString = max(maxString, dfs(i, i), dfs(i + 1, i), key=len)
        return maxString