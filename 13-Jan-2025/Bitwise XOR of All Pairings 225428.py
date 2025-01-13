# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        temp = 0
        for num in nums2:
            temp ^= num
        res = 0
        n2 = len(nums2)
        n1 = len(nums1)
        for i in range(n1):
            res ^= temp
            if n2%2==1:
                res^= nums1[i]
        return res