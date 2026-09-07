class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = set()
        j = 0
        k = len(nums) - 1
        for i in range(0, len(nums)):
            target = -1 * nums[i]
            j = i + 1
            k = len(nums) - 1 
            while (j < k):
                if i == j:
                    i = i+1
                    continue
                if i == k:
                    k = k-1
                    continue
                if (nums[j] + nums[k]) > target:
                    k = k-1
                    continue
                if (nums[j] + nums[k]) < target:
                    j = j+1
                    continue
                if (nums[j] + nums[k]) == target:
                    ret.add((nums[i], nums[j], nums[k]))
                    j = j + 1
    
        return [list(t) for t in ret]  # convert back to list
