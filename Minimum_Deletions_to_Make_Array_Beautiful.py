class Solution(object):
    def minDeletion(self, nums):
        minDel = 0
        for index in range(len(nums)-1):
            if (index-minDel)%2 == 0 and nums[index] == nums[index+1]:
                minDel+=1
        return minDel + (len(nums)-minDel)%2