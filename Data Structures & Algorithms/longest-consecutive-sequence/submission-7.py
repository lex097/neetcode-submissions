class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        ret = 0
        count = 1
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                ret = max(ret, count)
                count = 1
        return max(ret, count)  # final update
