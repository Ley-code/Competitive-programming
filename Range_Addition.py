def RangeAddition(updates,length):
    res = [0]*length
    for update in updates:
        start,end,inc=update
        res[start] += inc
        if end+1 < length:
            res[end+1]-= inc
    for i in range(1,len(res)):
        res[i] = res[i-1]+res[i]
    return res
print(RangeAddition([[2,4,6],[5,6,8],[1,9,-4]],10))