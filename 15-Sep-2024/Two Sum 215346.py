# Problem: Two Sum - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if nums[i] in hashmap:
                return [i,hashmap[nums[i]]]
            hashmap[complement] = i
        