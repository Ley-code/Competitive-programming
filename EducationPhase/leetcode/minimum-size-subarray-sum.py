class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minilen = len(nums)+1
        currsum = 0
        for r in range(len(nums)):
            currsum+=nums[r]
            while currsum>=target:
                minilen = min(minilen,r-l+1)
                currsum-=nums[l]
                l+=1
        return minilen if minilen!=len(nums)+1 else 0
        