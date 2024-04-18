# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        marked = set()
        n = len(board)
        m = len(board[0])
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(r,c):
            marked.add((r,c))
            for dr,dc in directions:
                newr,newc = r+dr,c+dc
                if inbound(newr,newc) and board[newr][newc]=="O" and (newr,newc) not in marked:
                    dfs(newr,newc)
        
        for i in range(n):
            for j in range(m):
                if board[i][j]=="X":continue
                if i==0:
                    dfs(0,j)
                elif i==n-1:
                    dfs(n-1,j)
                elif j==0:
                    dfs(i,0)
                elif j==m-1:
                    dfs(i,m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i,j) not in marked:
                    board[i][j] = "X"
        return board
        

            
        