class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [True] * len(s)
        
        hashSet = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True
            
            if i > len(s):
                return False
            
            if not memo[i]:
                return False

            for j in range(i, len(s)):
                if s[i : j + 1] in hashSet:
                    if dfs(j + 1):
                        memo[i] = True
                        return True
            memo[i] = False

            return False
        return dfs(0)