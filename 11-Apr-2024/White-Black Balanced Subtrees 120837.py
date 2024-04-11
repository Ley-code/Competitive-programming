# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

from collections import defaultdict

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    def dfs(node):
        nonlocal count
        if not node:
            return [0,0] #white black
        white,black = 0,0
        for neighbor in graph[node]:
            w,b = dfs(neighbor)
            white+=w
            black+=b
        if color[node-1]=="W":
            white+=1
        else:
            black+=1
        if white==black:
            count+=1
        return [white,black]
    for _ in range(int(input())):
        n = int(input())
        graph = defaultdict(list)
        a = list(map(int,input().split()))
        color = input()
        for i in range(n-1):
            graph[a[i]].append(i+2)
        count = 0
        dfs(1)
        print(count)

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()