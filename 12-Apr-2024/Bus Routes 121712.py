# Problem: Bus Routes - https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        n = len(routes)
        for i in range(n):
            for j in range(len(routes[i])):
                graph[routes[i][j]].append(i)
        visited = set()
        q = deque([graph[source]])
        level = 0
        if source==target:
            return 0
        while q:
            arr = q.popleft()
            buses = []
            for bus in arr:
                if bus not in visited:
                    visited.add(bus)
                    for route in routes[bus]:
                        if route==target:
                            return level+1
                        buses.extend(graph[route])
            if buses:
                q.append(list(set(buses)))
            level+=1
        return -1
