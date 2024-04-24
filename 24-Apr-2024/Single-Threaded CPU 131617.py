# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,task in enumerate(tasks):
            task.append(i)

        tasks.sort()
        heap = []
        l = 0
        time = tasks[0][0]
        ans = []
        while heap or l<len(tasks):
            while l<len(tasks) and tasks[l][0]<=time:
                heapq.heappush(heap,[tasks[l][1],tasks[l][2]])
                l+=1
            if not heap:
                time = tasks[l][0]
            else:
                end,idx = heapq.heappop(heap)
                time += end
                ans.append(idx)
        return ans    
        
