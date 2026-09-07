class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ret = []

        def backtrack(openN, closeN, combo):
            if (len(combo) == 2*n):
                self.ret.append("".join(combo))
                return
            
            if openN < n:
                combo.append("(")
                backtrack(openN + 1, closeN, combo)
                combo.pop()

            if closeN < openN:
                combo.append(")")
                backtrack(openN, closeN + 1, combo)
                combo.pop()
        backtrack(0,0,[])
        return self.ret
            