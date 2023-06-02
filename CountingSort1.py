def countingSort1(arr):
    # Write your code here
    result =[0]*100
    for i in range(len(arr)):
        result[arr[i]] = result[arr[i]] + 1
    return result
