class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        colset = defaultdict(set)
        rowset = defaultdict(set)
        cellset = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    colset[j].add(board[i][j])
                    rowset[i].add(board[i][j])
                    cellset[(i//3,j//3)].add(board[i][j])
        flag = False
        def backtrack(r,c):
            nonlocal flag
            if r==9:
                flag = True
                return
            if board[r][c].isdigit():
                if c<8 and r<=8:
                    backtrack(r,c+1)
                elif c==8 and r<=8:
                    backtrack(r+1,c-8)
            else:
                for num in range(1,10):
                    if str(num) in rowset[r] or str(num) in colset[c] or str(num) in cellset[(r//3,c//3)]:
                        continue
                    board[r][c] = str(num)
                    cellset[(r//3,c//3)].add(str(num))
                    rowset[r].add(str(num))
                    colset[c].add(str(num))
                    
                    if c<8 and r<=8:
                        backtrack(r,c+1)
                    elif c==8 and r<=8:
                        backtrack(r+1,c-8)
                    if not flag:
                        cellset[(r//3,c//3)].remove(board[r][c])
                        rowset[r].remove(board[r][c])
                        colset[c].remove(board[r][c])
                        board[r][c] = "."
        backtrack(0,0)
        return board