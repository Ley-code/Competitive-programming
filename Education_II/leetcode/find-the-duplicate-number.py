class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        while l<len(nums):
            correctpos = nums[l]-1
            if nums[l]!=l+1:
                if nums[l]==nums[correctpos]:
                    return nums[l]
                else:
                    nums[l],nums[correctpos] = nums[correctpos],nums[l]
            else:
                l+=1
                