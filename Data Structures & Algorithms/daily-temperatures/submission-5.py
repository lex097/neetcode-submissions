class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ret = [0] * len(temperatures)
        stack = [] # pair [temp, index]
        for i in range(0, len(temperatures)):
            if not stack:
                stack.append([temperatures[i], i])
                continue
            while stack and (stack[-1][0] < temperatures[i]):
                ret[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append([temperatures[i], i])
        return ret