def findMaxRam(n,k,a,b):
  ab = [(0,0)]*n
  for i in range(n):
    ab[i] = (a[i],b[i])
  ab.sort()
  for eachA,eachB in ab:
    if eachA <= k:
      k += eachB
  return k

t = int(input())
for _ in range(t):
  n,k = map(int,input().split())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))

  print(findMaxRam(n,k,a,b))


