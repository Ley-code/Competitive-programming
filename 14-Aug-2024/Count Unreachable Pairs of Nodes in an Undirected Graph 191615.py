# Problem: Count Unreachable Pairs of Nodes in an Undirected Graph - https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, rank):
        self.root = [i for i in range(rank)]
        self.rank = [1] * rank
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.root[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for a,b in edges:
            uf.union(a,b)
        for i in range(n):
            uf.find(i)
        counts = Counter(uf.root)
        values = list(counts.values())
        res = 0
        totsum = sum(values)
        for i in range(len(values)-1):
            totsum-=values[i]
            res += values[i]*totsum
        return res
        