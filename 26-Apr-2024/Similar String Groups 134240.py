# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        root = [i for i in range(n)]
        rank = [1] * (n)
        def find(x):
            if x==root[x]:
                return x
            root[x] = find(root[x])
            return root[x]
        def union( x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                else:
                    root[rootX] = rootY
                    rank[rootY] += 1
        for i in range(n):
            for j in range(i+1,n):
                l = 0
                letter = []
                diff = 0
                while l<m:
                    if strs[i][l] != strs[j][l]:
                        letter.append([strs[i][l],strs[j][l]])
                        diff +=1
                    l+=1
                if diff==0 or (diff==2 and letter[0][0]==letter[1][1] and letter[0][1]==letter[1][0]):
                    union(i,j)
        return len({find(x) for x in range(n)})