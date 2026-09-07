class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        def backtrack(index, combo):
            if index >= len(nums):
                ret.append(combo[:])
                return
            
            combo.append(nums[index])
            backtrack(index + 1, combo)
            combo.pop()

            while (index < len(nums) - 1) and (nums[index] == nums[index + 1]):
                index = index + 1
            backtrack(index + 1, combo)
        backtrack(0, [])
        return ret