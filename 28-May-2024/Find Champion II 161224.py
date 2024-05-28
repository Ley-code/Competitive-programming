# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = defaultdict(int)
        for edge in edges:
            u,v = edge
            indegree[v] += 1
        val = None
        for i in range(n):
            if indegree[i] == 0:
                if val==None:
                    val = i
                else:
                    return -1
        return val
