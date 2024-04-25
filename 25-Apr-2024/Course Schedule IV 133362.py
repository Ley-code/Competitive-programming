# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for pre,post in prerequisites:
            graph[pre].append(post)
        @cache
        def recurse(pre,target):
            if pre == target:
                return True
            for node in graph[pre]:
                if recurse(node,target):return True
            return False
        ans = []
        for pre,post in queries:
            if recurse(pre,post): 
                ans.append(True)
            else:
                ans.append(False)
        return ans
        
        
