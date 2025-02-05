# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prev = [intervals[0][0],intervals[0][1]]
        res = []
        for i in range(1,len(intervals)):
            if intervals[i][0]<= prev[1]:
                prev[1] = max(prev[1],intervals[i][1])
            else:
                res.append(prev)
                prev = [intervals[i][0],intervals[i][1]]
        
        res.append(prev)
        return res
