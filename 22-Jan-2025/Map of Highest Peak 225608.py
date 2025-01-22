# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        N = len(isWater)
        M = len(isWater[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        queue = deque([])
        def inbound(row,cols):
            return 0<=row<N and 0<=cols<M
        
        for i in range(N):
            for j in range(M):
                if isWater[i][j] == 1:
                    for dr,dc in directions:
                        newr,newc = dr+i,dc+j
                        if inbound(newr,newc) and (newr,newc) not in visited:
                            queue.append((newr,newc))
                    isWater[i][j] = 0
                    visited.add((i,j))
    
        while queue:
            r,c = queue.popleft()
            if (r,c) in visited:
                continue
            visited.add((r,c))
            mini = float('inf')
            for dr,dc in directions:
                newr,newc = dr+r,dc+c
                if inbound(newr,newc):
                    if (newr,newc) in visited:
                        mini = min(mini,isWater[newr][newc])
                    queue.append((newr,newc))

            isWater[r][c] = mini + 1
        return isWater
                
                
