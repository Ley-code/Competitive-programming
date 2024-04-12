# Problem: C - Maximizing Edges in a Tree - https://codeforces.com/gym/515998/problem/C



import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    from collections import defaultdict

    n = int(input())
    graph = defaultdict(list)
    for i in range(n-1):
        st,end = map(int,input().split())
        graph[st].append(end)
        graph[end].append(st)

    def dfs(node,clr):
        for adj in graph[node]:
            if color[adj]==-1:
                color[adj] = clr
                dfs(adj,1-clr)
    color = [-1]*(n+1)
    color[1]=1
    dfs(1,0)
    possible = color.count(1)*color.count(0)
    print(abs((n-1) - (possible)))
                
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

    

    
    