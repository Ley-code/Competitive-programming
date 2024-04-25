# Problem: A - Balanced Alphabet - https://codeforces.com/gym/519135/problem/A

for i in range(int(input())):
    n,k = map(int,input().split())
    ans = ""
    for i in range(n):
        ans+= chr((i%k+97))
    print(ans)