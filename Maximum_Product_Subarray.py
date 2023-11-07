class Solution(object):
    def maxProduct(self, nums):
        curMax,curMin = 1,1
        res = max(nums)
        for num in nums:
            if num == 0:
                curMax,curMin = 1,1
                continue
            temp = num*curMax
            curMax = max(num,num*curMax,num*curMin)
            curMin = min(num,num*curMin,temp)
            res = max(res,curMax)
        return res