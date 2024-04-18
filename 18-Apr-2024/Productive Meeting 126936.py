# Problem: Productive Meeting - https://codeforces.com/contest/1579/problem/D

import heapq


for i in range(int(input())):
    n = int(input())
    meeting = list(map(int,input().split()))
    for i in range(n):
        meeting[i] = [-meeting[i],i+1]
    heapq.heapify(meeting)
    talks = 0
    arr = []
    while len(meeting)>1:
        p1,idx1 = heapq.heappop(meeting)
        p2,idx2 = heapq.heappop(meeting)
        if p1==0 or p2==0:
            break
        arr.append([idx1,idx2])
        heapq.heappush(meeting,[p1+1,idx1])
        heapq.heappush(meeting,[p2+1,idx2])
        talks+=1
    print(talks)
    for pair in arr:
        print(*pair)