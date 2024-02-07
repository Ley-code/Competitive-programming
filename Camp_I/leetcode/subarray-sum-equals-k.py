class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0:1}
        presum = 0
        count = 0
        for i in range(len(nums)):
            presum+=nums[i]
            if presum-k in hashmap:
                count+=hashmap[presum-k]
            hashmap[presum] = hashmap.get(presum,0)+1
        return count