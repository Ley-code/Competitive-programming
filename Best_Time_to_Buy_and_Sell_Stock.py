class Solution(object):
    def maxProfit(self, prices):
        l = res = 0
        r = 1
        while r<len(prices):
            if prices[r] - prices[l] < 0:
                l=r
                r+=1
            else:
                res = max(prices[r]-prices[l],res)
                r+=1
        return res