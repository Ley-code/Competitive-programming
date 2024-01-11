class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum = 0
        currsum = 0
        l = 0
        hashmap = defaultdict(int)
        for r in range(len(nums)):
            currsum+=nums[r]
            while nums[r] in hashmap:
                hashmap[nums[l]]-=1
                currsum-=nums[l]
                if hashmap[nums[l]] == 0:
                    del hashmap[nums[l]]
                l+=1
            hashmap[nums[r]]+=1
            maxsum = max(maxsum,currsum)
        return maxsum
            