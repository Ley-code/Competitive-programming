# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        n,m = len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    rows.add(i)
                    cols.add(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        return

        