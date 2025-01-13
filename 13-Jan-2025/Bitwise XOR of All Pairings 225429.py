# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
        n2 = len(nums2)
        n1 = len(nums1)

        temp = 0
        for num in nums2:
            temp ^= num
        if n1%2==0:
            temp = 0
        if n2%2 == 1:
            for i in range(n1):
                temp ^= nums1[i]
        return temp