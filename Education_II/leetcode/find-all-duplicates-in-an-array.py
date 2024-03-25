class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = 0
        arr = set()
        while l<len(nums):
            correctpos = nums[l]-1
            if nums[l]!=l+1:
                if nums[l] == nums[correctpos]:
                    arr.add(nums[l])
                    l+=1
                else:
                    nums[l],nums[correctpos] = nums[correctpos],nums[l]
            else:
                l+=1
        return arr