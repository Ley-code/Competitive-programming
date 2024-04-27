# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root = [i for i in range(n)]
        rank = [1] * (n)
        characters = {i:[s[i]] for i in range(n)}
        def find( x):
            if x==root[x]:
                return x
            root[x]= find(root[x])
            return root[x]
        def union( x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    root[rootY] = rootX
                    p,c = rootX,rootY
                elif rank[rootX] < rank[rootY]:
                    root[rootX] = rootY
                    p,c = rootY,rootX
                else:
                    root[rootX] = rootY
                    rank[rootY] += 1
                    p,c = rootY,rootX
                characters[p] += characters[c]
                
        ans = ""
        for x,y in pairs:
            union(x,y)
        
        for char in characters:
            characters[char].sort(reverse = True)
        for i in range(n):
            ans+=characters[find(i)].pop()
        return ans
