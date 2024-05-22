# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[float('inf')]*(m+1) for _ in range(n+1)]
        if dungeon[n-1][m-1]>=0:
            dp[n-1][m-1]=1
        else:
            dp[n-1][m-1] = -dungeon[n-1][m-1] + 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i==n-1 and j==m-1:
                    continue
                minihealth = min(dp[i][j+1],dp[i+1][j])
                if dungeon[i][j]<0:
                    dp[i][j] = minihealth - dungeon[i][j]
                else:
                    if minihealth - dungeon[i][j] <1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = minihealth - dungeon[i][j]
        return dp[0][0]