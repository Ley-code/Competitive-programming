# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        size = len(grid)-2

        ans = [[0] * size for _ in range(size)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i<size+1 and i>0 and j<size+1 and j>0:
                    maxnum = grid[i][j]
                    for dr,dc in directions:
                        maxnum = max(maxnum,grid[i+dr][j+dc])
                    ans[i-1][j-1] = maxnum
        return ans
