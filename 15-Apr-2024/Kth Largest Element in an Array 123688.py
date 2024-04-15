# Problem: Kth Largest Element in an Array - https://leetcode.com/problems/kth-largest-element-in-an-array/description/

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]= -nums[i]
        heapify(nums)
        ans = None
        while k>0:
            ans = heappop(nums)
            k-=1
        return -ans