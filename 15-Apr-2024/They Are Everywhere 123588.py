# Problem: They Are Everywhere - https://codeforces.com/problemset/problem/701/C

from collections import defaultdict


n = int(input())
flats  = input()
tot = len(set(flats))
l = 0
length = n+1
currpokemons = defaultdict(int)
for r in range(n):
    currpokemons[flats[r]]+=1
    m = len(currpokemons)
    while m>tot:
        currpokemons[flats[l]]-=1
        if currpokemons[flats[l]]==0:
            del currpokemons[flats[l]]
        l+=1
    while len(currpokemons)==tot:
        length = min(length,r-l+1)
        currpokemons[flats[l]]-=1
        if currpokemons[flats[l]]==0:
            del currpokemons[flats[l]]
        l+=1
print(length)