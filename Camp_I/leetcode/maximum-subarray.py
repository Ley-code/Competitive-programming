class Solution(object):
    def maxSubArray(self, nums):
        currMax = maxSum = nums[0]
        for i in range(1,len(nums)):
            currMax = max(currMax+nums[i],nums[i])
            maxSum = max(maxSum,currMax)
        return maxSum
        