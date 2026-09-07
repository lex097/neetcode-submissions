class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]
                    
    def partition(self, s: str) -> List[List[str]]:
        self.ret = []

        def backtrack(start, e, combo):
            if e >= len(s):
                if (start == len(s)):
                    self.ret.append(combo[:])
                return
            
            if self.isPalindrome(s[start:e+1]):
                combo.append(s[start:e+1])
                backtrack(e+1,e+1,combo)
                combo.pop()
            
            backtrack(start, e+1, combo)
            return
        backtrack(0,0,[])
        return self.ret
            