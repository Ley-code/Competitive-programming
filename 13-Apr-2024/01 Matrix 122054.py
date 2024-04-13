# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque([])
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append((i,j,0))
                else:
                    mat[i][j]="N"
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c,depth = q.popleft()
            for dr,dc in directions:
                newr,newc = dr+r,dc+c
                if 0<=newr<n and 0<=newc<m and mat[newr][newc]=="N":
                    mat[newr][newc]= depth+1
                    q.append((newr,newc,depth+1))
        return mat
        