# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        lookup = {}
        for i,stone in enumerate(stones):
            lookup[stone]  = i
        memo = {}
        def dp(i,last):
            if i==n-1:
                return True
            if (i,last) in memo:
                return memo[(i,last)]
            for jump in [last+1,last,last-1]:
                if jump>0 and jump+stones[i] in lookup:
                    if dp(lookup[jump+stones[i]],jump):
                        memo[(i,last)] = True
                        return True
            memo[(i,last)] = False
            return False
        if stones[1]!=1:
            return False
        return dp(1,1)
