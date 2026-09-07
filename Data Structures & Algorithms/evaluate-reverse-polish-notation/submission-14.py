class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ret = 0
        stack = []
        operators = {"+", "*", "-", "/"}
        for i in tokens:
            if i not in operators:
                i = int(i)
                stack.append(i)
                ret = i
                continue
            
            elif i == "+":
                ret = stack[-1] + stack[-2]
                stack.pop()
                stack.pop()
                stack.append(ret)
            elif i == "-":
                ret = (stack[-2] - stack[-1])
                stack.pop()
                stack.pop()
                stack.append(ret)
            elif i == "*":
                ret = (stack[-2] * stack[-1])
                stack.pop()
                stack.pop()
                stack.append(ret)
            elif i == "/":
                ret = (int(stack[-2] / stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(ret)
        return ret