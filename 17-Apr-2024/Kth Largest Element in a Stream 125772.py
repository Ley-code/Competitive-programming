# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        heapify(self.heap)
        self.k = k
        for i in range(k,len(nums)):
            if nums[i]>self.heap[0]:
                heapreplace(self.heap,nums[i])
    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            heappush(self.heap,val)
        elif val>self.heap[0]:
            heapreplace(self.heap,val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)