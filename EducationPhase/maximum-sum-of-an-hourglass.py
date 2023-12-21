class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxsum = 0
        for down in range(rows-2):
            for right in range(cols-2):
                uppersum = sum(grid[down][right:right+3])
                middle = grid[down+1][right+1]
                lowersum = sum(grid[down+2][right:right+3])
                maxsum = max(maxsum,uppersum+middle+lowersum)
        return maxsum
