# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        ans = left = count = odd = 0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                odd+=1
                count = 0
            while odd == k:
                count+=1
                odd-=nums[left]&1
                left+=1
            ans+=count
        return ans
