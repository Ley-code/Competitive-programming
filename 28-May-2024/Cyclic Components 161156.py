# Problem: Cyclic Components - https://codeforces.com/problemset/problem/977/E

from collections import defaultdict


n,m = map(int,input().split())
graph = defaultdict(list)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
cycles = 0
def dfs(node):
    flag = True
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        if len(graph[curr])!=2:
            flag = False
        for neigh in graph[curr]:
            if neigh not in visited:
                stack.append(neigh)
    return flag
visited =  set()
for i in range(1,n+1):
    if i not in visited:
        if dfs(i):
            cycles+=1
print(cycles)
