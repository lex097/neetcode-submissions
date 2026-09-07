class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        def dfs(i, cSum):
            if cSum == target:
                return True
            if i >= len(nums) or cSum > target:
                return False
            return dfs(i + 1, cSum + nums[i]) or dfs(i + 1, cSum)
        return dfs(0, 0)