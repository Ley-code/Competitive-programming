class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i]<nums[i-1]:
                nspace = ceil(nums[i-1]/nums[i])
                op+=nspace-1
                nums[i-1] = nums[i-1]//nspace
        return op