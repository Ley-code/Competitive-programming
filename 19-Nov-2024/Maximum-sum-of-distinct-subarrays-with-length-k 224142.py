# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        count = defaultdict(int)
        cur_sum = 0
        max_sum = 0
        for r in range(N):
            cur_sum += nums[r]
            count[nums[r]]+=1
            if len(count)==k:
                max_sum = max(max_sum,cur_sum)
            if r>=k-1:
                cur_sum -= nums[l]
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    del count[nums[l]]
                l+=1
        return max_sum


