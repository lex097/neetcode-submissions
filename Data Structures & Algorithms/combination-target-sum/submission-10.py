class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = []

        def backtrack(index, combo, comboSum):
            if comboSum > target:
                return
            if comboSum == target:
                self.ret.append(combo[:])
                return
            
            for i in range(index, len(nums)):
                combo.append(nums[i])
                backtrack(i, combo, comboSum + nums[i])
                combo.pop()
            return
        backtrack(0, [], 0)
        return self.ret