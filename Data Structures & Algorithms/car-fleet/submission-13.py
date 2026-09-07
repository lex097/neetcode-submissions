class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ret = 0
        times = []
        stack = []
        sortedPos = sorted(position, reverse = True)
        myMap = {}
        for i in range(0, len(position)):
            myMap[position[i]] = speed[i]
        for i in range(0, len(sortedPos)):
            times.append(float((target - sortedPos[i]) / (myMap[sortedPos[i]])))
        for t in times:
            if not stack:
                stack.append(t)
                continue
            if t > stack[-1]:
                stack.append(t)
                ret = ret + 1
        return ret + 1
