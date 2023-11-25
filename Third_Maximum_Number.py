from ast import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        maxnum,r = nums[-1],len(nums)-1
        count= 1

        while r>=0 and count<3:
            if r> 0 and nums[r] == nums[r-1]:
                r-=1
            else:
                maxnum = nums[r-1]
                count+=1
                r-=1

        return maxnum

        
