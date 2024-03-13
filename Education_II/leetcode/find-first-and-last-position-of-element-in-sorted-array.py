class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if not nums:
            return ans
        left , right = 0 , len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid+1
        if left<len(nums) and nums[left]==target: 
            ans[0] = left
        l , r = left , len(nums)-1
        while l<=r:
            mid  = l + (r-l)//2
            if nums[mid]<=target:
                l = mid+1
            else:
                r = mid-1
        if r>=0 and nums[r] == target:
            ans[1] =  r
        return ans