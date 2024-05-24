# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0] * i  for i in range(1,n+1)]
        dp[-1] = triangle[-1]
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                print(i,j)
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        return dp[0][0]