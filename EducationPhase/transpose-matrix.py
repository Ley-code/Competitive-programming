class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = len(matrix[0])
        row = len(matrix)
        ans = [[0]*row for _ in range(col)]
        for row_idx in range(row):
            for col_idx in range(col):
                ans[col_idx][row_idx] = matrix[row_idx][col_idx]
        return ans