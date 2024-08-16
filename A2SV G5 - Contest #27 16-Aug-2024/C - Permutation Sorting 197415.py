# Problem: C - Permutation Sorting - https://codeforces.com/gym/538762/problem/C

for i in range(int(input())):
  n = int(input())
  nums = list(map(int,input().split()))
  prev = set()
  ans = 0
  for num in nums:
    if num + 1 in prev:
      ans += 1
      print(num,end=" ")
    
    prev.add(num)
  print(ans)