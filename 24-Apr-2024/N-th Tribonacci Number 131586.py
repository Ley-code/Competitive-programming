# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1
        while n>=3:
            temp0 = t0
            temp1 = t1
            t0 = t1
            t1 = t2
            t2 = t2+temp0+temp1   
            n-=1
        if n==0:
            return 0
        elif n==1:
            return 1
        return t2