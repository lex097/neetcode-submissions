class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ret = []

        def backtrack(index, subset):
            if index == len(nums):
                self.ret.append(subset[:]) #creates actual copy
                return
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()
            backtrack(index + 1, subset)
            return
        backtrack(0, [])
        return self.ret