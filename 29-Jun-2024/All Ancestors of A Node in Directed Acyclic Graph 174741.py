# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indeg = {i:0 for i in range(n)}
        for x,y in edges:
            graph[x].append(y)
            indeg[y]+=1
        ancest = [set() for i in range(n)]
        q = deque([num for num in indeg if indeg[num]==0])
        while q:
            num = q.popleft()
            for nei in graph[num]:
                ancest[nei].update(ancest[num])
                ancest[nei].add(num)
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        return [sorted(nums) for nums in ancest]
