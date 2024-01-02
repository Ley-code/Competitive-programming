class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        for r in range(len(nums)):
            if nums[l] == 0 and nums[r]!= 0:
                nums[l],nums[r] = nums[r],nums[l]
            if nums[l]!= 0:
                l+=1
        return nums

        