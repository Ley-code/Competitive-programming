# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        target = 0
        for num in nums:
            target ^= num
        diff = None
        for i in range(33):
            if (target & 1<<i) > 0:
                diff = 1<<i
                break
        res = [0,0]
        for num in nums:
            if num&diff > 0:
                res[1] ^= num
            else:
                res[0] ^= num
        return res
