# [2, 5, 6, 9]
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = []

        def backtrack(index, subset, subsetSum):
            if subsetSum > target:
                return
            if subsetSum == target:
                for i in self.ret:
                    if (i == subset):
                        return
                self.ret.append(subset[:])
                return
            if (index != 0):
                subset.append(nums[index-1])
                backtrack(index, subset, subsetSum + nums[index-1])
                subset.pop()
            if (index == len(nums)):
                return

            subset.append(nums[index])
            backtrack(index + 1, subset, subsetSum + nums[index])
            subset.pop()

            backtrack(index + 1, subset, subsetSum)
            return
        backtrack(0, [], 0)
        return self.ret