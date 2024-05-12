# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [[e,s] for s,e in zip(speed,efficiency)]
        pairs.sort(reverse = True)
        minheap = []
        totspeed = 0
        maxP = 0
        for e,s in pairs:
            heapq.heappush(minheap, s)
            totspeed += s
            if len(minheap)>k:
                s = heapq.heappop(minheap)
                totspeed-= s
            if len(minheap)<=k:
                maxP = max(maxP,totspeed*e)
        return maxP%(10**9 + 7)