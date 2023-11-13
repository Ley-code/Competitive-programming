def Maximum_Size_Subarray_Sum_Equals_K(nums,k):
    runningsum = 0
    hashmap = {0:-1}
    maximumsize = 0
    for r in range(len(nums)):
        runningsum+=nums[r]
        if runningsum - k in hashmap:
            maximumsize = max(maximumsize,(r-hashmap[runningsum-k]))
        else:
            if runningsum in hashmap:
                continue
            hashmap[runningsum] = r
    return maximumsize
print(Maximum_Size_Subarray_Sum_Equals_K([1,-1,5,-2,3],3))
