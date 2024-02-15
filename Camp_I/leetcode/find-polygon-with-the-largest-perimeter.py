class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        peri = 0
        presum = 0
        for i in range(len(nums)):
            if presum>nums[i] and i>=2:
                presum+=nums[i]
                peri = max(peri,presum)
            elif presum==nums[i] and i<=2:
                presum+=nums[i]
            else:
                presum+=nums[i]
        if peri==0:return -1
        return peri

                