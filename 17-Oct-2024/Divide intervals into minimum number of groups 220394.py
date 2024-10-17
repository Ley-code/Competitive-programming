# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        maxGroup = 0
        currGroup = 0
        minheap = [] #(end)
        for start,end in intervals:
            currGroup+=1
            heapq.heappush(minheap,end)
            while minheap and start> minheap[0]:
                currGroup-=1
                heapq.heappop(minheap)
            maxGroup = max(maxGroup,currGroup)
        return maxGroup

            

