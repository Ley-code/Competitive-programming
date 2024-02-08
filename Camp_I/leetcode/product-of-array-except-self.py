class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        prefix = postfix = 1
        for i in range(len(nums)-1):
            prefix*=nums[i]
            res[i+1] = prefix
        for j in range(-1,-(len(nums)),-1):
            postfix *=nums[j]
            res[j-1] *= postfix
        return res 
