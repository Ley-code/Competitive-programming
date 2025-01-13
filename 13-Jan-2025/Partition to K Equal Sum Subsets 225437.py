# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        val = sum(nums)
        if val%k:
            return False
        
        n = len(nums)
        used = [False]*n
        target = val/k
        
        def backtrack(i,k,subsetSum):
            if k==0:
                return True
            if subsetSum == target:
                return backtrack(0,k-1,0)
            
            for j in range(i,n):
                if used[j] or subsetSum+nums[j]>target:
                    continue
                used[j] = True
                if backtrack(j+1,k,subsetSum+nums[j]):
                    return True
                used[j] = False
                if subsetSum == 0:
                    break
            return False
        return backtrack(0,k,0)