# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N = len(grid)
        M = len(grid[0])

        def inbound(row,col):
            return 0<=row<N and 0<=col<M

        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        
        def dfs(r,c):
            if grid[r][c] =="0":
                return
            grid[r][c] = "0"
            for dr,dc in directions:
                newr,newc = dr+r,dc+c
                if inbound(newr,newc) and grid[newr][newc] == "1":
                    dfs(newr,newc)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]!="0":
                    dfs(i,j)
                    ans+=1
        return ans
        
            