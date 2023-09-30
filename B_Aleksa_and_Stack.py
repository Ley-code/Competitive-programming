res = []
for i in range(int(input())):
    n = int(input())
    temp = [1,4,7]
    if n == 3:
        res.append(temp)
    else:
        while len(temp) < n:
            temp.append(temp[-1] + 3)
        res.append(temp)

for i in res:
    print(*i)