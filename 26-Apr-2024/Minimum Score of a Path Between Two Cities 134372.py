# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
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
        mini = float('inf')
        for i in range(len(roads)):
            union(roads[i][0],roads[i][1])
        parent = find(1)
        for x,y,dist in roads:
            if find(x)==parent or find(y)==parent:
                mini = min(mini,dist)
        return mini   


