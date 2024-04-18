# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        l = 0
        heap = []
        heapq.heapify(heap)
        while l<len(heights)-1:
            if heights[l]>=heights[l+1]:
                l+=1
            else:
                diff = heights[l+1]-heights[l]
                bricks-= diff
                heapq.heappush(heap,-(diff))
                if bricks<0:
                    if ladders>0:
                        maxi = -heapq.heappop(heap)
                        bricks+=maxi
                        ladders-=1
                    else:
                        return l
                l+=1
        return l