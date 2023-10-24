def concatenate(res):
    result = ""
    for num in res:
        result+= (str(num)+" ")
    return result
def favorite(nums,n):
    res = []
    l,r=0,n-1
    while l<=r:
        if l==r:
            res.append(nums[l])
        else:
            res.append(nums[l])
            res.append(nums[r])
        l+=1
        r-=1
    return concatenate(res)
testcase = int(input())
for i in range(testcase):
    length = int(input())
    array = list(map(int,input().split()))
    print(favorite(array,length))

