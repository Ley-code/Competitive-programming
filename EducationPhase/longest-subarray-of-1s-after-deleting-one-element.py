class Solution(object):
    def longestSubarray(self, nums):
        nummap = {0:0,1:0}
        longest = 0
        l = 0
        for r in range(len(nums)):
            nummap[nums[r]] = nummap.get(nums[r],0)+1
            while nummap[0] == 2:
                nummap[nums[l]] -=1
                l+=1
            longest = max(longest,r-l)
        return longest