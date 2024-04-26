# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        root = [i for i in range(n+1)]
        rank = [1] * (n+1)
        def find(x):
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX!=rootY:
                if rank[rootY]>rank[rootX]:
                    root[rootX] = rootY
                elif rank[rootY]<rank[rootX]:
                    root[rootY] = rootX
                else:
                    rank[rootX]+=1
                    root[rootY] = rootX
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i,j)
        return n-len({find(x) for x in range(n)})
