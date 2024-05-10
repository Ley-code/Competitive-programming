# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,buy):
            if i >= len(prices):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if buy:
                buying = dp(i+1,False) - prices[i]
                notbuying = dp(i+1,True)
                memo[(i,buy)] = max(buying,notbuying)
                return memo[(i,buy)]
            else:
                selling = dp(i+2,True) + prices[i]
                notselling = dp(i+1,False)
                memo[(i,buy)] = max(selling,notselling)
                return memo[(i,buy)]
        return dp(0,True)