class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        presum = [0]*len(nums)
        for st,end in requests:
            presum[st]+=1
            if end == len(nums)-1:
                continue
            presum[end+1] -=1
        for i in range(len(nums)):
            if i>0:
                presum[i] += presum[i-1]
        totsum = 0
        presum.sort(reverse = True)
        nums.sort(reverse = True)
        for i in range(len(nums)):
            totsum+= nums[i]*presum[i]
        return totsum% (10**9+7)