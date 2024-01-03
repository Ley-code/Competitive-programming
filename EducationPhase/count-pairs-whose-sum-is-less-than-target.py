class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        l = 0
        while l<len(nums):
            r = l+1
            while r<len(nums) and nums[l]+nums[r]<target:
                count+=1
                r+=1
            l+=1
        return count

                    