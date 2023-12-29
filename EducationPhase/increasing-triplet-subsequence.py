class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mini1 = float('inf')
        mini2 = float('inf')
        for i in range(len(nums)):
            if nums[i] < mini1:
                mini1 = nums[i]
            elif nums[i] < mini2 and nums[i]>mini1:
                mini2 = nums[i]
            elif nums[i]> mini2:
                return True
        return False
        
