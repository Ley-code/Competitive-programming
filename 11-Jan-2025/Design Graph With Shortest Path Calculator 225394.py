# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for f,t,w in edges:
            self.graph[f].append([t,w])
        

    def addEdge(self, edge: List[int]) -> None:
        f,t,w = edge
        self.graph[f].append([t,w])

    def shortestPath(self, node1: int, node2: int) -> int:
        distances = defaultdict(lambda: float('inf'))
        distances[node1] = 0
        heap = [(0,node1)]
        processed = set()
        while heap:
            dist,curr = heapq.heappop(heap)
            if curr in processed:
                continue
            processed.add(curr)
            if curr==node2:
                return dist
            for child,weight in self.graph[curr]:
                if dist+weight<distances[child]:
                    distances[child] = dist+weight  
                    heapq.heappush(heap,(dist+weight,child))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)