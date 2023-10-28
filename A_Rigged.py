def rigged(array2d):
    maxe = array2d[0][1]
    maxs = array2d[0][0]
    next_best_e = 0
    next_best_e_idx = 0
    for i in range(1,len(array2d)):
        if array2d[i][0]>= maxs and array2d[i][1]>= maxe:
            maxs = -1
    return maxs 
testcase = int(input())
for i in range(testcase):
    array2d = []
    n = int(input())
    for j in range(n):
        array2d.append(list(map(int,input().split())))
    print(rigged(array2d))