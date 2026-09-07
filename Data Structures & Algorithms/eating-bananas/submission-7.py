class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search from 1 to max number of bananas

        #get max bananas
        maxPile = 0
        for i in piles:
            if i > maxPile:
                maxPile = i
        


        l, r = 1, maxPile

        #minimum rates[m] such that time of rates[m] < h
        while r >= l:
            m = (r + l) // 2
            time = 0
            for i in piles:
                if ((i % m) == 0):
                    time = time + (i // m)
                else:
                    time = time + (i // m) + 1
            if time <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res





