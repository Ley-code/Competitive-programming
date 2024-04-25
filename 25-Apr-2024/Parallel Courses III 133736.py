# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = {i:0 for i in range(1,n+1)}
        for x,y in relations:
            graph[x].append(y)
            indegree[y]+=1
        maxtime = 0
        q = deque([[num,time[num-1]] for num in indegree if indegree[num]==0])
        timemap = {i:time[i-1] for i in range(1,n+1)}
        while q:
            num,month = q.popleft()
            maxtime = max(timemap[num],maxtime)
            for nei in graph[num]:
                indegree[nei]-=1
                if timemap[nei]<month+time[nei-1]:
                    timemap[nei]=month+time[nei-1]
                if indegree[nei]==0:
                    q.append([nei,timemap[nei]])
        return maxtime
            

