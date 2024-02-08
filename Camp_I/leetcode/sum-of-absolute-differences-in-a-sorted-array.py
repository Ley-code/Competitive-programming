class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        presum = [0]*len(nums)
        sufsum = [0]*len(nums)
        res = []
        cursum = 0
        for i in range(len(nums)):
            presum[i] = cursum
            cursum+=nums[i]
        cursum = 0
        for i in range(-1,-(len(nums)+1),-1):
            sufsum[i] = cursum
            cursum+=nums[i]
        for i in range(len(nums)):
            sums = ((nums[i]*i)-presum[i])+(sufsum[i]-(nums[i]*(len(nums)-i-1)))
            res.append(sums)
        return res
