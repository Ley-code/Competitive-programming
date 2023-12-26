class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        incDiagonal = 0
        decDiagonal = 0

        for i in range(length):
            
            decDiagonal += mat[i][i]
            incDiagonal += mat[length-i-1][i]
        if length%2!=0:
            decDiagonal -= mat[(length//2)][(length//2)]
        return incDiagonal+decDiagonal

        