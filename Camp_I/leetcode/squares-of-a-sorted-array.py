class Solution(object):
    def sortedSquares(self, nums):
        l,r = 0,len(nums)-1
        newnums = []
        while l<=r:
            if abs(nums[l]) >= abs(nums[r]):
                newnums.append(nums[l]**2)
                l+=1
            elif abs(nums[r]**2) > abs(nums[l]**2):
                newnums.append(nums[r]**2)
                r-=1
        return newnums[::-1]
        