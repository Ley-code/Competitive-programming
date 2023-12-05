class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        totaltime = 0
        for i in range(len(points)-1):
            x1value,x2value = points[i][0],points[i+1][0]
            y1value,y2value = points[i][1],points[i+1][1]
            distancex = abs(x2value - x1value)
            distancey = abs(y2value - y1value)

            if distancex < distancey:
                totaltime+=distancex
                totaltime+=distancey-distancex
            elif distancex==distancey:
                totaltime+=distancex
            else:
                totaltime+=distancey
                totaltime+=distancex-distancey
        return totaltime
            
                
