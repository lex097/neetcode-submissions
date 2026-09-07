class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        curr = 1 << 31
        for i in range(32):
            if (n % 2 == 1):
                ret += curr
                print(curr)
            curr = curr >> 1
            n = n >> 1
        return ret
