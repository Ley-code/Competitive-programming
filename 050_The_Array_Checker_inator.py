def areEqual(array1,array2):
    Map1 = {}
    Map2 = {}
    for i in range(len(array1)):
        if array1[i] not in Map1:
            Map1[array1[i]] = 1
    for j in range(len(array2)):
        if array2[j] not in Map2:
            Map2[array2[j]] = 1
    if Map1 == Map2:
        return "YES"
    return "NO"
n = int(input())
array1 = []
array2 = []
for i in range(n):
    array1.append(int(input()))
m = int(input())
for i in range(m):
    array2.append(int(input()))
print(areEqual(array1,array2))