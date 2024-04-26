# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * (size)
    def find(self, x):
        if x==self.root[x]:
            return x
        self.root[x]= self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += 1
            return True
        return False
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        uf = UnionFind(n)
        costs  = []
        for i in range(n):
            for j in range(i+1,n):
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                costs.append((distance,i,j))
        costs.sort()
        total = 0
        for dist,p1,p2 in costs:
            if uf.union(p1,p2):
                total+=dist
        return total
            
