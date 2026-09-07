class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n) for _ in range(n)]
        def dfs(i, j):
            if i >= len(nums):
                return 0

            if memo[i][j+1] != -1:
                return memo[i][j+1]
            if j == -1 or nums[i] > nums[j]:
                LIS = max(1 + dfs(i + 1, i), dfs(i + 1, j))
                memo[i][j+1] = LIS
                return LIS
            memo[i][j+1] = dfs(i + 1, j)

            return memo[i][j+1]
        
        return dfs(0, -1)