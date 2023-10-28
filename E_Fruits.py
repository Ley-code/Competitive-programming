from collections import Counter
n,m=map(int,input().split())
ar=sorted(list(map(int,input().split())))
dic=Counter()
for _ in range(m):
    dic[input()]+=1
li=sorted(dic.values(),reverse=True)
mini= 0
maxi = 0
for i in range(len(li)):
    mini+=(ar[i]*li[i])

ar=ar[::-1]
for i in range(len(li)):
    maxi+=(ar[i]*li[i])
print(mini,maxi)