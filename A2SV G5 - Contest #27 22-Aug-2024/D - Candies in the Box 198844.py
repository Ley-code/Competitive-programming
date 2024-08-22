# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

n = int(input())

def check(val):
  eaten = 0
  candies = n
  while candies>0:
    val = min(val,candies)
    eaten += val
    candies-=val
    candies -= candies//10
  return eaten
low = 1
high = n
while low<=high:
  mid = low + (high-low)//2
  if check(mid)*2>= n:
    high = mid -1
  else:
    low = mid + 1

print(low)