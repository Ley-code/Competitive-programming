# Problem: Disjoint Sets Union 2 - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/B

n,m = map(int,input().split())
root = [i for i in range(n+1)]
rank = [1]*(n+1)
parents = {i:[i,i,1] for i in range(n+1)}
def find( x):
    if x==root[x]:
        return x
    root[x]= find(root[x])
    return root[x]
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            root[rootY] = rootX
            p,c = rootX,rootY
        elif rank[rootX] < rank[rootY]:
            root[rootX] = rootY
            p,c = rootY,rootX
        else:
            root[rootX] = rootY
            p,c = rootY,rootX
            rank[rootY] += 1
        minel = min(parents[p][0],parents[c][0])
        maxel = max(parents[p][1],parents[c][1])
        tot = parents[p][2]+parents[c][2]
        parents[p] = [minel,maxel,tot]
for i in range(m):
    task = list(map(str,input().split()))
    if task[0]=="union":
        union(int(task[1]),int(task[2]))
    else:
        print(*parents[find(int(task[1]))])
    