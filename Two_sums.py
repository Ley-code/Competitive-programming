class Solution(object):
    def twoSum(self, nums, target):
        nummap = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in nummap:
                return [nummap[value],i]
            nummap[nums[i]] = i
        return []
