# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

n,m,k = map(int,input().split())
count = 0
arr = []
for i in range(m+1):
    arr.append(int(input()))
for i in range(m):
    res = bin(arr[-1]^arr[i]).count("1")
    if res<=k:
        count+=1
print(count)