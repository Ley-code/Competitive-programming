# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefixsum = [nums[0]]
        for i in range(1,len(nums)):
            prefixsum.append(prefixsum[-1]^nums[i])
        limit = (2**maximumBit)-1
        ans = []
        for i in range(len(nums)-1,-1,-1):
            ans.append(limit^prefixsum[i])
        return ans
