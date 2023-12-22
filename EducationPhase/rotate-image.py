class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        seencol = 0
        for i in range(rows):
            for j in range(seencol,cols):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            seencol+=1
        for k in range(rows):
            matrix[k] = matrix[k][::-1]