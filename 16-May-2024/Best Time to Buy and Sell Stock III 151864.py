# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,buy,cnt):
            if i==len(prices) or cnt>2:
                return 0
            if(i,buy,cnt) in memo:
                return memo[(i,buy,cnt)]
            if buy:
                take = dp(i+1,not buy,cnt+1)-prices[i]
                notake = dp(i+1 , buy,cnt)
                memo[(i,buy,cnt)] =  max(take,notake)
                return memo[(i,buy,cnt)]
            else:
                sell = dp(i+1,not buy,cnt) + prices[i]
                notsell = dp(i+1,buy,cnt)
                memo[(i,buy,cnt)] = max(sell,notsell)
                return memo[(i,buy,cnt)]
                 
        return dp(0,True,0)