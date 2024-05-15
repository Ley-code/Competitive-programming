# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {}
        def dp(i,sums):
            if i==n or sums==n:
                return 1
            if sums>n:
                return 0
            if (i,sums) not in memo:
                take = dp(i,sums+i) * i
                donttake = dp(i+1,sums)
                memo[(i,sums)] = max(take,donttake)
            return memo[(i,sums)]
        return dp(1,0)