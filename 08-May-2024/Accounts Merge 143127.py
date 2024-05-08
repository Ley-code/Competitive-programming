# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size+1)]
        self.rank = [1] * (size+1)
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
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailtoacc = {}
        for i,acc in enumerate(accounts):
            for e in acc[1:]:
                if e in emailtoacc:
                    uf.union(i,emailtoacc[e])
                else:
                    emailtoacc[e] = i
        emailgroup = defaultdict(list)
        for e,i in emailtoacc.items():
            par = uf.find(i)
            emailgroup[par].append(e)
        res = []
        for i,e in emailgroup.items():
            res.append([accounts[i][0]]+sorted(emailgroup[i]))
        return res
        