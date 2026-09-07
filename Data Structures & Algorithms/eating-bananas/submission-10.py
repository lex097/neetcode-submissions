class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxBananas = 0
        for i in piles:
            if i > maxBananas:
                maxBananas = i
        l, r = 1, maxBananas
        while r >= l:
            rate = (r + l) // 2
            time = 0
            for i in piles:
                time = time + (math.ceil(i / rate))
            if time > h:
                l = rate + 1
            elif time <= h:
                ret = rate
                r = rate - 1
        return ret