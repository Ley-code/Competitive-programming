class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowlen = len(board)
        collen = len(board[0])
        seen = set()
        def backtrack(r,c,idx):
            if idx==len(word):
                return True
            if (r>=rowlen or c>=collen or r<0 or c<0 or board[r][c]!=word[idx] or (r,c) in seen):
                return False
            seen.add((r,c))
            resD = backtrack(r+1,c,idx+1)
            resU = backtrack(r-1,c,idx+1)
            resL = backtrack(r,c-1,idx+1)
            resR = backtrack(r,c+1,idx+1)
            seen.remove((r,c))
            if resD or resU or resL or resR:
                return True
        for r in range(rowlen):
            for c in range(collen):
                if backtrack(r,c,0): return True

        return False