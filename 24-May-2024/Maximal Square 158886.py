# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m+1) for _ in range(n+1)]
        maxi = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])+1
                    maxi = max(maxi,dp[i][j]*dp[i][j])    
        return maxi
