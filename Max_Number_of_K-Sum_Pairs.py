class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        left,right = 0,len(nums)-1
        res = 0
        while left<right:
            if nums[left]+nums[right] > k:
                right-=1
            elif nums[left]+nums[right]<k:
                left+=1
            else:
                res+=1
                right-=1
                left+=1
        return res