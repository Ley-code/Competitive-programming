# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        target = max(nums)
        maxlen = 1
        l = 0
        r = 0
        while l<len(nums):
            while l<len(nums) and nums[l] == target:
                r+=1
                l+=1 
            maxlen = max(maxlen,r)
            r = 0
            l+=1
        return maxlen