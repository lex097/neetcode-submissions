class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index, combo, comboSum):
            if comboSum == target:
                res.append(combo[:])
                return
            if (index >= len(candidates)) or (comboSum > target):
                return
            
            combo.append(candidates[index])
            backtrack(index + 1, combo, comboSum + candidates[index])
            combo.pop()

            while (index < len(candidates) - 1) and (candidates[index] == candidates[index+1]):
                index = index + 1
            backtrack(index + 1, combo, comboSum)
            return
        backtrack(0, [], 0)
        return res