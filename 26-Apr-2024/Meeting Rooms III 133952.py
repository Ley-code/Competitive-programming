# Problem: Meeting Rooms III - https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        arr = [0]*n
        freeroom = [i for i in range(n)]
        minheap = [] #[endtime,room]
        
        for start,end  in meetings:
            while minheap and minheap[0][0]<=start:
                _ ,room = heapq.heappop(minheap)
                heapq.heappush(freeroom,room)
            if not freeroom:
                end_time,room = heapq.heappop(minheap)
                end = end_time +(end-start)
                heapq.heappush(freeroom,room)

            room = heapq.heappop(freeroom)
            heapq.heappush(minheap,(end,room))
            arr[room]+=1 
        maxnum,idx = -1,0
        for i,num in enumerate(arr):
            if num>maxnum:
                maxnum = num
                idx = i 
        return idx