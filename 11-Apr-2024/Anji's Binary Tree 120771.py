# Problem: Anji's Binary Tree - https://codeforces.com/contest/1900/problem/C


import sys, threading
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()

def main():
    # def dfs(node,ops):
    #     nonlocal miniops
    #     left,right = graph[node]
    #     if not right and not left:
    #         miniops = min(miniops,ops)
    #         return
    #     if a[node-1]=="L":
    #         if right:
    #             dfs(right,ops+1)
    #         if left:
    #             dfs(left,ops)
    #     elif a[node-1]=="U":
    #         if left:
    #             dfs(left,ops+1)
    #         if right:
    #             dfs(right,ops+1)
    #     else:
    #         if right:
    #             dfs(right,ops)
    #         if left:
    #             dfs(left,ops+1)
    
    #stack implementation    
    for i in range(int(input())):
        n = int(input())
        a = input()
        graph = defaultdict(list)
        for i in range(n):
            left,right = map(int,input().split())
            graph[i+1].append(left)
            graph[i+1].append(right)
        miniops = float('inf')
        stack = [[1,0]] # node ops
        while stack:
            node,ops = stack.pop()
            left,right = graph[node]
            if not left and not right:
                miniops = min(miniops,ops)
                continue
            if left:
                if a[node-1]=="L": stack.append([left,ops])
                elif a[node-1]=="R": stack.append([left,ops+1])
                else: stack.append([left,ops+1])
            if right:
                if a[node-1]=="L":stack.append([right,ops+1])
                elif a[node-1]=="R":stack.append([right,ops])
                else: stack.append([right,ops+1])
        print(miniops)
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
