class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = nums[0]

        curr = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > curr + nums[i]:
                curr = 0
            curr = curr + nums[i]
            ret = max(ret, curr)
        
        return ret



