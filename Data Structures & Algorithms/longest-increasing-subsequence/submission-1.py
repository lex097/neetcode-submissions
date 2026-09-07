class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, j):
            if i >= len(nums):
                return 0
            if j == -1 or nums[i] > nums[j]:
                return max(1 + dfs(i + 1, i), dfs(i + 1, j))
            return dfs(i + 1, j)
        
        return dfs(0, -1)