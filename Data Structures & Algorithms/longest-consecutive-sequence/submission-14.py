class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 1
        maxCount = 0
        if not nums:
            return 0
        for i in nums:
            if (i - 1) not in nums:
                k = 1
                while ((i + k) in nums):
                    count = count + 1
                    k = k + 1
                maxCount = max(count, maxCount)
                count = 1
        return maxCount


