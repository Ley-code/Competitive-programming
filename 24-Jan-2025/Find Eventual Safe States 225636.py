# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(len(graph))}
        newgraph = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                indegree[i] += 1
                newgraph[graph[i][j]].append(i)
        
        queue = deque([])
        for num in indegree:
            if indegree[num] == 0:
                queue.append(num)

        ans = []
        while queue:
            num = queue.popleft()
            ans.append(num)
            for neighbor in newgraph[num]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        ans.sort()
        return ans