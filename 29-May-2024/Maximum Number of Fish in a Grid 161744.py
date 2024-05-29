# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class UnionFind:
    def __init__(self, size,grid):
        self.root = [i for i in range(size+1)]
        self.rank = [1] * (size+1)
        self.sums = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                oned = i*len(grid[0])+j
                self.sums[oned] = grid[i][j]
        print(self.sums)
    def find(self, x):
        if x==self.root[x]:
            return x
        self.root[x]= self.find(self.root[x])
        return self.root[x]
    def union(self, x, y,grid,m):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.sums[rootX] += self.sums[rootY]
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
                self.sums[rootY] += self.sums[rootX]
            else:
                self.root[rootX] = rootY
                self.sums[rootY] += self.sums[rootX]
                self.rank[rootY] += 1
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)
        uf = UnionFind(m*n,grid)
        visited = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        def dfs(r,c):
            onedX = r*m + c
            visited.add((r,c))
            for dr,dc in directions:
                newr,newc = r+dr,c+dc
                if inbound(newr,newc) and grid[newr][newc]!=0 and (newr,newc) not in visited:
                    onedY = newr*m + newc
                    uf.union(onedX,onedY,grid,m)
                    dfs(newr,newc)
        for i in range(n):
            for j in range(m):
                if grid[i][j] and (i,j) not in visited:
                    dfs(i,j)
        print(uf.sums)
        print(uf.root)
        return max(list(uf.sums.values()))
        
        