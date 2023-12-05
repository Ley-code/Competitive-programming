class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        playerescapeDistance = abs(target[0]) + abs(target[1])
        for i in range(len(ghosts)):
            ghostDistance = abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1])
            if playerescapeDistance >= ghostDistance:
                return False
        return True