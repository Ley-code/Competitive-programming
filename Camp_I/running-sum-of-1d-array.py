class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = 0
        for i in range(len(nums)):
            runningsum+=nums[i]
            nums[i] = runningsum
        return nums