# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []        
        self.minsize = 0
        self.maxsize = 0
        heapify(self.minheap)
        heapify(self.maxheap)
    def addNum(self, num: int) -> None:
            if self.minsize == self.maxsize == 0:
                heappush(self.maxheap,-num)
                self.maxsize+=1
                return
            if self.minsize==self.maxsize:
                if num>= -self.maxheap[0]:
                    heappush(self.minheap,num)
                    self.minsize+=1
                else:
                    heappush(self.maxheap,-num)
                    self.maxsize+=1
            elif self.minsize>self.maxsize:
                if num>= -self.maxheap[0]:
                    heappush(self.minheap,num)
                    val = heappop(self.minheap)
                    heappush(self.maxheap,-val)
                else:
                    heappush(self.maxheap,-num)
                self.maxsize+=1
            else:
                if num>= -self.maxheap[0]:
                    heappush(self.minheap,num)
                else:
                    heappush(self.maxheap,-num)
                    val = heappop(self.maxheap)
                    heappush(self.minheap,-val)
                self.minsize+=1
    def findMedian(self) -> float:
        if self.minsize>self.maxsize:
            return self.minheap[0]
        elif self.minsize<self.maxsize:
            return -self.maxheap[0]
        return (self.minheap[0]-self.maxheap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()