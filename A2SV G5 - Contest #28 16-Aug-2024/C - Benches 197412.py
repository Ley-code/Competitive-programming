# Problem: C - Benches - https://codeforces.com/gym/540354/problem/C

from math import ceil
 
 
n = int(input())
m = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
maxnum = max(arr)
totaldiffs = 0
for num in arr:
  totaldiffs += abs(num-maxnum)
ans1 = maxnum
ans2 = maxnum + m
if m>totaldiffs:
  level = m-totaldiffs
  level = ceil(level/n) 
  ans1+= level
 
print(ans1,ans2)
