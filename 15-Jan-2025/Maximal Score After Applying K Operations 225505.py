# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        totscore = 0
        while k>0:
            curr = heapq.heappop(heap)
            totscore += -curr
            heapq.heappush(heap,-ceil(-curr/3))
            k-=1
        return totscore
