class Solution(object):
    def minSubArrayLen(self, target, nums):
        st = 0
        sum = 0
        shortest = len(nums)+1
        for en in range(len(nums)):
            sum+=nums[en]
            while sum>= target:
                shortest = min(shortest,en-st+1)
                sum-=nums[st]
                st+=1
        return 0 if shortest == len(nums)+1 else shortest