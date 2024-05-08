# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x^y
        count = 0
        n = len(bin(res))-2
        for i in range(n):
            if res&(1<<i)>0:
                count+=1
        return count