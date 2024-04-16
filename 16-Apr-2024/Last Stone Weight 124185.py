# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapify(stones)
        while len(stones)>=2:
            y,x = heappop(stones),heappop(stones)
            y = -y
            x = -x
            print(x,y)
            if x!=y:
                heappush(stones,-abs(x-y))
        return -stones[0] if stones else 0
