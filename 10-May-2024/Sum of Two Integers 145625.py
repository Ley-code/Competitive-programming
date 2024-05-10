# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = (a&b)<<1
        sums = a^b
        mask = 0xffffffff
        while carry & mask !=0:
            temp = sums
            sums = sums^carry
            carry = (temp&carry)<<1
        return sums&mask if carry>0 else sums        