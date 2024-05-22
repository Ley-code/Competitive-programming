# Problem: Longest Arithmetic Subsequence of Given Difference - https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        hashmap = defaultdict(int)
        dp = [1]*len(arr)
        longest = 1
        for i in range(len(arr)):
            if arr[i]-difference in hashmap:
                dp[i] += dp[hashmap[arr[i]-difference]]
                longest = max(longest,dp[i])
            hashmap[arr[i]] = i
        return longest