class Solution:
    def findLengthOfLCIS(self, nums):
        res = r = 1
        l = 0
        while r<len(nums):
            if nums[r]>nums[r-1]:
                res = max(res,r-l+1)
            else:
                l=r
            r+=1
        return res