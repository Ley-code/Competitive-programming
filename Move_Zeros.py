class Solution(object):
    def moveZeroes(self, nums):
        new = nums
        for i in range(len(nums)):
            if nums[i]==0:
                new.insert(len(nums),nums[i])
                new.remove(nums[i])
        return new