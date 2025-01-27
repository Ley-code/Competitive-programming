# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = {i:0 for i in range(numCourses)}

        for pre,post in prerequisites:
            graph[pre].append(post)
            indegree[post] += 1

        queue = deque([])
        for num in indegree:
            if indegree[num] == 0:
                queue.append(num)
        
        premap = defaultdict(set)

        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                premap[neighbor].add(curr)
                premap[neighbor].update(premap[curr])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        ans = []
        
        for u,v in queries:
            if u in premap[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        
        
