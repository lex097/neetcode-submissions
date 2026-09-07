class Solution:
    def climbStairs(self, n: int) -> int:
        s1 = 1
        s2 = 1
        for i in range(n - 1):
            temp = s2
            s2 = s2 + s1
            s1 = temp
        return s2