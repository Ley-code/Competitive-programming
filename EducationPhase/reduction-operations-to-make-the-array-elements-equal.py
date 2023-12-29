class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]!=nums[i-1]:
                count += (n-i)
        return count
