class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ret = nums[0]
        while r >= l:
            if nums[l] < nums[r]:
                ret = min(ret, nums[l])
                break
            m = (r + l) // 2
            ret = min(ret, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return ret