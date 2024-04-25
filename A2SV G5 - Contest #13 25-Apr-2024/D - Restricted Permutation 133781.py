# Problem: D - Restricted Permutation - https://codeforces.com/gym/519135/problem/D

from collections import defaultdict, deque
import heapq


n,q = map(int,input().split())
graph = defaultdict(list)
indegree = {i:0 for i in range(1,n+1)}
for _ in range(q):
    pre,aft = map(int,input().split())
    graph[pre].append(aft)
    indegree[aft] += 1
topsort = []
heap = []
for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)
while heap:
    num = heapq.heappop(heap)
    topsort.append(num)
    for nei in graph[num]:
        indegree[nei]-=1
        if indegree[nei]==0:
            heapq.heappush(heap,nei)
if len(topsort)==n:
    print(*topsort)
else:
    print(-1)