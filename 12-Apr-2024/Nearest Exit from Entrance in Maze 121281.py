# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        n = len(maze)
        m = len(maze[0])
        q = deque([[entrance[0],entrance[1],0]])
        while q:
            r,c, depth = q.popleft()
            if (r==0 or r==n-1 or c==0 or c==m-1) and (r,c)!=(entrance[0],entrance[1]):
                return depth
            for dr,dc in directions:
                newr,newc = dr+r,dc+c            
                if 0<=newr<n and 0<=newc<m and maze[newr][newc]!="+":
                    q.append([newr,newc,depth+1])
                    maze[newr][newc] = "+"
        return -1