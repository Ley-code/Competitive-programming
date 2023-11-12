def numberof3sumSmaller(nums,target):
    if len(nums)<=2:
        return 0
    #[-2,0,1,3]
    res = 0
    nums.sort()
    for i in range(len(nums)-2):
        left = i+1
        right = len(nums)-1
        while left<right:
            threesum = nums[i]+nums[left]+nums[right]
            if threesum>=target:
                right-=1
            elif threesum<target:
                res+=right-left
                left+=1
                           
    return res
print(numberof3sumSmaller([0],2))
            
