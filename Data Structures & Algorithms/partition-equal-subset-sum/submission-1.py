class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        def dfs(i, ss1, ss2):
            if i >= len(nums):
                if ss1 == ss2:
                    return True
                return False
            
            return dfs(i + 1, ss1 + nums[i], ss2) or dfs(i + 1, ss1, ss2 + nums[i])

        return dfs(0, 0, 0)