# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from collections import defaultdict


for i in range(int(input())):
    n  = int(input())
    a = list(map(int,input().split()))
    factors = defaultdict(int)
    for i in range(n):
        d = 2
        while d*d<=a[i]:
            while a[i]%d==0:
                a[i]//=d
                factors[d]+=1
            d+=1
        if a[i]>1:
            factors[a[i]]+=1
    flag = True
    for val in factors:
        if factors[val]%n:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")