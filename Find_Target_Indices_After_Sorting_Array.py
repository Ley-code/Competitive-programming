class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        target_idx = []
        for idx in range(len(nums)):
            if nums[idx] == target:
                target_idx.append(idx)
        return target_idx