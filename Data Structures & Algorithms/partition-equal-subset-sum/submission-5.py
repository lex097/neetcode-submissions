class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, cSum):
            if cSum == target:
                return True
            if i >= len(nums) or cSum > target:
                return False
            if memo[i][cSum] != -1:
                return memo[i][cSum]
            memo[i][cSum] = dfs(i + 1, cSum + nums[i]) or dfs(i + 1, cSum)
            return memo[i][cSum]
        return dfs(0, 0)