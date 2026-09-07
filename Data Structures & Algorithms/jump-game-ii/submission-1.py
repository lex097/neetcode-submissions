class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0

        currIndex = len(nums) - 1

        p = 0

        while True:

            if nums[p] >= (currIndex - p):
                jumps = jumps + 1
                if p == 0:
                    return jumps
                currIndex = p
                p = 0
            else:
                p = p + 1
            

                
            