class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currsum = sum(nums[:k])
        maxaver = currsum/k
        for i in range(k,len(nums)):
            currsum+=nums[i]
            currsum-=nums[i-k]
            maxaver = max(maxaver,currsum/k)
        return maxaver