class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []
        def backtrack(i, curr):
            if i == len(nums):
                self.ret.append(curr[:])
                return
            
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()

            backtrack(i + 1, curr)
            return
        
        backtrack(0, [])
        return self.ret