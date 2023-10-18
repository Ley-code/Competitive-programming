class Solution(object):
    def pivotIndex(self, nums):
        leftsum = 0
        rightsum = sum(nums[1:])
        for i in range(len(nums)):
            if i == 0:
                if leftsum == rightsum:
                    return 0
            else:
                leftsum += nums[i-1]
                rightsum -= nums[i]
                
                if leftsum == rightsum:
                    return i
        return -1