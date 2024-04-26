# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(grid1)
        m = len(grid1[0])
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        def dfs(r,c):
            nonlocal is_subisland
            if grid1[r][c]==0:
                is_subisland = False
            grid2[r][c]=0
            for dr,dc in directions:
                newr,newc = r+dr,c+dc
                if inbound(newr,newc) and grid2[newr][newc]==1:
                    dfs(newr,newc)
        ncount = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1:
                    is_subisland = True
                    dfs(i,j)
                    if is_subisland:
                        ncount+=1
        return ncount