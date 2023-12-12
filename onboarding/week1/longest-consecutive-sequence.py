class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in nums:
                nextnum = num+1
                while nextnum in nums:
                    nextnum+=1
                longest = max(longest,nextnum - num)
        return longest