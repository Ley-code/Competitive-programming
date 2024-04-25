# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque


n = int(input())
arr = []
for i in range(n):
    arr.append(input())
graph = defaultdict(list)
indegree = {chr(i):0 for i in range(97,123)} 
nedges = 0
flag = False
for i in range(n-1):
    l = 0
    n = len(arr[i])
    m = len(arr[i+1])
    while l<n and l<m:
        if arr[i][l]==arr[i+1][l]:
            l+=1
        else:
            graph[arr[i][l]].append(arr[i+1][l])
            flag = True
            nedges+=1
            indegree[arr[i+1][l]]+=1
            break
    if l==m and l<n:
        print("Impossible")
        quit()  
q = deque([])
for char in indegree:
    if indegree[char]==0:
        q.append(char)
ans = ""
visited = set()
while q:
    char = q.popleft()
    ans+=char
    for nei in graph[char]:
        indegree[nei]-=1
        nedges-=1
        if indegree[nei]==0:
            q.append(nei)
if flag and nedges:
    print("Impossible")
else:
    print(ans)

