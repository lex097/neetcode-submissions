class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = max(nums)
        currMin, currMax = 1, 1
        for n in nums:
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            ret = max(ret, currMax)
        return ret