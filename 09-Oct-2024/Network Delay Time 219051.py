# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for source,dest,weight in times:
            graph[source].append((dest,weight))
        
        distances = {node:float('inf') for node in range(1,n+1)}
        distances[k] = 0
        heap = [(0,k)]
        while heap:
            dist, node = heapq.heappop(heap)
            
            for neighbor,weight in graph[node]:
                if dist + weight< distances[neighbor]:
                    distances[neighbor] = dist + weight
                    heapq.heappush(heap,(distances[neighbor],neighbor))
        maxi = max(distances.values())            
        return maxi if maxi!= float('inf') else -1