class Solution(object):
    def threeSumClosest(self, nums,target):
        res= nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right = len(nums)-1
            while left<right:
                sums = nums[i]+nums[right]+nums[left]
                if sums==target:
                    return sums
                elif sums>target:
                    right-=1
                elif sums<target:
                    left+=1
                if abs(sums-target)<abs(res-target):
                    res = sums
        return res