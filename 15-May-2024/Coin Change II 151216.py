# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(i,sums):
            if i==len(coins) or sums>amount:
                return 0
            if sums==amount:
                return 1
            if (i,sums) not in memo:
                memo[(i,sums)] = dp(i,sums+coins[i]) + dp(i+1,sums)
            return memo[(i,sums)]
        memo = {}
        return dp(0,0)