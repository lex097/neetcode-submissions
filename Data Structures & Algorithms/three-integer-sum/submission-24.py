class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(0, len(nums)):
            l, r = i + 1, len(nums) - 1
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            while l < r:
                target = -1 * nums[i]
                if (nums[l] + nums[r]) < target:
                    l = l +1
                    continue
                if (nums[l] + nums[r]) > target:
                    r = r - 1
                    continue
                else:
                    ret.append([nums[i], nums[l], nums[r]])
                    l = l+1
                    while (nums[l-1] == nums[l]) and (l < r):
                        l = l+1
        return ret