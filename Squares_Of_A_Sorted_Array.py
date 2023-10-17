class Solution(object):
    def sortedSquares(self, nums):
        l,r = 0,len(nums)-1
        newnums = []
        while l<=r:
            if nums[l]**2 >= nums[r]**2:
                newnums.append(nums[l]**2)
                l+=1
            elif nums[r]**2 > nums[l]**2:
                newnums.append(nums[r]**2)
                r-=1
        return newnums[::-1]