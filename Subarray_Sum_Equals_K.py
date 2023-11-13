class Solution(object):
    def subarraySum(self, nums, k):
        runningsum = 0
        hashmap = {0:1}
        count = 0
        for r in range(len(nums)):
            runningsum+=nums[r]
            if runningsum - k in hashmap:
                count+= hashmap[runningsum-k]
            hashmap[runningsum]= hashmap.get(runningsum,0)+1
        return count