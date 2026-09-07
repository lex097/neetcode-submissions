class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        numberMap = {
            2 : ["a", "b", "c"], 
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"],
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"],
            7 : ["p", "q", "r", "s"],
            8 : ["t", "u", "v"],
            9 : ["w", "x", "y", "z"]
            }
        self.ret = []
        def backtrack(index, combo):
            if index == len(digits):
                self.ret.append("".join(combo))
                return
            for char in numberMap[int(digits[index])]:
                combo.append(char)
                backtrack(index + 1, combo)
                combo.pop()
            return
        backtrack(0, [])
        return self.ret