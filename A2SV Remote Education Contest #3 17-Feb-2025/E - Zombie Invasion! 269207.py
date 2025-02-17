# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

from collections import defaultdict


for _ in range(int(input())):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  x = list(map(int,input().split()))

  posmap = defaultdict(int)
  for i in range(n):
    posmap[abs(x[i])] += a[i]

  val = list(posmap.keys())
  val.sort()
  flag = True
  l = 0
  _len = len(val)
  for start in range(val[-1]+1):
    if start in posmap:
      flag = False
      break
    curr = k
    while curr>0 and l<_len:
      zombie = posmap[val[l]]
      if curr>=zombie:
        curr-=zombie
        del posmap[val[l]]
        l+=1
      else:
        posmap[val[l]]-=curr
        curr = 0
  if flag:
    print("YES")
  else:
    print("NO")