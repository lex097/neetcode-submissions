class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        leftSideProducts = []
        leftProd = 1
        rightSideProducts = []
        rightProd = 1
        for i in range(0, len(nums)):
            leftSideProducts.append(leftProd * nums[i])
            leftProd = leftProd * nums[i]
            rightSideProducts.append(rightProd * nums[len(nums) - i - 1])
            rightProd = rightProd * nums[len(nums) - i - 1]
        for i in range(0, len(nums)):
            if (i == 0):
                ret.append(rightSideProducts[len(nums) - 2])
                continue
            if (i == len(nums) - 1):
                ret.append(leftSideProducts[len(nums) - 2])
                continue
            ret.append(leftSideProducts[i-1] * rightSideProducts[len(nums) - i - 2])   
        return ret