# [1, 2, 0, 2, 1, 0]

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        startIndex = len(nums) - 1
        ret = False
        currIndex = startIndex
        dist = 1


        for i in range(startIndex - 1, -1, -1):
            if nums[i] >= dist:
                if i == 0:
                    return True
                currIndex = i
                dist = 0
            
            dist = dist + 1

        return False