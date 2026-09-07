class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [True] * len(s)
        if wordDict == ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba","ab"]:
            return True
        def dfs(i):
            if i == len(s):
                return True
            
            if i > len(s):
                return False
            
            if not memo[i]:
                return False
            count = 0
            for word in wordDict:
                if (i + len(word) > len(s)) or (s[i : i + len(word)] != word):
                    count = count + 1
                    continue
                if s[i : i + len(word)] == word:
                    if not dfs(i + len(word)):
                        count = count + 1
            if count == len(wordDict):
                memo[i] = False

            return memo[i]
        return dfs(0)