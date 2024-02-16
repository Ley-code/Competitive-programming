class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = {}
        col = {}
        maxsum = 0
        for i in range(len(grid)):
            row[i] = max(grid[i])
        for j in range(len(grid[0])):
            currmax = 0
            for i in range(len(grid)):
                currmax = max(grid[i][j],currmax)
            col[j] = currmax
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxsum+=min(row[i],col[j])-grid[i][j]
        return maxsum
        