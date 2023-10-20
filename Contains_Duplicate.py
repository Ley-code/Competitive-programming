class Solution(object):
    def containsDuplicate(self, nums):
        map = {}
        for r in range(len(nums)):
            if nums[r] in map:
                return True
            else:
                map[nums[r]] = 1
        return False
