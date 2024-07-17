# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low,high = 1,position[-1]-position[0]
        
        def check(value):
            lastpos = position[0]
            balls = 1
            for i in range(1,len(position)):
                if position[i]-lastpos>=value:
                    lastpos = position[i]
                    balls+=1
            return balls
        while low<=high:
            mid = low+(high-low)//2
            if check(mid)<m:
                high = mid-1
            else:
                low = mid+1
        return low-1

            