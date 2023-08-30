testcase = int(input())
lever = []
for i in range(testcase):
    lever.append(list(map(int,input().split())))
    a = lever[i][0]
    b = lever[i][1]
    print(a/b)


