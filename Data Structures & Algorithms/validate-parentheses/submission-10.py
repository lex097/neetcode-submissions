class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        myMap = {')' : '(', '}' : '{', ']': '['}
        if len(s) % 2 == 1:
            return False
        for i in range(0, len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                continue
            if len(stack) == 0:
                return False
            if stack[-1] != myMap[s[i]]:
                return False
            else:
                stack.pop()
        if len(stack) != 0:
            return False
        return True

