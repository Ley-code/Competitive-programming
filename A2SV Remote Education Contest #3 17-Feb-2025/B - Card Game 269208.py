# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

n = int(input())
a = list(map(int,input().split()))
maps = [i for i in range(n)]
maps.sort(key = lambda x:a[x])
l = 0
r = n-1
while l<r:
  print(maps[l]+1,maps[r]+1)
  l+=1
  r-=1