# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        n,m = len(matrix),len(matrix[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        for i in range(n):
            for j in range(m):
                for dr,dc in directions:
                    newr,newc = dr+i,dc+j
                    if inbound(newr,newc) and matrix[i][j]<matrix[newr][newc]:
                        graph[(i,j)].append((newr,newc))
                        indegree[(newr,newc)]+=1
                if indegree[(i,j)]:continue
                indegree[(i,j)] = 0
        q = deque([[num[0],num[1],1] for num in indegree if indegree[num]==0])
        maxdepth = 1
        while q:
            r,c,depth = q.popleft()
            maxdepth = max(maxdepth,depth)
            for nei in graph[(r,c)]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append([nei[0],nei[1],depth+1])

        return maxdepth