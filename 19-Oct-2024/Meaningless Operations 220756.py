# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

from math import sqrt


def gcd(num):
  gd = 1
  i = 1
  while i<=sqrt(num):
    if num%i==0:
      n = num//i
      if n!=num:
        gd = max(gd,n)
    i+=1
  return gd
for i in range(int(input())):
  a = int(input())
  binary = bin(a)[2:]
  length = len(binary)
  if length==binary.count("1"):
    print(gcd(a))
  else:
    print(pow(2,length)-1)
