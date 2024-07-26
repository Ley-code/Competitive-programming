# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        l = 0
        longest = 0
        for r in range(len(nums)):
            hashmap[nums[r]]+=1
            while hashmap[0]>1:
                hashmap[nums[l]]-=1
                l+=1
            longest = max(longest,r-l)
        return longest