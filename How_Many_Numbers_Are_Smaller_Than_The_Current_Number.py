def smallerNumbersThanCurrent(nums):
    newnums = []
    res = []
    smallerNumMap={num:0 for num in nums}

    for i in range(len(nums)):
        newnums.append(nums[i])
    newnums.sort()
    
    for i in range(len(nums)):
        smallerNumMap[nums[i]] = newnums.index(nums[i])
    for i in range(len(nums)):
        res.append(smallerNumMap.get(nums[i]))
    return res
