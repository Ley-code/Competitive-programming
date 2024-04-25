# Problem: E - Seamless Flow - https://codeforces.com/gym/519135/problem/E

from collections import defaultdict, deque


for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = defaultdict(list)
    indegree = {i:0 for i in range(1,n+1)}
    mark = set()
    for i in range(m):
        t,x,y = map(int,input().split())
        if t == 0:
            graph[x].append(y)
            graph[y].append(x)
            mark.add((x,y))
            mark.add((y,x))
        else:
            graph[x].append(y)
            indegree[y]+=1

    topsort = 0
    q = deque([num for num in indegree if indegree[num]==0])
    visited = set()
    ans = []
    while q:
        num = q.popleft()
        topsort+=1
        visited.add(num)
        for nei in graph[num]:
            if nei not in visited:
                if (num,nei) not in mark:
               
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        q.append(nei)
                ans.append([num,nei])

    if topsort==n:
        print("YES")
        for num in ans:
            print(*num)
    else:
        print("NO")

                    


