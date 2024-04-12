# Problem: D - The Flip Tree - https://codeforces.com/gym/515998/problem/D


from collections import defaultdict, deque
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    graph = defaultdict(list)
    n = int(input())
    for _ in range(n-1):
        s,d = map(int,input().split())
        graph[d].append(s)
        graph[s].append(d)
        
    current = list(map(int,input().split()))
    target = list(map(int,input().split()))

    def dfs(node,parent,grandparent):
        nonlocal count
        visited.add(node)
        flip = grandparent
        if grandparent:
            current[node-1]= 1-current[node-1]
        if current[node-1]!=target[node-1]:
            count+=1
            nodes.append(node)
            flip = not grandparent
        for adj in graph[node]:
            if adj not in visited:
                dfs(adj,flip,parent)
    count = 0
    nodes = []
    visited = set()
    dfs(1,False,False)
    print(count)
    for i in range(len(nodes)):
        print(nodes[i])    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()