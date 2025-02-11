# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        output = [0,0]
        for values in count.values():
            output[1]+=values%2
            output[0]+=values//2
        return output