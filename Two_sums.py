def twosums(nums,target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
print(twosums([3,2,4],6))