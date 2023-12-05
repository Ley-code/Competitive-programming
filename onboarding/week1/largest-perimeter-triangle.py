class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        perimeter = 0
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]+nums[i+1] > nums[i+2]:
                threesum = nums[i]+nums[i+1]+nums[i+2]
                perimeter = max(perimeter,threesum)
        return perimeter