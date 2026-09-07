class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        used = set()

        def backtrack(permutation):
            if len(permutation) == len(nums):
                ret.append(permutation[:])
                return
            
            for i in range(0, len(nums)):
                if i in used:
                    continue
                permutation.append(nums[i])
                used.add(i)
                backtrack(permutation)
                permutation.pop()
                used.remove(i)
            return
        backtrack([])
        return ret
