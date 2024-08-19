# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
        memo = {}
        def dp(current,copied):
            if current==n:
                return 0
            if current>n:
                return float('inf')
            if (current,copied) in memo:
                return memo[(current,copied)]
            memo[(current,copied)] = min(dp(2*current,current)+2,dp(current+copied,copied)+1)
            return memo[(current,copied)]
        return dp(1,1)+1
