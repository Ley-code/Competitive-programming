class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        hashmap = {0:0,1:0}
        l = maxLen = 0
        for r in range(len(nums)):
            hashmap[nums[r]]+=1
            if hashmap[0] <= k and  (r-l+1)>maxLen:
                maxLen = r-l+1
            else:
                while hashmap[0]>k:
                    hashmap[nums[l]]-=1
                    l+=1
        return maxLen
            