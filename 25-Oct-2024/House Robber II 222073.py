# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, arr: List[int]) -> int:
        
        def dp(i,nums):
            if i >= len(nums):
                return 0
            if i not in memo:
                memo[i] = max(dp(i+1,nums),dp(i+2,nums)+nums[i])
            return memo[i]
        memo = {}
        first = dp(0,arr[:-1])
        memo = {}
        second = dp(0,arr[1:])
        return max(first,second,arr[0])