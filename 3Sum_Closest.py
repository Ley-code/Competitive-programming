class Solution(object):
    def threeSumClosest(self, nums,target):
        res = nums[0] + nums[1] + nums[2]
        nums.sort()

        for i,item in enumerate(nums):
            if i > 0 and nums[i-1] == item:
                continue

            l,r = i+1 , len(nums) -1 
            while l < r:
                threeSum = nums[l] + item + nums[r]
                if threeSum == target:
                    return threeSum
                elif threeSum > target:
                    r -= 1
                else:
                    l += 1
                if abs(threeSum-target) < abs(res-target):
                    res = threeSum
        return res