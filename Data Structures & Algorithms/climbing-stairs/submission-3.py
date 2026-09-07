class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(step):
            if step >= n:
                return step == n
            
            if cache[step] != -1:
                return cache[step]
            cache[step] = dfs(step+1) + dfs(step + 2)
            return dfs(step + 1) + dfs(step + 2)
        return dfs(0)