# Problem: Minimum Height Trees  - https://leetcode.com/problems/minimum-height-trees/description/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph  = defaultdict(list)
        indegree = {i:0 for i in range(n)}
        for src,dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)
            indegree[src]+=1
            indegree[dest]+=1
        q = deque([node for node in indegree if indegree[node]==1])
        while q:
            if n<=2:
                return list(q)
            for i in range(len(q)):
                node = q.popleft()
                n-=1
                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei]==1:
                        q.append(nei)
        return [0]
            