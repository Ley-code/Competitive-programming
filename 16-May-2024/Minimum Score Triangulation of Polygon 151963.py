# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        memo = {}
        def dp(i, j):
            if i+1 == j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            m = float('inf')
            for k in range(i+1, j):
                m = min(m, values[i]*values[j]*values[k] + dp(i, k) + dp(k, j))
            memo[(i,j)] = m
            return memo[(i,j)]
        n = len(values)
        return dp(0, n-1)