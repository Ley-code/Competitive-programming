# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1,n2 in edges:
            if graph[n1]:
                return n1
            if graph[n2]:
                return n2
            graph[n1].append(n2)
            graph[n2].append(n1)
        return -1