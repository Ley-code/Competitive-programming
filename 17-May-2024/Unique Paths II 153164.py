# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=1:
                    if inbound(i-1,j):
                        dp[i][j] += dp[i-1][j] 
                    if inbound(i,j-1):
                        dp[i][j] += dp[i][j-1]
        if grid[0][0]==1 or grid[-1][-1] == 1:
            return 0
        else:
            return dp[-1][-1]

