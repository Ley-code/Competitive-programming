# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        miniarr = sorted(zip(capital,profits))
        maxheap = []
        l = 0
        while k>0:
            while l<len(profits) and miniarr[l][0]<=w:
                heapq.heappush(maxheap, -miniarr[l][1])
                l+=1
            if not maxheap:
                break
            w += -heapq.heappop(maxheap)
            k-=1
        return w