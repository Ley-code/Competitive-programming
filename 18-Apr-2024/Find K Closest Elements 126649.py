# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        for i in range(len(arr)):
            heapq.heappush(diff,(abs(arr[i]-x),i))
        ans = []
        while k>0:
            val,idx = heapq.heappop(diff)
            ans.append(arr[idx])
            k-=1
        ans.sort()
        return ans
