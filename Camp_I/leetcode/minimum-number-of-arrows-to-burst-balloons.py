class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        prev = -float('inf')
        shots = 0
        for start,end in points:
            if start>prev:
                shots+=1
                prev = end
        return shots
