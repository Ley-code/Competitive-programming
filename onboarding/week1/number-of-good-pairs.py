class Solution(object):
    def numIdenticalPairs(self, nums):
        hashmap = {}
        count = 0
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
            if hashmap[nums[i]]>1:
                count+=(hashmap[nums[i]]-1)
        return count