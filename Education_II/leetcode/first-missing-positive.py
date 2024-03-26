class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        l = 0
        while l<len(nums):
            correctpos = nums[l]-1
            if nums[l]<=0 or correctpos>=len(nums) or nums[l]==nums[correctpos] or nums[l]==l+1:
                l+=1
            else:
                nums[l],nums[correctpos] = nums[correctpos],nums[l]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return nums[-1]+1
        
        
