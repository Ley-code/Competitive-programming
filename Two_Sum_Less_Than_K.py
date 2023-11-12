def TwoSumLessThanK(nums,k):
    #[1,8,23,24,33,34,54,75] k = 60
    nums.sort()
    maxsum = 0
    l,r = 0,len(nums)-1
    while l<r:
        sumation = nums[l]+nums[r]
        if sumation>k:
            r-=1
        else:
            maxsum = max(maxsum,sumation)
            l+=1
    return maxsum if maxsum!= 0 else -1        
print(TwoSumLessThanK([10,20,30],15))