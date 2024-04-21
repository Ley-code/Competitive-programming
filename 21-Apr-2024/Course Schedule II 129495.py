# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for nex,pre in prerequisites:
            graph[pre].append(nex)
        WHITE = 0
        GRAY = 1
        BLACK = 2
        color = [WHITE]*numCourses
        stack = []
        flag = False
        def dfs(node):
            if color[node]== GRAY:
                return False
            color[node] = GRAY
            for neigh in graph[node]:
                if color[neigh]==BLACK:
                    continue
                if not dfs(neigh): return False
            color[node] = BLACK
            stack.append(node)
            return True
        for i in range(numCourses):
            if color[i]==WHITE:
                if not dfs(i): return []
        return stack[::-1]