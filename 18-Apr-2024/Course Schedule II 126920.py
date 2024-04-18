# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = {x:0 for x in range(numCourses)}
        graph = defaultdict(list)
        for nex,pre in prerequisites:
            graph[pre].append(nex)
            degree[nex]+=1
        q = deque([x for x in degree if degree[x]==0])
        topsort = []
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                degree[neigh]-=1
                if degree[neigh]==0:
                    q.append(neigh)
            topsort.append(node)
        return topsort if len(topsort)==numCourses else []