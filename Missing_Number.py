class Solution(object):
    def missingNumber(self, nums):
        
        missing = -1
        for i in range(len(nums)):
            if i!= nums[i]:
                missing = i
                break
        if missing == -1:
            return len(nums)
        return missing 