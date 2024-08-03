# Problem: B - Mohammed's Magical Cleaning Machine - https://codeforces.com/gym/537362/problem/B

for i in range(int(input())):
  n = int(input())
  arr = list(map(int,input().split()))
  maxops = 0
  for dust in arr[:-1]:
    if dust:
      maxops+=dust
    if maxops and dust==0:
      maxops+=1
  print(maxops)
