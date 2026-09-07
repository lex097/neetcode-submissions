class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        ret = 0
        count = 1
        for i in range(0, len(nums) - 1):
            if (nums[i+1] - nums[i]) == 1:
                count = count + 1
                continue
            if ret < count:
                ret = count
            count = 1
        return max(ret, count)