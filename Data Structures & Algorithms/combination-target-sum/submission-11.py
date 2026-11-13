class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = []

        def backtrack(i, curr, currComb):
            if (curr == target):
                self.ret.append(currComb[:])
                return

            if (i >= len(nums) or curr > target):
                return
            
            currComb.append(nums[i])
            backtrack(i, curr + nums[i], currComb)
            currComb.pop()

            backtrack(i + 1, curr, currComb)
            return
        backtrack(0, 0, [])

        return self.ret