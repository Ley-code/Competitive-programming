# Problem: Heap Operations - https://codeforces.com/contest/681/problem/C

import heapq


ops = []
for i in range(int(input())):
    ops.append(list(map(str,input().split())))
heap = []
ans = []
for op in ops:
    if op[0]=="removeMin":
        if heap:
            heapq.heappop(heap)
        else:
            ans.append(["insert",0])
        ans.append(op)
    elif op[0]=="insert":
        heapq.heappush(heap,int(op[1]))
        ans.append(op)
    else:
        num = int(op[1])
        while heap and heap[0]<num:
            heapq.heappop(heap)
            ans.append(["removeMin"])
        if not heap or heap[0]>num:
            ans.append(["insert", num])
            heapq.heappush(heap,num)
        ans.append(["getMin",num])
print(len(ans))
for pair in ans:
    print(*pair)



