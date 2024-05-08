# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num))-2
        for i in range(n):
            num ^= (1<<i)
        return num