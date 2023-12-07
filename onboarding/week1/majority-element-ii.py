class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = set()
        hashmap = {}
        for i in range(n):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
            if hashmap[nums[i]] > n/3:
                if nums[i]==0:
                    result.add(0)
                result.add(nums[i])
        return result 