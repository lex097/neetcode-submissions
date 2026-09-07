class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r = r + 1
            else:
                profit = prices[r] - prices[l]
                ret = max(profit, ret)
                r = r+1
        return ret
