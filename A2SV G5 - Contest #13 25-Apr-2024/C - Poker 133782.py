# Problem: C - Poker - https://codeforces.com/gym/519135/problem/C

import heapq


for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    heap = []
    tot = 0
    for num in arr:
        if num!=0:
            heapq.heappush(heap,-num)
        elif num==0 and heap:
            tot+= -heapq.heappop(heap)
    print(tot)