# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums%2==1:
            return False
        target = sums//2
        N = len(nums)
        memo = {}
        def dp(i,sums):
            if i == N:
                return sums == target
            if sums>target:
                return False
            if (i,sums) not in memo:
                memo[(i,sums)] = dp(i+1,sums+nums[i]) or dp(i+1,sums) 
            return memo[(i,sums)]
        return dp(0,0)