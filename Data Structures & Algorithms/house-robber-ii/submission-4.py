class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = [-1] * (len(nums))
        def dfs(s, e):
            if s >= (e + 1):
                return 0
            if memo[s] != -1:
                return memo[s]
            
            memo[s] = max(nums[s] + dfs(s + 2, e), dfs(s + 1, e))

            return memo[s]
        
        poss1 = dfs(0, len(nums) - 2)
        memo = [-1] * (len(nums))
        poss2 = dfs(1, len(nums) - 1)

        return max(poss1, poss2)