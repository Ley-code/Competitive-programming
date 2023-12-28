class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    res = res + [(num,i),(j,num),(i//3,j//3,num)]
        return len(res) == len(set(res))