def countingSort1(arr):
    # Write your code here
    result =[]
    for i in range(100):
        result.append(0) 
    for i in range(len(arr)):
        result[arr[i]] = result[arr[i]] + 1
    return result
