class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        zeroIndices = []
        product = 1
        for i in range(0, len(nums)):
            if (nums[i] == 0):
                zeroIndices.append(i)
                continue
            product = product * nums[i]
        for i in range(0, len(nums)):
            if (len(zeroIndices) > 1):
                ret.append(0)
                continue
            if (len(zeroIndices) == 1) and (nums[i] == 0):
                ret.append(product)
                continue
            if (len(zeroIndices) == 1) and not (nums[i] == 0):
                ret.append(0)
                continue
            ret.append(int(product / nums[i]))
        return ret