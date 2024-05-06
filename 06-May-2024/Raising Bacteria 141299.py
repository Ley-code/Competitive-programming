# Problem: Raising Bacteria - https://codeforces.com/contest/579/problem/A

num = int(input())
cnt = 1
while num>1:
    cnt+=num%2
    num= num//2
print(cnt)