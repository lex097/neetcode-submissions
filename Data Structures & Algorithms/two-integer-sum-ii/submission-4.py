class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        k = len(numbers) - 1
        ret = []
        while (numbers[i] + numbers[k] != target):
            if (numbers[i] + numbers[k]) < target:
                i = i + 1
                continue
            if (numbers[i] + numbers[k]) > target:
                k = k-1
                continue
        ret = [i + 1, k + 1]
        return ret