def minimumarray(array2d):
    minarray = []
    secondMinArray = []
    for array in array2d:
        array.sort()
        minarray.append(array[0])
        secondMinArray.append(array[1])
    sum = min(minarray)
    secondMinArray.sort()
    for i in range(1,len(secondMinArray)):
        sum+=secondMinArray[i]
    return sum
testcase = int(input())
for i in range(testcase):
    num_of_arrays = int(input())
    array2d = []
    for i in range(num_of_arrays):
        length_of_array = int(input())
        array2d.append(list(map(int,input().split())))
    print(minimumarray(array2d))
        