def luckynumber(left,right):
    maxdiff = 0
    res = left
    for num in range(left,right+1):
        newnum = sorted(str(num))
        currdiff = int(newnum[len(newnum)-1])-int(newnum[0])
        if currdiff >= maxdiff:
            maxdiff = currdiff
            res = num  
        if maxdiff == 9:
            break
    return res
testcase = int(input())
for i in range(testcase):
    value = list( map(int,input().split()))
    print(luckynumber(value[0],value[1]))
