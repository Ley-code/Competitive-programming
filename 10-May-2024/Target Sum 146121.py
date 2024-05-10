# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        memo = {}
        def dp(i,sums):     
            if i==N:
                if sums==target:
                    return 1
                return 0 
            if (i,sums) not in memo:
                res = dp(i+1,sums+nums[i]) + dp(i+1,sums-nums[i])
                memo[(i,sums)] = res
            return memo[(i,sums)] 
        return dp(0,0)
        
