# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(l,r,turn):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            if turn:
                memo[(l,r)] = max(dp(l+1,r, not turn)+piles[l],dp(l,r-1,not turn)+piles[r])
                return memo[(l,r)]
            else:
                return dp(l+1,r,not turn)
                return dp(l,r-1,not turn)

        maxpoints = dp(0,len(piles)-1,True)
        return maxpoints>sum(piles)-maxpoints
        