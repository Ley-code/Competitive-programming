class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        ans = l = 0
        pre = 1
        for r in range(len(nums)):
            pre*=nums[r]
            while pre>=k and l<=r:
                pre/=nums[l]
                l+=1
            ans+=r-l+1
        return ans