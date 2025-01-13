# Problem: Maximum Number of Points with Cost - https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])
        dp = [[0] * m for _ in range(n)]
        for j in range(m):
            dp[0][j] = points[0][j]
        print(dp)
        for i in range(1,n):
            left = [0]*m
            right = [0]*m
            for j in range(m):
                if j==0:
                    left[j] = dp[i-1][j]
                else:
                    left[j] = max(dp[i-1][j],left[j-1]-1)    
            for j in range(m-1,-1,-1):
                if j==m-1:
                    right[j] = dp[i-1][j]
                else:
                    right[j] = max(dp[i-1][j],right[j+1]-1)    
            for j in range(m):
                dp[i][j] = points[i][j] + max(left[j],right[j])
        return max(dp[n-1])
