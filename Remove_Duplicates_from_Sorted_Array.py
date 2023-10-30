class Solution:
    def removeDuplicates(self, nums):
        count=1
        idx = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx+=1
                count+=1
        return count