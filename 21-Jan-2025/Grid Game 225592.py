# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        res = float('inf')
        N = len(grid[0])
        for i in range(1,N):
            grid[0][i] += grid[0][i-1]
            grid[1][i] += grid[1][i-1]
        for j in range(N):
            top = grid[0][-1] - grid[0][j]
            bottom = None
            if j>0:
                bottom = grid[1][j-1]
            else:
                bottom = 0
            secondrobot = max(top,bottom)
            res= min(res,secondrobot)
        return res