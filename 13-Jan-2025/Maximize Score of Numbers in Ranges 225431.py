# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def check(gap):
            point = start[0]
            for i in range(1,len(start)):
                if point+gap>= start[i] and point+gap<=start[i]+d:
                    point += gap
                elif point+gap<start[i]:
                    point = start[i]
                else:
                    return False
            return True
        low = 0
        high = start[-1]+d - start[0]
        while low<=high:
            mid = low + (high-low)//2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        return high