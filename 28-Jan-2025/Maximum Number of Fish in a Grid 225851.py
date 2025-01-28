# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        def inbound(r,c):
            return 0<=r<N and 0<=c<M
        directions= [(1,0),(-1,0),(0,1),(0,-1)]
        seen = set()
        def dfs(r,c):
            seen.add((r,c))
            sums = grid[r][c]
            for dr,dc in directions:
                newr,newc = dr+r,dc+c
                if (newr,newc) in seen or not inbound(newr,newc) or grid[newr][newc] == 0:
                    continue
                sums += dfs(newr,newc)
            return sums
        maxi = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j]!= 0:
                    maxi = max(maxi,dfs(i,j))
        return maxi
