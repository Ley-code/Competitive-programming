# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class UnionFind:
    def __init__(self, s1,s2,basestr):
        self.root = {}
        for c in s1:
            self.root[c]= c
        for c in s2:
            self.root[c] = c
        for c in basestr:
            self.root[c] = c
    def find(self, x):
        if x==self.root[x]:
            return x
        self.root[x]= self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if rootX < rootY:
                self.root[rootY] = rootX
            else:
                self.root[rootX] = rootY
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(s1,s2,baseStr)
        for i in range(len(s1)):
            uf.union(s1[i],s2[i])
        ans = ""
        for c in baseStr:
            ans+= uf.find(c)
        return ans