class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        subarraysum = maxsum = sum(nums[:k]) 
        for r in range(k,len(nums)):
            subarraysum+=nums[r]
            subarraysum-=nums[l]
            maxsum = max(maxsum,subarraysum)
            l+=1
        return maxsum/k