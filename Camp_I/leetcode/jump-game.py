class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=curr:
                curr = i
        if curr==0:
            return True
        return False
            
            
            