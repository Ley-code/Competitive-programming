class Solution(object):
    def numberOfSubarrays(self, nums, k):
        ans = left = cnt = odd = 0
        for i in range(len(nums)):
            if nums[i]%2!=0:
                odd+=1
                cnt = 0
            while odd == k:
                cnt+=1
                if nums[left]%2!=0:
                    odd-=1
                left+=1
            ans+=cnt
        return ans
