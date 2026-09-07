class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        ret = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                ret = max(ret, (prices[r] - prices[l]))
                r = r + 1
            else:
                l = r
                r = r + 1
        return ret