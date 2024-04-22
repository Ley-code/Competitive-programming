# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = {i:0 for i in range(len(graph))}
        for i in range(len(graph)):
            for num in graph[i]:
                adj[num].append(i)
                indegree[i]+=1
        q = deque([num for num in indegree if indegree[num]==0])
        ans = []
        while q:
            num = q.popleft()
            ans.append(num)
            for nei in adj[num]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return sorted(ans)
