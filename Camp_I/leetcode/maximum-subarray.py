class Solution(object):
    def maxSubArray(self, nums):
        curmax = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            curmax = max(curmax+nums[i],nums[i])
            maxsum = max(maxsum,curmax)
        return maxsum
        