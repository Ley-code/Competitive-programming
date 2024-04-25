# Problem: B - Chat - https://codeforces.com/gym/519135/problem/B

import heapq


n,k,q = map(int,input().split())
t = list(map(int,input().split()))
heap = []
seen = set()
for i in range(q):
    ty,idx = map(int,input().split())
    if ty == 1:
        if len(heap)<k:
            heapq.heappush(heap,t[idx-1])
            seen.add(t[idx-1])
        else:
            if t[idx-1]>heap[0]:
                seen.remove(heap[0])
                heapq.heapreplace(heap,t[idx-1])
                seen.add(t[idx-1])
    else:
        if t[idx-1] in seen:
            print("YES")
        else:
            print("NO")   