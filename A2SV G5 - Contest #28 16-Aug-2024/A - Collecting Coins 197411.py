# Problem: A - Collecting Coins - https://codeforces.com/gym/540354/problem/A

for i in range(int(input())):
  arr = list(map(int,input().split()))
  maxnum = max(arr[:len(arr)-1])
  nums = 0
  for i in range(len(arr)-1):
    nums+= maxnum-arr[i]
  if nums>arr[-1] or (arr[-1]-nums)%3:
    print("NO")
  else:
    print("YES")
  