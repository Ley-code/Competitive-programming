# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        count = defaultdict(int)
        def dp(idx):
            if idx == len(nums):
                return 0
            maxlen = 0
            for i in range(idx):
                if nums[i]<nums[idx]:
                    maxlen = max(count[i],maxlen)
            count[idx] = maxlen+1
            return max(count[idx],dp(idx+1))
        return dp(0)