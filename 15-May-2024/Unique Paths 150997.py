# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(row,col):
            return 0<=row<m and 0<=col<n
        def dp(i,j):
            if i==m-1 and j==n-1:
                return 1
            if not inbound(i,j):
                return 0
            if (i,j) not in memo:
                memo[(i,j)] = dp(i+1,j) + dp(i,j+1)
            return memo[(i,j)]
        memo = {}
        return dp(0,0)