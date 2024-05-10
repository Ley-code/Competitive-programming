# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(sums):
            if sums==amount:
                return 0
            if sums>amount:
                return float('inf')  
            if sums in memo:
                return memo[sums]
            mina = float('inf')
            for c in coins:
                mina = min(dp(sums+c),mina)
            memo[sums] = mina+1
            return mina+1
        val = dp(0)
        if val!=float('inf'):
            return val
        return -1 