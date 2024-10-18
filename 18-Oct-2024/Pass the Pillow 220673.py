# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direc = time // (n-1)
        if direc%2==0:
            return time%(n-1)+1
        else:
            return n-(time%(n-1))