# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[float('inf')]*(m+1) for _ in range(n)]
        dp[n-1][m-1] = grid[n-1][m-1]
        for j in range(m-2,-1,-1):
            dp[n-1][j] = dp[n-1][j+1] + grid[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(m-1,-1,-1):
                dp[i][j] = min(dp[i+1][j],dp[i][j+1]) + grid[i][j]
        return dp[0][0]