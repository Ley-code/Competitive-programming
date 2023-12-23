class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0,0):1}
        startpos = [0,0]
        for i in range(len(path)):
            if path[i] == "N":
                startpos[1] +=1
            elif path[i] == "E":
                startpos[0] +=1
            elif path[i] == "S":
                startpos[1] -=1
            else:
                startpos[0] -=1
            if tuple(startpos) in visited:
                return True
            visited[tuple(startpos)] = 1 
        return False